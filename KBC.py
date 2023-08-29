# print('''What is the capital of India
#          a)Mumbai  b)Delhi
#          c)Chennai d)Jaipur''')
# user = input()
# if user=="Delhi":
#   print("7 crore")
# else:
#   print("Aap is game se bahr hogye hai")

tupleq = ("Capital","Longest River","Pink City","Most prayed Diety", "Richest Man")
tupleans=("Delhi","Brahmaputra","Jodhpur",'Krishna','Ambani')
tupleopt=('''a)Mumbai       b)Delhi
c)Chennai      d)Jaipur''',
          '''a)Ganga        b)Yamuna
c)Brahmaputra  d)Kaveri''',
          '''a)Jodhpur      b)Jaipur
c)Manali       d)Lucknow''',
          '''a)Shiva        b)Rama
c)Hanuman      d)Krishna''',
          '''a)Ratan Tata   b)Narendra Modi
c)Ambani       d)Indira Gandhi''')

for n in range(5):
  print("What is the "+tupleq[n]+" of India")
  print(tupleopt[n])
  
  ans=input()
  if ans==tupleans[n]:
     print("\n7 crore\n")
  else:
    print("Aap is game se bahr hogye hai")
    break
  if n<4:
    print("Agle Sawaal ki taraf badhte hai\n")