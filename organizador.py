import pathlib
from tkinter.filedialog import askdirectory

# Seleciona pasta e valida
caminho = askdirectory(title="Selecione uma pasta")
if not caminho:
    exit()

# Categorias ampliadas com tipos comuns
locais = {
    "imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".mpeg"],
    "audios": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "documentos": [".pdf", ".doc", ".docx", ".odt", ".rtf"],
    "planilhas": [".xls", ".xlsx", ".ods", ".csv", ".tsv"],
    "presentacoes": [".ppt", ".pptx", ".odp"],
    "compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "executaveis": [".exe", ".msi", ".bat", ".sh", ".apk"],
    "programacao": [".py", ".js", ".java", ".c", ".cpp", ".html", ".css", ".php", ".json", ".xml"],
    "sistema": [".iso", ".img", ".dmg"],
    "fontes": [".ttf", ".otf", ".woff", ".woff2"],
    "banco_dados": [".sql", ".db", ".sqlite", ".mdb"],
    "projetos": [".aep", ".psd", ".ai", ".xd", ".sketch"],
    "ebooks": [".epub", ".mobi"],
    "torrents": [".torrent"],
    "configs": [".ini", ".cfg", ".conf", ".env"],
    "logs": [".log", ".txt"],
}

# Mapeamento extensão → pasta
mapa_extensoes = {}
for pasta, exts in locais.items():
    for ext in exts:
        mapa_extensoes[ext] = pasta

# Prepara caminhos com pathlib
path = pathlib.Path(caminho)
arquivos = [entry for entry in path.iterdir() if entry.is_file()]

# Processa cada arquivo
for arquivo in arquivos:
    extensao = arquivo.suffix.lower()  # Normaliza extensão
    
    # Usa 'outros' se extensão não estiver mapeada
    pasta_destino = mapa_extensoes.get(extensao, "outros")
    
    # Cria pasta de destino
    destino = path / pasta_destino
    if not destino.exists():
        destino.mkdir()
    
    # Move o arquivo evitando duplicatas
    novo_caminho = destino / arquivo.name
    if not novo_caminho.exists():
        arquivo.rename(novo_caminho)
    else:
        # Adiciona timestamp em caso de conflito
        timestamp = arquivo.stat().st_mtime
        novo_nome = f"{arquivo.stem}_{timestamp}{arquivo.suffix}"
        arquivo.rename(destino / novo_nome)
