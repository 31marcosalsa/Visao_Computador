import math

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Classe que define uma letra e seus parametros a serem medidos
class Letter:
    letterName = ""
    letterHistPos = []
    letterArea = 0
    letterPerimeter = 0
    letterCircularity = 0
    letterCompactness = 0



# ================================================================================================================================================= # Ler imagem


# Preencher um array com todas as letras do alfabeto e todos os parametros previamente medidos para cada letra
def fillAlphabetLetterParams():
    alphabetLetterParams = []

    a_letter = Letter()
    a_letter.letterName = "a"
    # a.letterWhites[0][1]
    a_letter.letterHistPos = [(0, 6), (1, 13), (2, 18), (3, 22), (4, 24), (5, 28), (6, 30), (7, 28), (8, 25),
                             (9, 23), (10, 23), (11, 21), (12, 21), (13, 19), (14, 21), (15, 21), (16, 21),
                             (17, 21), (18, 20), (19, 20), (20, 21), (21, 20), (22, 21), (23, 22), (24, 22),
                             (25, 22), (26, 22), (27, 25), (28, 34), (29, 39), (30, 38), (31, 38), (32, 37),
                             (33, 35), (34, 31), (35, 4), (36, 1)]
    a_letter.letterArea = 857
    a_letter.letterPerimeter = 223
    a_letter.letterCircularity = 0.21656135487353073
    a_letter.letterCompactness = 58.02683780630105



    b_letter = Letter()
    b_letter.letterName = "b"
    b_letter.letterHistPos = [(0, 55), (1, 55), (2, 55), (3, 55), (4, 55), (5, 55), (6, 45), (7, 14), (8, 13),
                             (9, 14), (10, 13), (11, 13), (12, 14), (13, 14), (14, 13), (15, 14), (16, 14),
                             (17, 14), (18, 14), (19, 14), (20, 14), (21, 16), (22, 14), (23, 16), (24, 18),
                             (25, 18), (26, 20), (27, 24), (28, 34), (29, 32), (30, 30), (31, 27), (32, 24),
                             (33, 19), (34, 12)]
    b_letter.letterArea = 871
    b_letter.letterPerimeter = 225
    b_letter.letterCircularity = 0.2162036307181598
    b_letter.letterCompactness = 58.12284730195178



    c_letter = Letter()
    c_letter.letterName = "c"
    c_letter.letterHistPos = [(0, 6), (1, 17), (2, 22), (3, 26), (4, 30), (5, 32), (6, 34), (7, 26), (8, 20),
                             (9, 18), (10, 16), (11, 16), (12, 15), (13, 14), (14, 16), (15, 14), (16, 14),
                             (17, 14), (18, 14), (19, 14), (20, 14), (21, 14), (22, 15), (23, 14), (24, 15),
                             (25, 16), (26, 16), (27, 20), (28, 23), (29, 22), (30, 21), (31, 17), (32, 14),
                             (33, 10), (34, 4), (35, 1)]
    c_letter.letterArea = 614
    c_letter.letterPerimeter = 169
    c_letter.letterCircularity = 0.2701499092194437
    c_letter.letterCompactness = 46.51628664495114



    d_letter = Letter()
    d_letter.letterName = "d"
    d_letter.letterHistPos = [(0, 12), (1, 19), (2, 24), (3, 27), (4, 30), (5, 32), (6, 34), (7, 23), (8, 19),
                             (9, 18), (10, 18), (11, 16), (12, 14), (13, 16), (14, 15), (15, 14), (16, 14),
                             (17, 14), (18, 14), (19, 14), (20, 13), (21, 14), (22, 14), (23, 14), (24, 13),
                             (25, 14), (26, 14), (27, 14), (28, 43), (29, 55), (30, 55), (31, 55), (32, 55),
                             (33, 55), (34, 55)]
    d_letter.letterArea = 870
    d_letter.letterPerimeter = 182
    d_letter.letterCircularity = 0.33005501855127645
    d_letter.letterCompactness = 38.0735632183908

    # TODO adicionar as restantes letras

    alphabetLetterParams.append(a_letter)
    alphabetLetterParams.append(b_letter)
    alphabetLetterParams.append(c_letter)
    alphabetLetterParams.append(d_letter)
    """
    alphabetLetterParams.append(e_letter)
    alphabetLetterParams.append(f_letter)
    alphabetLetterParams.append(g_letter)
    alphabetLetterParams.append(h_letter)
    alphabetLetterParams.append(i_letter)
    alphabetLetterParams.append(j_letter)
    alphabetLetterParams.append(k_letter)
    alphabetLetterParams.append(l_letter)
    alphabetLetterParams.append(m_letter)
    alphabetLetterParams.append(n_letter)
    alphabetLetterParams.append(o_letter)
    alphabetLetterParams.append(p_letter)
    alphabetLetterParams.append(q_letter)
    alphabetLetterParams.append(r_letter)
    alphabetLetterParams.append(s_letter)
    alphabetLetterParams.append(t_letter)
    alphabetLetterParams.append(u_letter)
    alphabetLetterParams.append(v_letter)
    alphabetLetterParams.append(w_letter)
    alphabetLetterParams.append(x_letter)
    alphabetLetterParams.append(y_letter)
    alphabetLetterParams.append(z_letter)
    """
    return alphabetLetterParams



