import csv
def write_into_csv(take_list):
    with open('student_data.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        arr=["Name","Age","Contact number","Email_Id"]
        if(csv_file.tell()==0):
          writer.writerow(arr)

        writer.writerow(take_list)
class school_admin:
    def take_data():
        flag=True
        student_num=1
        while (flag):
          student_data=input("please enter info for student#{} following order:Name Age Contact_no email_ID:-".format(student_num))
          student_data_list=student_data.split(" ")
          print("\nThe entered information is:-\nName:{}\nAge:{}\nContact number:{}\nEmail id:{}".format(student_data_list[0],student_data_list[1],student_data_list[2],student_data_list[3]))
          choice_option=input("Is the data corect:yes/no:-")
          if(choice_option=="yes"):
               write_into_csv(student_data_list)
               cond_check=input("write yes for more input else write no:")
               if(cond_check=="yes"):
                 student_num=student_num+1  
                 flag=True
               elif(cond_check=="no"):
                 flag=False
          elif(choice_option=="no"):
             print("re-enter data")
    take_data()
