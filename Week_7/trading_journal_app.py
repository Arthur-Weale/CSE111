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
    header = ["Trade Date", "Instrument","Position", "Entry Price", "Exit Price", "Stop Loss","Take Profit", "Lot Size","Result", "Status"]
    with open(csv_log_file , 'a', newline='') as file:
        write = csv.writer(file)

        if not file_exist:
            write.writerow(header)


def main():
    root = tk.Tk()
    root.title('Trading Journal')
    root.geometry('500x500')
    root.configure(bg='#16213e')

    main_frame = Frame(root)
    main_frame = tk.Frame(root)
    main_frame.pack(padx=10 , pady=10, fill=tk.BOTH ,expand=True)
    main_frame.configure(bg='#16213e')
    csv_check()
    populate_ui(main_frame)
    root.mainloop()

def populate_ui(main_frame):
    trade_date_label = tk.Label(main_frame, text='Trade Date')
    trade_date_label.configure(bg='#16213e', fg='white')
    trade_date_entry = tk.Entry(main_frame)
    
    instrument_label = tk.Label(main_frame, text='Instrument')
    instrument_label.configure(bg='#16213e', fg='white')
    instrument_entry = tk.Entry(main_frame)

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
            result_entry_str = result_entry.get()

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

            }

            print(trade_log_dict)

            with open(csv_log_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(trade_log_dict.values())

    """
    
    save_trade_to_csv(): Saves the trade data entered by the user to a CSV file.
    load_trades_from_csv(): Loads trade data from the CSV file to display in the GUI.
    calculate_profit_loss(): Calculates the profit or loss for each trade based on entry and exit prices.
    display_trade_history(): Displays the trade history in the GUI.
    filter_trades(): Allows the user to filter the displayed trades based on certain criteria (e.g., date range, strategy used).
    create_trade_log(): Writes important actions (such as saving a trade) into a TXT log file.
    calculate_win_rate(): Calculates the win rate based on the results of the trades (wins/losses).
    calculate_average_risk_reward(): Calculates the average risk-reward ratio of trades.


    """

    def calculate_profit_loss():
        """
        Profit/Loss=(Exit Price−Entry Price)×Lot Size
        """

    def display_trade_history():
        pass

    def load_trades_from_csv():
        pass

    def filter_trades():
        pass

    def create_trade_log():
        pass    

    def calculate_win_rate():   
        pass

    def calculate_average_risk_reward():            
        pass

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