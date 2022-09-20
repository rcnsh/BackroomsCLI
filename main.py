from levels.Level0 import level0

healthFile = open("./profileData/health.txt", "w")
healthFile.write("100")
healthFile.close()

noclipFile = open("./profileData/noclip.txt", "w")
noclipFile.write("3")
noclipFile.close()

nameFile = open("./profileData/name.txt", "w")
ageFile = open("./profileData/age.txt", "w")

name = input("Please enter your name: ")
nameFile.write(name)
nameFile.close()

age = input("Please enter your age: ")
ageFile.write(age)
ageFile.close()

almondFile = open("./profileData/almondWater.txt", "w")
almondFile.write("0")
almondFile.close()

level0()
