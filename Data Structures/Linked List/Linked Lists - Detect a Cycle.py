def has_cycle(head):
    
    curr = head
    valList = []
    while curr:
        if curr not in valList:
            valList.append(curr)
            curr = curr.next
        else:
            return True
    return False