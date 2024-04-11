# Six Thinking Chatbots
Prototypical Implemention of a AI-supported Six Thinking Hats-Methodology

# Requirements
* Up to date Python
* OpenAI Library
* OpenAI Account and Billing Plan

# How to use
1. (If necessary, read [this wikipedia page](https://en.wikipedia.org/wiki/Six_Thinking_Hats) to understand Six Thinking Hats.)
2. Checkout repository.
3. Create a file config.py with variable API_KEY

```python
    API_KEY='your-api-key'
```

4. Create file runtime.py or any other name, such as

```python
    from config import API_KEY
    from sixthinkingchatbots import SixThinkingChatbots
    problemStatement = 'This is the problem statement.
    idea = SixThinkingChatbots(problemStatement, "idea")
    print(idea.exportToMd())
```

5. Run. See result as a string (please, be patient; there is a built-in delay callChatGPT(), to not-freak out OpenAI).
