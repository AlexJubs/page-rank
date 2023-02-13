# page-rank

#### Summary

This is a sample of code that implements the PageRank algorithm, which is used by Google to rank websites based on the number and quality of links pointing to them.

This implementation takes as input an adjacency matrix `G`, representing a graph with `n` nodes, and returns the PageRank of each node in the graph. The damping factor `damping_factor` and the tolerance `epsilon` can be adjusted to fine-tune the computation. The function iteratively updates the PageRank vector until convergence, which is determined by the sum of the absolute differences between the current and previous PageRank vectors.

The PageRank algorithm uses a mathematical model of the web graph to compute the importance of each page. The web graph is represented as a directed graph, where each node represents a web page and each directed edge represents a link from one page to another. The PageRank of a page is defined as the probability that a random surfer following links on the web will end up on that page after a large number of clicks.

#### Updating Values

Firstly all the pagerank values are initialized to 1/N where N is the total number of pages. Thus, all pages have the same initial value.

We update the pagerank value for each page iteratively. Suppose the damping factor is "d", and L(X) is the number out outgoing pages from X. We have a given page "A" with incoming connections from pages B, C, and D. In each iteration, we shall update the pagerank of A as such:

![mathematical formula of the original PageRank](https://cdn1.link-assistant.com/thumbs/w700-c1/upload/news/posts/422/2.png)

#### The Damping Factor

In practice, the PageRank algorithm is modified to handle issues such as the existence of dead ends (pages with no outgoing links) and spider traps (pages with links that point back to themselves). To handle these issues, the algorithm is usually run with a damping factor that reduces the contribution of each link to the PageRank of the target page. The damping factor can be thought of as representing the probability that a random surfer will continue following links, rather than jumping to a random page.

#### Testing

This test case creates a small graph with four nodes and three links, and checks that the PageRank computed by the `page_rank` function is close to the expected result. The `np.allclose` function is used to compare the computed PageRank with the expected result, with a relative tolerance of `1e-6` and an absolute tolerance of `1e-6`. If the computation is correct, the test should pass without raising an exception.

![Example image](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/PageRanks-Example.svg/660px-PageRanks-Example.svg.png)
