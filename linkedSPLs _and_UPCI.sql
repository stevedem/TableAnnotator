SELECT DISTINCT RowN, 
				ColumnN, 
                Cell.Content, 
                idTable,
				TableOrder, 
                Article.SpecId, 
                ArtTable.Section, 
                fullName
FROM linkedSPLs.drug_interactions 
	JOIN linkedSPLs.structuredProductLabelMetadata
		ON (drug_interactions.splId=structuredProductLabelMetadata.id) 
	JOIN linkedSPLs.SPLSetIDToRxNORM 
		ON (structuredProductLabelMetadata.setId=SPLSetIDToRxNORM.setId)  
	JOIN UPCI_table_db_spls.Article 
		ON (SPLSetIDToRxNORM.setId = Article.SpecId) 
	JOIN UPCI_table_db_spls.ArtTable 
		ON (idArticle=Article_idArticle) 
	JOIN UPCI_table_db_spls.Cell 
		ON (ArtTable.idTable=Cell.Table_idTable) 
	JOIN UPCI_table_db_spls.Annotation 
		ON (Annotation.Cell_idCell=Cell.idCell)
WHERE SpecId= 'c5fffc50-2c4c-41a9-9c63-b1a7f8ab76e6' AND ArtTable.Section LIKE '%Drug Interaction%'

ORDER BY idTable ASC, RowN ASC, ColumnN ASC;
