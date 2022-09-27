import heapq


class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HeapNode):
            return False
        return self.freq == other.freq


def make_frequency_dict(symbols):
    frequency = {}
    for character in symbols:
        if character not in frequency:
            frequency[character] = 0
        frequency[character] += 1
    return frequency


class HuffmanCoding:
    def __init__(self, probabilities):
        self.probabilities = probabilities
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def generate_huffman_code(self):

        frequency = make_frequency_dict(self.probabilities)
        self.make_heap(frequency)
        self.merge_nodes()
        self.make_codes()
        return self.codes

    def make_heap(self, frequency):
        for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)


# with open('input.txt') as file:
#     data = file.read().strip().replace('\n', ' ').split(' ')
# HuffmanCoding(data).generate_huffman_code()

def get_huffman_result(cond: list):
    return HuffmanCoding(cond).generate_huffman_code()
