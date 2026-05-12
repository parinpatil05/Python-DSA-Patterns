class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous

        previous = current
        current = next_node

    return previous


def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next

    print("None")


# Creating linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original Linked List:")
print_list(head)

reversed_head = reverse_linked_list(head)

print("Reversed Linked List:")
print_list(reversed_head)
