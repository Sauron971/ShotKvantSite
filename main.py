from flask import Flask, render_template, request, send_file

app = Flask(__name__)

def read_file():
    with open('data.txt', 'r') as f:
        count = f.read()
        return count
def write_file(string):
    with open('data.txt', 'w') as f:
        f.write(string)

@app.route('/', methods=["GET", "POST"])
def index():
    count = read_file()
    return render_template('index.html', count=count)

@app.route('/donation', methods=["GET", "POST"])
def donation():
    return render_template('donation.html')

@app.route('/download')
def download_file ():
    path = "D:\programms\openserver\domains\localhost\static\images\privet.png"
    count = read_file()
    count = int(count) + 1
    write_file(str(count))
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(host='192.168.1.34', port='80')
