def caluculate_ticket_cost(age):
usd_to_inr=83
if 18<=age<=30:
    cost_usd=5
elif 30<age<=50:
    cost_usd=20
elif age>50:
    cost_usd=0
else:
    return"age below 18 is not eligiable for a ticket"
return
