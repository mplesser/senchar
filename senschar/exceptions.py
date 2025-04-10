"""
Contains custom exceptions and warnings used throughout senschar.
"""

import senschar

import warnings

warnings.filterwarnings("ignore")


def warning(message: str) -> None:
    """
    Print and log a warning message.
    """

    # warnings.warn(message)
    # print(f"Warning: {message}")

    try:
        senschar.logger.warning(message)
    except Exception:
        print(f"Warning: {message}")

    return


class SenscharError(Exception):
    """
    Base custom error class for azsenscharam.
    """

    def __init__(self, message: str, error_code: int = 0):
        """
        Custom error exception for senschar.

        Usage:  raise senschar.exceptions.SenscharError(message)

        Args:
          message: string message to display when error is raised
          error_code: flag for code, from list below
          - 0 - no error
        """

        super().__init__(message)

        self.error_code = 0

        # Now for your custom code...
        if error_code is not None:
            self.error_code = error_code
            # Original error was self.errors.message

        if senschar.logger is not None:
            senschar.logger.error(message)
        else:
            print(f"SenscharError: {message}")
