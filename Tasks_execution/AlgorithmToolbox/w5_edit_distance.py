# Uses python3   

def edit_distance(a, b):
    m = len(b) + 1
    n = len(a) + 1

    import numpy as np
    D = np.zeros((n, m), dtype=int)
    
    for i in range(n):
        D[i, 0] = i

    for j in range(m):
        D[0, j] = j

    for j in range(1, m):        
        for i in range(1, n):
            if a[i-1] == b[j-1]:
                D[i, j] = D[i - 1, j - 1]
            else:
                D[i, j] = D[i - 1, j - 1] + 1

            if D[i, j - 1] + 1 < D[i, j]:
                D[i, j] = D[i, j - 1] + 1

            if D[i - 1, j] + 1 < D[i, j]:
                D[i, j] = D[i - 1, j] + 1

    return D[n-1, m-1]
            




if __name__ == '__main__':
    a = str(input())
    b = str(input())
    
    #a = "editingasdvsdvsdavfsawdrgfwerewrwrghrtheyjhbrtnj67ukkkkkktyltyltyltyltylmujirejbswrgovijewrgrgwerigjvoijewrgwogrjvreiwjogivjewrgiqjergjribthnj;tykjnltkewjeroqwwnerovqwnevohnerogbnj4woiyhw"
    #b = "distancedrcfjwerjgveir5jgbwrjegbtjmohiprnjotihnjrmeothnimjreothnimerojihmreothjreothjmorethjormehjoejpotmhirjeotmhirjemnoyiwjerhouchegqregportihpyjinprtipmemouwhmvuigwquig"
    
    print(edit_distance(a, b))
