from numpy import random

logic = 0
holder = 0

enc = open("encryptkey.txt", "w")
enc.close()
enc = open("encryptkey.txt", "a")

#nums for enc
while logic < 27:
  writing = str(random.randint(0, 9))
  enc.write(writing)
  enc.flush()
  logic += 1

enc = open("encryptkey.txt", "r")

alph = {
  "a": enc.read(1),
  "b": enc.read(2),
  "c": enc.read(3),
  "d": enc.read(4),
  "e": enc.read(5),
  "f": enc.read(6),
  "g": enc.read(7),
  "h": enc.read(8),
  "i": enc.read(9),
  "j": enc.read(10),
  "k": enc.read(11),
  "l": enc.read(12),
  "m": enc.read(13),
  "n": enc.read(14),
  "o": enc.read(15),
  "p": enc.read(16),
  "q": enc.read(17),
  "r": enc.read(18),
  "s": enc.read(19),
  "t": enc.read(20),
  "u": enc.read(21),
  "v": enc.read(22),
  "w": enc.read(23),
  "x": enc.read(24),
  "y": enc.read(25),
  "z": enc.read(26),
  " ": enc.read(27)
}


enc.close()




type = input("What is the data type? (text or file?) ")
if type == "text":
  stuff = input("What is the text to encrypt ")
  stufflen = len(stuff)
  output = open("message.txt", "w")
  output = open("message.txt", "a")
  while holder < stufflen: 
    value = stuff[(holder)]
    writer = alph[value]
    writer = str(writer)
    print(writer)
    output.write(writer)
    output.flush()
    holder = holder + 1
output.close()
