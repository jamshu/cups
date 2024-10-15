# dummy_cups/__init__.py
class Connection:
    def printFile(self, printer_name, filename, job_name=None):
        print(f"Mock printing file '{filename}' to printer '{printer_name}'.")

def getPrinters():
    return {"MockPrinter": "Mock Printer"}
