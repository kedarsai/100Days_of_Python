import random
op=0
for i in range(10000):
    result = random.randint(0,1)
    op=op+result
if op>5000:
    print('heads')
else:
    print('trails')