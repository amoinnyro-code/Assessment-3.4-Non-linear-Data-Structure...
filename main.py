from collections import deque
import sys

# -------------------------------------------------------------
# 1. BINARY TREE IMPLEMENTATION & TRAVERSAL
# -------------------------------------------------------------
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def bfs_binary_tree(root):
    """Breadth-First Search (Level-Order) for Binary Tree"""
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        current = queue.popleft()
        result.append(current.val)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            
    return result

def dfs_binary_tree(root):
    """Depth-First Search (Pre-Order) for Binary Tree"""
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        current = stack.pop()
        result.append(current.val)
        
        # Push right first so left is processed first (LIFO)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
            
    return result


# -------------------------------------------------------------
# 2. GRAPH IMPLEMENTATION & TRAVERSAL
# -------------------------------------------------------------
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # Undirected graph

    def bfs(self, start_node):
        visited = set([start_node])
        queue = deque([start_node])
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return result

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Push neighbors in reverse order to preserve order
                for neighbor in reversed(self.adj_list.get(vertex, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        
        return result


# -------------------------------------------------------------
# HELPER FUNCTIONS TO DISPLAY SECTIONS
# -------------------------------------------------------------
def display_binary_tree(root):
    print("\n==========================================")
    print("      1. BINARY TREE & TRAVERSALS         ")
    print("==========================================")
    print("Structure (Surname: A-M-O-I-N):")
    print(r"        A        ")
    print(r"       / \      ")
    print(r"      M   O      ")
    print(r"     / \         ")
    print(r"    I   N        ")
    print("------------------------------------------")
    print("BFS (Level-Order) :", " -> ".join(bfs_binary_tree(root)))
    print("DFS (Pre-Order)   :", " -> ".join(dfs_binary_tree(root)))
    print("==========================================\n")

def display_graph(g):
    print("\n==========================================")
    print("        2. GRAPH & TRAVERSALS             ")
    print("==========================================")
    print("Adjacency List:")
    print("  Node A -> M, O")
    print("  Node M -> A, I, N")
    print("  Node O -> A")
    print("  Node I -> M")
    print("  Node N -> M")
    print("------------------------------------------")
    print("BFS Traversal      :", " -> ".join(g.bfs('A')))
    print("DFS Traversal      :", " -> ".join(g.dfs('A')))
    print("==========================================\n")


# -------------------------------------------------------------
# INTERACTIVE MENU SYSTEM
# -------------------------------------------------------------
def main():
    # Constructing Binary Tree for AMOIN (A, M, O, I, N)
    root = TreeNode('A')
    root.left = TreeNode('M')
    root.right = TreeNode('O')
    root.left.left = TreeNode('I')
    root.left.right = TreeNode('N')

    # Constructing Graph for AMOIN
    g = Graph()
    g.add_edge('A', 'M')
    g.add_edge('A', 'O')
    g.add_edge('M', 'I')
    g.add_edge('M', 'N')

    while True:
        print("=== ASSESSMENT 3.4: NON-LINEAR DATA STRUCTURES (AMOIN) ===")
        print("1. Show binary tree and its traversals")
        print("2. Show graph and its traversals")
        print("3. Show both")
        print("0. Exit")
        print("--------------------------------------------------")
        
        choice = input("Enter your choice (0-3): ").strip()
        
        if choice == '1':
            display_binary_tree(root)
        elif choice == '2':
            display_graph(g)
        elif choice == '3':
            display_binary_tree(root)
            display_graph(g)
        elif choice == '0':
            print("Exiting program. Goodbye!")
            sys.exit(0)
        else:
            print("\n[!] Invalid option. Please enter 0, 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
