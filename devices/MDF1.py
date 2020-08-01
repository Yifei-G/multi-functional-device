from sys import path
path.append("../package")
from packages.printer import Printer
from packages.scanner import Scanner


class MDF1(Scanner, Printer):

    def __init__(self, serial_number, scan_resolution="360ppi", print_resolution="480ppi"):
        self.serial_number = serial_number
        self.scan_resolution = scan_resolution
        self.print_resolution = print_resolution

    def scan_document(self):
        print("The document has been scanned by device {}".format(self.serial_number))

    def get_scanner_status(self):
        print("The device is:", self.serial_number)
        print("The resolution is:", self.scan_resolution)

    def print_document(self):
        print("The document has been printed by device {}".format(self.serial_number))

    def get_printer_status(self):
        print("The device is:", self.serial_number)
        print("The resolution is:", self.print_resolution)
