from flask import Flask, render_template , request
from util import bd
app = Flask(__name__)
@app.route('/')
def login_form():
  return render_template('login.html')

@app.route('/pass', methods=['GET'])
def process_login():
  user = request.args.get('user').lower()
  senha = request.args.get('senha')

  # Faça o processamento necessário com os valores recebidos
  # Neste exemplo, vamos apenas retornar os valores dentro de uma função
  if (user == 'guilherme' and senha == '0000') or (user == 'arash' and senha == '0014') or (user == 'vinicius' and senha == '1234')or (user == 'arthur' and senha == '4321') \
          or (user == 'glauber' and senha == '007') :
    return render_template('index.html', nome=user.upper())
  else:
    return render_template('login.html')

@app.route('/go')
def process():
  return render_template('index.html', nome="")

  # Faça o processamento necessário com os valores recebidos
  # Neste exemplo, vamos apenas retornar os valores dentro de uma função

  # banco = bd.SQL("root", "art88043101", "test_1")
  # comando = "select * from Automoveis ORDER BY  Modelo;"
  # cs = banco.consultar(comando, [])

  # def login_data(username, password):
  #   banco = bd.SQL("root", "art88043101", "test_1")
  #   comando = f"SELECT id_login FROM login WHERE nome_login = %s AND senha_login = %s"
  #   cs = banco.consultar(comando, [username, password])
  #
  #   if result:
  #     return render_template('teste.html', dados=dados)
  #   else:
  #     return render_template('.html')
  #
  # result = login_data(user, senha)
  # return result

@app.route('/select_a')
def a():
  banco = bd.SQL("root", "art88043101", "test_1")
  comando = "SELECT DISTINCT modelo, ano, marca FROM automoveis WHERE marca = 'Toyota' ORDER BY ano ASC;"
  cs = banco.consultar(comando, [])
  dados = ""
  for (modelo, ano,marca) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>Modelo : {}</p>
                            <p>Ano : {} </p>
                          </td>
                          <td style='padding: 30px'>
                             <img src="\static\{}.jpg" width="300px" height="200px">
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(modelo,modelo ,ano,marca)
  return render_template('accordion.html', dados = dados)

@app.route('/select_a2')
def a2():
  banco = bd.SQL("root", "art88043101", "test_1")
  comando = """
  SELECT contato, sigla
FROM agencia
WHERE nome LIKE 'A%'
ORDER BY sigla ASC;
  """
  cs = banco.consultar(comando, [])
  dados = ""
  for (contato, sigla) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>sigla : {}</p>
                            <p>contato : {} </p>
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(contato, sigla,contato)
  return render_template('accordion.html', dados = dados)

