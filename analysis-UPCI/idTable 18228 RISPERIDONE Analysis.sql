SELECT DISTINCT RowN, ColumnN, idArticle, Article.SpecId, idTable, Article_idArticle, idCell, CellID , Cell.Content, Annotation.Content
idAnnotation, AnnotationID, AnnotationDescription,Cell_idCell, CUI, LAT
FROM UPCI_table_db_spls.Article 
JOIN UPCI_table_db_spls.ArtTable ON(Article_idArticle = idArticle) 
JOIN UPCI_table_db_spls.Cell ON(Table_idTable = idTable) 
JOIN UPCI_table_db_spls.Annotation ON(Cell_idCell = idCell) 
JOIN umls.MRCONSO ON(AnnotationID = CUI)
WHERE Article.SpecId = 'd072638f-70d6-4ce9-a0d4-16db4b31d824' AND LAT = 'ENG' AND idTable = '18228';
/* Query returns the data on a very large table does not return null boxes which is good. The column and row
assignment is accurate. */