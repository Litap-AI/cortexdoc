class Message:

    def __init__(
        self,
        sender,
        receiver,
        content
    ):

        self.sender = sender

        self.receiver = receiver

        self.content = content

    def display(self):

        return f"""
FROM: {self.sender}
TO: {self.receiver}

{self.content}
"""
    