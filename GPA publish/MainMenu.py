import wpf
import clr

from System.Windows import Window
from System.Windows import *

globaltotalpoints = 0
globaltotalunits = 0

globaltotalpoints2 = 0
globaltotalunits2 = 0

class MainMenu(Window):
    
    def __init__(self):
        wpf.LoadComponent(self, 'MainMenu.xaml')
    
    def TextBox_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore1.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.TXTGRADE1.Text = ""
                 self.txtscore1.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.TXTGRADE1.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.TXTGRADE1.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.TXTGRADE1.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.TXTGRADE1.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.TXTGRADE1.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.TXTGRADE1.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtScore2_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtScore2.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.TXTGRADE2.Text = ""
                 self.txtScore2.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.TXTGRADE2.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.TXTGRADE2.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.TXTGRADE2.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.TXTGRADE2.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.TXTGRADE2.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.TXTGRADE2.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
        
    def txtscore3_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore3.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE3.Text = ""
                 self.txtscore3.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE3.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE3.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE3.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE3.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE3.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE3.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore4_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore4.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE4.Text = ""
                 self.txtscore4.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE4.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE4.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE4.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE4.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE4.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE4.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore5_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore5.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE5.Text = ""
                 self.txtscore5.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE5.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE5.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE5.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE5.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE5.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE5.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore6_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore6.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE6.Text = ""
                 self.txtscore6.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE6.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE6.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE6.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE6.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE6.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE6.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore7_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore7.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE7.Text = ""
                 self.txtscore7.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE7.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE7.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE7.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE7.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE7.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE7.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore8_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore8.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE8.Text = ""
                 self.txtscore8.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE8.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE8.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE8.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE8.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE8.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE8.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore9_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore9.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE9.Text = ""
                 self.txtscore9.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE9.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE9.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE9.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE9.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE9.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE9.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore10_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore10.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE10.Text = ""
                 self.txtscore10.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE10.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE10.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE10.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE10.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE10.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE10.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore11_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore11.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE11.Text = ""
                 self.txtscore11.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE11.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE11.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE11.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE11.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE11.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE11.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore12_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore12.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE12.Text = ""
                 self.txtscore12.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE12.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE12.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE12.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE12.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE12.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE12.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore13_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore13.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE13.Text = ""
                 self.txtscore13.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE13.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE13.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE13.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE13.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE13.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE13.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore14_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore14.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE14.Text = ""
                 self.txtscore14.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE14.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE14.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE14.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE14.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE14.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE14.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore15_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore15.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE15.Text = ""
                 self.txtscore15.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE15.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE15.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE15.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE15.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE15.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE15.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def Button_Click(self, sender, e):
        try:
            totalpoints = 0

            #perform validations 
            if self.txtcu1.Text == "":
                self.txtcu1.Text = "0"
            if self.txtcu2.Text == "":
                self.txtcu2.Text = "0"
            if self.txtcu3.Text == "":
                self.txtcu3.Text = "0"
            if self.txtcu4.Text == "":
                self.txtcu4.Text = "0"
            if self.txtcu5.Text == "":
                self.txtcu5.Text = "0"
            if self.txtcu6.Text == "":
                self.txtcu6.Text = "0"
            if self.txtcu7.Text == "":
                self.txtcu7.Text = "0"
            if self.txtcu8.Text == "":
                self.txtcu8.Text = "0"
            if self.txtcu9.Text == "":
                self.txtcu9.Text = "0"
            if self.txtcu10.Text == "":
                self.txtcu10.Text = "0"
            if self.txtcu11.Text == "":
                self.txtcu11.Text = "0"
            if self.txtcu12.Text == "":
                self.txtcu12.Text = "0"
            if self.txtcu13.Text == "":
                self.txtcu13.Text = "0"
            if self.txtcu14.Text == "":
                self.txtcu14.Text = "0"
            if self.txtcu15.Text == "":
                self.txtcu15.Text = "0"

            #grade1
            if self.TXTGRADE1.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu1.Text)
            elif self.TXTGRADE1.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu1.Text)
            elif self.TXTGRADE1.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu1.Text)
            elif self.TXTGRADE1.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu1.Text)
            elif self.TXTGRADE1.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu1.Text)

            #grade2
            if self.TXTGRADE2.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu2.Text)
            elif self.TXTGRADE2.Text == "B": 
                totalpoints = totalpoints + 4.00 * int(self.txtcu2.Text)
            elif self.TXTGRADE2.Text == "C":
                totalpoints = totalpoints + 3.00  * int(self.txtcu2.Text)
            elif self.TXTGRADE2.Text == "D":
                totalpoints = totalpoints + 2.00  * int(self.txtcu2.Text)
            elif self.TXTGRADE2.Text == "E":
                totalpoints = totalpoints + 1.00  * int(self.txtcu2.Text)

            #grade3
            if self.txtGRADE3.Text == "A":
                totalpoints = totalpoints + 5.00  * int(self.txtcu3.Text)
            elif self.txtGRADE3.Text == "B":
                totalpoints = totalpoints + 4.00  * int(self.txtcu3.Text)
            elif self.txtGRADE3.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu3.Text)
            elif self.txtGRADE3.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu3.Text)
            elif self.txtGRADE3.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu3.Text)

            #grade4
            if self.txtGRADE4.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu4.Text)
            elif self.txtGRADE4.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu4.Text)
            elif self.txtGRADE4.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu4.Text)
            elif self.txtGRADE4.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu4.Text)
            elif self.txtGRADE4.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu4.Text)

            #grade5
            if self.txtGRADE5.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu5.Text)
            elif self.txtGRADE5.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu5.Text)
            elif self.txtGRADE5.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu5.Text)
            elif self.txtGRADE5.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu5.Text)
            elif self.txtGRADE5.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu5.Text)

            #grade6
            if self.txtGRADE6.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu6.Text)
            elif self.txtGRADE6.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu6.Text)
            elif self.txtGRADE6.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu6.Text)
            elif self.txtGRADE6.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu6.Text)
            elif self.txtGRADE6.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu6.Text)

            #grade7
            if self.txtGRADE7.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu7.Text)
            elif self.txtGRADE7.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu7.Text)
            elif self.txtGRADE7.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu7.Text)
            elif self.txtGRADE7.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu7.Text)
            elif self.txtGRADE7.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu7.Text)

            #grade8
            if self.txtGRADE8.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu8.Text)
            elif self.txtGRADE8.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu8.Text)
            elif self.txtGRADE8.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu8.Text)
            elif self.txtGRADE8.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu8.Text)
            elif self.txtGRADE8.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu8.Text)

            #grade9
            if self.txtGRADE9.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu9.Text)
            elif self.txtGRADE9.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu9.Text)
            elif self.txtGRADE9.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu9.Text)
            elif self.txtGRADE9.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu9.Text)
            elif self.txtGRADE9.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu9.Text)

            #grade10
            if self.txtGRADE10.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu10.Text)
            elif self.txtGRADE10.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu10.Text)
            elif self.txtGRADE10.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu10.Text)
            elif self.txtGRADE10.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu10.Text)
            elif self.txtGRADE10.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu10.Text)

            #grade11
            if self.txtGRADE11.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu11.Text)
            elif self.txtGRADE11.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu11.Text)
            elif self.txtGRADE11.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu11.Text)
            elif self.txtGRADE11.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu11.Text)
            elif self.txtGRADE11.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu11.Text)


            #grade12
            if self.txtGRADE12.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu12.Text)
            elif self.txtGRADE12.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu12.Text)
            elif self.txtGRADE12.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu12.Text)
            elif self.txtGRADE12.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu12.Text)
            elif self.txtGRADE12.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu12.Text)

            #grade13
            if self.txtGRADE13.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu13.Text)
            elif self.txtGRADE13.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu13.Text)
            elif self.txtGRADE13.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu13.Text)
            elif self.txtGRADE13.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu13.Text)
            elif self.txtGRADE13.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu13.Text)

            #grade14
            if self.txtGRADE14.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu14.Text)
            elif self.txtGRADE14.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu14.Text)
            elif self.txtGRADE14.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu14.Text)
            elif self.txtGRADE14.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu14.Text)
            elif self.txtGRADE14.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu14.Text)

            #grade15
            if self.txtGRADE15.Text == "A":
                totalpoints = totalpoints + 5.00 * int(self.txtcu15.Text)
            elif self.txtGRADE15.Text == "B":
                totalpoints = totalpoints + 4.00 * int(self.txtcu15.Text)
            elif self.txtGRADE15.Text == "C":
                totalpoints = totalpoints + 3.00 * int(self.txtcu15.Text)
            elif self.txtGRADE15.Text == "D":
                totalpoints = totalpoints + 2.00 * int(self.txtcu15.Text)
            elif self.txtGRADE15.Text == "E":
                totalpoints = totalpoints + 1.00 * int(self.txtcu15.Text)

            totalunits = int(self.txtcu1.Text) + int(self.txtcu2.Text) + int(self.txtcu3.Text) + int(self.txtcu4.Text) + int(self.txtcu5.Text) + int(self.txtcu6.Text) + int(self.txtcu7.Text) + int(self.txtcu8.Text) + int(self.txtcu9.Text) + int(self.txtcu10.Text) + int(self.txtcu11.Text) + int(self.txtcu12.Text) + int(self.txtcu13.Text) + int(self.txtcu14.Text) + int(self.txtcu15.Text)
            gpa = totalpoints / totalunits
            globaltotalpoints = totalpoints
            globaltotalunits = totalunits
            self.lblgtpoints1.Content = str(globaltotalpoints)
            self.lbgcupoints1.Content = str(globaltotalunits)
            self.lbldisplayfirst.Content = "First Semester GPA is {gpa}".format(gpa=str(gpa))
            #MessageBox.Show("Global points {gpa}".format(gpa=str(globaltotalpoints)))
        except Exception as ex:
            MessageBox.Show("System Error {error}".format(error=ex.message))
        pass
    
    def txtscore1_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore1_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.TXTGRADE1_Copy.Text = ""
                 self.txtscore1_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.TXTGRADE1_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.TXTGRADE1_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.TXTGRADE1_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.TXTGRADE1_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.TXTGRADE1_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.TXTGRADE1_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtScore2_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtScore2_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.TXTGRADE2_Copy.Text = ""
                 self.txtScore2_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.TXTGRADE2_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.TXTGRADE2_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.TXTGRADE2_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.TXTGRADE2_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.TXTGRADE2_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.TXTGRADE2_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore3_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore3_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE3_Copy.Text = ""
                 self.txtscore3_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE3_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE3_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE3_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE3_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE3_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE3_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore4_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore4_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE4_Copy.Text = ""
                 self.txtscore4_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE4_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE4_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE4_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE4_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE4_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE4_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore5_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore5_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE5_Copy.Text = ""
                 self.txtscore5_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE5_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE5_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE5_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE5_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE5_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE5_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore6_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore6_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE6_Copy.Text = ""
                 self.txtscore6_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE6_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE6_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE6_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE6_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE6_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE6_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore7_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore7_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE7_Copy.Text = ""
                 self.txtscore7_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE7_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE7_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE7_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE7_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE7_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE7_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore8_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore8_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE8_Copy.Text = ""
                 self.txtscore8_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE8_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE8_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE8_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE8_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE8_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE8_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore9_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore9_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE9_Copy.Text = ""
                 self.txtscore9_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE9_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE9_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE9_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE9_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE9_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE9_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore10_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore10_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE10_Copy.Text = ""
                 self.txtscore10_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE10_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE10_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE10_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE10_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE10_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE10_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore11_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore11_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE11_Copy.Text = ""
                 self.txtscore11_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE11_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE11_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE11_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE11_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE11_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE11_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore12_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore12_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE12_Copy.Text = ""
                 self.txtscore12_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE12_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE12_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE12_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE12_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE12_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE12_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore13_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore13_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE13_Copy.Text = ""
                 self.txtscore13_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE13_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE13_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE13_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE13_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE13_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE13_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore14_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore14_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE14_Copy.Text = ""
                 self.txtscore14_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE14_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE14_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE14_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE14_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE14_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE14_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def txtscore15_Copy_KeyUp(self, sender, e):
        try:
            score1 = int(self.txtscore15_Copy.Text)
            if score1 == "":
                MessageBox.Show("Enter your score please")
            if score1 > 100:
                 MessageBox.Show("Score is high")
                 self.txtGRADE15_Copy.Text = ""
                 self.txtscore15_Copy.Text = ""
            else: 
                if score1 >=70 and score1 <=100: 
                    self.txtGRADE15_Copy.Text = "A"
                elif score1 >=60 and score1 <=69:
                    self.txtGRADE15_Copy.Text = "B"
                elif score1 >=50 and score1 <=59:
                    self.txtGRADE15_Copy.Text = "C"
                elif score1 >=45 and score1 <=49:
                    self.txtGRADE15_Copy.Text = "D"
                elif score1 >=40 and score1 <=44:
                    self.txtGRADE15_Copy.Text = "E"
                elif score1 >=0 and score1 <=39:
                    self.txtGRADE15_Copy.Text = "F"
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
    
    def Button_Click1(self, sender, e):
        try:
            totalpoints2 = 0

            #perform validations 
            if self.txtcu1_Copy.Text == "":
                self.txtcu1_Copy.Text = "0"
            if self.txtcu2_Copy.Text == "":
                self.txtcu2_Copy.Text = "0"
            if self.txtcu3_Copy.Text == "":
                self.txtcu3_Copy.Text = "0"
            if self.txtcu4_Copy.Text == "":
                self.txtcu4_Copy.Text = "0"
            if self.txtcu5_Copy.Text == "":
                self.txtcu5_Copy.Text = "0"
            if self.txtcu6_Copy.Text == "":
                self.txtcu6_Copy.Text = "0"
            if self.txtcu7_Copy.Text == "":
                self.txtcu7_Copy.Text = "0"
            if self.txtcu8_Copy.Text == "":
                self.txtcu8_Copy.Text = "0"
            if self.txtcu9_Copy.Text == "":
                self.txtcu9_Copy.Text = "0"
            if self.txtcu10_Copy.Text == "":
                self.txtcu10_Copy.Text = "0"
            if self.txtcu11_Copy.Text == "":
                self.txtcu11_Copy.Text = "0"
            if self.txtcu12_Copy.Text == "":
                self.txtcu12_Copy.Text = "0"
            if self.txtcu13_Copy.Text == "":
                self.txtcu13_Copy.Text = "0"
            if self.txtcu14_Copy.Text == "":
                self.txtcu14_Copy.Text = "0"
            if self.txtcu15_Copy.Text == "":
                self.txtcu15_Copy.Text = "0"

            #grade1
            if self.TXTGRADE1_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu1_Copy.Text)
            elif self.TXTGRADE1_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu1_Copy.Text)
            elif self.TXTGRADE1_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu1_Copy.Text)
            elif self.TXTGRADE1_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu1_Copy.Text)
            elif self.TXTGRADE1_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu1_Copy.Text)

            #grade2
            if self.TXTGRADE2_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu2_Copy.Text)
            elif self.TXTGRADE2_Copy.Text == "B": 
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu2_Copy.Text)
            elif self.TXTGRADE2_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00  * int(self.txtcu2_Copy.Text)
            elif self.TXTGRADE2_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00  * int(self.txtcu2_Copy.Text)
            elif self.TXTGRADE2_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00  * int(self.txtcu2_Copy.Text)

            #grade3
            if self.txtGRADE3_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00  * int(self.txtcu3_Copy.Text)
            elif self.txtGRADE3_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00  * int(self.txtcu3_Copy.Text)
            elif self.txtGRADE3_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu3_Copy.Text)
            elif self.txtGRADE3_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu3_Copy.Text)
            elif self.txtGRADE3_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu3_Copy.Text)

            #grade4
            if self.txtGRADE4_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu4_Copy.Text)
            elif self.txtGRADE4_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu4_Copy.Text)
            elif self.txtGRADE4_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu4_Copy.Text)
            elif self.txtGRADE4_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu4_Copy.Text)
            elif self.txtGRADE4_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu4_Copy.Text)

            #grade5
            if self.txtGRADE5_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu5_Copy.Text)
            elif self.txtGRADE5_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu5_Copy.Text)
            elif self.txtGRADE5_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu5_Copy.Text)
            elif self.txtGRADE5_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu5_Copy.Text)
            elif self.txtGRADE5_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu5_Copy.Text)

            #grade6
            if self.txtGRADE6_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu6_Copy.Text)
            elif self.txtGRADE6_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu6_Copy.Text)
            elif self.txtGRADE6_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu6_Copy.Text)
            elif self.txtGRADE6_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu6_Copy.Text)
            elif self.txtGRADE6_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu6_Copy.Text)

            #grade7
            if self.txtGRADE7_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu7_Copy.Text)
            elif self.txtGRADE7_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu7_Copy.Text)
            elif self.txtGRADE7_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu7_Copy.Text)
            elif self.txtGRADE7_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu7_Copy.Text)
            elif self.txtGRADE7_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu7_Copy.Text)

            #grade8
            if self.txtGRADE8_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu8_Copy.Text)
            elif self.txtGRADE8_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu8_Copy.Text)
            elif self.txtGRADE8_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu8_Copy.Text)
            elif self.txtGRADE8_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu8_Copy.Text)
            elif self.txtGRADE8_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu8_Copy.Text)

            #grade9
            if self.txtGRADE9_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu9_Copy.Text)
            elif self.txtGRADE9_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu9_Copy.Text)
            elif self.txtGRADE9_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu9_Copy.Text)
            elif self.txtGRADE9_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu9_Copy.Text)
            elif self.txtGRADE9_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu9_Copy.Text)

            #grade10
            if self.txtGRADE10_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu10_Copy.Text)
            elif self.txtGRADE10_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu10_Copy.Text)
            elif self.txtGRADE10_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu10_Copy.Text)
            elif self.txtGRADE10_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu10_Copy.Text)
            elif self.txtGRADE10_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu10_Copy.Text)

            #grade11
            if self.txtGRADE11_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu11_Copy.Text)
            elif self.txtGRADE11_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu11_Copy.Text)
            elif self.txtGRADE11_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu11_Copy.Text)
            elif self.txtGRADE11_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu11_Copy.Text)
            elif self.txtGRADE11_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu11_Copy.Text)


            #grade12
            if self.txtGRADE12_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu12_Copy.Text)
            elif self.txtGRADE12_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu12_Copy.Text)
            elif self.txtGRADE12_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu12_Copy.Text)
            elif self.txtGRADE12_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu12_Copy.Text)
            elif self.txtGRADE12_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu12_Copy.Text)

            #grade13
            if self.txtGRADE13_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu13_Copy.Text)
            elif self.txtGRADE13_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu13_Copy.Text)
            elif self.txtGRADE13_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu13_Copy.Text)
            elif self.txtGRADE13_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu13_Copy.Text)
            elif self.txtGRADE13_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu13_Copy.Text)

            #grade14
            if self.txtGRADE14_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu14_Copy.Text)
            elif self.txtGRADE14_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu14_Copy.Text)
            elif self.txtGRADE14_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu14_Copy.Text)
            elif self.txtGRADE14_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu14_Copy.Text)
            elif self.txtGRADE14_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu14_Copy.Text)

            #grade15
            if self.txtGRADE15_Copy.Text == "A":
                totalpoints2 = totalpoints2 + 5.00 * int(self.txtcu15_Copy.Text)
            elif self.txtGRADE15_Copy.Text == "B":
                totalpoints2 = totalpoints2 + 4.00 * int(self.txtcu15_Copy.Text)
            elif self.txtGRADE15_Copy.Text == "C":
                totalpoints2 = totalpoints2 + 3.00 * int(self.txtcu15_Copy.Text)
            elif self.txtGRADE15_Copy.Text == "D":
                totalpoints2 = totalpoints2 + 2.00 * int(self.txtcu15_Copy.Text)
            elif self.txtGRADE15_Copy.Text == "E":
                totalpoints2 = totalpoints2 + 1.00 * int(self.txtcu15_Copy.Text)

            totalunits2 = int(self.txtcu1_Copy.Text) + int(self.txtcu2_Copy.Text) + int(self.txtcu3_Copy.Text) + int(self.txtcu4_Copy.Text) + int(self.txtcu5_Copy.Text) + int(self.txtcu6_Copy.Text) + int(self.txtcu7_Copy.Text) + int(self.txtcu8_Copy.Text) + int(self.txtcu9_Copy.Text) + int(self.txtcu10_Copy.Text) + int(self.txtcu11_Copy.Text) + int(self.txtcu12_Copy.Text) + int(self.txtcu13_Copy.Text) + int(self.txtcu14_Copy.Text) + int(self.txtcu15_Copy.Text)
            gpa = totalpoints2 / totalunits2
            globaltotalpoints2 = totalpoints2
            globaltotalunits2 = totalunits2
            self.lblgtpoints2.Content = str(globaltotalpoints2)
            self.lbgcupoints2.Content = str(globaltotalunits2)
            self.lbldisplayfirst_Copy.Content = "First Semester GPA is {gpa}".format(gpa=str(gpa))
        except Exception as ex:
            MessageBox.Show("System Error {error}".format(error=ex.message))
        pass
    
    def Button_Click2(self, sender, e):
        try:
            gpoints1 = float(self.lblgtpoints1.Content)
            gunits1 = float(self.lbgcupoints1.Content)
            gpoints2 = float(self.lblgtpoints2.Content)
            gunits2 = float(self.lbgcupoints2.Content)
            if float(gpoints1) <= 0:
                MessageBox.Show("Please calculate your first semester gpa")
            elif float(gpoints2) <= 0:
                MessageBox.Show("Please calculate your second semester gpa")
            else:
                totalp =  float(gpoints1) + float(gpoints2)
                totalu = float(gunits1) + float(gunits2)
                cpga = totalp / totalu
                self.lbldisplayfirst_Copy1.Content = "CGPA {cgpaaa}".format(cgpaaa=str(cpga))
        except Exception as ex:
            MessageBox.Show(ex.message)
        pass
