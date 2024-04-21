class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        

    def entry_show(self,movie_name,id, time):
        new_show = (movie_name,id, time)
        self.__show_list.append(new_show)
        self.__seats[id] = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
       

    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            print("Show ID is Invalid")
            return
        
        for row, col in seat_list:
            if row >= 0 and row < self.__rows or col >= 0 and col < self.__cols:
                if self.__seats[id][row][col] == 0:
                    self.__seats[id][row][col] = 1
                    print(f"Seat ({row}, {col}) booked for show {id}.")
                else:
                    print(f"Seat ({row}, {col}) already booked.")
            else:
                print(f"Seat ({row}, {col}) is invalid.")

    def view_show_list(self):
        print('These shows are running')
        print('If you want to watch please book seat')
        print('----------------')
        for show in self.__show_list:
            print(f'Movie name: {show[0]} Show ID: {show[1]} Time:21/04/2024 {show[2]}')
        print('-----------------')

    def view_available_seats(self, id):
        if id not in self.__seats:
            print("Show ID is Invalid")
            return
        seats = self.__seats[id]
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(seats[i][j],end =' ')
            print()

        

        

hall1 = Hall(4, 4, 1)
hall1.entry_show('Spiderman','1', '9:00AM')
hall1.entry_show('Ironman','2', '12:00PM')
hall1.entry_show('Superman','3', '3:00PM')
hall1.entry_show('Machineman','4', '6:00pm')


run = True
while run:

    print("Options: \n")       
    print("1 : view all show today")
    print("2 : View available seats")
    print("3 : Book ticket")
    print("4 : Exit")

    ch=int(input("\nEnter Option: "))

    

    if ch == 1:
       hall1.view_show_list()
    elif ch == 2:
       show_id = input('\nEnter show id: ')
       hall1.view_available_seats(show_id)
    elif ch == 3:
       show_id = input("Enter show ID: ")
       row = int(input("Enter seat row: "))
       col = int(input("Enter seat col: "))
       hall1.book_seats(show_id, [(row, col)])
    elif ch == 4:
        run = False


        