#burbujeo / bubble sort

def burbujeo (l):
    n= len(l)#n=5
    i=0
    s=[1]
    t=[2]
    while i< n or s!=t:
        for i in range(n):#i 0..4
            t=l
            print("SOY t",t)
            
            print("soy i==>",i,"y asi va la lista2",l)
            # Desde la primera posición hasta la anteúltima        
            for j in range(0,n-i-1):#j 0..3
                s=l
                print("soy jota==>",j,"y asi va la lista2",l)
            #comparo adyacentes e intercambio desordenados
                if l[j]> l[j+1]:
                    l[j], l[j+1]=l[j+1],l[j]
                    #a,b=b,a
                    print("SOY S",s)
            i += 1
    return l

def main():
    
    #lista= [1,2,3,4,5]
    #listaalreves=lista[::-1]
    lista2=[4,10,1,2,11]
    print(burbujeo(lista2))
    print(lista2)

    
main()
