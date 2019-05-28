# [],(),{}
# we have to find if opening parenthesis is closed or not 

def paren_balance(s):

    # check if string is even number or not
    # if it's odd then its impossible to balance

    if(len(s)%2 != 0):
        return ("parenthesis is not even number")

    # we define opening parens
    opening=set('([{')
    matches=set([ ('(',')'), ('[',']'),('{','}') ] )

    # now we put opening parens in stack

    stack=[]

    for paren in s:

        if paren in opening:
            stack.append(paren)
        else:

            if len(stack)==0:
                return False

            last_open=stack.pop()
            
            if (last_open,paren) not in matches:
                return False

    return len(stack)==0 



print(paren_balance('[{)}'))