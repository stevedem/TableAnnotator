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
                                            Article.SpecId,
                                            MRREL.CUI1,*/
                                            ArtTable.Section,
                                            MRCONSO.CODE,
                                            MRCONSO.STR,
                                            Cell.RowN,
                                            Cell.ColumnN,
                                            Article.SpecId,
                                            ArtTable.idTable
                                            #structuredProductLabelMetadata.fullName
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
                                            AND ArtTable.idTable IN ('39', '75', '229', '169', '209', '249', '355', '552', '704', '8590', '14194', '13141')
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
                                                                                       'Food (food)') 
                                            AND  (ArtTable.Section LIKE '7%' OR
                                                Section LIKE '%drug%interactions%' OR
                                                Section LIKE '%drug%alter%' OR
                                                Section LIKE '%drug%increase%' OR
                                                Section LIKE '%drug%concentration%' OR
                                                Section LIKE  '%drug%potentiate%');""", ('ATC', 'expanded_form', 'REL'))
         print "Query executed successfully"
         rows = cursor.fetchall()
         level = 0
         for row in rows:
            setid = str(row[5])
            drug = str(row[2])
            if re.search('.*7..*', unicode(row[0])) or re.search(('.*drugs.*interactions.*'), unicode(row[0])) or re.search('.*drug.*alter.*', unicode(row[0])) or re.search('.*drug.*increase.*', unicode(row[0])) or re.search('.*drug.*concentration.*', unicode(row[0])) or re.search('.*drug.*potentiate.*', unicode(row[0])):
                if len(str(row[1])) == 1:
                    level = 1
                elif len(str(row[1])) == 3:
                    level = 2
                elif len(str(row[1])) == 4:
                    level = 3
                elif len(str(row[1])) == 5:
                    level = 4
                else:
                    level = 5
                if level == 5:
                    cursor2.execute("""SELECT structuredProductLabelMetadata.fullName                                          
                                    FROM linkedSPLs.structuredProductLabelMetadata 
                                        WHERE setId = %s
                                        AND fullName != %s;""", (setid, drug))
                    data = cursor2.fetchall()
                    if (len(data) > 0):
                        print 'Ingredient'
                        print row[1]
                        print row[2]
                        print row[3], row[4]
                        print row[5]
                        print row[6]
                    print '\n'
                
     except Error as e:
         print (e)
     finally:
        cursor.close()
        cursor2.close()
        conn.close()

if __name__ == '__main__':
     firstQuery()
