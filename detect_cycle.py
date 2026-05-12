class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Creating linked list with cycle
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)

head.next = second
second.next = third
third.next = fourth
fourth.next = second

print("Cycle Detected:", has_cycle(head))
