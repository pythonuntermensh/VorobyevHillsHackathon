from datetime import datetime
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from util import FileReader, Predictor
import pickle

app = Flask(__name__)
CORS(app)

model = None
predictor = None
file_reader = FileReader()

MODEL_FILE_NAME = "model.pk"

UPLOAD_FOLDER = 'archieve'

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

@app.route('/uploads', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({'error': 'netu nekogo'})

    files = request.files.getlist('files')
    texts_list = []
    file_names = []
    for file in files:
        if file.filename == '':
            return jsonify({'error': 'netu nekogo'})
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
        filename = f"{timestamp}___|___{file.filename}"

        file_names.append(os.path.join(UPLOAD_FOLDER, filename))

        file.save(os.path.join(UPLOAD_FOLDER, filename))
        texts_list.append(file_reader.convert_to_text(os.path.join(UPLOAD_FOLDER, filename)))

    predictions = predictor.predict(texts_list)

    results = {}
    for i in range(len(files)):
        results[files[i].filename] = predictions[i]
        os.rename(file_names[i], os.path.join(file_names[i].split("/")[0], predictions[i] + "___|___" + file_names[i].split("/")[1]))

    return jsonify({'message': results})


@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    
    result = []
    for file in files:
        class_name, timestamp, file_name = file.split("___|___")
        result.append({"name": file_name, "class": class_name, "timestamp": timestamp})

    return jsonify({'files': result})

@app.route('/files/download', methods=['GET'])
def download_file():
    path = os.path.join(BASE_DIR, UPLOAD_FOLDER, request.args.get("class") + "___|___" + request.args.get("timestamp") + "___|___" + request.args.get('name'))
    return send_file(path, as_attachment=True)


def load_model():
    print("Loading the model...")
    with open('./models/' + MODEL_FILE_NAME, 'rb') as f:
        model = pickle.load(f)
        print("The model has been loaded... doing predictions now...")
        return model


if __name__ == '__main__':

    model = load_model()
    predictor = Predictor(model)

    if not os.path.exists(os.path.join(BASE_DIR, UPLOAD_FOLDER)):
        os.mkdir(UPLOAD_FOLDER)

    app.run(host="0.0.0.0", debug=True, port=8000)

