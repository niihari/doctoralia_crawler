import argparse
from pathlib import Path

def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

def run_config():
    parser = argparse.ArgumentParser(description="Crawl Doctoralia.com to extract predefined information.")
    number_of_doctors_group = parser.add_mutually_exclusive_group(required=True)
    number_of_doctors_group.add_argument("-n", "--number_doctors", dest="n_results", type=check_positive, default=1, help="Defines number of doctors to be returned.")
    number_of_doctors_group.add_argument("-a", "--all_results", default=False, dest="all_results", action="store_true", help="Returns all doctors.")
    parser.add_argument("-s", "--show-browser", action="store_true", default=False, dest="show_browser", help="Runs with visible browser.")
    parser.add_argument("-c", "--chrome-driver-path", dest="chrome_driver_path", default=str(Path.cwd().joinpath("chromedriver.exe")), help="Path to chromedriver. If not defined, default is set to current working directory.")
    return parser


args = run_config().parse_args()
