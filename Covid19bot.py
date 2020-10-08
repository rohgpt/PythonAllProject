import time
from win10toast import ToastNotifier
import requests

def gen():
  try:
    r=requests.get("https://api.covid19api.com/summary")
    r=r.json()
    i=0
    while(r["Countries"][i]["Country"]!="India"):
      i+=1
    text=f'today covid19 Track of {r["Countries"][i]["Country"]} :NewCase {r["Countries"][i]["NewConfirmed"]},TotalCase {r["Countries"][i]["TotalConfirmed"]},Total death:{r["Countries"][i]["TotalDeaths"]}'
    while(True):
      toast=ToastNotifier()
      toast.show_toast("covid19 india",text,duration=10)
      time.sleep(2)
  except requests.exceptions.ConnectionError:
    print("Connection error")
gen()
