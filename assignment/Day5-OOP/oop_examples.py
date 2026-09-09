# from pydantic import BaseModel, model_validator

# class User(BaseModel):
#     password: str
#     confirm_password: str

#     @model_validator(mode="after")
#     def validate_passwords(self):
#         if self.password != self.confirm_password:
#             raise ValueError("Password and Confirm Password do not match")
#         return self

# try:
#     user = User(
#         password=input("Enter Password: "),
#         confirm_password=input("Confirm Password: ")
#     )
#     print("Password confirmed successfully")
# except Exception as e:
#     print(e)

from pydantic import BaseModel, model_validator

class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="before")
    @classmethod
    def validate_passwords(cls, data):
        if data["password"] != data["confirm_password"]:
            raise ValueError("Password and Confirm Password do not match")
        return data

try:
    user = User(
        password=input("Enter Password: "),
        confirm_password=input("Confirm Password: ")
    )
    print("Password confirmed successfully")
except Exception as e:
    print(e)