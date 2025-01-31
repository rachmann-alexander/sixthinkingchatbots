""" Six Thinking Chatbots, see https://github.com/rachmann-alexander/sixthinkingchatbots"""

from datetime import datetime
from abc import ABC
import time
import logging
from openai import OpenAI
from transformers import pipeline
from huggingface_hub import login
import requests

from promptstrings import *
from llmhandler import *
from outputhandler import *


""" Domain class of this prototype """
class SixThinkingChatbots():
    problem_statement = ''    
    white_system_content = PS_WHITE_SYSTEM_CONTENT
    white_prompt = ''
    white_response = ''

    green_system_content = PS_GREEN_SYSTEM_CONTENT
    green_prompt = ''
    green_response = ''

    yellow_system_content = PS_YELLOW_SYSTEM_CONTENT
    yellow_prompt = ''
    yellow_response = ''

    black_system_content = PS_BLACK_SYSTEM_CONTENT
    black_prompt = ''
    black_response = ''

    red_system_content = PS_RED_SYSTEM_CONTENT
    red_prompt = ''
    red_response = ''

    blue_system_content = PS_BLUE_SYSTEM_CONTENT
    blue_prompt = ''
    blue_response = ''

    result = ''
    

    def __init__(self, problem_statement, mode="alternativesCascading", model="Mistral", outputhandler="md"):

        self.mode = mode

        self.problem_statement = problem_statement

        self.outputhandler = ''

        match outputhandler:
            case "md":
                self.outputhandler = MarkdownHandler()
            case "html":
                self.outputhandler = HtmlHandler()
            case _:
                self.outputhandler = MarkdownHandler()

        match model:
            case "Mistral":
                self.llm = MistralHandler()
            case "gpt4o":    
                self.llm = Gpt4oHandler()
            case _:
                self.llm = MistralHandler()


        match self.mode:
            case "idea":
                self.renderIdea()
                
            case "alternatives":
                self.renderAlternatives()
                
            case "alternativesCascading":
                self.renderAlternativesCasc()

            case "solutions":
                self.renderSolutions()

            case "feedback":
                self.renderFeedback()

            case "planning":
                self.renderPlanning()

            case "processimprovement":
                self.renderProcessImprovement()

            case "solvingproblems":
                self.renderSolvingProblems()

            case "review":
                self.renderReview()

            case _:
                print("Specify mode.")


    def renderFeedback(self):   
        return True
    
    def renderPlanning(self):   
        return True

    def renderProcessImprovement(self):   
        return True
    
    def renderSolvingProblems(self):   
        return True

    def renderReview(self):   
        return True

    def renderSolutions(self):        
        self.white_prompt = self.problem_statement + PS_GENERIC_TASK
        self.white_response = self.llm.call(self.white_system_content, self.white_prompt)

        self.black_prompt = self.problem_statement + PS_GENERIC_TASK
        self.black_response = self.llm.call(self.black_system_content, self.black_prompt)

        self.green_prompt = self.problem_statement + PS_GENERIC_TASK
        self.green_response = self.llm.call(self.green_system_content, self.green_prompt)

        self.blue_prompt = (PS_BLUE_GENERIC_TASK 
                            + PS_BLUE_PROBLEM_TASK + self.problem_statement 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_WHITE_TASK  + self.white_response 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_RED_TASK + self.red_response 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_BLACK_TASK + self.black_response 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_YELLOW_TASK + self.yellow_response
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_GREEN_TASK + self.green_response)
        self.blue_response = self.llm.call(self.blue_system_content, self.blue_prompt)

    def renderAlternatives(self):
        self.white_prompt = self.problem_statement + PS_GENERIC_TASK
        self.white_response = self.llm.call(self.white_system_content, self.white_prompt)

        self.green_prompt = self.problem_statement + PS_GENERIC_TASK
        self.green_response = self.llm.call(self.green_system_content, self.green_prompt)

        self.yellow_prompt = self.problem_statement + PS_GENERIC_TASK
        self.yellow_response = self.llm.call(self.yellow_system_content, self.yellow_prompt)

        self.black_prompt = self.problem_statement + PS_GENERIC_TASK
        self.black_response = self.llm.call(self.black_system_content, self.black_prompt)

        self.red_prompt = self.problem_statement + PS_GENERIC_TASK
        self.red_response = self.llm.call(self.red_system_content, self.red_prompt)

        self.blue_prompt = (PS_BLUE_GENERIC_TASK 
                            + PS_BLUE_PROBLEM_TASK + self.problem_statement 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_WHITE_TASK  + self.white_response 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_RED_TASK + self.red_response 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_BLACK_TASK + self.black_response 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_YELLOW_TASK + self.yellow_response
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_GREEN_TASK + self.green_response)
        self.blue_response = self.llm.call(self.blue_system_content, self.blue_prompt)

    def renderAlternativesCasc(self):
        self.white_prompt = (self.problem_statement 
                             + PS_GENERIC_TASK)
        self.white_response = self.llm.call(self.white_system_content, self.white_prompt)
        
        self.green_prompt = (self.problem_statement 
                             + PS_GENERIC_TASK
                             + self.green_prompt 
                             + PS_GENERIC_PREDECESSOR 
                             + self.white_response)
        self.green_response = self.llm.call(self.green_system_content, self.green_prompt)

        self.yellow_prompt = (self.problem_statement 
                              + PS_GENERIC_TASK
                              + self.yellow_prompt 
                              + PS_GENERIC_PREDECESSOR 
                              + self.white_response 
                              + PS_GENERIC_LINEBREAK_M 
                              + self.green_response)
        self.yellow_response = self.llm.call(self.yellow_system_content, self.yellow_prompt)

        self.black_prompt = (self.problem_statement 
                             + PS_GENERIC_TASK
                             + self.black_prompt 
                             + PS_GENERIC_PREDECESSOR 
                             + self.white_response
                            + self.black_prompt 
                            + PS_GENERIC_LINEBREAK_M 
                            + self.green_response 
                            + PS_GENERIC_LINEBREAK_M 
                            + self.yellow_response)
        self.black_response = self.llm.call(self.black_system_content, self.black_prompt)

        self.red_prompt = (self.problem_statement 
                           + PS_GENERIC_TASK
                           + self.red_prompt 
                           + PS_GENERIC_PREDECESSOR 
                           + self.white_response
                           + self.red_prompt 
                           + PS_GENERIC_LINEBREAK_M 
                           + self.green_response 
                           + PS_GENERIC_LINEBREAK_M 
                           + self.yellow_response 
                           + PS_GENERIC_LINEBREAK_M 
                           + self.black_response)
        self.red_response = self.llm.call(self.red_system_content, self.red_prompt)
  
        self.blue_prompt = (PS_BLUE_GENERIC_TASK 
                            + PS_BLUE_PROBLEM_TASK 
                            + self.problem_statement 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_WHITE_TASK  
                            + self.white_response 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_RED_TASK 
                            + self.red_response 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_BLACK_TASK 
                            + self.black_response 
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_YELLOW_TASK 
                            + self.yellow_response
                            + PS_GENERIC_LINEBREAK_L 
                            + PS_BLUE_CONTRIB_GREEN_TASK 
                            + self.green_response)
        self.blue_response = self.llm.call(self.blue_system_content, self.blue_prompt)

    def renderIdea(self):
        self.white_prompt = self.problem_statement + PS_GENERIC_TASK
        self.white_response = self.llm.call(self.white_system_content, self.white_prompt)

        self.green_prompt = self.problem_statement + PS_GENERIC_TASK
        self.green_response = self.llm.call(self.green_system_content, self.green_prompt)

        self.blue_prompt = (PS_BLUE_GENERIC_TASK
                            + PS_BLUE_PROBLEM_TASK
                            + self.problem_statement 
                            + PS_GENERIC_LINEBREAK_L
                            + PS_BLUE_CONTRIB_WHITE_TASK 
                            + self.white_response 
                            + PS_GENERIC_LINEBREAK_L
                            + PS_BLUE_CONTRIB_GREEN_TASK 
                            + self.green_response)
        self.blue_response = self.llm.call(self.blue_system_content, self.blue_prompt)

    def export(self):
        '''Export the content of the chatbots to a file
        
        The method takes not input parameters, but relies heavily on
        class variables. Also the methods uses the outputhandler a lot.

        It checks for every hat, if there are responses from the hat; if there are none of a hat, no text of this hat will be exported.
        The order in which the results of the hats are exported is always the same: white, green, yellow, black, red, blue; it does not matter in which order they were prompted.
        '''
        contentheader = "".join([
            self.outputhandler.h1(PS_LITERAL_STC),
            self.outputhandler.p(PS_LITERAL_MODE
                                 + self.mode),
            self.outputhandler.p(PS_LITERAL_DATE
                                 + datetime.now().strftime("%d.%m.%Y %H:%M:%S")),
            self.outputhandler.h2(PS_LITERAL_PROBLEM_STATEMENT),
            self.outputhandler.p(self.problem_statement)])

        if self.white_response != '':
            contentwh = "".join([
                self.outputhandler.h2(PS_LITERAL_WH),
                self.outputhandler.p(PS_LITERAL_PROMPT 
                          + self.white_system_content 
                          + self.white_prompt),
                self.outputhandler.p(PS_LITERAL_RESPONSE   
                          + self.white_response)])
        else: 
            contentwh = ""

        if self.green_response != '':
            contentgh = "".join([
                self.outputhandler.h2(PS_LITERAL_GH),
                self.outputhandler.p(PS_LITERAL_PROMPT 
                          + self.green_system_content 
                          + self.green_prompt),
                self.outputhandler.p(PS_LITERAL_RESPONSE   
                          + self.green_response)])
        else: 
            contentgh = ""

        if self.yellow_response != '':
            contentyh = "".join([
                self.outputhandler.h2(PS_LITERAL_YH),
                self.outputhandler.p(PS_LITERAL_PROMPT 
                          + self.yellow_system_content 
                          + self.yellow_prompt),
                self.outputhandler.p(PS_LITERAL_RESPONSE   
                          + self.yellow_response)])
        else: 
            contentyh = ""

        if self.black_response != '':
            contentbh = "".join([
                self.outputhandler.h2(PS_LITERAL_BH),
                self.outputhandler.p(PS_LITERAL_PROMPT 
                          + self.black_system_content 
                          + self.black_prompt),
                self.outputhandler.p(PS_LITERAL_RESPONSE   
                          + self.black_response)])
        else: 
            contentbh = ""

        if self.red_response != '':
            contentrh = "".join([
                self.outputhandler.h2(PS_LITERAL_RH),
                self.outputhandler.p(PS_LITERAL_PROMPT 
                          + self.red_system_content 
                          + self.red_prompt),
                self.outputhandler.p(PS_LITERAL_RESPONSE   
                          + self.red_response)])
        else: 
            contentrh = ""

        if self.blue_response != '':
            contentbh = "".join([
                self.outputhandler.h2(PS_LITERAL_BH),
                self.outputhandler.p(PS_LITERAL_PROMPT 
                          + self.blue_system_content 
                          + self.blue_prompt),
                self.outputhandler.p(PS_LITERAL_RESPONSE   
                          + self.blue_response)])
        else: 
            contentbh = ""

        document = "".join([contentheader, 
                          contentwh, 
                          contentgh, 
                          contentyh, 
                          contentbh, 
                          contentrh, 
                          contentbh])

        return(self.outputhandler.document("", document))


