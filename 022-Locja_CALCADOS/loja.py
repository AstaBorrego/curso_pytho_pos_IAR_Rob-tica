import uuid  # Biblioteca para gerar IDs únicos reais
# Autor: Profº Astarote
# Inicío do códgio que limpa o terminal

import os  # Importa a biblioteca que conversa com o sistema operacional
import platform  # Importa a biblioteca para saber qual sistema você está usando

# Definimos uma função para organizar a limpeza do terminal
def limpar_terminal():
    # O comando 'cls' funciona no Windows. O comando 'clear' funciona no Linux/Mac.
    # Esta linha escolhe o comando certo dependendo do sistema detectado.
    comando = 'cls' if platform.system() == 'Windows' else 'clear'
    
    # O comando 'os.system' envia essa instrução para o prompt do sistema.
    os.system(comando)

# Agora, toda vez que você quiser limpar a tela, basta chamar a função abaixo:
limpar_terminal()
print("O terminal foi limpo com sucesso!")
# Fim de código que limpa o terminal
class Pessoa:
    def __init__(self, nome: str, endereco: str, cep: str, rg: str, cpf: str, login: str, senha: str):
        self.id_pess = str(uuid.uuid4())[:8]  # Gera um ID único simplificado para a pessoa
        self.nome = input("Nome : ")                    # Atributo público: nome completo
        self.endereco = input("endereco : ")             # Atributo público: logradouro
        self.cep = input("cep : ")                     # Atributo público: código postal
        self.rg = input("rg  :")                        # Atributo público: registro geral
        self.cpf = input("cpf : ")                        # Atributo público: cadastro de pessoa física
        self.login = input("login : ")                # Atributo para credencial de acesso
        self.__senha = ("senha : ")                  # Atributo privado (__): segurança básica de dados

    def cadastrar_perfil(self):
        # Simula a persistência de dados e criação de conta vinculada
        login_pessoa = Login(self.id_pess, self.login, self.__senha)
        login_pessoa.cria_login()             # Instancia e executa o método da classe Login
        print(f"Perfil de {self.nome} cadastrado com sucesso!")
        return self.id_pess                   # Retorna a chave primária do usuário

    def alterar_perfil(self, novos_dados: dict):
        # Atualiza os atributos do objeto baseados em um dicionário de entrada
        for chave, valor in novos_dados.items():
            setattr(self, chave, valor)       # Função nativa para setar atributos dinamicamente
        print("Dados atualizados.")

    def excluir_perfil(self):
        # Lógica para marcar o perfil como inativo ou remover da memória
        self.id_pess = None                   # Limpa a referência de identificação
        print("Perfil removido do sistema.")

class Funcionario(Pessoa):
    def __init__(self, id_depto: int, pis: str, entrada: str, saida: str, *args, **kwargs):
        super().__init__(*args, **kwargs)     # super() repassa os dados comuns para a classe Pessoa
        self.id_depto = id_depto              # FK: Identificador do departamento
        self.pis = pis                        # Atributo específico: Programa de Integração Social
        self.horario_entrada = entrada        # Registro de jornada: início
        self.horario_saida = saida            # Registro de jornada: fim
        self.dependentes = []                 # Lista para armazenar objetos da classe Dependente

    def adicionar_dependente(self, nome_dep: str):
        novo_dep = Dependente(self.id_pess, nome_dep) # Associa o dependente ao ID do funcionário
        self.dependentes.append(novo_dep)     # Composição: armazena o objeto na lista

class Cliente(Pessoa):
    def __init__(self, resposta_pesquisa: str, *args, **kwargs):
        super().__init__(*args, **kwargs)     # Inicializa os dados herdados de Pessoa
        self.resposta = resposta_pesquisa     # Atributo específico de marketing/pesquisa

class Login:
    def __init__(self, id_pess: str, login: str, senha: str):
        self.id_pess = id_pess                # Vinculação com a tabela Pessoa (Chave Estrangeira)
        self.login = login                    # Nome de usuário
        self.senha = senha                    # Hash ou texto da senha

    def cria_login(self):
        # Simula a inserção na tabela de logins separada, conforme o requisito
        print(f"Login '{self.login}' vinculado ao ID {self.id_pess} criado.")

class Dependente:
    def __init__(self, id_func: str, nome: str):
        self.id_func = id_func                # ID do funcionário responsável
        self.nome = nome                      # Nome do dependente

class Departamento:
    def __init__(self, id_depto: int, descricao: str):
        self.id_depto = id_depto              # Identificador único do setor
        self.descricao = descricao            # Nome do setor (ex: RH, Vendas)

# --- Exemplo de Uso (Teste) ---
if __name__ == "__main__":
    # Criando a Astarote Warrior conforme o exemplo do enunciado
    astarote = Funcionario(
        10, "123.456.78.9", "08:00", "18:00", 
        "Astarote Warrior", "Rua das Flores, 123", "01010-000", 
        "12.345.678-x", "123.456.789-00", "astarote.rh", "senha123"
    )
    astarote.cadastrar_perfil()
    astarote.adicionar_dependente("Pedro Henrique Borrego")