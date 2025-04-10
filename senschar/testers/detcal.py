import os
import shutil
import time

import numpy

import senschar
import senschar.utils
import senschar.fits
import senschar_console.console
from senschar_console.testers.basetester import Tester


class DetCal(Tester):
    """
    Detector calibration routines to:
     - find and set video offsets
     - find exposure levels in DN and electrons at specified wavelengths
     - find system gains
     - read diode flux calibration data

    Fluxes are reported as per unbinned pixel even if taken binned.
    """

    def __init__(self):
        super().__init__("detcal")

        self.mean_count_goal = 5000
        self.zero_image = "test.fits"
        self.data_file = "detcal.txt"

        self.exposure_type = "flat"
        self.overwrite = 0  # True to overwrite old data
        self.wavelength_delay = 2  # seconds to delay after changing wavelengths
        self.zero_mean = []
        self.system_gain = []

        self.range_factor = 2.0  # allowed range factor for meeting mean goal

        self.exposures = {}  # dictionaries of {wavelength:initial guess et}
        self.mean_counts = {}  # dictionaries of {wavelength:Counts/Sec}
        self.mean_electrons = {}  # dictionaries of {wavelength:Electrons/Sec}

    def calibrate(self):
        """
        Take images at each wavelength to get count levels.
        Use gain data to find offsets and gain.
        If no wavelengths are specified, only calibrate current wavelength
        """

        senschar.log("Running detector calibration sequence")

        # save pars to be changed
        impars = {}
        senschar.util.save_imagepars(impars)

        # create new subfolder
        if self.overwrite:
            if os.path.exists("detcal"):
                shutil.rmtree("detcal")
        startingfolder, subfolder = senschar_console.utils.make_file_folder("detcal")
        senschar.db.parameters.set_par("imagefolder", subfolder)
        senschar.util.curdir(subfolder)

        senschar.db.parameters.set_par(
            "imageincludesequencenumber", 1
        )  # don't use sequence numbers
        senschar.db.parameters.set_par("imageautoname", 0)  # manually set name
        senschar.db.parameters.set_par("imagetest", 0)  # turn off TestImage
        senschar.db.parameters.set_par("imageoverwrite", 1)

        # get gain and ROI
        self.system_gain = senschar.db.tools["gain"].get_system_gain()
        self.roi = senschar_console.utils.get_image_roi()

        self.system_gain = senschar.db.tools["gain"].system_gain
        self.zero_mean = senschar.db.tools["gain"].zero_mean

        # clear device
        senschar.db.tools["exposure"].test(0)
        bin1 = int(senschar.fits.get_keyword("test", "CCDBIN1"))
        bin2 = int(senschar.fits.get_keyword("test", "CCDBIN2"))
        binning = bin1 * bin2

        self.mean_counts = {}
        self.mean_electrons = {}

        wavelengths = sorted(self.exposures.keys())

        # not used, for reference
        # detcal.mean_electrons = {int(k): v for k, v in detcal.mean_electrons.items()}
        # detcal.mean_counts = {int(k): v for k, v in detcal.mean_counts.items()}

        # get flat at each wavelength
        for wave in wavelengths:
            # set wavelength
            wave = int(wave)
            wave1 = int(senschar.db.tools["instrument"].get_wavelength())
            if wave1 != wave:
                senschar.log(f"Setting wavelength to {wave} nm")
                senschar.db.tools["instrument"].set_wavelength(wave)

            # take flat
            doloop = 1
            try:
                # et = self.exposures[wave] / binning
                et = self.exposures[wave]
            except Exception:
                et = 1.0
            while doloop:
                senschar.db.parameters.set_par("imagetype", self.exposure_type)
                senschar.log(f"Taking flat for {et:0.3f} seconds")
                flatfilename = senschar.db.tools["exposure"].get_filename()
                senschar.db.tools["exposure"].expose(
                    et, self.exposure_type, "detcal flat"
                )

                # get counts
                flatmean = numpy.array(senschar.fits.mean(flatfilename)) - numpy.array(
                    self.zero_mean
                )
                flatmean = flatmean.mean()
                senschar.log(f"Mean signal at {wave} nm is {flatmean:0.0f} DN")

                if flatmean > self.mean_count_goal * self.range_factor:
                    et = et * (self.mean_count_goal / flatmean)
                    senschar.log(f"--> Retest at {et:0.3f} seconds")
                    continue
                elif flatmean < self.mean_count_goal / self.range_factor:
                    et = et * (self.mean_count_goal / flatmean)
                    senschar.log(f"--> Retest at {et:0.3f} seconds")
                    continue

                self.mean_counts[wave] = flatmean / et / binning
                self.mean_electrons[wave] = self.mean_counts[wave] * numpy.array(
                    self.system_gain
                )

                self.mean_counts[wave] = self.mean_counts[wave].mean()
                self.mean_electrons[wave] = self.mean_electrons[wave].mean()
                doloop = 0

        # define dataset
        self.dataset = {
            "data_file": self.data_file,
            "wavelengths": wavelengths,
            "mean_electrons": self.mean_electrons,
            "mean_counts": self.mean_counts,
            "system_gain": self.system_gain,
        }

        # write data file
        senschar.util.curdir(startingfolder)
        self.write_datafile()

        self.is_valid = True

        # finish
        senschar.util.restore_imagepars(impars)
        senschar.util.curdir(startingfolder)
        senschar.log("detector calibration sequence finished")

        return

    def read_datafile(self, filename="default"):
        """
        Read data file and set object as valid.
        """

        super().read_datafile(filename)

        # convert types
        self.mean_counts = {int(k): v for k, v in self.mean_counts.items()}
        self.mean_electrons = {int(k): v for k, v in self.mean_electrons.items()}

        return
