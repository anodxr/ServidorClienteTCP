# ServidorClienteTCP
Proyecto para fines educativos referente a un servidor y cliente sencillo en python TCP.

**Servidor:** Maneja una conexión a la vez. Al recibir "DESCONEXION", cierra la conexión activa pero sigue aceptando nuevas.

**Cliente:** Envía mensajes hasta que se ingresa "DESCONEXION", luego cierra la conexión.

**Formato:** Los mensajes se convierten a mayúsculas antes de ser respondidos, así mismo en particular para la entrada "hola servidor" se responde "HOLA CLIENTE".

Para ejecutar:
### Ejecución
1. **Iniciar servidor:**
```bash
python servidor.py
```

2. **Iniciar cliente:**
```bash
python cliente.py
```
