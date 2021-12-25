import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

rail_ziegler=pd.read_csv("D:\L-3 T-2\python-control-system\python-control-system\dataset/exp8-rail-ziegler-nichols-group-5.csv", sep="\t")
rzn_zero=rail_ziegler[~(rail_ziegler.Position==0)]
ziegler_desire1=rzn_zero[(rzn_zero.TimeStamp>=10) & (rzn_zero.TimeStamp<=11.32)]
rail_ziegler_halfc=rzn_zero[(rzn_zero.TimeStamp>=10) & (rzn_zero.TimeStamp<=11.32)]
rail_ziegler_halfc["TimeShift"]=rail_ziegler_halfc.TimeStamp-10
fig, ax1=plt.subplots()
ax1.plot(rail_ziegler_halfc.TimeShift, rail_ziegler_halfc.Position, lw=2, color="DarkBlue")

rail_quater=pd.read_csv("D:\L-3 T-2\python-control-system\python-control-system\dataset/exp8-rail-quater-amp-group-5.csv", sep="\t")
rq_zero=rail_quater[~(rail_quater.Position==0)]
rail_quater_halfc=rq_zero[(rq_zero.TimeStamp>=5) & (rq_zero.TimeStamp<=6.5)]
rail_quater_halfc["TimeShift"]=rail_quater_halfc.TimeStamp-5
fig, ax2=plt.subplots()
ax2.plot(rail_quater_halfc.TimeShift, rail_quater_halfc.Position, lw=2, color="DarkBlue")
ax2.scatter([0.17, 0.5], [26.76, 14.58], marker="o", color="m")
ax2.annotate("(0.17,26.76)", xy=(0.17, 26.76), xytext=(0.3, 22), arrowprops={"arrowstyle": "->", "color":"m", "linewidth":2}, fontsize=15)
ax2.annotate("(0.5,14.58)", xy=(0.5, 14.58), xytext=(0.8, 12), arrowprops={"arrowstyle": "->", "color":"m", "linewidth":2}, fontsize=15)

rail_damp=pd.read_csv("D:\L-3 T-2\python-control-system\python-control-system\dataset/exp8-rail-sig-damp-group-5.csv", sep="\t")
rd_zero=rail_damp[~(rail_damp.Position==0)]
rail_damp_halfc=rd_zero[(rd_zero.TimeStamp>=5) & (rd_zero.TimeStamp<=5.5)]
rail_damp_halfc["TimeShift"]=rail_damp_halfc.TimeStamp-5
fig, ax3=plt.subplots()
ax3.plot(rail_damp_halfc.TimeShift, rail_damp_halfc.Position, lw=2, color="DarkBlue")

motor_ziegler=pd.read_csv("D:\L-3 T-2\python-control-system\python-control-system\dataset/exp8-motor-ziegler-nichols-group-5.csv", sep="\t")
motor_ziegler_halfc=motor_ziegler[(motor_ziegler.TimeStamp>=50) & (motor_ziegler.TimeStamp<=50.6)]
motor_ziegler_halfc["TimeShift"]=motor_ziegler_halfc.TimeStamp-50
fig, ax4=plt.subplots()
ax4.plot(motor_ziegler_halfc.TimeShift, motor_ziegler_halfc.Position, lw=2, color="DarkBlue")
ax4.scatter([0.08, 0.27], [6.9, 4.12], marker="o", color="m")
ax4.annotate("(0.08,6.9)", xy=(0.08, 6.9), xytext=(0.15, 6), arrowprops={"arrowstyle": "->", "color":"m", "linewidth":2}, fontsize=15)
ax4.annotate("(0.27,4.12)", xy=(0.27, 4.12), xytext=(0.35, 3), arrowprops={"arrowstyle": "->", "color":"m", "linewidth":2}, fontsize=15)

motor_quater=pd.read_csv("D:\L-3 T-2\python-control-system\python-control-system\dataset/exp8-motor-quater-amp-group-5.csv", sep="\t")
mq_zero=motor_quater[~(motor_quater.Position==0)]
motor_quater_halfc=mq_zero[(mq_zero.TimeStamp>=5) & (mq_zero.TimeStamp<=6.5)]
motor_quater_halfc["TimeShift"]=motor_quater_halfc.TimeStamp-5
fig, ax5=plt.subplots()
ax5.plot(motor_quater_halfc.TimeShift, motor_quater_halfc.Position, lw=2, color="DarkBlue")
ax5.scatter([0.11, 0.34], [21.86, 11.16], marker="o", color="m")
ax5.annotate("(0.11,21.86)", xy=(0.11, 21.86), xytext=(0.3, 17), arrowprops={"arrowstyle": "->", "color":"m", "linewidth":2}, fontsize=15)
ax5.annotate("(0.34,11.16)", xy=(0.34, 11.16), xytext=(0.5, 5), arrowprops={"arrowstyle": "->", "color":"m", "linewidth":2}, fontsize=15)

motor_damp=pd.read_csv("D:\L-3 T-2\python-control-system\python-control-system\dataset/exp8-motor-sig-damp-group-5.csv", sep="\t")
md_noise=motor_damp.loc[262:, :]
motor_damp_halfc=md_noise[(md_noise.TimeStamp>=5) & (md_noise.TimeStamp<=5.5)]
motor_damp_halfc["TimeShift"]=motor_damp_halfc.TimeStamp-5
fig, ax6=plt.subplots()
ax6.plot(motor_damp_halfc.TimeShift, motor_damp_halfc.Position)
axes_list=[ax1, ax2, ax3, ax4, ax5, ax6]
for ax in axes_list:
	ax.xaxis.set_minor_locator(AutoMinorLocator(3))
	ax.yaxis.set_minor_locator(AutoMinorLocator(3))

	ax.spines["left"].set_position(("data", 0))
	ax.spines["bottom"].set_position(("data", 0))
	ax.spines["top"].set_visible(False)
	ax.spines["right"].set_visible(False)

	#ax.set_facecolor("darkorange")
	ax.set_xlim(0)

	ax.plot(1, 0, ">k", ms=12, transform=ax.get_yaxis_transform(), clip_on=False)
	ax.plot(0, 1, "^k", ms=12, transform=ax.get_xaxis_transform(), clip_on=False)
	ax.set_xlabel(xlabel="t(s)", fontsize=15)
	ax.set_ylabel(ylabel="Position(%)", rotation="horizontal", fontsize=15)
	ax.yaxis.set_label_coords(0.05,1.03)
	ax.xaxis.set_label_coords(1.04,0.38)
	ax.tick_params(axis="both", which="major", labelsize=15)

	ax.grid(which="major", color="k", alpha=0.7)
	ax.grid(which="minor", color="gray", alpha=0.3)
plt.show()