import os
import shutil

# Tipos de arquivos

diretorio_alvo = input("Digite o caminho do diretório a ser organizado: ")
CATEGORIAS_PADRAO = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xls", ".xlsx"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],
    "Áudios": [".mp3", ".wav", ".aac"],
    "Compactados": [".zip", ".rar", ".tar", ".gz"],
    "Executáveis": [".exe", ".msi", ".bat"]
}
#função que classifica os arquivos presentes
def classificar_arquivo(nome_arquivo, categorias):
    _, extensao = os.path.splitext(nome_arquivo.lower())
    for categoria, extensoes in categorias.items():
        if extensao in extensoes:
            return categoria
    return "Outros"

#Função que organiza os arquivos
def organizar_arquivos(pasta, categorias):
    for item in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, item)

        if os.path.isfile(caminho_completo):
            categoria = classificar_arquivo(item, categorias)
            pasta_destino = os.path.join(pasta, categoria)

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            shutil.move(caminho_completo, os.path.join(pasta_destino, item))
            print(f"Movido: {item} -> {categoria}")

#Menu
if __name__ == "__main__":
    print("Organizador de Arquivos")
    usar_padrao = input("Deseja usar as categorias padrão? (s/n): ").lower()

    if usar_padrao != "s":
        categorias = {}
        while True:
            categoria = input("Digite o nome da categoria (ou 'fim' para encerrar): ")
            if categoria.lower() == "fim":
                break
            extensoes = input(f"Digite as extensões para '{categoria}' separadas por vírgula: ")
            categorias[categoria] = [ext.strip().lower() for ext in extensoes.split(",")]
    else:
        categorias = CATEGORIAS_PADRAO

    organizar_arquivos(diretorio_alvo, categorias)
    print("Organização concluída!")
