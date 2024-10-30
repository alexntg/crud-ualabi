# Gestión de Secretos con SOPS

Este proyecto utiliza SOPS para encriptar y desencriptar archivos de configuración sensibles, específicamente `secrets.yaml`. Además, se incluye un `Makefile` para simplificar el proceso.

## Requisitos

- Tener SOPS instalado en tu sistema.
## Archivos

- `secrets.yaml`: Archivo que contiene secretos en texto plano.
- `secrets.enc.yaml`: Archivo encriptado generado por SOPS.
- `Makefile`: Contiene las reglas para encriptar y desencriptar.

## Comandos

### Encriptar el archivo

Para encriptar el archivo `secrets.yaml`, utiliza el siguiente comando:

```bash
make encrypt
```
### Desencriptar el archivo

Para desencriptar el archivo `secrets.yaml`, utiliza el siguiente comando:

```bash
make decrypt
```
