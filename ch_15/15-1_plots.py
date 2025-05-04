import matplotlib.pyplot as plt

x_values = [125,512,1000,1331,4096]
y_values = [125,512,1000,1331,4096]
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

ax.plot(x_values,y_values,color = "orange", s=100)

#set chart and title and label axes
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick tables
ax.tick_params(labelsize=14)
plt.show()