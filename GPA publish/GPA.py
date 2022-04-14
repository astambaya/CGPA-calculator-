import wpf
import sys
import clr

clr.AddReference("System.Data")

from System.Data import OleDb as mysqlclient
from System.Windows import *
from System.Windows import Application, Window
from System import DBNull
from Create import *
from MainMenu import *

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'GPA.xaml')
    
    def Button_Click(self, sender, e):
        try:
            username = self.txtusername.Text
            password = self.txtpassword.Password
            if username == "":
                MessageBox.Show("Enter your username please!")
            elif password == "":
                MessageBox.Show("Enter your password please!")
                self.txtpassword.Focus()
            else:
                con = mysqlclient.OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:/Users/YFSOFT/Documents/gpa.mdb;Jet OLEDB:Database Password=yfsoftbuilder;")
                con.Open()
                sql = "SELECT * FROM newuser WHERE [userid]='{useriddd}'".format(useriddd=username)
                command = mysqlclient.OleDbCommand(sql, con)
                reader = mysqlclient.OleDbDataReader
                reader = command.ExecuteReader()
                if reader.Read():
                    mypassword = reader['password']
                    if mypassword == password:
                        form = MainMenu() 
                        form.ShowDialog()
                    else:
                        MessageBox.Show("Incorrect Password")
                else:
                    MessageBox.Show("Incorrect Username")
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass

    
    def Window_Loaded(self, sender, e):
        self.txtusername.Text = ""
        self.txtpassword.Password = ""
        pass
        
    def Button_Click1(self, sender, e):
        create = Create()
        create.ShowDialog()

 
if __name__ == '__main__':
    Application().Run(MyWindow())
