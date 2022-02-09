# Adivina el número

En este repositorio vamos a desplegar un contrato inteligente básico, al cual se le asigna un número secreto y las personas van a poder adivinar dicho número pero deben pagar 1 eth para participar del juego.

Seguimos la explicación de canal de youtube de Moralis -> https://youtu.be/yJQJ7pw_9C0

## Prerequisitos

Por favor instale o tenga instalado lo siguiente:

- [nodejs y npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)

## Instalación

1. [Instalar brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), sino lo haz hecho, esta es una forma sencilla de hacerlo.


```bash
pip install eth-brownie
```
Sino funciona podrias hacerlo via pipx
```bash
pip install --user pipx
pipx ensurepath
# restart your terminal
pipx install eth-brownie
```

2. Clone este repo 
```
https://github.com/camohe90/brownie_basic
```

3. [Instala ganache ganache-cli](https://www.npmjs.com/package/ganache-cli)

```bash
npm install -g ganache-cli
```


5. Configura la red con la que vamos a trabajar

En el archvio brownie-confir.yaml configuramos la red en con la cual vamos a trabajar en este caso seria la red ganache-cli, para ello seleccionamos development  

## Interactuando con los contratos





## Recursos

Para empezar con brownie:

* [Canal de youtube de moralis ](https://youtu.be/yJQJ7pw_9C0)
* Puedes revisar los otros [Brownie mixes](https://github.com/brownie-mix/) que pueden ser usado como punto de partida para tus propios contratos. Allí encontraras ejemplos para emepzar como.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) es un buen tutorial para que te familiarices con Brownie.
* Para más información especifica, puedes revisar la [documentación Brownie](https://eth-brownie.readthedocs.io/en/stable/).

## Licencia

This project is licensed under the [MIT license](LICENSE).

