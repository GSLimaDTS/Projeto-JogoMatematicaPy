from Models.calcular import Calcular
import Models.Tela


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    Models.Tela.nivel_dificuldade()
    dificuldade: int = int(input())

    calc: Calcular = Calcular(dificuldade)

    Models.Tela.informe_resultado_operacao()
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        Models.Tela.mostar_pontos(pontos)
    else:
        pontos -= 1
        Models.Tela.mostar_pontos(pontos)

    Models.Tela.escolha_continuar()
    continuar: int = int(input())

    if continuar:
        jogar(pontos)
    else:
        Models.Tela.mensagem_encerramneto(pontos)


if __name__ == '__main__':
    main()
