import tkinter as tk
from datetime import datetime
from tkinter import Frame
from tkinter import ttk
import os
import csv


csv_log_file = 'tradelog.csv'
# trade_date_entry = None
# instrument_entry = None
# entry_price_entry = None
# exit_price_entry = None
# stoploss_entry = None
# lotsize_entry = None
# status_display = None


def csv_check():
    file_exist = os.path.exists(csv_log_file)
    header = ["Trade Date", "Instrument","Position", "Entry Price", "Exit Price", "Stop Loss","Take Profit", "Lot Size", "Status"]
    with open(csv_log_file , 'a', newline='') as file:
        write = csv.writer(file)

        if not file_exist:
            write.writerow(header)


def main():
    root = tk.Tk()
    root.title('Trading Journal')
    root.geometry('400x400')

    main_frame = Frame(root)
    main_frame = tk.Frame(root)
    main_frame.pack(padx=10 , pady=10, fill=tk.BOTH ,expand=True)
    csv_check()
    populate_ui(main_frame)
    root.mainloop()

def populate_ui(main_frame):
    trade_date_label = tk.Label(main_frame, text='Trade Date')
    trade_date_entry = tk.Entry(main_frame)
    
    instrument_label = tk.Label(main_frame, text='Instrument')
    instrument_entry = tk.Entry(main_frame)

    options= ['Long', 'Short']
    pos_variable = tk.StringVar(main_frame)
    pos_variable.set(options[0])
    position_label = tk.Label(main_frame, text='Position')
    position_entry = ttk.Combobox(main_frame, textvariable= pos_variable,state= 'readonly', values=options)
    
    entry_price_label = tk.Label(main_frame, text='Entry Price')
    entry_price_entry = tk.Entry(main_frame)
    
    exit_price_label = tk.Label(main_frame, text='Exit Price')
    exit_price_entry = tk.Entry(main_frame)
    
    stoploss_label = tk.Label(main_frame, text='Stop Loss')
    stoploss_entry = tk.Entry(main_frame)
    
    lotsize_label = tk.Label(main_frame, text='Lot Size')
    lotsize_entry = tk.Entry(main_frame)
    
    status_label = tk.Label(main_frame, text='Status')
    status_display = tk.Label(main_frame, width=30, text="Pending")

    save_button = tk.Button(main_frame, text='Save')
    clear_button = tk.Button(main_frame, text='Clear')

    take_profit_label = tk.Label(main_frame, text='Take Profit')
    take_profit_entry = tk.Entry(main_frame)


    # Widget Placements
    trade_date_label.grid(column=0, row=0, sticky='w')
    trade_date_entry.grid(column=1, row=0)

    instrument_label.grid(column=0, row=1, sticky='w')
    instrument_entry.grid(column=1, row=1)

    
    position_label.grid(column=0, row=2, sticky='w')
    position_entry.grid(column=1, row=2, columnspan=5)

    entry_price_label.grid(column=0, row=3, sticky='w')
    entry_price_entry.grid(column=1, row=3)

    exit_price_label.grid(column=0, row=4, sticky='w')
    exit_price_entry.grid(column=1, row=4)

    stoploss_label.grid(column=0, row=5, sticky='w')
    stoploss_entry.grid(column=1, row=5)

    lotsize_label.grid(column=0, row=6, sticky='w')
    lotsize_entry.grid(column=1, row=6)

    take_profit_label.grid(column=0, row=7, sticky='w')
    take_profit_entry.grid(column=1, row=7)

    status_label.grid(column=0, row=8, sticky='w')
    status_display.grid(column=1, row=8)

    save_button.grid(column=0, row=9, padx=10, pady=10)
    clear_button.grid(column=1, row=9, padx=10, pady=10)


    def save_trade_to_csv():
        try:
            trade_date_entry_str = trade_date_entry.get()
            instrument_entry_str = instrument_entry.get()  
            trade_position = position_entry.cget()
            entry_price_entry_str = entry_price_entry.get()
            exit_price_entry_str = exit_price_entry.get()
            stoploss_entry_str = stoploss_entry.get()
            take_profit_entry_str = take_profit_entry.get()
            lotsize_entry_str = lotsize_entry.get()

            entry_date = datetime.strptime(trade_date_entry_str, "%Y-%m-%d")
            entry_price = float(entry_price_entry_str)
            exit_price = float(exit_price_entry_str)
            stoploss = float(stoploss_entry_str)
            take_profit = float(take_profit_entry_str)
            lotsize = float(lotsize_entry_str)

        except ValueError as e:
            status_display.config(text="Invalid Input on one or more fields")
        else:
            status_display.config(text="Saved")

            trade_log_dict = {
                "Trade Date": entry_date,
                "Instrument": instrument_entry_str,
                "Position": trade_position ,
                "Entry Price": entry_price,
                "Exit Price": exit_price,
                "Stop Loss": stoploss,
                "Take Profit": take_profit,
                "Lot Size" : lotsize,
                "Status": status_display.cget('text')
            }

            print(trade_log_dict)

            with open(csv_log_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(trade_log_dict.values())

    def clear_entry():
        trade_date_entry.delete(0, "end")
        instrument_entry.delete(0, "end")
        entry_price_entry.delete(0, "end")
        exit_price_entry.delete(0, "end")
        stoploss_entry.delete(0, "end")
        lotsize_entry.delete(0, "end")
        status_display.config(text="")

    save_button.config(command=save_trade_to_csv)
    clear_button.config( command=clear_entry)


if __name__ == '__main__':
    main()