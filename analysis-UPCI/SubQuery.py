import mysql.connector
from mysql.connector import Error
import keyword
import re

def firstQuery():
     rel = {}
     duplicates = []
     try:
         conn = mysql.connector.connect(host='localhost',
                                         database= 'UPCI_table_db_spls',
                                         user= 'anaygupta',
                                         password= 'anayguptadbmi')
         cursor = conn.cursor()
         cursor2 = conn.cursor()
         rel = {}
         print "Executing query..."
         print '\n'
         cursor.execute("""SELECT DISTINCT
                                            /*Annotation.Content,
                                            Cell.Content,

                                            Article.SpecId,*/
                                            MRREL.CUI1,
                                            ArtTable.Section,
                                            MRCONSO.CODE,
                                            MRCONSO.STR,
                                            Cell.RowN,
                                            Cell.ColumnN,
                                            Article.SpecId,
                                            ArtTable.idTable
                                            FROM umls.MRDOC
                                            JOIN umls.MRREL ON (MRDOC.VALUE = MRREL.REL)
                                            JOIN umls.MRCONSO ON (MRREL.CUI1 = MRCONSO.CUI)
                                            JOIN UPCI_table_db_spls.Annotation ON (MRCONSO.CUI = Annotation.AnnotationID)
                                            JOIN UPCI_table_db_spls.Cell ON (Annotation.Cell_idCell = Cell.idCell)
                                            JOIN UPCI_table_db_spls.ArtTable ON (Cell.Table_idTable = ArtTable.idTable)
                                            JOIN UPCI_table_db_spls.Article ON (ArtTable.Article_idArticle = Article.idArticle)
                                            WHERE MRCONSO.SAB = %s
                                            AND MRDOC.TYPE = %s
                                            AND MRDOC.DOCKEY = %s
                                            AND Annotation.AnnotationDescription IN ('Pharmacologic Substance (phsu)' ,
                                                                                       'Biologically Active Substance (bacs)',
                                                                                       'Organic Chemical (orch)',
                                                                                       'Hazardous or Poisonous Substance (hops)',
                                                                                       'Carbohydrate (carb)',
                                                                                       'Element, Ion, or Isotope (elii)',
                                                                                       'Nucleic Acid, Nucleoside, or Nucleotide (nnon)',
                                                                                       'Indicator, Reagent, or Diagnostic Aid (irda)',
                                                                                       'Biomedical or Dental Material (bodm)',
                                                                                       'Inorganic Chemical (inch)',
                                                                                       'Food (food)') LIMIT 100;""", ('ATC', 'expanded_form', 'REL'))
         print "Query executed successfully"
         rows = cursor.fetchall()
         level = 0
         for row in rows:
             if re.search('.*7\..*', unicode(row[1])) or re.search(('.*drugs.*interactions.*'), unicode(row[1])) or re.search('.*drug.*alter.*', unicode(row[1])) or re.search('.*drug.*increase.*', unicode(row[1])) or re.search('.*drug.*concentration.*', unicode(row[1])) or re.search('.*drug.*potentiate.*', unicode(row[1])):
                 if len(str(row[2])) == 1:
                     level = 1
                 elif len(str(row[2])) == 3:
                     level = 2
                 elif len(str(row[2])) == 4:
                     level = 3
                 elif len(str(row[2])) == 5:
                     level = 4
                 else:
                     level = 5
                 if level == 5:
                     print 'Ingredient'
                     print row[3]
                     print row[2]
                     print row[4], row[5]
                     print row[6]
                     print row[7]
                 print '\n'
     except Error as e:
         print (e)
     finally:
        cursor.close()
        cursor2.close()
        conn.close()

if __name__ == '__main__':
     firstQuery()
