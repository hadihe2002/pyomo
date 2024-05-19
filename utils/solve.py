from pyomo.environ import SolverFactory, value


def solve(model):
    solver = SolverFactory('cplex')
    solver.solve(model)
    return value(model.objective)
