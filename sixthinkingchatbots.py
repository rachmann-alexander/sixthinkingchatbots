""" Six Thinking Chatbots, see https://github.com/rachmann-alexander/sixthinkingchatbots"""

from datetime import datetime
import time
from openai import OpenAI

from config import API_KEY

client = OpenAI(api_key = API_KEY)

# COLOR                             OVERVIEW
# BLUE	                            "The Big Picture"
# WHITE	                            "Facts & Information"
# RED	                            "Feelings & Emotions"
# BLACK	                            "Negative"
# YELLOW	                        "Positive"
# GREEN	                            "New Ideas"

# ACTIVITY	                        HAT SEQUENCE
# Initial Ideas	                    Blue, White, Green, Blue
# Choosing between alternatives	    Blue, White, (Green), Yellow, Black, Red, Blue
# Identifying Solutions	            Blue, White, Black, Green, Blue
# Quick Feedback	                Blue, Black, Green, Blue
# Strategic Planning	            Blue, Yellow, Black, White, Blue, Green, Blue
# Process Improvement	            Blue, White, White (Other People's Views), Yellow, 
#                                   Black, Green, Red, Blue
# Solving Problems	                Blue, White, Green, Red, Yellow, Black, Green, Blue
# Performance Review	            Blue, Red, White, Yellow, Black, Green, Blue


####################################
# Choosing between alternatives	    Blue, White, (Green), Yellow, Black, Red, Blue
####################################

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

    def __init__(self, problem_statement, mode):
        self.problem_statement = problem_statement
        self.mode = mode

        match self.mode:
            case "alternatives":
                self.renderAlternatives()
                #self.renderAlternativesSetPromptsWithoutBlue()
                #self.white_response = self.callChatGPT(self.white_system_content, self.white_prompt)
                #self.green_response = self.callChatGPT(self.green_system_content, self.green_prompt)
                #self.yellow_response = self.callChatGPT(self.yellow_system_content, self.yellow_prompt)
                #self.black_response = self.callChatGPT(self.black_system_content, self.black_prompt)
                #self.red_response = self.callChatGPT(self.red_system_content, self.red_prompt)
  
                #self.renderAlternativesSetPromptsOnlyBlue()
                #self.blue_response = self.callChatGPT(self.blue_system_content, self.blue_prompt)

            case "somethingElse":
                print("something else")

            case _:
                print("Specify mode.")


    def renderAlternatives(self):
        self.white_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.white_response = self.callChatGPT(self.white_system_content, self.white_prompt)

        self.green_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.green_response = self.callChatGPT(self.green_system_content, self.green_prompt)

        self.yellow_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints. '
        self.yellow_response = self.callChatGPT(self.yellow_system_content, self.yellow_prompt)

        self.black_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints.'
        self.black_response = self.callChatGPT(self.black_system_content, self.black_prompt)

        self.red_prompt = self.problem_statement + ' Describe your point of view to this problem, using only three bulletpoints.'
        self.red_response = self.callChatGPT(self.red_system_content, self.red_prompt)
  
        self.blue_prompt = 'Summarize the contributions of the participants, as listed beneath. Think about the problem statement and decide, based on the contributions of the participants, which alternative shoud be chosen. '
        self.blue_prompt += 'The problem statement of the workshop is as follows: ' + self.problem_statement + '\n\n'
        self.blue_prompt += 'Contribution from a fact-oriented participant: ' + self.white_response + '\n\n'
        self.blue_prompt += 'Contribution from a emotion-oriented participant: ' + self.red_response + '\n\n'
        self.blue_prompt += 'Contribution from a pessimist: ' + self.black_response + '\n\n'
        self.blue_prompt += 'Contribution from an optimist: ' + self.yellow_response + '\n\n'
        self.blue_prompt += 'Contribution from a innovation-oriented participant: ' + self.green_response
        self.blue_response = self.callChatGPT(self.blue_system_content, self.blue_prompt)

        self.renderAlternativesResults()


    def renderAlternativesResults(self):
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
  
    def exportToMd(self):
        export = '# Six Thinking Chatbots ' + '\n'
        export += ' Mode: ' + self.mode + '\n'
        export += ' ' + datetime.now().strftime("%d.%m.%Y %H:%M:%S") + '\n'
        export += '## Problem statement\n' + self.problem_statement + '\n\n\n'

        export += self.result

        return(export)


    def callChatGPT(self, system_content, prompt):
        dialogue = client.chat.completions.create(
           model="gpt-4",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt}
            ]
        )

        time.sleep(0.1)
        return dialogue.choices[0].message.content

problem = 'The goal of the workshop is to evaluate three alternatives to a problem. The problem is: '
problem += 'The sales process on our companies website does not work very well. Management wants us to change the sales process to one of the three alternatives: '
problem += 'First, an old-school chatbot with a beforehand written structure. '
problem += 'Second, a chatbot using a large language model, without a pre-defined structure. '
problem += 'Third, an old-school contact form. '

idea = SixThinkingChatbots(problem, "alternatives")
print(idea.exportToMd())


