import psutil
import time
import os

#выводить самое загруженное ядро
#красить загруженные ядра
#вывод температуры


class SystemCollector:
    def __init__(self):
        self.cores=[]
        self.ram=0.0
    def update(self):
        self.cores=psutil.cpu_percent(interval=1, percpu=True)
        self.ram=psutil.virtual_memory().percent

class ProgressBar:
    def __init__(self, length=20):
        self.length = length
    def create_bar(self, percent,label=""):
        filled = int(self.length * percent/100)
        bar = "█"*filled + "░"*(self.length - filled)
        return f"[{bar}]{percent:5.1f}%{label}"

class DashBoard:
    def __init__(self):
        self.collector=SystemCollector()
        self.bar = ProgressBar(length=20)
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            self.collector.update()
            lines = []
            for i,percent in enumerate(self.collector.cores,start=1):
                 lines.append(self.bar.create_bar(percent,f": ядро {i}"))
            lines.append(self.bar.create_bar(self.collector.ram,": оперативная память"))
            print(f"\033[H\033[J"+ "\n" .join(lines))
            time.sleep(1)

if __name__ == "__main__":
    app = DashBoard()
    app.run()





