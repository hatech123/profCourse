import requests
import json
import tkinter as tk
endpoint_device = 'https://api.weather.yandex.ru/v2/informers?lat=55.75396&lon=37.620393&extra=true'
headers = {'X-Yandex-API-Key': '7db1ea84-a07c-4bfc-937a-bf45c29adca0'}
r_dev = requests.get(endpoint_device, headers=headers, verify=False)
print(r_dev)
j_dev = json.loads(r_dev.text)
# print(json.dumps(j_dev, indent=4))
#
# with open('weather.json', 'w') as f:
#     json.dump(j_dev, f)
t=j_dev["fact"]["temp"]
h=j_dev["fact"]["humidity"]
c=j_dev["fact"]["condition"]
print(c)
window=tk.Tk()
window.geometry("200x200")
label=tk.Label(text="температура "+str(t),relief=tk.RAISED,width=20)
label.pack()
label1=tk.Label(text="влажность "+str(h),relief=tk.RAISED,width=20)
label1.pack()
label2=tk.Label(text="условия "+str(c),relief=tk.RAISED,width=20)
label2.pack()
window.mainloop()