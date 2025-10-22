

def mealy_01_detector(input_bits):
    state = 'A'  # initial state
    output = []

    for bit in input_bits:
        if state == 'A':
            if bit == '0':
                state = 'B'
                output.append('b')
            else:  # bit == '1'
                state = 'A'
                output.append('b')

        elif state == 'B':
            if bit == '0':
                state = 'B'
                output.append('b')
            elif bit == '1':
                state = 'A'  
                output.append('a')  #

    return ''.join(output)


# Test examples
inputs = ["011001",  "010101", "000111"]

for seq in inputs:
    print(f"Input:  {seq}")
    print(f"Output: {mealy_01_detector(seq)}\n")
