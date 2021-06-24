import os, sys, time

PACKAGE_PARENT = ".."
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
)
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import yaml
from blueprint.pods import PodManager

pm = yaml.load(
    open("yaml/pods.yml"),
    Loader=yaml.Loader,
)
pm.run()
while True:
    time.sleep(10)


# if __name__ == "__main__":
#     pm.run()
#     while 1:
#         time.sleep(10)