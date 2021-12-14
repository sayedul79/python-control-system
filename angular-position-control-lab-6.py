import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#plt.xkcd()

freq_2=0.2
period_2=1/freq_2

step2_raw_g6=pd.read_csv("D:\Extra Knowledge\HP-NPC\dataset/exp6-step2-group-6.csv")
remove_zero=step2_raw_g6.loc[203:,:]

step2_g6_half_cycle=remove_zero[remove_zero.TimeStamp<=period_2/2]
step2_g6_half_cycle.tail()
step2_g6_half_cycle.reset_index(drop=True, inplace=True)
step2_g6_half_cycle["TimeShift"]=step2_g6_half_cycle.TimeStamp-step2_g6_half_cycle.TimeStamp[0]

step6_raw=pd.read_csv("D:\Extra Knowledge\HP-NPC\dataset/exp6-step6-group-6.csv")
step6_half_cycle=step6_raw[(step6_raw.TimeStamp>=20.24) & (step6_raw.TimeStamp<=22.29)]
step6_half_cycle.reset_index(drop=True, inplace=True)
step6_half_cycle["TimeShift"]=step6_half_cycle.TimeStamp-step6_half_cycle.TimeStamp[0]


step7_raw=pd.read_csv("D:\Extra Knowledge\HP-NPC\dataset/exp6-step7-group-4.csv")
step7_fil=step7_raw.loc[504:, :]
step7_fil.reset_index(drop=True, inplace=True)
step7_fil["TimeShift"]=step7_fil.TimeStamp-step7_fil.TimeStamp[0]
step7_half_cycle=step7_fil[step7_fil.TimeShift<=period_2/2]


freq_11=0.2
period_11=1/freq_11
step11_raw=pd.read_csv("D:\Extra Knowledge\HP-NPC\dataset/exp6-step11-group-4.csv")
step11_raw["TimeShift"]=step11_raw.TimeStamp-step11_raw.TimeStamp[0]

step13_raw=pd.read_csv("D:\Extra Knowledge\HP-NPC\dataset/exp6-step13-group-3.csv")

step13_raw["TimeShift"]=step13_raw.TimeStamp-step13_raw.TimeStamp[0]

step18_raw=pd.read_csv("D:\Extra Knowledge\HP-NPC\dataset/exp6-step18-group-2.csv")
step18_fil=step18_raw.loc[234:, :]

step18_fil.reset_index(drop=True, inplace=True)

step18_fil["TimeShift"]=step18_fil.TimeStamp-step18_fil.TimeStamp[0]
step18_half_cycle=step18_fil[step18_fil.TimeShift<=period_2/2]

step27_raw=pd.read_csv("D:\Extra Knowledge\HP-NPC\dataset/exp6-step27-group-4.csv")
step27_fil=step27_raw.loc[0:, :]

step27_fil.reset_index(drop=True, inplace=True)

step27_fil["TimeShift"]=step27_fil.TimeStamp-step27_fil.TimeStamp[0]
step27_half_cycle=step27_fil[step27_fil.TimeShift<=period_2/2]


font = {'family': 'JetBrains Mono',
        'color':  'black',
        'weight': 'normal',
        'size': 15,
        }
fig, ax2=plt.subplots(figsize=(10,6))
ax2.plot(step2_g6_half_cycle.TimeShift, step2_g6_half_cycle.Position, color="red", 
       linewidth=1.5)

step2_tex=r"$f=0.2 Hz$, $A=80\%$, $K_p=0.14$"
ax2.text(1.0, 30, step2_tex, fontdict=font, color="DarkBlue", fontsize=20)

fig,ax6=plt.subplots(figsize=(10,6))
c_max=step6_half_cycle.Position.max()
c_final=step6_half_cycle.Position[step6_half_cycle.Position.shape[0]-1]
ax6.plot(step6_half_cycle.TimeShift, step6_half_cycle.Position, color="red", 
               linewidth=1.5)

