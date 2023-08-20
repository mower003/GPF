from GPFUI import GPFUI
from StartUpProcedures import StartUpProcedures

#NOTES 

#When building with autopy-to-exe you must include babel.numbers as hidden import
#additional files -> GPFISHTMLObjects as a folder. This will add everything in that folder.
#Additional files -> database folder make sure DB is included.

#Connect to DB from command line use below from C:\Users\User\Desktop\GPF_Project\GPF\database\sqlite> directory
#sqlite3 c:\Users\User\Desktop\GPF_Project\GPF\database\sqlite\db\gpfdb.db

##C:\Users\dunju\Documents\GPF\database\sqlite
#sqlite3 C:\Users\dunju\Documents\GPF\database\sqlite\db\gpfdb.db
#.headers on
#.mode columns

#Reset the sequence id inside the invoice table because it uses the built one
#SELECT * FROM `sqlite_sequence`;
#UPDATE `sqlite_sequence` SET `seq` = 0 WHERE `name` = 'table_name';

#dlm_fanatik@msn.com

#auto-py-to-exe

##C:\Users\dunju\output\GPF Invoicing Software\database\sqlite\db\gpfdb.db

def main():
    sup = StartUpProcedures()
    sup.getCurrentWorkingDir()
    sup.check_if_DB_exists()

    gpfui = GPFUI()
    gpfui.start()

if __name__ == "__main__":
    main()
