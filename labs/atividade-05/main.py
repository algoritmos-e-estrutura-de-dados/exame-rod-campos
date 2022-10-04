def maximizar_troca_de_figurinhas(figurinhasDaMaria, figurinhasDoJoao):
    troca = 0
   
    menor_fig = figurinhasDaMaria if len(figurinhasDaMaria) <= len(figurinhasDoJoao) else figurinhasDoJoao
    maior_fig = figurinhasDaMaria if len(figurinhasDaMaria) >= len(figurinhasDoJoao) else figurinhasDoJoao
   
    for index, n_fig in enumerate(menor_fig):
        if not n_fig in maior_fig:
            for n in range(index, len(maior_fig)):
                if n_fig != maior_fig[n]:
                    aux = maior_fig[n]
                    maior_fig[n] = n_fig
                    menor_fig[index] = aux
                    troca = troca + 1
                    break
    return troca

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhasDaMaria = input().split(' ')
    figurinhasDoJoao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhasDaMaria, figurinhasDoJoao)
