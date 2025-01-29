"""Module providing an interface to Six Thinking Chatbots"""

from config import MISTRAL_API_KEY
from stc2 import SixThinkingChatbots

problemAlternativesMode = 'The goal of the workshop is to evaluate three alternatives to a problem. The problem is: '
problemAlternativesMode += 'The sales process on our companies website does not work very well. Management wants us to change the sales process to one of the three alternatives: '
problemAlternativesMode += 'First, an old-school chatbot with a beforehand written structure. '
problemAlternativesMode += 'Second, a chatbot using a large language model, without a pre-defined structure. '
problemAlternativesMode += 'Third, an old-school contact form. '
idea = SixThinkingChatbots(problemAlternativesMode, "alternativesCascading", MISTRAL_API_KEY)

#problemIdeaMode = 'The goal of the workshop is to find new ideas. The problem is: '
#problemIdeaMode += 'The sales process on our companies website does not work very well. Management wants us to generate ideas how to improve the sales process.'
#idea = SixThinkingChatbots(problemIdeaMode, "idea", MISTRAL_API_KEY)

print(idea.exportToMd())
