from collections import deque

def manage_delivery_queue():
    try:
        delivery_queue = deque(["order_1", "order_2", "order_3", "order_4", "order_5",])
        delivery_queue.append("order_6")
        delivery_queue.appendleft("order_0")
        delivery_queue.pop()
        delivery_queue.popleft()

        return delivery_queue

    except Exception as ex:
        print(ex)

queue = manage_delivery_queue()
print(queue)