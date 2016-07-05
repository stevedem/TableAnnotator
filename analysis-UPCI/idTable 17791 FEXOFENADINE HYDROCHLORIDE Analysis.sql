SELECT DISTINCT RowN, ColumnN, idArticle, Article.SpecId, idTable, Article_idArticle, idCell, CellID , Cell.Content, Annotation.Content
idAnnotation, AnnotationID, AnnotationDescription,Cell_idCell, CUI, LAT
FROM UPCI_table_db_spls.Article 
JOIN UPCI_table_db_spls.ArtTable ON(Article_idArticle = idArticle) 
JOIN UPCI_table_db_spls.Cell ON(Table_idTable = idTable) 
JOIN UPCI_table_db_spls.Annotation ON(Cell_idCell = idCell) 
JOIN umls.MRCONSO ON(AnnotationID = CUI)
WHERE Article.SpecId = 'f4a41d2b-9f00-4768-b375-5749793e7de3' AND LAT = 'ENG' AND idTable = '17791';
/* tables.html seems much more accurate in parsing out tables only related to PDDIs. When querying for tables 
with this SpecID many tables showed up containing dosing information not pertinent to PDDIs */