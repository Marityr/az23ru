import openpyxl
from adminpanel.models import Number_catalog


class Export_file:
    """Экспорт данных из exlc файла"""
    
    def read_data():
        """считывание файла"""
        book = openpyxl.open("media/abcp_ts.xlsx", read_only=True)

        sheet = book.active
        nb_row = sheet.max_row

        Number_catalog.objects.all().delete()
        i = 0
        # TODO убрать считывание первой титульной строки
        for row in sheet.rows:
            if row == 0:
                pass
            print(i)
            i += 1

            try:
                instanse = Number_catalog.objects.get(number_cat=str(row[0].value))
                instanse.number_cat = str(row[0].value)
                instanse.brand = str(row[1].value)
                instanse.descriptions = str(row[2].value)
                instanse.cuantity = str(row[3].value)
                instanse.price = str(row[4].value)
                instanse.save()
            except Number_catalog.DoesNotExist:
                number_catalog = Number_catalog()
                number_catalog.number_cat = str(row[0].value)
                number_catalog.brand = str(row[1].value)
                number_catalog.descriptions = str(row[2].value)
                number_catalog.cuantity = str(row[3].value)
                number_catalog.price = str(row[4].value)
                number_catalog.save()
            
            # if item == 50:
            #     print('----------')
            

    def write_data_db(item1, item2, item3, item4, item5):
        """сохранение данных в бд"""
        pass
