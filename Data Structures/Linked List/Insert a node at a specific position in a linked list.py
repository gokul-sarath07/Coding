def insertNodeAtPosition(head, data, position):
	
    node = SinglyLinkedListNode(data)
    count = 0
    curr = head
    prev = 0

    if head is None:
        head = node
        return head

    while curr and count != position:
        count += 1
        prev = curr
        curr = curr.next
    
    if not curr:
        return head
    
    prev.next = node
    node.next = curr
    return head