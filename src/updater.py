import requests
import os, sys
import platform
import subprocess
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="log.log", level=logging.INFO, format = LOG_FORMAT)
logger = logging.getLogger()

class updater():
    def __init__(self, app_version: float) -> None:
        self.app_version = app_version
        url = "http://127.0.0.1:5000/calc_update/version"

        r = requests.get(url)
        self.server_ver = r.text

        self.os_sys = platform.system()

        self.__run__()


    def __run__(self) -> None:
        if self.is_newer_version():
            self.get_update()
            self.unpack_update()
            self.create_file()
            self.run_update_file()


    def is_newer_version(self) -> bool:
        if self.server_ver > str(self.app_version):
            logger.info("Server Version is Newer")
            return True
        else:
            logger.info("Server Version is not newer")
            return False

    
    def get_update(self) -> None:
        try:
            logger.info("Getting new update")
            url = "http://127.0.0.1:5000/calc_update"

            os.system(f"""wget -O ./patch.zip '{url}'""")
        except Exception as e:
            print(e)
            logger.info(e)


    def unpack_update(self) -> None:
        logger.info("Unpacking new patch")
        os.system("unzip ./patch.zip")


    def create_file(self) -> None:
        if self.os_sys == 'Linux':
            logger.info("Creating Linux batch file")
            with open('./linux', 'r') as lin_file:
                with  open("./updater.sh", 'w') as upd_file:
                    upd_file.write(lin_file.read())
            os.system("chmod +x updater.sh")
        elif platform.system() == "Windows":
            logger.info("Creating Windows batch file")
            with open("./windows", 'r') as win_file:
                with  open("updater.bat", 'w') as upd_file:
                    upd_file.write(win_file.read())


    def run_update_file(self) -> None:
        if self.os_sys == "Linux":
            logger.info("Running updater for Linux")
            subprocess.Popen("./updater.sh",  shell=True)
            sys.exit()
        elif self.os_sys == "Windows":
            # subprocess.Popen([sys.executable, "./updater.sh"], creationflags=subprocess.CREATE_NEW_CONSOLE)
            # os.system("./updater.sh")
            # sys.exit()
            pass


def debug() -> None:
    updater(0.001)

if __name__=="__main__":
    debug()