import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import askinteger
root=tk.Tk()
root.title("BattleCalc")

data={'run1':{'battles':0,'time':0},'run2':{'battles':0,'time':0},'run3':{'battles':0,'time':0}}
matches_done=0
global_output=()
def begin_calc():
    global matches_done
    matches_done=askinteger("Completed Battles","Enter the number of battles you have done so far:")
    output=calc()
    est=est_time()
    result_text=f"Matches per minute: {output[0]:.4f}\nMatches per hour: {output[1]:.2f}\nMatches remaining: {1000-matches_done}\nEstimated time to 1000 matches: {int(est//60)} hours and {int(est%60)} seconds"
    result_label=ttk.Label(root,text=result_text)
    result_label.grid(row=4,column=0,columnspan=2,padx=10,pady=10)
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
def input_run(run_number:int):
    global completed_messages
    battles=askinteger(f"Set #{run_number}","Enter number of battles:")
    time=askinteger(f"Set #{run_number}","Enter time in minutes (rounded up):")
    data[f'run{run_number}']={'battles':battles,'time':time}
    completed_messages[run_number-1].config(text="Inputed!")
input_buttons=[]
completed_messages=[]
for set_num in range(1,4):
    input_buttons.append(ttk.Button(root, text=f"Input Set #{set_num}", command=lambda n=set_num: input_run(n)))
    input_buttons[-1].grid(row=set_num-1,column=0,padx=10,pady=10)
    completed_messages.append(ttk.Label(text=""))
    completed_messages[-1].grid(row=set_num-1,column=1,padx=10,pady=10)
calc_button=ttk.Button(root,text="Calculate!",command=begin_calc)
calc_button.grid(row=3,column=0,padx=10,pady=10,columnspan=2)
root.mainloop()