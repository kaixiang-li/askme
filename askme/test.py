from __init__ import Askme


terminal = Askme()

condition = terminal.ask("hi?where are you from:  ", default = "so nice",
                        validate="^[A-Z]{2}$", uppercase = True )
name = terminal.ask("hi?what's your name:  ")

password = terminal.ask("password: ", echo = "*")


print "the man %(name)s is from %(condition)s, %(password)s" % locals()
