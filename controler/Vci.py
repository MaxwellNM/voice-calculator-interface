import json
import re
import transformers
from transformers import pipeline


class Vci:
    def __init__(self) -> None:
        self.ops = {}
        self.atomExpression = None 
        self.transformerModel = None #Whisper


    def initialiseItems (self, filename):
        with open(filename) as user_file:
            self.alphabetExpression = json.load(user_file) #load Json File of canonic text expression

    def loadTransformer (self):
        self.transformerModel = pipeline("automatic-speech-recognition", model='openai/whisper-medium')

    def filterExpression(self, expresssion):
        pass

    def parseExpression(self, expresssion):
        pass

    def voice2Text(self, audio):
        text = self.transformerModel(audio)
        return text.text
    
    def text2Expression(self, textExpression):
        """Reads a text arithmetic expression and returns its arithmetic expression."""
        # Split the text into words.
        words = textExpression.split()
        
        # Find the words that represent the numbers.
        numbers = [word for word in words if word.isdigit()]

        # Find the words that represent the operators.
        operators = [word for word in words if word not in numbers]

        # Create the arithmetic expression.
        arithmetic_expression = " ".join([numbers[0]] + operators + numbers[1:])

        return arithmetic_expression
    

        

        
 