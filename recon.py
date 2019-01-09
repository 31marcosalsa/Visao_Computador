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
    a_letter.letterHistPos = [(0, 6), (1, 13), (2, 18), (3, 22), (4, 24), (5, 28), (6, 30), (7, 28), (8, 25), (9, 23),
                              (10, 23), (11, 21), (12, 21), (13, 19), (14, 21), (15, 21), (16, 21), (17, 21), (18, 20),
                              (19, 20), (20, 21), (21, 20), (22, 21), (23, 22), (24, 22), (25, 22), (26, 22), (27, 25),
                              (28, 34), (29, 39), (30, 38), (31, 38), (32, 37), (33, 35), (34, 31), (35, 4), (36, 1)]
    a_letter.letterArea = 857
    a_letter.letterPerimeter = 223
    a_letter.letterCircularity = 0.21656135487353073
    a_letter.letterCompactness = 58.02683780630105
    alphabetLetterParams.append(a_letter)

    b_letter = Letter()
    b_letter.letterName = "b"
    b_letter.letterHistPos = [(0, 55), (1, 55), (2, 55), (3, 55), (4, 55), (5, 55), (6, 45), (7, 14), (8, 13), (9, 14),
                              (10, 13), (11, 13), (12, 14), (13, 14), (14, 13), (15, 14), (16, 14), (17, 14), (18, 14),
                              (19, 14), (20, 14), (21, 16), (22, 14), (23, 16), (24, 18), (25, 18), (26, 20), (27, 24),
                              (28, 34), (29, 32), (30, 30), (31, 27), (32, 24), (33, 19), (34, 12)]
    b_letter.letterArea = 871
    b_letter.letterPerimeter = 225
    b_letter.letterCircularity = 0.2162036307181598
    b_letter.letterCompactness = 58.12284730195178
    alphabetLetterParams.append(b_letter)

    c_letter = Letter()
    c_letter.letterName = "c"
    c_letter.letterHistPos = [(0, 6), (1, 17), (2, 22), (3, 26), (4, 30), (5, 32), (6, 34), (7, 26), (8, 20), (9, 18),
                              (10, 16), (11, 16), (12, 15), (13, 14), (14, 16), (15, 14), (16, 14), (17, 14), (18, 14),
                              (19, 14), (20, 14), (21, 14), (22, 15), (23, 14), (24, 15), (25, 16), (26, 16), (27, 20),
                              (28, 23), (29, 22), (30, 21), (31, 17), (32, 14), (33, 10), (34, 4), (35, 1)]
    c_letter.letterArea = 614
    c_letter.letterPerimeter = 169
    c_letter.letterCircularity = 0.2701499092194437
    c_letter.letterCompactness = 46.51628664495114
    alphabetLetterParams.append(c_letter)

    d_letter = Letter()
    d_letter.letterName = "d"
    d_letter.letterHistPos = [(0, 12), (1, 19), (2, 24), (3, 27), (4, 30), (5, 32), (6, 34), (7, 23), (8, 19), (9, 18),
                              (10, 18), (11, 16), (12, 14), (13, 16), (14, 15), (15, 14), (16, 14), (17, 14), (18, 14),
                              (19, 14), (20, 13), (21, 14), (22, 14), (23, 14), (24, 13), (25, 14), (26, 14), (27, 14),
                              (28, 43), (29, 55), (30, 55), (31, 55), (32, 55), (33, 55), (34, 55)]
    d_letter.letterArea = 870
    d_letter.letterPerimeter = 182
    d_letter.letterCircularity = 0.33005501855127645
    d_letter.letterCompactness = 38.0735632183908
    alphabetLetterParams.append(d_letter)

    e_letter = Letter()
    e_letter.letterName = "e"
    e_letter.letterHistPos = [(0, 10), (1, 18), (2, 23), (3, 26), (4, 29), (5, 32), (6, 34), (7, 29), (8, 26), (9, 25),
                              (10, 23), (11, 23), (12, 22), (13, 21), (14, 22), (15, 21), (16, 21), (17, 21), (18, 21),
                              (19, 21), (20, 21), (21, 21), (22, 21), (23, 21), (24, 21), (25, 22), (26, 22), (27, 23),
                              (28, 25), (29, 27), (30, 29), (31, 27), (32, 25), (33, 21), (34, 18), (35, 14), (36, 8)]
    e_letter.letterArea = 834
    e_letter.letterPerimeter = 208
    e_letter.letterCircularity = 0.2422418891543905
    e_letter.letterCompactness = 51.875299760191844
    alphabetLetterParams.append(e_letter)

    f_letter = Letter()
    f_letter.letterName = "f"
    f_letter.letterHistPos = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 48), (7, 52), (8, 52), (9, 51),
                              (10, 53), (11, 55), (12, 55), (13, 16), (14, 15), (15, 14), (16, 14), (17, 14), (18, 14),
                              (19, 14), (20, 14), (21, 7), (22, 7), (23, 1)]
    f_letter.letterArea = 538
    f_letter.letterPerimeter = 160
    f_letter.letterCircularity = 0.264090132442392
    f_letter.letterCompactness = 47.58364312267658
    alphabetLetterParams.append(f_letter)

    g_letter = Letter()
    g_letter.letterName = "g"
    g_letter.letterHistPos = [(0, 13), (1, 23), (2, 29), (3, 35), (4, 37), (5, 40), (6, 42), (7, 32), (8, 28), (9, 24),
                              (10, 23), (11, 22), (12, 19), (13, 21), (14, 19), (15, 19), (16, 19), (17, 19), (18, 19),
                              (19, 19), (20, 19), (21, 19), (22, 20), (23, 21), (24, 21), (25, 22), (26, 24), (27, 27),
                              (28, 39), (29, 52), (30, 51), (31, 50), (32, 49), (33, 46), (34, 42)]
    g_letter.letterArea = 1004
    g_letter.letterPerimeter = 219
    g_letter.letterCircularity = 0.2630603218618588
    g_letter.letterCompactness = 47.7699203187251
    alphabetLetterParams.append(g_letter)

    h_letter = Letter()
    h_letter.letterName = "h"
    h_letter.letterHistPos = [(0, 55), (1, 55), (2, 55), (3, 55), (4, 55), (5, 55), (6, 55), (7, 9), (8, 7), (9, 6),
                              (10, 6), (11, 7), (12, 6), (13, 7), (14, 6), (15, 7), (16, 7), (17, 7), (18, 7), (19, 7),
                              (20, 7), (21, 8), (22, 8), (23, 8), (24, 9), (25, 11), (26, 39), (27, 39), (28, 38),
                              (29, 37), (30, 36), (31, 34), (32, 30)]
    h_letter.letterArea = 778
    h_letter.letterPerimeter = 187
    h_letter.letterCircularity = 0.27958009488322333
    h_letter.letterCompactness = 44.947300771208226
    alphabetLetterParams.append(h_letter)

    i_letter = Letter()
    i_letter.letterName = "i"
    i_letter.letterHistPos = [(0, 47), (1, 47), (2, 47), (3, 47), (4, 47), (5, 47), (6, 47)]
    i_letter.letterArea = 329
    i_letter.letterPerimeter = 68
    i_letter.letterCircularity = 0.8941037915493442
    i_letter.letterCompactness = 14.054711246200608
    alphabetLetterParams.append(i_letter)

    j_letter = Letter()
    j_letter.letterName = "j"
    j_letter.letterHistPos = [(0, 5), (1, 5), (2, 5), (3, 6), (4, 6), (5, 61), (6, 61), (7, 61), (8, 61), (9, 60),
                              (10, 59), (11, 55)]
    j_letter.letterArea = 445
    j_letter.letterPerimeter = 91
    j_letter.letterCircularity = 0.9235700625136659
    j_letter.letterCompactness = 13.606299212598426
    alphabetLetterParams.append(j_letter)

    k_letter = Letter()
    k_letter.letterName = "k"
    k_letter.letterHistPos = [(0, 55), (1, 55), (2, 55), (3, 55), (4, 55), (5, 55), (6, 55), (7, 8), (8, 8), (9, 8),
                              (10, 8), (11, 8), (12, 9), (13, 11), (14, 14), (15, 16), (16, 19), (17, 20), (18, 19),
                              (19, 20), (20, 20), (21, 20), (22, 20), (23, 20), (24, 19), (25, 18), (26, 16), (27, 13),
                              (28, 11), (29, 9), (30, 7), (31, 5), (32, 2), (33, 1)]
    k_letter.letterArea = 734
    k_letter.letterPerimeter = 197
    k_letter.letterCircularity = 0.23766951044705176
    k_letter.letterCompactness = 52.8732970027248
    alphabetLetterParams.append(k_letter)

    l_letter = Letter()
    l_letter.letterName = "l"
    l_letter.letterHistPos = [(0, 55), (1, 55), (2, 55), (3, 55), (4, 55), (5, 55), (6, 55)]
    l_letter.letterArea = 385
    l_letter.letterPerimeter = 62
    l_letter.letterCircularity = 1.2585985136650057
    l_letter.letterCompactness = 9.984415584415585
    alphabetLetterParams.append(l_letter)

    m_letter = Letter()
    m_letter.letterName = "m"
    m_letter.letterHistPos = [(0, 40), (1, 40), (2, 40), (3, 40), (4, 40), (5, 40), (6, 33), (7, 9), (8, 7), (9, 6),
                              (10, 6), (11, 7), (12, 6), (13, 7), (14, 6), (15, 7), (16, 7), (17, 7), (18, 7), (19, 7),
                              (20, 7), (21, 8), (22, 9), (23, 9), (24, 40), (25, 39), (26, 39), (27, 38), (28, 36),
                              (29, 34), (30, 33), (31, 9), (32, 7), (33, 6), (34, 6), (35, 6), (36, 6), (37, 6),
                              (38, 6), (39, 7), (40, 7), (41, 7), (42, 7), (43, 7), (44, 8), (45, 8), (46, 9), (47, 9),
                              (48, 40), (49, 40), (50, 39), (51, 38), (52, 37), (53, 36), (54, 33), (55, 1)]
    m_letter.letterArea = 1039
    m_letter.letterPerimeter = 288
    m_letter.letterCircularity = 0.15741294208525244
    m_letter.letterCompactness = 79.8306063522618
    alphabetLetterParams.append(m_letter)

    n_letter = Letter()
    n_letter.letterName = "n"
    n_letter.letterHistPos = [(0, 40), (1, 40), (2, 40), (3, 40), (4, 40), (5, 40), (6, 36), (7, 9), (8, 8), (9, 7),
                              (10, 6), (11, 7), (12, 7), (13, 7), (14, 6), (15, 7), (16, 7), (17, 7), (18, 7), (19, 7),
                              (20, 7), (21, 8), (22, 8), (23, 8), (24, 9), (25, 11), (26, 39), (27, 39), (28, 38),
                              (29, 37), (30, 36), (31, 34), (32, 30)]
    n_letter.letterArea = 672
    n_letter.letterPerimeter = 159
    n_letter.letterCircularity = 0.33402954997228607
    n_letter.letterCompactness = 37.620535714285715
    alphabetLetterParams.append(n_letter)

    o_letter = Letter()
    o_letter.letterName = "o"
    o_letter.letterHistPos = [(0, 14), (1, 20), (2, 24), (3, 28), (4, 30), (5, 32), (6, 34), (7, 24), (8, 18), (9, 18),
                              (10, 16), (11, 16), (12, 14), (13, 14), (14, 16), (15, 14), (16, 14), (17, 14), (18, 14),
                              (19, 14), (20, 14), (21, 14), (22, 16), (23, 14), (24, 14), (25, 16), (26, 16), (27, 18),
                              (28, 18), (29, 24), (30, 34), (31, 32), (32, 30), (33, 28), (34, 24), (35, 20), (36, 14)]
    o_letter.letterArea = 734
    o_letter.letterPerimeter = 169
    o_letter.letterCircularity = 0.3229479370799213
    o_letter.letterCompactness = 38.91144414168937
    alphabetLetterParams.append(o_letter)

    p_letter = Letter()
    p_letter.letterName = "p"
    p_letter.letterHistPos = [(0, 54), (1, 54), (2, 54), (3, 54), (4, 54), (5, 54), (6, 42), (7, 14), (8, 13), (9, 14),
                              (10, 13), (11, 13), (12, 14), (13, 14), (14, 14), (15, 14), (16, 14), (17, 14), (18, 14),
                              (19, 14), (20, 14), (21, 16), (22, 14), (23, 16), (24, 17), (25, 18), (26, 19), (27, 24),
                              (28, 34), (29, 32), (30, 30), (31, 28), (32, 23), (33, 19), (34, 11)]
    p_letter.letterArea = 860
    p_letter.letterPerimeter = 225
    p_letter.letterCircularity = 0.21347316006615089
    p_letter.letterCompactness = 58.866279069767444
    alphabetLetterParams.append(p_letter)

    q_letter = Letter()
    q_letter.letterName = "q"
    q_letter.letterHistPos = [(0, 12), (1, 19), (2, 23), (3, 27), (4, 30), (5, 32), (6, 34), (7, 24), (8, 19), (9, 18),
                              (10, 17), (11, 16), (12, 14), (13, 16), (14, 15), (15, 14), (16, 14), (17, 14), (18, 14),
                              (19, 14), (20, 12), (21, 14), (22, 14), (23, 14), (24, 13), (25, 13), (26, 14), (27, 17),
                              (28, 49), (29, 55), (30, 55), (31, 55), (32, 55), (33, 55), (34, 55)]
    q_letter.letterArea = 876
    q_letter.letterPerimeter = 184
    q_letter.letterCircularity = 0.3251459315388302
    q_letter.letterCompactness = 38.64840182648402
    alphabetLetterParams.append(q_letter)

    r_letter = Letter()
    r_letter.letterName = "r"
    r_letter.letterHistPos = [(0, 40), (1, 40), (2, 40), (3, 40), (4, 40), (5, 40), (6, 35), (7, 9), (8, 7), (9, 7),
                              (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (17, 7), (18, 7), (19, 8),
                              (20, 6), (21, 2)]
    r_letter.letterArea = 377
    r_letter.letterPerimeter = 115
    r_letter.letterCircularity = 0.3582247048478947
    r_letter.letterCompactness = 35.07957559681697
    alphabetLetterParams.append(r_letter)

    s_letter = Letter()
    s_letter.letterName = "s"
    s_letter.letterHistPos = [(0, 1), (1, 4), (2, 13), (3, 19), (4, 23), (5, 26), (6, 29), (7, 31), (8, 26), (9, 25),
                              (10, 24), (11, 22), (12, 23), (13, 23), (14, 23), (15, 22), (16, 22), (17, 23), (18, 23),
                              (19, 22), (20, 22), (21, 23), (22, 23), (23, 23), (24, 24), (25, 26), (26, 27), (27, 31),
                              (28, 29), (29, 26), (30, 23), (31, 18), (32, 13), (33, 7)]
    s_letter.letterArea = 739
    s_letter.letterPerimeter = 187
    s_letter.letterCircularity = 0.2655651543942185
    s_letter.letterCompactness = 47.31935047361299
    alphabetLetterParams.append(s_letter)

    t_letter = Letter()
    t_letter.letterName = "t"
    t_letter.letterHistPos = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 44), (6, 49), (7, 49), (8, 49), (9, 52),
                              (10, 54), (11, 55), (12, 15), (13, 14), (14, 14), (15, 14), (16, 14), (17, 14), (18, 14),
                              (19, 1)]
    t_letter.letterArea = 487
    t_letter.letterPerimeter = 144
    t_letter.letterCircularity = 0.29513032837543
    t_letter.letterCompactness = 42.57905544147844
    alphabetLetterParams.append(t_letter)

    u_letter = Letter()
    u_letter.letterName = "u"
    u_letter.letterHistPos = [(0, 30), (1, 34), (2, 36), (3, 37), (4, 38), (5, 39), (6, 39), (7, 11), (8, 9), (9, 8),
                              (10, 8), (11, 8), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (17, 7), (18, 6), (19, 7),
                              (20, 6), (21, 7), (22, 7), (23, 7), (24, 7), (25, 10), (26, 35), (27, 40), (28, 40),
                              (29, 40), (30, 40), (31, 40), (32, 6)]
    u_letter.letterArea = 637
    u_letter.letterPerimeter = 191
    u_letter.letterCircularity = 0.21942320883053623
    u_letter.letterCompactness = 57.27001569858713
    alphabetLetterParams.append(u_letter)

    v_letter = Letter()
    v_letter.letterName = "v"
    v_letter.letterHistPos = [(0, 1), (1, 3), (2, 6), (3, 9), (4, 11), (5, 14), (6, 16), (7, 19), (8, 19), (9, 18),
                              (10, 18), (11, 18), (12, 18), (13, 18), (14, 18), (15, 18), (16, 15), (17, 12), (18, 8),
                              (19, 8), (20, 13), (21, 16), (22, 18), (23, 17), (24, 17), (25, 18), (26, 17), (27, 17),
                              (28, 18), (29, 18), (30, 17), (31, 15), (32, 12), (33, 10), (34, 7), (35, 4), (36, 2)]
    v_letter.letterArea = 503
    v_letter.letterPerimeter = 157
    v_letter.letterCircularity = 0.25643573447290613
    v_letter.letterCompactness = 49.00397614314115
    alphabetLetterParams.append(v_letter)

    w_letter = Letter()
    w_letter.letterName = "w"
    w_letter.letterHistPos = [(0, 1), (1, 4), (2, 7), (3, 10), (4, 14), (5, 17), (6, 20), (7, 24), (8, 23), (9, 23),
                              (10, 22), (11, 22), (12, 21), (13, 17), (14, 13), (15, 9), (16, 8), (17, 14), (18, 18),
                              (19, 22), (20, 22), (21, 21), (22, 21), (23, 21), (24, 21), (25, 17), (26, 12), (27, 9),
                              (28, 12), (29, 17), (30, 21), (31, 24), (32, 24), (33, 24), (34, 24), (35, 23), (36, 19),
                              (37, 15), (38, 10), (39, 9), (40, 14), (41, 17), (42, 20), (43, 20), (44, 19), (45, 20),
                              (46, 20), (47, 20), (48, 20), (49, 17), (50, 13), (51, 10), (52, 7), (53, 4), (54, 1)]
    w_letter.letterArea = 897
    w_letter.letterPerimeter = 284
    w_letter.letterCircularity = 0.1397544440721109
    w_letter.letterCompactness = 89.917502787068
    alphabetLetterParams.append(w_letter)

    x_letter = Letter()
    x_letter.letterName = "x"
    x_letter.letterHistPos = [(0, 2), (1, 4), (2, 7), (3, 10), (4, 13), (5, 16), (6, 19), (7, 22), (8, 24), (9, 24),
                              (10, 24), (11, 24), (12, 24), (13, 23), (14, 20), (15, 17), (16, 13), (17, 11), (18, 13),
                              (19, 16), (20, 20), (21, 22), (22, 24), (23, 24), (24, 24), (25, 24), (26, 25), (27, 23),
                              (28, 20), (29, 17), (30, 14), (31, 11), (32, 8), (33, 5), (34, 3), (35, 1)]
    x_letter.letterArea = 591
    x_letter.letterPerimeter = 154
    x_letter.letterCircularity = 0.3131525144664476
    x_letter.letterCompactness = 40.12859560067682
    alphabetLetterParams.append(x_letter)

    y_letter = Letter()
    y_letter.letterName = "y"
    y_letter.letterHistPos = [(0, 1), (1, 3), (2, 6), (3, 15), (4, 16), (5, 19), (6, 22), (7, 25), (8, 24), (9, 24),
                              (10, 25), (11, 25), (12, 26), (13, 28), (14, 30), (15, 29), (16, 24), (17, 18), (18, 15),
                              (19, 16), (20, 18), (21, 18), (22, 18), (23, 17), (24, 18), (25, 18), (26, 18), (27, 18),
                              (28, 19), (29, 17), (30, 14), (31, 11), (32, 9), (33, 6), (34, 3), (35, 1)]
    y_letter.letterArea = 614
    y_letter.letterPerimeter = 192
    y_letter.letterCircularity = 0.2093031563915075
    y_letter.letterCompactness = 60.039087947882734
    alphabetLetterParams.append(y_letter)

    z_letter = Letter()
    z_letter.letterName = "z"
    z_letter.letterHistPos = [(0, 1), (1, 7), (2, 16), (3, 17), (4, 18), (5, 19), (6, 19), (7, 21), (8, 22), (9, 23),
                              (10, 23), (11, 23), (12, 23), (13, 23), (14, 24), (15, 24), (16, 24), (17, 24), (18, 23),
                              (19, 23), (20, 23), (21, 23), (22, 23), (23, 23), (24, 23), (25, 23), (26, 22), (27, 21),
                              (28, 18), (29, 18), (30, 17), (31, 16), (32, 15), (33, 14), (34, 13), (35, 7)]
    z_letter.letterArea = 696
    z_letter.letterPerimeter = 159
    z_letter.letterCircularity = 0.3459591767570106
    z_letter.letterCompactness = 36.32327586206897
    alphabetLetterParams.append(z_letter)

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
        # print("    Histogram Input is Larger")

        # percorre primeiro o histograma mais pequeno (histograma da letra default)
        for value in range(len(alphabetLetterHistPos)):
            histDif = abs(letterInputHistPos[value][1] - alphabetLetterHistPos[value][1])
            totalHistDif += histDif
            lastCommonIndex = value

        # percorre depois o resto (histograma da letra a ser avaliada)
        for remain in range(lastCommonIndex + 1, len(letterInputHistPos)):
            totalHistDif += letterInputHistPos[remain][1]

        print("       Número de pixeis diferentes entre os dois histogramas: ", totalHistDif, "\n")


    # se o histograma da letra a ser avaliada for menor que o histograma da letra default que está a ser usado como comparação
    elif len(letterInputHistPos) < len(alphabetLetterHistPos):
        # print("    Histogram Input is Smaller")

        # percorre primeiro o histograma mais pequeno (histograma da letra a ser avaliada)
        for value in range(len(letterInputHistPos)):
            histDif = abs(letterInputHistPos[value][1] - alphabetLetterHistPos[value][1])
            totalHistDif += histDif
            lastCommonIndex = value

        # percorre depois o resto (histograma da letra default)
        for remain in range(lastCommonIndex + 1, len(alphabetLetterHistPos)):
            totalHistDif += alphabetLetterHistPos[remain][1]

        print("       Número de pixeis diferentes entre os dois histogramas: ", totalHistDif, "\n")

    # se o histograma da letra a ser avaliada tiver o mesmo tamanho que o histograma da letra default que está a ser usado como comparação
    else:
        # print("    Histogram Input is Equal")
        for value in range(len(letterInputHistPos)):
            histDif = abs(letterInputHistPos[value][1] - alphabetLetterHistPos[value][1])
            totalHistDif += histDif

        print("       Número de pixeis diferentes entre os dois histogramas: ", totalHistDif, "\n")

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
        print("\nNOVA LETRA A TENTAR IDENTIFICAR:  ")

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
        print("    -> COMEÇAR A PERCORRER TODAS AS LETRAS DEFAULT")

        # Antes de comparar o número de pixeis diferentes entre o histograma da letra a ser identificada e de cada uma das letras default, considera-se que a menor diferença de pixeis são todos os pixeis da ROI da letra que está a ser identificada
        minHistDif = imageROISize[0] * imageROISize[1]
        mostNearLetter = "Nada Reconhecido"

        print("       Tamanho do histograma da letra a identificar: ", len(letterHistPos), )
        # Neste ciclo, compara-se a letra a ser identificada com todas as letras default (para encontrar aquela cujos parametros mais se aproximam dos da letra a ser identificada)
        for alphabetLetter in alphabetLetterParams:
            print("\n       Letra default a avaliar: ", alphabetLetter.letterName,
                  " ,tamanho do histograma da letra default: ", len(alphabetLetter.letterHistPos))

            # se os histogramas tiverem um tamanho próximo, então avalia a diferença que há no número de pixeis ao longo das posições
            if abs(len(letterHistPos) - len(alphabetLetter.letterHistPos)) < 5:
                totalHistDif = getTotalPixelDiffBetweenHists(letterHistPos, alphabetLetter.letterHistPos)

                # após calcular a diferença total, avaliar a letra com parâmetros mais próximos
                # Avaliar se a letra default e seus parâmetros se aproximam dos mesmos parâmetros medidos para a letra a ser identificada
                if totalHistDif < 50 and totalHistDif < minHistDif and abs(
                        circularity - alphabetLetter.letterCircularity) < 0.1:
                    minHistDif = totalHistDif
                    mostNearLetter = alphabetLetter

        # Apresentar a letra reconhecida depois de avaliar o histograma da letra a ser identificada com os histogramas de todas as letras default
        # Apresenta-se também a diferença entre a área, perimetro, circularidade e compactividade da letra a ser identificada e da letra que foi reconhecida
        try:
            print("LETRA RECONHECIDA: ", mostNearLetter.letterName)

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
            reDrawHist(letterHistPos, mostNearLetter.letterHistPos)

        except AttributeError:
            print("Letra Não Reconhecida")

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
