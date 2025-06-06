# unopar-desktop-notification-service
Um sistema de notificação para Windows, contendo também um pequeno sistema de coleta de dados com Selenium para mapear as atividades na plataforma UNOPAR.

## coletor-de-dados
Só será necessário rodar esse serviço uma única vez, ele irá abrir seu navegador, logar na plataforma e navegar por ela, realizando assim a coleta de dados. Após a coleta ele vai reprocessar esses dados e originar um arquivo `atividade.json` na raiz do projeto de `coletor-de-dados`.

### Tecnologias
- Python 3.13
- Selenium

### Antes de rodar

Certifique-se de ter [Chrome Driver](https://googlechromelabs.github.io/chrome-for-testing/) intalado e devidamente configurado.

#### Envs
Crie um arquivo `.env` na raiz do projeto e preencha-o com as seguintes chaves:
```.env
URL_UNOPAR=
INST_USERNAME=
INST_PASSWORD=
```

---

## notification-service
Esse serviço notifica o usuário a partir do sistema de notificações do Windows 11. Ele consome o arquivo `atividades.json` gerado pelo serviço de coleta de dados. Esse serviço é dependente dos dados gerados pelo serviço de coleta de dados, rode-o apenas após fazer a coleta.

### Tecnologias
- Python 3.13

## Como rodar
#### Dependencias
Na raiz do projeto execute:
```bash
pip install -r requirements.txt
```

#### Run
Na raiz do projeto execute:
```bash
python main.py
```
