def minimize_dfa(states, alphabet, transitions, start_state, accept_states):
    # Step 1: Split states into two sets - accept and non-accept
    accept_set = set(accept_states)
    non_accept_set = set(states) - accept_set

    # Step 2: Initialize the partition with the two sets
    partition = [accept_set, non_accept_set]

    # Step 3: Initialize the list of equivalence classes
    equivalence_classes = [accept_set, non_accept_set]

    # Step 4: Iterate until no more refinements are possible
    while True:
        new_partition = []

        for equivalence_class in equivalence_classes:
            for symbol in alphabet:
                # Find the next state for each symbol in the equivalence class
                next_states = set()
                for state in equivalence_class:
                    next_states.add(transitions[state][symbol])

                # Check if the next states belong to an existing equivalence class
                for existing_class in new_partition:
                    if next_states.issubset(existing_class):
                        existing_class.update(equivalence_class)
                        break
                else:
                    new_partition.append(next_states | equivalence_class)

        # Check if the partition is the same as the previous iteration
        if new_partition == equivalence_classes:
            break

        equivalence_classes = new_partition

    # Step 5: Construct the minimized DFA
    minimized_states = []
    minimized_transitions = {}
    minimized_start_state = None
    minimized_accept_states = []

    # Create new states for each equivalence class
    for equivalence_class in equivalence_classes:
        new_state = ",".join(sorted(equivalence_class))
        minimized_states.append(new_state)

        # Check if the equivalence class contains the start state
        if start_state in equivalence_class:
            minimized_start_state = new_state

        # Check if the equivalence class contains any accept state
        if equivalence_class.intersection(accept_set):
            minimized_accept_states.append(new_state)

        # Create new transitions for the minimized DFA
        new_transitions = {}
        for symbol in alphabet:
            next_states = set()
            for state in equivalence_class:
                next_states.add(transitions[state][symbol])
            new_transitions[symbol] = ",".join(sorted(next_states))

        minimized_transitions[new_state] = new_transitions

    minimized_dfa = {
        "states": minimized_states,
        "alphabet": alphabet,
        "transitions": minimized_transitions,
        "start_state": minimized_start_state,
        "accept_states": minimized_accept_states
    }

    return minimized_dfa


# Example usage

# Define the DFA
states = ["A", "B", "C", "D"]
alphabet = ["0", "1"]
transitions = {
    "A": {"0": "B", "1": "C"},
    "B": {"0": "B", "1": "D"},
    "C": {"0": "B", "1": "C"},
    "D": {"0": "D", "1": "C"}
}
start_state = "A"
accept_states = ["C"]

# Minimize the DFA
minimized_dfa = minimize_dfa(
    states, alphabet, transitions, start_state, accept_states)

# Print the minimized DFA
print("Minimized DFA:")
print("States:", minimized_dfa["states"])
print("Alphabet:", minimized_dfa["alphabet"])
print("Transitions:", minimized_dfa["transitions"])
print("Start State:", minimized_dfa["start_state"])
print("Accept States:", minimized_dfa["accept_states"])
