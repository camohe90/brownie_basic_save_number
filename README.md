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

Antes de ejecutar los script es fundamental tener en una terminal ganacle-cli, para ellos usaremos el siguiente comando

```bash
ganache-cli
```

Si se ejecuta correctamente nos deberia salir una lista de las cuentas disponibles en esta ambiente local de ganache. A continuación en el archivo .env se debe agregar una de las llaves privadas listadas en la terminal donde se esta ejecutando ganache-cli.

Ahora si estamos listos para ejecutar ejecutar el scrip deploy_guess

```bash
brownie run deploy_guess_number.py
```

Si al ejecutar este comando se despliega el contrato correctamente deberian recibir un mensaje como el siguiente

```bash
BrownieBasicProject is the active project.
Attached to local RPC client listening at '127.0.0.1:8545'...

Running 'scripts/deploy_guess_number.py::main'...
Transaction sent: 0xef4700ad72b3822187c6ee60c5a09c5a3c2b476e819281e5793b105f7ce643e7
  Gas price: 0.0 gwei   Gas limit: 6721975   Nonce: 0
  Guess_number.constructor confirmed   Block: 1   Gas used: 243586 (3.62%)
  Guess_number deployed at: 0x9eD482F454E964021d2CB79D9Aeea38603466d9f
```


## Recursos

Para empezar con brownie:

* [Canal de youtube de moralis ](https://youtu.be/yJQJ7pw_9C0)
* Puedes revisar los otros [Brownie mixes](https://github.com/brownie-mix/) que pueden ser usado como punto de partida para tus propios contratos. Allí encontraras ejemplos para emepzar como.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) es un buen tutorial para que te familiarices con Brownie.
* Para más información especifica, puedes revisar la [documentación Brownie](https://eth-brownie.readthedocs.io/en/stable/).

## Licencia

This project is licensed under the [MIT license](LICENSE).

