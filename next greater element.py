def NGE(arr):
    st=[]
    n=len(arr)
    nge=[-1]*n
    for i in range(n-1,-1,-1):
        while st and st[-1]<=arr[i]:
            st.pop()
        if st:
            nge[i]=st[-1]
        st.append(arr[i])
    return nge
arr=list(map(int,input().split()))
print(NGE(arr))