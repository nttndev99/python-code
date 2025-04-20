class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
        
    @property
    def balance(self):
        return self._balance #Getter: Trả về số dư tài khoản
    
    @balance.setter
    def balance(self, value):
        """Setter: Kiểm tra và thay đổi số dư tài khoản"""
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    def deposit(self, amount):
        """Phương thức gửi tiền vào tài khoản"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount  # Gọi setter để thay đổi balance
    def withdraw(self, amount):
        """Phương thức rút tiền từ tài khoản"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount  # Gọi setter để thay đổi balance
# Sử dụng lớp
account = BankAccount(100)  # Khởi tạo tài khoản với số dư 100
print(f"Initial balance: {account.balance}")  # Truy cập số dư tài khoản
account.deposit(50)  # Gửi 50 vào tài khoản
print(f"Balance after deposit: {account.balance}")
account.withdraw(30)  # Rút 30 từ tài khoản
print(f"Balance after withdrawal: {account.balance}")
# Sẽ gây lỗi:
# account.withdraw(200)  # ValueError: Insufficient funds
