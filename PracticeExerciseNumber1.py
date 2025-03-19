provider_cost=0.51
provider_cost_perhour=provider_cost*60
provider_cost_perday=provider_cost_perhour*24
provider_cost_permonth=provider_cost_perday*30
print('How much does it cost to operate one server per day?')
print('It is {:.2f}'.format(provider_cost_perday))
print('How much does it cost to operate one server per month? ')
print('It is {:.2f}'.format(provider_cost_permonth))
