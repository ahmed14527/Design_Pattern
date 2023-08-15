class SMSService:
    def send_sms(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")


class SMSServiceProxy:
    def __init__(self, sms_service):
        self.sms_service = sms_service
        self.sms_count = 0

    def send_sms(self, recipient, message):
        self.sms_count += 1
        print(f"Total SMS sent: {self.sms_count}")

        if self.sms_count >= 2:
            print("Not sending SMS. Limit reached.")
            return

        self.sms_service.send_sms(recipient, message)


# Usage
sms_service = SMSService()
proxy = SMSServiceProxy(sms_service)

proxy.send_sms("1234567890", "Hello, World!")
proxy.send_sms("9876543210", "How are you?")
proxy.send_sms("9876543210", "Third SMS")  # This SMS won't be sent due to the limit
