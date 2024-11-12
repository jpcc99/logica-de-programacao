# Aula 6 - Lógica de Programação

## Repetição

O que é repetição?

* Fazer a mesma ação várias vezes;
* Uma sequência que se repete ao longo de um tempo;
* Algo que se repete.

### Repetições 

Juntamente com os condicionais, as repetiçõs a base de vários programas. São utilizadas para executar a mesma parte de um progarma várias vezes, a depender de uma condição. Exemplo:

```python
x = 1
print(x)
x = 2
print(x)
x = 3
print(x)
```

Podemos usar laçoes de repetições para reduzir a quantidade de código que usamos. 

```python
x = 1
while x <= 3:
    print(x)
    x += 1
```

### O `while`

A palavra-chave `while` é usada para criar repetições ao avaliar uma condição, enquanto a condição for verdadeira ele irá executar o bloco de código dentro de seu escopo.

```python
while True:
    # Aqui temos um loop infinito


while False:
    # Esse código nunca irá ser executado
```

Mas como funciona?

```python
x = 1
while x <= 3:
    print(x)
    x = x + 1

```

Como vai rodar?
Primeiro temos o x sendo inicializado: `x = 1`.
Depois temos a linha do while `while x <= 3:`.
Aqui o while é como um `if`. 
Ele irá checar se o valor de `x` é menor ou igual a **3**;
que no caso é, porque x foi definido como `x = 1`
chegamos na linha do `print(x)`
Então teremos a saída **1**
E logo em seguida, adicionamos **1** ao valor de `x` logo,
`x = x + 1` (*x agora vale 2* )
E voltamos no começo do loop, de volta ao `while`
Que será menor ou igual a 3 e será impresso na tela 
e então o loop fará as mesmas coisas até que `x` não seja mais `<= 3`

#### O `else` do `while`

Assim como um if, o while tbm tem o else, e é usado da mesma maneira:

```python
num = int(input())

while num % 2 == 0:
    print(f"{num} é par!")
    num += 1
else:
    prinf(f"{num} é ímpar!")
```

### O `for`

Já com o `for` podemos usá-lo quando queremos iterar numa `range`, ou usar um contador. Exemplo:


##### exemplo.py
```python
for i in range(3):
    print(i + 1)
```
##### saída:
```bash
$ python3 exemplo.py
1 2 3
```

#### O `range()`

O range é uma função que retorna uma sequência de números começando por 0 por padrão. Tbm podemos *settar* diferentes valores para sobreescrever o padrão. Exemplos:

```python
# Uso default
for i in range(3):
    print(i)

# O loop agora irá inicializar o i com 1 ao invés de 0
for i in range(1, 3):
    print(i)

# O terceiro é o step, ou seja, quanto vai adicionar no fim de cada loop
for i in range(0, 10, 2):
    print(i)

# Para uma contagem decrescente
for i in range(0, -10, -1):
    print(i)
```
### O `break` e o `continue`

O `break` servirá como um "freio" em nossos laços, geralmente usando junto a uma condição de parada, exemplo:

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

O código ao executar o break no laço irá causar o programa a pular todo o resto do bloco de código e sair do loop quando o i for igual a 5.

Já o `continue` é o mesmo do `break`, mas irá pular direto para a próxima interação, exemplo:

```python
for i in range(4):
    if i == 2:
        continue
    print(i)

# a saída será:
# 0
# 1
# 3
```

Sim, ele irá pular o `2`.
