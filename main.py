import api, coh, overheads, profit_loss

def main():

    forex = api.api_function()
    overheads.overhead_function()
    coh.coh_function()
    profit_loss.profitloss_function()

main()

##SECOND WAY ? 

# import api, coh, overheads, profit_loss

# def main():

#     forex = api.api_function()
#     overheads.overhead_function(forex)
#     coh.coh_function(forex)
#     profit_loss.profitloss_function(forex)

# main()