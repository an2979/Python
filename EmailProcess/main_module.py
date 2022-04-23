#xu ly nhieu email 
from xulymail import emailProcess, printMsg    #import 2 ham tu xulymail.py

 
def main():
    emails = ['vietanh82696@gmail.com' , 'quynhhuong.61199@gmail.com', 'ManchesterUnited@gmail.com']      # danh sach email
    for e in emails:   # su dung vong lap tung phan tu trong list emails o tren
        username, emaildomain=  emailProcess(e)
        printMsg(username, emaildomain)


if __name__ == "__main__" :
    main()
 

