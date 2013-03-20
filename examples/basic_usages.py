from datetime import date
from askme import Askme

terminal = Askme()

name = terminal.ask("<% cprint('Hello, World!', 'green', 'on_red') %>")

condition = terminal.ask("hi?where are you from:  ", default = "so nice", uppercase = True
                        ,validate="^[A-Z]{2}$")

birthday = terminal.ask("birthday?(year,month,day): ", date)

password = terminal.ask("password: ", echo = False)



print birthday
print password
print "the man %(name)s is from %(condition)s" % locals()
