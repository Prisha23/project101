import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BIWy0MDJIkgSWfrRiUxCDpDPSytmf9tds9GA07QLQBePn6AAjSUxVKHMBuQWWhD7BguL0IwbDaeXpVxoJn89zdtmzfuN_ix9gcibvRukN_Z5Qt0Imu2LSZczBBpaVVlXhdL6c5Q'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer")
    file_to = input("enter the full path to upload to dropbox")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()
