summa=float(input("Введите общую сумму накоплений: "))
claim=float(input("Введите текущую сумму покупки: "))
if summa<0 or claim<0:
    print("Input error")
else:
    if summa<500:
        discont=0
    elif 500<=summa<=999:
        discont=5
    elif 1000<=summa<=4999:
        discont=10
    elif 5000<=summa:
        discont=15
    if claim>1000:
        add_discont=10
    elif claim>300:
        add_discont=5
    elif claim<=300:
        add_discont=0
    all_discont=discont+add_discont
    if all_discont>25:
       all_discont=25
    pay=claim-((all_discont*claim)/100)
    print(f"Итоговая скидка: {all_discont} %")
    print(f"Сумма к оплате с учетом скидки: {pay}")
    

   