def readImage(imageInput):
    try:
        testImage = cv.imread(imageInput)
        return testImage
    except:
        blankImage = np.zeros((200, 500, 3), np.uint8)
        cv.putText(blankImage, "Imagem Treino Nao Lida", (53, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                   cv.LINE_AA)
        cv.imshow("Erro", blankImage)
        cv.waitKey(0)
        cv.destroyAllWindows()
        return


# Greyscale
def getGreyscale(image, imageName, imageExtension):
    greyImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imwrite(imageName + "Grey." + imageExtension, greyImage)
    # cv.imshow(imageName + "Grey", greyImage)
    # cv.setMouseCallback(imageName + "Grey", showMousePos)
    # cv.waitKey(0)
    return greyImage


# Threshold
def getThreshold(image, imageName, imageExtension):
    thresholdImage = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2)
    cv.imwrite(imageName + "Threshold." + imageExtension, thresholdImage)
    cv.imshow(imageName + "Threshold", thresholdImage)
    cv.setMouseCallback(imageName + "Threshold", showMousePos)
    cv.waitKey(0)
    return thresholdImage


# Array base para Histograma de posição [(posX, número pixeis brancos)]
def getPosHistogram(image, imageSize):
    baseArrayForPosHistogram = []
    for column in range(imageSize[1]):
        whitePixel = 0
        for row in range(imageSize[0]):
            if image.item(row, column) == 255:
                whitePixel += 1
        baseArrayForPosHistogram.append(tuple((column, whitePixel)))
    # print(baseArrayForPosHistogram)
    return baseArrayForPosHistogram


# Guardar posições iniciais e finais onde há letras no eixo do x
def getXPos(baseArrayForPosHistogram):
    letterPosX = []
    xMin = 0
    xMax = 0
    for current, next in zip(baseArrayForPosHistogram, baseArrayForPosHistogram[1:]):
        if current[1] == 0 and next[1] != 0:
            xMin = next[0]

        if current[1] != 0 and next[1] == 0:
            xMax = current[0]

        if xMin != 0 and xMax != 0 and tuple((xMin, xMax)) not in letterPosX:
            letterPosX.append(tuple((xMin, xMax)))
            xMax = 0

    print("Limites das letras eixo X: ", letterPosX)
    return letterPosX


# Guardar posições iniciais e finais onde há letras no eixo do y
def getYPos(letterPosX, thresholdImage, imageSize):
    letterPosY = []
    for xPos in letterPosX:
        yMin = imageSize[0] - 1
        yMax = 0
        for column in range(xPos[0], xPos[1]):
            for row in range(imageSize[0] - 1):
                nextRow = row + 1
                if thresholdImage.item(row, column) == 0 and thresholdImage.item(nextRow, column) == 255:
                    if nextRow < yMin:
                        yMin = nextRow

                if thresholdImage.item(row, column) == 255 and thresholdImage.item(nextRow, column) == 0:
                    if row > yMax:
                        yMax = row

        if yMin != imageSize[0] - 1 and yMax != 0:
            letterPosY.append(tuple((yMin, yMax)))

    print("Limites das letras eixo Y: ", letterPosY)
    return letterPosY


# Histograma de Posição
def drawHist(baseArrayForPosHistogram):
    xAxis = []
    yAxis = []
    for i in range(len(baseArrayForPosHistogram)):
        xAxis.append(baseArrayForPosHistogram[i][0])
        yAxis.append(baseArrayForPosHistogram[i][1])
    plt.bar(xAxis, yAxis, color=(0, 0.63, 0.9))
    plt.xlabel("Posição X")
    plt.ylabel("Número Pixeis Brancos")
    plt.legend(["letra(s) input"])
    plt.title("Histograma Posição Imagem / Número Píxeis Brancos")
    plt.show()


# Definir os limites das letras no espaço num único array [(xMin, xMax, yMin, yMax)]
def letterPos(letterPosX, letterPosY):
    letterCoords = []
    for i in range(len(letterPosX)):
        xMin = letterPosX[i][0]
        xMax = letterPosX[i][1]
        yMin = letterPosY[i][0]
        yMax = letterPosY[i][1]
        letterCoords.append(tuple((xMin, xMax, yMin, yMax)))
    print("Limites das letras nos 2 eixos: ", letterCoords)
    return letterCoords


# Recortar a ROI de uma dada letra (mediante a letterPosition dada)
# topLeftX = xMin; topLeftY = yMin; bottomRightX = xMax; bottomRightY = yMax
def getLetterROI(letterPosition, testImage, thresholdImage, imageName):

    # Recorta a ROI apenas com 1 pixel preto na borda da imagem (necessario para o algoritmo de calculo do perimetro)
    topLeftX = letterPosition[0] - 1
    topLeftY = letterPosition[2] - 1
    bottomRightX = letterPosition[1] + 1
    bottomRightY = letterPosition[3] + 1

    # Desenha um retangulo verde com a letra que foi identificada na image input
    cv.rectangle(testImage, (topLeftX, topLeftY), (bottomRightX, bottomRightY), (0, 255, 0), 2)

    imageROI = thresholdImage[topLeftY: bottomRightY, topLeftX: bottomRightX]
    imageROISize = imageROI.shape
    cv.imshow(imageName, testImage)
    cv.imshow("imageROI", imageROI)

    return imageROI, imageROISize


