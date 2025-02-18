import tkinter as tk
from datetime import datetime
from tkinter import Frame
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import os
import csv

# Define the log filenames
csv_log_file = 'tradelog.csv'
txt_log_file = 'tradelog.txt'

# Check if the CSV file exists; if not, create it with headers
def csv_check():
    file_exist = os.path.exists(csv_log_file)
    header = ["Trade Date", "Instrument","Position", "Entry Price", "Exit Price", "Stop Loss","Take Profit", "Lot Size","Result", "Status", "Profit/Loss"]
    with open(csv_log_file , 'a', newline='') as file:
        write = csv.writer(file)

        if not file_exist:
            write.writerow(header)

# Main function to create the GUI window
def main():
    root = tk.Tk()
    root.title('Trading Journal')
    root.geometry('500x600')
    root.configure(bg='#16213e')

    main_frame = Frame(root)
    main_frame = tk.Frame(root)
    main_frame.pack(padx=10 , pady=10, fill=tk.BOTH ,expand=True)
    main_frame.configure(bg='#16213e')
    csv_check() # Check CSV file and add header if needed
    populate_ui(main_frame)   # Build the GUI layout
    root.mainloop()


# Function to create and place all widgets in the GUI
def populate_ui(main_frame):
    trade_date_label = tk.Label(main_frame, text='Trade Date')
    trade_date_label.configure(bg='#16213e', fg='white')
    trade_date_entry = tk.Entry(main_frame)
    
    instrument_label = tk.Label(main_frame, text='Instrument')
    instrument_label.configure(bg='#16213e', fg='white')
    instrument_entry = tk.Entry(main_frame)

    # Combobox for position (Long/Short)
    options= ['Long', 'Short']
    pos_variable = tk.StringVar(main_frame)
    pos_variable.set(options[0])
    position_label = tk.Label(main_frame, text='Position')
    position_label.configure(bg='#16213e', fg='white')
    position_entry = ttk.Combobox(main_frame, textvariable= pos_variable,state= 'readonly', values=options, width=17)
    position_entry.option_add('*TCombobox*Listbox.justify', 'center')
    
    entry_price_label = tk.Label(main_frame, text='Entry Price')
    entry_price_label.configure(bg='#16213e', fg='white')
    entry_price_entry = tk.Entry(main_frame)
    
    exit_price_label = tk.Label(main_frame, text='Exit Price')
    exit_price_label.configure(bg='#16213e', fg='white')
    exit_price_entry = tk.Entry(main_frame)
    
    stoploss_label = tk.Label(main_frame, text='Stop Loss')
    stoploss_label.configure(bg='#16213e', fg='white')
    stoploss_entry = tk.Entry(main_frame)
    
    lotsize_label = tk.Label(main_frame, text='Lot Size')
    lotsize_label.configure(bg='#16213e', fg='white')
    lotsize_entry = tk.Entry(main_frame)

    result_label = tk.Label(main_frame, text='Result')
    result_label.configure(bg='#16213e', fg='white')
    res_option = ['Win', 'Loss', 'Breakeven']
    res_variable = tk.StringVar(main_frame)
    result_entry = ttk.Combobox(main_frame, textvariable= res_variable, state='readonly', values=res_option, width=17)
    res_variable.set(res_option[0])
    
    status_label = tk.Label(main_frame, text='Status')
    status_label.configure(bg='#16213e', fg='white')
    status_display = tk.Label(main_frame, text="Pending", width=17)

    save_button = tk.Button(main_frame, text='Save Entry')
    save_button.configure(bg='#D50032', fg='#16213e')
    clear_button = tk.Button(main_frame, text='Clear Entry')
    clear_button.configure(bg='#D50032', fg='#16213e')

    take_profit_label = tk.Label(main_frame, text='Take Profit')
    take_profit_label.configure(bg='#16213e', fg='white')
    take_profit_entry = tk.Entry(main_frame)

    profit_loss_label = tk.Label(main_frame, text='Profit/Loss')
    profit_loss_label.configure(bg='#16213e', fg='white')
    profit_loss_display = tk.Label(main_frame, text="0.0", width=17)

    # Widget Placements
    trade_date_label.grid(column=0, row=0, sticky='w')
    trade_date_entry.grid(column=1, row=0, columnspan=50, padx=10 , pady=10)

    instrument_label.grid(column=0, row=1, sticky='w')
    instrument_entry.grid(column=1, row=1, columnspan=50, padx=10, pady=10)

    position_label.grid(column=0, row=2, sticky='w')
    position_entry.grid(column=1, row=2, padx=10, pady=10)

    entry_price_label.grid(column=0, row=3, sticky='w')
    entry_price_entry.grid(column=1, row=3, columnspan=50, padx=10, pady=10)

    exit_price_label.grid(column=0, row=4, sticky='w')
    exit_price_entry.grid(column=1, row=4, columnspan=50, padx=10, pady=10)

    stoploss_label.grid(column=0, row=5, sticky='w')
    stoploss_entry.grid(column=1, row=5, columnspan=50, padx=10, pady=10)

    lotsize_label.grid(column=0, row=6, sticky='w')
    lotsize_entry.grid(column=1, row=6, columnspan=50, padx=10, pady=10)

    result_label.grid(column=0, row=7, sticky='w')
    result_entry.grid(column=1, row=7, padx=10, pady=10)

    take_profit_label.grid(column=0, row=8, sticky='w')
    take_profit_entry.grid(column=1, row=8, columnspan=50, padx=10, pady=10)

    status_label.grid(column=0, row=9, sticky='w')
    status_display.grid(column=1, row=9, columnspan=50, padx=10, pady=10)

    save_button.grid(column=0, row=10, padx=10, pady=10)
    clear_button.grid(column=1, row=10, padx=10, pady=10)

    profit_loss_label.grid(column=0, row=11, sticky='w')
    profit_loss_display.grid(column=1, row=11, columnspan=50, padx=10, pady=10)

    # Win Rate Label
    win_rate_label = tk.Label(main_frame, text='Win Rate')
    win_rate_label.configure(bg='#16213e', fg='white')
    win_rate_display = tk.Label(main_frame,  width=17)
    win_rate_label.grid(column=0, row=12, columnspan=2, padx=10, pady=10, sticky='w')
    win_rate_display.grid(column=1, row=12, columnspan=2, padx=10, pady=10, sticky='w')

    # Average Risk-Reward Label
    average_rr_label = tk.Label(main_frame, text='Average RR')
    average_rr_label.configure(bg='#16213e', fg='white')
    average_rr_display = tk.Label(main_frame, width=17)
    average_rr_label.grid(column=0, row=13, columnspan=2, padx=10, pady=10, sticky='w')
    average_rr_display.grid(column=1, row=13, columnspan=2, padx=10, pady=10, sticky='w')
    

    def save_trade_to_csv():
        try:
            # Get values from the UI
            trade_date_entry_str = trade_date_entry.get()
            instrument_entry_str = instrument_entry.get()  
            trade_position = position_entry.get()
            entry_price_entry_str = entry_price_entry.get()
            exit_price_entry_str = exit_price_entry.get()
            stoploss_entry_str = stoploss_entry.get()
            take_profit_entry_str = take_profit_entry.get()
            lotsize_entry_str = lotsize_entry.get()
            result_entry_str = result_entry.get()
            profit_or_loss = calculate_profit_loss()

            entry_date = trade_date_entry_str
            entry_price = float(entry_price_entry_str)
            exit_price = float(exit_price_entry_str)
            stoploss = float(stoploss_entry_str)
            take_profit = float(take_profit_entry_str)
            lotsize = float(lotsize_entry_str)

        except ValueError as e:
            status_display.config(text="Invalid Input on one or more fields")
        else:
            status_display.config(text="Saved")
            # Build dictionary for the trade log
            trade_log_dict = {
                "Trade Date": entry_date,
                "Instrument": instrument_entry_str,
                "Position": trade_position ,
                "Entry Price": entry_price,
                "Exit Price": exit_price,
                "Stop Loss": stoploss,
                "Take Profit": take_profit,
                "Lot Size" : lotsize,
                "Result": result_entry_str,
                "Status": status_display.cget('text'),
                "Profit/Loss": profit_or_loss
            }

            print(trade_log_dict)
            create_trade_log(trade_log_dict)

            with open(csv_log_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(trade_log_dict.values())

            win_rate = calculate_win_rate()
            average_rr = calculate_average_risk_reward()
            win_rate_display.config(text=f"{win_rate:.2f}%")
            average_rr_display.config(text=f"{average_rr:.2f}")
            return trade_log_dict
            

        #debug code...................................................
        #result_entry.bind("<keyRelease>",calculate_win_rate())
        #result_entry.bind("<KeyRelease>", calculate_average_risk_reward())
        #calculate_win_rate()
        #calculate_average_risk_reward()

    def calculate_profit_loss():
        """
        Profit/Loss=(Exit_Price-Entry_Price) * Lot_Size
        """
        trade_position = position_entry.get()
        entry_price_entry_str = entry_price_entry.get()
        exit_price_entry_str = exit_price_entry.get()
        stoploss_entry_str = stoploss_entry.get()
        lotsize_entry_str = lotsize_entry.get()

        try:
            entry_price = float(entry_price_entry_str)if entry_price_entry_str else 0
            exit_price = float(exit_price_entry_str)if exit_price_entry_str else 0
            lotsize = float(lotsize_entry_str) if lotsize_entry_str else 0
            
            if trade_position == 'Long':
                profit_loss = (exit_price - entry_price) * lotsize
            else:
                profit_loss = (entry_price - exit_price) * lotsize

            profit_loss_display.config(text= f"{profit_loss}")
            return profit_loss

        except ValueError:
            print("Invalid input: Please enter numbers only.")
        except UnboundLocalError:
            print("lotsize should be an number value")
            return 0

    lotsize_entry.bind("<KeyRelease>",calculate_profit_loss ())
    
    

    def create_trade_log(trade_log_dict):
        # trade_logs = save_trade_to_csv()
        with open('tradelog.txt', 'a', newline= '') as txt_file:
            txt_file.write("New Trade Entry:\n")
            for key, value in trade_log_dict.items():
                print(f'{key}: {value}\n')
                txt_file.write(f'{key}: {value}\n')
            txt_file.write("\n" + "-"*20 + "\n\n")  # Separator between entries

    def clear_entry():
        trade_date_entry.delete(0, "end")
        instrument_entry.delete(0, "end")
        entry_price_entry.delete(0, "end")
        exit_price_entry.delete(0, "end")
        stoploss_entry.delete(0, "end")
        lotsize_entry.delete(0, "end")
        status_display.config(text="Pending")
        position_entry.set("")
        result_entry.set("")
        take_profit_entry.delete(0, "end")
        win_rate_display.config(text="")
        average_rr_display.config(text="")
        profit_loss_display.config( text="")

    # Bind Save and Clear button commands

    save_button.config(command=save_trade_to_csv)
    # save_button.config( command=calculate_win_rate)
    # save_button.config( command=calculate_average_risk_reward)
    clear_button.config( command=clear_entry)

def calculate_win_rate(csv_filename=csv_log_file):
    """
    Win Rate = (Number of Winning Trades / Total Number of Trades) * 100
    """   
    try:
        with open(csv_filename, 'r') as file:
            reader = csv.DictReader(file)
            trades = list(reader)
            total_trades = len(trades)
            if total_trades == 0:
                return 0.0
            wins = sum(1 for trade in trades if trade['Result'].lower() == 'win')
            win_rate = (wins / total_trades) * 100
            #win_rate_display.config(text = f"{win_rate}")
            print(win_rate) #debug
            return win_rate
    except FileNotFoundError:
        return 0.0

def calculate_average_risk_reward(csv_filename=csv_log_file):
    try:
        with open(csv_filename, 'r') as file:
            reader = csv.DictReader(file)
            profits = []
            losses = []
            for trade in reader:
                pnl = float(trade['Profit/Loss'])
                if pnl > 0:
                    profits.append(pnl)
                elif pnl < 0:
                    losses.append(abs(pnl))
            if not profits or not losses:
                return 0.0
            avg_profit = sum(profits) / len(profits)
            avg_loss = sum(losses) / len(losses)
            average_rr = avg_profit / avg_loss
            print(average_rr) #debug
            return average_rr
    except FileNotFoundError:
        return 0.0
    average_rr_display.config(text=f"{average_rr}")




if __name__ == '__main__':
    main()