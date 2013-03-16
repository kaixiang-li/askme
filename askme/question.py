import re
class QuestionError(Exception): pass

class Question(object):
    '''One "option" to be passed into an ArgumentParser.'''
    def __init__(self, question, answer_type=None):
        # initialize question data
        self.question = question
        self.answer_type = answer_type

        # some configs
        self.default = None
        self.uppercase = None
        self.lowercase = None
        self.gather = False
        self.echo = False
        self.first_answer = None
        self.confirm = False
        self.validate = None
        self.reponses = {}

    def answer_or_default(self, answer_string):
        if answer_string:
            return answer_string
        else:
            return self.default

    # convert the type
    def convert(self, answer_string):
        if answer_type == None:
            return answer_string
        elif answer_type == str:
            return str(answer_string)
        elif answer_type == int:
            return int(answer_string)

    def valid_answer(self, answer_string):
        if self.validate:
            pattern = re.compile(self.validate)
            return pattern.match(answer_string)
        else:
            return True

    def build_responses(self):
        return {}

    def update(self):
        if self.default:
            self.question = self.question + "(default:" + self.default  +"): "

    def change_case(self, answer_string):
        if self.uppercase:
            return answer_string.upper()
        elif self.lowercase:
            return answer_string.lower()
        else:
            return answer_string



