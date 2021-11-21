with open('desktop/Labs Python/Lab 4/highscores.txt', 'r') as file:
    sorted_data=sorted(file.readlines(), 
                       key=lambda item: int(item.rsplit(':',1)[-1].strip()))

for i in range(int(len(sorted_data)/2)):
    b = sorted_data[i]
    sorted_data[i] = sorted_data[-1*i-1]
    sorted_data[-1*i-1] = b 

out = open('desktop/Labs Python/Lab 4/highscores2.txt', 'w')
for i in range(int(len(sorted_data))):
    out.write(sorted_data[i])
out.close()