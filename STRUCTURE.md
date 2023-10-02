# Estrutura

<pre>
.
└── R4BANK/
    ├── cadastro/
    │   ├── cadastrar.py
    │   ├── erros.py
    │   ├── password_security.py
    │   ├── requisicoes.py
    │   ├── validacao_cpf.py
    │   └── validacao_email.py
    ├── login/
    │   ├── authentication.py
    │   └── main.py
    ├── testes/
    │   ├── gerador.py
    │   └── teste_cpf.py
    ├── app.py
    ├── database.py
    ├── classes.py
    └── menu.py
</pre>

***menu.py***: A estrutura principal do programa. Executa a área de login/cadastro.

***classes.py***: Efetua as operações de _saque, deposito, transferência, visualização de saldo_.

***database.py***: Onde estão as _funções SQL_

***app.py***: A estrutura base do sistema bancario. Da sentido logico as operações do banco


