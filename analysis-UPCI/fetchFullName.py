import mysql.connector
from mysql.connector import Error
from mySQLconnect import connect
def fetchFullNameIntAgent():
    try:
        conn = mysql.connector.connect(host='localhost',
                                        database= 'linkedSPLs',
                                        user= 'austin',
                                        password= 'austindbmi')
        cursor = conn.cursor()
        cursor.execute("""SELECT  DISTINCT structuredProductLabelMetadata.FullName, Annotation.Content FROM UPCI_table_db_spls.Annotation
                            JOIN UPCI_table_db_spls.Cell ON(Cell_idCell = idCell)
                            JOIN UPCI_table_db_spls.ArtTable ON(Table_idTable = idTable)
                            JOIN UPCI_table_db_spls.Article ON(Article_idArticle = idArticle)
                            JOIN linkedSPLs.structuredProductLabelMetadata
                            ON(structuredProductLabelMetadata.setId = Article.SpecId)
                            WHERE  AnnotationDescription IN (
                                                'Pharmacologic Substance (phsu)' ,
                                                'Biologically Active Substance (bacs)',
                                                'Organic Chemical (orch)',
                                                'Hazardous or Poisonous Substance (hops)',
                                                'Carbohydrate (carb)',
                                                'Element, Ion, or Isotope (elii)',
                                                'Nucleic Acid, Nucleoside, or Nucleotide (nnon)',
                                                'Indicator, Reagent, or Diagnostic Aid (irda)',
                                                'Biomedical or Dental Material (bodm)',
                                                'Inorganic Chemical (inch)',
                                                'Food (food)')
                                    AND ;""")
        originalDrugList = []
        rows = cursor.fetchall()
        """for row in rows:
            print row
            originalDrugList.append(row) #writes main drug names into a list
        cursor.execute("""SELECT  Annotation.Content FROM UPCI_table_db_spls.Annotation
                            JOIN UPCI_table_db_spls.Cell ON(Cell_idCell = idCell)
                            JOIN UPCI_table_db_spls.ArtTable ON(Table_idTable = idTable)
                            JOIN UPCI_table_db_spls.Article ON(Article_idArticle = idArticle)
                            JOIN linkedSPLs.structuredProductLabelMetadata
                            ON(structuredProductLabelMetadata.setId = Article.SpecId)
                            WHERE  AnnotationDescription IN (
                                                'Pharmacologic Substance (phsu)' ,
                                                'Biologically Active Substance (bacs)',
                                                'Organic Chemical (orch)',
                                                'Hazardous or Poisonous Substance (hops)',
                                                'Carbohydrate (carb)',
                                                'Element, Ion, or Isotope (elii)',
                                                'Nucleic Acid, Nucleoside, or Nucleotide (nnon)',
                                                'Indicator, Reagent, or Diagnostic Aid (irda)',
                                                'Biomedical or Dental Material (bodm)',
                                                'Inorganic Chemical (inch)',
                                                'Food (food)');""")
        interactingDrugList = []
        rows = cursor.fetchall()
        for row in rows:
            print row
            interactingDrugList.append(row) # list slots already pair up with OriginalDrugList """
    except Error as e:
        print (e)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    fetchFullNameIntAgent()
