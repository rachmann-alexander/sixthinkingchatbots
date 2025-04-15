""" Six Thinking Chatbots, see https://github.com/rachmann-alexander/sixthinkingchatbots"""

from datetime import datetime
from abc import ABC
import time
import logging
from openai import OpenAI
from transformers import pipeline
from huggingface_hub import login
import requests

from language import *
from llmhandler import *
from outputhandler import *



class SixThinkingChatbots():
    """ Domain class of this application 
    Takes four arguments:

    problem_statement: The text of what the user want to be discussed by the chatbots
    mode: A mode is the order in which the hats are prompted. Default is alternativesCascading. Other modes may be idea, alternatives, solutions, feedback, planning, processimprovement, solvingproblems, review. See literature about Six Thinking Hats to understand more about the modes.
    model: The large language model the hats will use. Default is Mistral. 
    outputhandler: Is the format the chatbot will put out. Default is markdown ("md"). Html ist also implemented.
    
    """ 
    white_system_content = ''
    white_prompt = ''
    white_response = ''

    green_system_content = ''
    green_prompt = ''
    green_response = ''

    yellow_system_content = ''
    yellow_prompt = ''
    yellow_response = ''

    black_system_content = ''
    black_prompt = ''
    black_response = ''

    red_system_content = ''
    red_prompt = ''
    red_response = ''

    blue_system_content = ''
    blue_prompt = ''
    blue_response = ''

    result = ''
    

    def __init__(self, problem_statement, mode="alternativesCascading", model="Mistral", outputhandler="reveal", language="de"):
        ''' Constructor of the class SixThinkingChatbots

        The constructor takes four arguments; see the docstring of the class for more information.

        The constructor controls more or less which mode is used; that is all.
        '''


        self.mode = mode

        self.problem_statement = problem_statement

        self.outputhandler = ''

        match outputhandler:
            case "md":
                self.outputhandler = MarkdownHandler()
            case "html":
                self.outputhandler = HtmlHandler()
            case "reveal":
                self.outputhandler = RevealJSHandler()
            case _:
                self.outputhandler = MarkdownHandler()


        self.language = language

        match language:
            case "de":
                self.language = German()
            case "en":
                self.language = English()
            case _:
                self.language = German()

        self.white_system_content = self.language.PS_WHITE_SYSTEM_CONTENT
        self.green_system_content = self.language.PS_GREEN_SYSTEM_CONTENT
        self.yellow_system_content = self.language.PS_YELLOW_SYSTEM_CONTENT
        self.black_system_content = self.language.PS_BLACK_SYSTEM_CONTENT
        self.red_system_content = self.language.PS_RED_SYSTEM_CONTENT
        self.blue_system_content = self.language.PS_BLUE_SYSTEM_CONTENT


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
        self.white_prompt = self.problem_statement + self.language.PS_GENERIC_TASK
        self.white_response = self.llm.call(self.white_system_content, self.white_prompt)

        self.black_prompt = self.problem_statement + self.language.PS_GENERIC_TASK
        self.black_response = self.llm.call(self.black_system_content, self.black_prompt)

        self.green_prompt = self.problem_statement + self.language.PS_GENERIC_TASK
        self.green_response = self.llm.call(self.green_system_content, self.green_prompt)

        self.blue_prompt = (self.language.PS_BLUE_GENERIC_TASK 
                            + self.language.PS_BLUE_PROBLEM_TASK + self.problem_statement 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_WHITE_TASK  + self.white_response 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_RED_TASK + self.red_response 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_BLACK_TASK + self.black_response 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_YELLOW_TASK + self.yellow_response
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_GREEN_TASK + self.green_response)
        self.blue_response = self.llm.call(self.blue_system_content, self.blue_prompt)

    def renderAlternatives(self):
        self.white_prompt = self.problem_statement + self.language.PS_GENERIC_TASK
        self.white_response = self.llm.call(self.white_system_content, self.white_prompt)

        self.green_prompt = self.problem_statement + self.language.PS_GENERIC_TASK
        self.green_response = self.llm.call(self.green_system_content, self.green_prompt)

        self.yellow_prompt = self.problem_statement + self.language.PS_GENERIC_TASK
        self.yellow_response = self.llm.call(self.yellow_system_content, self.yellow_prompt)

        self.black_prompt = self.problem_statement + self.language.PS_GENERIC_TASK
        self.black_response = self.llm.call(self.black_system_content, self.black_prompt)

        self.red_prompt = self.problem_statement + self.language.PS_GENERIC_TASK
        self.red_response = self.llm.call(self.red_system_content, self.red_prompt)

        self.blue_prompt = (self.language.PS_BLUE_GENERIC_TASK 
                            + self.language.PS_BLUE_PROBLEM_TASK + self.problem_statement 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_WHITE_TASK  + self.white_response 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_RED_TASK + self.red_response 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_BLACK_TASK + self.black_response 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_YELLOW_TASK + self.yellow_response
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_GREEN_TASK + self.green_response)
        self.blue_response = self.llm.call(self.blue_system_content, self.blue_prompt)

    def renderAlternativesCasc(self):
        self.white_prompt = (self.problem_statement 
                             + self.language.PS_GENERIC_TASK)
        self.white_response = self.llm.call(self.white_system_content, self.white_prompt)
        
        self.green_prompt = (self.problem_statement 
                             + self.language.PS_GENERIC_TASK
                             + self.green_prompt 
                             + self.language.PS_GENERIC_PREDECESSOR 
                             + self.white_response)
        self.green_response = self.llm.call(self.green_system_content, self.green_prompt)

        self.yellow_prompt = (self.problem_statement 
                              + self.language.PS_GENERIC_TASK
                              + self.yellow_prompt 
                              + self.language.PS_GENERIC_PREDECESSOR 
                              + self.white_response 
                              + self.language.PS_GENERIC_LINEBREAK_M 
                              + self.green_response)
        self.yellow_response = self.llm.call(self.yellow_system_content, self.yellow_prompt)

        self.black_prompt = (self.problem_statement 
                             + self.language.PS_GENERIC_TASK
                             + self.black_prompt 
                             + self.language.PS_GENERIC_PREDECESSOR 
                             + self.white_response
                            + self.black_prompt 
                            + self.language.PS_GENERIC_LINEBREAK_M 
                            + self.green_response 
                            + self.language.PS_GENERIC_LINEBREAK_M 
                            + self.yellow_response)
        self.black_response = self.llm.call(self.black_system_content, self.black_prompt)

        self.red_prompt = (self.problem_statement 
                           + self.language.PS_GENERIC_TASK
                           + self.red_prompt 
                           + self.language.PS_GENERIC_PREDECESSOR 
                           + self.white_response
                           + self.red_prompt 
                           + self.language.PS_GENERIC_LINEBREAK_M 
                           + self.green_response 
                           + self.language.PS_GENERIC_LINEBREAK_M 
                           + self.yellow_response 
                           + self.language.PS_GENERIC_LINEBREAK_M 
                           + self.black_response)
        self.red_response = self.llm.call(self.red_system_content, self.red_prompt)
  
        self.blue_prompt = (self.language.PS_BLUE_GENERIC_TASK 
                            + self.language.PS_BLUE_PROBLEM_TASK 
                            + self.problem_statement 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_WHITE_TASK  
                            + self.white_response 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_RED_TASK 
                            + self.red_response 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_BLACK_TASK 
                            + self.black_response 
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_YELLOW_TASK 
                            + self.yellow_response
                            + self.language.PS_GENERIC_LINEBREAK_L 
                            + self.language.PS_BLUE_CONTRIB_GREEN_TASK 
                            + self.green_response)
        self.blue_response = self.llm.call(self.blue_system_content, self.blue_prompt)

    def renderIdea(self):
        self.white_prompt = self.problem_statement + self.language.PS_GENERIC_TASK
        self.white_response = self.llm.call(self.white_system_content, self.white_prompt)

        self.green_prompt = self.problem_statement + self.language.PS_GENERIC_TASK
        self.green_response = self.llm.call(self.green_system_content, self.green_prompt)

        self.blue_prompt = (self.language.PS_BLUE_GENERIC_TASK
                            + self.language.PS_BLUE_PROBLEM_TASK
                            + self.problem_statement 
                            + self.language.PS_GENERIC_LINEBREAK_L
                            + self.language.PS_BLUE_CONTRIB_WHITE_TASK 
                            + self.white_response 
                            + self.language.PS_GENERIC_LINEBREAK_L
                            + self.language.PS_BLUE_CONTRIB_GREEN_TASK 
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
            self.outputhandler.h1(self.language.PS_LITERAL_STC),
            self.outputhandler.p(self.language.PS_LITERAL_MODE
                                 + self.mode),
            self.outputhandler.p(self.language.PS_LITERAL_DATE
                                 + datetime.now().strftime("%d.%m.%Y %H:%M:%S")),
            self.outputhandler.h2(self.language.PS_LITERAL_PROBLEM_STATEMENT),
            self.outputhandler.p(self.problem_statement)])
        contentheader = self.outputhandler.sectionWrap(contentheader)

        if self.white_response != '':
            contentwh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_WH),
                self.outputhandler.p(self.language.PS_LITERAL_PROMPT 
                          + self.white_system_content 
                          + self.white_prompt),
                self.outputhandler.p(self.language.PS_LITERAL_RESPONSE   
                          + self.white_response)])
        else: 
            contentwh = ""
        contentwh = self.outputhandler.sectionWrap(contentwh)

        if self.green_response != '':
            contentgh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_GH),
                self.outputhandler.p(self.language.PS_LITERAL_PROMPT 
                          + self.green_system_content 
                          + self.green_prompt),
                self.outputhandler.p(self.language.PS_LITERAL_RESPONSE   
                          + self.green_response)])
        else: 
            contentgh = ""
        contentgh = self.outputhandler.sectionWrap(contentgh)

        if self.yellow_response != '':
            contentyh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_YH),
                self.outputhandler.p(self.language.PS_LITERAL_PROMPT 
                          + self.yellow_system_content 
                          + self.yellow_prompt),
                self.outputhandler.p(self.language.PS_LITERAL_RESPONSE   
                          + self.yellow_response)])
        else: 
            contentyh = ""
        contentyh = self.outputhandler.sectionWrap(contentyh)

        if self.black_response != '':
            contentbh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_BlaH),
                self.outputhandler.p(self.language.PS_LITERAL_PROMPT 
                          + self.black_system_content 
                          + self.black_prompt),
                self.outputhandler.p(self.language.PS_LITERAL_RESPONSE   
                          + self.black_response)])
        else: 
            contentbh = ""
        contentbh = self.outputhandler.sectionWrap(contentbh)

        if self.red_response != '':
            contentrh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_RH),
                self.outputhandler.p(self.language.PS_LITERAL_PROMPT 
                          + self.red_system_content 
                          + self.red_prompt),
                self.outputhandler.p(self.language.PS_LITERAL_RESPONSE   
                          + self.red_response)])
        else: 
            contentrh = ""
        contentrh = self.outputhandler.sectionWrap(contentrh)

        if self.blue_response != '':
            contentbluh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_BluH),
                self.outputhandler.p(self.language.PS_LITERAL_PROMPT 
                          + self.blue_system_content 
                          + self.blue_prompt),
                self.outputhandler.p(self.language.PS_LITERAL_RESPONSE   
                          + self.blue_response)])
        else: 
            contentbluh = ""
        contentbluh = self.outputhandler.sectionWrap(contentbluh)

        document = "".join([contentheader, 
                          contentwh, 
                          contentgh, 
                          contentyh, 
                          contentbh, 
                          contentrh, 
                          contentbluh])
        
        full_document = self.outputhandler.document("", document)

        self.outputhandler.storeFile(full_document, "index")

        return(full_document)
    
    def exportShort(self):
        '''Export the content of the chatbots to a file
        
        The method takes not input parameters, but relies heavily on
        class variables. Also the methods uses the outputhandler a lot.

        It checks for every hat, if there are responses from the hat; if there are none of a hat, no text of this hat will be exported.
        The order in which the results of the hats are exported is always the same: white, green, yellow, black, red, blue; it does not matter in which order they were prompted.

        Different to export(), only responses of the hats are exported.
        '''

        if isinstance(self.outputhandler, RevealJSHandler):
            whimage = '<img class="reveal" src="img/whitehat.png" alt="White Hat" />'
            bluhimage = '<img class="reveal" src="img/bluehat.png" alt="Blue Hat" />'
            bhimage = '<img class="reveal" src="img/blackhat.png" alt="Black Hat" />'
            yhimage = '<img class="reveal" src="img/yellowhat.png" alt="Yellow Hat" />'
            ghimage = '<img class="reveal" src="img/greenhat.png" alt="Green Hat" />'
            rhimage = '<img class="reveal" src="img/redhat.png" alt="Red Hat" />'
            resultimage = '<img class="reveal" src="img/result.png" alt="Result from Blue Hat" />'
        else:
            rhimage = ''
            resultimage = ''
            whimage = ''
            bluhimage = ''
            bhimage = ''
            yhimage = ''
            ghimage = ''

        contentheader = "".join([
            self.outputhandler.h1(self.language.PS_LITERAL_STC),
            bluhimage,
            self.outputhandler.h2(self.language.PS_LITERAL_PROBLEM_STATEMENT),
            self.outputhandler.p(self.problem_statement)])
        contentheader = self.outputhandler.sectionWrap(contentheader)

        if self.white_response != '':
            contentwh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_WH),
                whimage,
                self.outputhandler.p(self.white_response)])
        else: 
            contentwh = ""
        contentwh = self.outputhandler.sectionWrap(contentwh)

        if self.green_response != '':
            contentgh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_GH),
                ghimage,
                self.outputhandler.p(self.green_response)])
        else: 
            contentgh = ""
        contentgh = self.outputhandler.sectionWrap(contentgh)

        if self.yellow_response != '':
            contentyh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_YH),
                yhimage,
                self.outputhandler.p(self.yellow_response)])
        else: 
            contentyh = ""
        contentyh = self.outputhandler.sectionWrap(contentyh)

        if self.black_response != '':
            contentbh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_BlaH),
                bhimage,
                self.outputhandler.p(self.black_response)])
        else: 
            contentbh = ""
        contentbh = self.outputhandler.sectionWrap(contentbh)

        if self.red_response != '':
            contentrh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_RH),
                rhimage,
                self.outputhandler.p(self.red_response)])
        else: 
            contentrh = ""
        contentrh = self.outputhandler.sectionWrap(contentrh)

        if self.blue_response != '':
            contentbluh = "".join([
                self.outputhandler.h2(self.language.PS_LITERAL_BluH),
                resultimage,
                self.outputhandler.p(self.blue_response)])
        else: 
            contentbluh = ""
        contentbluh = self.outputhandler.sectionWrap(contentbluh)

        document = "".join([contentheader, 
                          contentwh, 
                          contentgh, 
                          contentyh, 
                          contentbh, 
                          contentrh, 
                          contentbluh])
        
        full_document = self.outputhandler.document("", document)

        self.outputhandler.storeFile(full_document, "index")

        return(full_document)

