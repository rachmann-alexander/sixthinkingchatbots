"""Module providing an interface to Six Thinking Chatbots"""

from config import API_KEY
from sixthinkingchatbots import SixThinkingChatbots

problemAlternativesMode = 'The goal of the workshop is to evaluate three alternatives to a problem. The problem is: '
problemAlternativesMode += 'The sales process on our companies website does not work very well. Management wants us to change the sales process to one of the three alternatives: '
problemAlternativesMode += 'First, an old-school chatbot with a beforehand written structure. '
problemAlternativesMode += 'Second, a chatbot using a large language model, without a pre-defined structure. '
problemAlternativesMode += 'Third, an old-school contact form. '
idea = SixThinkingChatbots(problemAlternativesMode, "alternativesCascading", API_KEY)

#problemIdeaMode = 'The goal of the workshop is to find new ideas. The problem is: '
#problemIdeaMode += 'The sales process on our companies website does not work very well. Management wants us to generate ideas how to improve the sales process.'
#idea = SixThinkingChatbots(problemIdeaMode, "idea")

print(idea.exportToMd())