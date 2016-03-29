
	#########################################################
	#							#
	#	ScriptValidator v.0.1 by Andrea Dell'Orto	#
	#							#
	#########################################################


Utility che permette di analizzare tutti i file SQL presenti nella directory 'input'.
Per definire il Path di tale directory è possibile utilizzare il file config.ini ed editarne il Path.

Gli errori che vengono cercati sono presenti nel file di configurazione config.ini, nella sezione [errors],
è possibile variare gli errori da cercare aggiungendo dei valori.

Per abilitare la modalità debug è necessario editare la variabile isDebug direttamente nello script,
questa scelta è stata fatta per non abilitare la modalità di debug da configurazione.