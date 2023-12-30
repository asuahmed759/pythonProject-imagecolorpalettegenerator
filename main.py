import os
from flask import Flask, render_template, request
from colorthief import ColorThief
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' in request.files:
        image = request.files['image']
        ct = ColorThief(image)

        # Get the top 10 most common colors
        palette = ct.get_palette(color_count=10)

        # Plotting the colors
        plt.imshow([palette])
        plt.show()

        return "Analysis completed."
    else:
        return "No image uploaded."

if __name__ == '__main__':
    app.run(debug=True)
