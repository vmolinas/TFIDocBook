# TFIDocBook
## Crear llave SSH y agregar a cuenta de Github
### 1. Abra Git Bash.
### 2. Pega el siguiente texto, que sustituye tu dirección de correo electrónico en GitHub.
```
ssh-keygen -t ed25519 -C "your_email@example.com"
```
### Cuando se te pida: "Introduce un archivo en el que se pueda guardar la clave", teclea Enter para aceptar la ubicación de archivo predeterminada. Ten en cuenta que si ya creaste claves SSH anteriormente, ssh-keygen puede pedirte que vuelvas a escribir otra clave. En este caso, se recomienda crear una clave SSH con nombre personalizado. Para ello, escribe la ubicación de archivo predeterminada y reemplaza id_ssh_keyname por el nombre de clave personalizado.

```
> Enter a file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):[Press enter]
```
### 3. Cuando se le pida, escriba una frase de contraseña segura. Para obtener más información, vea «Trabajar con contraseñas de clave SSH».
```> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```


## Agregar una clave SSH nueva a tu cuenta de GitHub
### Si tu archivo de llave SSH pública tiene un nombre diferente que en el código de ejemplo, modifica el nombre de archivo para que coincida con tu configuración actual. Al copiar tu clave, no agregues líneas nuevas o espacios en blanco.
```
$ clip < ~/.ssh/id_ed25519.pub
  # Copies the contents of the id_ed25519.pub file to your clipboard
```
### 1. Ve a https://github.com/settings/keys
### 2. Haga clic en "New SSH key".
### 3. Escribe el nombre de la clave SSH en el campo "Title".
### 4. Pega el contenido de la clave SSH en el campo "Key".
### 5. Haga clic en "Add SSH key".

## Probar tu conexión SSH
### 1. Para probar la conexión SSH, ejecuta el siguiente comando en Git Bash.
```
$ ssh -T git@github.com
# Attempts to ssh to GitHub
```
### Puedes ver una advertencia como la siguiente:
```
The authenticity of host 'github.com (192.30.255.112)' can't be established.
ECDSA key fingerprint is SHA256:....
RSA key fingerprint is SHA256:....
Are you sure you want to continue connecting (yes/no)?
```
### 2. Compruebe que la huella digital del mensaje que ve coincide con la huella digital de clave pública de GitHub. En caso afirmativo, escriba yes:.
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```