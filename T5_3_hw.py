
invest = float(input('Сумма инвестиций: ')) 
mike = float(input('У Майка: '))
ivan = float(input('У Ивана: '))

if invest <= mike + ivan and invest <= mike and invest <= ivan: 
    print ('2')
elif invest <= mike + ivan and invest > mike and invest > ivan:
    print ('1')
elif invest <= mike:
    print ('Mike')
elif invest <= ivan:
    print ('Ivan')
else:
    print ('0')