"""     def callLlm(self, system_content, prompt, model="Mistral"):
        match model:
            case "Mistral":
                return self.callMistral(system_content, prompt)
            case  "gpt4o":
                return self.callChatGPT(system_content, prompt)
            case  "llama":
                return self.callLlama(system_content, prompt)
            case _:
                return "Specify model."



    def callChatGPT(self, system_content, prompt):

        client = OpenAI(api_key = self.key)

        dialogue = client.chat.completions.create(
           model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5, 
            top_p=0.5
        )

        time.sleep(0.1)
        return dialogue.choices[0].message.content

    def callLlama(self, system_content, prompt):
        login(token=self.key) 
    
        self.llm = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")

        input_text = f"System: {system_content}\nUser: {prompt}"

        response = self.llm(
            input_text,
            max_length=512,
            temperature=0.5,
            top_p=0.5,
            num_return_sequences=1
        )

        time.sleep(0.1)
        return response[0]['generated_text'].split("User:")[-1].strip()

    
    def callMistral(self, system_content, prompt):
        api_url = "https://api.mistral.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "mistral-tiny", 
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 512,
            "temperature": 0.5,
            "top_p": 0.5
        }

        response = requests.post(api_url, json=payload, headers=headers)
        time.sleep(1)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"Fehler: {response.status_code}, {response.text}" """
