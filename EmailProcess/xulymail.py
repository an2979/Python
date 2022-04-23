def emailProcess(email):       #ham emailProcess la ham de xu ly email nhan email truyen vao
    email_username= email[0:email.index("@")]   #email[0:1] nghia la cat chuoi tu vi tri 0 den 1.
                                                 #email.index("@") : nghia la vi tri co phan tu @
                                                 #email_username : muc dich la cat email bo phan sau @ di
    email_domain = email[email.index("@")+1:]   #email_domain : cat chuoi lay phan tu sau @ toi het
    # print(email_domain)
    #print(email_username)    
    return [email_username, email_domain]   # tra ve 2 gia tri sau khi cat
    

def printMsg(email_username, email_domain):        # ham de in 2 bien vua cat duoc o tren
    print(f"Username is {email_username}; email Domain is {email_domain}")

def main():
    email = input("please enter your email add: ").strip()   # strip chi lay chu ko lay ky tu so va dac biet
    #print(email)   # in truc tiep bien email
    #print(f"Hello {email}")   #in kem theo cau chao.
    
    username, domain  = emailProcess(email)    # goi ham xu ly email emailProcess ra , gan gia tri vao
                                                          # tao 2 bien de hung gia tri duoc tra ve o dong 8
    printMsg(username, domain)

if __name__ == "__main__":
    main()


#ket qua: please enter your email add: vietanh82696@gmail.com 
        #Username is vietanh82696; email Domain is gmail.com

