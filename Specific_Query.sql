SELECT DISTINCT #Article.SpecId,
				MRDOC.DOCKEY,        
				MRCONSO.SAB,
				MRREL.RUI,        
				MRREL.CUI1,
                MRREL.CUI2,
                MRCONSO.CODE,
				Annotation.AnnotationDescription,
				MRDOC.TYPE,         
				MRREL.REL,
                MRREL.RELA,
				MRDOC.Value,        
				MRDOC.EXPL
				/*Cell.RowN,
				Cell.ColumnN
				Cell.Content*/ FROM umls.MRDOC
	JOIN umls.MRREL ON (MRDOC.VALUE = MRREL.REL)   
	JOIN umls.MRCONSO ON (MRREL.CUI1 = MRCONSO.CUI) 
    JOIN UPCI_table_db_spls.Annotation ON (MRCONSO.CUI = Annotation.AnnotationID)
    /*JOIN UPCI_table_db_spls.Cell ON (Annotation.Cell_idCell = Cell.idCell)
    JOIN UPCI_table_db_spls.ArtTable ON (Cell.Table_idTable = ArtTable.idTable)
    JOIN UPCI_table_db_spls.Article ON (ArtTable.Article_idArticle = Article.idArticle)
WHERE Article.specId = '0a8f3137-0e3a-4a60-a872-cb7d761b30e1'*/
AND MRCONSO.SAB = 'ATC'
AND MRDOC.TYPE = 'expanded_form'      
AND MRDOC.DOCKEY = 'REL' ;
