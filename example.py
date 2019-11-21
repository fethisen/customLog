import logging
from customLog import log_mebbis

log_mebbis.logger("Harmless debug Message", logging.DEBUG, "debug.log")
log_mebbis.logger("Just an information", logging.INFO, "info.log")
log_mebbis.logger("Its a Warning", logging.WARNING, "wawrning.log")