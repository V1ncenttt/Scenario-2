from automata_tools import NFAtoDFA
from automata_tools import NFAtoDFA
from automata_tools.Automata import Automata
from automata_tools.DFAtoMinimizedDFA import DFAtoMinimizedDFA
from NFAfromRegex import NFAfromRegex
import pydot

def regToNFA(regex) :
    x = NFAfromRegex(regex).getNFA()
    # return Automata.getDotFile(x)
    return x

def NFAtoDFA(nfa):
    x = NFAtoDFA(nfa)
    # return Automata.getDotFile(x)
    return x

def minimise(dfa):
    x = DFAtoMinimizedDFA(dfa)
    # return Automata.getDotFile(x)
    return x

def writeDot(fsa, path = "static/Images/graph.png"):
    graphs = pydot.graph_from_dot_data(Automata.getDotFile(fsa))
    graph = graphs[0]
    graph.write_png(path)
