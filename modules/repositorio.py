"""Persistência em JSON"""
#Eu vou enlouquecer com esse JSON
#Aqui segue o mais próximo de algo funcional

import json
import os


class RepositorioJSON:
    """Salva e carrega dados em JSON"""

    def __init__(self, caminho_arquivo="dados.json"):
        self.caminho = caminho_arquivo

    def carregar(self):
        """Carrega dados do JSON, se o arquivo existir"""
        if not os.path.exists(self.caminho):
            return None

        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print("[AVISO] Erro ao ler o arquivo JSON (conteúdo inválido).")
            return None

    def salvar(self, dados: dict):
        """Salva os dados no JSON como um dict"""
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
