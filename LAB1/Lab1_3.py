print('Lab1_3')

name = str(input('What is your name?\n'))
labGrade = float(input('Enter your Lab Grade : \n'))
midtermGrade = float(input('Enter your midterm grade : \n'))
finalGrade = float(input('Enter your final grade : \n'))

lab = labGrade / 4
midterm = (midtermGrade * 35) / 100
final = (finalGrade * 40) / 100
lastScore = lab + midterm + final

print("Name: " + name)
print("Lab : ", + lab)
print("Midterm : ", + midterm)
print("Final : ", + final)
print("Last Score : ", + lastScore)