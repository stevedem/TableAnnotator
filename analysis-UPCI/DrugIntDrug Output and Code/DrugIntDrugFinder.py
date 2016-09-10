import mysql.connector
from mysql.connector import Error

def connect():
    #connect to db
    try:
        conn = mysql.connector.connect(host='localhost',
                                        database= 'UPCI_table_db_spls',
                                        user= 'austin',
                                        password= 'austindbmi')
        if conn.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(e)
def finder():
    try:
        conn = mysql.connector.connect(host='localhost',
                                        database= 'UPCI_table_db_spls',
                                        user= 'austin',
                                        password= 'austindbmi')
        cursor = conn.cursor()
        cursor.execute("""SELECT  DISTINCT structuredProductLabelMetadata.FullName, Annotation.Content, Section
                            FROM UPCI_table_db_spls.Annotation
                            JOIN UPCI_table_db_spls.Cell ON(Cell_idCell = idCell)
                            JOIN UPCI_table_db_spls.ArtTable ON(Table_idTable = idTable)
                            JOIN UPCI_table_db_spls.Article ON(Article_idArticle = idArticle)
                            JOIN linkedSPLs.structuredProductLabelMetadata ON(structuredProductLabelMetadata.setId = Article.SpecId)
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
                                AND (RowN = '0' OR ColumnN ='0')
                                AND (Section LIKE '7%' OR
                                    Section LIKE '%drug%interactions%')
                                AND (Annotation.Content NOT IN('drugs','drug', 'mg', 'food'));""")
        rows = cursor.fetchall()
        for row in rows:
            print row
    except error as e:
        print (e)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    connect()
    finder()
