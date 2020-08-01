from sys import path
from devices.MDF1 import MDF1
from devices.MDF2 import MDF2
from devices.MDF3 import MDF3

separate_line = "*" * 20
print(separate_line)
print("MDF type 1:")
mdf1 = MDF1("GYF2046")

mdf1.print_document()
mdf1.get_printer_status()
mdf1.scan_document()
mdf1.get_scanner_status()

print(separate_line)
print("MDF type 2:")
mdf2_1 = MDF2("GYF3000", "test.pdf")

mdf2_1.print_document()
mdf2_1.get_printer_status()
mdf2_1.scan_document()
mdf2_1.get_scanner_status()


mdf2_2 = MDF2("GYF3000", "exam.pdf")
mdf2_3 = MDF2("GYF3000", "password.txt")


mdf2_2.print_document()
mdf2_2.scan_document()


mdf2_3.print_document()
mdf2_3.get_printer_status()
mdf2_3.scan_document()
mdf2_3.get_scanner_status()

MDF2.get_print_history()

print(separate_line)
print("MDF type 3:")

mdf3_1 = MDF3("GYF3000", "book1.pdf")

mdf3_1.print_document()
mdf3_1.get_printer_status()
mdf3_1.scan_document()
mdf3_1.get_scanner_status()


mdf3_2 = MDF2("GYF3000", "book2.pdf")
mdf3_3 = MDF2("GYF3000", "recipe.txt")


mdf3_2.print_document()
mdf3_2.scan_document()


mdf3_3.print_document()
mdf3_3.get_printer_status()
mdf3_3.scan_document()
mdf3_3.get_scanner_status()

MDF3.get_print_history()
