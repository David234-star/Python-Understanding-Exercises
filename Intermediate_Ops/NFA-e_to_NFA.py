class NFA:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def epsilon_closure(self, state):
        closure = {state}
        stack = [state]

        while stack:
            current_state = stack.pop()
            epsilon_transitions = self.transitions.get(
                current_state, {}).get('ε', [])

            for state in epsilon_transitions:
                if state not in closure:
                    closure.add(state)
                    stack.append(state)

        return closure

    def convert_epsilon_to_nfa(self):
        nfa = NFA(set(), self.alphabet, {}, set(), set())

        for state in self.states:
            closure = self.epsilon_closure(state)
            nfa.states.update(closure)

            for symbol in self.alphabet:
                transitions = set()

                for epsilon_state in closure:
                    transitions.update(
                        self.transitions.get(epsilon_state, {}).get(symbol, []))

                if transitions:
                    nfa.transitions[(state, symbol)] = transitions

        nfa.initial_state = self.epsilon_closure(self.initial_state)

        for final_state in self.final_states:
            nfa.final_states.update(self.epsilon_closure(final_state))

        return nfa


def parse_regex(regex):
    stack = []
    transitions = {}

    for i, char in enumerate(regex):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                start = stack.pop()
                transitions[start] = {'ε': {i + 1}}
                transitions[i] = {'ε': {start + 1}}
            else:
                raise ValueError(
                    "Mismatched parentheses in the regular expression")
        elif char == '|':
            if stack:
                start = stack[-1]
                transitions[start] = {'ε': {i + 1}}
                stack.append(i)
            else:
                raise ValueError(
                    "Mismatched parentheses in the regular expression")
        elif char == '*':
            transitions[i] = {'ε': {i, i + 1}}
            if stack:
                transitions[stack[-1]]['ε'].add(i + 1)
        else:
            transitions[i] = {char: {i + 1}}

    if stack:
        raise ValueError("Mismatched parentheses in the regular expression")

    states = set(range(len(regex) + 1))
    alphabet = set(char for char in regex if char not in '()*|')
    initial_state = 0
    final_states = {len(regex)}

    return NFA(states, alphabet, transitions, initial_state, final_states)


def convert_regex_to_nfa(regex):
    nfa_with_epsilon = parse_regex(regex)
    nfa_no_epsilon = nfa_with_epsilon.convert_epsilon_to_nfa()
    return nfa_no_epsilon


# Example usage
nfa_no_epsilon = convert_regex_to_nfa('a*b')
print(nfa_no_epsilon.states)
print(nfa_no_epsilon.alphabet)
print(nfa_no_epsilon.transitions)
print(nfa_no_epsilon.initial_state)
print(nfa_no_epsilon.final_states)
