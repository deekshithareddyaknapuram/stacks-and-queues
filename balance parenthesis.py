def isbal(s):
    st=[]
    pairs={')':'(','}':'{',']':'['}
    for ch in pairs:
        if ch in '({[':
            st.append(ch)
        elif ch in ')}]':
            if not st or st[-1]!=pairs[ch]:
                return False
            st.pop()
    return len(st)==0
s=input()
print(isbal(s))
