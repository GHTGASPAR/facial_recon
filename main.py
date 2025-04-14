import cv2
import face_recognition  # Importação necessária
import os
# Configurações
pasta_imagens = "fotos"
extensoes_validas = (".jpg", ".jpeg", ".png")
rostos_conhecidos = 0
rosto_desconhecido = 0

# Listas para armazenar os resultados
embeddings_treinamento = []
rotulos_treinamento = []

# Processar cada arquivo na pasta
for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.lower().endswith(extensoes_validas):
        
        # Carregar a imagem
        caminho_imagem = os.path.join(pasta_imagens, nome_arquivo)
        image = face_recognition.load_image_file(caminho_imagem)
        
        # Extrair embedding facial
        encodings = face_recognition.face_encodings(image)
        
        if len(encodings) > 0:
            # Usar o primeiro rosto encontrado na imagem
            embedding = encodings[0]
            
            # Extrair o nome do arquivo sem extensão como label
            rotulo = os.path.splitext(nome_arquivo)[0]
            
            # Adicionar às listas
            embeddings_treinamento.append(embedding)
            rotulos_treinamento.append(rotulo)
        else:
            print(f"Nenhum rosto detectado em: {nome_arquivo}")
print("Processamento concluído!")
print(f"Total de embeddings gerados: {len(embeddings_treinamento)}")
print(f"Rótulos correspondentes: {rotulos_treinamento}")


# Criar e treinar o modelo K-NNclear


# --- Captura de vídeo e reconhecimento ---
video = cv2.VideoCapture(0)  # Inicia a webcam


while True:
    ret, frame = video.read()
    if not ret:
        break  # Se não conseguir capturar o frame, sai do loop

    # Reduz o tamanho do frame para melhorar desempenho
    frame_pequeno = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Detecta rostos no frame
    rostos = face_recognition.face_locations(frame_pequeno)
   
    if not rostos:
        cv2.imshow('Reconhecimento Facial', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue  # Pula o restante se não houver rostos

    # Converte os rostos para embeddings
    embeddings = face_recognition.face_encodings(frame_pequeno, rostos)

    # Reconhece cada rosto
    for (top, right, bottom, left), embed in zip(rostos, embeddings):
        # Ajusta as coordenadas (já que o frame foi reduzido)
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Faz a previsão
        matches = face_recognition.compare_faces(embeddings_treinamento, embed, tolerance=0.5 )
        if True in matches:
            indice_melhor_match = matches.index(True)
            rotulo = rotulos_treinamento[indice_melhor_match]
            desc = None
        else:
            rotulo = "Desconhecido"
            desc = True 
           


        # Desenha retângulo e texto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, rotulo, (left, top - 10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    #identifica se há dois rostos , se tiver e um for desconhecido bloquear entrada     
    if len(rostos) == 2 :
        if desc == True :
            print("entrada proibida")
        else : print("pode entrar")
    elif len(rostos) == 1 : 
        if desc == True: 
            print("entrada proibida")
        else : print("pode entrar")
         
   
    cv2.imshow('Reconhecimento Facial', frame)  
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()