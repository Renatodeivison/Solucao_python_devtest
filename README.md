# Prova para desenvolvedor Python - Questão 7

**Crie uma API que receba uma requisição POST com os campos `username` e `password` e verifique se são credenciais válidas.**

- O `endpoint` deverá receber apenas requisições POST.
- Os campos `username` e `password` deverão ser enviadas no corpo de um formulário.
- Se as credenciais fornecidas forem inválidas a API deverá retornar a mensagem de erro, código 403.
- Se as credenciais fornecidas forem válidas a API deverá retornar a mensagem de confirmação, código 200.
- Não deve ser utilizadas views do Django, a implementação deverá ser realizada utilizando views de API (DRF)
