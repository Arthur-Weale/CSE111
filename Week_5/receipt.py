import csv
from datetime import datetime

# def main ():
#     products_csv = r"C:/Users/Arthur/repos/CSE111/Week_5/products.csv"
#     get_product= read_dictionary(products_csv, PRODUCT_NUMBER_KEY_INDEX)
#     # return get_product

# PRODUCT_REQUEST_KEY_NUM = 0
# PRODUCT_REQUEST_QUANTITY = 1
# PRODUCT_NUMBER_KEY_INDEX = 0
# PRODUCT_NAME_INDEX = 1
# PRODUCT_PRICE_INDEX = 2
# PRODUCT_DICT = {}
# REQUEST_DICT = {}
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
PRODUCT_REQUEST_KEY_NUM = 0
PRODUCT_REQUEST_QUANTITY = 1
REQUEST_DICT = {}
PRODUCT_NUMBER_KEY_INDEX = 0

def read_dictionary(filename, key_column_index):
    products_csv = r"C:/Users/Arthur/repos/CSE111/Week_5/products.csv"
    #get_product= read_dictionary(products_csv, PRODUCT_NUMBER_KEY_INDEX)
    # return get_product

    PRODUCT_DICT = {}

    try:
        with open(filename, "rt") as product_file:
            products = csv.reader(product_file)
            next(products)
            for product_list in products:

                if len(product_list) != 0:
                    product_key = product_list[key_column_index]
                    PRODUCT_DICT[product_key] = product_list
            return PRODUCT_DICT
    except FileNotFoundError:
        print(f"The {filename} not found or file not added correctly")
        return{} #To avoid crashes we return an empty dictionary

# if __name__ == "__main__":
#     main()
    
def main():

    request_csv = r"C:/Users/Arthur/repos/CSE111/Week_5/request.csv" 
    products_csv = r"C:/Users/Arthur/repos/CSE111/Week_5/products.csv"

    products_dict = read_dictionary(products_csv, PRODUCT_NUMBER_KEY_INDEX)
    #print(products_dict)
    print("Pick'n'Pay")

    try:
        with open (request_csv, "rt") as request_file:
            request = csv.reader(request_file)
            next(request)

            orders_running_total = 0
            running_subtotal = 0
            now = datetime.now()

            for product_request_row in request:
                try:
                    product_id = product_request_row[PRODUCT_REQUEST_KEY_NUM]
                    quantity = int(product_request_row[PRODUCT_REQUEST_QUANTITY])

                    # if product_id in products_dict :
                    product_name = products_dict[product_id][PRODUCT_NAME_INDEX] 
                    product_price = float(products_dict[product_id][PRODUCT_PRICE_INDEX])

                    print(f"{product_name}: {quantity} @ ${product_price:.2f} each")
                    # else:
                    #     print(f"Product ID {product_id} not found in products.csv")

                    orders_running_total += quantity
                    running_subtotal += product_price * quantity
                    sales_tax = (6/100) * running_subtotal
                    total = sales_tax + running_subtotal

                except ValueError:
                    print(f"Invalid quantity for product ID {product_id}")
                except KeyError:
                    print(f"Product ID {product_id} not found in products.csv")


    except FileNotFoundError:
        print(f"File not found or file not added correctly") 
    except KeyError:
        print(f"Key not found in dictionary")
    except ValueError:
        print("Value error occurred") 
    else:
        print(f"Number of items: {orders_running_total}")
        print(f"Subtotal: ${running_subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")
        print("Thank you for shopping at Pick'n'Pay.")
        print(now.strftime("%a %b %d %H:%M:%S %Y"))

if __name__ == "__main__":
    main()