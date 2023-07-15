fruit = {'apple':150,
         'durian':300,
         'orange':50}

while True:
    product = input('กรุณาเลือกสินค้า: apple, durian, orange: ')
    quantity = float(input('จำนวนสินค้า กี่ิกิโลกรัม: '))
    print(quantity * fruit[product])
    print('--------')
