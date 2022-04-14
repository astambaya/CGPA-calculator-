import wpf
import clr

clr.AddReference("System.Data")

from System.Windows import Window
from System.Windows import *
from System.Data import OleDb as mysqlclient

class Create(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Create.xaml')
    
    def Button_Click(self, sender, e):
        self.Close()
        pass
    
    def Button_Click1(self, sender, e):
        userfullname = self.txtfullname.Text
        userid = self.txtuserid.Text
        password = self.txtPassword.Password
        verifypassword = self.txtrpassword.Password
        if userfullname == "":
            MessageBox.Show("Enter your fullname")
            self.txtfullname.Focus()
        elif userid == "":
            MessageBox.Show("Enter your user id")
            self.txtuserid.Focus()
        elif password == "":
            MessageBox.Show("Enter your password")
            self.txtPassword.Focus()
        elif verifypassword == "":
            MessageBox.Show("Please re-enter your password")
            self.txtrpassword.Focus()
        else:
            try:
                if password != verifypassword:
                    MessageBox.Show("Your password do not match!")
                else:
                    con = mysqlclient.OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:/Users/YFSOFT/Documents/gpa.mdb;Jet OLEDB:Database Password=yfsoftbuilder;")
                    con.Open()
                    sql = "SELECT [fname], [userid], [password] FROM newuser WHERE [userid]='{parameter}'".format(parameter=userid)
                    command = mysqlclient.OleDbCommand(sql, con)
                    reader = mysqlclient.OleDbDataReader
                    reader = command.ExecuteReader()
                    if reader.Read():
                        MessageBox.Show("Please change your user ID")
                    else:
                        sql = "INSERT INTO newuser ([fname], [userid], [password]) VALUES ('{fname}','{userid}','{password}')".format(fname=userfullname,userid=userid,password=password)
                        command = mysqlclient.OleDbCommand(sql, con)
                        command.ExecuteNonQuery()
                        MessageBox.Show("User Account Created Successfully")
                        self.txtfullname.Text = ""
                        self.txtuserid.Text = ""
                        self.txtPassword.Password = ""
                        self.txtrpassword.Password = ""
            except Exception as ex:
                MessageBox.Show(ex.message)

        pass
