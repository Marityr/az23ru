import openpyxl
from adminpanel.models import Number_catalog


class Export_file:
    """Экспорт данных из exlc файла"""
    
    def read_data():
        """считывание файла"""
        book = openpyxl.open("media/abcp_ts.xlsx", read_only=True)

        sheet = book.active

        #Number_catalog.objects.all().delete()
        i = 0

        """
            Проверка записи на существование и изменение если она есть
            Создание новой записи в модель
        """
        for row in sheet.rows:
            try:
                instanse = Number_catalog.objects.get(number_cat=str(row[0].value))
                # TODO проверить почему тождество не выполняется при неизменном файле!!!
                string = ''
                if str(instanse.number_cat) != str(row[0].value):
                    string = '-'
                    instanse.number_cat = str(row[0].value)
                if str(instanse.brand) != str(row[1].value):
                    string = '-'
                    instanse.brand = str(row[1].value)
                if str(instanse.descriptions) != str(row[2].value):
                    string = '-'
                    instanse.cuantity = str(row[3].value)
                if str(instanse.price) != str(row[4].value):
                    string = '-'
                    instanse.price = str(row[4].value)
                instanse.save()
                if string == '-':
                    print(string, str(row[0].value))
            except Number_catalog.DoesNotExist:
                number_catalog = Number_catalog()
                number_catalog.number_cat = str(row[0].value)
                number_catalog.brand = str(row[1].value)
                number_catalog.descriptions = str(row[2].value)
                number_catalog.cuantity = str(row[3].value)
                number_catalog.price = str(row[4].value)
                number_catalog.save()
                print('$', i)
            
            """Удаление титульной строки файла"""
            try:
                tmp = Number_catalog.objects.get(number_cat='Каталожный номер')
                tmp.delete()
            except Number_catalog.DoesNotExist:
                pass

            i += 1
            
