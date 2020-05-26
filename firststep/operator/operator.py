superToto = False
cumul = 0

#if elif else
if bool(superToto):
    print('superToto is true')
elif bool(superToto) is False:
    print('superToto is not !')
else:
    print('dafuk')

# while
while cumul is not 5:
  cumul += 1
  print(cumul)

while True:
  print("Type the best number to continue : ")
  responseFromUser = input()

  if(responseFromUser % 8 == 0):
      print("YES ! You are free.")
      break
  else:
      print("This is not the best number at all")

# for
for x in range(5):
  print(x)