# FaceRecogniton | CETIHP 
## Repositório para controle de versões do sistema de Reconhecimento Facial do Homero Pires (RFHP) 
Este repositório serve para controlar as versões do nosso projeto para a Escola Homero Pires. Momentaneamente privado mas o projeto será OpenSource para contribuições . **Projeto dedicado para a segurança dos alunos na escola!**
# Documentação do Sistema de Reconhecimento Facial

## *1. Objetivo*  
Este sistema realiza reconhecimento facial em tempo real para controle de acesso, identificando rostos pré-cadastrados em um banco de dados e tomando decisões de permissão com base nas detecções.

---

## *2. Pré-requisitos*  
### *2.1 Bibliotecas Necessárias*
bash
pip install opencv-python face-recognition


### *2.2 Estrutura de Arquivos*

├── fotos/               # Pasta com imagens de treinamento (uma por pessoa)
│   ├── pessoa1.jpg      # Nome do arquivo = rótulo do rosto
│   └── pessoa2.png
└── main.py              # Código principal


---

## *3. Funcionamento*  
### *3.1 Treinamento*  
1. Lê imagens da pasta fotos/ (formatos: JPG, JPEG, PNG)
2. Extrai embeddings faciais usando face_recognition
3. Armazena os dados em:
   - embeddings_treinamento: Vetores numéricos dos rostos
   - rotulos_treinamento: Nomes das pessoas (extraídos dos nomes dos arquivos)

### *3.2 Reconhecimento em Tempo Real*  
1. Captura vídeo da webcam
2. Para cada frame:
   - Reduz o tamanho do frame para otimização
   - Detecta rostos usando face_recognition.face_locations()
   - Compara cada rosto com o banco de dados usando compare_faces()
   - Exibe resultados na tela e no console

### *3.3 Regras de Acesso*  
- *1 rosto detectado*:
  - Conhecido → "pode entrar"
  - Desconhecido → "entrada proibida"
- *2 rostos detectados*:
  - Pelo menos 1 conhecido → "pode entrar"
  - Ambos desconhecidos → "entrada proibida"

---

## *4. Saídas Visuais*  
- Retângulo verde ao redor de rostos reconhecidos
- Rótulo com o nome da pessoa abaixo do retângulo
- Mensagens no console indicando o status de acesso

---

## *5. Personalização*  
### *5.1 Ajuste de Sensibilidade*  
Modifique o limiar de similaridade no código:
python
matches = face_recognition.compare_faces(..., tolerance=0.5)  # Valores entre 0.4 e 0.6


### *5.2 Adição de Novos Rostos*  
Basta adicionar novas imagens na pasta fotos/ seguindo o padrão de nomenclatura.

---

## *6. Limitações*  
- Requer imagens de treino com apenas um rosto por arquivo
- Desempenho depende da qualidade das imagens de treino
- Funciona melhor com rostos frontais e boa iluminação

---

## *7. Execução*  
bash
python main.py
  
Pressione Q para encerrar a execução.

---

## *8. Melhorias Sugeridas*  
- Adicionar verificação de rostos mascarados
- Implementar registro de tentativas de acesso
- Usar modelos mais eficientes para embeddings faciais
- Adicionar interface gráfica para cadastro de novos usuários

Este sistema oferece uma base para implementações de controle de acesso por reconhecimento facial, podendo ser adaptado para diferentes cenários de uso.
