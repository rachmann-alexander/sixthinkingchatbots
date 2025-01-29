""" Six Thinking Chatbots, see https://github.com/rachmann-alexander/sixthinkingchatbots"""

from datetime import datetime
import time
import logging
from openai import OpenAI
from transformers import pipeline
from huggingface_hub import login
import requests
from config import MISTRAL_API_KEY



""" Domain class of this prototype """
class SixThinkingChatbots():
    problem_statement = ''    
    white_system_content = 'You are a participant of a workshop. Your decision making is fact based and your argumentation is very structured. '
    white_prompt = ''
    white_response = ''

    green_system_content = 'You are a participant of a workshop. Your decision making is based on the possibilities of innovations. '
    green_prompt = ''
    green_response = ''

    yellow_system_content = 'You are a participant of a workshop. You are an optimist. '
    yellow_prompt = ''
    yellow_response = ''

    black_system_content = 'You are a participant of a workshop. You are a pessimist. '
    black_prompt = ''
    black_response = ''

    red_system_content = 'You are a participant of a workshop. Your decision making is emotion based. '
    red_prompt = ''
    red_response = ''

    blue_system_content = 'You are the moderator of a workshop, using the Six Thinking Hats methodology. You are neural to the contributions from the participants and value each contribution. '
    blue_prompt = ''
    blue_response = ''

    mode = ''

    result = ''

    key = ''

    def __init__(self, problem_statement, mode, key):
        #logging.basicConfig(filename='stc.log', encoding='utf-8', level=logging.DEBUG)

        self.problem_statement = problem_statement
        self.mode = mode
        self.key = key

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
        self.white_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.white_response = self.callLlm(self.white_system_content, self.white_prompt)

        self.black_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints.'
        self.black_response = self.callLlm(self.black_system_content, self.black_prompt)

        self.green_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.green_response = self.callLlm(self.green_system_content, self.green_prompt)

        self.blue_prompt = 'Summarize the contributions of the participants, as listed beneath. Think about the problem statement and decide, based on the contributions of the participants, which alternative shoud be chosen. '
        self.blue_prompt += 'The problem statement of the workshop is as follows: ' + self.problem_statement + '\n\n'
        self.blue_prompt += 'Contribution from a fact-oriented participant: ' + self.white_response + '\n\n'
        self.blue_prompt += 'Contribution from a emotion-oriented participant: ' + self.red_response + '\n\n'
        self.blue_prompt += 'Contribution from a pessimist: ' + self.black_response + '\n\n'
        self.blue_prompt += 'Contribution from an optimist: ' + self.yellow_response + '\n\n'
        self.blue_prompt += 'Contribution from a innovation-oriented participant: ' + self.green_response
        self.blue_response = self.callLlm(self.blue_system_content, self.blue_prompt)

        self.result = '## White Hat\n'
        self.result += '### Prompt\n' + self.white_system_content + '\n' + self.white_prompt + '\n'
        self.result += '### Response\n' + self.white_response + '\n\n\n'

        self.result += '## Black Hat\n'
        self.result += '### Prompt\n' + self.black_system_content + '\n' + self.black_prompt + '\n'
        self.result += '### Response\n' + self.black_response + '\n\n\n'

        self.result += '## Green Hat\n'
        self.result += '### Prompt\n' + self.green_system_content + '\n' + self.green_prompt + '\n'
        self.result += '### Response\n' + self.green_response + '\n\n\n'

        self.result += '## Blue Hat\n'
        self.result += '### Prompt\n' + self.blue_system_content + '\n' + self.blue_prompt + '\n'
        self.result += '### Response\n' + self.blue_response + '\n\n\n'


    def renderAlternatives(self):
        self.white_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.white_response = self.callLlm(self.white_system_content, self.white_prompt)
        logging.info('White prompt: %s \n White response: %s ', self.white_prompt, self.white_response)

        self.green_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.green_response = self.callLlm(self.green_system_content, self.green_prompt)

        self.yellow_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.yellow_response = self.callLlm(self.yellow_system_content, self.yellow_prompt)

        self.black_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints.'
        self.black_response = self.callLlm(self.black_system_content, self.black_prompt)

        self.red_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints.'
        self.red_response = self.callLlm(self.red_system_content, self.red_prompt)
  
        self.blue_prompt = 'Summarize the contributions of the participants, as listed beneath. Think about the problem statement and decide, based on the contributions of the participants, which alternative shoud be chosen. '
        self.blue_prompt += 'The problem statement of the workshop is as follows: ' + self.problem_statement + '\n\n'
        self.blue_prompt += 'Contribution from a fact-oriented participant: ' + self.white_response + '\n\n'
        self.blue_prompt += 'Contribution from a emotion-oriented participant: ' + self.red_response + '\n\n'
        self.blue_prompt += 'Contribution from a pessimist: ' + self.black_response + '\n\n'
        self.blue_prompt += 'Contribution from an optimist: ' + self.yellow_response + '\n\n'
        self.blue_prompt += 'Contribution from a innovation-oriented participant: ' + self.green_response
        self.blue_response = self.callLlm(self.blue_system_content, self.blue_prompt)

        self.result = '## White Hat\n'
        self.result += '### Prompt\n' + self.white_system_content + '\n' + self.white_prompt + '\n'
        self.result += '### Response\n' + self.white_response + '\n\n\n'

        self.result += '## Green Hat\n'
        self.result += '### Prompt\n' + self.green_system_content + '\n' + self.green_prompt + '\n'
        self.result += '### Response\n' + self.green_response + '\n\n\n'

        self.result += '## Yellow Hat\n'
        self.result += '### Prompt\n' + self.yellow_system_content + '\n' + self.yellow_prompt + '\n'
        self.result += '### Response\n' + self.yellow_response + '\n\n\n'

        self.result += '## Black Hat\n'
        self.result += '### Prompt\n' + self.black_system_content + '\n' + self.black_prompt + '\n'
        self.result += '### Response\n' + self.black_response + '\n\n\n'

        self.result += '## Red Hat\n'
        self.result += '### Prompt\n' + self.red_system_content + '\n' + self.red_prompt + '\n'
        self.result += '### Response\n' + self.red_response + '\n\n\n'

        self.result += '## Blue Hat\n'
        self.result += '### Prompt\n' + self.blue_system_content + '\n' + self.blue_prompt + '\n'
        self.result += '### Response\n' + self.blue_response + '\n\n\n'

    def renderAlternativesCasc(self):
        self.white_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.white_response = self.callLlm(self.white_system_content, self.white_prompt)
        
        self.green_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.green_prompt += self.green_prompt + 'These are statements by your predecessor: ' + self.white_response
        self.green_response = self.callLlm(self.green_system_content, self.green_prompt)

        self.yellow_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.yellow_prompt += self.yellow_prompt + 'These are statements by your predecessor: ' + self.white_response + '\n' + self.green_response
        self.yellow_response = self.callLlm(self.yellow_system_content, self.yellow_prompt)

        self.black_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints.'
        self.black_prompt += self.black_prompt + 'These are statements by your predecessor: ' + self.white_response
        self.black_prompt += self.black_prompt + '\n' + self.green_response + '\n' + self.yellow_response
        self.black_response = self.callLlm(self.black_system_content, self.black_prompt)

        self.red_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints.'
        self.red_prompt += self.red_prompt + 'These are statements by your predecessor: ' + self.white_response
        self.red_prompt += self.red_prompt + '\n' + self.green_response + '\n' + self.yellow_response + '\n' + self.black_response
        self.red_response = self.callLlm(self.red_system_content, self.red_prompt)
  
        self.blue_prompt = 'Summarize the contributions of the participants, as listed beneath. Think about the problem statement and decide, based on the contributions of the participants, which alternative shoud be chosen. '
        self.blue_prompt += 'The problem statement of the workshop is as follows: ' + self.problem_statement + '\n\n'
        self.blue_prompt += 'Contribution from a fact-oriented participant: ' + self.white_response + '\n\n'
        self.blue_prompt += 'Contribution from a emotion-oriented participant: ' + self.red_response + '\n\n'
        self.blue_prompt += 'Contribution from a pessimist: ' + self.black_response + '\n\n'
        self.blue_prompt += 'Contribution from an optimist: ' + self.yellow_response + '\n\n'
        self.blue_prompt += 'Contribution from a innovation-oriented participant: ' + self.green_response
        self.blue_response = self.callLlm(self.blue_system_content, self.blue_prompt)

        self.result = '## White Hat\n'
        self.result += '### Prompt\n' + self.white_system_content + '\n' + self.white_prompt + '\n'
        self.result += '### Response\n' + self.white_response + '\n\n\n'

        self.result += '## Green Hat\n'
        self.result += '### Prompt\n' + self.green_system_content + '\n' + self.green_prompt + '\n'
        self.result += '### Response\n' + self.green_response + '\n\n\n'

        self.result += '## Yellow Hat\n'
        self.result += '### Prompt\n' + self.yellow_system_content + '\n' + self.yellow_prompt + '\n'
        self.result += '### Response\n' + self.yellow_response + '\n\n\n'

        self.result += '## Black Hat\n'
        self.result += '### Prompt\n' + self.black_system_content + '\n' + self.black_prompt + '\n'
        self.result += '### Response\n' + self.black_response + '\n\n\n'

        self.result += '## Red Hat\n'
        self.result += '### Prompt\n' + self.red_system_content + '\n' + self.red_prompt + '\n'
        self.result += '### Response\n' + self.red_response + '\n\n\n'

        self.result += '## Blue Hat\n'
        self.result += '### Prompt\n' + self.blue_system_content + '\n' + self.blue_prompt + '\n'
        self.result += '### Response\n' + self.blue_response + '\n\n\n'
  
    def renderIdea(self):
        self.white_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.white_response = self.callLlm(self.white_system_content, self.white_prompt)

        self.green_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.green_response = self.callLlm(self.green_system_content, self.green_prompt)

        self.blue_prompt = 'Summarize the contributions of the participants, as listed beneath. Think about the problem statement and decide, based on the contributions of the participants, which ideas shoud be chosen. '
        self.blue_prompt += 'The problem statement of the workshop is as follows: ' + self.problem_statement + '\n\n'
        self.blue_prompt += 'Contribution from a fact-oriented participant: ' + self.white_response + '\n\n'
        self.blue_prompt += 'Contribution from a innovation-oriented participant: ' + self.green_response
        self.blue_response = self.callLlm(self.blue_system_content, self.blue_prompt)
        
        self.result = '## White Hat\n'
        self.result += '### Prompt\n' + self.white_system_content + '\n' + self.white_prompt + '\n'
        self.result += '### Response\n' + self.white_response + '\n\n\n'

        self.result += '## Green Hat\n'
        self.result += '### Prompt\n' + self.green_system_content + '\n' + self.green_prompt + '\n'
        self.result += '### Response\n' + self.green_response + '\n\n\n'

        self.result += '## Blue Hat\n'
        self.result += '### Prompt\n' + self.blue_system_content + '\n' + self.blue_prompt + '\n'
        self.result += '### Response\n' + self.blue_response + '\n\n\n'



    def exportToMd(self):
        export = '# Six Thinking Chatbots ' + '\n'
        export += ' Mode: ' + self.mode + '\n'
        export += ' ' + datetime.now().strftime("%d.%m.%Y %H:%M:%S") + '\n'
        export += '## Problem statement\n' + self.problem_statement + '\n\n\n'

        export += self.result

        return(export)


    def callLlm(self, system_content, prompt):
        return self.callMistral(system_content, prompt)



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
            return f"Fehler: {response.status_code}, {response.text}"

