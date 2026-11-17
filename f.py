import random
x=y=0;pts=[]
for i in range(60000):
    r=random.random()
    if r<.01:x,y=0,.16*y
    elif r<.86:x,y=.85*x+.04*y,-.04*x+.85*y+1.6
    elif r<.93:x,y=.2*x-.26*y,.23*x+.22*y+1.6
    else:x,y=-.15*x+.28*y,.26*x+.24*y+.44
    pts.append((x,y))
s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="-3 -0.3 6 10.3"><rect x="-3" y="-1" width="6" height="12" fill="#10201a"/>'
for k,(a,b) in enumerate(pts[100:]):
    s+='<circle cx="%.3f" cy="%.3f" r=".02" fill="hsl(%d,60%%,%d%%)"/>'%(a,10-b,100+b*8,35+b*3)
open('f.svg','w').write(s+'</svg>')
