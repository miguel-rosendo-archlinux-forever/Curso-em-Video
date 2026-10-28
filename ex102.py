import math
from typing import Union

def calculate_factorial(num: int, show_calculation: bool = False) -> Union[int, str]:
    """Calcula o fatorial de um número inteiro não-negativo.

    Args:
        num (int): O número para o qual o fatorial será calculado.
        show_calculation (bool, optional): Define o formato de saída. 
            Se True, retorna a representação em string do cálculo. 
            Se False, retorna apenas o valor inteiro do resultado. Padrão é False.

    Returns:
        Union[int, str]: O fatorial calculado (int) ou a string contendo o passo a passo do cálculo (str).

    Raises:
        TypeError: Se o parâmetro `num` não for do tipo inteiro.
        ValueError: Se o parâmetro `num` for um número negativo.
    """
    # 1. Validação de Tipo (Fail-fast)
    if not isinstance(num, int):
        raise TypeError(f"O parâmetro 'num' deve ser do tipo int. Tipo recebido: {type(num).__name__}")
    
    # 2. Validação de Valor de Negócio (Fail-fast)
    if num < 0:
        raise ValueError("O fatorial não está definido para números negativos.")

    # 3. Performance: Delegação do cálculo pesado para a biblioteca padrão implementada em C
    result = math.factorial(num)

    if show_calculation:
        if num == 0:
            return "0! = 1"
        # 4. Performance: Uso de join() com generator expression em vez de concatenação em loop
        steps_str = ' x '.join(str(i) for i in range(num, 0, -1))
        return f"{steps_str} = {result}"
    
    return result

if __name__ == '__main__':
    # Bloco isolado para a camada de I/O (Input/Output)
    try:
        entrada_num = input('Digite um número inteiro: ').strip()
        num = int(entrada_num)  # Pode gerar ValueError se não for número
        
        entrada_show = input('Você quer ver o cálculo? [S/N]: ').strip().upper()
        # Tratamento seguro da string de input para extrair o booleano
        show = True if entrada_show and entrada_show[0] == 'S' else False
        
        print('=' * 30)
        
        # Chamada da regra de negócios
        resultado = calculate_factorial(num, show_calculation=show)
        print(resultado)
        
    except ValueError as e:
        print(f"\n[Erro de Validação] Entrada inválida: {e}")
    except TypeError as e:
        print(f"\n[Erro de Tipo] {e}")
    except Exception as e:
        print(f"\n[Erro Inesperado] Ocorreu um problema na execução: {e}")