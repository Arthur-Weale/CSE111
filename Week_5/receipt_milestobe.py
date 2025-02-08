import csv

def main ():
    #products_csv = r"C:/Users/Arthur/repos/CSE111/Week_5/products.csv"
    get_product= read_dictionary("products.csv", PRODUCT_NUMBER_KEY_INDEX)
    return get_product

PRODUCT_REQUEST_KEY_NUM = 0
PRODUCT_REQUEST_QUANTITY = 1
PRODUCT_NUMBER_KEY_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
PRODUCT_DICT = {}
REQUEST_DICT = {}

def read_dictionary(filename, key_column_index):
    with open(filename, "rt") as product_file:
        products = csv.reader(product_file)
        next(products)
        for product_list in products:

            if len(product_list) != 0:
                product_key = product_list[key_column_index]
                PRODUCT_DICT[product_key] = product_list
        return PRODUCT_DICT

    

if __name__ == "__main__":
    main()

def main():
    #request_csv = r"C:/Users/Arthur/repos/CSE111/Week_5/request.csv" 
    #products_csv = r"C:/Users/Arthur/repos/CSE111/Week_5/products.csv"

    products_dict = read_dictionary("products.csv", PRODUCT_NUMBER_KEY_INDEX)
    print(products_dict)

    with open ("request.csv", "rt") as request_file:
        request = csv.reader(request_file)
        next(request)
        for product_request_row in request:
            product_id = product_request_row[PRODUCT_REQUEST_KEY_NUM]
            quantity = int(product_request_row[PRODUCT_REQUEST_QUANTITY])

            #print(products_dict[product_request_row[PRODUCT_REQUEST_KEY_NUM]][PRODUCT_NUMBER_KEY_INDEX])
            if product_id in products_dict :
                product_name = products_dict[product_id][PRODUCT_NAME_INDEX] 
                product_price = float(products_dict[product_id][PRODUCT_PRICE_INDEX])

                print(f"{product_name}: {quantity} @ ${product_price:.2f} each")
            else:
                print(f"Product ID {product_id} not found in products.csv")

                

if __name__ == "__main__":
    main()