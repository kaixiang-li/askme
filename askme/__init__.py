__version__ = (0, 0, 1)

import sys
from question import Question, QuestionError
import readline
from mako.template import Template
from system_extension import getch
from getpass import getpass
from termcolor import colored, cprint

class Askme(object):
    def __init__(self, input=sys.stdin, output=sys.stdout):
        self.input = input
        self.output = output

    def ask(self, question, answer_type = str, **configs):
        self.question = Question(question, answer_type)
        self.answer = ""
        for key, value in configs.iteritems():
            self.question.__dict__[key] = value

        if self.question.gather:
            return self.gather()

        self.say(self.question.question)
        # retry until the correct answer
        while True:
            try:
                self.answer = self.question.answer_or_default(self.get_response())
                self.answer = self.question.change_case(self.answer)
                self.__class__(self.input, self.output)
                self.question.update()
                if not self.question.valid_answer(self.answer):
                    self.explain_error("not_valid")
                    raise QuestionError()
                self.answer = self.question.convert(self.answer)
            except QuestionError:
                pass
            else:
                self.question = None
                break
        return self.answer

    def get_line(self):
        raw_answer = self.input.readline().strip('\n')
        return raw_answer


    def say(self, statement):
        statement = "<%! from termcolor import colored, cprint %>" + str(statement)
        # if statement ends with a whitespace before a color escape
        template = Template(statement)
        if statement:
            sys.stdout.write("%s" % template.render())
        else:
            sys.stdout.write("%s" % template.render())


    def get_response(self):
        if self.question.first_answer:
            return self.question.first_answer
        if self.question.echo == True:
            return self.get_line()
        else:
            line = ""
            while True:
                if self.question.echo == False:
                    line = getpass("")
                    break
                else:
                    self.output.write(self.question.echo)

                    character = getch()
                    character_code = ord(character)
                    # backspace or delete
                    if character_code == 127 or character_code == 8:
                        #line = line[:-1]
                        pass
                    else:
                        line += character
                    # carriage or newline
                    if character_code == 13 or character_code == 10:
                        break
            return self.question.change_case(line)

    def explain_error(self, error):
        self.say(self.question.responses[error]) if error else None

