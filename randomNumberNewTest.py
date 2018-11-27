from qiskit import *
#7 is 1 - 127
#6 1 -63

IBMQ.load_accounts()
qr = QuantumRegister(4)
cr = ClassicalRegister(4)
qc = QuantumCircuit(qr, cr)


qc.h(qr[0]) #Create a superposition on the quantum bit
qc.h(qr[1]) #Create a superposition on the quantum bit
qc.h(qr[2]) #Create a superposition on the quantum bit
qc.h(qr[3]) #Create a superposition on the quantum bit
# qc.h(qr[4]) #Create a superposition on the quantum bit
# qc.h(qr[5]) #Create a superposition on the quantum bit
# qc.h(qr[6]) #Create a superposition on the quantum bit



qc.measure(qr[0], cr[0]) #Measure the bit, and store its value in the clasical bit
qc.measure(qr[1], cr[1]) #Measure the bit, and store its value in the clasical bit
qc.measure(qr[2], cr[2]) #Measure the bit, and store its value in the clasical bit
qc.measure(qr[3], cr[3]) #Measure the bit, and store its value in the clasical bit
# qc.measure(qr[4], cr[4]) #Measure the bit, and store its value in the clasical bit
# qc.measure(qr[5], cr[5]) #Measure the bit, and store its value in the clasical bit
# qc.measure(qr[6], cr[6]) #Measure the bit, and store its value in the clasical bit


backend_sim = Aer.get_backend('qasm_simulator')

backend = 'ibmqx5' #Replace 'ibmq_qasm_simulator' with 'ibmqx5' to run on the quantum computer
shots_sim = 2 #Adjust this number as desired, with effects as described above




def random():
    job_sim = execute(qc, backend_sim, shots=shots_sim) #Run job on chosen backend for chosen number of shots
    stats_sim = job_sim.result().get_counts() #Retrieve results
    temp = ""
    for x in stats_sim:
         temp += x

    num = int(temp, 2)
    return num

for x in range(0, 100):
    num = random()
    print(num)


#for i in temp:
#print(max)
#print(max_val)
