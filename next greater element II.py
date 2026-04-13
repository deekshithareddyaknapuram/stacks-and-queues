def NGE(arr):
    st=[]
    n=len(arr)
    nge=[-1]*n
    for i in range(2*n-1,-1,-1):
        while st and st[-1]<=arr[i%n]:
            st.pop()
        if st:
            nge[i%n]=st[-1]
        st.append(arr[i%n])
    return nge
arr=list(map(int,input().split()))
print(NGE(arr))
    