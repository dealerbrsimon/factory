from abc import ABC, abstractmethod, abstractproperty
from typing import Any,NewType,List

color_name = NewType('color_name',str)

color_code_hex = NewType('color_code',str)

color_code_rbg = NewType('color_code_rbg',str)

color = NewType('color',str)


class ColorBuilder(ABC):
	'''
	La classe ColorBuilder specifie la démarche à suivre pour construire des objects de type couleur
  '''

	@abstractproperty
	def color(self) -> None :
		pass

	@abstractmethod
	def produce_part_a(self) -> None :
		pass

	@abstractmethod
	def produce_part_b(self) -> None :
		pass	

class ColorConcreteBuilder1(ColorBuilder):
	'''
La classe en question poursuit l'implémentation de linterface du constructeur plus général et donne une
implementation concrète pour les étapes du processus de construction. Vous pouvez ajoutez d'autres variations
de constucteurs pour construire autrement si besoin est. 
  	'''		

	def __init__(self)-> None :
		'''
	Une instance concrète du constructeur avec un object vierge qui pourra être utiliser pour construire
	le reste dans le processus d'assemblage	
    		'''
		self.reset()


	def reset(self) -> None :
		self._color = Color1()

	@property
	def color(self) -> Color1	:
		'''
	Les constructeurs concrêts doivent produirent leurs
	méthodes pour récupérer les résutlats.
	
	Cest pour cette raison que des types variés de construceurs peuvent créer de nouvelles couleurs qui
	ne correspondent pas à la même interface. 

	Toutefois, ces méthodes ne peuvent pas être déclarés dans l'interface du Builder primordial,
	considérant un langage typé

	Habituellement, après avoir retourné le résutlat pour main, on s'attends de  l'instance de constructeur
	d'être prête à produire une autre couleur.

	Cest Pourquoi je recommande d'appeller la méthode reset a la fin du bloc de la méthode en question.

	Toutefois, si ce comportement n'est pas obligatoire, vous pouvez faire des construceurs qui attendent
	explicitement une invocation de la méthode reset de la part de main avant de délaisser le fruit de son labeur. Pas facile la vie pour le constructeur !
    		'''
		color = self._color

		self.reset()
		print("Ok...")

		return color


	def produce_part_a(self)-> None :
		'''
	La partie A de l'objet finale implémenté par la méthode du constructeur concrêt 1 
		'''
		self._color.add('middle blue')
		

	def produce_part_b(self) -> None :
		'''
	La partie B de l'objet finale implémenté par la méthode du constructeur concrêt 1 
		'''
		self._color.add('#68D8D6')

	def produce_part_c(self)->None:
		'''
	La partie C de l'objet finale implémenté par la méthode du constructeur concrêt 1 
		'''
		self._color.add('rgb(104,216,214)')	


class Color1 :
	'''
La classe couleur n'est pas très complexe à première vue mais on veux pouvoir ajouter différentes notations
afin de facilité le travail du Décorateur.

Contrairement à d'autres patterns de création, différents constructeurs concrêts peuvent produire des objets
qui ne sont pas vraiment liés,
qui peuvent ne pas suivre pas la même interface.
  	'''

	def __init__(self) -> None : 
		'''
	instancie une objet de type liste pour guarder une oeil sur lensemble des différentes parties. 
		'''	
		self.parts = []


	def add(self,part:Any)-> None :
		'''
	Méthode pour ajouter les différentes parties ensemble pour en faire un tout.	
		'''
		self.parts.append(part)

	def list_parts(self) -> None :
		'''
	Un méthode de courtoisie pour jetter un oeil une liste des différentes parties de lobjet couleur
		'''
		pass
		


class Director : 
	'''
Le Directeur est seulement responsable dexecuter les différentes étapes de la séquence de construction pour une sequence donné.	

Il est utile lorsque vient le temps de produire des couleurs qui ont une configuration spécifique.

À strictement parler, le directeur est optionnel, car main peut controler le constructeur directement 
	'''
  
	def __init__(self)-> None :
		'''
	Les différentes parties de l'objet directeur 
		'''	 
		self._builder = None 


	@property
	def builder(self)->ColorBuilder:
		return self._builder	

	@builder.setter
	def builder(self,builder:ColorBuilder)-> None : 

		'''
Le directeur travaille avec nimporte quelle instance de code que main lui donne. 

Ce faisait, le code du client peut potentiellement altérer le type final de la nouvelle couleur assemblée		
    		'''	

		self._builder = builder 

		'''
	Le directeur peut construire plusieurs couleurs avec les variations du même processus de construction.
	
		'''

	def build_minimal_viable_product(self) -> None : 
		self.builder.produce_part_a()
		print('Bob va faire une couleur')
		

	def build_full_featured_product(self) -> None:
		self.builder.produce_part_a()
		self.builder.produce_part_b()	
		self.builder.produce_part_c()	
		print('Bob je veux plus de details...')

def colorbuilders():
	'''
  Interface cocasse pour illustrer les séquences possibles de construction. Les classes,méthodes et de nombreux 
  éléments du programmes sont en anglais mais commentés intensivement en francais afin de facilier la
  compréhension. Le directeur donne les ordres et le builder exécute dépendemment des instructions qu'il a recu. 
  
  Le builder pourrait très bien fonctionner tout seul toutefois.
  L'invocation de la méthode colorbuilders retourn un constructeur et un directeur.
	'''
	print('\n')

	director = Director()
	builder = ColorConcreteBuilder1()
	director.builder = builder



	director.fais_ca_vite = director.build_minimal_viable_product()
	builder.butch_la_job = builder.color.list_parts()
	director.fais_ca_bien = director.build_full_featured_product()

	builder.prends_sontemp = builder.color.list_parts()

	




	return builder,director



