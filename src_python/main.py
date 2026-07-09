from equipamento import Equipamento


class SensorTemperatura(Equipamento):
    def __init__(self, tag, descricao, ativo, valor_atual):
        super().__init__(tag, descricao, ativo)
        self._valor_atual = valor_atual

    def atualizar_leitura(self, novo_valor):
        self._valor_atual = novo_valor

    def exibir_resumo(self):
        print(f"[SensorTemperatura] {self.tag} - valorAtual={self._valor_atual}")
