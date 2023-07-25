import numpy as np


class CSP:
    def __init__(self, n):
        """
        Here we initialize all the required variables for the CSP computation,
        according to the n.
        """
        # Your code here
        self.n = n
        self.grid = np.array(np.zeros(shape=(n, n), dtype=int))
        self.domain = np.array(np.ones(shape=(n, n), dtype=int))
        self.number_of_iteration = 0

    def check_constraints(self) -> bool:
        """
        Here we check the grid horizontally, vertically and diagonally
        """
        pass

    def forward_check(self, i):
        """
        After assigning a queen to ith column, we can make a forward check
        to boost up the computing speed and prune our search tree.
        """
        pass

    def assign(self, row, column):
        """
        assign 1 to self.grid[row,colmn]
        """
        # fill me
        pass

    def _solve_problem_with_backtrack(self, i):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem.
        """
        # Your code here
        pass

    def solve_problem_with_backtrack(self):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem
         and return solution's grid
        """
        return self._solve_problem_with_backtrack(0)

    def _solve_problem_with_forward_check(self, i):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem.
        """
        # Your code here
        pass

    def solve_problem_with_forward_check(self):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem
         and return solution's grid
        """
        return self._solve_problem_with_forward_check(0)
