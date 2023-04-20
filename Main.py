import mysql.connector
from mysql.connector import errorcode
import os, sys
from colorama import just_fix_windows_console
from termcolor import colored


class Main():
    def __init__(self) -> None:
        just_fix_windows_console()
        connection = self.mysql_connection('localhost', 'root', '','enem')
        if not connection:
            return print(colored("Não conectou ao banco de dados",'red'))


        self.controller(connection)





    def mysql_connection(self, host, user, password, database):
        try:
            connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
            )
            return connection
        except mysql.connector.Error as error:
            return False




    def controller(self,connection):
        cursor = connection.cursor()

        menu = '''
        Menu de opções:
        
        A - Sair
        B - Adicionar nova fórmula
        C - Pesquisar Fórmulas
        
        '''

        while True:
            print(menu)

            try:
                opcoes = ['a','b','c']
                Opc = str(input("Opção: "))

                if(Opc.lower() not in opcoes):
                    os.system('cls')
                    print(colored("Escreva uma opção dentro do menu",'red'))
                    continue
                
                if(Opc.lower() == 'a'):
                    sys.exit()
                
                if(Opc.lower() == 'b'):
                    os.system('cls')
                    print('em construção')
                
                if(Opc.lower() == 'c'):
                    os.system('cls')
                    chaves = str(input('Palavras Chaves: ')).split(" ")
                    query = "SELECT * FROM formulas WHERE"

                    cont = 0
                    for k in chaves:
                        if cont == len(chaves)-1:
                            query += f" chaves LIKE '%{k}%';"
                        else:
                            query += f" chaves LIKE '%{k}%' and"

                        cont+=1
                

                    cursor.execute(query)
                    result = cursor.fetchall()
                    self.EstilizarResultado(result)



            except OSError as error:
                os.system('cls')
                print(error)
                print(colored('Escreva uma opção válida','red'))




    def EstilizarResultado(self,result):
        os.system('cls')
        if(len(result) == 0):
            print(colored("Não encontramos resultados com essas palavras chaves",'cyan'))
            return
        for Formula in result:
            print("-"*100)
            print(f"Formula: {Formula[1]}\nDescrição: {Formula[2]}\n"+colored(f"Macete: {Formula[3]}",'green'))
            print("-"*100)
        

        input("\n\nAperte Enter Para acessar o menu")
        os.system('cls')
            




Main()