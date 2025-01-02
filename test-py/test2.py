

def calcul_mul(nb : int, lev : int):
    for i in range(lev):
        print(nb, "x" ,i , "=" , nb*i)
        

def main():
    '''
        Function main()
    '''
    calcul_mul(8, 12)
    
main()