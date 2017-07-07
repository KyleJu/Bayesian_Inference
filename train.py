import evaluate as e
from simulate import simulation as sim
import distribution as ds
import matplotlib.pyplot as plt


def main():
  sz = 100
  d = 4
  p = 0.04
  res = e.Approximate_Bayesian_Computation(
    simulate = (lambda x : sim(x,sz).simulate_conversion()),
    prior = (ds.distribution().uni() for i in range(1000)),
    size = sz,
    data = d)
  print (res)
  abbins = [i/200.0 for i in range(50)]  
  plt.hist(res, bins=abbins, normed=True)
  plt.xlim(0, max(abbins));
  plt.show()
  

if __name__ == '__main__':
  main()
