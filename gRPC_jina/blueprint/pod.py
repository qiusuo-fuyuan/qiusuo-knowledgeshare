import os, sys, time

PACKAGE_PARENT = ".."
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
)
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from HeadPea import Headpeas
from BodyPea import BodyPea
from multiprocessing import Event, Process
from threading import Thread
from PeaMeta import PeaType, _get_event


class PodManager:
    def __init__(self, num_peas):
        self.num_peas = num_peas

    def run(self, num_peas):
        with Headpeas(Process) as hdp:
            print("headpea is started")
            Event = _get_event(hdp)
            Event.set()
        if Event.isSet():
            for i in range(self.num_peas):
                pea = BodyPea(Process)
                pea.start()


if __name__ == "__main__":
    # pea = BodyPea(Thread)
    num_peas = 3
    pm = PodManager(num_peas)
    pm.run(num_peas)
    print("bodypea is running")
    while 1:
        time.sleep(10)
