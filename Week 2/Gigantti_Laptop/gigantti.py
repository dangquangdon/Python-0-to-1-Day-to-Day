from bs4 import BeautifulSoup

with open('gigantti_laptop.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

containers = soup.findAll('div', class_="mini-product")

csv_file = "gigantti_laptop.csv"
file = open(csv_file, 'w')
headers = "Product Name,Product Number,Product Price\n"
file.write(headers)

for cont in containers:
    product_number = cont.findChild('div',class_="product-number").text
    product_name = cont.findChild('span', class_="table-cell").text
    product_price = cont.findChild('div', class_="product-price").text

    file.write("{},{},{}\n".format(
                        product_name.replace(",","."),
                        product_number,
                        product_price))

file.close()
print('Done !')
