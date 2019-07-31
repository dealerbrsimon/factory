'''
Exemple d'utilisation par une méthode client(main) avec l'interface amusante pour illustrer le fonctionnement du programme
aux développeurs.
'''


from colorbuilder import colorbuilders as cb 


def main():

	bob,marie = cb()
	'''
	L'invocation de cb retourne un constructeur ainsi qu'un directeur pour le constructeur en question.
	Le directeur est déjà lié avec le constructeur via l'invocation de la méthode, ses invocations guident 
	les actions du constructeur, qui aurait pu le faire de manière indépendante si on l'avais désiré.
	Si vous désirer séparer les fonctionnalités du constructeur et du directeur, prière de me le faire 
	savoir.
	'''
	
	marie.fais_ca_vite
	
	bob.butch_la_job
	
	marie.fais_ca_bien

	bob.prends_sontemp

	



	return 0


if __name__ == '__main__':
	main()
