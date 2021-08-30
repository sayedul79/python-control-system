import control
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

w=np.logspace(-1,3,1000)
tf1=signal.TransferFunction([10],[1,14,40])
omega1,mag1,phase1=signal.bode(tf1,w)

tf2=signal.TransferFunction([10],[0.5,8,34,40])
omega2,mag2,phase2=signal.bode(tf2,w)
plt.figure()
fig,ax=plt.subplots(nrows=2)
ax[0].semilogx(omega1,mag2,color='r',label='System Without Time Delay',lw=2.5)
ax[0].semilogx(omega2,mag2,color='g',label='System With Time Delay',lw=2.5)
ax[0].set_ylabel('Magnitude(dB)')
ax[0].axhline(-34,color='k')
ax[0].axvline(8.246,color='k')
ax[0].annotate('$(8.246,-34)$',
            xy=(8.246,-34), xycoords='data',
            xytext=(0.3,0.55), textcoords='axes fraction',color='k',
            arrowprops=dict(facecolor='k', shrink=0.005),
            horizontalalignment='left', verticalalignment='bottom')

ax[1].semilogx(w,phase1,color='r',label='System Without Time Delay',lw=2.5)
ax[1].semilogx(w,phase2,color='g',label='System With Time Delay',lw=2.5)
ax[1].set_ylabel('Phase(Degree)')
ax[1].set_xlabel('Frequency($ rad s^{-1}$)')
ax[1].axhline(-180,color='k')
ax[1].axvline(8.246,color='k')
ax[1].annotate('$(8.246,-180^{\circ})$',
            xy=(8.246,-180), xycoords='data',
            xytext=(0.3,0.2), textcoords='axes fraction',color='k',
            arrowprops=dict(facecolor='k', shrink=0.005),
            horizontalalignment='left', verticalalignment='bottom')
ax[0].legend()
ax[1].legend()
ax[0].grid(True,which='both')
ax[1].grid(True,which='both')
plt.show()

# =============================================================================
# G=control.tf([10],[1,14,40])
# print(G)
# 
# Gp = control.tf([10],[0.5,8,34,40])
# print(Gp)
# 
# 
# t = np.linspace(0, 10, 1000)
# _,yp=control.step_response(Gp,t)
# plt.plot(t,yp)
# _,y=control.step_response(G,t)
# plt.plot(t,y)
# plt.show()
# =============================================================================
