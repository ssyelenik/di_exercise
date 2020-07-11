
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
from pathlib import Path
import json




class MyForm(FlaskForm):
    id_num=0


    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])




    def get_all_users(self):
        data_folder=Path("C:/BootCamp/di_exercise/week_12/day_2/daily_challenge/login/")
        file_to_open=data_folder / "user.json"
        with open(file_to_open,"r") as users:
            user_list=json.load(users)
        return user_list

    def locate_user(self,name):
        print("from locate user",name)
        user_list=self.get_all_users()
        if len(user_list)>0:
            for i in range(len(user_list)):
                print(name[0].lower(),user_list[i]["first_name"].lower())
                print(name[1].lower(),user_list[i]["last_name"].lower())
                if name[0].lower()==user_list[i]["first_name"].lower() and name[1].lower()==user_list[i]["last_name"].lower():
                     print("got to mach--no update to json file")
                     return True


        return False


    def add_user(self,name):
        data_folder=Path("C:/BootCamp/di_exercise/week_12/day_2/daily_challenge/login/")
        file_to_open=data_folder / "user.json"
        user_list=self.get_all_users()
        id_num=0
        while True:
            print("checking ids")
            id_found="yes"
            for user in user_list:
                print(user['id'],id_num)

                if user['id']==id_num:
                    print("same")
                    id_num+=1
                    id_found="no"
                    break
            if id_found=="yes":
                break

        new_entry={"id":id_num,"first_name":name[0],"last_name":name[1]}
        user_list.append(new_entry)
        with open(file_to_open,"w") as users:
            json.dump(user_list,users)

