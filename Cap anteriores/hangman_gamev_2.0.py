from random import choice

class Forca():
    def __init__(self,palavra_secreta):
        self.palavra_secreta = palavra_secreta
        self.palavra_descoberta = ['_' for _ in self.palavra_secreta]
        self.letras_erradas = []
        self.tentativas_restantes = 6
    
    def exibir_progresso(self):
        print("\nPalavra secreta🕵️ :")
        print(" ".join(self.palavra_descoberta))
        print(f"🍀 Tentativas restantes: {self.tentativas_restantes}")
        print(f"❌ Letras erradas: {', '.join(self.letras_erradas)}")
    
    def tentar_letra(self,letra_digitada):

        letra_digitada = letra_digitada.lower().strip()

        # Validação de entrada
        if not letra_digitada or not letra_digitada.isalpha() or len(letra_digitada) != 1:
            print("❌ Entrada inválida. Digite apenas UMA letra do alfabeto.")
            return

        if letra_digitada in self.palavra_descoberta or letra_digitada in self.letras_erradas:
            print("⚠️ Você já tentou essa letra. Tente outra.")
            return

        if letra_digitada in self.palavra_secreta:
            for indice, letra in enumerate(self.palavra_secreta):
                if letra == letra_digitada:
                    self.palavra_descoberta[indice] = letra_digitada
            print("✅ Acertou!")
        else:
            self.letras_erradas.append(letra_digitada)
            self.tentativas_restantes -= 1
            print("❌ Errou!")
    
    def venceu(self):
        # Retorna True se não há mais traços ocultando letras
        return '_' not in self.palavra_descoberta

    def jogo_terminou(self):
        # Retorna True se o jogador venceu ou ficou sem tentativas
        return self.venceu() or self.tentativas_restantes == 0
    
class Jogo():
    def Iniciar(self):
        lista_palavras = ["computador", "internet", "programacao", "python", "desenvolvimento",
            "algoritmo", "inteligencia", "dados", "aprendizagemdemaquina", "scikitlearn"]
        palavra = choice(lista_palavras)

        forca = Forca(palavra)

        while not forca.jogo_terminou():
            forca.exibir_progresso()  # Mostra o estado atual do jogo
            letra = input("Digite uma letra: ")  # Pede letra ao jogador
            forca.tentar_letra(letra)  # Aplica tentativa

        print("\n" + "-" * 40)
        if forca.venceu():
            print("🎉 Parabéns! Você acertou a palavra:", forca.palavra_secreta)
        else:
            print("💀 Você perdeu! A palavra era:", forca.palavra_secreta)
        print("-" * 40)

# Programa principal
if __name__ == "__main__":
    jogo = Jogo()
    jogo.Iniciar()