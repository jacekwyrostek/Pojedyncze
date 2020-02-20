def checkPhrase(txtFile):
  list=open(txtFile,'r')
  x=0
  for line in list:
      duplicates=False
      line=line.rstrip()
      print(line)
      line2=line.split(' ')
      count=0
      for word in line2:
          count=line2.count(word)
          if count > 1:
              duplicates=True
      if duplicates:
          x+=1
      print('duplicate='+str(duplicates))
      print('='*20)
  print(x)
