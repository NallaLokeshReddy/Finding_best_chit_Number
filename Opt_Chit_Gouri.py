# This is used to find out the best month on which highest interest rate 
# will be obtained. You have to update the previous paid amounts in the 
# program.

# The optimisation method includes the interest obtained from an external
# source by lending bid winning amount.


Paid_amt = dict()             # This has user defined Paid amounts for months upto chit months happened and for upcoming cht months, max_Paid_amt is taken as Paid amount.
# Updation of Previous months Paid amounts Begins
Paid_amt['Chit No:1'] = 10100
Paid_amt['Chit No:2'] = 10100
Paid_amt['Chit No:3'] = 10600
Paid_amt['Chit No:4'] = 11100
Paid_amt['Chit No:5'] = 11300
Paid_amt['Chit No:6'] = 11700
Paid_amt['Chit No:7'] = 11800
Paid_amt['Chit No:8'] = 11600
Paid_amt['Chit No:9'] = 12200
Paid_amt['Chit No:10'] = 13100
Paid_amt['Chit No:11'] = 13450
# Updation of Previous months Paid amounts ends

# Pooled amount is the sum of club owner commision per month and the ...
#.... amount collected by the last bid winner.

max_bidwin_amt = dict()         # This is the maximum amount that bid winner gets on every month
min_bid_amt = dict()            # This is Inital Bid amount on every month
max_Paid_amt = dict()           # This is the maximum/worst amount paid on every month.
PT = dict()                     # This is part of Interest calculation i.e., PT/100.
PT_sum = dict()
Gain_ext = dict()                    # PT[str(n)], n indicates the multiplication factor but not chit number
Int_Rate = dict()
Profit_amt = dict()

def returnSum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i
    return str(sum)

# Asking for Pooled Amount
while True:
    inp = input('Enter the Pooled amount in Rs: ')
    try:
        pooled_amount = float(inp)
        break
    except:
        print('\n Enter a valid numeric input for the Pooled amount \n')
        continue

# Asking for club owner commission in percentage
while True:
    inp0 = input('Enter the club owner commission in percentage: ')
    try:
        commission = float(inp0)*pooled_amount/100   # club owner gets this amount every month
        break
    except:
        print('\n Enter a valid numeric input for the commission \n')
        continue

Previous_chitno = len(Paid_amt)
Coming_chitno = Previous_chitno + 1

# Maximum bid win amount is calculated such that winner pays interest of
# Rs:1/- pm on a bid win amount
def max_bidwin_amount(p, c, m):        # p: pooled amount, c = club owner commision in Rs per month, m = chit number
    a = 1 + ((20 - m) / 100)
    return str( (p - c) / a )
# Note: max_bidwin_amount is a user defined function.
    
# Minimum bid amount dictionary calculation begins
d = 1
while d <= 20:
    e = 'Chit No:'+str(d)
    max_bidwin_amt[e] = int( float( max_bidwin_amount(pooled_amount, commission, d) ) )
    min_bid_amt[e] = pooled_amount - max_bidwin_amt[e]
    d = d + 1
print('\n Minimum or starting Bid amounts for every Month are as follows:')
print(min_bid_amt,'\n')
# Minimum bid amount dictionary calculation ends

# Maximum paid amount dictionary calculation begins
ab = 1
while ab <= 20:
    max_Paid_amt['Chit No:'+str(ab)] = ( max_bidwin_amt['Chit No:'+str(ab)] + commission ) / 20
    ab = ab + 1
# Maximum paid amount dictionary calculation ends

# Paid Amount dictionary calculation begins
Ccn0 = Coming_chitno
while Ccn0 <= 20 :
    Paid_amt['Chit No:'+str(Ccn0)] = max_Paid_amt['Chit No:'+str(Ccn0)]
    Ccn0 = Ccn0 + 1
# Paid Amount dictionary calculation ends

Paid_amt_sum = float( returnSum(Paid_amt) )

Ccn = Coming_chitno
Ccn1 = Coming_chitno
# Interest calculation for all the upcoming months begins
while Ccn <= 20:
    Ur_bidwin_amt = max_bidwin_amt['Chit No:'+str(Ccn)]         # Bid winning amount is the amount collected by the bid winner from all the club members
# PT/100 list calculation begins
    n = Ccn - 1
    while n > 0:
        PT[str(n)] = (Ccn - n) * Paid_amt['Chit No:'+str(n)] / 100
        n = n-1
    f = Ccn
    while f <= 20 :
        PT[str(f)] = (20 - f) * Paid_amt['Chit No:'+str(f)] / 100
        f = f + 1
# PT/100 list calculation ends

    def returnSum(dict):
        sum = 0
        for i in dict.values():
            sum = sum + i
        return str(sum)

    PT_sum['Chit No:'+str(Ccn)] = float( returnSum(PT) )

# Asking for the availability of external Interest payer begins
    while Ccn1 == Coming_chitno:
        inp4 = input('\n Have you found a customer to pay you interest on bid winning amount: Yes/No ? ')
        if inp4 == 'Yes' :
            while True:
                inp5 = input('\n What is the deal of interest rate in Rs: ')
                try:
                    R = float(inp5)
                    break
                except:
                    print('\n Enter a valid numeric input for interest rate  \n')
                    continue

        elif inp4 == 'No' :
            Ccn1 = Ccn1 + 1
            break
        else:
            continue
        Ccn1 = Ccn1 + 1
# Asking for the availability of external Interest payer ends

    while True:
        if inp4 == 'Yes' :
            Gain_ext['Chit No:'+str(Ccn)] = Ur_bidwin_amt * (20 - Ccn) * R / 100          # It is the amount recieved by giving bid win amount for interest
            Profit_amt['Chit No:'+str(Ccn)] = Ur_bidwin_amt - Paid_amt_sum
            Int_Rate['Chit No:'+str(Ccn)] = ( Profit_amt['Chit No:'+str(Ccn)] + Gain_ext['Chit No:'+str(Ccn)] ) / PT_sum['Chit No:'+str(Ccn)]
            break
        else:
            Profit_amt['Chit No:'+str(Ccn)] = Ur_bidwin_amt - Paid_amt_sum
            Int_Rate['Chit No:'+str(Ccn)] = Profit_amt['Chit No:'+str(Ccn)] / PT_sum['Chit No:'+str(Ccn)]
            break

    Ccn = Ccn + 1
# Interest calculation for all the upcoming months ends

Opt_Int_Rate = max(Int_Rate.values())
print('\n Paid amount: ', Paid_amt)
print('\n Sum of Paid amounts is: ', Paid_amt_sum)
print('\n Minimum Proft amounts will be as follows: ', Profit_amt)
print('\n Interests obtained on bid winning amount will be as follows: ', Gain_ext)
print('\n Minimum Interest rates will be as follows: ', Int_Rate)

# Searching for a corresponding key of Opt_Int_Rate value in Int_Rate dictionary begins
for chit_no, interest in Int_Rate.items():
    if interest == Opt_Int_Rate:
        print('\n The best month to be a bid winner: ', chit_no)
# Searching for a corresponding key of Opt_Int_Rate value in Int_Rate dictionary ends
print('\n Maximum Interest rate is: ', Opt_Int_Rate)
