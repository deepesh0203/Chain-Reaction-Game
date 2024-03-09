import copy
import math
import random


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0


def mcts(root_state, iterations):
    root = Node(root_state)

    for _ in range(iterations):
        selected_node = select(root)
        expanded_node = expand(selected_node)
        simulation_result = simulate(expanded_node)
        backpropagate(expanded_node, simulation_result)

    best_child = max(root.children, key=lambda child: child.visits)
    return best_child.state


def is_terminal(state):
    pass


def get_winner(state):
    pass


def get_random_action(state):
    pass


def resulting_state(state, action):
    pass


def get_all_states(state):
    pass


def select(node):
    while node.children:
        if not all(child.visits for child in node.children):
            # If any child has not been visited, visit it
            return expand(node)
        else:
            node = max(node.children, key=ucb)
    return node


def expand(node):
    # Generate all possible child states and create child nodes
    child_states = get_all_states(node.state)
    for child_state in child_states:
        child_node = Node(child_state, parent=node)
        node.children.append(child_node)
    return random.choice(node.children)


def simulate(node):
    # Simulate a random playout until a terminal state is reached
    while not is_terminal(node.state):
        action = get_random_action()
        node = Node(resulting_state(node.state, action), parent=node)
    return get_winner(node.state)


def backpropagate(node, result):
    while node:
        node.visits += 1
        node.wins += result
        node = node.parent


def ucb(node):
    if node.visits == 0:
        return float("inf")
    return (node.wins / node.visits) + math.sqrt(
        2 * math.log(node.parent.visits) / node.visits
    )
