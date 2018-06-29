import sys
import datetime as dt
import time
from ftplib import FTP
import subprocess
import glob
import os

def logToFile (text):
    with open("NWIO.log", 'a') as logfile:
        logfile.write("%s\n"%text)
        return "%s"%text;
    
def printDT():
    dtt = dt.datetime.now()
    dtt = "%04i-%02i-%02i_%02i-%02i-%02i" % (dtt.year,dtt.month,dtt.day,dtt.hour,dtt.minute,dtt.second)
    return dtt;

class DownloadGrib:
    def __init__(self, file_dates): # hours_hindcast = 18; hours_forecast = 180 

        logToFile("\n\n=== DONWLOAD NETCDF ===") # log to file
        

        # === DOWNLOAD ===
        logToFile("%s: Starting download" % printDT()) # log to file

        readDates = open(file_dates, 'r').readlines()
        print readDates

        for dates in readDates:
            r = 1
            while r != -1:
                try:
                    print "Y"
                    '''
                    ftp = FTP('polar.ncep.noaa.gov')
                    print "Connected | Downloading files"
                      
                    ftp.login() # user anon, passw anon
                    '''
                    ftpfolder = 'pub/history/nopp-phase2/%s/partitions/' % dates.split()[0]
                    filename = "multi_reanal.partition.nwio_10m.%s.nc" % dates.split()[0]
                    #filename = "multi_reanal.partition.aoc_15m.%s.nc" % dates.split()[0]

                    print logToFile("%s%s" %(ftpfolder, filename))

                    '''
                    ftp.cwd(ftpfolder) #change dir
                    
                    ftp.retrbinary('RETR %s' % filename, open('NWIO\%s' % filename, 'wb').write)
                    print logToFile("File downloaded : NWIO\%s" % filename)
                    '''
                    r = -1

                except:
                    print logToFile("Connection error, retrying...(%i)" % r)
                    time.sleep(5)
                    r += 1
            


DownloadGrib("dates.inp")