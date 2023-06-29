from flask import Flask
from flask import Flask, render_template #, request, url_for, flash, redirect
import gradio as gr
from controler import Vci
import os

app = Flask(__name__)

def record_audio(duration):
  # Create a temporary file to store the audio recording.
  file_name = os.path.join(app.config["UPLOAD_FOLDER"], "recording.wav")

  # Start recording audio.
  with open(file_name, "wb") as f:
    f.write(gr.audio(duration))

  # Return the path to the audio file.
  return file_name

@app.route("/")
def index():
  demo = gr.Interface(fn=record_audio, inputs="number", outputs="file")
  return demo.launch()

if __name__ == "__main__":
  # Set the media folder to the current directory.
  app.config["UPLOAD_FOLDER"] =  os.path.join(os.getcwd(), "media")
  app.run(debug=True)