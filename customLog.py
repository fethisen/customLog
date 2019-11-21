import logging

"""
   Farklı log seviyelerine gore farklı dosyalara kayit atmayı saglar.
"""


class LogMebbis():

    def setup_logger(self, logger_name, log_file_name, level):
        """
        log serviyelerine gore ayri ayri loggerları oluşturumamizi saglar.
        :param logger_name: log seviyelerine gore ayri ayri loggerlar olusturmak icin kullanılan parametre
        :param log_file_name: log atilacak dosya ismi
        :param level: log seviyesi
        :return:
        """
        log_setup = logging.getLogger(logger_name)
        formatter = logging.Formatter('%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler = logging.FileHandler(log_file_name, mode='w')
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        log_setup.setLevel(level)
        log_setup.addHandler(fileHandler)
        log_setup.addHandler(streamHandler)

    def logger(self, msg, level, log_file_name):
        """
        tutulacak log bilgilerini, log seviyseini ve log atilacak dosya bilgisini de alarak
        log tutmayi saglayan metot.
        :param msg: yazilacak mesaj bilgisi
        :param level: log seviyesi
        :param log_file_name:
        :return:
        """
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        if level == logging.DEBUG:
            self.setup_logger('log_debug', log_file_name, logging.DEBUG)
            logger = logging.getLogger('log_debug')
            logger.debug(msg)

        if level == logging.INFO:
            self.setup_logger('log_info', log_file_name, logging.INFO)
            logger = logging.getLogger('log_info')
            logger.info(msg)

        if level == logging.WARNING:
            self.setup_logger('log_warning', log_file_name, logging.WARNING)
            logger = logging.getLogger('log_warning')
            logger.warning(msg)

        if level == logging.ERROR:
            self.setup_logger('log_error', log_file_name, logging.ERROR)
            logger = logging.getLogger('log_error')
            logger.error(msg)


log_mebbis = LogMebbis()
