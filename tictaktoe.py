import pygame

pygame.init()
field = pygame.display.set_mode((500, 500))
pygame.display.set_caption("TicTakToe")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 225, 0)

draw_object = "x"

game = True

game_won = False

first_b = True
second_b = True
third_b = True
fourth_b = True
fifth_b = True
sixth_b = True
seventh_b = True
eighth_b = True
ninth_b = True

res = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]


def display_fill(color):
    pygame.display.get_surface().fill(color)


def draw_rect(x, y, width, height, color):
    pygame.draw.rect(field, color, (x, y, width, height))


def check_win(player):
    # CHECK ROW WIN
    row_counter = 0
    for row in res:
        for i in row:
            if i == player:
                continue
            else:
                break
        else:
            if row_counter == 0:
                pygame.draw.line(field, yellow, (10, 80), (490, 80), 10)
            elif row_counter == 1:
                pygame.draw.line(field, yellow, (10, 250), (490, 250), 10)
            else:
                pygame.draw.line(field, yellow, (10, 420), (490, 420), 10)

            return True
        row_counter += 1

    # CHECK COLUMN WIN
    column_counter = 0
    for i in range(3):
        for column in res:
            if column[i] == player:
                continue
            else:
                break
        else:
            if column_counter == 0:
                pygame.draw.line(field, yellow, (80, 10), (80, 490), 10)
            elif column_counter == 1:
                pygame.draw.line(field, yellow, (250, 10), (250, 490), 10)
            else:
                pygame.draw.line(field, yellow, (420, 10), (420, 490), 10)
            return True
        column_counter += 1

    # CHECK DIAGONAL WIN
    for i in range(3):
        if res[i][i] == player:
            continue
        else:
            break
    else:
        pygame.draw.line(field, yellow, (10, 10), (490, 490), 10)
        return True

    for i in range(3):
        if res[i][2-i] == player:
            continue
        else:
            break
    else:
        pygame.draw.line(field, yellow, (10, 490), (490, 10), 10)
        return True


display_fill(white)

first = pygame.draw.rect(field, black, (0, 0, 160, 160))
second = pygame.draw.rect(field, black, (170, 0, 160, 160))
third = pygame.draw.rect(field, black, (340, 0, 160, 160))
fourth = pygame.draw.rect(field, black, (0, 170, 160, 160))
fifth = pygame.draw.rect(field, black, (170, 170, 160, 160))
sixth = pygame.draw.rect(field, black, (340, 170, 160, 160))
seventh = pygame.draw.rect(field, black, (0, 340, 160, 160))
eighth = pygame.draw.rect(field, black, (170, 340, 160, 160))
ninth = pygame.draw.rect(field, black, (340, 340, 160, 160))

pygame.display.update()

