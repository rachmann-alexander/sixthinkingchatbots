from abc import ABC
import os

class outputhandler(ABC):
    ''' Defines only the interface of the subclasses.
    '''
    def __init__(self):
        pass

    def document(self, head, body):
        pass

    def sectionWrap(self, content):
        pass
    
    def h1(self, content):
        pass
    
    def h2(self, content):
        pass
    
    def h3(self, content):
        pass
        

class MarkdownHandler(outputhandler):
    '''
    Gives helper methods to use markdown syntax.
    '''
    def __init__(self):
        pass

    def document(self, head, body):
        return body
    
    def sectionWrap(self, content):
        return f"{content}"
    
    def h1(self, content):
        return f"# {content}\n\n"   
    
    def h2(self, content):
        return f"## {content}\n\n"
    
    def h3(self, content):
        return f"### {content}\n\n"
    
    def p(self, content):
        return f"{content}\n\n"
    
    def storeFile(self, content, filename):
        with open(filename+".md", 'w') as f:
            f.write(content)

        print(f"File {filename}.md written.")
        


class HtmlHandler(outputhandler):
    '''
    Gives helper methods to use HTML syntax.
    '''
    def __init__(self):
        pass

    def document(self, head, body):
        return f"<head>{head}</head><body>{body}</body>"
    
    def sectionWrap(self, content):
        return f"{content}"
    
    def h1(self, content):
        return f"<h1>{content}</h1>"
    
    def h2(self, content):
        return f"<h2>{content}</h2>"
    
    def h3(self, content):
        return f"<h3>{content}</h3>"
        
    def p(self, content):
        return f"<p>{content}</p>"
    
    def storeFile(self, content, filename):
        pass
    

class RevealJSHandler(outputhandler):
    '''
    Gives helper methods to use HTML syntax.
    '''
    def __init__(self):
        pass

    def document(self, head, body):
        html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"><title>Sechs Denkhüte</title><link rel="stylesheet" href="dist/reset.css"><link rel="stylesheet" href="dist/reveal.css"><link rel="stylesheet" href="dist/theme/beige.css"><link rel="stylesheet" href="plugin/highlight/monokai.css"></head><body><div class="reveal"><div class="slides">'
        html += '<section><form id="myForm"><label for="userInput">Enter something:</label><br><input type="text" id="userInput" name="userInput" style="width: 400px"><br><br><button type="submit">Submit</button></form></section>'
        html += '<section><h2>Bitte warten ...</h2></section>'
        html += f"{body}"
        html += '<script src="https://unpkg.com/reveal.js/dist/reveal.js"></script><script>Reveal.initialize(); document.getElementById("myForm").addEventListener("submit", function(e) { e.preventDefault(); const input = document.getElementById("userInput").value; fetch("/process", { method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({ userInput: input }) });Reveal.slide(1); // Move to second slide}); Reveal.on("slidechanged", function(event) { if (event.indexh === 1) { setTimeout(() => { Reveal.slide(2);}, 10000);}});</script>'
        html += "</div></div><script src='dist/reveal.js'></script><script src='plugin/highlight/highlight.js'></script><script>Reveal.initialize({hash: true, plugins: [RevealHighlight]});</script></body></html>"
        return html

    def sectionWrap(self, content):
        return f"<section>{content}</section>"
    
    def h1(self, content):
        return f"<h1>{content}</h1>"
    
    def h2(self, content):
        return f"<h2>{content}</h2>"
    
    def h3(self, content):
        return f"<h3>{content}</h3>"
        
    def p(self, content):
        return f"<p>{content}</p>"
    
    def storeFile(self, content, filename):
        working_directory = os.getcwd()
        with open(working_directory+"/src/sixthinkingchatbots_alexander.rachmann/reveal.js-master/"+filename+".html", 'w') as f:
            f.write(content)
        