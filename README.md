# page-rank

#### Summary

This is a sample of code that implements the PageRank algorithm, which is used by Google to rank websites based on the number and quality of links pointing to them.

This implementation takes as input an adjacency matrix `G`, representing a graph with `n` nodes, and returns the PageRank of each node in the graph. The damping factor `damping_factor` and the tolerance `epsilon` can be adjusted to fine-tune the computation. The function iteratively updates the PageRank vector until convergence, which is determined by the sum of the absolute differences between the current and previous PageRank vectors.

#### Testing:

This test case creates a small graph with four nodes and three links, and checks that the PageRank computed by the `page_rank` function is close to the expected result. The `np.allclose` function is used to compare the computed PageRank with the expected result, with a relative tolerance of `1e-6` and an absolute tolerance of `1e-6`. If the computation is correct, the test should pass without raising an exception.
