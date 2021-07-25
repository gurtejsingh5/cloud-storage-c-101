import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
        
def main():
    access_token='sl.A1QoZy054EqTagOanLuoGJ4DN9zX_m0H7UjZZbirVjw0gXt8MQUheJRRMuRmQmvXEncqY4O_yhJG8_MoGstsPGUEKrvd6kfI460dOjyZ15eLEMla9zUEIqavPFMuwpOisR9v2N4'
    transferData=TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()













