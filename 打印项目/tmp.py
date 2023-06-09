import win32api
import win32print

name = win32print.GetDefaultPrinter()

#printdefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_ADMINISTER}
printdefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_USE}
handle = win32print.OpenPrinter(name, printdefaults)

level = 2
attributes = win32print.GetPrinter(handle, level)

print("Old Duplex = %d" % attributes['pDevMode'].Duplex)

#attributes['pDevMode'].Duplex = 1    # no flip
#attributes['pDevMode'].Duplex = 2    # flip up
attributes['pDevMode'].Duplex = 3    # flip over

## 'SetPrinter' fails because of 'Access is denied.'
## But the attribute 'Duplex' is set correctly
try:
    win32print.SetPrinter(handle, level, attributes, 0)
except:
    print("win32print.SetPrinter: set 'Duplex'")

res = win32api.ShellExecute(0, 'print', r'C:\Users\15379\Downloads/111.docx', None, '.', 0)

win32print.ClosePrinter(handle)