from datetime import datetime
from flask import Flask, request, jsonify
import os
from util import FileReader, Predictor
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

model = None
predictor = None
file_reader = FileReader()

MODEL_FILE_NAME = "model.pk"

UPLOAD_FOLDER = 'archieve'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}___|___{file.filename}"

        file_names.append(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        texts_list.append(file_reader.convert_to_text(os.path.join(app.config['UPLOAD_FOLDER'], filename)))

    predictions = predictor.predict(texts_list)

    results = {}
    for i in range(len(files)):
        results[files[i].filename] = predictions[i]
        os.rename(file_names[i], file_names[i].split("/")[0] + "/" + predictions[i] + "___|___" + file_names[i].split("/")[1])

    return jsonify({'message': results})


@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    
    result = []
    for file in files:
        class_name, timestamp, file_name = file.split("___|___")
        result.append({"name": file_name, "class": class_name, "timestamp": timestamp})

    return jsonify({'files': result})


def load_model():
    print("Loading the model...")
    with open('./models/' + MODEL_FILE_NAME, 'rb') as f:
        model = pickle.load(f)
        print("The model has been loaded... doing predictions now...")
        return model


if __name__ == '__main__':
    model = load_model()
    predictor = Predictor(model)
    app.run(debug=True, port=8000)

