import logging
from time import time

logging.captureWarnings(True)
logging.basicConfig(format='%(asctime)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

def spd_pgs_progress_update(last_update_time=None, current_sample=None, total_samples=None, type_string=None):
    """

    """

    if current_sample is None or total_samples is None:
        logging.error('Error, both current sample and total # of samples must be specified.')
        return

    if last_update_time is None:
        return time()

    if type_string is None:
        type_string = 'Data'

    if time()-last_update_time > 10:
        logging.info(type_string + ' is ' + str(round(100.0*current_sample/total_samples)) + '% done.')
        last_update_time = time()

    return last_update_time