import logging

log = logging.getLogger(__name__)


class BaseState(object):
	name = "base"

	def __init__(self, brain):
		self.brain = brain

	@property
	def owner(self):
		return self.brain.owner

	def pop(self):
		self.brain.pop()

	# What follows is empty methods to be overloaded.
	def on_enter(self):
		pass

	def on_exit(self):
		pass

	def process(self, dt):
		pass

	def __repr__(self):
		return "<{}>".format(self.__class__.__name__)


class Idle(BaseState):
	name = "idle"

	def __init__(self, brain):
		BaseState.__init__(self, brain)

	def on_enter(self):
		log.debug("Entered idle state.")

	def on_exit(self):
		log.debug("Left idle state.")
