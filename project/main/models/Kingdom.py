class Kingdom:

    """
    Model to represent Kingdom
    """

    def __init__(self, name: str, emblem: str):

        """
        : name : Name of the Kingdom
        : emblem : Emblem of the Kingdom
        """

        self.name = name
        self.emblem = emblem

    def send_message(self, reciever_kingdom: Kingdom, message: str) -> bool:

        """
        Send Message to the Reciever Kingdom and check if it is an ally
        : reciever_kingdom : Kingdom Object of the Kingdom to whom message is sent
        : message : String message to be sent to the other country
        """

        return reciever_kingdom.recieve_message(message)

    def recieve_message(self, message: str) -> bool:

        """
        Check if the message recived has the emblem after decryption
        : message : Recieved string message
        """

        return False

    def __str__(self):

        """
        Return String representation of the object
        """
        return self.name + " " + self.emblem
