from datetime import datetime
import socket
import subprocess
import time


class FurnaceData:

    def __init__(self, temperature: str, working_set_point: str):
        self.temperature = temperature
        self.working_set_point = working_set_point
        self.measured_at = datetime.now()

    def __str__(self):
        return f'Measuring time: {self.measured_at}\t' \
               f'T: {self.temperature}\t' \
               f'WSP: {self.working_set_point}'


class FurnaceIO:

    def __init__(self, ip: str, port: str):
        self.ip = ip
        self.port = port

    def check_ping(self) -> bool:
        try:
            response = subprocess.check_output(f'ping -n 1 {self.ip}',
                                               shell=True).decode("cp866")

            if "TTL" in response:
                print(f'resource {self.ip} is available,')
                return True
            else:
                print(f'resource {self.ip} + is unavailable')
                return False
        except subprocess.CalledProcessError as e:
            print(e.output)
            return False

    def scan_cell(self, cell_n: int):
        with socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM) as sock:
            sock.connect((self.ip, int(self.port)))
            str_2_send = "Get:" + str(cell_n)
            print('->', str_2_send)
            sock.sendall(str_2_send.encode())
            time.sleep(0.01)
            str_get = sock.recv(16)
            print('<-', str_get)
            sock.close()
        return str_get.decode()

    def get_current_data(self):
        if self.check_ping():
            return FurnaceData(temperature=self.scan_cell(cell_n=1),
                               working_set_point=self.scan_cell(cell_n=2))
        else:
            return 'The furnace is out of tracking.'
