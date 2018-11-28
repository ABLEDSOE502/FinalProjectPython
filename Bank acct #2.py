#import tkinter
from tkinter import *

#define constants used for fonts
HEADER_FONT = "Arial", 14
BUTTON_FONT = "Arial", 10
NORMAL_FONT = "Arial", 12 
PROMPT_FONT = "Arial", 12, "italic"

#define main class
class BankManager:
    def __init__(self):
        window = Tk()
        window.title("Friendly Bank")
        window["bg"] = "dark olive green"

        welcome = Label(window, text = "Welcome to the Friendly Bank account manager app!", font = HEADER_FONT, fg = "gray99")
        welcome.grid(row = 0, column = 0, columnspan = 4)
        welcome["bg"] = "dark olive green"
        
        balance = Button(window, text = "Check account balance", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = BalancePage)
        balance.grid(row = 1, column = 0)

        deposit = Button(window, text = "Make a deposit", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = DepositPage)
        deposit.grid(row = 1, column = 1)

        withdrawal = Button(window, text = "Make a withdrawal", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = WithdrawalPage)
        withdrawal.grid(row = 1, column = 2)

        transfer = Button(window, text = "Make a transfer", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = TransferPage)
        transfer.grid(row = 1, column = 3)

        #add image to welcome screen
        moneyPic = PhotoImage(file = "F:\money-2724241_960_720.gif")
        label = Label(image = moneyPic)
        label.image = moneyPic
        label.grid(row = 3, column = 0, columnspan = 4)  

#create window to see balance of accounts
class BalancePage:
    def __init__ (self):
        window = Toplevel()
        window.title("Balance")
        window["bg"] = "dark olive green"
        
        checkBalance = Label(window, text = "What account would you like to view?", font = HEADER_FONT, fg = "gray99")
        checkBalance.grid(row = 0, column = 0, columnspan = 2)
        checkBalance["bg"] = "dark olive green"
        
        checkingBtn = Button(window, text = "Checking Account", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = CheckingPage)
        checkingBtn.grid(row = 1, column = 0)
        
        savingsBtn = Button (window, text = "Savings Account", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = SavingsPage)
        savingsBtn.grid(row = 1, column = 1)

#create window to make deposits
class DepositPage:
    def __init__(self):
        window = Toplevel()
        window.title("Deposits")
        window["bg"] = "dark olive green"
        
        makeDeposit = Label(window, text = "Where would you like to make the deposit?", font = HEADER_FONT, fg = "gray99")
        makeDeposit.grid(row = 0, column = 0, columnspan = 2)
        makeDeposit["bg"] = "dark olive green"
        
        savingsBtn = Button(window, text = "Savings Account", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = SavingsPage)
        savingsBtn.grid(row = 1, column = 0)

        checkingBtn  = Button(window, text = "Checking Account", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = CheckingPage)
        checkingBtn.grid(row = 1, column = 1)


#create window to make withdrawals
class WithdrawalPage:
    def __init__ (self):
        window = Toplevel()
        window.title("Withdrawals")
        window["bg"] = "dark olive green"
        
        label = Label (window, text = "What account would you like to make a withdrawal from?", font = HEADER_FONT, fg = "gray99")
        label.grid(row = 0, column = 0, columnspan = 2)
        label["bg"] = "dark olive green"
        
        checkingBtn = Button(window, text = "Checking Account", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = CheckingPage)
        checkingBtn.grid(row = 1, column = 0)
        
        savingsBtn = Button (window, text = "Savings Account", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = SavingsPage)
        savingsBtn.grid(row = 1, column = 1)

#create window for transfer
class TransferPage:
    def __init__ (self):
        window = Toplevel()
        window.title("Transfers")
        window["bg"] = "dark olive green"
        
        transBalance = Label(window, text = "Which account would you like to make a transfer from?", font = HEADER_FONT, fg = "gray99")
        transBalance.grid(row = 0, column = 0, columnspan = 2)
        transBalance["bg"] = "dark olive green"
        
        checkingBtn = Button(window, text = "Checking Account", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = CheckingPage)
        checkingBtn.grid(row = 1, column = 0)
        
        savingsBtn = Button(window, text = "Savings Account", font = BUTTON_FONT, bg = "olive drab", fg = "gray99", command = SavingsPage)
        savingsBtn.grid(row = 1, column = 1)


#create window to deposit into savings account
class SavingsPage:
    def __init__(self):
        window = Toplevel()
        window.title("Savings Account")
        window["bg"] = "dark olive green"
        
        label = Label(window, text = "How much would you like to deposit?", font = PROMPT_FONT, fg = "gray99")
        label.pack()
        label["bg"] = "dark olive green"
        
        entrySavings = Entry(window)
        entrySavings.pack()

#create window to deposit into checking account
class CheckingPage:
    def __init__(self):
        window = Toplevel()
        window.title("Checking Account")
        window["bg"] = "dark olive green"
        
        label = Label(window, text = "How much would you like to deposit?", font = PROMPT_FONT, fg = "gray99")
        label.pack()
        label["bg"] = "dark olive green"
        
        entryChecking = Entry(window)
        entryChecking.pack()
        
        window.mainloop()
BankManager()
