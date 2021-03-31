from Models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nivel de dificuldade desejado:[1, 2, 3, 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado da seguinte operacao: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Voce Tem {pontos} ponto(s)')

    continuar: int = int(input('Deseja continuar jogando? [1 = sim, 0 = nao]: '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Voce finalizou o jogo com {pontos} ponto(s)')
        print('Ate a proxima!')


if __name__ == '__main__':
    main()
