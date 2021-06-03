from datetime import date

with open('path/to/infile') as infile, open('path/to/outfile', 'w') as outfile:
    for line in infile:
        if line.startswith(("Name", "birthDate", "----")):
            outfile.write(line)

def calculateAge(birthDate):
	today = date.today()
	age = today.year - birthDate.year -	((today.month, today.day) <
		(birthDate.month, birthDate.day))

	return age

print(calculateAge(date(line.birthDate)), "years")

	
def cal_average(age):
    sum_age = 0
    for t in age:
        sum_age = sum_age + t           

    avg = sum_age / len(age)
    return avg

