from flask import Flask, render_template, request
import boto3
from datetime import datetime
import os

app = Flask(__name__)

# AWS S3 configuration
s3 = boto3.client('s3',
    aws_access_key_id="AKIARWPFIYHPKRD3ZI5B",
    aws_secret_access_key="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",
    region_name="us-east-1"
)

BUCKET_NAME = 'siva.frontend.test1'

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/decoder', methods=['GET', 'POST'])
def decoder():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        
        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
            
        # Add timestamp to filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
        s3_filename = timestamp + file.filename
        
        # Upload file to S3
        if BUCKET_NAME is None:
            return 'Error: S3 bucket name not configured', 500
            
        try:
            s3.upload_fileobj(file, BUCKET_NAME, s3_filename)
            return render_template('decoder.html', message=f'File uploaded successfully as {s3_filename}')
        except Exception as e:
            return f'Error uploading file: {str(e)}', 500
            
    return render_template('decoder.html')

@app.route('/knowledge-base')
def knowledge_base():
    return render_template('knowledge_base.html')

if __name__ == '__main__':
    app.run(debug=True)