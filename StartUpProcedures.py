import os

class StartUpProcedures():

    absolute_path = os.path.dirname(__file__)

    db_relative_path = "database\sqlite\db\gpfdb.db"
    css_relative_path = "GPFISHTMLObjects\Invoices\css\gpf.css"
    template_relative_path = "GPFISHTMLObjects\Invoices\\template\gpf.html"
    images_relative_path = "GPFISHTMLObjects\Invoices\imgs\green-leaf-logo-vector.jpg"

    db_full_path = os.path.join(absolute_path, db_relative_path)
    css_full_path = os.path.join(absolute_path, css_relative_path)
    template_full_path = os.path.join(absolute_path, template_relative_path)
    images_full_path = os.path.join(absolute_path, images_relative_path)


    def getCurrentWorkingDir(self):
        print("ABS: {0}".format(self.absolute_path))
        print("DB: {0}".format(self.db_full_path))
        print('CSS: ', self.css_full_path)
        print('TMPLT: ', self.template_full_path)
        print('IMG: ', self.images_full_path)

    def check_if_DB_exists(self):
        print(os.path.isfile(self.db_full_path))
        pass

    def check_if_HTML_Objects_exist(self):
        #check for GPFISHTMLObjects folder. Should contain (invoices/css/gpf.css, invoices/images/gpf_logo.jpg, template/gpf_template.html)
        pass

sup = StartUpProcedures()
sup.check_if_DB_exists()