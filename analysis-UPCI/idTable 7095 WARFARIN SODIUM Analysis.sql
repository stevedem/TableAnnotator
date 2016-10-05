SELECT DISTINCT RowN, ColumnN, ArtTable.Section, idArticle, Article.SpecId, idTable, Article_idArticle, idCell, CellID , Cell.Content, Annotation.Content
idAnnotation, AnnotationID, AnnotationDescription,Cell_idCell, CUI, LAT
FROM UPCI_table_db_spls.Article 
JOIN UPCI_table_db_spls.ArtTable ON(Article_idArticle = idArticle) 
JOIN UPCI_table_db_spls.Cell ON(Table_idTable = idTable) 
JOIN UPCI_table_db_spls.Annotation ON(Cell_idCell = idCell) 
JOIN umls.MRCONSO ON(AnnotationID = CUI)
WHERE Article.SpecId = '4445c26e-ec5c-40f4-956b-93c12fc73c1d' AND idTable = '7095';
/*Only problem with table annotator is the table listed has the heading "Table 3
Drugs that Can Increase the Risk of Bleeding" Which is identical in definition but not 
in wording the Section which tableannotator pulled out*/