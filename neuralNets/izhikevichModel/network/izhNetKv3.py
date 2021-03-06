import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

#needs to be optimized for fewer matricies
#needs random starting point
#[ROW][Collumn]

numNeurons = 5
steps = 2
maxTme = int(np.ceil(steps/.025))


#probably unessary...
dtMat = .025 *np.ones((numNeurons, 1), dtype=np.float32)

tMinusZs = np.zeros((numNeurons, maxTme-1), dtype=np.float32)


#do I really need individual matrices for these?
##aMat = .02*np.ones((numNeurons, 1), dtype=np.float32)
##bMat = .2*np.ones((numNeurons, 1), dtype=np.float32)
##cMat = -65. * np.ones((numNeurons, 1), dtype=np.float32)
##dMat = 2. * np.ones((numNeurons, 1), dtype=np.float32)

#vMat = -65. * np.ones((numNeurons, 1), dtype=np.float32)
#vMat = -65 * np.random.randint(2, size=(numNeurons, maxTme))

#concat random start with the zero matrix at axis 1
vMat = np.append(-65 * np.random.randint(2, size=(numNeurons, 1)), tMinusZs, 1)
#xprint('vMat:\n', vMat)
uMat = 0. * np.random.randint(2, size=(numNeurons, maxTme))
#uMat = np.append(0.0 * np.random.randint(2, size=(numNeurons, 1)), tMinusZs, 1)


dtN = np.ones((numNeurons, maxTme), dtype=np.float32)
vN = np.ones((numNeurons, maxTme), dtype=np.float32) 
uN = np.ones((numNeurons, maxTme), dtype=np.float32)

plt.subplot(1,3,1)
connect = np.random.randint(2, size=(numNeurons, numNeurons))
plt.imshow(connect, cmap=plt.cm.gray)
plt.title('connectome')

plt.subplot(1,3,2)
fired = np.zeros((numNeurons, maxTme), dtype=np.float32)
plt.imshow(vMat, cmap=plt.cm.gray)
plt.title('pre-fired')

plt.subplot(1,3,3)
spikes = np.zeros((numNeurons, int(np.ceil(steps/.025))))
plt.imshow(spikes, cmap=plt.cm.gray)
plt.title('Spikes')
plt.show()


def getI(vMat, connect, i, step, bias):
    #iterates through fired, if connection, then increments input I
    #Should make the 'bias' a parameter
    #this could be where hebbian learning etc. could be implimented
    I = 0
    for j in range(0, numNeurons):
        if vMat[i][step] > 25 and connect[i][j] == 1:
            I += 1
    #print('Found ', I)
    return I + bias


#Simulation
t = 0
cnt = int(np.ceil(steps/.025))
step = 0

Is = []
while step < cnt:
    #iterate through each neuron, i
    for i in range(0, numNeurons):
        I = getI(vMat, connect, i, step, 5)
        Is.append(I)

        u = uMat[i][step]
        v = vMat[i][step]
##        a = aMat[i]
##        b = bMat[i]
##        c = cMat[i]
##        d = dMat[i]

        a = .02
        b = .2
        c = -65.
        d = 8.
        dt = dtMat[i]
        
        if v > 25:
            spikes[i][step] = 1
            v = c
            u = u + d
            
            
        dv = (.04 *( v ** 2)) + (5 * v) + 140 - u + I
        du = a * ((b*v) - u)

        v = v + dt*dv
        u = u + dt*du


        #update the next time step...
        #has to be a better way to get around the out of bounds error
        if step < 39:
            uMat[i][step+1] = u
            vMat[i][step+1] = v
        #print('new vMat:\n', vMat)

##    uMat = uN
##    vMat = vN
    #print(vMat)

    t += dt
    step += 1

plt.subplot(1,2,1)
plt.imshow(spikes, cmap=plt.cm.gray)
plt.title('Post-Spikes')

plt.subplot(1,2,2)
plt.imshow(vMat, cmap=plt.cm.gray)
cbar = plt.colorbar()
plt.title('Post-Voltage')
plt.show()
