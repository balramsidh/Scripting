#! python3
# Purpose of this script is to check for source csv files
# and if found, run the ssis package
# Created by : Balram Sidh

# importing required modules
import datetime
import glob
import sys
import time
import subprocess
import configparser
import logging
import os

# defining a few global variables
current_dir = os.getcwd()
script_name = os.path.splitext(os.path.basename(__file__))[0]
date = datetime.datetime.now().strftime("%Y%m%d")
log_file = current_dir + '/LOGS/' + script_name + '_' + date + '.log'

# Checking if the LOGS folder exists, creating it if not
if not os.path.exists(current_dir + '/LOGS/'):
    os.makedirs(current_dir + '/LOGS/')

# configuration of logs
logging.basicConfig(filename=log_file, level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info('#'*(31 + len(script_name)))
logging.info('########## START OF ' + script_name + ' ##########')
logging.info('#'*(31 + len(script_name)))

# function to check for input file and run the script if found.


def runscript(source_file_path, script):
    while True:
        input_file_name = glob.glob(source_file_path)
        if len(input_file_name) > 0:
            return(subprocess.run(script, capture_output=True))
            break
        else:
            logging.warning('file ' + source_file_path +
                            ' not found , checking again after a min')
            time.sleep(10)


# Check if config file provided in the script arguments
if len(sys.argv) > 1:
    config_file = sys.argv[1]
else:
    logging.critical("Config file not provided, exiting")
    logging.info('########## END OF ' + script_name + ' ##########' + '\n')
    sys.exit()


# Reading the parameters from config file provided in argument
config = configparser.ConfigParser()
config.read(config_file)

# running the scripts for each section in the config file
for section in config.sections():
    source_folder = config.get(section, "source_folder")
    source_file = config.get(section, 'source_file')
    script = [config.get(section, "script")]
    script_args = config.get(section, "script_args")

    # creating a list with script and arguments
    for arg in filter(None, script_args.split(',')):
        script.append(arg)

    # full path of the input file
    file_full_path = source_folder + '/' + date + '/' + source_file

    # calling runscript function defined on the top
    status = runscript(file_full_path, script)

    # printing result to the log
    logging.info('Section: ' + section)
    for line in status.stdout.decode('utf-8').split('\n'):
        if 'Error:' in line:
            logging.error(line)
        else:
            logging.debug(line)
    if status.returncode > 0:
        logging.critical('Failed to run section: ' +
                         section + ', exiting the script')
        break

logging.info('########## END OF ' + script_name + ' ##########' + '\n')
