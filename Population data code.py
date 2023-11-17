import random
import pandas as pd
[w1,w2,w3,w4] = [0.25,0.25,0.25,0.25,0.25]
vals = []
for i in range(1000000):
    x1 = random.randint(1, 100)
    x2 = random.randint(1, 5)
    x3 = random.randint(1, 130)
    x4 = random.randint(0, 70)
    x5 = random.randint(1, 100)
    eq = w1*x1+w2*x2+w3*x3+w4*x4+w5*x5
    vals.append([x1,x2,x3,x4,x5,eq])
df = pd.DataFrame(vals,columns=['SPARE PARTS AVAILABILITY','DESIGN','COST','MILAGE','SATISFACTORY RATE','CUSTOMER DATA ANALYSIS'])
pipdf.to_csv('productivity.csv',index=False)