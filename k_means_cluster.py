import random
import matplotlib.pyplot as plt
import numpy as np

def read_txt(fn):
    with open(fn) as f:
        lines =  [[eval(v) for v in t.strip().split(" ")[1:]] for t in f.readlines()]
    return lines

#kmeans funcs go here

def centroid(points: list()):
    return [sum(x)/len(x) for x in zip(*points)]

def distance(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)
    
def error(points: list(), centerp: list()): 
    f = {tuple(p):[] for p in centerp}
    for x in points:
        y = []
        for p in centerp: 
            y.append((p,distance(x,p),x))
        tempMin = min((yh for yh in y), key=lambda yh:yh[1])
        f[tuple(tempMin[0])].append(tempMin[2])
    return f
   
def kmeans(data: dict(), k): #{1: [x,y], [x,y], 2: [x,y]}
    starters = []
    for i in range(k):
        starters.append((random.randrange(0,1000000)/1000000, random.randrange(0,1000000)/1000000))
    
    last = None
    new = error(data, starters)
    while last != new: 
        centroids = []
        for cen, pts in new.items():
            cen = centroid(pts)
            if len(cen)==0:
                centroids.append([0.5,0.5])
            else:
                centroids.append(cen)
        last = new
        new = error(data, centroids)
    #plot(data,new.keys())
    return new    

def plot(data, centers):
    e = error(data, centers)
    for cen, pts in e.items():
        x = [d[0] for d in pts]
        y = [d[1] for d in pts]
        col = (np.random.random(),np.random.random(),np.random.random())
        plt.scatter(x,y,c=col, marker=".")    
        plt.scatter(cen[0],cen[1], c=col, s=60, marker="*")

    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.show()
    
def main(data, points):
    ref = {}
    for c,pts in enumerate(points.keys()):
        ref[pts] = c
    for d in data:
        for cen, pts in points.items():
            if d in pts:
                print(ref[cen])
    
if __name__=="__main__":
    data = read_txt("example_inputs.txt")
    cluster = kmeans(data,2)
    main(data, cluster)