@app.route('/select_a3')
def a3():
  banco = bd.SQL("root", "art88043101", "test_1")
  comando = """
  SELECT nome, salario
FROM pessoa_fisica
WHERE salario > 1000
ORDER BY salario DESC;
  """
  cs = banco.consultar(comando, [])
  dados = ""
  for (nome, salario) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>nome : {}</p>
                            <p>salario : {} </p>
                          </td>
                      </table>
                  </div>
               '''.format(nome, nome,salario)
  return render_template('accordion.html', dados = dados)

@app.route('/select_b')
def b():
  banco = bd.SQL("root", "art88043101", "test_1")
  comando = """SELECT pf.Nome AS Nome_Pessoa, ag.Sigla AS Sigla_Agencia
FROM Pessoa_Fisica pf
JOIN Contrata c ON pf.CPF = c.fk_Pessoa_Fisica_CPF
JOIN Agencia ag ON c.fk_Agencia_CNPJ = ag.CNPJ
ORDER BY pf.Nome;"""
  cs = banco.consultar(comando, [])
  dados = ""
  for (Nome_Pessoa,Sigla_Agencia) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>Nome Pessoa: {}</p>
                            <p>Sigla Agencia : {}</p>
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(Sigla_Agencia,Nome_Pessoa,Sigla_Agencia)
  return render_template('accordion.html', dados = dados)


@app.route('/select1')
def accordion():
  banco = bd.SQL("root", "art88043101", "test_1")
  comando = "select * from Automoveis ORDER BY  Modelo;"
  cs = banco.consultar(comando, [])
  dados = ""
  for (Placa, Marca, Modelo, Ano, Valor_diaria,s_n, Cor, Qtd_Portas,chassi ) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>Placa : {}</p>
                            <p>Modelo : {}</p>
                            <p>Valor diaria: R$ {}0  </p>
                            <p>Cor : {} </p>
                            <p>Quantidade de Portas : {}</p>
                            <p>chassi : {} </p>
                            <p>Ano : {} </p>
                          </td>
                          <td style='padding: 30px'>
                             <img src="\static\{}.jpg" width="300px" height="200px">
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(Modelo,Placa,Marca,Valor_diaria,Cor,Qtd_Portas,chassi,Ano,Marca)
  return render_template('accordion.html', dados = dados)
  #Placa, Marca, Modelo, Ano, Valor_diaria,s_n, Cor, Qtd_Portas,chassi)

@app.route('/select2')
def select2():
  banco = bd.SQL("root", "art88043101", "test_1")
  comando = "select * from Automoveis ORDER BY  Valor_diaria ;"
  cs = banco.consultar(comando, [])
  dados = ""
  for (Placa, Marca, Modelo, Ano, Valor_diaria,s_n, Cor, Qtd_Portas,chassi ) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>Placa : {}</p>
                            <p>Modelo : {}</p>
                            <p>Valor diaria: R$ {}0  </p>
                            <p>Cor : {} </p>
                            <p>Quantidade de Portas : {}</p>
                            <p>chassi : {} </p>
                            <p>Ano : {} </p>
                          </td>
                          <td style='padding: 30px'>
                             <img src="\static\{}.jpg" width="300px" height="200px">
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(Modelo,Placa,Marca,Valor_diaria,Cor,Qtd_Portas,chassi,Ano,Marca)
  return render_template('accordion.html', dados = dados)
  #Placa, Marca, Modelo, Ano, Valor_diaria,s_n, Cor, Qtd_Portas,chassi)
@app.route('/select3')
def select3():
  banco = bd.SQL("root", "art88043101", "test_1")
  comando = "SELECT a.modelo, a.Marca, ag.nome FROM possui p JOIN agencia ag ON ag.CNPJ = p.fk_Agencia_CNPJ JOIN automoveis a ON p.fk_automoveis_chassi = a.chassi ORDER BY a.modelo ASC;"
  cs = banco.consultar(comando, [])
  dados = ""
  for (modelo, Marca, nome ) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>Nome : {}</p>
                            <p>Modelo : {}</p>
                            <p>Marca : {}</p>
                          </td>
                           <td style='padding: 30px'>
                             <img src="\static\{}.jpg" width="300px" height="200px">
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(nome, nome, modelo, Marca , Marca)
  return render_template('accordion.html', dados = dados)
@app.route('/select4')
def select4():
  banco = bd.SQL("root", "art88043101", "test_1")
  comando = "SELECT c.fk_Pessoa_Fisica_CPF AS CPF, s.Agencia_de_seguro, s.valor FROM cliente c JOIN locacao l ON c.Codigo_Cliente = l.fk_Cliente_Codigo_Cliente JOIN seguro s ON l.Codigo_locacao = s.fk_Locacao_Codigo_Locacao ORDER BY s.valor DESC;"
  cs = banco.consultar(comando, [])
  dados = ""
  for (cpf, Agencia_de_seguro, valor ) in cs:
      dados += '''
                  <h3>{}</h3>
                  <div>
                      <table>
                        <tr>
                          <td style='padding: 30px'>
                            <p>CPF : {}</p>
                            <p>Agenciab de seguro : {}</p>
                            <p>valor : R$ {}0</p>
                          </td>
                        </tr>
                      </table>
                  </div>
               '''.format(Agencia_de_seguro, cpf, Agencia_de_seguro, valor )
  return render_template('accordion.html', dados = dados)
@app.route('/select5')
def select5():
 banco = bd.SQL("root", "art88043101", "test_1")
 comando = """SELECT f.nome, a.modelo, ag.Sigla , ag.nome,a.marca
FROM pessoa_fisica f
JOIN contrata c ON c.fk_Pessoa_Fisica_CPF = f.CPF
JOIN agencia ag ON c.fk_Agencia_CNPJ = ag.CNPJ
JOIN possui p ON ag.CNPJ = p.fk_Agencia_CNPJ
JOIN automoveis a ON p.fk_Automoveis_chassi = a.chassi
ORDER BY f.nome ASC;"""
 cs = banco.consultar(comando, [])
 dados = ""
 for (fnome, modelo, Sigla,agnome,marca ) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Nome F : {}</p>
                           <p>Agenci Nome : {}</p>
                           <p>Sigla : {}</p>
                         </td>
                         <td style='padding: 30px'>
                             <img src="\static\{}.jpg" width="300px" height="200px">
                          </td>
                       </tr>
                     </table>
                 </div>
              '''.format(modelo,fnome,agnome , Sigla,marca)
 return render_template('accordion.html', dados = dados)

