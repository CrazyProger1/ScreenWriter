class DocumentError(Exception):
    pass


class FormatError(DocumentError):
    def __init__(self, msg):
        self.msg = msg
        super(FormatError, self).__init__(msg)
