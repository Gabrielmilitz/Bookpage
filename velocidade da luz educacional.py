import time

def veloluz():
    print('''

       * *                     .
   .    *                           *    .
  .    *     *    .
 .   *                                *                            * *    .
   .    *   *                             .
  .    *     *    .
 .   *                         *   *             *    .    
                                         .       *   *    .
  .    *                                                                           *    *                              * 
===========================
CHEGANDO À VELOCIDADE DA LUZ 🚀
===========================
   * *    .
                                   .    *              *    .
  .    *                                  *    .
                                                    .   *                             *                    * *    .
   .                  * *    .
   .    *   *    .
  .    *                                                                   *    .
 .   *       *                          * *    .
   .                                                                                        *   *    .
  .    *                    *    .
 .   *       * *   *    .
  .    *                                                          *    .
 .   *       * 
Esse é um programa para demonstrar os efeitos da velocidade de um
objeto quando ele se aproxima da velocidade da luz. Sabemos que é
impossível, com a tecnologia atual, um objeto viajar em tamanha velocidade.
   * *    .
   .       *                          *    .   * *    .
              .           *   *    .
  .    *                                                                                                                     *    .
      .   *                    *                         
  .    *     *    .
 .   *       * 
angelus dev
Valeu galera!
''')

    try:
        usuario = float(input("Digite a velocidade inicial do objeto a partir de 15000 km/s: "))

        if usuario < 0:
            print("A velocidade não pode ser negativa. Tente novamente.")
            return

        distancia_percorrida = 0  

        for i in range(int(usuario), 300001):
            distancia_percorrida += i 

            
            if i == 270000:
                print("🔘💨💨💨\nA massa do objeto não é mais a mesma.\nO objeto tem um tamanho menor do que em repouso.\nO tempo está ainda mais devagar em relação a um observador parado.")

            elif i == 299700:
                print("🔘💨💨\nAqui o objeto está muito próximo da luz.\nO objeto tem um peso muito maior do que em repouso.\nSeu comprimento é drasticamente menor.\nO tempo dentro do objeto está ficando ainda mais lento 🕖.")

            elif i == 300000:
                print("🔘\n💥\nParabéns! Seu objeto atingiu ou superou a velocidade da luz.\nO tempo está parado agora 🕖.\nO comprimento do objeto na direção do movimento é 0.")

            
            print(f"Velocidade: {i} km/s")
            print(f"Distância percorrida: {distancia_percorrida} km")

         
            if i < 250000:
                time.sleep(0.0001)  # Execução rápida para velocidades abaixo de 250.000 km/s
            elif i < 265000:
                time.sleep(0.001)   # Diminui a velocidade a partir de 250.000 km/s
            else:
                time.sleep(1)     #  espera 1 segundo por iteração

            if i == 300000:
                break

    except ValueError:
        print("Por favor, insira um valor numérico válido.")

veloluz()

usuario = input("Pressione Enter para finalizar...")
