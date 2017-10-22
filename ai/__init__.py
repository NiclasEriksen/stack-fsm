import logging
from .brain import Brain
from .states import BaseState as State

logging.getLogger(__name__).addHandler(logging.NullHandler())

try:
	import coloredlogs
	coloredlogs.install(
		level="DEBUG",
		fmt="%(asctime)s %(levelname)s %(message)s"
	)
except ImportError:
	print("coloredlogs not installed, not enabling log color.")