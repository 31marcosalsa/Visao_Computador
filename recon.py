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
    # TODO
    imageInput = "m.png"
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
        topLeftX = letter[0] - 4
        topLeftY = letter[2] - 4
        bottomRightX = letter[1] + 4
        bottomRightY = letter[3] + 4

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
        minHistDif = imageROISize[0] * imageROISize[1]
        print(minHistDif)

        # letterRecogn = reconLetter(letter, area, perimeter, circularity, compactness, whites)
        a_letter = Letter()
        a_letter.letterName = "a"
        # a.letterWhites[0][1]
        a_letter.letterWhites = [(0, 6), (1, 13), (2, 18), (3, 22), (4, 24), (5, 28), (6, 30), (7, 28), (8, 25),
                                 (9, 23),
                                 (10, 23), (11, 21), (12, 21), (13, 19), (14, 21), (15, 21), (16, 21), (17, 21),
                                 (18, 20),
                                 (19, 20), (20, 21), (21, 20), (22, 21), (23, 22), (24, 22), (25, 22), (26, 22),
                                 (27, 25),
                                 (28, 34), (29, 39), (30, 38), (31, 38), (32, 37), (33, 35), (34, 31), (35, 4), (36, 1)]
        a_letter.letterArea = 857
        a_letter.letterPerimeter = 233
        a_letter.letterCircularity = 0.19837130204103615
        a_letter.letterCompactness = 63.34772462077013

        b_letter = Letter()
        b_letter.letterName = "b"
        # a.letterWhites[0][1]
        b_letter.letterWhites = [(0, 55), (1, 55), (2, 55), (3, 55), (4, 55), (5, 55), (6, 45), (7, 14), (8, 13),
                                 (9, 14),
                                 (10, 13),
                                 (11, 13), (12, 14), (13, 14), (14, 13), (15, 14), (16, 14), (17, 14), (18, 14),
                                 (19, 14),
                                 (20, 14),
                                 (21, 16), (22, 14), (23, 16), (24, 18), (25, 18), (26, 20), (27, 24), (28, 34),
                                 (29, 32),
                                 (30, 30),
                                 (31, 27), (32, 24), (33, 19), (34, 12)]
        b_letter.letterArea = 851
        b_letter.letterPerimeter = 144
        b_letter.letterCircularity = 0.5157205532802689
        b_letter.letterCompactness = 24.36662749706228

        c_letter = Letter()
        c_letter.letterName = "c"
        # a.letterWhites[0][1]
        c_letter.letterWhites = [(0, 6), (1, 17), (2, 22), (3, 26), (4, 30), (5, 32), (6, 34), (7, 26), (8, 20),
                                 (9, 18),
                                 (10, 16),
                                 (11, 16), (12, 15), (13, 14), (14, 16), (15, 14), (16, 14), (17, 14), (18, 14),
                                 (19, 14),
                                 (20, 14),
                                 (21, 14), (22, 15), (23, 14), (24, 15), (25, 16), (26, 16), (27, 20), (28, 23),
                                 (29, 22),
                                 (30, 21),
                                 (31, 17), (32, 14), (33, 10), (34, 4), (35, 1)]
        c_letter.letterArea = 604
        c_letter.letterPerimeter = 144
        c_letter.letterCircularity = 0.3660343292376997
        c_letter.letterCompactness = 34.33112582781457

        d_letter = Letter()
        d_letter.letterName = "d"
        # a.letterWhites[0][1]
        d_letter.letterWhites = [(0, 12), (1, 19), (2, 24), (3, 27), (4, 30), (5, 32), (6, 34), (7, 23), (8, 19),
                                 (9, 18),
                                 (10, 18),
                                 (11, 16), (12, 14), (13, 16), (14, 15), (15, 14), (16, 14), (17, 14), (18, 14),
                                 (19, 14),
                                 (20, 13),
                                 (21, 14), (22, 14), (23, 14), (24, 13), (25, 14), (26, 14), (27, 14), (28, 43),
                                 (29, 55),
                                 (30, 55),
                                 (31, 55), (32, 55), (33, 55), (34, 55)]
        d_letter.letterArea = 807
        d_letter.letterPerimeter = 151
        d_letter.letterCircularity = 0.4447638737681615
        d_letter.letterCompactness = 28.254027261462205

        e_letter = Letter()
        e_letter.letterName = "e"
        # a.letterWhites[0][1]
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
        # a.letterWhites[0][1]
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
        # a.letterWhites[0][1]
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

        print(len(a_letter.letterWhites))

        alphabetLetterParams.append(a_letter)
        alphabetLetterParams.append(b_letter)
        alphabetLetterParams.append(c_letter)
        alphabetLetterParams.append(d_letter)
        alphabetLetterParams.append(e_letter)
        alphabetLetterParams.append(f_letter)
        alphabetLetterParams.append(g_letter)
        alphabetLetterParams.append(h_letter)
        alphabetLetterParams.append(i_letter)
        alphabetLetterParams.append(j_letter)
        alphabetLetterParams.append(k_letter)
        alphabetLetterParams.append(l_letter)
        alphabetLetterParams.append(m_letter)

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

                if totalHistDif < 50 and totalHistDif < minHistDif and abs(
                        circularity - alphabetLetter.letterCircularity) < 0.1:
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
