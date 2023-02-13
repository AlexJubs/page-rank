import copy

def page_rank(G, damping_factor, epsilon):
    """
    Compute the PageRank of nodes in the graph.
    
    Parameters
    ----------
    G : numpy matrix
        Adjacency matrix of the graph.
    damping_factor : float
        The damping factor in the PageRank computation.
    epsilon : float
        The tolerance used to determine convergence.
        
    Returns
    -------
    numpy array
        The PageRank of each node in the graph.
    """
    # get the number of pages, n
    n = len(G)

    # counting how many outbound links there are for each page
    outbound_link_counts = [sum(row) for row in G]
    pr = [1.0 / n for _ in range(n)]
    damping_value = (1 - damping_factor) / n
    
    num_iterations = 0
    while True:
        new_pr = [damping_value for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # for each incoming node onto i
                if G[j][i] == 0: continue
                new_pr[i] += (damping_factor * pr[j]) / outbound_link_counts[j]
        
        delta = sum(abs(pr[i] - new_pr[i]) for i in range(n))
        if delta <= epsilon:
            print(f"terminated after {num_iterations} iterations")
            return new_pr
        print(f"pagerank after {num_iterations} iterations:")
        print(pr)
        pr = copy.deepcopy(new_pr)
        num_iterations += 1

def pretty_print(M):
    for row in M: print(row)

def test_page_rank():
    # 1 on (i,j) indicates an outbound link from i to j
    G = [[0, 1, 0, 0],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 0, 0]]
    # 0 -> (1), 1 -> (0,2), 2 -> (0,1,3), 3 -> (0)
    print(f"testing pagerank with {len(G)} pages, with the following initial popularity scores:")
    pr = page_rank(G, damping_factor=0.85, epsilon=0.0001)
    print("Final PageRank scores (for pages 1-4):")
    for i in range(len(pr)):
        print(f"page {i} has score: {pr[i]}")

if __name__ == "__main__":
    test_page_rank()