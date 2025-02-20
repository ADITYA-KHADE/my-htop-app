import getpass
import subprocess
import datetime
import pytz
from flask import Flask

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "John Doe"  # Replace with your full name
    username = getpass.getuser()
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode(errors="ignore")
    return f"""
Name - {name}<br>
Username - {username}<br>
Server Time (IST) - {server_time}<br>
<pre>{top_output}</pre>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
