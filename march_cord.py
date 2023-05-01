import win32ui
from pypresence import Presence
from time import sleep, time

def wrap(id): # JIC discord isnt open
  app = None
  while not app: # loop if no app
    try: app = Presence(id)
    except: sleep(15) # zZ
  return app


def is_honkai():
  try: win32ui.FindWindow('Qt5QWindowIcon', 'Star Rail') # Qt5QWindowIcon = honkai star rail window
  except win32ui.error: return False # if not found ;-;
  return True # if found ;)

def _(mod):
  honkai = is_honkai()
  if (not honkai) and (mod):
    app.close() # close app
    return False # mod = False
  if (honkai) and (not mod):
    app.connect() # connect app
    app.update(large_image='honkai', start=time()) # update uwO
    return True # mod = True

  return mod # return mod

app = wrap('1040182356092395550') # app id
mod = False

while 'mod': # inf loop
  try: mod = _(mod)
  except: mod = False # if discord closes ;-;
  sleep(15) # zZ 
  
