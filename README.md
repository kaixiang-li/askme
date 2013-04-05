# Askme

Don't use it now, I haven't finished it yet.

## API

**the unfinished goal comes first...**

Basic usage:
```python
agent = Askme()
agent.ask("Hi?Are you happy tonight: ", default = "Of course I'm happy") 
```

You can do validation:
```python
agent.ask("So..which country are you from? ", uppercase = True,
          validate = "^[A-Z]{2}$")
```

You can get a password without worry:
```python
agent.ask("input your password, but don't let me know it: ", echo = False)
```

And Askme can help you handle type correctly either:
```python
from datetime import date
agent.ask("tell me your birthday baby: ", date)
```

More, you can have mako templates embebbed(cprint is included internally)
```python
name = terminal.ask("<% cprint('Hello, World!', 'green', 'on_red') %>")
```


## LICENSE
MIT







