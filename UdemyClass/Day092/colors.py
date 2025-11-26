# testing Copilot generation

import numpy as np
from PIL import Image
from collections import Counter
from flask import Flask, request, render_template
import os


def extract_top_colors(image_path, top_n=10):
    img = Image.open(image_path).convert("RGB")
    arr = np.array(img)
    pixels = arr.reshape(-1, 3)  # flatten to list of RGB
    counts = Counter(map(tuple, pixels))
    most_common = counts.most_common(top_n)
    return [{"color": rgb, "count": count} for rgb, count in most_common]


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            colors = extract_top_colors(path)
            return render_template("result.html", colors=colors)
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
