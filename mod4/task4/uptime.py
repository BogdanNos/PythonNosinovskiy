from datetime import timedelta

from flask import Flask

app = Flask(__name__)

@app.route("/uptime")
def uptime():
    with open('/proc/uptime', 'r') as f:
        seconds = float(f.readline().split(maxsplit=1)[0])
    UPTIME = str(timedelta(seconds=seconds)).split('.')[0]
    return f"Current uptime is {UPTIME}"


if __name__ == "__main__":
    app.run(debug=True)