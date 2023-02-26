import pandas as pd
import matplotlib.pyplot as plt
# data={"Bob":23,"Oleg":17,"Sasha":54,"Dod":24,"MIke":76}
data={"Bob":[23],"Oleg":[17],"Sasha":[54],"Dod":[24],"MIke":[76]}
pd_frame=pd.DataFrame.from_dict(data)
pd_frame.to_csv("data.csv",index=False,sep=";")
lists=data.items()
x,y=zip(*lists)
print(x,y)
y=list(y)
y=[item[0] for item in y]
print(y)
fig, ax = plt.subplots()
# bar_labels = x
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange','tab:green']
ax.bar(x, y, color=bar_colors)
plt.show()