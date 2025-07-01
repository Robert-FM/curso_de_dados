from random import choice

palavras = ["computador", "internet", "programacao", "python", "desenvolvimento",
            "algoritmo", "inteligencia", "dados", "aprendizagemdemaquina", "scikitlearn"]

palavra_secreta = choice(palavras)
letra_descobertas = ["_" for _ in palavra_secreta]
letras_erradas = []
tentativas_restantes = 6

while tentativas_restantes > 0 and "_" in letra_descobertas:
    print("\nPalavra secreta🕵️ :")
    print(" ".join(letra_descobertas))
    print(f"🍀 Tentativas restantes: {tentativas_restantes}")
    print(f"❌ Letras erradas: {', '.join(letras_erradas)}")

    letra_digitada = input("Digite uma letra: ").lower().strip()

    # Validação de entrada
    if not letra_digitada or not letra_digitada.isalpha() or len(letra_digitada) != 1:
        print("❌ Entrada inválida. Digite apenas UMA letra do alfabeto.")
        continue

    if letra_digitada in letra_descobertas or letra_digitada in letras_erradas:
        print("⚠️ Você já tentou essa letra. Tente outra.")
        continue

    if letra_digitada in palavra_secreta:
        for indice, letra in enumerate(palavra_secreta):
            if letra == letra_digitada:
                letra_descobertas[indice] = letra_digitada
        print("✅ Acertou!")
    else:
        letras_erradas.append(letra_digitada)
        tentativas_restantes -= 1
        print("❌ Errou!")

# Resultado final
print("\n" + "-"*40)
if "_" not in letra_descobertas:
    print("🎉 Parabéns! Você acertou a palavra:", palavra_secreta)
else:
    print("💀 Você perdeu! A palavra era:", palavra_secreta)
print("-"*40)
