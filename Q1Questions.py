filehandle = open("testFile.txt",'w')
Question = input("What is your question?" )
filehandle.write(Question +'\n')
for i in range (4):
answer = input ("Options:")
filehandle.write(answer +'\n')
answer = input("Correct answer?")
filehandle.write(answer +'\n')
filehandle.close()
