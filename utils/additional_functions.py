import csv
import time


class AdditionalFunctions():

    def select_item_from_list(values_list, value_to_select):
        time.sleep(1)
        for result in values_list:
            if value_to_select in result.get_attribute("value"):
                result.click()
                break

    def read_data_from_csv(file_name):
        data_list = []
        csvdata = open(file_name, "r")
        reader = csv.reader(csvdata)
        next(reader)  # skip header string
        
        for row in reader:
            data_list.append(row)
        
        return data_list