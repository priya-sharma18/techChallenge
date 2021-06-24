from google.cloud import storage
import logging
import configparser
import datetime
from datetime import date, timedelta


def download_gcs_file(obj, to, bucket):
    client = storage.Client()
    bucket = client.get_bucket(bucket)
    blob = bucket.blob(obj)
    blob.download_to_filename(to)
    return file_to_upload

# Function to load the landing tables from Source files.
def load_bq_table( file_to_upload):
    dataset= "dataset_lz"
    file_location= file_to_upload
    table_name= "dest_table"
    field_delimiter= ","
    command= 'bq load --skip_leading_rows=1 --field_delimiter="{}" {}.{}  {}/*.csv'.format( field_delimiter, dataset, table_name, file_location)
    log.info("command is:- {}".format(command))
    try:
        os.system(command)
        log.info("Files loaded to the landing table successfully")
    except:
        log.error("Error occurred while loading the table")


def main():
    print("inside main function")
    web_input = data['name'] # Name of the input file landed in the bucket
    folder='websource' # Folder in the GCS bucket where the Web files are expected to land

    if web_input.startswith(folder):
        sourcefile=web_input
        bucket = data['bucket'] # Name of the GCS bucket

        outputfilename='data_merged_web.csv'

    #Downoad a file from GCS storage which needs to be processed
    file_to_upload = download_gcs_file(sourcefile, outputfilename, bucket)
    load_dq_table(file_to_upload)


if __name__ == "__main__":
    main()
