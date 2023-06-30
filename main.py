from flask import Flask
from flask import Flask, render_template, request #, url_for, flash, redirect
from controler import Vci
import os
import time

app = Flask(__name__, static_folder='static')

vcInterface  =  Vci.Vci()

#Initialze the alphabet
vcInterface.initialiseItems("./controler/Itemset.json")
# Load the Openai/whisper_medium Transformer Model
vcInterface.loadTransformer()

def vciProcessAudio(filename):
  number = 0
  expresion = ""

  return {"representation":expresion, "result":number}

@app.route("/", methods=['POST', 'GET'])
def index():
  filePrefix = "recording_"+time.strftime("%Y%m%d-%H%M%S")
  file_name = os.path.join(app.config["UPLOAD_FOLDER"], filePrefix+".wav")
  f = open(file_name, 'wb')
  f.write(request.get_data("speech_data"))
  f.close()
  if os.path.isfile(file_name):
    #Vci Process the filename and render the result to page
    print(vcInterface.alphabetExpression["operators"].keys())
    dataVci = vciProcessAudio(file_name)
    
    return render_template('index.html', request="POST", value=dataVci)   
  else:
    return render_template("index.html")

if __name__ == "__main__":
  # Set the media folder to the current directory.
  app.config["UPLOAD_FOLDER"] =  os.path.join(os.getcwd(), "media")
  app.run(debug=True)