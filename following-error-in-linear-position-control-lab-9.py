import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
#Read raw datasset 
raw=pd.read_csv("D:\L-3 T-2\python-control-system\python-control-system\dataset/exp9-group-1-2.csv")
remove_noise=raw.loc[4006:, :]#Remove unwanted position(%) data
#Select desired dataset
position_ref=remove_noise[(remove_noise.TimeStamp>200) & (remove_noise.TimeStamp<=230)]
speed=remove_noise[(remove_noise.TimeStamp>200) & (remove_noise.TimeStamp<=215)]
following_error=remove_noise[(remove_noise.TimeStamp>200) & (remove_noise.TimeStamp<=210)]
#plot time vs position
fig, ax1=plt.subplots()
ax1.plot(position_ref.TimeStamp, position_ref.Position, lw=2, color="DarkBlue")
#plot time vs reference
fig, ax2=plt.subplots()
ax2.plot(position_ref.TimeStamp, position_ref.Reference, lw=2, color="DarkOrange")
#position and reference in same plot
fig, ax3=plt.subplots()
ax3.plot(position_ref.TimeStamp, position_ref.Reference, lw=2, color="DarkOrange", label="Reference")
ax3.plot(position_ref.TimeStamp, position_ref.Position, lw=2, color="DarkBlue", label="Position")
#plot time vs speed
fig, ax4=plt.subplots()
ax4.plot(speed.TimeStamp, speed.Speed, color="DarkRed")
#plot time vs following error
fig, ax5=plt.subplots()
ax5.plot(following_error.TimeStamp, following_error.Error, lw=2, color="DarkGreen")
axes_list=[ax1, ax2, ax3, ax4, ax5]
ylabel=["Position(%)", "Reference", None, "Speed", "Following error"]
for ax, ylabel in zip(axes_list, ylabel):
	ax.xaxis.set_minor_locator(AutoMinorLocator(3))
	ax.yaxis.set_minor_locator(AutoMinorLocator(3))

	ax.spines["left"].set_position(("data", 200))
	ax.spines["bottom"].set_position(("data", 0))
	ax.spines["top"].set_visible(False)
	ax.spines["right"].set_visible(False)

	#ax.set_facecolor("darkorange")
	ax.set_xlim(200)

	ax.plot(1, 0, ">k", ms=12, transform=ax.get_yaxis_transform(), clip_on=False)
	ax.plot(200, 1, "^k", ms=12, transform=ax.get_xaxis_transform(), clip_on=False)
	ax.set_xlabel(xlabel="t(s)", fontsize=15)
	ax.set_ylabel(ylabel=ylabel, rotation="horizontal", fontsize=15)
	ax.yaxis.set_label_coords(0.04,1.03)
	ax.xaxis.set_label_coords(1.04,0.45)
	ax.tick_params(axis="both", which="major", labelsize=15)

	ax.grid(which="major", color="k", alpha=0.7)
	ax.grid(which="minor", color="gray", alpha=0.3)
ax3.legend(loc="upper center")
plt.show()