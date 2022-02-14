# Guardar un número

En este repositorio vamos a desplegar un contrato inteligente básico, al cual permite escribir/reescribir un numero en la variable number y leer el valor que quedo almacenado.


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
https://github.com/camohe90/brownie_basic_save_number
```

3. Configura las variables de entorno

Configura tus [variables de entorno](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) `WEB3_INFURA_PROJECT_ID`, y `PRIVATE_KEY` . 

Puedes obtener un `WEB3_INFURA_PROJECT_ID` creando una cuenta en [Infura](https://infura.io/). Creas un nuevo proyecto y seleccionas la red de pruebas rinkeby. 

En cuanto a tu `PRIVATE_KEY` las puedes obtener de una wallet como [metamask](https://metamask.io/). 

Tambien vas a necesitar ETH rinkeby de prueba. Puedes obtener ETH usando el siguiente [faucet de rinkeby en el siguiente enlace](https://faucets.chain.link/rinkeby). Si eres nuevo por favor, [mira este video.](https://www.youtube.com/watch?v=P7FX_1PePX0)

Puedes agregar tus variables de entorno en el archivo `.env`:

```
export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
export PRIVATE_KEY=<PRIVATE_KEY>
```

Luego, debes estar seguro que tu archivo `brownie-config.yaml` tenga:

```
dotenv: .env
```

## Interactuando con los contratos

Ahora si estamos listos para ejecutar ejecutar el scriprt deploy_basic_storage

```bash
brownie run deploy_basic_storage.py --network rinkeby
```

Si se ejecuto de forma correcta el comando brownie run deploy_guess_number.py --network rinkebyal  deberian recibir un mensaje como el siguiente

```bash
Running 'scripts\deploy_basic_storage.py::main'...
Transaction sent: 0x30ab8e9d53fbd154029f9a61d632e6bc7fe49924590b9614a25bb9d9ae92efd6
  Gas price: 2.275551272 gwei   Gas limit: 99606   Nonce: 436
  Basic_storage.constructor confirmed   Block: 10144322   Gas used: 90551 (90.91%)
  Basic_storage deployed at: 0x104ea61A2642d0667c607E76eC4faE7F8E5D016B
```

Ahora solo haría falta ejecutar el script save_number, en la linea 6 se debe colocar la dirección del contrato que se desplego anteriormente, por defecto brownie crea un objeto donde agrupa las direcciones de los contratos inteligentes desplegados, y normalmente uno trabaja con la última dirección de contrato.

Pero muchas veces necesitamos trabajar o experimentar con varios contratos ya desplegados por lo cual dejar por defecto la dirección del ultimo desplegado no es recomendable por eso es mejor que en la linea 6 coloques directamente la dirección del contrato.

En la linea 10 el primer parametro que se le pasa a la función save es el número que deseo guardar.

Para ello usamos el siguiente comando

```bash
brownie run save_number.py --network rinkeby
```
Y por ultimo podemos utilzar el script read_number que nos permite consultar cuando el número que se encuentra almacenado en la variable number del contrato inteligente

```bash
brownie run read_number.py --network rinkeby
```

Y el resultado de la ejecución deberia ser similar a este

```bash
Running 'scripts\read_number.py::main'...
2
```

## Recursos

Para empezar con brownie:

* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) es un buen tutorial para que te familiarices con Brownie.
* Para más información especifica, puedes revisar la [documentación Brownie](https://eth-brownie.readthedocs.io/en/stable/).

## Licencia

This project is licensed under the [MIT license](LICENSE).

