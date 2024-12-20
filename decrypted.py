# projetoderansonware
Curso de CiberSecurity
import os
import pyaes

def descriptografar_arquivo(file_name, key):
    try:
        # Verifica se o arquivo existe
        if not os.path.exists(file_name):
            print(f"Erro: O arquivo {file_name} não existe.")
            return

        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Chave para descriptografia
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Criar o arquivo descriptografado
        new_file_name = file_name.replace(".ransomwaretroll", "")
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo {new_file_name} descriptografado com sucesso.")

    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

# Exemplo de uso
file_name = "teste.txt.ransomwaretroll"
key = b"testeransomwares"
descriptografar_arquivo(file_name, key)

#Explicação das Melhorias:
#Uso de with: Garante que os arquivos sejam fechados corretamente.

#Verificação de Existência do Arquivo: Evita erros ao tentar abrir ou remover um arquivo inexistente.

#Tratamento de Exceções: Captura e exibe mensagens de erro, facilitando a identificação de problemas.
