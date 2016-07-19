SELECT DISTINCT idTable, 
				Article.SpecId, 
				ArtTable.Section, 
                Cell.Content, 
                fullName,
                Cell.RowN, 
                Cell.ColumnN,
                AnnotationDescription,
                MRCONSO.CUI,
                SPLSetIDToRxNORM.RxCUI,
                MRSTY.TUI,
                MRSTY.STY
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
	JOIN umls.MRCONSO 
		ON(Annotation.AnnotationID = MRCONSO.CUI)
	JOIN umls.MRSTY
		ON (MRCONSO.CUI = MRSTY.CUI)
	JOIN rxnorm.RXNSTY
		ON (MRSTY.TUI = RXNSTY.TUI)
	JOIN rxnorm.RXNCONSO
		ON (RXNSTY.RXCUI=RXNCONSO.RXCUI)
WHERE 	/*Article.SpecId LIKE '2a7ffb2a-2db7-4a19-b58c-8bae33dd349b'*/
		/*RXNSTY.STY LIKE '%pharmacologic%substance%' OR '%organic%chemical%'
		AND*/
		ArtTable.Section LIKE '%drug%interaction%'
				OR '%other%drug%interaction%'
				OR '%interaction%'
				OR '%drug%increase%'
				OR '%drug%decrease%'
				OR '%effect%'
				OR '%effect%drug%'
				OR '%drug%affect%'
				OR '%pharmacodynamic%'
				OR '%contraindicate%'
				OR '%absorption%'
				OR '%distribution%'
				OR '%metabolism%';
		/*AND MRSTY.STY IN ('Pharmacologic Substance (phsu)' ,
					'Biologically Active Substance (bacs)',
					'Organic Chemical (orch)',
					'Hazardous or Poisonous Substance (hops)',
					'Carbohydrate (carb)',
					'Element, Ion, or Isotope (elii)',
					'Nucleic Acid, Nucleoside, or Nucleotide (nnon)',
					'Indicator, Reagent, or Diagnostic Aid (irda)',
					'Biomedical or Dental Material (bodm)',
					'Inorganic Chemical (inch)',
					'Food (food)');*/