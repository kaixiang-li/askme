__version__ = (1, 3, 0)

import sys
from option import Option
from command import Command, CommandError
from application import Application, ApplicationError
from question import Question, QuestionError
import readline
from mako.template import Template
from system_extension import getch

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
        try:
            self.answer = self.question.answer_or_default(self.get_response())
            self.answer = self.question.change_case(self.answer)
            self.__class__(self.input, self.output)
            self.question.update()
            if not self.question.valid_answer(self.answer):
                self.explain_error("not valid")
                raise QuestionError()
            self.answer = self.question.covert(self.answer)
        except:
            pass
        else:
            self.question = None
        return self.answer

    def say(self, statement):
        statement = str(statement)
        if statement:
           template = Template(statement)
           self.output.write(template.render())
        else:
            return


    def get_response(self):
        if self.question.first_answer:
            return self.question.first_answer
        else:
            line = ""
            character = getch()
            while True:
                character_code = ord(character)
                if not self.question.echo:
                    self.say(character)
                else:
                    self.say(self.question.echo)
                # carriage or newline
                if character_code == 13 or character_code == 10:
                    break
                # backspace or delete
                if character_code == 127 or character_code == 8:
                    break;
                else:
                    if not self.question.echo:
                        line += character
                    else:
                        line += self.question.echo
                character = getch()
            print line
            return line


    def explain_error(self, error_report):
        print error_report
        return error_report

