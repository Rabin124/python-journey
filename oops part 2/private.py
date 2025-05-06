class Account:
  def __init__(self,acc_no,acc_pass):
    self.__acc_no = acc_no
    self.__acc_pass = acc_pass

  def reset_pass():
    print(acc1.__acc_pass)  # This will raise an AttributeError because __acc_pass is private

acc1 = Account(1234567890, "password123")
print(acc1.acc_no)  # This will raise an AttributeError because __acc_no is private
print(acc1.reset_pass())  