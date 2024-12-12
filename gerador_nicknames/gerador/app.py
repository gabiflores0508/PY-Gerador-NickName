from funcoes import (
    gerar_nickname_basico,
    gerar_nickname_por_tema,
    gerar_nickname_personalizado,
    gerar_nickname_com_palavra_especifica,
)


def menu():
    print("=== GERADOR DE NICKNAMES ===")
    print("1. Gerar nickname básico")
    print("2. Gerar nickname por tema")
    print("3. Gerar nickname personalizado")
    print("4. Gerar nickname com palavra específica")
    print("5. Exportar nicknames gerados")
    print("0. Sair")
    print("=============================")


def interface_terminal():
    gerados = []
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nickname = gerar_nickname_basico()
            print("\nNickname gerado:", nickname)
            gerados.append(nickname)
            input("\nPressione Enter para continuar...")

        elif escolha == "2":
            tema = (
                input("Escolha um tema (fantasia, tecnologia, espacial): ")
                .strip()
                .lower()
            )
            nickname = gerar_nickname_por_tema(tema)
            print("\nNickname gerado:", nickname)
            gerados.append(nickname)
            input("\nPressione Enter para continuar...")

        elif escolha == "3":
            tema = (
                input("Escolha um tema (fantasia, tecnologia, espacial): ")
                .strip()
                .lower()
            )
            incluir_simbolos = input("Incluir símbolos? (s/n): ").strip().lower() == "s"
            numero_customizado = input("Número customizado (ou deixe vazio): ").strip()
            numero_customizado = (
                int(numero_customizado) if numero_customizado.isdigit() else None
            )
            inicial = input("Letra inicial personalizada (ou deixe vazio): ").strip()

            nickname = gerar_nickname_personalizado(
                tema, incluir_simbolos, numero_customizado, inicial
            )
            print("\nNickname gerado:", nickname)
            gerados.append(nickname)
            input("\nPressione Enter para continuar...")

        elif escolha == "4":
            palavra = input("Digite a palavra que deseja usar: ").strip()
            incluir_simbolos = input("Incluir símbolos? (s/n): ").strip().lower() == "s"
            numero_customizado = input("Número customizado (ou deixe vazio): ").strip()
            numero_customizado = (
                int(numero_customizado) if numero_customizado.isdigit() else None
            )

            nickname = gerar_nickname_com_palavra_especifica(
                palavra, incluir_simbolos, numero_customizado
            )
            print("\nNickname gerado:", nickname)
            gerados.append(nickname)
            input("\nPressione Enter para continuar...")

        elif escolha == "5":
            if gerados:
                with open("nicknames_gerados.txt", "w") as arquivo:
                    arquivo.write("\n".join(gerados))
                print("Nicknames exportados para 'nicknames_gerados.txt'.")
            else:
                print("Nenhum nickname foi gerado ainda.")
            input("\nPressione Enter para continuar...")

        elif escolha == "0":
            print("Saindo... Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    interface_terminal()
