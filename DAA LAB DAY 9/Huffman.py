import heapq

# Input
n = 4
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]

# Create a priority queue using heapq
priority_queue = [(freq, char) for char, freq in zip(frequencies, characters)]
heapq.heapify(priority_queue)

# Build the Huffman Tree
while len(priority_queue) > 1:
    freq1, left = heapq.heappop(priority_queue)
    freq2, right = heapq.heappop(priority_queue)
    heapq.heappush(priority_queue, (freq1 + freq2, (left, right)))

# The final element in the priority queue is the root of the Huffman Tree
huffman_tree = heapq.heappop(priority_queue)[1]

# Function to generate Huffman Codes
def generate_codes(node, prefix="", codebook={}):
    if isinstance(node, str):
        codebook[node] = prefix
    else:
        left, right = node
        generate_codes(left, prefix + "0", codebook)
        generate_codes(right, prefix + "1", codebook)
    return codebook

# Generate the Huffman Codes
huffman_codes = generate_codes(huffman_tree)

# Output the Huffman Codes in the desired format
output = [(char, huffman_codes[char]) for char in characters]
print(output)  # Expected output: [('a', '110'), ('b', '10'), ('c', '0'), ('d', '111')]
