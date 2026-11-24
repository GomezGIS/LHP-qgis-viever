import os
from datetime import datetime


class LHPLogger:

    def __init__(self, xml_file):

        self.logfile = os.path.join(
            os.path.dirname(xml_file),
            "lhp_import.log"
        )

    def write(self, text):

        with open(
            self.logfile,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                f"{datetime.now()} | {text}\n"
            )
