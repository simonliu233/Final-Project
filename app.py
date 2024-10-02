from flask import Flask, render_template, request, redirect, url_for
import face_recognition
import cv2
import os

app = Flask(__name__)

# Ensure uploads directory exists
os.makedirs('static/uploads', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    # Save the uploaded file
    file_path = os.path.join('static/uploads', file.filename)
    file.save(file_path)

    # Load the image and perform face recognition
    image = face_recognition.load_image_file(file_path)
    face_locations = face_recognition.face_locations(image)

    # Count detected faces
    num_faces = len(face_locations)

    return render_template('index.html', num_faces=num_faces, file_url=file_path)

if __name__ == '__main__':
    app.run(debug=True)