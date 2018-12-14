import math

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


class Letter:
    letterName = ""
    letterWhites = []
    letterArea = 0
    letterPerimeter = 0
    letterCircularity = 0
    letterCompactness = 0

    # def getAlphabetLetterParams(self):

# ================================================================================================================================================= # Ler imagem

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
    whites = []
    for column in range(imageSize[1]):
        whitePixel = 0
        for row in range(imageSize[0]):
            if image.item(row, column) == 255:
                whitePixel += 1
        whites.append(tuple((column, whitePixel)))
    print(whites)
    return whites


# Guardar posições iniciais e finais onde há letras no eixo do x
def getXPos(whites):
    letterPosX = []
    xMin = 0
    xMax = 0
    for current, next in zip(whites, whites[1:]):
        if current[1] == 0 and next[1] != 0:
            xMin = next[0]

        if current[1] != 0 and next[1] == 0:
            xMax = current[0]

        if xMin != 0 and xMax != 0 and tuple((xMin, xMax)) not in letterPosX:
            letterPosX.append(tuple((xMin, xMax)))
            xMax = 0

    print("Limites das letras eixo X: " + str(letterPosX))
    return letterPosX


# Guardar posições iniciais e finais onde há letras no eixo do y
def getYPos(letterPosX, image, imageSize):
    letterPosY = []
    for xPos in letterPosX:
        yMin = imageSize[0] - 1
        yMax = 0
        for column in range(xPos[0], xPos[1]):
            for row in range(imageSize[0] - 1):
                nextRow = row + 1
                if image.item(row, column) == 0 and image.item(nextRow, column) == 255:
                    if nextRow < yMin:
                        yMin = nextRow

                if image.item(row, column) == 255 and image.item(nextRow, column) == 0:
                    if row > yMax:
                        yMax = row

        if yMin != imageSize[0] - 1 and yMax != 0:
            letterPosY.append(tuple((yMin, yMax)))

    print("Limites das letras eixo Y: " + str(letterPosY))
    return letterPosY


# Histograma de Posição
def drawHist(whites):
    xAxis = []
    yAxis = []
    for i in range(len(whites)):
        xAxis.append(whites[i][0])
        yAxis.append(whites[i][1])
    plt.bar(xAxis, yAxis, color=(0, 0.63, 0.9))
    plt.xlabel("Posição X")
    plt.ylabel("Número Pixeis Brancos")
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
    print("Limites das letras nos 2 eixos: " + str(letterCoords))
    return letterCoords


