# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
cur_month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while True:
    cur_month = cur_month + 1
    cur_pay = payment
    if cur_month >= extra_payment_start_month and cur_month <= extra_payment_end_month:
        cur_pay = cur_pay+extra_payment
    if(principal > cur_pay):
        principal = principal * (1+rate/12) - cur_pay
        total_paid = total_paid+cur_pay
        print(f'{cur_month:4d}{total_paid:14.2f}{principal:14.2f}')
    else:
        total_paid = total_paid + principal
        principal = 0
        print(f'{cur_month:4d}{total_paid:14.2f}{principal:14.2f}')
        break

print(f'Total paid {total_paid:0.2f}')
print('Months', cur_month)
