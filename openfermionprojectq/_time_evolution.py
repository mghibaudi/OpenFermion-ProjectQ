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

import copy

import projectq

from openfermion.ops import QubitOperator


def TimeEvolution(time, hamiltonian):
    """
    Converts the Hamiltonian to an instance of the ProjectQ QubitOperator
    and then returns an instance of the ProjectQ TimeEvolution gate.
    This gate is the unitary time evolution propagator:
    exp(-i * H * t),
    where H is the Hamiltonian of the system and t is the time. Note that -i
    factor is stored implicitly.

    Example:
            wavefuction = eng.allocate_qureg(5)
            hamiltonian = 0.5 * QubitOperator("X0 Z1 Y5")
            # Apply exp(-i * H * t) to the wavefunction:
            TimeEvolution(time=2.0, hamiltonian=hamiltonian) | wavefunction

    Args:
        time(float, int): time t
        hamiltonian(QubitOperator): hamiltonaian H

    Returns:
        Instance of ProjectQ TimeEvolution gate.

    Raises:
        TypeError: If time is not a numeric type and hamiltonian is not a
            QubitOperator.
        NotHermitianOperatorError: If the input hamiltonian is not
            hermitian (only real coefficients).
    """
    projectq_qubit_operator = projectq.ops.QubitOperator()
    for term, coefficient in hamiltonian.terms.items():
        projectq_qubit_operator.terms[term] = coefficient
    return projectq.ops.TimeEvolution(time, projectq_qubit_operator)
