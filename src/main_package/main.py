import logging
import sys

import main_package

import support_package.helper

log = logging.getLogger()


def entrypoint(some_arg: str = "foo"):
    log.debug(f"Entrypoint triggered with argument: '{some_arg}'")
    log.warning(f"Entrypoint for {main_package.__name__} not implemented!")
    # Call helper function
    return support_package.helper.foo("Baz")


if __name__ == "__main__":
    entrypoint(*sys.argv)
