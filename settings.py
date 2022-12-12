import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
invalid_password = '1234'
invalid_data = 'РШ4KJvAПi%rRоLs)жЦнскGбMPЪфЪюXгQя1DТGz5б^Uщ6ЧТOwtРy' \
               'ЗlсgA4tйtdш)rЮДЪЩ7uG(qjпxШЪЕoИ^7МеplЕJ@ГgXtr8#буЭSiНYf' \
               'д*ЫDеГ4.РУЭУ7ЪзСD1rнЬt4Ч1гHВhhча6uouПzакr2EtH!h$=Ы$J5n' \
               'ICщfгшфaQO*м2ZБшОFГЗ^eqГhШ#^МдмДZLTр8NJаV4Eнлр1еi7Sсpч%' \
               'МТ*-ZзAрйbжВeЩа!СDOШДю#RЬg7VДazGьыдbQgРeLр67'
invalid_email = '5930@mail.ru'
