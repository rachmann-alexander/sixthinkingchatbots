# Six Thinking Chatbots
Prototypical Implemention of a AI-supported Six Thinking Hats-Methodology

# Requirements
* Up to date Python
* Modules: datetime, time, logging, OpenAI, transformers, huggingface_hub, requests. Not all of them are required.
* January 2025: Mistral Plan in Experimental stage

# How to use
1. (If necessary, read [this wikipedia page](https://en.wikipedia.org/wiki/Six_Thinking_Hats) to understand Six Thinking Hats.)
2. Checkout repository.
3. Create a file config.py with variable MISTRAL_API_KEY 

```python
    MISTRAL_API_KEY='your-api-key'
```

4. Create file runtime.py or any other name, such as

```python
from config import MISTRAL_API_KEY
from stc2 import SixThinkingChatbots

problemAlternativesMode = 'The goal of the workshop is to evaluate three alternatives to a problem. The problem is: '
problemAlternativesMode += 'The sales process on our companies website does not work very well. Management wants us to change the sales process to one of the three alternatives: '
problemAlternativesMode += 'First, an old-school chatbot with a beforehand written structure. '
problemAlternativesMode += 'Second, a chatbot using a large language model, without a pre-defined structure. '
problemAlternativesMode += 'Third, an old-school contact form. '
idea = SixThinkingChatbots(problemAlternativesMode, "alternativesCascading")

print(idea.exportToMd())
```

5. Run. See result as a string (please, be patient; there is a built-in delay, to not-freak out the API). Change "idea" to something else:
* alternatives
* alternativesCascading
* solutions

# Addendum
There are methods for usage with OpenAI / ChatGPT and Meta / Llama. In order to use these, change method callLlm() and change api keys.
