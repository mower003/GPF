from GPFUI import GPFUI
from StartUpProcedures import StartUpProcedures


#When building with autopy-to-exe you must include babel.numbers as hidden import
#additional files -> GPFISHTMLObjects as a folder. This will add everything in that folder.
#Additional files -> database folder make sure DB is included.


##C:\Users\dunju\output\GPF Invoicing Software\database\sqlite\db\gpfdb.db

def main():
    sup = StartUpProcedures()
    sup.getCurrentWorkingDir()
    sup.check_if_DB_exists()

    gpfui = GPFUI()
    gpfui.start()

if __name__ == "__main__":
    main()
