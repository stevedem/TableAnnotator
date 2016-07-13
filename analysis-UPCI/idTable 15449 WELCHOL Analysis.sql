SELECT DISTINCT RowN, ColumnN, ArtTable.Section, idArticle, Article.SpecId, idTable, Article_idArticle, idCell, CellID , Cell.Content, Annotation.Content
idAnnotation, AnnotationID, AnnotationDescription,Cell_idCell, CUI, LAT
FROM UPCI_table_db_spls.Article 
JOIN UPCI_table_db_spls.ArtTable ON(Article_idArticle = idArticle) 
JOIN UPCI_table_db_spls.Cell ON(Table_idTable = idTable) 
JOIN UPCI_table_db_spls.Annotation ON(Cell_idCell = idCell) 
JOIN umls.MRCONSO ON(AnnotationID = CUI)
WHERE Article.SpecId = 'b9df447c-b65b-45b9-873a-07a2ab6e2d1f' AND idTable = '15449';
/* Table is a formatting exception, table name is originally foramtted as 0.0 cellID in 
the table(table annotator thinks it is a cell, other tables like this?) TableAnnotator doesn't read
the bottom notes as well and does not include them in reference to their respective boxes? Their
formatting is like that of a regular cell and I see no reason as to why it would not extract that data.*/