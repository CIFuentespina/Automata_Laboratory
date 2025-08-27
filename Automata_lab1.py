# Question 1 DFA
# Language: strings of the form a 1* b 0* 1+
def dfa1(string):
    state = "q0"
    for ch in string:
        if state == "q0":
            if ch == "a":
                state = "q1"
            else:
                return False   #  must start with 'a'
        elif state == "q1":
            if ch == "1":
                state = "q1"
            elif ch == "b":
                state = "q2"
            else:
                return False   #  only '1' or 'b' allowed
        elif state == "q2":
            if ch == "0":
                state = "q2"
            elif ch == "1":
                state = "q3"
            else:
                return False   #  only '0' or '1' allowed
        elif state == "q3":
            if ch == "1":
                state = "q3"
            else:
                return False   #  only '1' allowed
    return state == "q3"   #  accepted only if ending in q3


# Question 2 DFA
# Language: accepts strings that end in q0 (loop back to start)
def dfa2(string):
    state = "q0"
    for ch in string:
        if state == "q0":
            state = "q1" if ch == "a" else "q2" if ch == "b" else None
        elif state == "q1":
            state = "q0" if ch == "a" else "q3" if ch == "b" else None
        elif state == "q2":
            state = "q3" if ch == "a" else "q0" if ch == "b" else None
        elif state == "q3":
            state = "q2" if ch == "a" else "q1" if ch == "b" else None
        if state is None:
            return False   #  invalid symbol
    return state == "q0"   #  accepted only if ending in q0


if __name__ == "__main__":
    # --- Test cases for Question 1 ---
    print("Question 1 (DFA1) Tests:")

    #ACCEPTED IN QUESTION 1
    accepted_q1 = ["ab1", "a111b000111", "ab0001111"]


     #REJECTED IN QUESTION 1
    rejected_q1 = ["a", "ab0", "b01"]

    for t in accepted_q1:
        print(f"{t}: {dfa1(t)}  (Accepted)")
    for t in rejected_q1:
        print(f"{t}: {dfa1(t)}  (Rejected)")

    # --- Test cases for Question 2 ---
    print("\nQuestion 2 (DFA2) Tests:")
    #ACCEPTED IN QUESTION 2
    accepted_q2 = ["aa", "bb", "abba"]

      #REJECTED IN QUESTION 2
    rejected_q2 = ["a", "b", "ab"]

    for t in accepted_q2:
        print(f"{t}: {dfa2(t)}  (Accepted)")
    for t in rejected_q2:
        print(f"{t}: {dfa2(t)}  (Rejected)")
