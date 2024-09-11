import random

clean = 0
totol_move = 0

for x in range(10):
    tile1 = random.randint(0,1)
    tile2 = random.randint(0,1)
    
    # here i consider clean==0 and dirty==1
    if tile1==1:
        clean = clean + 1
    
    if tile2==1:
        clean = clean + 1
        totol_move = totol_move + 1
    
print("total move = ",totol_move);
print("clean = ",clean);
print("performance = ",(clean/totol_move)*100,"%");