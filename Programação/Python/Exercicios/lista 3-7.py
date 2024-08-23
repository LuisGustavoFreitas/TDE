print()
print('     Conversão de metros para milhas')
print()
print('   Kilometros  |   Metros   |  Milhas')
print()
for km in range( 20 , 161 ,10):
    metros=km * 1000
    milhas = metros / 1609.344
    print(f' {km:10d} km | {metros: 8d} m | {milhas: .3f} mi')
