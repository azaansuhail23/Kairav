def isValid_Parenthesis(str):
    n = len(str)

    stack = []

    for i in range(n):
        curr = str[i]

        # Case 1 : Opening Bracket
        if curr == "(" or curr == "{" or curr == "[":
            stack.append(curr)

        # Case 2 : Closing Bracket
        else:
            if len(stack)==0:
                return False
            
            peek = stack[-1]
            
            #valid pair
            if (curr==')' and peek=='(' 
                    or 
                curr=='}' and peek=='{' 
                    or
                curr==']' and peek=='['):
                    stack.pop()
                
    return len(stack)==0

str="([)]{}"

print(isValid_Parenthesis(str))