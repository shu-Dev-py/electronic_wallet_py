import sys
import time
import subprocess
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QFrame,QLabel,QGridLayout
from PyQt6.QtCore import Qt,QThread, pyqtSignal
class SiteCard(QFrame):
    def __init__(self,site_name):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.name_label = QLabel(site_name)
        self.ping_label = QLabel("ожидание задержки")

        card_layout = QVBoxLayout()

        card_layout.setSpacing(3)
        card_layout.setContentsMargins(10,10,10,10)
        card_layout.addWidget(self.name_label)
        card_layout.addWidget(self.ping_label)

        card_layout.addStretch()
        self.setLayout(card_layout)

        self.setStyleSheet("""
            SiteCard {
                background-color: #2d2d2d; 
                border: 2px solid #000000; 
                border-radius: 8px;
            }
        """)

        self.name_label.setStyleSheet("color: white; font-weight : bold;border: none; background: transparent;")
        self.ping_label.setStyleSheet("color: #666666;border: none; background: transparent;")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ping_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(130,70)

    def site_ping(self,is_online,ping_ms):
        if is_online:
            self.ping_label.setText(f"{ping_ms} мс")

            self.setStyleSheet("""
                   SiteCard {
                       background-color: #99ff99; 
                       border: 6px solid #000000; 
                       border-radius: 8px;
                   }
               """)
        else:
            self.ping_label.setText(f"{ping_ms} мс")

            self.setStyleSheet("""
              SiteCard {
                    background-color: #993300; 
                    border: 6px solid #000000; 
                    border-radius: 8px;
                }
            """)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

class PingWorker(QThread):

    result_signal=pyqtSignal(str,int)

    def __init__(self,hosts_list):
        super().__init__()
        self.hosts = hosts_list

    def run(self):
        while True:
            for host in self.hosts:
                try:
                    response = subprocess.run(
                        ["ping", "-n", "1", host],
                        capture_output=True,
                    )
                    try:
                        stdout_text = response.stdout.decode("cp866", errors= "ignore")
                    except:
                        stdout_text = response.stdout.decode("utf-8", errors="ignore")

                    if response.returncode == 0 and "время=" in stdout_text:
                        text_after_time = stdout_text.split("время=")[1]
                        ping_str = text_after_time.split("мс")[0]
                        ping_init =int(ping_str.strip())
                        self.result_signal.emit(host,ping_init)
                    else:
                        self.result_signal.emit(host,0)
                except Exception as e:
                    print(f"ошибка внутри потока при проверке сайта{host}: {e}")
                    self.result_signal.emit(host,0)
            time.sleep(6)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("тест потоков")
        self.resize(400,100)
        self.hosts =["test.com","ue.bot", "vk.com", "yandex.ru", "error_test.com", "googl.com"]

        main_Layout = QGridLayout()

        self.cards = {}
        for index,host in enumerate(self.hosts):
            card = SiteCard(host)
            self.cards[host] = card
            main_Layout.addWidget(card, 0 ,index)
        self.setLayout(main_Layout)
        self.worker = PingWorker(self.hosts)
        self.worker.result_signal.connect(self.update_card_status)
        self.worker.start()
    def update_card_status(self,host,ping_init):
        card = self.cards[host]
        if ping_init>0:
            card.site_ping(True,ping_init)
        else:
            card.site_ping(False, 0)
    def close_event(self,event):
        self.worker.terminate()
        self.worker.wait()
        event.accept()
app = QApplication(sys.argv)
window = App()
window.show()
app.exec()