# Mostra no terminal a posição (x,y) do click do rato na imagem de input
def showMousePos(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("X -> " + str(x) + ", Y -> " + str(y))


# Calcular a área da ROI/letra identificada
def calcROIArea(imageROI, imageROISize):
    area = 0
    for column in range(imageROISize[1]):
        for row in range(imageROISize[0]):
            if imageROI.item(row, column) == 255:
                area += 1
    print("  Área: ", area)
    return area


# Calcular o perímetro da ROI/letra identificada
def calcROIPerimeter(imageROI, imageROISize):
    borderPixels = []

    # faz uma passagem vertical e conta os pixeis da border
    for column in range(imageROISize[1]):
        for row in range(imageROISize[0] - 1):
            nextRow = row + 1
            if imageROI.item(row, column) == 0 and imageROI.item(nextRow, column) == 255:
                borderPixels.append(tuple((row, column)))

            if imageROI.item(row, column) == 255 and imageROI.item(nextRow, column) == 0:
                borderPixels.append(tuple((nextRow, column)))

    # faz uma passagem horizontal e conta os pixeis da border, tendo em atenção os pixeis já contados
    for row in range(imageROISize[0]):
        for column in range(imageROISize[1] - 1):
            nextColumn = column + 1
            if imageROI.item(row, column) == 0 and imageROI.item(row, nextColumn) == 255 and (row, column) not in borderPixels:
                borderPixels.append(tuple((row, column)))

            if imageROI.item(row, column) == 255 and imageROI.item(row, nextColumn) == 0 and (row, nextColumn) not in borderPixels:
                borderPixels.append(tuple((row, nextColumn)))

    print("  Perímetro: ", len(borderPixels), ",Pixeis da border (row, column): ", borderPixels)
    return len(borderPixels)


# Calcular circularidade da ROI/letra identificada(4*pi*(area / perimetro^2)
# quanto + próximo de 1, + circular é
def calcROICirc(area, perimeter):
    circularity = 4 * math.pi * (area / perimeter ** 2)
    print("  Circularidade: ", circularity)
    return circularity


# Calcular compactividade da ROI/letra identificada (perimetro^2 / area)
# quanto menor, + circular é
def calcROICompc(area, perimeter):
    compactness = perimeter ** 2 / area
    print("  Compactividade: ", compactness)
    return compactness


# Do histograma de posição da imagem original com as várias letras, retorna apenas a porção do histograma de uma letra em específico
def getPositionHistogramOfLetter(letterPosX, baseArrayForPosHistogram, letterOrder):
    letterInputPositionHistogram = []

    for j in range(letterPosX[letterOrder][0], letterPosX[letterOrder][1] + 1):
        letterInputPositionHistogram.append(baseArrayForPosHistogram[j])

    return letterInputPositionHistogram



# Calcula a totalidade de pixeis diferentes entre os dois histogramas
def getTotalPixelDiffBetweenHists(letterInputHistPos, alphabetLetterHistPos):
    totalHistDif = 0
    lastCommonIndex = 0

    # se o histograma da letra a ser avaliada for maior que o histograma da letra default que está a ser usado como comparação
    if len(letterInputHistPos) > len(alphabetLetterHistPos):
        print("    Histogram Input is Larger")

        # percorre primeiro o histograma mais pequeno (histograma da letra default)
        for value in range(len(alphabetLetterHistPos)):
            histDif = abs(letterInputHistPos[value][1] - alphabetLetterHistPos[value][1])
            totalHistDif += histDif
            lastCommonIndex = value

        # percorre depois o resto (histograma da letra a ser avaliada)
        for remain in range(lastCommonIndex + 1, len(letterInputHistPos)):
            totalHistDif += letterInputHistPos[remain][1]

        print("    TotalHistDif: ", totalHistDif)


    # se o histograma da letra a ser avaliada for menor que o histograma da letra default que está a ser usado como comparação
    elif len(letterInputHistPos) < len(alphabetLetterHistPos):
        print("    Histogram Input is Smaller")

        # percorre primeiro o histograma mais pequeno (histograma da letra a ser avaliada)
        for value in range(len(letterInputHistPos)):
            histDif = abs(letterInputHistPos[value][1] - alphabetLetterHistPos[value][1])
            totalHistDif += histDif
            lastCommonIndex = value

        # percorre depois o resto (histograma da letra default)
        for remain in range(lastCommonIndex + 1, len(alphabetLetterHistPos)):
            totalHistDif += alphabetLetterHistPos[remain][1]

        print("    TotalHistDif: ", totalHistDif)

    # se o histograma da letra a ser avaliada tiver o mesmo tamanho que o histograma da letra default que está a ser usado como comparação
    else:
        print("    Histogram Input is Equal")
        for value in range(len(letterInputHistPos)):
            histDif = abs(letterInputHistPos[value][1] - alphabetLetterHistPos[value][1])
            totalHistDif += histDif

        print("    TotalHistDif: ", totalHistDif)

    return totalHistDif



# Histograma de Posição redesenhado com os dois histogramas (da letra a ser avaliada e da letra que foi reconhecida como igual)
def reDrawHist(letterHistPos, alphabetLetterHistPos):
    xAxis1 = []
    xAxis2 = []
    yAxis1 = []
    yAxis2 = []

    # print(len(letterHistPos))
    space = 0
    for i in range(len(letterHistPos)):
        xAxis1.append(letterHistPos[i][0] + space)
        xAxis2.append(letterHistPos[i][0] + space + 1)
        yAxis1.append(letterHistPos[i][1])
        yAxis2.append(alphabetLetterHistPos[i][1])
        space += 2

    plt.bar(xAxis1, yAxis1, color=(0, 0.63, 0.9))
    plt.bar(xAxis2, yAxis2, color=(0, 1, 0))
    plt.xlabel("Pos_X Original = Pos_X no hist - ((número de linhas do hist. até à posição) -1) *2)")
    plt.ylabel("Número Pixeis Brancos")
    plt.legend(["letra input", "letra reconhecida"])
    plt.title("Histograma De Comparação Entre Pixeis Brancos Por Posição")
    plt.show()


# Início do programa
def main():
    # TODO
    alphabetLetterParams = fillAlphabetLetterParams()
    imageInput = "atst.png"
    imageName = imageInput.partition(".")[0]
    imageExtension = imageInput.partition(".")[2]
    testImage = readImage(imageInput)
    imageSize = testImage.shape
    print("Image Input Size: ", imageSize)

    # Operações morfológicas na imagem de input
    # Greyscale
    greyImage = getGreyscale(testImage, imageName, imageExtension)

    # Threshold
    thresholdImage = getThreshold(greyImage, imageName, imageExtension)

    # Array base para Histograma de posição [(posX, número pixeis brancos)]
    baseArrayForPosHistogram = getPosHistogram(thresholdImage, imageSize)

    # Guardar posições iniciais e finais onde há letras no eixo do x
    letterPosX = getXPos(baseArrayForPosHistogram)

    # Guardar posições iniciais e finais onde há letras no eixo do y
    letterPosY = getYPos(letterPosX, thresholdImage, imageSize)

    # Desenha Histograma de Posição
    drawHist(baseArrayForPosHistogram)

    # Definir os limites das letras no espaço num único array [(xMin, xMax, yMin, yMax)]
    letterCoords = letterPos(letterPosX, letterPosY)

    # Para cada letra que vai sendo identificada (para cada um dos elementos do array letterCoords, elementos esses que correspondem a posições das letras na imagem input):
    letterOrder = 0
    for letterPosition in letterCoords:
        print("NOVA LETRA RECONHECIDA:  ")

        # Recortar a ROI da letra identificada
        imageROI, imageROISize = getLetterROI(letterPosition, testImage, thresholdImage, imageName)

        # Calcular perimetro, area, circularidade e compactividade da letra identificada
        perimeter = calcROIPerimeter(imageROI, imageROISize)

        area = calcROIArea(imageROI, imageROISize)

        circularity = calcROICirc(area, perimeter)

        compactness = calcROICompc(area, perimeter)

        # Histograma de posição só da letra a ser identificada [(posX, número pixeis brancos)] e não de todas as letras que se encontram na imagem input
        letterHistPos = getPositionHistogramOfLetter(letterPosX, baseArrayForPosHistogram, letterOrder)


        print("  letterHistPos: ", letterHistPos, "\n  len(letterHistPos): ", len(letterHistPos))


        # Reconhecer a letra identificada com base nos parâmetros medidos e comparando com os parâmetros das letras default
        print("    -> STARTED HISTS EVAL")


        # Antes de comparar o número de pixeis diferentes entre o histograma da letra a ser identificada e de cada uma das letras default, considera-se que a menor diferença de pixeis são todos os pixeis da ROI da letra que está a ser identificada
        minHistDif = imageROISize[0] * imageROISize[1]
        mostNearLetter = "Nada Reconhecido"


        # Neste ciclo, compara-se a letra a ser identificada com todas as letras default (para encontrar aquela cujos parametros mais se aproximam dos da letra a ser identificada)
        for alphabetLetter in alphabetLetterParams:
            print("    lenWhitesInput: ", len(letterHistPos), "  letterTryingToRecon: ", alphabetLetter.letterName, " len", len(alphabetLetter.letterHistPos))


            # se os histogramas tiverem um tamanho próximo, então avalia a diferença que há no número de pixeis ao longo das posições
            if abs(len(letterHistPos) - len(alphabetLetter.letterHistPos)) < 5:
                totalHistDif = getTotalPixelDiffBetweenHists(letterHistPos, alphabetLetter.letterHistPos)

                # após calcular a diferença total, avaliar a letra com parâmetros mais próximos
                print("      -> STARTED LETTER EVAL")

                # Avaliar se a letra default e seus parâmetros se aproximam dos mesmos parâmetros medidos para a letra a ser identificada
                if totalHistDif < 50 and totalHistDif < minHistDif and abs(circularity - alphabetLetter.letterCircularity) < 0.1:
                    minHistDif = totalHistDif
                    mostNearLetter = alphabetLetter


        # Apresentar a letra reconhecida depois de avaliar o histograma da letra a ser identificada com os histogramas de todas as letras default
        # Apresenta-se também a diferença entre a área, perimetro, circularidade e compactividade da letra a ser identificada e da letra que foi reconhecida
        print("Letra Reconhecida: ", mostNearLetter.letterName)

        areaDif = abs(area - mostNearLetter.letterArea)
        print("Diferenças na área: " + str(areaDif))

        perimeterDif = abs(perimeter - mostNearLetter.letterPerimeter)
        print("Diferenças no perímetro: " + str(perimeterDif))

        areaDif = abs(area - mostNearLetter.letterArea)
        print("Diferenças na área: " + str(areaDif))

        circularityDif = abs(circularity - mostNearLetter.letterCircularity)
        print("Diferenças na circularidade: " + str(circularityDif))

        compactnessDif = abs(compactness - mostNearLetter.letterCompactness)
        print("Diferenças na compactness: " + str(compactnessDif))

        # Desenhar os dois histogramas de posição (da letra a ser identificada e da letra que foi reconhecida)
        if mostNearLetter.letterHistPos:
            reDrawHist(letterHistPos, mostNearLetter.letterHistPos)

        letterOrder += 1
        cv.waitKey(0)
        cv.destroyWindow("imageROI")

    cv.imshow(imageName, testImage)
    cv.setMouseCallback(imageName, showMousePos)
    cv.waitKey(0)
    cv.destroyAllWindows()


# Iniciar Programa
if __name__ == "__main__":
    main()
# end if

"""
# Variáveis e função auxiliar
MIN_CONTOUR_AREA = 100
RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30
font = cv.FONT_HERSHEY_SIMPLEX
# Mostra no terminal a posição (x,y) do click do rato
def showMousePos(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("X -> " + str(x) + ", Y -> " + str(y))
# Início do programa
def main():
    imageInput = "im4.png"
    imageName = imageInput.partition(".")[0]
    # Ler ficheiro das classificações
    try:
        npaClassifications = np.loadtxt(imageName + "_classifications.txt", np.float32)
    except:
        blankImage = np.zeros((200, 500, 3), np.uint8)
        cv.putText(blankImage, 'Classificador Dos Contornos', (23, 100), font, 1, (0, 0, 255), 2, cv.LINE_AA)
        cv.putText(blankImage, 'Nao Lido', (185, 150), font, 1, (0, 0, 255), 2, cv.LINE_AA)
        cv.imshow("Erro", blankImage)
        cv.waitKey(0)
        cv.destroyAllWindows()
        return
    # Ler ficheiro das imagens geradas no treino
    try:
        npaFlattenedImages = np.loadtxt(imageName + "_flattened_images.txt", np.float32)
    except:
        blankImage = np.zeros((200, 500, 3), np.uint8)
        cv.putText(blankImage, 'Contornos Gerados ', (93, 100), font, 1, (0, 0, 255), 2, cv.LINE_AA)
        cv.putText(blankImage, 'Nao Lidos', (165, 150), font, 1, (0, 0, 255), 2, cv.LINE_AA)
        cv.imshow("Erro", blankImage)
        cv.waitKey(0)
        cv.destroyAllWindows()
        return
    # Ler imagem teste
    testImage = cv.imread(imageInput)
    # print(npaClassifications) [ 99.  97.  65.  49.  68.  66.  67.  51. 100.  98.]
    # A função kNearest.train recebe um array 1d
    npaClassifications = npaClassifications.reshape((npaClassifications.size, 1))
    # print(npaClassifications)v[[ 99.]
    #                            [ 97.]]
    kNearest = cv.ml.KNearest_create()
    kNearest.train(npaFlattenedImages, cv.ml.ROW_SAMPLE, npaClassifications)
    # Operações morfológicas na imagem de teste
    # Greyscale
    greyImage = cv.cvtColor(testImage, cv.COLOR_BGR2GRAY)
    cv.imwrite(imageName + "_test" + "_greyscale.png", greyImage)
    cv.imshow(imageName + "_greyscale", greyImage)
    # Blur
    blurImage = cv.GaussianBlur(greyImage, (5, 5), 0)
    cv.imwrite(imageName + "_test" + "_blur.png", blurImage)
    # cv.imshow(imageName + "_blur", blurImage)
    # Threshold
    thresholdImage = cv.adaptiveThreshold(blurImage, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2)
    cv.imwrite(imageName + "_test" + "_threshold.png", thresholdImage)
    cv.imshow(imageName + "_threshold", thresholdImage)
    # Dilatation
    dilatedImage = cv.dilate(thresholdImage, (5, 5), iterations=5)
    cv.imwrite(imageName + "_test" + "_dilatation.png", dilatedImage)
    cv.imshow(imageName + "_dilated", dilatedImage)
    # Criar cópia da imagem com threshold e dilatada porque findContours modifica a imagem
    threshDilatedImage = dilatedImage.copy()
    # Encontrar contornos das letras
    contourImage, contourArray, contourHierarchy = cv.findContours(threshDilatedImage, cv.RETR_EXTERNAL,
                                                                   cv.CHAIN_APPROX_SIMPLE)
    cv.imwrite(imageName + "_test" + "_contours.png", contourImage)
    cv.imshow(imageName + "_contours", contourImage)
    # Preencher array com coordenadas dos retângulos que abrangem os contornos das letras
    boundRectArray = []
    for p in range(0, len(contourArray)):
        if cv.contourArea(contourArray[p]) > MIN_CONTOUR_AREA:
            boundRectArray.append(cv.boundingRect(contourArray[p]))
    # Ordenar o boundRectArray com as letras da esquerda para a direita
    for passnum in range(len(boundRectArray) - 1, 0, -1):
        for i in range(passnum):
            if boundRectArray[i][0] > boundRectArray[i + 1][0]:
                tmp = boundRectArray[i]
                boundRectArray[i] = boundRectArray[i + 1]
                boundRectArray[i + 1] = tmp
    # Juntar o bound rectangle dos acentos ao das letras (no caso do u)
    posRemoveRect = []
    for i in range(0, len(boundRectArray) - 1):
        nextBottomRightY = boundRectArray[i + 1][1] + boundRectArray[i + 1][3]
        currentTopLeftY = boundRectArray[i][1]
        if nextBottomRightY > currentTopLeftY and nextBottomRightY - currentTopLeftY < 4:
            nextTopLeftY = boundRectArray[i + 1][1]
            offsetY = currentTopLeftY - nextTopLeftY
            lst = list(boundRectArray[i])
            lst[1] = nextTopLeftY
            lst[3] = lst[3] + offsetY
            boundRectArray[i] = tuple(lst)
            posRemoveRect.append(i + 1)
    # Limpar o array dos retângulos de ruído
    cleanBRA = []
    for i in range(0, len(boundRectArray)):
        if i not in posRemoveRect:
            cleanBRA.append(boundRectArray[i])
    # Preparar o array para leitura topLeft - bottomRight
    # Ordenar as letras por linha
    cleanBRA = sorted(cleanBRA, key=itemgetter(1))
    # Ordenar as letras na mesma linha
    for passnum in range(0, len(cleanBRA)):
        for i in range(passnum):
            currentTopLeftX = cleanBRA[i][0]
            currentTopLeftY = cleanBRA[i][1]
            nextTopLeftX = cleanBRA[i + 1][0]
            nextTopLeftY = cleanBRA[i + 1][1]
            if abs(currentTopLeftY - nextTopLeftY) < 31 and currentTopLeftX > nextTopLeftX:
                tmp = cleanBRA[i]
                cleanBRA[i] = cleanBRA[i + 1]
                cleanBRA[i + 1] = tmp
    # print(cleanBRA)
    # Encontrar posições onde meter espaços e descobrir mudanças de linha
    spacePos = []
    newlinePos = []
    for i in range(0, len(cleanBRA) - 1):
        currentTopLeftX = cleanBRA[i][0]
        currentBottomRightX = cleanBRA[i][0] + cleanBRA[i][2]
        nextTopLeftX = cleanBRA[i + 1][0]
        if nextTopLeftX - currentBottomRightX > 20 and i + 1 not in spacePos:
            spacePos.append(i+1)
        if currentTopLeftX > nextTopLeftX:
            newlinePos.append(i+1)
    print("\nEspaços encontrados nas posições: " + str(spacePos))
    print("\nMudanças de linha encontradas nas posições: " + str(newlinePos))
    # Avaliar cada letra identificada e desenhar retângulo
    phrasePos = 0
    resultString = ""
    for contourRect in cleanBRA:
        topLeftX = contourRect[0]
        topLeftY = contourRect[1]
        rectW = contourRect[2]
        rectH = contourRect[3]
        bottomRightX = topLeftX + rectW
        bottomRightY = topLeftY + rectH
        cv.rectangle(testImage, (topLeftX, topLeftY), (bottomRightX, bottomRightY), (0, 255, 0), 2)
        imageROI = thresholdImage[topLeftY: bottomRightY, topLeftX: bottomRightX]
        imageROIResized = cv.resize(imageROI, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))
        # A função kNearest.findNearest recebe um array
        imageROIResArray = np.float32(imageROIResized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT)))
        retval, npaResults, neigh_resp, dists = kNearest.findNearest(imageROIResArray, k=1)
        resultChar = chr(int(npaResults[0][0]))
        # Inserir espaços se necessário
        if phrasePos in spacePos:
            resultString += " " + resultChar
        elif phrasePos in newlinePos:
            resultString += "\n              " + resultChar
        else:
            resultString += resultChar
        phrasePos += 1
    # Mostrar Resultado Final
    print("\n" + "Texto Lido:   " + resultString + " \n")
    cv.imshow(imageInput, testImage)
    cv.setMouseCallback(imageInput, showMousePos)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return
    
    
    
    
    
        e_letter = Letter()
        e_letter.letterName = "e"
        e_letter.letterWhites = [(0, 10), (1, 18), (2, 23), (3, 26), (4, 29), (5, 32), (6, 34), (7, 29), (8, 26),
                                 (9, 25),
                                 (10, 23),
                                 (11, 23), (12, 22), (13, 21), (14, 22), (15, 21), (16, 21), (17, 21), (18, 21),
                                 (19, 21),
                                 (20, 21),
                                 (21, 21), (22, 21), (23, 21), (24, 21), (25, 22), (26, 22), (27, 23), (28, 25),
                                 (29, 27),
                                 (30, 29),
                                 (31, 27), (32, 25), (33, 21), (34, 18), (35, 14), (36, 8)]
        e_letter.letterArea = 816
        e_letter.letterPerimeter = 175
        e_letter.letterCircularity = 0.3348296627368844
        e_letter.letterCompactness = 37.53063725490196



        f_letter = Letter()
        f_letter.letterName = "f"
        f_letter.letterWhites = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 48), (7, 52), (8, 52), (9, 51),
                                 (10, 53),
                                 (11, 55),
                                 (12, 55), (13, 16), (14, 15), (15, 14), (16, 14), (17, 14), (18, 14), (19, 14),
                                 (20, 14),
                                 (21, 7), (22, 7),
                                 (23, 1)]
        f_letter.letterArea = 530
        f_letter.letterPerimeter = 133
        f_letter.letterCircularity = 0.3765151464531834
        f_letter.letterCompactness = 33.37547169811321



        g_letter = Letter()
        g_letter.letterName = "g"
        g_letter.letterWhites = [(0, 13), (1, 23), (2, 29), (3, 35), (4, 37), (5, 40), (6, 42), (7, 32), (8, 28),
                                 (9, 24),
                                 (10, 23),
                                 (11, 22), (12, 19), (13, 21), (14, 19), (15, 19), (16, 19), (17, 19), (18, 19),
                                 (19, 19),
                                 (20, 19),
                                 (21, 19), (22, 20), (23, 21), (24, 21), (25, 22), (26, 24), (27, 27), (28, 39),
                                 (29, 52),
                                 (30, 51),
                                 (31, 50), (32, 49), (33, 46), (34, 42)]
        g_letter.letterArea = 940
        g_letter.letterPerimeter = 190
        g_letter.letterCircularity = 0.3272129744459175
        g_letter.letterCompactness = 38.40425531914894



        h_letter = Letter()
        h_letter.letterName = "h"
        h_letter.letterWhites = [(0, 55), (1, 55), (2, 55), (3, 55), (4, 55), (5, 55), (6, 55), (7, 9), (8, 7), (9, 6),
                                 (10, 6), (11, 7),
                                 (12, 6), (13, 7), (14, 6), (15, 7), (16, 7), (17, 7), (18, 7), (19, 7), (20, 7),
                                 (21, 8),
                                 (22, 8), (23, 8),
                                 (24, 9), (25, 11), (26, 39), (27, 39), (28, 38), (29, 37), (30, 36), (31, 34),
                                 (32, 30)]
        h_letter.letterArea = 735
        h_letter.letterPerimeter = 119
        h_letter.letterCircularity = 0.6522337689113757
        h_letter.letterCompactness = 19.266666666666666



        i_letter = Letter()
        i_letter.letterName = "i"
        i_letter.letterWhites = [(0, 47), (1, 47), (2, 47), (3, 47), (4, 47), (5, 47), (6, 47)]
        i_letter.letterArea = 329
        i_letter.letterPerimeter = 122
        i_letter.letterCircularity = 0.2777704872429567
        i_letter.letterCompactness = 45.24012158054711



        j_letter = Letter()
        j_letter.letterName = "j"
        j_letter.letterWhites = [(0, 5), (1, 5), (2, 5), (3, 6), (4, 6), (5, 61), (6, 61), (7, 61), (8, 61), (9, 60),
                                 (10, 59), (11, 55)]
        j_letter.letterArea = 381
        j_letter.letterPerimeter = 72
        j_letter.letterCircularity = 0.9235700625136659
        j_letter.letterCompactness = 13.606299212598426



        k_letter = Letter()
        k_letter.letterName = "k"
        k_letter.letterWhites = [(0, 55), (1, 55), (2, 55), (3, 55), (4, 55), (5, 55), (6, 55), (7, 8), (8, 8), (9, 8),
                                 (10, 8), (11, 8), (12, 9), (13, 11), (14, 14), (15, 16), (16, 19), (17, 20), (18, 19),
                                 (19, 20), (20, 20), (21, 20), (22, 20), (23, 20), (24, 19), (25, 18), (26, 16),
                                 (27, 13),
                                 (28, 11), (29, 9), (30, 7), (31, 5), (32, 2), (33, 1)]
        k_letter.letterArea = 718
        k_letter.letterPerimeter = 132
        k_letter.letterCircularity = 0.5178290921206317
        k_letter.letterCompactness = 24.26740947075209



        l_letter = Letter()
        l_letter.letterName = "l"
        l_letter.letterWhites = [(0, 55), (1, 55), (2, 55), (3, 55), (4, 55), (5, 55), (6, 55), (7, 8), (8, 8), (9, 8),
                                 (10, 8), (11, 8), (12, 9), (13, 11), (14, 14), (15, 16), (16, 19), (17, 20), (18, 19),
                                 (19, 20), (20, 20), (21, 20), (22, 20), (23, 20), (24, 19), (25, 18), (26, 16),
                                 (27, 13),
                                 (28, 11), (29, 9), (30, 7), (31, 5), (32, 2), (33, 1)]
        l_letter.letterArea = 718
        l_letter.letterPerimeter = 132
        l_letter.letterCircularity = 0.5178290921206317
        l_letter.letterCompactness = 24.26740947075209



        m_letter = Letter()
        m_letter.letterName = "m"
        m_letter.letterWhites = [(0, 40), (1, 40), (2, 40), (3, 40), (4, 40), (5, 40), (6, 33), (7, 9), (8, 7), (9, 6),
                                 (10, 6), (11, 7), (12, 6), (13, 7), (14, 6), (15, 7), (16, 7), (17, 7), (18, 7),
                                 (19, 7),
                                 (20, 7), (21, 8), (22, 9), (23, 9), (24, 40), (25, 39), (26, 39), (27, 38), (28, 36),
                                 (29, 34), (30, 33), (31, 9), (32, 7), (33, 6), (34, 6), (35, 6), (36, 6), (37, 6),
                                 (38, 6),
                                 (39, 7), (40, 7), (41, 7), (42, 7), (43, 7), (44, 8), (45, 8), (46, 9), (47, 9),
                                 (48, 40),
                                 (49, 40), (50, 39), (51, 38), (52, 37), (53, 36), (54, 33), (55, 1)]
        m_letter.letterArea = 1039
        m_letter.letterPerimeter = 311
        m_letter.letterCircularity = 0.13499094372803405
        m_letter.letterCompactness = 93.09047160731473

        
        n_letter = Letter()
        n_letter.letterName = "n"
        n_letter.letterWhites = [(0, 40), (1, 40), (2, 40), (3, 40), (4, 40), (5, 40), (6, 33), (7, 9), (8, 7), (9, 6),
                                 (10, 6), (11, 7), (12, 6), (13, 7), (14, 6), (15, 7), (16, 7), (17, 7), (18, 7),
                                 (19, 7),
                                 (20, 7), (21, 8), (22, 9), (23, 9), (24, 40), (25, 39), (26, 39), (27, 38), (28, 36),
                                 (29, 34), (30, 33), (31, 9), (32, 7), (33, 6), (34, 6), (35, 6), (36, 6), (37, 6),
                                 (38, 6),
                                 (39, 7), (40, 7), (41, 7), (42, 7), (43, 7), (44, 8), (45, 8), (46, 9), (47, 9),
                                 (48, 40),
                                 (49, 40), (50, 39), (51, 38), (52, 37), (53, 36), (54, 33), (55, 1)]
        n_letter.letterArea = 1039
        n_letter.letterPerimeter = 311
        n_letter.letterCircularity = 0.13499094372803405
        n_letter.letterCompactness = 93.09047160731473
        
        o_letter = Letter()
        o_letter.letterName = "o"
        o_letter.letterWhites = [(0, 14), (1, 20), (2, 24), (3, 28), (4, 30), (5, 32), (6, 34), (7, 24), (8, 18),
                                 (9, 18),
                                 (10, 16),
                                 (11, 16), (12, 14), (13, 14), (14, 16), (15, 14), (16, 14), (17, 14), (18, 14),
                                 (19, 14),
                                 (20, 14),
                                 (21, 14), (22, 16), (23, 14), (24, 14), (25, 16), (26, 16), (27, 18), (28, 18),
                                 (29, 24),
                                 (30, 34),
                                 (31, 32), (32, 30), (33, 28), (34, 24), (35, 20), (36, 14)]
        o_letter.letterArea = 734
        o_letter.letterPerimeter = 192
        o_letter.letterCircularity = 0.2502093107351246
        o_letter.letterCompactness = 50.223433242506815
        
        
        p_letter = Letter()
        p_letter.letterName = "p"
        p_letter.letterWhites = []
        p_letter.letterArea = 734
        p_letter.letterPerimeter = 192
        p_letter.letterCircularity = 0.2502093107351246
        p_letter.letterCompactness = 50.223433242506815
        
        
        q_letter = Letter()
        q_letter.letterName = "q"
        q_letter.letterWhites = []
        q_letter.letterArea = 734
        q_letter.letterPerimeter = 192
        q_letter.letterCircularity = 0.2502093107351246
        q_letter.letterCompactness = 50.223433242506815
        
        
        r_letter = Letter()
        r_letter.letterName = "r"
        r_letter.letterWhites = []
        r_letter.letterArea = 734
        r_letter.letterPerimeter = 192
        r_letter.letterCircularity = 0.2502093107351246
        r_letter.letterCompactness = 50.223433242506815
        
        
        s_letter = Letter()
        s_letter.letterName = "s"
        s_letter.letterWhites = []
        s_letter.letterArea = 734
        s_letter.letterPerimeter = 192
        s_letter.letterCircularity = 0.2502093107351246
        s_letter.letterCompactness = 50.223433242506815
        
        
        t_letter = Letter()
        t_letter.letterName = "t"
        t_letter.letterWhites = []
        t_letter.letterArea = 734
        t_letter.letterPerimeter = 192
        t_letter.letterCircularity = 0.2502093107351246
        t_letter.letterCompactness = 50.223433242506815
        
        
        u_letter = Letter()
        u_letter.letterName = "u"
        u_letter.letterWhites = []
        u_letter.letterArea = 734
        u_letter.letterPerimeter = 192
        u_letter.letterCircularity = 0.2502093107351246
        u_letter.letterCompactness = 50.223433242506815
        
        
        v_letter = Letter()
        v_letter.letterName = "v"
        v_letter.letterWhites = []
        v_letter.letterArea = 734
        v_letter.letterPerimeter = 192
        v_letter.letterCircularity = 0.2502093107351246
        v_letter.letterCompactness = 50.223433242506815
        
        
        w_letter = Letter()
        w_letter.letterName = "w"
        w_letter.letterWhites = []
        w_letter.letterArea = 734
        w_letter.letterPerimeter = 192
        w_letter.letterCircularity = 0.2502093107351246
        w_letter.letterCompactness = 50.223433242506815
        
        
        x_letter = Letter()
        x_letter.letterName = "x"
        x_letter.letterWhites = []
        x_letter.letterArea = 734
        x_letter.letterPerimeter = 192
        x_letter.letterCircularity = 0.2502093107351246
        x_letter.letterCompactness = 50.223433242506815
        
        
        y_letter = Letter()
        y_letter.letterName = "y"
        y_letter.letterWhites = []
        y_letter.letterArea = 734
        y_letter.letterPerimeter = 192
        y_letter.letterCircularity = 0.2502093107351246
        y_letter.letterCompactness = 50.223433242506815
        
        
        z_letter = Letter()
        z_letter.letterName = "z"
        z_letter.letterWhites = []
        z_letter.letterArea = 734
        z_letter.letterPerimeter = 192
        z_letter.letterCircularity = 0.2502093107351246
        z_letter.letterCompactness = 50.223433242506815
        
        
        
"""
