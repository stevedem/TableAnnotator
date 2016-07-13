SELECT DISTINCT RowN, ColumnN, ArtTable.Section, idArticle, Article.SpecId, idTable, Article_idArticle, idCell, CellID , Cell.Content, Annotation.Content
idAnnotation, AnnotationID, AnnotationDescription,Cell_idCell, CUI, LAT
FROM UPCI_table_db_spls.Article 
JOIN UPCI_table_db_spls.ArtTable ON(Article_idArticle = idArticle) 
JOIN UPCI_table_db_spls.Cell ON(Table_idTable = idTable) 
JOIN UPCI_table_db_spls.Annotation ON(Cell_idCell = idCell) 
JOIN umls.MRCONSO ON(AnnotationID = CUI)
WHERE Article.SpecId = 'bd9eca8a-87df-46c8-b731-9d8211296e0c' AND LAT = 'ENG' AND idTable = '18336';
/* Very small table, looking at tables of the same drug there are small tables like this for it. 
Valuable table to test heuristics? Section Heuristic does not work with this table. NULL Section.*/