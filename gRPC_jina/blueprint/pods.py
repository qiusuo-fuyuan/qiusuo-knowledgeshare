import os, sys, time

PACKAGE_PARENT = ".."
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
)
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from HeadPea import Headpeas
from BodyPea import BodyPea
import yaml


class PodManager(yaml.YAMLObject):
    yaml_tag = u"!PodManager"

    def __init__(self, num_peas):
        self.num_peas = num_peas

    def run(self):
        with Headpeas({"runtime_backend": "process"}) as hdp:
            if hdp.is_ready.wait():
                print("headpea is started")
                for i in range(self.num_peas):
                    pea = BodyPea({"runtime_backend": "process"})
                    pea.start()
            else:
                print("Headpea fail to start,can't start body pea")


if __name__ == "__main__":
    num_peas = 3
    pm = PodManager(num_peas)
    pm.run(num_peas)
    while 1:
        time.sleep(10)