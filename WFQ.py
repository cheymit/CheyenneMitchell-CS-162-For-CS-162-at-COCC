from collections import deque #imports deque (double ended queue)

# Option 1: Input as list
input_stream = [ #list of packet imputs. Each name come with a "priority" letter
    "S Mary", "P Dee", "P Dee", "E Eileen", "E Mike", "E Joe", "P Dee", "E Vicky",
    "E George", "P Dee", "P Joe", "E Sally", "P Joe", "S Pete", "P Dee",
    "S Bill", "S Chase", "E Price", "P Dee", "E Sue"
]

# Create 3 separate queues -- priority letters come from here P, S, E
premium_queue = deque() #holds packets that start with P
standard_queue = deque() #""" start with S
economy_queue = deque() #""" start with S

# Sort packets into appropriate queues
for packet in input_stream: #loop that goes through each packet
    priority = packet[0]
    if priority == 'P':
        premium_queue.append(packet)
    elif priority == 'S':
        standard_queue.append(packet)
    elif priority == 'E':
        economy_queue.append(packet)

# WFQ Function Weighted Fair Queuing
def weighted_fair_queuing(p_queue, s_queue, e_queue):
    output = []
    while p_queue or s_queue or e_queue:
        # Dequeue 3 Premium packets
        for _ in range(3):
            if p_queue:
                output.append(p_queue.popleft())
        # Dequeue 2 Standard packets
        for _ in range(2):
            if s_queue:
                output.append(s_queue.popleft())
        # Dequeue 1 Economy packet
        if e_queue:
            output.append(e_queue.popleft())
    return output

# calls WFQ
output_packets = weighted_fair_queuing(premium_queue, standard_queue, economy_queue)

#prints final output list
print("Dequeued Packet Order (WFQ):")
for packet in output_packets:
    print(packet)
