from flask import Flask, jsonify, request
#from yolo import get_predictions

import folium

app = Flask(__name__)

@app.route("/")
def index():

    m = folium.Map(
        location=(-27.469913, 153.024547), 
        zoom_start=10,
        tiles='Stamen Toner'
    )

    tooltip_1 = '<b>Yan\'s Home</b>'
    tooltip_2 = '<b>Chao\'s Home</b>'

    html_1 = """
        <h3> html popup</h3><br>
        With a few lines of info...
        <p>
        <code>
            Built: 1989 <br>
            Ranking: ***<br>
            Price: $89k
        </code>
        </p>
    """
    iframe_1 = folium.IFrame(html=html_1, width=200, height=200)
    html_popup_1 = folium.Popup(iframe_1, max_width=1650)

    html_2 = """
        <h3> html popup</h3><br>
        With a few lines of info...
        <p>
        <code>
            Built: 1992<br>
            Ranking: *****<br>
            Price: $100k
        </code>
        </p>
    """
    iframe_2 = folium.IFrame(html=html_2, width=200, height=200)
    html_popup_2 = folium.Popup(iframe_2, max_width=1650)

    folium.Marker(
        (-27.567667, 153.119333),
        popup=html_popup_1, 
        tooltip=tooltip_1,
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

    folium.Marker(
        (-27.604134, 153.132601), 
        popup=html_popup_2,
        tooltip=tooltip_2,
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

    return m._repr_html_()

# def landing():
#     return "Hey, you are hitting Yan's playround."

@app.route("/predict", methods=["POST"])
def predict():
    predictions = get_predictions(request)

    return jsonify(predictions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

