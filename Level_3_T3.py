import pandas as pd

def process_customer_records(input_file, output_file):
    customer_records = pd.read_csv(input_file)

customer_records = customer_records.drop_duplicates()
customer_records = customer_records.fillna("")

customer_records["Name"] = customer_records["Name"].str.title()
customer_records["Email"] = customer_records["Email"].str.lower()

customer_records.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "customer_records.csv"
output_file = "processed_customer_records.csv"
process_customer_records(input_file, output_file)
