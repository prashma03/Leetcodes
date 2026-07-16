class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def count_nodes(head):
    count = 0

    while head:
        count += 1
        head = head.next

    return count
