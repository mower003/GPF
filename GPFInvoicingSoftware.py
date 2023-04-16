from GPFUI import GPFUI
from StartUpProcedures import StartUpProcedures


#When building with autopy you must include babel.numbers as hidden import
#additional files -> GPFISHTMLObjects as a folder. This will add everything in that folder.
#Additional files -> database folder make sure DB is included.

def main():
    sup = StartUpProcedures()
    sup.getCurrentWorkingDir()
    sup.check_if_DB_exists()
    GPFUI.start()

if __name__ == "__main__":
    main()
