class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def cr_lkd_lst(lst_values):
    lst_head = None
    lst_current = None

    for value in lst_values:
        if lst_head is None:
            lst_head = Node(value)
            lst_current = lst_head
        else:
            lst_current.next = Node(value)  # type: ignore
            lst_current = lst_current.next  # type: ignore

    return lst_head


def rvrse_lkd_lst(rvr_head):
    previous = None
    rvr_current = rvr_head

    while rvr_current:
        rvr_current.next, previous, rvr_current = previous, rvr_current, rvr_current.next

    return previous


print("---------------------------------Welcome to Linked list Process---------------------------------")
print("-------------Here you can reverse the numbers that have been given as input by user-------------")
# Getting the number of test cases from the user
test_cases = int(input("Enter the number of test cases: "))

# Processing each test case
for _ in range(test_cases):
    print("-----")
    # Creating a linked list from user input
    values = list(
        map(int, input("Enter space-separated values for the linked list: ").split()))
    head = cr_lkd_lst(values)
    # Reversing the linked list
    reversed_head = rvrse_lkd_lst(head)

    # Printing the reversed linked list
    current = reversed_head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
