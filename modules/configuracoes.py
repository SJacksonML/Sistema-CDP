class Configuracoes:
    def __init__(self, alerta_alto_gasto, meses_comparativo, meta_economia_padrao):
        # foram definidos valores arbitrários para limites, apenas para dar um pontapé inicial no projeto 
        """
        Inicializa as configurações do sistema.
        """
        self.alerta_alto_gasto = alerta_alto_gasto
        self.meses_comparativo = meses_comparativo
        self.meta_economia_padrao = meta_economia_padrao

    def carregar(self):
        """
        Carrega configurações de um parâmetro já estabelecido, como meses de comparativo.
        """
        pass

    def salvar(self):
        """
        Salva configurações de um parâmetro, como meta de economia
        """
        pass
