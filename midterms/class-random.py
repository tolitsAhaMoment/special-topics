import random

population = [
#'AMBI, TIM M. ',
#'ABDUL, JEMARIE M. ',
#'ACACIO, CHARINA MAE T. ',
#'BERNAL, ZOILO ENRICO C. ',
'CACAS, EARVIN PHILIP M. ',
'CALIXTO, RHOD SHEFFTON S. ',
# 'CAMPOS, CHARLENE JOYCE C.', 
#'CASTRO, FRANZ JERIC C.', 
'CASTRO, SHALOM C. ',
#'CHUA, MARVIN M. ',
'COLLINS, JACQUILINE T. ',
#'CONCEPCION, KEITH T. ',
'DE VERA, GEORGE BRYAN V.', 
#'DEMIRTEPE, MUSTAFA ',
#'DIAZ, LEONARDO II R. ',
#'DLAMINI, SIHLE ',
'EBOJO, CYRIL MAIDEN B.', 
'ELSAFADI, OTHMAN F. ',
#'GALAMAY, KHERVIN X-EL O. ',
'GALAPON, CHARLIE ROD D.', 
'HABAN, CESAR JR. H. ',
# 'HORTALEZA, JHON LAWRENCE A. ', A
#'JOSON, DOMRIX L. ',
# 'KIMPAY, GLEN H. ',
# 'LONGOG, GIRLIE E.', A
#'MADAU, SANDILE ',
# 'MOLINA, JOSHUA D. ',
#'MOLINA, KHRYSS ERROL G. ',
# 'MONIS, JEROME G. ', A
# 'NGOLOB, MICAH AMOR E. ',
#'OPELINIA, JOLINA ROSE V.', 
'ORPILLA, JEFFERSON B. ',
#'PACUDAN, PAULINE ANGEL S. ',
'PALAGANAS, LYKA M. ',
# 'PALPAL, PAOLO JOHN T. ',
# 'PIMENTEL, MARY ANNE CASSANDRA M. ', A
'QUIBEN, CARLO YVAN T. ',
#'REYES, HARA MARIA CARMELA CELSEA P. ',
# 'ROMERO, JOHN JEROME T. ',
#'SALVALEON, ALDWIN A. ',
#'SOKKONG, BENICIO JR F. ',
'SOLOMON, JOHN MICHAEL S. ',
'SORIANO, CLEOFE G. ',
# 'TABORA, SAMMY JOHSUA M. ', A
'VALDEZ, CLARISSA CYCONNE W. ',
#'VALENTON, KATE HOLLI P.', 
#'YUSON, JOHN CARLO D. ',
]

population = set(population)
pop_size = int(input("Enter population size: "))
samples = random.sample(population, pop_size)

for names in samples :
	print names
