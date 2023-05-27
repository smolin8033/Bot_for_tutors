import logging
from textwrap import wrap


class MultiLineHandler(logging.StreamHandler):
    def __init__(self, line_length: int):
        logging.StreamHandler.__init__(self)
        self.line_length = line_length

    def emit(self, record: logging.LogRecord) -> None:
        record.msg = "\n".join(wrap(record.msg, self.line_length))
        super().emit(record)
