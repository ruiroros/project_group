from pathlib import Path
import csv, requests

coh_fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv" 

def coh_function():
    cash_on_hand = []
    days = []

    with coh_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        cash_read = csv.reader(file)
        next(cash_read)
        
        for line in cash_read:
            coh = line[1]
            cash_on_hand.append(coh)

            day = line[0]
            days.append(day)
        
            x = 1
        
        try:
            while x < len(cash_on_hand):
                api_key = "0PXEE709XYMK7M42"
                url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
                response = requests.get(url)
                info = response.json()
                forex = float(info['Realtime Currency Exchange Rate']['5. Exchange Rate'])

                difference = float(cash_on_hand[x]) - float(cash_on_hand[x-1])
                x += 1
                if difference <= 0:
                    message = f"[CASH DEFICIT] DAY: {days[x-1]}, AMOUNT: SGD{abs(difference*forex)} "

                else:
                    continue 
                return message 

            if difference > 0:
                message = f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY "
                return message

        except ValueError:
            print("Please enter an appropriate value according to the argument type.")
        
        except TypeError:
            print("Please apply an appropriate operation or function according to the object type.")


print(coh_function())
