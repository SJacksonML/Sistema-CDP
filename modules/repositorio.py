import json
import os

class RepositorioJSON:
    """Repositório simples que salva/carrega dicts em JSON"""
    def __init__(self, caminho_arquivo='dados.json'):
        self.caminho = caminho_arquivo

    def carregar(self):
        if not os.path.exists(self.caminho):
            return {}
        try:
            with open(self.caminho, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print('[AVISO] Arquivo JSON inválido. Carregando vazio.')
            return {}

    def salvar(self, dados: dict):
        with open(self.caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
