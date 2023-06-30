from datetime import datetime

class Date:

    def __init__(self):
       self.__month = {
                "01": [1, 'janvier', 'janv'],
                "02": [2, 'février', 'fevr'],
                "03": [3, 'mars', 'mars'],
                "04": [4, 'avril', 'avr'],
                "05": [5, 'mai', 'mai'],
                "06": [6, 'juin', 'juin'],
                "07": [7, 'juillet', 'juill'],
                "08": [8, 'aout', 'aout'],
                "09": [9, 'septembre', 'sept'],
                "10": ['octobre', 'oct'],
                "11": ['novembre', 'nov'],
                "12": ['decembre', 'dec'],
            }
    
    def __cleanDate(self, date):
        print('[cleanDate]')
        date= str(date)
        dateArray = date.split('-')
        # print(dateArray)
        return dateArray
    
    def __transformMonth(self, date):
        for el in self.__month:
            if date == el:
                # print(el)
                # print(self.month[el])
                return self.__month[el]
    

    def transformDate (self, initiale_word_array, exitArray):
        for word in initiale_word_array:
            try:
                datetime.strptime(word, '%Y-%m-%d')
                date_clean = self.__cleanDate(word)
                for date in date_clean:
                    exitArray.append(date)
                month = self.__transformMonth(date_clean[1])
                for el in month:
                    exitArray.append(str(el))
            except ValueError:
                False

        return exitArray