@app.route('/select6')
def select6():
 banco = bd.SQL("root", "art88043101", "test_1")
 comando = """SELECT ag.nome, l.forma_pagamento, SUM(a.valor_diaria) AS valor_total_diaria 
FROM agencia ag
JOIN possui p ON ag.cnpj = p.fk_agencia_cnpj
JOIN automoveis a ON p.fk_automoveis_chassi = a.chassi
JOIN tem t ON t.fk_Automoveis_chassi = a.chassi
JOIN locacao l ON t.fk_Locacao_Codigo_locacao = l.Codigo_locacao
GROUP BY ag.nome, l.forma_pagamento
ORDER BY ag.nome ASC;"""
 cs = banco.consultar(comando, [])
 dados = ""
 for (agnome, forma_pagamento, valor_total_diaria ) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Nome F : {}</p>
                           <p>Forma Pagamento : {}</p>
                           <p>valor Total Diaria : R${}0</p>
                         </td>
                        
                       </tr>
                     </table>
                 </div>
              '''.format(agnome,agnome, forma_pagamento, valor_total_diaria )
 return render_template('accordion.html', dados = dados)

@app.route('/select7')
def select7():
 banco = bd.SQL("root", "art88043101", "test_1")
 comando = """SELECT ag.nome, f.nome, a.modelo, r.data_retira, l.preco ,a.marca
FROM agencia ag
JOIN retirada r ON ag.cnpj = r.fk_agencia_cnpj
JOIN locacao l ON r.fk_locacao_codigo_locacao = l.codigo_locacao
JOIN cliente c ON l.fk_cliente_codigo_cliente = c.codigo_cliente
JOIN pessoa_fisica f ON c.fk_Pessoa_Fisica_CPF = f.CPF
JOIN tem t ON t.fk_Locacao_Codigo_locacao = l.Codigo_locacao
JOIN automoveis a ON t.fk_Automoveis_chassi = a.chassi
ORDER BY ag.nome ASC;"""
 cs = banco.consultar(comando, [])
 dados = ""
 for (agnome, fnome, modelo, data_retira, preco,marca) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Nome AG : {}</p>
                           <p>Nome F: {}</p>
                           <p>data_retira: {} </p>
                           <p>Preco: R${}0 </p>
                         </td>
                         <td style='padding: 30px'>
                             <img src="\static\{}.jpg" width="300px" height="200px">
                          </td>
                       </tr>
                     </table>
                 </div>
              '''.format( modelo,agnome, fnome, data_retira, preco, marca)
 return render_template('accordion.html', dados = dados)

@app.route('/select81')
def select81():
 banco = bd.SQL("root", "art88043101", "test_1")
 comando = """SELECT ag.nome, COUNT(a.chassi) AS quantidade
 FROM agencia ag
 JOIN possui p ON ag.cnpj = p.fk_agencia_cnpj
 JOIN automoveis a ON p.fk_automoveis_chassi = a.chassi
 WHERE a.status = 1
 GROUP BY ag.nome;"""
 cs = banco.consultar(comando, [])
 dados = ""
 for (agnome, quantidade) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Nome AG : {}</p>
                           <p>Quantidade: {}</p>
                         </td>
                       </tr>
                     </table>
                 </div>
              '''.format(agnome,agnome, quantidade)
 return render_template('accordion.html', dados = dados)

@app.route('/select82')
def select82():
 banco = bd.SQL("root", "art88043101", "test_1")
 comando = """SELECT ag.nome, AVG(pf.salario) AS media_salario
 FROM agencia ag
 JOIN contrata c ON ag.cnpj = c.fk_agencia_cnpj
 JOIN pessoa_fisica pf ON c.fk_pessoa_fisica_cpf = pf.cpf
 GROUP BY ag.nome;"""
 cs = banco.consultar(comando, [])
 dados = ""
 for (agnome, media_salario) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Media Salario : {}</p>
                         </td>
                       </tr>
                     </table>
                 </div>
              '''.format(agnome, media_salario)
 return render_template('accordion.html', dados = dados)


