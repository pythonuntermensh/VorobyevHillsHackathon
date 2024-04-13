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

UPLOAD_FOLDER = 'archieve'
UPLOAD_MODEL_FOLDER = 'models'

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
        if len(file.split("___|___")) < 3: continue
        class_name, timestamp, file_name = file.split("___|___")
        result.append({"name": file_name, "class": class_name, "timestamp": timestamp})

    return jsonify({'files': result})

@app.route('/files/download', methods=['GET'])
def download_file():
    path = os.path.join(BASE_DIR, UPLOAD_FOLDER, request.args.get("class") + "___|___" + request.args.get("timestamp") + "___|___" + request.args.get('name'))
    return send_file(path, as_attachment=True)


def load_model(file_name):
    print("Loading the model...")
    with open('./models/' + file_name, 'rb') as f:
        model = pickle.load(f)
        print("The model has been loaded... doing predictions now...")
        return model


@app.route('/uploadmodel', methods=['POST'])
def upload_model():
    if 'model' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    model_file = request.files['model']
    if model_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if model_file:
        filename = model_file.filename
        if filename.endswith('.pk'):
            file_path = os.path.join(UPLOAD_MODEL_FOLDER, filename)
            clear_folder()
            model_file.save(file_path)

            global model
            global predictor
            model = load_model(filename)
            predictor = Predictor(model)

            return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 200
        else:
            return jsonify({'error': 'File format not supported. Please upload a .pk file'}), 400


def clear_folder():
    folder_path = UPLOAD_MODEL_FOLDER
    if os.path.exists(folder_path):
        files = os.listdir(folder_path)
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Ошибка при удалении файла {file_path}: {e}")


if __name__ == '__main__':
    files = os.listdir(os.path.join(BASE_DIR, UPLOAD_MODEL_FOLDER))
    model = load_model(files[0])
    predictor = Predictor(model)

    if not os.path.exists(os.path.join(BASE_DIR, UPLOAD_FOLDER)):
        os.mkdir(UPLOAD_FOLDER)

    app.run(host="0.0.0.0", debug=True, port=8000)

