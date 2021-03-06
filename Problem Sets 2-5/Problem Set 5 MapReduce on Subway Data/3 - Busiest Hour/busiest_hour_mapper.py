import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    """
    The input to this mapper will be the final Subway-MTA dataset, the same as
    in the previous exercise.  You can check out the csv and its structure below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    For each line, this mapper should return the following: The UNIT, the
    ENTRIESn_hourly, and the DATEn and TIMEn columns, separated by tabs.  Example:
    R001    100000.0    2011-05-01  01:00:00
    Since you are printing the actual output of your program, you
    can't print a debug statement without breaking the grader.
    Instead, you should use the logging module, which we've configured
    to log to a file which will be printed when you hit "Test Run".
    For example:
    logging.info("My debugging message")
    """
    sys.stdin.readline()
    cc = 0
    for line in sys.stdin:
        data = line.strip().split(",")
        thisunit = data[1]
        entries = data[6]
        date = data[2]
        tm = data[3]
        val = "{0}\t{1}\t{2}\t{3}".format(thisunit,entries,  date, tm)
        print val
        #if cc < 5:
        #    logging.info( val)
        #    cc = cc + 1

mapper()