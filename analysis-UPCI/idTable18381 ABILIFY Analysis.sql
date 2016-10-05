SELECT DISTINCT RowN, ColumnN, idArticle, Article.SpecId, idTable, Article_idArticle, idCell, CellID , Cell.Content,
idAnnotation, AnnotationID, AnnotationDescription,Cell_idCell, CUI, LAT
FROM UPCI_table_db_spls.Article 
JOIN UPCI_table_db_spls.ArtTable ON(Article_idArticle = idArticle) 
JOIN UPCI_table_db_spls.Cell ON(Table_idTable = idTable) 
JOIN UPCI_table_db_spls.Annotation ON(Cell_idCell = idCell) 
JOIN umls.MRCONSO ON(AnnotationID = CUI)
WHERE Article.SpecId = 'c040bd1d-45b7-49f2-93ea-aed7220b30ac' AND LAT = 'ENG' AND idTable = '18381';