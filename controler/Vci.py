import json
import re
import transformers
from transformers import pipeline


class Vci():
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

    def numberExtraction(self, expresssion):
        # Split the text into words.
        words = expresssion.split()
        status = 0

        numberValue = 0
        for word in words:
            val = 0
            if word in self.alphabetExpression["unit"].keys():
                val = int(self.alphabetExpression["unit"][word])

            elif word in self.alphabetExpression["tense"].keys():
                val = int(self.alphabetExpression["tense"][word])

            elif word in self.alphabetExpression["others"].keys():
                val = numberValue*int(self.alphabetExpression["unit"][word])
            else:
                val = None
                
            numberValue += val

        return numberValue

    def voiceToText(self, audio):
        text = self.transformerModel(audio)
        return text["text"]
    
    def textToExpression(self, textExpression):
        """ Reads a text  expression from transformer output and 
           returns its arithmetic expression and the status of current operation.
        """

        arithmetic_expression = ""
        # Split the text into words.
        words = textExpression.split()
        status = 0

        # Find the operators in the text representation of math expression.
        index_operators = [i for i in range(len(words)) if words[i] in self.alphabetExpression["operators"].keys()]

        if len(index_operators) == 0:
            # Execption Level 1
            status = 1
            print("No operation symbol found from the Voice")
            return ["", 1]
        
        # Find number 
        pos = 0
        for i in range(len(index_operators)):
            subtextToNumber = words[pos:i] 
            # Find the words that represent the numbers.
            val = self.numberExtraction(subtextToNumber)
            if val == None:
                # Execption Level 2
                status = 2
                print("No number symbol found from the Voice")
                return ["", 2]    
            arithmetic_expression= arithmetic_expression + str(val)+" "+words[index_operators[i]]  
            pos = i         

        # Return the arithmetic expression
        return [arithmetic_expression, 3]
    

        

        
 