import subprocess


class Process:
    def __init__(self, filename=""):
        self._filename = filename
        self.process = None

    def run(self):
        if self.process:
            self.stop()
        self.process = subprocess.Popen(['python', self._filename])

    def stop(self):
        if self.process:
            self.process.terminate()


if __name__ == "__main__":
    main_process = Process()
    while True:
        command = input()
        if command == "run":
            main_process.stop()
            main_process = Process("./main.py")
            main_process.run()
        elif command == "setup":
            main_process.stop()
            main_process = Process("setup_screen.py")
            main_process.run()
