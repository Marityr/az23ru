import openpyxl

from openpyxl.styles import PatternFill
from openpyxl.styles import Font

from config.exelconfig import title, width_column
from adminpanel.models import Orders, Product


class Importxl:
    """Импорт данных в эксель"""

    def importxl() -> None:
        book = openpyxl.Workbook()
        sheet = book.active

        fontStyle = Font(size = "10")


        for counter, item in enumerate(title, 1):
            sheet.cell(row=1, column=counter).value = item
            sheet.cell(row=1, column=counter).font = fontStyle
            sheet.cell(row=1, column=counter) .fill = PatternFill(
                start_color="ffff00",
                end_color="ffff00",
                fill_type="solid")
            counter += 1

        orders = Orders.objects.all()[:100]
        row = 2
        for counter, obj in enumerate(orders, 2):
            products = Product.objects.filter(number_order=obj.number)

            sheet.cell(row=counter, column=1).value = obj.number
            sheet.cell(row=counter, column=2).value = obj.id_manager
            sheet.cell(row=counter, column=3).value = str(obj.data_orders)[:10]

            for i, product in enumerate(products, 0):
                if i == 0:
                    sheet.cell(row=counter, column=4).value = product.status
                    sheet.cell(row=counter, column=5).value = product.descriptions
                    sheet.cell(row=counter, column=6).value = product.brand
                    sheet.cell(row=counter, column=7).value = product.article
                    sheet.cell(row=counter, column=8).value = product.quantity
                    sheet.cell(row=counter, column=9).value = product.price_product

                    sheet.cell(row=counter, column=10).value = obj.price
                    sheet.cell(row=counter, column=11).value = obj.paid
                    sheet.cell(row=counter, column=12).value = obj.debt
                    sheet.cell(row=counter, column=13).value = str(obj.name_client)
                    sheet.cell(row=counter, column=14).value = obj.phone

                    sheet.cell(row=counter, column=15).value = str(product.date_deadline)[:10]
                    sheet.cell(row=counter, column=16).value = product.distributor
                    sheet.cell(row=counter, column=17).value = product.order_distributer
                    sheet.cell(row=counter, column=18).value = product.comment

                    sheet.cell(row=counter, column=19).value = str(obj.update_date)[:10]
                    sheet.cell(row=counter, column=20).value = obj.manager
                else:
                    sheet.cell(row=counter, column=4).value = product.status
                    sheet.cell(row=counter, column=5).value = product.descriptions
                    sheet.cell(row=counter, column=6).value = product.brand
                    sheet.cell(row=counter, column=7).value = product.article
                    sheet.cell(row=counter, column=8).value = product.quantity
                    sheet.cell(row=counter, column=9).value = product.price_product

                    sheet.cell(row=counter, column=15).value = str(product.date_deadline)[:10]
                    sheet.cell(row=counter, column=16).value = product.distributor
                    sheet.cell(row=counter, column=17).value = product.order_distributer
                    sheet.cell(row=counter, column=18).value = product.comment
                counter += 1

        for object in width_column:
            sheet.column_dimensions[object['column']].width = object['width']
            sheet.column_dimensions[object['column']].font = fontStyle

        book.save("myexel.xlsx")
        book.close()
