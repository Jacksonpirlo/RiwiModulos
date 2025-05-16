from datetime import time
vuelos = {
"AV-101": {
    "origen": "Lima",
    "destino": "Bogotá",
    "asientos": ["A1", "A2", "B1", "B2"],
    "horario": (15, 30)
},

"AV-102": {
    "origen": "Caracas",
    "destino": "Tachira",
    "asientos": ["C1", "C2", "D1", "D2"],
    "horario": (15, 30)
},

"AV-103": {
    "origen": "Valencia",
    "destino": "Maracaibo",
    "asientos": ["E1", "E2", "F1", "F2"],
    "horario": (15, 30)
}
}

reserved = []

def see_flights():
    print('FLY RESERVATIONS')
    for vuelo in vuelos:
        print(f'ABOUT {vuelo}')
        print(f'LEAVE: {vuelos[vuelo]["origen"]}')
        print(f'ARRIVE: {vuelos[vuelo]["destino"]}')
        print(f'SEATS: {vuelos[vuelo]["asientos"]}')
        print(f'SCHEDULES: {vuelos[vuelo]["horario"]} \n')

def reserve_flights():
    reserve = input('Flight to reserve: ').upper()
    if reserve in vuelos.keys():
        print(f'Flight {reserve}')
        print(f'Free seats: {vuelos[reserve]['asientos']}')
        seat_reserve = input('Reserve a seat: ').upper()
        if seat_reserve in vuelos[reserve]["asientos"]:
            vuelos[reserve]["asientos"].remove(seat_reserve)
            print("SEAT SUCCESSFULLY RESERVED")
            print(f"SEAT: {seat_reserve.upper()}")
            reserved.append(seat_reserve.upper())
            print(reserved)
            do_you_want = input("Do you want to reserved another seat? yes / no: ")
            if do_you_want.lower() == "yes":
                reserve_flights()
            elif do_you_want.lower() == "no":
                print('Have a good trip')
                for vuelo in vuelos:
                    print(f'Your seats {reserved}')
                    print(f'Flight occupancy: {len(reserved) * 100 / len(vuelos[vuelo]["asientos"])}%')
                    with open('report.txt','a') as reporte:
                        reporte.write(f'''

                        Flight data
                        LEAVE: {vuelos[vuelo]["origen"]}
                        ARRIVE: {vuelos[vuelo]["destino"]}
                        SCHEDULES: {vuelos[vuelo]["horario"][0]}:{vuelos[vuelo]["horario"][1]}
                        SEATS: {vuelos[vuelo]["asientos"]}
                        Flight occupancy: {len(reserved) * 100 / len(vuelos[vuelo]["asientos"])}%
                        ''')
            else:
                print('Invalid argument')
                return
        else:    
            print('Seat not found')
            reserve_flights()
    else:
        print('flight not found')
        reserve_flights()

def main():
    while True:

        status = input('''

        WELCOME TO AVIANCA AIRPORT
                   
        PRESS:
                   1) See flights
                   2) Reserve flights
                   3) Print report


    ''')
    
        if status == "1":
            see_flights()
        elif status == "2":
            reserve_flights()

main()