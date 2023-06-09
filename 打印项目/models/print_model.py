from utils import connect_db
import win32print
import win32api
import time
import os
def get_queue_length():
    conn = connect_db()
    if not conn:
        return 0
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM printfile"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count

def print_file( filename, copies, side, color):
    #print("Printing:", filedata, filename, copies, side, color)
    try:
        name = win32print.GetDefaultPrinter()

        #printdefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_ADMINISTER}
        printdefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_USE}
        handle = win32print.OpenPrinter(name, printdefaults)

        level = 2
        attributes = win32print.GetPrinter(handle, level)

        print("Old Duplex = %d" % attributes['pDevMode'].Duplex)
        attributes['pDevMode'].PaperSize = 9  # Set paper size to A4
        if side == '双面':
            attributes['pDevMode'].Orientation = 2  # Set duplex printing
        else:
            attributes['pDevMode'].Orientation = 1  # Set single-side printing
        if color == '彩色':
            attributes['pDevMode'].Color = 1  # Set color printing
        else:
            attributes['pDevMode'].Color = 2  # Set black-and-white printing
        print(type(copies))
        attributes['pDevMode'].Copies = copies    # flip over

        ## 'SetPrinter' fails because of 'Access is denied.'
        ## But the attribute 'Duplex' is set correctly
        try:
            win32print.SetPrinter(handle, level, attributes, 0)
        except:
            print("win32print.SetPrinter: set 'Duplex'")
        for i in range(copies):
            print(i)
            res = win32api.ShellExecute(0, 'print', filename, None, '.', 0) 
        win32print.ClosePrinter(handle)

        # Delete the printed file from the database
        conn = connect_db()
        if not conn:
            return
        cursor = conn.cursor()
        delete_query = "DELETE FROM printfile WHERE filename = %s"
        cursor.execute(delete_query, (filename,))
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(e)
        print("Printing Error:", str(e))

# def print_file(filedata, filename, copies, side, color):
#     print("Printing:", filename)
#     # Perform printing operation using win32print
#     printer_name = "Canon TS3400 series"
#     handle = win32print.OpenPrinter(printer_name)
#     print(handle)
#     try:
#         # Set the printer properties
#         properties = win32print.GetPrinter(handle, 2)
#         devmode = properties['pDevMode']
#         print(dict(devmode))
#         devmode.PaperSize = 9  # Set paper size to A4
#         if side == '双面':
#             devmode.Orientation = 2  # Set duplex printing
#         else:
#             devmode.Orientation = 1  # Set single-side printing
#         if color == '彩色':
#             devmode.Color = 1  # Set color printing
#         else:
#             devmode.Color = 2  # Set black-and-white printing
        
#         win32print.SetPrinter(handle, 2, properties, 0)

#         # Start the printing job
#         win32print.StartDocPrinter(handle, 1, (filename, None, "RAW"))
#         for i in range(copies):
#             win32print.StartPagePrinter(handle)
#             win32print.WritePrinter(handle, filedata)
#             win32print.EndPagePrinter(handle)

#         # End the printing job and close the printer handle
#         win32print.EndDocPrinter(handle)
#         win32print.ClosePrinter(handle)

#         # Delete the printed file from the database
#         conn = connect_db()
#         if not conn:
#             return
#         cursor = conn.cursor()
#         delete_query = "DELETE FROM printfile WHERE filename = %s"
#         cursor.execute(delete_query, (filename,))
#         conn.commit()
#         cursor.close()
#         conn.close()

#     except Exception as e:
#         print(e)
#         print("Printing Error:", str(e))

def print_first_file():
    conn = connect_db()
    if not conn:
       return
    cursor = conn.cursor()
    query = "SELECT file, filename, copies, side, color FROM printfile LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        filedata, filename, copies, side, color = result
        
        print_file( os.getcwd()+'/tmp/tmp_'+filename, copies, side, color)
    cursor.close()
    conn.close()

def print_files():
    while True:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM printfile"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        if count > 1:
            print_first_file()
        time.sleep(1)