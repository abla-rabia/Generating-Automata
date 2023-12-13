from modules.expressionReg import ExpressionReg
from modules.automate import Automate
import networkx as nx
import matplotlib.pyplot as plt

def draw_automaton(automaton):
    G = nx.DiGraph()
    G.add_node(automate.S0, color='green', style='filled')
    for state in automate.S:
        if state in automate.F:
            G.add_node(state, color='blue', style='filled')

    for transition in automate.I:
        G.add_edge(transition.Si, transition.Sj, label=transition.w)

    pos = nx.spring_layout(G)  # You can change the layout if needed
    edge_labels = nx.get_edge_attributes(G, 'label')

    node_colors = [G.nodes[node].get('color', 'red') for node in G.nodes]

    nx.draw(G, pos, with_labels=True, arrows=True, node_color=node_colors, node_size=1000, font_size=10, font_color="black")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()


print("Welcome to our Program")
# Get the expression from the user
expression = input("Enter the expression: ")

# Extract the alphabet from the expression
alphabet = set(char for char in expression if char.isalpha())

# Display the results
print("Expression:", expression)
print("Alphabet:", alphabet)
# Transformt to Automate
postfix_expression = ExpressionReg(alphabet,expression)
postfix_expression.infix_to_postfix()
automate=Automate(alphabet)
automate=postfix_expression.evaluate_postfix(automate)
# Display the results in the terminal
print("Final Result:")
automate.printAutomate()
# Display the results by drawing
draw_automaton(automate)

