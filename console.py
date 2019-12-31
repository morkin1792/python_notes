from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

#https://python-prompt-toolkit.readthedocs.io/en/master/pages/asking_for_input.html#history
class Console():

    def __init__(self):
        self.session = PromptSession()
        self.prompt = self.session.prompt
        self.PS1="h~ "

    def readinput(self):
        html_completer = WordCompleter(['<html>', '<body>', '<head>', '<title>'])
        answer = self.prompt(self.PS1, completer=html_completer)
        # print('pegou ' + answer)
        
    
if __name__ == '__main__':
    c = Console()
    while True:
        c.readinput()
    
    