@app.route('/select83')
def select83():
 banco = bd.SQL("root", "art88043101", "test_1")
 comando = """SELECT p.nome, COUNT(l.codigo_locacao) AS quantidade_locacoes, SUM(l.preco) AS total_gasto
 FROM cliente c
 JOIN locacao l ON c.codigo_cliente = l.fk_cliente_codigo_cliente
 JOIN pessoa_fisica p ON c.fk_Pessoa_Fisica_CPF = p.CPF
 GROUP BY p.nome;"""
 cs = banco.consultar(comando, [])
 dados = ""
 for (Pnome, quantidade_locacoes, total_gasto) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Nome  : {}</p>
                           <p>Quantidade Locacoes: {}</p>
                           <p>Total Gasto: R${}0 </p>
                         </td>
                       </tr>
                     </table>
                 </div>
              '''.format(Pnome,Pnome, quantidade_locacoes, total_gasto)
 return render_template('accordion.html', dados = dados)

@app.route('/select91')
def select91():
 banco = bd.SQL("root", "art88043101", "test_1")
 comando = """
 SELECT C.Plano, AVG(PF.Idade) AS media_idade 
 FROM Cliente C LEFT JOIN Pessoa_Fisica PF 
 ON C.fk_Pessoa_Fisica_CPF = PF.CPF GROUP BY C.Plano;
 """
 cs = banco.consultar(comando, [])
 dados = ""
 for (Plano, media_idade) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Plano  : {}</p>
                           <p>media_idade : {}</p>
                         </td>
                       </tr>
                     </table>
                 </div>
              '''.format(Plano, Plano,media_idade)
 return render_template('accordion.html', dados = dados)

@app.route('/select92')
def select92():
 banco = bd.SQL("root", "art88043101", "test_1")
 comando = """
 SELECT A.Marca, COUNT(*) AS quantidade_locacoes 
 FROM Automoveis A INNER JOIN Tem T ON 
 A.chassi = T.fk_Automoveis_chassi GROUP BY A.Marca;
 """
 cs = banco.consultar(comando, [])
 dados = ""
 for (Marca, quantidade_locacoes) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Quantidade Locacoes : {}</p>
                           <p>Marca : {}</p>
                         </td>
                         <td style='padding: 30px'>
                             <img src="\static\{}.jpg" width="300px" height="200px">
                          </td>
                       </tr>
                     </table>
                 </div>
              '''.format(Marca,Marca, quantidade_locacoes,Marca)
 return render_template('accordion.html', dados = dados)

@app.route('/select93')
def select93():
 banco = bd.SQL("root", "art88043101", "test_1")
 comando = """
 SELECT EXTRACT(MONTH FROM E.Data_entrega) AS mes,
  SUM(L.Preco) AS total_vendas FROM Locacao L 
  LEFT JOIN Entrega E ON L.Codigo_locacao = E.fk_Locacao_Codigo_locacao 
  WHERE E.Data_entrega IS NOT NULL GROUP BY
   EXTRACT(MONTH FROM E.Data_entrega) ORDER BY mes ASC;
 """
 cs = banco.consultar(comando, [])
 dados = ""
 for (mes, total_vendas) in cs:
     dados += '''
                 <h3>{}</h3>
                 <div>
                     <table>
                       <tr>
                         <td style='padding: 30px'>
                           <p>Mes  : {}</p>
                           <p>Total Vendas : {}</p>
                         </td>
                       </tr>
                     </table>
                 </div>
              '''.format(mes,mes, total_vendas)
 return render_template('accordion.html', dados = dados)

app.run(debug=True)