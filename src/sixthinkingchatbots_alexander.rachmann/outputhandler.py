from abc import ABC

class outputhandler(ABC):
    ''' Defines only the interface of the subclasses.
    '''
    def __init__(self):
        pass

    def document(self, head, body):
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
    
    def h1(self, content):
        return f"<h1>{content}</h1>"
    
    def h2(self, content):
        return f"<h2>{content}</h2>"
    
    def h3(self, content):
        return f"<h3>{content}</h3>"
        
    def p(self, content):
        return f"<p>{content}</p>"
        