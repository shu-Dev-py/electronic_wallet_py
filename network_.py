import subprocess
import time


class CheckNet:
    def __init__(self,site_list):
        self.site_list = site_list

    def ping_one_site(self,host):
        response = subprocess.run(["ping","-n","1",host],capture_output=True,text= True,encoding="cp866" )
        if response.returncode == 0:
            if"время=" in response.stdout:

                text_after_time = response.stdout.split("время=")[1]
                ping_str = text_after_time[1].split("мс")[0]
                ping_int = int(ping_str.strip())
                return True,ping_int
        return False,0


    def start_monitoring(self):
        while True:
            print("--запуск проверки сети--\n")

            for site in self.site_list:
                is_oline,ping_ms = self.ping_one_site(site)

                if is_oline == True:
                    print(f"{site} [oline] / {ping_ms} ms")
                else:
                    print(f" {site} [offline] / {ping_ms} ms ")
            time.sleep(3)
            print("\n")



check_list = ["google.com","youtube.com","vk.com","test_site.com" ]

checker = CheckNet(check_list)
checker.start_monitoring()

