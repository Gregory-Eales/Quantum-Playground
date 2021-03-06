import cirq
import random


def make_oracle(input_qubits, output_qubit, x_bits):
    yield(cirq.CNOT(q, output_qubit) for (q, bit) in zip(input_qubits, x_bits) if bit)
    yield(cirq.I(q) for (q, bit) in zip(input_qubits, x_bits) if not bit)


def set_io_qubits(num_qubits=10):

	input_qubits = [cirq.GridQubit(i, 0) for i in range(num_qubits)]
	output_qubit = cirq.GridQubit(num_qubits, 0)


	return input_qubits, output_qubit


# make bv circuit
def make_bv_circuit(input_qubits, output_qubit, oracle):
	
	circuit = cirq.Circuit()

	# put into superposition
	circuit.append(cirq.H.on_each(*input_qubits))


	# apply oracle
	circuit.append(oracle)

	# take out of superpositon
	circuit.append(cirq.H.on_each(*input_qubits))

	# measure qubits
	circuit.append(cirq.measure(*input_qubits))

	return circuit


#print(cirq.GridQubit(10, 0))


x_bits = [random.randint(0, 1) for _ in range(10)]
input_qubits, output_qubit = set_io_qubits()
oracle = make_oracle(input_qubits, output_qubit, x_bits)
circuit = make_bv_circuit(input_qubits, output_qubit, oracle)
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1)

print(x_bits)
print(result)
