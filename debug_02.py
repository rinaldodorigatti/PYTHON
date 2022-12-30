import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Ca c'est du debug")
logging.info("Ca c'est du info")
logging.warning("Ca c'est du warning")
logging.error("Ca c'est du error")
logging.critical("Ca c'est du critical")

# order debug, info, warning, error, critical
# if you disable warning logging all predecessors are disabled
logging.disable(logging.WARNING)
logging.warning("Ca c'est du warning disable")
logging.critical("Ca c'est du critical disable")
logging.error("Ca c'est du error après warning disable")
