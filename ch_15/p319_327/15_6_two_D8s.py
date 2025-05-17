from die import Die
import plotly.express as px

# Create a D6

die_1 =Die(8)
die_2 = Die(8) #Create instance of class Die
# make some rolls, and store results in a list
results = []
for roll_num in range(100000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
#anazyle the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2,max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)



title = "Results of rolling one d8 and a d8 100000times"
labels = {"x":"result","y" : "frequency of results"}
fig = px.bar(x=poss_results, y = frequencies,title=title, labels=labels)
fig.update_layout(xaxis_dtick =1)
fig.show()
print(frequencies)