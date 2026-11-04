import time
import subprocess
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout
from PyQt6.QtCore import QThread, pyqtSignal
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("тест потоков")
        self.resize(200,100)

        main_Layout = QVBoxLayout()
        self.card = SiteCard("yandex.ru")
        main_Layout.addWidget(self.card)
        self.setLayout(main_Layout)

        self.worker = PingWorker()
        self.worker.result_signal.connect(self.receive_ping)
        self.worker.start()

    def receive_ping(self,host,ping_value):
        print(f"окно поймало пинг для{host}:{ping_value}")
        if ping_value>0:
            self.card.site_ping(True,ping_value)
            self.setStyleSheet("""
                SiteCard {
                    background-color: #99ff99; 
                    order: 6px solid #000000; 
                    border-radius: 8px;
                }
            """)
        else:
            self.card.site_ping(False,0)
            self.setStyleSheet("""
                SiteCard {
                background-color: #993300; 
                border: 6px solid #000000; 
                border-radius: 8px;
                }
            """)

class PingWorker(QThread):

    result_signal=pyqtSignal(str,int)

    def run(self):
        host = "yandex.ru"

        try:
            response = subprocess.run(
                ["ping", "-n", "1", host],
                capture_output=True,
                text=True,
                encoding="utf-8"
            )

            if response.returncode == 0 and "время=" in response.stdout:
                text_after_time = response.stdout.split("время=")[1]
                ping_str = text_after_time.split("мс")[0]
                ping_int = int(ping_str.strip())
                self.result_signal.emit(host, ping_int)
            else:
                self.result_signal.emit(host, 0)

        except Exception as e:
            print(f"ошибка внутри потока при проверке сайта{host}:{e}")
            self.result_signal.emit(host, 0)


