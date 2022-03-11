import requests
import os, sys
import platform

class updater():
    def __init__(self, app_version: float) -> None:
        self.app_version = app_version
        url = "http://127.0.0.1:5000/calc_update/version"

        r = requests.get(url)
        self.server_ver = r.text

        self.os_sys = platform.system()

        # self.__run__()
        self.create_file()
        self.run_update_file()

    def __run__(self) -> None:
        if self.is_newer_version():
            self.get_update()


    def is_newer_version(self) -> bool:
        if self.server_ver > str(self.app_version):
            return True
        else:
            return False

    
    def get_update(self) -> None:
        url = "http://127.0.0.1:5000/calc_update"

        os.system(f"""wget '{url}'""")


    def create_file(self) -> None:
        if self.os_sys == 'Linux':
            with open('./linux', 'r') as lin_file:
                with  open("./updater.sh", 'w') as upd_file:
                    upd_file.write(lin_file.read())
            os.system("chmod +x updater.sh")
        elif platform.system() == "Windows":
            with open("./windows", 'r') as win_file:
                with  open("updater.bat", 'w') as upd_file:
                    upd_file.write(win_file.read())


    def run_update_file(self) -> None:
        if self.os_sys == "Linux":
            os.system("./updater.sh")
            sys.exit()


def debug() -> None:
    updater(0.001).create_file()
    updater(0.001).run_update_file()


if __name__=="__main__":
    debug()