SELECT DISTINCT RowN, ColumnN, ArtTable.Section, idArticle, Article.SpecId, idTable, Article_idArticle, idCell, CellID , Cell.Content, Annotation.Content
idAnnotation, AnnotationID, AnnotationDescription,Cell_idCell, CUI, LAT
FROM UPCI_table_db_spls.Article 
JOIN UPCI_table_db_spls.ArtTable ON(Article_idArticle = idArticle) 
JOIN UPCI_table_db_spls.Cell ON(Table_idTable = idTable) 
JOIN UPCI_table_db_spls.Annotation ON(Cell_idCell = idCell) 
JOIN umls.MRCONSO ON(AnnotationID = CUI)
WHERE SpecID = '000e2ca1-9a11-46f2-860c-4de0ca5be369' AND idTable = '2014';
/*Sodium Iodide 131, small table with very simple layout, would be identified with our first 2 heuristics
*/