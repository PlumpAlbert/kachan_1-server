from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value
import numpy as np


def thing(minimal_production, annual_production, priorities, periods):
    problem = LpProblem("Calendar planning", LpMaximize)

    z = 0
    products = []
    for period in range(1, periods + 1):
        products.append([])
        for product_type in range(len(minimal_production)):
            mp = minimal_production[product_type]
            p = priorities[product_type]
            product = LpVariable(f"product_{product_type+1}_{period}",
                                 mp[period - 1])
            z += (1.0 / (p * period)) * product
            products[period - 1].append(product)

    problem += z

    for product_type in range(len(minimal_production)):
        problem += np.sum([row[product_type] for row in products
                           ]) == annual_production[product_type]

    problem.solve()
    print("Status: ", LpStatus[problem.status])
    for v in problem.variables():
        print(v.name, "=", v.varValue)

    print("\nSolution = ", value(problem.objective))


thing([[2, 4], [3, 5]], [45, 40], [2, 1], 2)
