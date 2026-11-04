import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFrame,QGridLayout,QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QTimer

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
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Адаптивное окно")
        self.resize(400, 100)


        self.hosts = ["test.com", "vk.com", "yandex.ru", "error_test.com", "googl.com"]

        main_layout = QGridLayout()
        self.cards = {}

        for index, host in enumerate(self.hosts):
            card = SiteCard(host)
            self.cards[host] = card
            main_layout.addWidget(card,0,index)



        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status)
        self.setLayout(main_layout)
        self.timer.start(10000)

        self.update_status()

    def update_status(self):
        for host in self.hosts:
            try:
                response = subprocess.run(
                    ["ping", "-n", "1", host],
                    capture_output=True,
                    text=True,
                    encoding="cp866"
                )

                if response.returncode == 0 and "время=" in response.stdout:
                    # Режем аккуратно и безопасно
                    text_after_time = response.stdout.split("время=")[1]
                    ping_str = text_after_time.split("мс")[0]
                    ping_int = int(ping_str.strip())

                    self.cards[host].site_ping(True, ping_int)
                else:
                    self.cards[host].site_ping(False, 0)

            except Exception as e:
                print(f"Ошибка при проверке {host}: {e}")
                self.cards[host].site_ping(False, 0)

app = QApplication(sys.argv)
window =App()
window.show()
app.exec()
