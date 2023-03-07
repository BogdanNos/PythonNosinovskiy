import os
import shlex
import subprocess
import signal
from flask import Flask
app = Flask(__name__)


def try_open_port(port: int):
    command_str = f'lsof -i :{port}'
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    resultList = result.stdout.decode().split('\n')[1:-1]
    pidList = []
    for item in resultList:
        pidList.append(int(item.split()[1]))

    if not os.getpid() in pidList:
        for pid in pidList:
            os.kill(pid, signal.SIGKILL)
    app.run(debug=True, port=port)

if __name__ == "__main__":
    try_open_port(5000)