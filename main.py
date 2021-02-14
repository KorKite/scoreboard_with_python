from flask import Flask, url_for, flash ,redirect, render_template, request, abort
from scoring import scoring
import json

app = Flask(__name__)
app.secret_key = "dsfajkl23@!fesjkl#"
scr = scoring()

@app.route("/")
def index():
    rankings = scr.read_rank()
    return render_template("index.html", rankings = rankings)

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        s_id = (request.form["register_name"])
        f = request.files["csv_file"]
        user_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) 
        if f.headers["Content-Type"]=="text/csv":
            path = f"./reported/{s_id}.csv"
            f.save(path)
            message = scr.write(path, s_id, f.filename, user_ip)
            flash(message)
        else:
            flash("CSV파일이 아닙니다. CSV파일을 제출해주세요.")

    else:
        abort(404)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="0.0.0.0", threaded=True)