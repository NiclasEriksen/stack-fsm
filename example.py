from ai import Brain, State


"""
Define a state, apart from the default "Idle" state that does nothing.
States must inherit from State, and contain a name attribute.
"""
class Attack(State):
	name = "attack"

	def __init__(self, brain):
		State.__init__(self, brain)
		self.cooldown_timer = 0.0

	def on_enter(self):
		# This method is called when state is entered, either when pushed to
		# the stack, or when a state in front of it is removed and it becomes
		# the active state.
		print("We're now in the Attack state!")

	def process(self, dt):
		# The brain calls this method every time it's updated, this is where
		# you write the logic for the state.
		if self.cooldown_timer <= 0.0:
			# Here we interact with the brain's owner
			self.brain.owner.attack()
			self.cooldown_timer = self.brain.owner.attack_cooldown
		else:
			self.cooldown_timer -= dt


class Agent:
	def __init__(self):
		self.brain = Brain(self)
		self.attack_cooldown = 1.5

	def attack(self):
		print("I'm attacking!")

	def update(self, dt):
		self.brain.update(dt)


if __name__ == "__main__":
	import time
	a = Agent()
	a.brain.register(Attack)
	a.brain.push("attack")
	while True:
		a.update(0.1)
		time.sleep(0.1)
