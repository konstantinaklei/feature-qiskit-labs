from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Φτιάχνουμε ένα κβαντικό κύκλωμα με 2 Qubits και 2 κλασικά bits (για να αποθηκεύσουμε το αποτέλεσμα)
qc = QuantumCircuit(2, 2)

# Hadamard στο Qubit 0 (το βάζει σε υπέρθεση)
qc.h(0)

# CNOT μεταξύ Qubit 0 και Qubit 1 (αυτό δημιουργεί τη διεμπλοκή)
qc.cx(0, 1)

# Μετράμε τα Qubits
qc.measure([0, 1], [0, 1])

print("Το Κβαντικό μου Κύκλωμα:")
print(qc.draw("text"))

simulator = AerSimulator()
job = simulator.run(qc, shots=1000) # Το τρέχουμε 1000 φορές
result = job.result()

counts = result.get_counts(qc)
print("\nΑποτελέσματα μετά από 1000 μετρήσεις:")
print(counts)