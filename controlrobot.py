#importa sim.py y numpy
import sim
import numpy as np

def connect(port):
    clientID=sim.simxStart('127.0.0.1',port,True,True,2000,5) # Conectarse a Copellia
    if clientID == 0: print("conectado a", port)
    else: print("no se pudo conectar, revisar que este simulando")
    return clientID
    print (clientID)

clientID = connect(19999)
# obtenemos los manejadores
returnCode,handle=sim.simxGetObjectHandle(clientID,'Dummy',sim.simx_opmode_blocking)
dummy = handle
ret,joint1=sim.simxGetObjectHandle(clientID,'joint1',sim.simx_opmode_blocking)
ret,joint2=sim.simxGetObjectHandle(clientID,'joint2',sim.simx_opmode_blocking)
ret,joint3=sim.simxGetObjectHandle(clientID,'joint3',sim.simx_opmode_blocking)
#movemos
q1= int(input('angulo joint1: '))
q1 = int(q1) * np.pi/180
returnCode = sim.simxSetJointTargetPosition(clientID, joint1, q1, sim.simx_opmode_oneshot)
q2= int(input('angulo joint2: '))
q2 = int(q2) * np.pi/180
returnCode = sim.simxSetJointTargetPosition(clientID, joint2, q2, sim.simx_opmode_oneshot)
q3= int(input('angulo joint3: '))
q3 = int(q3) * np.pi/180
returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)

returnCode,pos=sim.simxGetObjectPosition(clientID, dummy, -1, sim.simx_opmode_blocking)

print("La posicion de Dummy es: ",pos)