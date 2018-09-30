#!/usr/bin/python3

#        отступы пробелами
#        by Andrew Sotnikov aka Luca Brasi,
#        e-mail: andrew.sotnikov@zoho.com
#        --------------

#        clearing cash in DB and removing log file_as_well  


from saumysql import Crud
from subprocess import call

passwd = "fearofthedark"
logfile = "/var/log/andrew/good_verse_mailer.log"

#removing temporary tables from DataBase
crud = Crud('localhost','andrew','andrew','verses')
crud.sql = ("DROP TABLE queue, time_marks")
crud.deleteAct()

#clearing logs
call("echo \"{0}\" | sudo -S rm {1}".format(passwd, logfile), shell=True, universal_newlines=True)