# Mostra no terminal a posição (x,y) do click do rato
def showMousePos(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("X -> " + str(x) + ", Y -> " + str(y))


# Calcular a área de um contorno
def calcROIArea(imageROI, imageROISize):
    area = 0
    for column in range(imageROISize[1]):
        for row in range(imageROISize[0]):
            if imageROI.item(row, column) == 255:
                area += 1
    print("Área: ", area)
    return area


# Calcular o perímetro de um contorno
def calcROIPerimeter(imageROI, imageROISize):
    perimeter = 0
    for column in range(imageROISize[1]):
        for row in range(imageROISize[0] - 1):
            nextRow = row + 1
            if imageROI.item(row, column) == 0 and imageROI.item(nextRow, column) == 255:
                perimeter += 1
                imageROI.itemset((row, column), 50)

            if imageROI.item(row, column) == 255 and imageROI.item(nextRow, column) == 0:
                perimeter += 1
                imageROI.itemset((nextRow, column), 50)


    for row in range(imageROISize[0]):
        for column in range(imageROISize[1] - 1):
            nextColumn = column + 1
            if imageROI.item(row, column) == 0 and imageROI.item(row, nextColumn) == 255:
                perimeter += 1
                imageROI.itemset((row, column), 50)

            if imageROI.item(row, column) == 255 and imageROI.item(row, nextColumn) == 0:
                perimeter += 1
                imageROI.itemset((row, nextColumn), 50)

    print("Perímetro: ", perimeter)
    return perimeter


# Calcular circularidade de um contorno(4*pi*(area / perimetro^2)
# quanto + próximo de 1, + circular é
def calcROICirc(area, perimeter):
    circularity = 4 * math.pi * (area / perimeter ** 2)
    print("Circularidade: ", circularity)
    return circularity


# Calcular compactividade (perimetro^2 / area)
# quanto menor, + circular é
def calcROICompc(area, perimeter):
    compactness = perimeter ** 2 / area
    print("Compactividade: ", compactness)
    return compactness



# def reconLetter(letter, area, perimeter, circularity, compactness, whites):


# Histograma de Posição
def reDrawHist(whites, reconWhites):
    xAxis1 = []
    xAxis2 = []
    yAxis1 = []
    yAxis2 = []

    print(len(whites))
    space = 0
    for i in range(len(whites)):
        xAxis1.append(whites[i][0] + space)
        xAxis2.append(whites[i][0] + space + 1)
        yAxis1.append(whites[i][1])
        yAxis2.append(reconWhites[i][1])
        space += 2

    plt.bar(xAxis1, yAxis1, color=(0, 0.63, 0.9))
    plt.bar(xAxis2, yAxis2, color=(0, 1, 0))
    plt.xlabel("Pos_X Original = Pos_X no hist - ((número de linhas do hist. até à posição) -1) *2)")
    plt.ylabel("Número Pixeis Brancos")
    plt.title("Histograma De Comparação Entre Píxeis Brancos Por Posição")
    plt.show()


# Início do programa
def main():
    alphabetLetterParams = []
    imageInput = "tst.png"
    imageName = imageInput.partition(".")[0]
    imageExtension = imageInput.partition(".")[2]
    testImage = readImage(imageInput)
    imageSize = testImage.shape
    print(imageSize)


    # Operações morfológicas na imagem de teste
    # Greyscale
    greyImage = getGreyscale(testImage, imageName, imageExtension)


    # Threshold
    thresholdImage = getThreshold(greyImage, imageName, imageExtension)


    # Array base para Histograma de posição [(posX, número pixeis brancos)]
    whites = getPosHistogram(thresholdImage, imageSize)


    # Guardar posições iniciais e finais onde há letras no eixo do x
    letterPosX = getXPos(whites)


    # Guardar posições iniciais e finais onde há letras no eixo do y
    letterPosY = getYPos(letterPosX, thresholdImage, imageSize)


    # Histograma de Posição
    drawHist(whites)


    # Definir os limites das letras no espaço num único array [(xMin, xMax, yMin, yMax)]
    letterCoords = letterPos(letterPosX, letterPosY)


    # Definir a ROI na imagem inicial
    # topLeftX = xMin; topLeftY = yMin; bottomRightX = xMax; bottomRightY = yMax
    i = 0
    for letter in letterCoords:
        topLeftX = letter[0]
        topLeftY = letter[2]
        bottomRightX = letter[1]
        bottomRightY = letter[3]

        cv.rectangle(testImage, (topLeftX, topLeftY), (bottomRightX, bottomRightY), (0, 255, 0), 2)

        imageROI = thresholdImage[topLeftY: bottomRightY, topLeftX: bottomRightX]
        imageROISize = imageROI.shape
        cv.imshow(imageName, testImage)
        cv.imshow("imageROI", imageROI)


        # Identificar a letra com base no seu ROI

        perimeter = calcROIPerimeter(imageROI, imageROISize)

        area = calcROIArea(imageROI, imageROISize)

        circularity = calcROICirc(area, perimeter)

        compactness = calcROICompc(area, perimeter)

        letterWhites = []

        for j in range(letterPosX[i][0], letterPosX[i][1] + 1):
            letterWhites.append(whites[j])

        print(letterWhites)
        print(len(letterWhites))
        # ========== #
        minHistDif = imageSize[0]*imageSize[1]
        print(minHistDif)

        # letterRecogn = reconLetter(letter, area, perimeter, circularity, compactness, whites)
        a = Letter()
        a.letterName = "a"
        # a.letterWhites[0][1]
        a.letterWhites = [(0, 6), (1, 13), (2, 18), (3, 22), (4, 24), (5, 28), (6, 30), (7, 28), (8, 25), (9, 23),
                          (10, 23), (11, 21), (12, 21), (13, 19), (14, 21), (15, 21), (16, 21), (17, 21), (18, 20),
                          (19, 20), (20, 21), (21, 20), (22, 21), (23, 22), (24, 22), (25, 22), (26, 22), (27, 25),
                          (28, 34), (29, 39), (30, 38), (31, 38), (32, 37), (33, 35), (34, 31), (35, 4), (36, 1)]
        a.letterArea = 933.0
        a.letterPerimeter = 199.05382251739502
        a.letterCircularity = 0.2959037464901487
        a.letterCompactness = 42.46776447887095


        b = Letter()
        b.letterName = "b"
        # a.letterWhites[0][1]
        b.letterWhites = [(0, 55), (1, 55), (2, 55), (3, 55), (4, 55), (5, 55), (6, 45), (7, 14), (8, 13), (9, 14), (10, 13),
                          (11, 13), (12, 14), (13, 14), (14, 13), (15, 14), (16, 14), (17, 14), (18, 14), (19, 14), (20, 14),
                          (21, 16), (22, 14), (23, 16), (24, 18), (25, 18), (26, 20), (27, 24), (28, 34), (29, 32), (30, 30),
                          (31, 27), (32, 24), (33, 19), (34, 12)]
        b.letterArea = 1269.0
        b.letterPerimeter = 182.42640626430511
        b.letterCircularity = 0.4791771284108277
        b.letterCompactness = 26.2248965346803

        c = Letter()
        c.letterName = "c"
        # a.letterWhites[0][1]
        c.letterWhites = [(0, 6), (1, 17), (2, 22), (3, 26), (4, 30), (5, 32), (6, 34), (7, 26), (8, 20), (9, 18), (10, 16),
                          (11, 16), (12, 15), (13, 14), (14, 16), (15, 14), (16, 14), (17, 14), (18, 14), (19, 14), (20, 14),
                          (21, 14), (22, 15), (23, 14), (24, 15), (25, 16), (26, 16), (27, 20), (28, 23), (29, 22), (30, 21),
                          (31, 17), (32, 14), (33, 10), (34, 4), (35, 1)]
        c.letterArea = 516.0
        c.letterPerimeter = 199.6812390089035
        c.letterCircularity = 0.1626241501779213
        c.letterCompactness = 77.27247521730784


        d = Letter()
        d.letterName = "d"
        # a.letterWhites[0][1]
        d.letterWhites = [(0, 12), (1, 19), (2, 24), (3, 27), (4, 30), (5, 32), (6, 34), (7, 23), (8, 19), (9, 18), (10, 18),
                          (11, 16), (12, 14), (13, 16), (14, 15), (15, 14), (16, 14), (17, 14), (18, 14), (19, 14), (20, 13),
                          (21, 14), (22, 14), (23, 14), (24, 13), (25, 14), (26, 14), (27, 14), (28, 43), (29, 55), (30, 55),
                          (31, 55), (32, 55), (33, 55), (34, 55)]
        d.letterArea = 1225.5
        d.letterPerimeter = 182.66904664039612
        d.letterCircularity = 0.4615229004197284
        d.letterCompactness = 27.228054345582382

        print(len(a.letterWhites))

        alphabetLetterParams.append(a)
        alphabetLetterParams.append(b)
        alphabetLetterParams.append(c)
        alphabetLetterParams.append(d)
        # para todas as letras default
        # for a in LettersARRAY

        for alphabetLetter in alphabetLetterParams:

            if abs(len(letterWhites) - len(alphabetLetter.letterWhites)) < 5:
                totalHistDif = 0
                lastSmallestIndex = 0

                if len(letterWhites) > len(alphabetLetter.letterWhites):
                    print("hist input larger")

                    for value in range(len(alphabetLetter.letterWhites)):
                        histDif = abs(letterWhites[value][1] - alphabetLetter.letterWhites[value][1])
                        print(histDif)
                        totalHistDif += histDif
                        lastSmallestIndex = value

                    for remain in range(lastSmallestIndex, len(letterWhites)):
                        totalHistDif += letterWhites[remain][1]

                    print(totalHistDif)


                elif len(letterWhites) < len(alphabetLetter.letterWhites):
                    print("hist input smaller")
                    for value in range(len(letterWhites)):
                        histDif = abs(letterWhites[value][1] - alphabetLetter.letterWhites[value][1])
                        totalHistDif += histDif
                        lastSmallestIndex = value

                    for remain in range(lastSmallestIndex, len(alphabetLetter.letterWhites)):
                        totalHistDif += alphabetLetter.letterWhites[remain][1]

                    print(totalHistDif)

                else:
                    print("hist input equal")
                    for value in range(len(letterWhites)):
                        histDif = abs(letterWhites[value][1] - alphabetLetter.letterWhites[value][1])
                        print(histDif)
                        totalHistDif += histDif

                    print(totalHistDif)


                if totalHistDif < 10 and totalHistDif < minHistDif and abs(circularity - alphabetLetter.letterCircularity) < 0.1:
                    minHistDif = totalHistDif
                    mostNearLetter = alphabetLetter

                    print("Letra Reconhecida: ", mostNearLetter.letterName)

                    areaDif = abs(area - alphabetLetter.letterArea)
                    print("Diferenças na área: " + str(areaDif))

                    perimeterDif = abs(perimeter - alphabetLetter.letterPerimeter)
                    print("Diferenças no perímetro: " + str(perimeterDif))

                    areaDif = abs(area - alphabetLetter.letterArea)
                    print("Diferenças na área: " + str(areaDif))

                    circularityDif = abs(circularity - alphabetLetter.letterCircularity)
                    print("Diferenças na circularidade: " + str(circularityDif))

                    compactnessDif = abs(compactness - alphabetLetter.letterCompactness)
                    print("Diferenças na compactness: " + str(compactnessDif))

                    # Desenhar a letra reconhecida no histograma de posição
                    reDrawHist(letterWhites, alphabetLetter.letterWhites)

        i += 1
        cv.waitKey(0)
        cv.destroyWindow("imageROI")
        # cv.destroyWindow("imageContour")

    cv.imshow(imageName, testImage)
    cv.setMouseCallback(imageName, showMousePos)
    cv.waitKey(0)
    cv.destroyAllWindows()
















    """
        # Skeleton
        imageSize = thresholdImage.shape

        skeleton = np.zeros(imageSize, np.uint8)
        eroded = np.zeros(imageSize, np.uint8)
        tmp = np.zeros(imageSize, np.uint8)
        structuringElement = cv.MORPH_RECT
        kernel = cv.getStructuringElement(structuringElement, imageSize[0]*imageSize[1])

        while cv.countNonZero(thresholdImage) != 0:
            cv.erode(thresholdImage, kernel, eroded)
            cv.dilate(eroded, kernel, tmp)
            cv.subtract(thresholdImage, tmp, tmp)
            cv.bitwise_or(skeleton, tmp, skeleton)
            thresholdImage, eroded = eroded, thresholdImage
    """


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
"""
