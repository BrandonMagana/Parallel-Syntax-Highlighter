from constants import OPERATORS
from Token_Splitter.token_splitter_helper import *

class Token_Splitter:
    def __init__(self, lines):
        self.lines = lines
        self.tokens = ""


    def split(self):
        tokens = []
        for line in self.lines:
            #Check if line has a comment
            comment_index = line_has_a_comment(line)

            #If is a comment divide token in two: before and after comment has been found
            if comment_index != -1:
                before_comment = line[:comment_index]
                comment = line[comment_index:]

                if before_comment != "": 
                    new_line = separate_line_by_operators(before_comment)
                    tokens += new_line.split()
            
                tokens.append(comment)

            else:
                new_line = separate_line_by_operators(line)
                tokens += new_line.split()
        self.tokens = tokens
        return tokens