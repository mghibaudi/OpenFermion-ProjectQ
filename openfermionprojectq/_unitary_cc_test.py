#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Module to test unitary coupled cluster operators."""

from __future__ import absolute_import

from numpy.random import randn
import scipy

import itertools
import os
import unittest

import openfermion
from openfermion.config import THIS_DIRECTORY
from openfermion.hamiltonians import MolecularData
from openfermion.ops import *
from openfermion.transforms import *
from openfermion.utils import *

from openfermionprojectq import TimeEvolution
from openfermionprojectq._graph import (Graph, Node)
from openfermionprojectq._unitary_cc import *

from projectq.ops import All, Measure, X


class UnitaryCC(unittest.TestCase):

    def test_simulation_energy(self):
        """Test UCCSD Singlet Energy for H2"""

        # Define H2 Hamiltonian inline
        hamiltonian = ((-0.0453222020986) * QubitOperator("X0 X1 Y2 Y3") +
                       (0.165867023964) * QubitOperator("Z0 Z3") +
                       (0.174348441706) * QubitOperator("Z2 Z3") +
                       (0.120544821866) * QubitOperator("Z0 Z2") +
                       (3.46944695195e-18) * QubitOperator("X0 Y1 X2 Y3") +
                       (0.165867023964) * QubitOperator("Z1 Z2") +
                       (0.171197748533) * QubitOperator("Z0") +
                       (-0.222785928901) * QubitOperator("Z3") +
                       (3.46944695195e-18) * QubitOperator("X0 X1 X2 X3") +
                       (0.168622191433) * QubitOperator("Z0 Z1") +
                       (0.120544821866) * QubitOperator("Z1 Z3") +
                       (3.46944695195e-18) * QubitOperator("Y0 Y1 Y2 Y3") +
                       (-0.0988639735178) * QubitOperator("") +
                       (0.171197748533) * QubitOperator("Z1") +
                       (0.0453222020986) * QubitOperator("Y0 X1 X2 Y3") +
                       (3.46944695195e-18) * QubitOperator("Y0 X1 Y2 X3") +
                       (-0.0453222020986) * QubitOperator("Y0 Y1 X2 X3") +
                       (-0.222785928901) * QubitOperator("Z2") +
                       (0.0453222020986) * QubitOperator("X0 Y1 Y2 X3"))
        hamiltonian.compress()
        compiler_engine = uccsd_trotter_engine()
        wavefunction = compiler_engine.allocate_qureg(4)
        test_amplitudes = [-1.14941450e-08, 5.65340614e-02]
        for i in range(2):
            X | wavefunction[i]
        evolution_operator = uccsd_singlet_evolution(test_amplitudes, 4, 2)
        evolution_operator | wavefunction
        compiler_engine.flush()
        energy = compiler_engine.backend.get_expectation_value(hamiltonian,
                                                               wavefunction)
        All(Measure) | wavefunction
        self.assertAlmostEqual(energy, -1.13727017463)

    def test_simulation_with_graph(self):
        """Test UCCSD Singlet Energy for H2 using a restricted qubit_graph"""

        # Define H2 Hamiltonian inline
        hamiltonian = ((-0.0453222020986) * QubitOperator("X0 X1 Y2 Y3") +
                       (0.165867023964) * QubitOperator("Z0 Z3") +
                       (0.174348441706) * QubitOperator("Z2 Z3") +
                       (0.120544821866) * QubitOperator("Z0 Z2") +
                       (3.46944695195e-18) * QubitOperator("X0 Y1 X2 Y3") +
                       (0.165867023964) * QubitOperator("Z1 Z2") +
                       (0.171197748533) * QubitOperator("Z0") +
                       (-0.222785928901) * QubitOperator("Z3") +
                       (3.46944695195e-18) * QubitOperator("X0 X1 X2 X3") +
                       (0.168622191433) * QubitOperator("Z0 Z1") +
                       (0.120544821866) * QubitOperator("Z1 Z3") +
                       (3.46944695195e-18) * QubitOperator("Y0 Y1 Y2 Y3") +
                       (-0.0988639735178) * QubitOperator("") +
                       (0.171197748533) * QubitOperator("Z1") +
                       (0.0453222020986) * QubitOperator("Y0 X1 X2 Y3") +
                       (3.46944695195e-18) * QubitOperator("Y0 X1 Y2 X3") +
                       (-0.0453222020986) * QubitOperator("Y0 Y1 X2 X3") +
                       (-0.222785928901) * QubitOperator("Z2") +
                       (0.0453222020986) * QubitOperator("X0 Y1 Y2 X3"))
        hamiltonian.compress()

        # Create a star graph of 4 qubits, all connected through qubit 0
        qubit_graph = Graph()
        compiler_engine = uccsd_trotter_engine(qubit_graph=qubit_graph,
                                               opt_size=3)
        wavefunction = compiler_engine.allocate_qureg(4)
        for i in range(4):
            qubit_graph.add_node(Node(value=wavefunction[i].id))
        for i in range(1, 4):
            qubit_graph.add_edge(0, i)

        test_amplitudes = [-1.14941450e-08, 5.65340614e-02]
        for i in range(2):
            X | wavefunction[i]
        evolution_operator = uccsd_singlet_evolution(test_amplitudes, 4, 2)
        evolution_operator | wavefunction
        compiler_engine.flush()

        energy = compiler_engine.backend.get_expectation_value(hamiltonian,
                                                               wavefunction)
        self.assertAlmostEqual(energy, -1.13727017463)

        # Check swap only with non-adjacent qubits functions without error
        projectq.ops.Swap | (wavefunction[0], wavefunction[3])
        projectq.ops.Swap | (wavefunction[0], wavefunction[3])
        compiler_engine.flush()
        energy = compiler_engine.backend.get_expectation_value(hamiltonian,
                                                               wavefunction)
        All(Measure) | wavefunction
        self.assertAlmostEqual(energy, -1.13727017463)
