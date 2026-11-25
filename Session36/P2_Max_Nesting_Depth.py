def Max_Nesting_Depth(str):
    n=len(str)

    maxDepth=0
    depth=0

    for i in range(n):
        curr=str[i]

        # Case 1 : Openining Bracket
        if curr=='(':
            depth+=1
            maxDepth=max(depth,maxDepth)

        # Case 2 : Closing Bracket
        elif curr==')':
            depth -=1

    return maxDepth

str = "(1+(2*3)+((8)/4))+1"

print(Max_Nesting_Depth(str))
