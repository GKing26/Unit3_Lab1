#Griffin King
# Unit 3 Lab 1
# Thingy thingy thing do thiny with a while loop no loop recursion

def while_substitute(num):
  returningNum = num
  while num >= 1:
    print(f"Recursing; num = {num}")
    num -= 1
  print("\nBASE CASE REACH\n")
  while num < returningNum:
    num += 1
    print(f"Returning; num = {num}")
while_substitute(5)
