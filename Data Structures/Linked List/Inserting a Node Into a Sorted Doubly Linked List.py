def sortedInsert(head, data):

    p = head
    q = head.next
    new_node = DoublyLinkedListNode(data)

    while p and q:
        if data <= p.data and p.prev is None:
            new_node.next = p
            p.prev = new_node
            head = new_node
            return head
        elif p.data <= data <= q.data:
            nxt = p.next
            p.next = new_node
            new_node.next = nxt
            nxt.prev = new_node
            new_node.prev = p
            return head
        elif p.data <= q.data <= data and q.next is None:
            q.next = new_node
            new_node.prev = q
            return head
        q = q.next
        p = p.next