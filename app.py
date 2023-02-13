from flask import Flask, request, render_template, redirect, url_for
import random

app = Flask(__name__)

outfits = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        outfit = request.form["outfit"]
        outfits.append(outfit)
        return redirect(url_for("index"))
    return render_template("index.html", outfits=outfits)

@app.route("/generate_outfit")
def generate_outfit():
    random_outfit = random.choice(outfits)
    outfits.remove(random_outfit)
    return "Today's outfit: " + random_outfit

@app.route("/delete_outfit/<outfit>")
def delete_outfit(outfit):
    outfits.remove(outfit)
    return redirect(url_for("index"))
