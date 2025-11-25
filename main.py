import tkinter as tk
from tkinter import ttk

# root=tk.Tk()
# root.title("BattleCalc")

data={
    'run1':{'battles':34,'time':12},
    'run2':{'battles':30,'time':11},
    'run3':{'battles':12,'time':8},
}
matches_done=355
global_output=()
def calc():
    global global_output
    total_matches=data['run1']['battles']+data['run2']['battles']+data['run3']['battles']
    total_time=data['run1']['time']+data['run2']['time']+data['run3']['time']
    matches_per_min=total_matches/total_time
    matches_per_hour=matches_per_min*60
    global_output=(matches_per_min, matches_per_hour)
    return (matches_per_min, matches_per_hour)
def est_time():
    return (1000-matches_done)/global_output[0]
print(calc())
print(f'{int(est_time()//60)} hrs {int(round(est_time()%60,0))} min')