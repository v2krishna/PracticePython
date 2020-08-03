import pickle

##d = {'id':1000, 'age':23, 'name':'krishna', 'sal':1000.00}
##f = open('serialize.pkl','wb')
##pickle.dump(d,f)
##f.close()
##

##f = open('serialize.pkl','rb')
##d1 = pickle.load(f)
##print(d1)
##f.close()

f = open('squares2.pkl','wb')
for i in range(1,201):
    pickle.dump(f'the square of {i} is {i*i}\n', f)
f.close()