while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                first_b = True
                second_b = True
                third_b = True
                fourth_b = True
                fifth_b = True
                sixth_b = True
                seventh_b = True
                eighth_b = True
                ninth_b = True

                res = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

                draw_object = "x"

                game_won = False                

                display_fill(white)

                first = pygame.draw.rect(field, black, (0, 0, 160, 160))
                second = pygame.draw.rect(field, black, (170, 0, 160, 160))
                third = pygame.draw.rect(field, black, (340, 0, 160, 160))
                fourth = pygame.draw.rect(field, black, (0, 170, 160, 160))
                fifth = pygame.draw.rect(field, black, (170, 170, 160, 160))
                sixth = pygame.draw.rect(field, black, (340, 170, 160, 160))
                seventh = pygame.draw.rect(field, black, (0, 340, 160, 160))
                eighth = pygame.draw.rect(field, black, (170, 340, 160, 160))
                ninth = pygame.draw.rect(field, black, (340, 340, 160, 160))
            
            pygame.display.update()
        if game_won != True:
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                if first.collidepoint(position) and first_b == True:
                    if draw_object == 'x':
                        pygame.draw.line(field, red, (10, 10), (150, 150), 5)
                        pygame.draw.line(field, red, (10, 150), (150, 10), 5)
                        res[0][0] = 1
                        draw_object = 'o'
                    else:
                        pygame.draw.circle(field, green, (80, 80), 75, 5)
                        draw_object = 'x'
                        res[0][0] = 2
                    first_b = False
                if second.collidepoint(position) and second_b == True:
                    if draw_object == 'x':
                        pygame.draw.line(field, red, (180, 10), (320, 150), 5)
                        pygame.draw.line(field, red, (180, 150), (320, 10), 5)
                        draw_object = 'o'
                        res[0][1] = 1
                    else:
                        pygame.draw.circle(field, green, (250, 80), 75, 5)
                        draw_object = 'x'
                        res[0][1] = 2
                    second_b = False
                if third.collidepoint(position) and third_b == True:
                    if draw_object == 'x':
                        pygame.draw.line(field, red, (350, 10), (490, 150), 5)
                        pygame.draw.line(field, red, (350, 150), (490, 10), 5)
                        draw_object = 'o'
                        res[0][2] = 1
                    else:
                        pygame.draw.circle(field, green, (420, 80), 75, 5)
                        draw_object = 'x'
                        res[0][2] = 2
                    third_b = False
                if fourth.collidepoint(position) and fourth_b == True:
                    if draw_object == 'x':
                        pygame.draw.line(field, red, (10, 180), (150, 320), 5)
                        pygame.draw.line(field, red, (10, 320), (150, 180), 5)
                        draw_object = 'o'
                        res[1][0] = 1
                    else:
                        pygame.draw.circle(field, green, (80, 250), 75, 5)
                        draw_object = 'x'
                        res[1][0] = 2
                    fourth_b = False
                if fifth.collidepoint(position) and fifth_b == True:
                    if draw_object == 'x':
                        pygame.draw.line(field, red, (180, 180), (320, 320), 5)
                        pygame.draw.line(field, red, (180, 320), (320, 180), 5)
                        draw_object = 'o'
                        res[1][1] = 1
                    else:
                        pygame.draw.circle(field, green, (250, 250), 75, 5)
                        draw_object = 'x'
                        res[1][1] = 2
                    fifth_b = False
                if sixth.collidepoint(position) and sixth_b == True:
                    if draw_object == 'x':
                        pygame.draw.line(field, red, (350, 180), (490, 320), 5)
                        pygame.draw.line(field, red, (350, 320), (490, 180), 5)
                        draw_object = 'o'
                        res[1][2] = 1
                    else:
                        pygame.draw.circle(field, green, (420, 250), 75, 5)
                        draw_object = 'x'
                        res[1][2] = 2
                    sixth_b = False
                if seventh.collidepoint(position) and seventh_b == True:
                    if draw_object == 'x':
                        pygame.draw.line(field, red, (10, 350), (150, 490), 5)
                        pygame.draw.line(field, red, (10, 490), (150, 350), 5)
                        draw_object = 'o'
                        res[2][0] = 1
                    else:
                        pygame.draw.circle(field, green, (80, 420), 75, 5)
                        draw_object = 'x'
                        res[2][0] = 2
                    seventh_b = False
                if eighth.collidepoint(position) and eighth_b == True:
                    if draw_object == 'x':
                        pygame.draw.line(field, red, (180, 350), (320, 490), 5)
                        pygame.draw.line(field, red, (180, 490), (320, 350), 5)
                        draw_object = 'o'
                        res[2][1] = 1
                    else:
                        pygame.draw.circle(field, green, (250, 420), 75, 5)
                        draw_object = 'x'
                        res[2][1] = 2
                    eighth_b = False
                if ninth.collidepoint(position) and ninth_b == True:
                    if draw_object == 'x':
                        pygame.draw.line(field, red, (350, 350), (490, 490), 5)
                        pygame.draw.line(field, red, (350, 490), (490, 350), 5)
                        draw_object = 'o'
                        res[2][2] = 1
                    else:
                        pygame.draw.circle(field, green, (420, 420), 75, 5)
                        draw_object = 'x'
                        res[2][2] = 2
                    ninth_b = False
    pygame.display.update()

    if check_win(1):
        game_won = True
    if check_win(2):
        game_won = True
pygame.quit()
