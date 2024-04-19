import os
import pickle


def improved_tsp_approximation(matrix):
    # YOUR CODE HERE
    pass


def validate_tour(tour, matrix):
    """
    Provided function to verify the validity of your TSP approximation function.
    Returns the length of the tour if it is valid, -1 otherwise.
    Feel free to use or modify this function however you please,
    as the autograder will only call your tsp_approximation function.
    """
    n = len(tour)
    cost = 0
    for i in range(n):
        if matrix[tour[i - 1]][tour[i]] == float("inf"):
            return -1
        cost += matrix[tour[i - 1]][tour[i]]
    return cost


def evaluate_tsp(tsp_approximation):
    """
    Provided function to evaluate your TSP approximation function.
    Feel free to use or modify this function however you please,
    as the autograder will only call your tsp_approximation function.
    """

    test_cases = pickle.load(open(os.path.join("tsp_cases.pkl"), "rb"))

    total_cost = 0
    for i, case in enumerate(test_cases["files"]):
        tour = tsp_approximation(case)
        cost = validate_tour(tour, case)
        assert cost != -1
        total_cost += cost
        print(f"Case {i}: {cost}")

    for i, case in enumerate(test_cases["generated"], start=len(test_cases["files"])):
        tour = tsp_approximation(case)
        cost = validate_tour(tour, case)
        assert cost != -1
        total_cost += cost
        print(f"Case {i}: {cost}")

    print(f"Total cost: {total_cost}")
    return total_cost


if __name__ == "__main__":
    evaluate_tsp(improved_tsp_approximation)
