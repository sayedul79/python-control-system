import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

#read dataset
tc_raw=pd.read_csv("D:\Extra Knowledge\HP-NPC\dataset/EEE364_exp3_f25%_A40%_offset40%.csv")
tc_fil=tc_raw.loc[203:, :] #select particular dataset
tc_fil_3rd=tc_raw.copy().loc[1002:, :]  #select 3rd cycle above dataset
tc_fil["Speed"]=tc_fil.Speed*np.pi      #convert rad/s
tc_fil_3rd["Speed"]=tc_fil_3rd.Speed*np.pi  #convert rad/s
tc_fil_3rd.reset_index(drop=True, inplace=True)

tc_fil_3rd["TimeShift"]=tc_fil_3rd.TimeStamp-tc_fil_3rd.TimeStamp[0] #shift to origin

tc_fil2=tc_fil[~((tc_fil.TimeStamp>=10) & (tc_fil.Speed==0.0))]
tc_fil2["Voltage_Mul"]=tc_fil2.Voltage*0.48

#selct half cycle dataset
freq=0.25
period=1/freq
tc_fil_one=tc_fil_3rd[tc_fil_3rd.TimeShift<=period/2]

steady_state=tc_fil_one.Speed.max()
amp_tcon=0.632*steady_state     #amplitude at time constant
t_cons=np.interp(amp_tcon, tc_fil_one.Speed, tc_fil_one.TimeShift)

#Compare second order system with approximated first order
t=np.arange(0, 2, 0.01)
E=35.394
k_s=5.86
tau=0.036
first_order=E*k_s*(1-np.exp(-t/tau))

fig, ax1=plt.subplots()
font = {'family': 'JetBrains Mono',
        'color':  'black',
        'weight': 'normal',
        'size': 15,
        }
#plot positive half cycle of speed vs time
ax1.plot(tc_fil_one.TimeShift, tc_fil_one.Speed, color="red", linewidth=1.5)

#fill transient and steady state area
ax1.axvspan(xmin=0.94, xmax=2.0, color="green", alpha=0.3)
ax1.axvspan(xmin=0, xmax=0.94, color="#F8E0C1")

#plot steady state horizontal line
ax1.axhline(y=steady_state, linestyle="--", color="grey")

#Write text and annotation for transient analysis
tex1="Transient"
tex2="Steady state"
ax1.text(1.25, 200, tex2, fontdict=font, color="DarkGreen")
ax1.text(0.3, 200, tex1, fontdict=font, color="#f78e31")
ax1.text(0.09, 10, r"$\tau =0.084s$", fontdict=font, color="blue")

ax1.hlines(amp_tcon, xmin=0, xmax=t_cons, linestyle="dashed")
ax1.vlines(t_cons, ymin=0, ymax=amp_tcon, linestyle="dashed")

ax1.scatter(t_cons, amp_tcon, marker = 'o', color="DarkBlue", zorder=10)

ax1.annotate("(0.084, 156.85)",xy=(t_cons, amp_tcon),
             xytext=[0.15, 130], 
            arrowprops={'arrowstyle':"->", "color":'m'}, fontsize=12)

#plot first order and 2nd order approximation
fig, ax2=plt.subplots()
ax2.plot(tc_fil_one.TimeShift, tc_fil_one.Speed, color="DarkBlue", linewidth=2, label="Second Order")
ax2.plot(t, first_order, color="DarkOrange", linewidth=2, label="First order")
ax2.axvspan(xmin=0, xmax=2, color="#F8E0C1")
ax2.set_xlim(0, 2.0)

#plot steady state horizontal line
ax2.axhline(y=steady_state, linestyle="--", color="grey")
ax2.axhline(y=first_order.max(), linestyle="--", color="grey")

#plot speed and voltage with respect to time
fig, ax3=plt.subplots()
ax3.plot(tc_fil2.TimeStamp, tc_fil2.Speed, color="DarkBlue", linewidth=2, label="Speed(rad/s)")
ax3.plot(tc_fil2.TimeStamp, tc_fil2.Voltage_Mul, color="DarkOrange", linewidth=2, label="Voltage")



# ax.fill_between(tc_fil_one.TimeStamp, 0, 1, where=tc_fil_one.Speed >= steady_state,
#                 color='green', alpha=0.5, transform=ax.get_xaxis_transform())


for ax in [ax1, ax2, ax3]:
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.grid(which='major',color='green', alpha=1.0, linewidth=1.2)
    ax.grid(which='minor',color="grey", alpha=0.3)
    # Move the left and bottom spines to x = 0 and y = 0, respectively.
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    # Hide the top and right spines.
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.set_xlabel(xlabel="Time(s)", fontsize=15)
    #ax.set_ylabel(ylabel="Speed(rad/s)", rotation="horizontal", fontsize=15)
    ax.yaxis.set_label_coords(0.04,1.02)
    ax.xaxis.set_label_coords(1.06,0.04)
    ax.tick_params(axis="both", which="major", labelsize=15)

 
#plt.legend(frameon=False, loc='center', fontsize=15)
plt.legend(frameon=False, fontsize=15, loc="center")
            
plt.show()
