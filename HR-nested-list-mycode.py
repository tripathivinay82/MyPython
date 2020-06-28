
#Actual Input: [['V1', 1.0], ['V2', 4.0], ['V3', 2.0]]

if __name__ == '__main__':
        arr=[[input(),float(input())] for _ in range(int(input()))]
        name=[n[0] for n in arr]
        score=[s[1] for s in arr]
        print(f"score is {score}")
        #s1=sorted(set(score))
        #print(f"s1 is {s1}")
        #s1=list(s1)
        #s2=s1[-2]
        s2=sorted(set(score))[1]
        print(f"s2 is {s2}")
        j=0
        c=[]
        for i in score:
            if i == s2:
                c.append(j)
            j=j+1        
        k=0
        print(f"c is {c}")
        c.sort(reverse=True)
        print(f"sorted c is {c}")
        for k in c:
            print(name[k])


            
        