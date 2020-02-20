import re
def count(txtFile):
  list=open(txtFile,'r')
  sum=0
  with open('skychallenge_accounting_input.txt') as file:
      for line in file:
          for i in re.findall(r'\d+', line):
              z=int(i)
              sum+=z
  print(sum)
