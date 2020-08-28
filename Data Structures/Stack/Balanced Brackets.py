import os

def match(p1,p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False 

def isBalanced(s):

    stack = []
    index=0
    is_balanced = True

    while index < len(s) and is_balanced:
        paren = s[index]
        if paren in "([{":
            stack.append(paren)
        else:
            if stack == []:
                is_balanced = False
            else:
                top = stack.pop()
                if not match(top,paren):
                    is_balanced = False
        index+=1
    
    if stack == [] and is_balanced:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()