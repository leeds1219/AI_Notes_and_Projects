# -*- coding: utf-8 -*-
"""2018140088.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uEk1y0Ws-fCZNurg211zSLGAkYtA5ChJ
"""

# Iterative min-conflict
import random

# filtering!!!
def min_conflicts(solution, n, iterative=1000):
    def random_position(list, filter_function):
        return random.choice([i for i in range(n) if filter_function(list[i])])

    # Lambda functions are often used when you need a small, simple function for a short period
    # and don't want to define a full function using the def keyword.
    # They are particularly useful when you need to pass a function as an argument to another function
    # Lambda arguments: expression

    for k in range(iterative):
        conflicts = find_conflicts(solution, n)
        if sum(conflicts) == 0:
            return solution
        column = random_position(conflicts, lambda conflict_list_element: conflict_list_element > 0)
        conflict_list = [column_conflict(solution, n, column, row) for row in range(n)]
        solution[column] = random_position(conflict_list, lambda conflict_list_element: conflict_list_element == min(conflict_list))
    raise Exception("Error")

def find_conflicts(solution, n):
    return [column_conflict(solution, n, column, solution[column]) for column in range(n)]

def column_conflict(solution, n, column, row):
    total = 0
    for i in range(n):
        if i == column:
            continue
        if solution[i] == row or abs(i - column) == abs(solution[i] - row):
            total += 1
    return total

N = int(input())
print(" ".join(map(str, min_conflicts(list(range(N)), N))))

# thanks to Vedant Kumar for the ideas