from abc import ABC, abstractmethod

class BaseCard(ABC):
	
	@abstractmethod
	def __init__(self) -> None:
		pass