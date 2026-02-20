rows = 50
columns = 50

for i in range(rows):
    for j in range(columns):
        #starting to print characters
        if i == 0:
            if j < 21:
                print(".", end="")
            elif j == 21:
                print(",", end="")
            elif j == 22:
                print(";", end="")
            elif j == 23:
                print("*", end="")
            elif j == 24 or j == 25 or j == 26:
                print("%", end="")
            elif j == 27:
                print("S", end="")
            elif j == 28 or j == 29:
                print("%", end="")
            elif j == 30:
                print("*", end="")
            elif j == 31:
                print(":", end="")
            elif j == 32 or j == 33:
                print(",", end="")
            else:
                print(".", end="")
        elif i == 1 :
            if j < 19:
                print(".", end="")
            elif j == 19:
                print(":", end="")
            elif j == 20:
                print(";", end="")
            elif j == 21:
                print("?", end="")
            elif j == 22:
                print("%", end="")
            elif j == 23 or j == 24 or j == 25:
                print("S", end="")
            elif j == 26 or j == 27:
                print("#", end="")
            elif j == 28 or j == 29 or j == 30:
                print("S", end="")
            elif j == 31:
                print("%", end="")
            elif j == 32:
                print("+", end="")
            elif j == 33:
                print(";", end="")
            elif j == 34:
                print(":", end="")
            elif j == 35:
                print(",", end="")
            elif 36 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i == 2:
            if j < 17:
                print(".", end="")
            elif j == 17:
                print(",", end="")
            elif j == 18:
                print("*", end="")
            elif j == 19 or j == 20 or j == 21 or j == 22 or j == 23:
                print("S", end="")
            elif 24 <= j <= 31:
                print("#", end="")
            elif j == 32:
                print("S", end="")
            elif j == 33:
                print("*", end="")
            elif j == 34 or j == 35:
                print(";", end="")
            elif j == 36:
                print(":", end="")
            elif j == 37:
                print(",", end="")
            elif 38 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")

        elif i == 3:

            if j < 15:
                print(".", end="")
            elif j == 15:
                print(",", end="")
            elif j == 16:
                print(";", end="")
            elif j == 17:
                print("%", end="")
            elif j == 18:
                print("#", end="")
            elif j == 19:
                print("S", end="")
            elif j == 20:
                print("%", end="")
            elif j == 21:
                print("S", end="")
            elif j == 22 or j == 23:
                print("#", end="")
            elif j == 24:
                print("S", end="")
            elif 25 <= j <= 30:
                print("#", end="")
            elif j == 31 or j == 32 or j == 33:
                print("S", end="")
            elif j == 34:
                print("?", end="")
            elif j == 35:
                print("*", end="")
            elif j == 36:
                print(";", end="")
            elif j == 37:
                print(":", end="")
            elif j == 38:
                print(",", end="")
            elif 39 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i == 4:
            if j < 14:
                print(".", end="")
            elif j == 14:
                print(":", end="")
            elif j == 15:
                print("*", end="")
            elif j == 16 or j == 17 or j == 18:
                print("S", end="")
            elif j == 19 or j == 20:
                print("%", end="")
            elif 21 <= j <= 31:
                print("#", end="")
            elif j == 32 or j == 33 or j == 34 or j == 35:
                print("S", end="")
            elif j == 36:
                print("?", end="")
            elif j == 37:
                print(";", end="")
            elif j == 38:
                print(":", end="")
            elif j == 39:
                print(",", end="")
            elif 40 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==5:
            if j < 13:
                print(".", end="")
            elif j == 13:
                print(":", end="")
            elif j == 14:
                print("*", end="")
            elif j == 15 or j == 16 or j == 17 or j == 18 or j == 19:
                print("%", end="")
            elif j == 20:
                print("S", end="")
            elif 21 <= j <= 30:
                print("#", end="")
            elif j == 31 or j == 32:
                print("S", end="")
            elif j == 33 or j == 34:
                print("%", end="")
            elif j == 35 or j == 36:
                print("S", end="")
            elif j == 37:
                print("*", end="")
            elif j == 38 or j == 39:
                print(",", end="")
            elif 40 <= j <= 47:
                print(".", end="")
            elif j == 48:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==6:
            if j < 12:
                print(".", end="")
            elif j == 12:
                print(":", end="")
            elif j == 13:
                print("*", end="")
            elif 14 <= j <= 19:
                print("%", end="")
            elif j == 20:
                print("S", end="")
            elif 21 <= j <= 31:
                print("#", end="")
            elif j == 32:
                print("S", end="")
            elif 33 <= j <= 35:
                print("%", end="")
            elif j == 36 or j == 37:
                print("S", end="")
            elif j == 38:
                print(";", end="")
            elif j == 39 or j == 40:
                print(",", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==7:
            if j < 11:
                print(".", end="")
            elif j == 11:
                print(",", end="")
            elif j == 12:
                print("*", end="")
            elif j == 13:
                print("%", end="")
            elif j == 14:
                print("?", end="")
            elif 15 <= j <= 18:
                print("%", end="")
            elif j == 19:
                print("?", end="")
            elif 20 <= j <= 24:
                print("S", end="")
            elif j == 25 or j == 26:
                print("#", end="")
            elif j == 27:
                print("S", end="")
            elif 28 <= j <= 30:
                print("#", end="")
            elif j == 31 or j == 32:
                print("S", end="")
            elif 33 <= j <= 36:
                print("%", end="")
            elif j == 37:
                print("S", end="")
            elif j == 38:
                print("%", end="")
            elif j == 39:
                print(",", end="")
            elif 40 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==8:
            if j < 11:
                print(".", end="")
            elif j == 11:
                print(";", end="")
            elif j == 12 or j == 13 or j == 14:
                print("%", end="")
            elif j == 15:
                print("S", end="")
            elif j == 16:
                print("%", end="")
            elif j == 17 or j == 18 or j == 19:
                print("?", end="")
            elif j == 20 or j == 21:
                print("%", end="")
            elif j == 22:
                print("?", end="")
            elif j == 23:
                print("*", end="")
            elif j == 24:
                print("?", end="")
            elif j == 25:
                print("S", end="")
            elif j == 26:
                print("#", end="")
            elif j == 27 or j == 28:
                print("S", end="")
            elif j == 29:
                print("#", end="")
            elif j == 30 or j == 31:
                print("S", end="")
            elif j == 32 or j == 33 or j == 34:
                print("%", end="")
            elif j == 35:
                print("S", end="")
            elif j == 36 or j == 37:
                print("%", end="")
            elif j == 38:
                print("#", end="")
            elif j == 39:
                print("*", end="")
            elif 40 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==9:
            if j < 10:
                print(".", end="")
            elif j == 10:
                print(",", end="")
            elif j == 11:
                print("?", end="")
            elif j == 12 or j == 13:
                print("%", end="")
            elif j == 14:
                print("#", end="")
            elif j == 15 or j == 16:
                print("%", end="")
            elif j == 17 or j == 18:
                print("?", end="")
            elif j == 19:
                print("%", end="")
            elif j == 20 or j == 21:
                print("?", end="")
            elif j == 22:
                print("+", end="")
            elif j == 23 or j == 24:
                print(";", end="")
            elif j == 25:
                print("%", end="")
            elif 26 <= j <= 30:
                print("S", end="")
            elif j == 31 or j == 32:
                print("%", end="")
            elif j == 33:
                print("?", end="")
            elif j == 34:
                print("%", end="")
            elif j == 35 or j == 36:
                print("S", end="")
            elif j == 37:
                print("%", end="")
            elif j == 38:
                print("S", end="")
            elif j == 39:
                print("#", end="")
            elif j == 40:
                print("+", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==10:
            if j < 10:
                print(".", end="")
            elif j == 10:
                print(";", end="")
            elif j == 11 or j == 12:
                print("%", end="")
            elif j == 13:
                print("#", end="")
            elif j == 14:
                print("S", end="")
            elif j == 15:
                print("?", end="")
            elif j == 16 or j == 17:
                print("%", end="")
            elif j == 18:
                print("S", end="")
            elif j == 19 or j == 20:
                print("%", end="")
            elif j == 21:
                print("?", end="")
            elif j == 22:
                print(";", end="")
            elif j == 23 or j == 24:
                print(":", end="")
            elif j == 25:
                print("*", end="")
            elif j == 26:
                print("S", end="")
            elif j == 27:
                print("%", end="")
            elif j == 28:
                print("?", end="")
            elif 29 <= j <= 32:
                print("%", end="")
            elif j == 33:
                print("?", end="")
            elif j == 34 or j == 35:
                print("%", end="")
            elif j == 36 or j == 37:
                print("#", end="")
            elif j == 38:
                print("%", end="")
            elif j == 39:
                print("#", end="")
            elif j == 40:
                print("%", end="")
            elif j == 41:
                print(",", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==11:
            if j < 9:
                print(".", end="")
            elif j == 9:
                print(",", end="")
            elif j == 10:
                print("*", end="")
            elif j == 11:
                print("%", end="")
            elif j == 12 or j == 13:
                print("#", end="")
            elif j == 14 or j == 15:
                print("%", end="")
            elif j == 16 or j == 17:
                print("S", end="")
            elif j == 18:
                print("#", end="")
            elif j == 19 or j == 20:
                print("S", end="")
            elif j == 21:
                print("*", end="")
            elif j == 22 or j == 23 or j == 24:
                print(":", end="")
            elif j == 25:
                print(";", end="")
            elif j == 26:
                print("?", end="")
            elif j == 27:
                print("%", end="")
            elif j == 28:
                print("*", end="")
            elif 29 <= j <= 33:
                print("?", end="")
            elif j == 34 or j == 35:
                print("%", end="")
            elif j == 36 or j == 37:
                print("#", end="")
            elif j == 38 or j == 39 or j == 40:
                print("S", end="")
            elif j == 41:
                print("+", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==12:
            if j < 8:
                print(".", end="")
            elif j == 8 or j == 9:
                print(",", end="")
            elif j == 10:
                print("*", end="")
            elif j == 11:
                print("S", end="")
            elif j == 12:
                print("#", end="")
            elif 13 <= j <= 16:
                print("S", end="")
            elif 17 <= j <= 19:
                print("#", end="")
            elif j == 20:
                print("%", end="")
            elif j == 21 or j == 22:
                print(";", end="")
            elif j == 23 or j == 24:
                print(":", end="")
            elif j == 25:
                print(",", end="")
            elif j == 26:
                print("+", end="")
            elif j == 27:
                print("%", end="")
            elif j == 28 or j == 29:
                print("*", end="")
            elif 30 <= j <= 32:
                print("?", end="")
            elif 33 <= j <= 35:
                print("%", end="")
            elif j == 36:
                print("S", end="")
            elif j == 37 or j == 38:
                print("#", end="")
            elif j == 39 or j == 40:
                print("S", end="")
            elif j == 41:
                print("*", end="")
            elif j == 42:
                print(",", end="")
            elif 43 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==13:
            if j < 7:
                print(".", end="")
            elif j == 7 or j == 8:
                print(",", end="")
            elif j == 9:
                print(":", end="")
            elif j == 10:
                print("?", end="")
            elif j == 11 or j == 12:
                print("#", end="")
            elif 13 <= j <= 16:
                print("S", end="")
            elif j == 17 or j == 18:
                print("#", end="")
            elif j == 19:
                print("S", end="")
            elif j == 20:
                print("+", end="")
            elif j == 21 or j == 22 or j == 23:
                print(";", end="")
            elif j == 24:
                print(":", end="")
            elif j == 25:
                print(",", end="")
            elif j == 26:
                print(":", end="")
            elif j == 27 or j == 28:
                print("?", end="")
            elif j == 29:
                print("*", end="")
            elif 30 <= j <= 33:
                print("?", end="")
            elif j == 34 or j == 35:
                print("%", end="")
            elif j == 36:
                print("S", end="")
            elif 37 <= j <= 40:
                print("#", end="")
            elif j == 41:
                print("+", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==14:
            if j < 7:
                print(".", end="")
            elif j == 7 or j == 8:
                print(",", end="")
            elif j == 9:
                print(";", end="")
            elif j == 10 or j == 11:
                print("%", end="")
            elif j == 12 or j == 13:
                print("#", end="")
            elif j == 14:
                print("S", end="")
            elif j == 15:
                print("#", end="")
            elif j == 16:
                print("S", end="")
            elif 17 <= j <= 19:
                print("#", end="")
            elif j == 20:
                print("?", end="")
            elif j == 21:
                print("+", end="")
            elif j == 22 or j == 23 or j == 24:
                print(";", end="")
            elif j == 25:
                print(":", end="")
            elif j == 26 or j == 27:
                print(",", end="")
            elif j == 28:
                print("+", end="")
            elif j == 29 or j == 30:
                print("*", end="")
            elif j == 31:
                print("?", end="")
            elif j == 32:
                print("*", end="")
            elif j == 33 or j == 34:
                print("?", end="")
            elif j == 35 or j == 36:
                print("%", end="")
            elif j == 37 or j == 38:
                print("S", end="")
            elif j == 39:
                print("@", end="")
            elif j == 40:
                print("#", end="")
            elif j == 41:
                print("S", end="")
            elif j == 42:
                print(";", end="")
            elif 43 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif 15==i:
            if j < 7:
                print(".", end="")
            elif j == 7 or j == 8:
                print(",", end="")
            elif j == 9:
                print("+", end="")
            elif j == 10:
                print("%", end="")
            elif j == 11:
                print("#", end="")
            elif j == 12:
                print("S", end="")
            elif j == 13 or j == 14:
                print("#", end="")
            elif j == 15:
                print("S", end="")
            elif j == 16 or j == 17:
                print("#", end="")
            elif j == 18:
                print("%", end="")
            elif j == 19 or j == 20:
                print("+", end="")
            elif j == 21 or j == 22 or j == 23:
                print(";", end="")
            elif j == 24 or j == 25:
                print(":", end="")
            elif j == 26:
                print(",", end="")
            elif j == 27:
                print(";", end="")
            elif j == 28 or j == 29 or j == 30 or j == 31:
                print("*", end="")
            elif j == 32:
                print("?", end="")
            elif 33 <= j <= 36:
                print("%", end="")
            elif j == 37:
                print("S", end="")
            elif j == 38 or j == 39 or j == 40:
                print("#", end="")
            elif j == 41:
                print(":", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==16:
            if j < 6:
                print(".", end="")
            elif j == 6 or j == 7:
                print(",", end="")
            elif j == 8:
                print(":", end="")
            elif j == 9:
                print("+", end="")
            elif j == 10:
                print("S", end="")
            elif j == 11:
                print("#", end="")
            elif j == 12:
                print("S", end="")
            elif 13 <= j <= 16:
                print("#", end="")
            elif j == 17:
                print("%", end="")
            elif j == 18:
                print("*", end="")
            elif j == 19 or j == 20 or j == 21:
                print("+", end="")
            elif j == 22 or j == 23:
                print(";", end="")
            elif j == 24:
                print(":", end="")
            elif j == 25 or j == 26:
                print(",", end="")
            elif j == 27:
                print(",", end="")
            elif j == 28:
                print("*", end="")
            elif j == 29:
                print("+", end="")
            elif j == 30:
                print("*", end="")
            elif j == 31:
                print("?", end="")
            elif j == 32:
                print("+", end="")
            elif j == 33:
                print("%", end="")
            elif j == 34 or j == 35:
                print("S", end="")
            elif j == 36:
                print("%", end="")
            elif j == 37:
                print("S", end="")
            elif 38 <= j <= 40:
                print("#", end="")
            elif j == 41:
               print(";", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==17:
            if j < 6:
                print(".", end="")
            elif j == 6 or j == 7:
                print(",", end="")
            elif j == 8:
                print(":", end="")
            elif j == 9:
                print("*", end="")
            elif j == 10 or j == 11 or j == 12:
                print("S", end="")
            elif 13 <= j <= 16:
                print("#", end="")
            elif j == 17 or j == 18:
                print("S", end="")
            elif j == 19:
                print("%", end="")
            elif 20 <= j <= 23:
                print("S", end="")
            elif j == 24:
                print("%", end="")
            elif j == 25:
                print("*", end="")
            elif j == 26 or j == 27:
                print(":", end="")
            elif j == 28 or j == 29:
                print("*", end="")
            elif j == 30:
                print("+", end="")
            elif j == 31 or j == 32 or j == 33:
                print("?", end="")
            elif 34 <= j <= 38:
                print("S", end="")
            elif j == 39 or j == 40:
                print("#", end="")
            elif j == 41:
                print("+", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==18:
            if j < 6:
                print(".", end="")
            elif j == 6 or j == 7:
                print(",", end="")
            elif j == 8:
                print(";", end="")
            elif j == 9:
                print("?", end="")
            elif j == 10 or j == 11:
                print("S", end="")
            elif 12 <= j <= 15:
                print("#", end="")
            elif j == 16:
                print("S", end="")
            elif j == 17:
                print("#", end="")
            elif j == 18:
                print("S", end="")
            elif j == 19:
                print("#", end="")
            elif 20 <= j <= 24:
                print("@", end="")
            elif j == 25:
                print("#", end="")
            elif j == 26:
                print("S", end="")
            elif j == 27 or j == 28 or j == 29:
                print("%", end="")
            elif j == 30:
                print("+", end="")
            elif j == 31:
                print("*", end="")
            elif j == 32:
                print("%", end="")
            elif j == 33:
                print("?", end="")
            elif j == 34:
                print("S", end="")
            elif j == 35 or j == 36:
                print("#", end="")
            elif j == 37:
                print("S", end="")
            elif j == 38 or j == 39 or j == 40:
                print("#", end="")
            elif j == 41:
                print("*", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==19:
            if j < 6:
                print(".", end="")
            elif j == 6 or j == 7:
                print(",", end="")
            elif j == 8:
                print(";", end="")
            elif j == 9:
                print("%", end="")
            elif j == 10 or j == 11:
                print("S", end="")
            elif 12 <= j <= 15:
                print("#", end="")
            elif j == 16:
                print("S", end="")
            elif j == 17:
                print("#", end="")
            elif j == 18:
                print("S", end="")
            elif 19 <= j <= 28:
                print("@", end="")
            elif j == 29:
                print("#", end="")
            elif j == 30 or j == 31:
                print("%", end="")
            elif 32 <= j <= 40:
                print("#", end="")
            elif j == 41:
                print("*", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==20:
            if j < 6:
                print(".", end="")
            elif j == 6 or j == 7:
                print(",", end="")
            elif j == 8:
                print(";", end="")
            elif j == 9:
                print("%", end="")
            elif j == 10 or j == 11:
                print("S", end="")
            elif 12 <= j <= 15:
                print("#", end="")
            elif j == 16:
                print("S", end="")
            elif j == 17:
                print("#", end="")
            elif j == 18:
                print("S", end="")
            elif 19 <= j <= 28:
                print("@", end="")
            elif j == 29:
                print("#", end="")
            elif j == 30 or j == 31:
                print("%", end="")
            elif 32 <= j <= 40:
                print("#", end="")
            elif j == 41:
                print("*", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==21:
            if j == 0:
                print(",", end="")
            elif 1 <= j <= 4:
                print(".", end="")
            elif j == 5 or j == 6:
                print(",", end="")
            elif j == 7:
                print(":", end="")
            elif j == 8:
                print("+", end="")
            elif j == 9:
                print("%", end="")
            elif j == 10:
                print("S", end="")
            elif 11 <= j <= 13:
                print("#", end="")
            elif 14 <= j <= 15:
                print("S", end="")
            elif 16 <= j <= 17:
                print("#", end="")
            elif j == 18:
                print("S", end="")
            elif 19 <= j <= 29:
                print("@", end="")
            elif 30 <= j <= 31:
                print("#", end="")
            elif 32 <= j <= 36:
                print("@", end="")
            elif j == 37:
                print("#", end="")
            elif j == 38:
                print("@", end="")
            elif 39 <= j <= 40:
                print("#", end="")
            elif j == 41:
                print("+", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==22:
            if j < 5:
                print(".", end="")
            elif j == 5 or j == 6:
                print(",", end="")
            elif j == 7:
                print(":", end="")
            elif j == 8:
                print("+", end="")
            elif j == 9:
                print("%", end="")
            elif 10 <= j <= 12:
                print("#", end="")
            elif 13==j or j == 14:
                print("S", end="")
            elif j == 15:
                print("#", end="")
            elif j == 16:
                print("S", end="")
            elif j == 17 or j == 18:
                print("#", end="")
            elif j == 19 or j == 20:
                print("@", end="")
            elif 21 <= j <= 27:
                print("#", end="")
            elif j == 28:
                print("@", end="")
            elif j == 29:
                print("%", end="")
            elif j == 30:
                print("?", end="")
            elif j == 31:
                print("#", end="")
            elif j == 32 or j == 33:
                print("@", end="")
            elif j == 34:
                print("#", end="")
            elif j == 35 or j == 36 or j == 37:
                print("@", end="")
            elif j == 38 or j == 39:
                print("#", end="")
            elif j == 40:
                print("S", end="")
            elif j == 41:
                print(";", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==23:
            if j < 5:
                print(".", end="")
            elif j == 5 or j == 6:
                print(",", end="")
            elif j == 7:
                print(":", end="")
            elif j == 8:
                print("*", end="")
            elif j == 9:
                print("S", end="")
            elif j == 10:
                print("#", end="")
            elif 11 <= j <= 13:
                print("S", end="")
            elif j == 14 or j == 15:
                print("#", end="")
            elif j == 16:
                print("%", end="")
            elif j == 17 or j == 18:
                print("*", end="")
            elif j == 19:
                print("S", end="")
            elif 20 <= j <= 24:
                print("#", end="")
            elif 25 <= j <= 28:
                print("S", end="")
            elif j == 29:
                print(";", end="")
            elif j == 30:
                print(":", end="")
            elif j == 31:
                print("S", end="")
            elif 32 <= j <= 37:
                print("@", end="")
            elif j == 38 or j == 39:
                print("#", end="")
            elif j == 40:
                print("S", end="")
            elif j == 41:
                print(",", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==24:
            if j < 5:
                print(".", end="")
            elif j == 5 or j == 6:
                print(",", end="")
            elif j == 7:
                print(":", end="")
            elif j == 8:
                print("*", end="")
            elif j == 9:
                print("%", end="")
            elif 10 <= j <= 13:
                print("S", end="")
            elif j == 14 or j == 15:
                print("#", end="")
            elif j == 16:
                print("%", end="")
            elif j == 17:
                print("+", end="")
            elif j == 18 or j == 19:
                print(";", end="")
            elif j == 20:
                print("+", end="")
            elif j == 21:
                print("?", end="")
            elif j == 22:
                print("%", end="")
            elif j == 23:
                print("S", end="")
            elif j == 24:
                print("#", end="")
            elif j == 25 or j == 26:
                print("S", end="")
            elif j == 27:
                print("%", end="")
            elif j == 28:
                print(";", end="")
            elif j == 29:
                print(":", end="")
            elif j == 30:
                print(",", end="")
            elif j == 31:
                print("?", end="")
            elif j == 32:
                print("#", end="")
            elif 33 <= j <= 37:
                print("@", end="")
            elif j == 38 or j == 39:
                print("#", end="")
            elif j == 40:
                print("S", end="")
            elif j == 41:
                print(",", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==25:
            if j < 5:
                print(".", end="")
            elif j == 5:
                print(",", end="")
            elif j == 6:
                print(":", end="")
            elif j == 7:
                print(";", end="")
            elif j == 8:
                print("*", end="")
            elif j == 9:
                print("%", end="")
            elif 10 <= j <= 14:
                print("S", end="")
            elif j == 15:
                print("#", end="")
            elif j == 16:
                print("%", end="")
            elif j == 17:
                print("+", end="")
            elif j == 18 or j == 19 or j == 20:
                print(";", end="")
            elif j == 21 or j == 22 or j == 23:
                print(":", end="")
            elif j == 24:
                print(";", end="")
            elif j == 25 or j == 26:
                print("+", end="")
            elif j == 27:
                print(";", end="")
            elif j == 28 or j == 29:
                print(":", end="")
            elif j == 30:
                print(",", end="")
            elif j == 31:
                print(";", end="")
            elif j == 32:
                print("?", end="")
            elif j == 33:
                print("#", end="")
            elif 34 <= j <= 36:
                print("@", end="")
            elif 37 <= j <= 39:
                print("#", end="")
            elif j == 40:
                print("%", end="")
            elif j == 41:
                print(",", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==26:
            if j < 4:
                print(".", end="")
            elif j == 4 or j == 5:
                print(",", end="")
            elif j == 6:
                print(":", end="")
            elif j == 7:
                print(";", end="")
            elif j == 8:
                print("*", end="")
            elif j == 9 or j == 10:
                print("%", end="")
            elif 11 <= j <= 14:
                print("S", end="")
            elif j == 15:
                print("#", end="")
            elif j == 16:
                print("%", end="")
            elif j == 17:
                print("+", end="")
            elif 18 <= j <= 20:
                print(";", end="")
            elif j == 21 or j == 22:
                print(":", end="")
            elif j == 23 or j == 24:
                print(",", end="")
            elif j == 25:
                print(":", end="")
            elif 26 <= j <= 28:
                print(";", end="")
            elif j == 29 or j == 30:
                print(":", end="")
            elif 31 <= j <= 33:
                print(";", end="")
            elif j == 34:
                print("*", end="")
            elif j == 35:
                print("?", end="")
            elif j == 36 or j == 37:
                print("*", end="")
            elif j == 38:
                print("S", end="")
            elif j == 39:
                print("#", end="")
            elif j == 40:
                print("%", end="")
            elif j == 41:
                print(",", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")     
        elif i==27:
            if j < 3:
                print(",", end="") if j == 0 else print(".", end="")
            elif 1 <= j <= 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5:
                print(":", end="")
            elif j == 6:
                print(";", end="")
            elif j == 7:
                print("?", end="")
            elif j == 8:
                print("S", end="")
            elif j == 9:
                print("%", end="")
            elif 10 <= j <= 14:
                print("S", end="")
            elif j == 15:
                print("%", end="")
            elif j == 16:
                print("*", end="")
            elif 17 <= j <= 20:
                print(";", end="")
            elif 21 <= j <= 24:
                print(":", end="")
            elif j == 25:
                print("+", end="")
            elif j == 26 or j == 27:
                print(";", end="")
            elif j == 28:
                print(":", end="")
            elif j == 29:
                print(",", end="")
            elif j == 30:
                print(";", end="")
            elif j == 31:
                print(";", end="")
            elif 32 <= j <= 34:
                print(":", end="")
            elif j == 35:
                print(";", end="")
            elif j == 36:
                print("*", end="")
            elif j == 37:
                print("%", end="")
            elif j == 38:
                print("S", end="")
            elif j == 39:
                print("?", end="")
            elif j == 40:
                print(",", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==28:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5:
                print(":", end="")
            elif j == 6:
                print(";", end="")
            elif j == 7:
                print("?", end="")
            elif j == 8:
                print("S", end="")
            elif j == 9:
                print("%", end="")
            elif j == 10 or j == 11:
                print("S", end="")
            elif j == 12:
                print("#", end="")
            elif j == 13:
                print("S", end="")
            elif j == 14:
                print("%", end="")
            elif j == 15:
                print("?", end="")
            elif j == 16 or j == 17:
                print("+", end="")
            elif 18 <= j <= 21:
                print(";", end="")
            elif j == 22:
                print(":", end="")
            elif j == 23:
                print(";", end="")
            elif j == 24:
                print(":", end="")
            elif j == 25:
                print(";", end="")
            elif j == 26 or j == 27:
                print("*", end="")
            elif j == 28:
                print(";", end="")
            elif j == 29:
                print(":", end="")
            elif j == 30:
                print("+", end="")
            elif j == 31:
                print(";", end="")
            elif j == 32 or j == 33:
                print(":", end="")
            elif j == 34 or j == 35:
                print(";", end="")
            elif j == 36 or j == 37:
                print("*", end="")
            elif j == 38:
                print("%", end="")
            elif j == 39:
                print("?", end="")
            elif j == 40:
                print(",", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==29:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5:
                print(":", end="")
            elif j == 6:
                print(";", end="")
            elif j == 7:
                print("?", end="")
            elif j == 8 or j == 9 or j == 10:
                print("S", end="")
            elif j == 11 or j == 12:
                print("#", end="")
            elif j == 13:
                print("S", end="")
            elif j == 14:
                print("?", end="")
            elif j == 15:
                print("*", end="")
            elif j == 16:
                print("+", end="")
            elif 17 <= j <= 21:
                print(";", end="")
            elif j == 22 or j == 23:
                print(":", end="")
            elif j == 24:
                print(",", end="")
            elif j == 25:
                print(":", end="")
            elif j == 26:
                print("*", end="")
            elif 27 <= j <= 30:
                print("%", end="")
            elif j == 31:
                print(";", end="")
            elif j == 32:
                print(":", end="")
            elif j == 33 or j == 34:
                print(";", end="")
            elif j == 35 or j == 36 or j == 37:
                print("+", end="")
            elif j == 38:
                print("?", end="")
            elif j == 39:
                print("+", end="")
            elif j == 40:
                print(",", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==30:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5:
                print(":", end="")
            elif j == 6:
                print(";", end="")
            elif j == 7:
                print("?", end="")
            elif j == 8 or j == 9 or j == 10:
                print("S", end="")
            elif j == 11 or j == 12:
                print("#", end="")
            elif j == 13:
                print("S", end="")
            elif j == 14:
                print("?", end="")
            elif j == 15:
                print("*", end="")
            elif 16 <= j <= 21:
                print(";", end="")
            elif 22 <= j <= 26:
                print(":", end="")
            elif j == 27:
                print(";", end="")
            elif j == 28:
                print("*", end="")
            elif j == 29:
                print("?", end="")
            elif j == 30:
                print("*", end="")
            elif j == 31 or j == 32:
                print(";", end="")
            elif j == 33:
                print("+", end="")
            elif j == 34 or j == 35:
                print("+", end="")
            elif j == 36 or j == 37:
                print(";", end="")
            elif j == 38:
                print("*", end="")
            elif j == 39:
                print(":", end="")
            elif j == 40:
                print(",", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==31:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5:
                print(":", end="")
            elif j == 6:
                print(";", end="")
            elif j == 7:
                print("*", end="")
            elif j == 8 or j == 9:
                print("S", end="")
            elif j == 10 or j == 11 or j == 12 or j == 13:
                print("#", end="")
            elif j == 14 or j == 15:
                print("*", end="")
            elif j == 16:
                print("+", end="")
            elif j == 17 or j == 18:
                print(";", end="")
            elif j == 19:
                print("+", end="")
            elif j == 20 or j == 21:
                print(";", end="")
            elif j == 22:
                print(":", end="")
            elif j == 23 or j == 24:
                print(";", end="")
            elif 25 <= j <= 28:
                print(":", end="")
            elif 29 <= j <= 32:
                print(";", end="")
            elif 33 <= j <= 35:
                print("+", end="")
            elif j == 36 or j == 37:
                print(":", end="")
            elif j == 38:
                print(";", end="")
            elif j == 39 or j == 40:
                print(",", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==32:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5:
                print(":", end="")
            elif j == 6:
                print(";", end="")
            elif j == 7:
                print("?", end="")
            elif j == 8 or j == 9 or j == 10:
                print("S", end="")
            elif j == 11 or j == 12:
                print("#", end="")
            elif j == 13:
                print("S", end="")
            elif j == 14:
                print("?", end="")
            elif j == 15:
                print("*", end="")
            elif 16 <= j <= 21:
                print(";", end="")
            elif 22 <= j <= 26:
                print(":", end="")
            elif j == 27:
                print(";", end="")
            elif j == 28:
                print("*", end="")
            elif j == 29:
                print("?", end="")
            elif j == 30:
                print("*", end="")
            elif j == 31 or j == 32:
                print(";", end="")
            elif j == 33:
                print("+", end="")
            elif j == 34 or j == 35:
                print("+", end="")
            elif j == 36 or j == 37:
                print(";", end="")
            elif j == 38:
                print("*", end="")
            elif j == 39:
                print(":", end="")
            elif j == 40:
                print(",", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==33:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5:
                print(":", end="")
            elif j == 6:
                print(";", end="")
            elif j == 7:
                print("*", end="")
            elif j == 8:
                print("%", end="")
            elif j == 9:
                print("S", end="")
            elif 10 <= j <= 13:
                print("#", end="")
            elif j == 14:
                print("?", end="")
            elif j == 15:
                print("*", end="")
            elif j == 16:
                print("+", end="")
            elif 17 <= j <= 22:
                print(";", end="")
            elif j == 23:
                print("*", end="")
            elif j == 24:
                print("?", end="")
            elif j == 25:
                print("*", end="")
            elif 26 <= j <= 29:
                print("?", end="")
            elif j == 30:
                print("*", end="")
            elif 31 <= j <= 34:
                print("+", end="")
            elif 35 <= j <= 37:
                print(":", end="")
            elif j == 38 or j == 39 or j == 40:
                print(",", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif 34==i:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5:
                print(":", end="")
            elif j == 6:
                print(";", end="")
            elif j == 7:
                print("*", end="")
            elif j == 8:
                print("%", end="")
            elif j == 9:
                print("S", end="")
            elif 10 <= j <= 13:
                print("#", end="")
            elif j == 14 or j == 15:
                print("?", end="")
            elif j == 16:
                print("*", end="")
            elif j == 17 or j == 18:
                print("+", end="")
            elif 19 <= j <= 23:
                print(";", end="")
            elif 24 <= j <= 27:
                print("+", end="")
            elif j == 28:
                print("*", end="")
            elif j == 29:
                print("?", end="")
            elif j == 30:
                print("%", end="")
            elif j == 31:
                print("*", end="")
            elif 32 <= j <= 34:
                print("+", end="")
            elif j == 35:
                print(":", end="")
            elif 36 <= j <= 40:
                print(",", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==35:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5:
                print(":", end="")
            elif j == 6:
                print(";", end="")
            elif j == 7:
                print("+", end="")
            elif j == 8:
                print("%", end="")
            elif j == 9 or j == 10:
                print("S", end="")
            elif 11 <= j <= 13:
                print("#", end="")
            elif 14 <= j <= 16:
                print("?", end="")
            elif j == 17 or j == 18:
                print("*", end="")
            elif 19 <= j <= 21:
                print("+", end="")
            elif j == 22 or j == 23:
                print(";", end="")
            elif j == 24 or j == 25:
                print("+", end="")
            elif j == 26:
                print("*", end="")
            elif j == 27 or j == 28:
                print("?", end="")
            elif j == 29:
                print("*", end="")
            elif 30 <= j <= 33:
                print("+", end="")
            elif j == 34:
                print(";", end="")
            elif j == 35:
                print(":", end="")
            elif 36 <= j <= 40:
                print(",", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==36:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5 or j == 6:
                print(":", end="")
            elif j == 7:
                print("+", end="")
            elif j == 8:
                print("%", end="")
            elif j == 9:
                print("#", end="")
            elif j == 10:
                print("S", end="")
            elif 11 <= j <= 13:
                print("#", end="")
            elif 14 <= j <= 18:
                print("?", end="")
            elif j == 19:
                print("*", end="")
            elif j == 20:
                print("+", end="")
            elif 21 <= j <= 25:
                print(";", end="")
            elif 26 <= j <= 31:
                print("+", end="")
            elif j == 32 or j == 33:
                print("*", end="")
            elif j == 34 or j == 35:
                print(":", end="")
            elif 36 <= j <= 40:
                print(",", end="")
            elif 41 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==37:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5 or j == 6 or j == 7:
                print(":", end="")
            elif j == 8:
                print("+", end="")
            elif j == 9:
                print("?", end="")
            elif j == 10 or j == 11 or j == 12:
                print("S", end="")
            elif j == 13 or j == 14:
                print("#", end="")
            elif 15 <= j <= 20:
                print("?", end="")
            elif j == 21:
                print("*", end="")
            elif j == 22:
                print("+", end="")
            elif j == 23 or j == 24:
                print(";", end="")
            elif 25 <= j <= 27:
                print(":", end="")
            elif j == 28 or j == 29:
                print(";", end="")
            elif j == 30 or j == 31:
                print("+", end="")
            elif j == 32:
                print("*", end="")
            elif j == 33:
                print("%", end="")
            elif j == 34:
                print("+", end="")
            elif j == 35 or j == 36:
                print(":", end="")
            elif 37 <= j <= 42:
                print(",", end="")
            elif 43 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==38:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5 or j == 6 or j == 7:
                print(":", end="")
            elif j == 8:
                print("+", end="")
            elif j == 9:
                print("%", end="")
            elif j == 10:
                print("S", end="")
            elif 11 <= j <= 14:
                print("#", end="")
            elif j == 15:
                print("?", end="")
            elif j == 16 or j == 17:
                print("*", end="")
            elif 18 <= j <= 21:
                print("?", end="")
            elif 22 <= j <= 23:
                print("%", end="")
            elif 24 <= j <= 30:
                print("*", end="")
            elif j == 31:
                print("S", end="")
            elif j == 32:
                print("%", end="")
            elif j == 33:
                print("*", end="")
            elif j == 34:
                print(";", end="")
            elif j == 35 or j == 36:
                print(":", end="")
            elif 37 <= j <= 42:
                print(",", end="")
            elif 43 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==39:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3 or j == 4:
                print(",", end="")
            elif j == 5 or j == 6 or j == 7:
                print(":", end="")
            elif j == 8:
                print("+", end="")
            elif j == 9:
                print("%", end="")
            elif 10 <= j <= 13:
                print("#", end="")
            elif j == 14:
                print("S", end="")
            elif j == 15:
                print("%", end="")
            elif j == 16 or j == 17 or j == 18:
                print("*", end="")
            elif 19 <= j <= 22:
                print("?", end="")
            elif 23 <= j <= 26:
                print("%", end="")
            elif j == 27:
                print("S", end="")
            elif j == 28 or j == 29 or j == 30:
                print("%", end="")
            elif j == 31:
                print("@", end="")
            elif j == 32:
                print("S", end="")
            elif j == 33:
                print(";", end="")
            elif j == 34 or j == 35:
                print(":", end="")
            elif 36 <= j <= 42:
                print(",", end="")
            elif j == 43 or j == 44:
                print(".", end="")
            elif j == 45 or j == 46:
                print(",", end="")
            elif j == 47 or j == 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i ==40:
            if j == 0:
                print(",", end="")
            elif 1 <= j <= 4:
                print(".", end="")
            elif j == 5 or j == 6:
                print(",", end="")
            elif j == 7:
                print(":", end="")
            elif j == 8:
                print("+", end="")
            elif j == 9:
                print("S", end="")
            elif 10 <= j <= 13:
                print("#", end="")
            elif j == 14:
                print("S", end="")
            elif j == 15:
                print("?", end="")
            elif 16 <= j <= 19:
                print("*", end="")
            elif 20 <= j <= 25:
                print("?", end="")
            elif 26 <= j <= 29:
                print("%", end="")
            elif j == 30:
                print("S", end="")
            elif j == 31 or j == 32:
                print("@", end="")
            elif j == 33:
                print("+", end="")
            elif j == 34:
                print(":", end="")
            elif 35 <= j <= 42:
                print(",", end="")
            elif j == 43 or j == 44:
                print(".", end="")
            elif j == 45 or j == 46:
                print(",", end="")
            elif j == 47:
                print(",", end="")
            elif j == 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==41:
            if j == 0:
                print(",", end="")
            elif 1 <= j <= 4:
                print(".", end="")
            elif j == 5:
                print(":", end="")
            elif j == 6:
                print("*", end="")
            elif j == 7:
                print("%", end="")
            elif j == 8:
                print("#", end="")
            elif j == 9:
                print("S", end="")
            elif 10 <= j <= 13:
                print("#", end="")
            elif j == 14:
                print("?", end="")
            elif j == 15:
                print("*", end="")
            elif 16 <= j <= 18:
                print("+", end="")
            elif j == 19:
                print("*", end="")
            elif 20 <= j <= 21:
                print("?", end="")
            elif j == 22:
                print("%", end="")
            elif j == 23:
                print("?", end="")
            elif 24 <= j <= 28:
                print("%", end="")
            elif j == 29:
                print("#", end="")
            elif j == 30:
                print("@", end="")
            elif j == 31:
                print("#", end="")
            elif j == 32:
                print("?", end="")
            elif j == 33:
                print("+", end="")
            elif j == 34:
                print(":", end="")
            elif j == 35 or j == 36:
                print(",", end="")
            elif j == 37 or j == 38:
                print(".", end="")
            elif j == 39 or j == 40:
                print(",", end="")
            elif j == 41 or j == 42 or j == 43:
                print(".", end="")
            elif j == 44:
                print(",", end="")
            elif j == 45:
                print(".", end="")
            elif j == 46:
                print(",", end="")
            elif j == 47:
                print(".", end="")
            elif j == 48:
                print(",", end="")
            elif j == 49:
                print(" ", end="")
            else:
                print(" ", end="")
        elif i==42:
            if j == 0:
                print(",", end="")
            elif j == 1 or j == 2:
                print(".", end="")
            elif j == 3:
                print(",", end="")
            elif j == 4:
                print(";", end="")
            elif j == 5:
                print("?", end="")
            elif j == 6:
                print("S", end="")
            elif j == 7 or j == 8:
                print("#", end="")
            elif j == 9:
                print("S", end="")
            elif j == 10:
                print("+", end="")
            elif j == 11:
                print("%", end="")
            elif j == 12 or j == 13 or j == 14:
                print("#", end="")
            elif j == 15:
                print("%", end="")
            elif 16 <= j <= 20:
                print("+", end="")
            elif j == 21 or j == 22:
                print("*", end="")
            elif 23 <= j <= 30:
                print("?", end="")
            elif j == 31 or j == 32:
                print("#", end="")
            elif j == 33:
                print("@", end="")
            elif j == 34 or j == 35 or j == 36:
                print("#", end="")
            elif j == 37:
                print("%", end="")
            elif j == 38:
                print("?", end="")
            elif j == 39:
                print("+", end="")
            elif j == 40:
                print(":", end="")
            elif j == 41:
                print(",", end="")
            elif 42 <= j <= 48:
                print(".", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        elif i==43:
            if j == 0:
                print(".", end="")
            elif j == 1:
                print(",", end="")
            elif j == 2:
                print(";", end="")
            elif j == 3:
                print("?", end="")
            elif j == 4:
                print("S", end="")
            elif 5 <= j <= 8:
                print("#", end="")
            elif j == 9:
                print("S", end="")
            elif j == 10:
                print("+", end="")
            elif 11 <= j <= 13:
                print("S", end="")
            elif 14 <= j <= 15:
                print("#", end="")
            elif j == 16:
                print("+", end="")
            elif j == 17 or j == 18:
                print(";", end="")
            elif j == 19 or j == 20:
                print("+", end="")
            elif j == 21 or j == 22:
                print("*", end="")
            elif 23 <= j <= 26:
                print("?", end="")
            elif j == 27 or j == 28:
                print("*", end="")
            elif j == 29:
                print("?", end="")
            elif j == 30 or j == 31:
                print("S", end="")
            elif 32 <= j <= 39:
                print("#", end="")
            elif j == 40:
                print("%", end="")
            elif j == 41:
                print("?", end="")
            elif j == 42 or j == 43:
                print("*", end="")
            elif j == 44:
                print("+", end="")
            elif 45 <= j <= 48:
                print(",", end="")
            elif j == 49:
                print(" ", end="")
            else:
                print(" ", end="")
        elif i==44:
            if j == 0:
                print("+", end="")
            elif j == 1:
                print("?", end="")
            elif 2 <= j <= 5:
                print("S", end="")
            elif 6 <= j <= 9:
                print("#", end="")
            elif j == 10:
                print("?", end="")
            elif 11 <= j <= 15:
                print("#", end="")
            elif j == 16:
                print("+", end="")
            elif 17 <= j <= 20:
                print(";", end="")
            elif j == 21 or j == 22:
                print("+", end="")
            elif 23 <= j <= 28:
                print("*", end="")
            elif j == 29:
                print("+", end="")
            elif j == 30:
                print("*", end="")
            elif j == 31 or j == 32:
                print("?", end="")
            elif j == 33:
                print("%", end="")
            elif 34 <= j <= 45:
                print("#", end="")
            elif j == 46:
                print("S", end="")
            elif j == 47:
                print("%", end="")
            elif j == 48:
                print("*", end="")
            elif j == 49:
                print(",", end="")
            else:
                print(" ", end="")
        #all the rows are completed
        # rest will be just space          
        else:
            print(' ',end='')
    print()   # move to next line