from flask import (
    Flask,
    render_template,
    flash,
    request,
    redirect,
    url_for,
    send_from_directory,
)
from werkzeug.utils import secure_filename
import os


# UPLOAD_FOLDER has to be an absolute path
basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)
upload_path = os.path.join(basedir, "files")
# print(upvoad_path)
UPLOAD_FOLDER = upload_path
ALLOWED_EXTENSIONS = set(["csv", "jpg"])


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    name = "Jose"
    letters = list(name)
    pup_dict = {"pup_name": "Sammy"}
    puppies = ["Fluffy", "Rufus", "Spike"]
    user_logged_in = True
    return render_template(
        "basic.html",
        name=name,
        letters=letters,
        pup_dict=pup_dict,
        puppies=puppies,
        user_logged_in=user_logged_in,
    )


@app.route("/information")
def info():
    return "<h1>Puppies are cute!</h1>"


@app.route("/puppy/<name>")
def puppy(name):
    return f"<h1>100th letter:  {name}</h1>"


@app.route("/puppylatin/<name>")
def puppylatin(name):
    if name[-1] == "y":
        output = name[:-1] + "iful"
    else:
        output = name + "y"
    return f"<h1>Hello, {output}!!!"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/file", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            print("filename:", filename)
            return redirect(url_for("uploaded_file", filename=filename))
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    """


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
   app.run(host='0.0.0.0')

