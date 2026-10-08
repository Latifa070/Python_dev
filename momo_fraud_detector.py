class MoMoSMS:
    def __init__(self,text):
        self.text = text

    def is_fake(self):
        if  "received"in self.text and "Transaction ID" not in self.text and  "Balance" not in self.text:
            print(" fake")
        else:
            print("Not fake ")

sms = MoMoSMS("You have received 100 cedis. Enjoy")
sms.is_fake()

sms = MoMoSMS("You have received 100 cedis. Transaction ID: 123 Balance: 50")
sms.is_fake()