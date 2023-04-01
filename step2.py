## PUT CODE HERE
import matplotlib.pylab as plt
from qiskit.visualization import plot_histogram
from qiskit import Aer, transpile
from step1 import ansatz
from step1 import get_init_params
import numpy as np

def counts_to_distr(counts):
    """
    Convert Qiskit result counts to dict with integers as
    keys, and pseudo-probabilities as values.
    """
    n_shots = sum(counts.values())
    return {int(k, 2): v/n_shots for k, v in counts.items()}

def create_target_distr(n_qbits, cross_over):
    """
    cross_over is the last zero point
    """
    n_states = 2**n_qbits
    if cross_over >= n_states:
        raise Exception("open your eyes mate")
    end = n_states-cross_over-1
    print(end)
    cumulant = sum(np.linspace(1, end, end)**2)
    print(np.linspace(1, end, end)**2)
    target_distr = {}
    for i in range(n_states):
        if i < cross_over:
            target_distr[i] = 0
        else:
            target_distr[i] = (i - cross_over)**2 / cumulant
    return target_distr

class CostFunction:
    """Compares the output distribution of our circuit with
    parameters `params` to the target distribution."""

    def __init__(self,n_qbits,rep,backend,target_distribution):
        self.n_qbits = n_qbits
        self.rep = rep
        self.backend = backend
        self.target_distribution = target_distribution


    # we defined cost function as a class method because optimizer.minimize requires
    # that the cost function only has the params parameter
    def return_cost_function(self,params):

        # Create circuit instance with paramters and simulate it
        #params = get_init_params(n_qbits, rep)
        qc = ansatz(params, self.n_qbits, self.rep)
        qc_t = transpile(qc, self.backend)
        result = self.backend.run(qc_t).result()
        # Get the counts for each measured state, and convert
        # those counts into a probability dict
        output_distr = counts_to_distr(result.get_counts())
        # Calculate the cost as the distance between the output
        # distribution and the target distribution
        cost = sum(
            abs(self.target_distribution.get(i, 0) - output_distr.get(i, 0))
            for i in range(2**self.n_qbits))
        
        return cost


def counts_to_distr(counts):
    """
    Convert Qiskit result counts to dict with integers as
    keys, and pseudo-probabilities as values.
    """
    n_shots = sum(counts.values())
    probs = {int(k, 2): v/n_shots for k, v in counts.items()}
    sorted_amplitudes = {key: np.sqrt(probs[key]) for key in sorted(probs)}
    return sorted_amplitudes 