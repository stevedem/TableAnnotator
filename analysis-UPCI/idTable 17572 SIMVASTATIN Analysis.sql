SELECT DISTINCT RowN, ColumnN, ArtTable.Section, idArticle, Article.SpecId, idTable, Article_idArticle, idCell, CellID , Cell.Content, Annotation.Content
idAnnotation, AnnotationID, AnnotationDescription,Cell_idCell, CUI, LAT
FROM UPCI_table_db_spls.Article 
JOIN UPCI_table_db_spls.ArtTable ON(Article_idArticle = idArticle) 
JOIN UPCI_table_db_spls.Cell ON(Table_idTable = idTable) 
JOIN UPCI_table_db_spls.Annotation ON(Cell_idCell = idCell) 
JOIN umls.MRCONSO ON(AnnotationID = CUI)
WHERE Article.SpecId = 'ff4a8eab-17d5-caf4-efba-7e7688202bf5' AND idTable = '17572';
/* large data set, tableAnnotator seems to work*/