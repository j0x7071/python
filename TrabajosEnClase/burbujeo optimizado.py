#burbujeo / bubble sort

def burbujeo (l):
    n= len(l)#n=5
    i=0
    intercambio=True
    while i< n and intercambio:
        intercambio=False
        for i in range(n):#i 0..4
            print("soy i==>",i,"y asi va la lista2",l)
        
            # Desde la primera posición hasta la anteúltima        
            for j in range(0,n-i-1):#j 0..3
                print("soy jota==>",j,"y asi va la lista2",l)
            #comparo adyacentes e intercambio desordenados
                if l[j]> l[j+1]:
                    l[j], l[j+1]=l[j+1],l[j]
                    #a,b=b,a
                    intercambio=True
            i += 1
    return l

def main():
    
    #lista= [1,2,3,4,5]
    #listaalreves=lista[::-1]
    lista2=[4,10,1,2,11]
    print(burbujeo(lista2))
    print(lista2)

    
main()