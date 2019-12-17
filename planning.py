from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value, lpSum, LpStatusOptimal
import numpy as np


def plan(products, resourceCount, periodsCount, fonds, resourceConsumption,
         mvp):
    problem = LpProblem("Calendar_planning", LpMaximize)

    z = 0
    periodPlan = []
    for period in range(1, periodsCount + 1):
        periodPlan.append([])
        for product in products:
            var_product = LpVariable(
                f"product_{product['id']}@period_{period}",
                lowBound=mvp[period - 1][product['id']],
                cat='Integer')
            z += (1.0 / (product['priority'])) * var_product
            periodPlan[period - 1].append(var_product)
        for resource in range(resourceCount):
            problem += lpSum([
                rc[resource] * periodPlan[period - 1][i]
                for i, rc in enumerate(resourceConsumption)
            ]) <= fonds[period - 1][resource]

    problem.setObjective(z)

    for product in products:
        problem += lpSum([p[product['id']]
                          for p in periodPlan]) == product['annual']

    for resource in range(resourceCount):
        problem += lpSum([p[resource] for p in resourceConsumption])

    problem.solve()
    if problem.status == LpStatusOptimal:
        result = []
        for v in problem.variables():
            if v.name == '__dummy': continue
            result.append({'name': v.name, 'value': v.varValue})
        return result
    else:
        return "Sosi hui"
