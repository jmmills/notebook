SELECT 
	concat(table_schema,'.',table_name) AS table_name, 
	ROUND( 
		( (data_length + index_length) / 1024 / 1024 ),
	2) AS "Size in MB" 
FROM information_schema.TABLES 
ORDER BY (data_length + index_length) DESC;