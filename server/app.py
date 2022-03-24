from flask import Flask, render_template, jsonify, request
import requests
import os

static_dir = str(os.path.abspath(os.path.join(__file__, "..", "frontend")))
app = Flask(__name__, static_folder=static_dir, static_url_path="", template_folder=static_dir)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/api/autocomplete', methods=['GET'])
def autocomplete():
    """Seqwa Autocomplete API"""
    response = requests.get('https://www.seqwa.com/api/v1/autocomplete', params={
        "index": 'cde1d8e5-f0af-4498-801d-3ff82acec9c6', # Replace with your Index Id
        "query": request.args.get('query'),
        "highlightField": 'title', # Include the field that needs to be highlighted for the suggestions. It is optional. By not setting this field you may end up with results from any field.
        "fields": 'title,price,image,link',
        "maxResults": 25,
    }, headers={'Content-Type': 'application/json', 'seqwa-api-key': 'ca3a6ba08d244a50ee43774b4e367c8876c214c4'})

    return jsonify(response.json())


if __name__ == '__main__':
    app.run()
