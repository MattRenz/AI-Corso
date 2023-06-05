"""In questo esempio, utilizziamo la funzione read_csv() di pandas per caricare il dataset. 
Passiamo l'URL del dataset come primo parametro e specifichiamo il parametro di compressione 
come 'gzip', poiché il dataset è compresso in formato gzip. Impostiamo anche il parametro 
header a None, poiché il set di dati non ha una riga di intestazione, e usiamo il parametro 
sep per specificare che le colonne sono separate da '\t'.

Infine, si utilizza il parametro names per specificare i nomi delle colonne come 'review' e 
'label'. Questo creerà un dataframe pandas con due colonne: 'review', che contiene il testo 
della recensione del film, e 'label', che contiene il sentiment della recensione (o 'pos' o 
'neg').

Il dataframe risultante avrà le prime righe del dataset di recensioni di film IMDB, con il 
testo della recensione e l'etichetta del sentiment per ogni riga.
"""

import pandas as pd

# Load the IMDB movie review dataset
df = pd.read_csv('https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz', 
                 compression='gzip', on_bad_lines="skip", header=None, sep='\t', names=['review', 'label'])

# Print the first few rows of the dataframe
print(df.head())
