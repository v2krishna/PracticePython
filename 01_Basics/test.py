f = open('squares2.txt','w')
for i in range(1,21):
    f.write(f'the square of {i} is {i*i}\n')
f.close()
