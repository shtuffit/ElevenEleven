from time import sleep, time

#Define segment display patterns
representations = {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    ':': ('   ', ' # ', '   ', ' # ', '   '),
}

def seven_segment(number):
    # treat the number as a string, since that makes it easier to deal with
    # on a digit-by-digit basis
    digits = [representations[digit] for digit in str(number)]
    # now digits is a list of 5-tuples, each representing a digit in the given number
    # We'll print the first lines of each digit, the second lines of each digit, etc.
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))

counter = 671 #11:11
while counter >= 0:
  start = time()
  # Clear the terminal
  print(chr(27) + "[2J")
  #Current minutes and seconds to seven segment
  minutes = str(counter//60).zfill(2)
  seconds = str(counter%60).zfill(2)
  seven_segment(f"{minutes}:{seconds}")
  counter -= 1
  #Sleep for 1 second minus the forloop iteration time 
  sleep(1-(time()-start))
