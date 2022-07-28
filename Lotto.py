from random import randint

results = []
my_coupon = []  #[6, 9, 14, 27, 33, 47]

class Lotto():
    def __init__(self, flag=True):
        self.flag = flag

    def lottery(self):
        i = 0
        balls = 6
        sorted_list = ""
        results.clear()

        while i < balls:
            i += 1
            rand = randint(1, 49)
            for result in results:
                while rand == result:
                    rand = randint(1, 49)
            results.append(rand)
            sorted_list = sorted(results)

        print(f'Wyniki losowania: {sorted_list}')
        return sorted_list

    def choosing(self):
        my_coupon.clear()
        i = 0
        while i < 6:
            lucky_numbers = int(input())
            if lucky_numbers == 0 or lucky_numbers > 49:
                print('Liczby mają być od 1 do 49')
            else:
                i += 1
                for number in my_coupon:
                    while number == lucky_numbers:
                        print('Liczby się powtarzają, wpisz ponownie.')
                        lucky_numbers = int(input())
                my_coupon.append(lucky_numbers)
        print(f'Szczęśliwe liczby to: {sorted(my_coupon)}')

    def checking(self):
        i = 0
        for result in results:
            for number in my_coupon:
                if result == number:
                    i += 1
        if i > 0:
            print(f'Trafiłeś liczb: {i}!')
        elif i == 6:
            print(f'Trafiłeś 6! Gratulacje!')
        else:
            print(f'Nic nie trafiłeś')

    def matching(self):
        count = 0
        self.flag = True
        result_lottery = self.lottery()

        while self.flag:
            if result_lottery != my_coupon:
                result_lottery = self.lottery()
                count += 1
                print(count, result_lottery)
            else:
                self.flag = False
                break
        print(f'Przeprowadzono iteracji: {count}')


lottery = Lotto()
print(f'Podaj 6 liczb od 1 do 49 (każdorazowo zatwierdź liczbę enterem)')
lottery.choosing()
lottery.lottery()
lottery.checking()
#lottery.matching()




