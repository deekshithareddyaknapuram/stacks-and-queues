def NSE(arr):
    st=[]
    n=len(arr)
    nse=[-1]*n
    for i in range(n-1,-1,-1):
        while st and st[-1]>arr[i]:
            st.pop()
        if st:
            nse[i]=st[-1]
        st.append(arr[i])
    return nse
arr=list(map(int,input().split()))
print(NSE(arr))