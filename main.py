import pandas as pd
import xml.etree.ElementTree as ET

# Функция для конвертации Excel данных в XML
def convert_excel_to_xml(file_path):
    # Чтение Excel файла
    df = pd.read_excel(file_path)

    # Создаем корневой элемент "Products"
    root = ET.Element('Products')

    # Перебор строк в DataFrame
    for index, row in df.iterrows():
        # Создаем элемент для каждого товара "Product"
        product_elem = ET.SubElement(root, 'Product')
        
        # Добавляем артикул
        article_elem = ET.SubElement(product_elem, 'Article')
        article_elem.text = str(row['артикул'])
        
        # Добавляем категорию
        category_elem = ET.SubElement(product_elem, 'Category')
        category_elem.text = str(row['Категория'])
        
        # # Добавляем название
        name_elem = ET.SubElement(product_elem, 'Name')
        name_elem.text = str(row['Название'])
        
        # Добавляем фото
        photo_elem = ET.SubElement(product_elem, 'Photo')
        photo_elem.text = str(row['фото'])
        #print(photo_elem.text +'\n')
        # Добавляем цену
        price_elem = ET.SubElement(product_elem, 'Price')
        price_elem.text = str(row['цена'])
        
        # Добавляем информацию о новинке или акции
        promo_elem = ET.SubElement(product_elem, 'Promo')
        promo_elem.text = str(row['Новинка/акция'])


    # Записываем результат в файл
    tree = ET.ElementTree(root)
    tree.write('output_products.xml', encoding='utf-8', xml_declaration=True)

# Пример использования
file_path = 'items.xlsx'  # Замени на путь к твоему файлу
convert_excel_to_xml(file_path)
