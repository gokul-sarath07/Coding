def findMergeNode(head1, head2):
	
    p = head1
    q = head2
    val1 = []

    while p:
        val1.append(p)
        p = p.next
    while q:
        if q in val1:
            return q.data
        else:
            q = q.next