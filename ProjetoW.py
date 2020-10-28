from PyQt5 import uic,QtWidgets
import random
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "controle_denuncias"
)

def ocId():
	numero = [0,1,2,3,4,5,6,7,8,9]
	numeros_extraidos = random.sample(numero,4)
	numeros_extraidos = ''.join(map(str, numeros_extraidos))
	print('OCID:',(numeros_extraidos))
	return numeros_extraidos


def funcao_principal():

	if projeto2.checkBox.isChecked() :
		linha1 = ''
		print("Sigilo")
	else:
		linha1 = projeto2.lineEdit.text()
		print("Nome:",linha1)
	
	linha2 = projeto2.lineEdit_2.text()
	print("Rua:",linha2)

	linha3 = projeto2.lineEdit_3.text()
	print("Número:",linha3)

	linha4 = projeto2.lineEdit_4.text()
	print("Bairro:",linha4)

	linha5 = projeto2.lineEdit_5.text()
	print("Cidade:",linha5)

	linha6 = projeto2.lineEdit_6.text()
	print("Estado:",linha6)

	caixaT1 = projeto2.plainTextEdit.toPlainText()
	print("Descrição da Ocorrência: ",caixaT1)
	
	OCID = ocId()
	cursor = banco.cursor()
	comando_SQL = "INSERT INTO denuncia (ocID,nome,rua,numero,bairro,cidade,estado,descriçao) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
	dados = (str(OCID),str(linha1),str(linha2),str(linha3),str(linha4),str(linha5),str(linha6),str(caixaT1))
	cursor.execute(comando_SQL,dados)

	banco.commit()

def chama_segundaTela():
	segundaTela.show()

	cursor = banco.cursor()
	comando_SQL = "SELECT * FROM denuncia"
	cursor.execute(comando_SQL)
	dados_lidos = cursor.fetchall()

	segundaTela.tableWidget.setRowCount(len(dados_lidos))
	segundaTela.tableWidget.setColumnCount(8)

	for i in range(0, len(dados_lidos)):
		for j in range(0,8):
			segundaTela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def chamar_teceiraTela():
	ExOcid.show()

def excluirOcid():
	idocorrencia = ExOcid.lineEdit_7.text()
	print('SUA DENÚNCIA',idocorrencia,'FOI DELETADA !!')
	idocorrencia = str(idocorrencia)
	cursor = banco.cursor()
	comando_sql = "DELETE FROM denuncia WHERE ocID = %s"
	transformar = (idocorrencia, )
	cursor.execute(comando_sql,transformar)
	banco.commit()


app=QtWidgets.QApplication([])
projeto2=uic.loadUi("projeto2.ui")
segundaTela=uic.loadUi("segundaTela.ui")
ExOcid=uic.loadUi("ExOcid.ui")
projeto2.pushButton.clicked.connect(funcao_principal)
projeto2.pushButton_2.clicked.connect(chama_segundaTela)
projeto2.pushButton_3.clicked.connect(chamar_teceiraTela)
ExOcid.pushButton_4.clicked.connect(excluirOcid)
projeto2.show()
app.exec()