def moore_01_detector(input_bits):
    state = 'A'  # Initial state
    output_map = {
        'A': 'b',
        'B': 'b',
        'C': 'a'
    }

    output = [output_map[state]]  # Output for initial state

    for bit in input_bits:
        if state == 'A':
            if bit == '0':
                state = 'B'
            else:
                state = 'A'

        elif state == 'B':
            if bit == '0':
                state = 'B'
            elif bit == '1':
                state = 'C'

        elif state == 'C':
            if bit == '0':
                state = 'B'
            else:
                state = 'A'

        output.append(output_map[state])

    return ''.join(output)
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
                state = 'C'
                output.append('a')  # Detected "01"

        elif state == 'C':
            if bit == '0':
                state = 'B'
                output.append('b')
            else:  # bit == '1'
                state = 'A'
                output.append('b')

    return ''.join(output)
inputs = ["011001", "01", "10", "1101" "110011"]

print("=== Mealy Machine ===")
for seq in inputs:
    print(f"Input:  {seq}")
    print(f"Output: {mealy_01_detector(seq)}\n")

print("=== Moore Machine ===")
for seq in inputs:
    print(f"Input:  {seq}")
    print(f"Output: {moore_01_detector(seq)}\n")  # remove first 'b' to align with Mealy

