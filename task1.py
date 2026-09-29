m=int(input("Введите количество собранных грибов: "))
if m<0:
    print("Input error!")
elif 11<=m%100<=20:
    print(f"Мы собрали {m} грибов")
elif 2<=m%10<=4:
    print(f"Мы собрали {m} гриба")
elif m%10==1:
    print(f"Мы собрали {m} гриб")
else:
    print(f"Мы собрали {m} грибов")



