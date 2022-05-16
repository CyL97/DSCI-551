import sqlalchemy
import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd
import sys

if __name__ == '__main__':
    first_name = sys.argv[1]
    #print(first_name)
    my_conn = sqlalchemy.create_engine("mysql+mysqldb://dsci551:Dsci-551@localhost/sakila")
    information = pd.read_sql('select \
        customer.first_name, \
        customer.last_name, \
        city.city \
    from \
        city, \
        address, \
        customer \
    where customer.first_name="{fname}" \
      and address.address_id=customer.address_id \
      and city.city_id=address.city_id;'.format(fname=first_name), my_conn)
    #print(information.to_string())
    if information.empty == False:
        info_list = information.values.tolist()
        for firstName, lastName, city in info_list:
            print(firstName.upper(), lastName.upper(), city.upper())
    else:
        print('Customer does not exist')