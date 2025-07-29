name = input('What is your name? ')
color = input('Which is your favorite color? ')

if len(name) and len(color) > 0:
  print(f"Hello, {name}! Your favorite color, {color}, is awesome!")
else:
  print('Please use valid name and color.')