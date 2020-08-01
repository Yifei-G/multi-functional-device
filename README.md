# multi-functional-device


## Estimated time

40 minutes
Level of difficulty

Medium
## Objectives

1. Creation of abstract classes and abstract methods;
2. Multiple inheritance of abstract classes;
3. Overriding abstract methods;
4. Delivering multiple child classes.

## Scenario
1. You are about to create a multifunction device (MFD) that can scan and print documents;
2. The system consists of a scanner and a printer;
3. Your task is to create blueprints for it and deliver the implementations;
4. Create an abstract class representing a scanner that enforces the following methods:
    - scan_document – returns a string indicating that the document has been scanned;
    - get_scanner_status – returns information about the scanner (max. resolution, serial number)
5. Create an abstract class representing a printer that enforces the following methods:
    - print_document – returns a string indicating that the document has been printed;
    - get_printer_status – returns information about the printer (max. resolution, serial number)
6. Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
    - MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
    - MFD2 – should be a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device;
    - MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.
7. Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.
