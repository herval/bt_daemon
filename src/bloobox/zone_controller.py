from lightblue import *
#from multiprocessing import Process
import logging
import datetime
import time
from threading import Thread

class Probe:
    def __init__(self):
        LOG_FILENAME = 'sms_daemon.log'
        logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
        pass
#        p = Process(target=self.start)
#        p.start()
#        p.join()

    def run(self):
        while True:

            init = False
            try:
                print "Starting probe, local addr: %s" % gethostaddr()
                init = True
            except BluetoothError, e: # TODO as
                print e

            if init:
                print "Finding devices..."
                devices = finddevices()
                for dev in devices:
                    logging.info("Dispositivo: " + dev[0] + " -- Nome: " + dev[1] + " -- Data: "+ datetime.datetime.now().strftime("%H:%M - %Y-%m-%d"))
                time.sleep(30)

        else:
            print "BT not loaded"

    def detect_services(addr):
        print "Services for %s:" % addr
        print findservices(dev[0])


'''
Created on Oct 10, 2009

@author: hervalfreire
'''
class ZoneController:

    def __init__(self):
        self.probe = Probe()
        thread = Thread(target=self.probe.run)
        thread.start()


        print ":-)"


if __name__ == '__main__':
    control = ZoneController()
    # file = open(__file__)
    # for line in file.readlines():
    #     print line

