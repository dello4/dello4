
	#########################################################
	#							#
	#	ScriptValidator v.0.1 by Andrea Dell'Orto	#
	#							#
	#########################################################


Utility che permette di analizzare tutti i file SQL presenti nella directory 'input'.
Per definire il Path di tale directory � possibile utilizzare il file config.ini ed editarne il Path.

Gli errori che vengono cercati sono presenti nel file di configurazione config.ini, nella sezione [errors],
� possibile variare gli errori da cercare aggiungendo dei valori.

Per abilitare la modalit� debug � necessario editare la variabile isDebug direttamente nello script,
questa scelta � stata fatta per non abilitare la modalit� di debug da configurazione.