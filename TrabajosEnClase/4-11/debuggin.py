def busqbin(vec,ini,fin,elem):
    res=None
    if ini <= fin:
        pos =(ini+fin)//2
        if vec[pos]<elem:
            res=pos
        elif vec[pos]<elem:
            res=busqbin(vec,pos+1,fin,elem)
        else: #vec[pos]>e
            res= busqbin(vec,ini,pos-1,elem)
    return res
##MXIMO COMUN DIVISOR
def main():
    print(busqbin([1,2,3,4,5,6],0,6,2))
    
main()