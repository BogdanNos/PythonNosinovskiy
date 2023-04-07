from flask import Flask, request

app = Flask(__name__)

@app.route("/save_log", methods=["POST"])
def log_collector():
    form_data = request.form.to_dict()
    with open("./main.log", "a+") as logger:
        log = f"{form_data['levelname']} | {form_data['name']} | {form_data['asctime']} | {form_data['lineno']} | {form_data['msg']}\n"
        logger.write(log)
    return ''

@app.route("/get_loq", methods=["GET"])
def get_log() -> str:
    with open("./main.log", "r") as log:
        return log.read()

if __name__ == '__main__':
    app.run(debug=True)