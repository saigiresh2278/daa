import heapq

# Input
n = 4
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]
encoded_string = '1101100111110'

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

# Function to decode the Huffman encoded string
def decode_huffman(encoded_string, huffman_tree):
    decoded_string = ""
    node = huffman_tree
    for digit in encoded_string:
        if digit == '0':
            node = node[0]
        else:
            node = node[1]
        if isinstance(node, str):
            decoded_string += node
            node = huffman_tree
    return decoded_string

# Decode the encoded string using the Huffman Tree
decoded_string = decode_huffman(encoded_string, huffman_tree)

# Output the decoded string
print(decoded_string)  # Expected output: "abacd"
