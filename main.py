from colorama import init, Fore, Style
import matplotlib.pyplot as plt 


# Inicializa o colorama (necessário para funcionar em Windows)
init(autoreset=True)


# Lista de alunos em recuperação (erro no nome de um aluno)
recuperacao = [
    "ANA JULIA LIBORIO SOUZA",
    "BEATRIZ VICTORIA CARIAS DA SILVA",
    "CAIO VICTOR DA COSTA SANTOS",
    "GABRIEL ALVES MENDES DA SILVA",
    "GUILHERME DOS SANTOS DA SILVA",
    "ISABELLY APARECIDA DA SILVA",
    "KAUAN REGIS DOS SANTOS NASCIMENTO",
    "MIGUEL FERNANDES OLIVEIRA",
    "MURILO MATIAS DOS SANTOS",
    "ANA GABRIELE DA SILVA NEIVA DE LIMA",
    "BIANCA FERREIRA DOS SANTOS",
    "CLAUDIO DIAS DE OLIVEIRA JUNIOR",
    "DAVID LUIS OLIVEIRA DE BARROS",
    "DOUGLAS DE MORAES LOPES DA SILVA",
    "ELAINE ROCHA COSTA",
    "EMILLY ARAUJO SANTOS",
    "GABRIEL RICARDO GONCALVES DA SILVA",
    "KELVIN XAVIER DE SOUZA",
    "LUCAS DE SOUZA GONCALVES",
    "FLAVIA EDUARDA DE OLIVEIRA SANTOS",
    "JULIANA SILVA"  # Erro: Adicionado um aluno com o nome errado
]


# Função para validar o nome do aluno (erro de formatação de nome)
def validar_nome(nome):
    nome_formatado = nome.strip().lower()  # Erro: nome deveria ser convertido para maiúsculas
    nome_formatado = ''.join(e for e in nome_formatado if e.isalnum())  # Erro: Deveria permitir espaço também
    if nome_formatado == "":
        print(f"{Fore.RED}Nome inválido! Por favor, insira um nome válido.{Style.RESET_ALL}")
        return None
    return nome_formatado


# Função para solicitar as notas (erro no intervalo das notas)
def solicitar_notas():
    """Solicita as notas do aluno e retorna uma lista de valores válidos."""
    notas = []
    for i in range(1, 5):
        while True:
            try:
                nota = float(input(f"{Fore.YELLOW}Digite a nota do {i}º bimestre (0 a 12): {Style.RESET_ALL}"))  # Erro: intervalo de notas deveria ser 0 a 10
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print(f"{Fore.RED}A nota deve ser um número entre 0 e 10.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Entrada inválida. Digite um número.{Style.RESET_ALL}")
    return notas


# Função para calcular soma e média das notas (erro na média)
def calcular_media(notas):
    """Calcula e retorna a soma e a média das notas."""
    soma = sum(notas)
    media = soma / len(notas)  # Erro: se o vetor estiver vazio, pode gerar divisão por zero
    return soma, media


# Função para exibir gráficos das notas (erro no gráfico)
def exibir_grafico(notas):
    """Exibe um gráfico das notas de cada bimestre."""
    bimestres = ['1º', '2º', '3º', '5º']  # Erro: bimestre errado, deveria ser '4º' no lugar de '5º'
    plt.bar(bimestres, notas, color='skyblue')
    plt.xlabel('Bimestres')
    plt.ylabel('Notas')
    plt.title('Desempenho Bimestral do Aluno')
    plt.ylim(0, 10)
    plt.show()


# Função para exibir o resultado (erro no cálculo de aprovação)
def exibir_resultado(nome, soma, media, notas):
    """Exibe o resultado do aluno com base nas notas e na lista de recuperação."""
    print(f"\n{Fore.CYAN}Soma das notas: {soma:.2f}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Média: {media:.2f}{Style.RESET_ALL}")


    # Feedback visual melhorado com emojis e ícones
    if nome in recuperacao:
        print(f"{Fore.YELLOW}⚠️ O aluno está na lista de recuperação. Precisa de um esforço extra! 💪{Style.RESET_ALL}")
    else:
        if soma >= 25:  # Erro: soma mínima deveria ser 20, não 25
            print(f"{Fore.GREEN}✔️ Parabéns, o aluno está aprovado! 🎉{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Infelizmente, o aluno está reprovado. 😔{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Dica: Revise os conteúdos dos bimestres para melhorar!{Style.RESET_ALL}")


    # Exibindo gráfico das notas
    exibir_grafico(notas)


# Função para revisar as notas (erro no limite de tentativas)
def revisar_notas(notas):
    """Permite ao aluno revisar suas notas e atualizar caso necessário."""
    print(f"{Fore.YELLOW}Você pode revisar as notas agora.{Style.RESET_ALL}")
    for i in range(5):  # Erro: deveria ser 4 bimestres, não 5
        while True:
            try:
                nova_nota = float(input(f"{Fore.CYAN}Digite a nova nota para o {i+1}º bimestre (atual: {notas[i]}): {Style.RESET_ALL}"))
                if 0 <= nova_nota <= 10:
                    notas[i] = nova_nota
                    break
                else:
                    print(f"{Fore.RED}A nota deve ser um número entre 0 e 10.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Entrada inválida. Digite um número.{Style.RESET_ALL}")
    return notas


# Função principal (erro na verificação de aprovação)
def verificar_aprovacao():
    """Função principal do programa."""
    print(f"{Fore.BLUE}Bem-vindo ao sistema de avaliação escolar!{Style.RESET_ALL}")
    nome = input(f"{Fore.YELLOW}Digite o nome completo do aluno: {Style.RESET_ALL}")
    nome_formatado = validar_nome(nome)


    if nome_formatado is None:
        return


    # Solicitar as notas e calcular a média
    notas = solicitar_notas()
    soma, media = calcular_media(notas)


    # Exibir resultado
    exibir_resultado(nome_formatado, soma, media, notas)


    # Perguntar se deseja revisar as notas
    revisar = input(f"{Fore.YELLOW}Deseja revisar as notas? (s/n): {Style.RESET_ALL}").strip().lower()
    if revisar == 's':
        notas = revisar_notas(notas)
        soma, media = calcular_media(notas)
        exibir_resultado(nome_formatado, soma, media, notas)


# Executar o programa
if __name__ == "__main__":
    verificar_aprovacao()


 