class Email: 
    def __init__(self, subject: str, body: str, sender: str, recipients: list[str]):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.recipients = recipients
        
    def __str__(self) -> str:
        return f"Email(subject={self.subject}, body={self.body}, sender={self.sender}, recipients={self.recipients})"
    
    def send_email(self) -> bool:
        pass

    def read_email(self) -> str:
        pass
    
    def delete_email(self) -> bool:
        pass
    