from sys import path
path.append("../package")
from packages.printer import Printer
from packages.scanner import Scanner


class MDF3(Scanner, Printer):

    printed_documents = []

    def __init__(self, serial_number, document_name, scan_resolution="1080ppi", print_resolution="1080ppi"):
        self.serial_number = serial_number
        self.scan_resolution = scan_resolution
        self.print_resolution = print_resolution
        self.document_name = document_name

    def scan_document(self):
        print("The document {} has been scanned by device {}".format(
            self.document_name, self.serial_number))

    def get_scanner_status(self):
        print("The device is:", self.serial_number)
        print("The resolution is:", self.scan_resolution)

    def print_document(self):
        print("The document {} has been printed by device {}".format(
            self.document_name, self.serial_number))
        MDF3.printed_documents.append(self.document_name)

    @classmethod
    def get_print_history(cls):
        print("Printing history:")
        for name in cls.printed_documents:
            print("The file has been printend:", name, end="\n")
        print()

    def get_printer_status(self):
        print("The device is:", self.serial_number)
        print("The resolution is:", self.print_resolution)
