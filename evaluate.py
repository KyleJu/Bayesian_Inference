
def Approximate_Bayesian_Computation(simulate, prior, size, data):
  res = []
  for pr in prior:
    if simulate(pr) == data:
      res.append(pr)
  return res
