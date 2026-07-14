def reverseList(head):
    prev = None
    current = head

    while current:
        next_node = current.next   # Save where to go next
        current.next = prev        # Reverse the arrow
        prev = current             # Move prev forward
        current = next_node        # Continue with saved node

    return prev