step6_tex=r"$f=0.2 Hz$, $A=15\%$, $K_p=2$"
ax6.text(1.0, 20, step6_tex, fontdict=font, color="DarkBlue", fontsize=20)

ax6.scatter([0.09, 0.65], [c_max, c_final], color="DarkBlue")

fig, ax7=plt.subplots(figsize=(10,6))
ax7.plot(step7_half_cycle.TimeShift, step7_half_cycle.Position, color="red", 
       linewidth=1.5)

step7_tex=r"$f=0.2 Hz$, $A=15\%$, $K_p=3$"
ax7.text(1.0, 30, step7_tex, fontdict=font, color="DarkBlue", fontsize=20)

#plt.plot(step11_raw.TimeStamp, step11_raw.Position)
fig, ax11=plt.subplots(figsize=(10,6))
ax11.plot(step11_raw.TimeShift, step11_raw.Reference, color="DarkBlue", 
       linewidth=1.5, 
       label="Reference")
ax11.plot(step11_raw.TimeShift, step11_raw.Position, color="red", 
       linewidth=1.5, 
       label="Position(%)")

step11_tex=r"$f=0.10 Hz$, $A=10\%$, $K_p=1.0$"
ax11.text(2.1, 12, step11_tex, fontdict=font, fontsize=20)

fig, ax13=plt.subplots(figsize=(10,6))
ax13.plot(step13_raw.TimeShift, step13_raw.Reference, color="DarkBlue", 
       linewidth=1.5, 
       label="Reference")
ax13.plot(step13_raw.TimeShift, step13_raw.Position, color="red", 
       linewidth=1.5, 
       label="Position(%)")
step13_tex=r"$f=0.10 Hz$, $A=10\%$, $K_p=1.75$"
ax13.text(0.5, -15, step13_tex, fontdict=font, fontsize=20)

fig, ax18=plt.subplots(figsize=(10, 6))

ax18.plot(step18_half_cycle.TimeShift, step18_half_cycle.Reference, color="DarkBlue", 
       linewidth=1.5, 
       label="Reference")
ax18.plot(step18_half_cycle.TimeShift, step18_half_cycle.Position, color="red", 
       linewidth=1.5, 
       label="Position(%)")
step18_tex=r"$f=0.2 Hz$, $A=15\%$, $K_p=0.9$"
ax18.text(0.5, -15, step13_tex, fontdict=font, fontsize=20)

fig27, ax27=plt.subplots(figsize=(10,6))
ax27.plot(step27_raw.TimeStamp, step27_raw.Reference, color="DarkBlue", 
      linewidth=1.5, 
        label="Reference")
ax27.plot(step27_raw.TimeStamp, step27_raw.Position, color="red", 
        linewidth=1.5, 
        label="Position(%)")

step27_tex=r"$f=0.2 Hz$, $A=20\%$, $K_p=3.6$"
ax27.text(40, -10, step27_tex, fontdict=font, fontsize=20)

for ax in [ax2, ax6, ax7, ax11, ax13, ax18, ax27]:
    
    ax.set_facecolor("#F8E0C1")
    # Move the left and bottom spines to x = 0 and y = 0, respectively.
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    # Hide the top and right spines.
    ax.spines["top"].set_visible(False)

    ax.spines["right"].set_visible(False)

    ax.plot(1, 0, ">k", ms=12, transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", ms=12, transform=ax.get_xaxis_transform(), clip_on=False)
    ax.set_xlabel(xlabel="Time", fontsize=15)
    ax.set_ylabel(ylabel="Position(%)", rotation="horizontal", fontsize=15)
    ax.yaxis.set_label_coords(0.05,1.03)
    ax.xaxis.set_label_coords(1.04,0.0)
    ax.tick_params(axis="both", which="major", labelsize=15)
    ax.xaxis.set_label_coords(1.045,0.3)


plt.show()

