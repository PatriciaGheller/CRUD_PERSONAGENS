#Este script simula funcionalidades de banco de dados para o nosso projeto de CRUD

#O dicionário é nosso respositório principal

personagens = {
    1:{
        "nome": "Harry Potter",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "01/03/1980",
        "imagem" : "https://upload.wikimedia.org/wikipedia/en/5/5e/Harry_Potter_character_poster.jpg"

    },
    2:{
        "nome": "Ron Weasley",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "31/07/1980",
        "imagem" : "https://upload.wikimedia.org/wikipedia/en/d/d7/Ron_Weasley_poster.jpg"

    },
    3:{
        "nome": "Hermione Granger",
        "raca": "Humana",
        "casa": "Grifinória",
        "altura": 1.65,
        "nascimento": "19/09/1979",
        "imagem" : "https://upload.wikimedia.org/wikipedia/en/d/d3/Hermione_Granger_poster.jpg"

    },
    4:{
        "nome": "Draco Malfoy",
        "raca": "Humano",
        "casa": "Sonserina",
        "altura": 1.80,
        "nascimento": "05/06/1980",
        "imagem" : "https://upload.wikimedia.org/wikipedia/en/1/16/Draco_Mal.JPG"

    },

}

#Esta função gera um novo id
def gerar_id():
    id = len(personagens) + 1
    return id

#Cria um novo personagem no dicionário;
def criar_personagem(nome, raca,casa, altura, nascimento, imagem):
    personagens[gerar_id()] = {"nome":nome, "raca":raca, "casa":casa, "altura":altura, "nacimento":nascimento, "imagem":imagem}

    #retorna um dicionário com todos os personagens
def retornar_personagens():
    return personagens

#retorna um único personagem
def retornar_personagem(id:int):
    if id in personagens.keys():
        return personagens[id]
    else:
        return {}
    
#Atualiza os dados de um personagem
def atualizar_personagem(id:int, dados_personagem:dict):
    personagens[id] = dados_personagem

#remove um personagem       
def remover_personagem(id:int):
    del personagens[id]



#Testes das funções
#print(retornar_personagens())

#criar_personagem("André", "Humano", "Grifinória", 1.65, "24/08/1989", "" )

#print(retornar_personagem(5))

#atualizar_personagem(5, {'Nome':'André David', 'raca':'humano', 'casa':'Grifinória', 'altura':1.65, 'nascimento':'24/08/1989', 'imagem':''})

#print(retornar_personagem(5))
#remover_personagem(5)
#print(retornar_personagem(5))
    
    
