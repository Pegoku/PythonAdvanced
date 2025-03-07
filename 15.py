import pygame
import sys
import random

# Game Config
WIDTH, HEIGHT = 600, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_RADIUS = 10
FPS = 60

WHITE = (255, 255, 255)
BLUE = (128, 131, 255)

BG_GRAY = (200, 200, 200)
BORDER_COLOR = (40, 40, 40)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3 en ratlla")

running = True
currentPlayer = 1
useBot = True
ready = False
GameBoard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def bot_move():
    global GameBoard, currentPlayer
    empty_cells = [(r, c) for r in range(3)
                   for c in range(3) if GameBoard[r][c] == 0]
    if empty_cells:
        move = random.choice(empty_cells)
        GameBoard[move[0]][move[1]] = currentPlayer
        currentPlayer = 1 if currentPlayer == 2 else 2
        print("Bot placed: ", move, currentPlayer)


def draw():
    global currentPlayer, GameBoard, running, useBot, ready
    if running:
        if ready:
            screen.fill(BG_GRAY)

            # Draw grid lines
            for x in range(1, 3):
                pygame.draw.line(screen, BORDER_COLOR,
                                 (x * WIDTH // 3, 0), (x * WIDTH // 3, HEIGHT), 5)
                pygame.draw.line(screen, BORDER_COLOR,
                                 (0, x * HEIGHT // 3), (WIDTH, x * HEIGHT // 3), 5)

            # Draw buttons
            buttons = {}
            for row in range(3):
                for col in range(3):
                    button_name = f"{row}{col}"
                    rect = pygame.Rect(
                        col * WIDTH // 3 + 5, row * HEIGHT // 3 + 5, WIDTH // 3 - 10, HEIGHT // 3 - 10)
                    buttons[button_name] = rect
                    pygame.draw.rect(screen, WHITE, rect)
            for button_name, rect in buttons.items():
                if rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0]:
                        # print(button_name)
                        buttonVar = ""
                        for i in button_name:
                            buttonVar += i+","
                        ButtonPressed = buttonVar[0:3].split(",")
                        ButtonPressedFunc(ButtonPressed)
                        if useBot and currentPlayer == 2:
                            bot_move()

            for x, a in enumerate(GameBoard):
                for y, b in enumerate(a):
                    if b == 1:
                        # print("X", x, "Y", y)
                        pygame.draw.circle(screen, BLUE, ((
                            ((WIDTH // 6*2)*(int(y)))+100), (((HEIGHT // 6*2)*(int(x)))+100)), 50, 5)
                    elif b == 2:
                        # print("X", x, "Y", y)

                        pygame.draw.line(screen, BLUE, (y * WIDTH // 3 + 20, x * HEIGHT // 3 + 20),
                                         ((y + 1) * WIDTH // 3 - 20, (x + 1) * HEIGHT // 3 - 20), 5)
                        pygame.draw.line(screen, BLUE, ((y + 1) * WIDTH // 3 - 20, x * HEIGHT //
                                                        3 + 20), (y * WIDTH // 3 + 20, (x + 1) * HEIGHT // 3 - 20), 5)

            win, howWin = checkIfWin()

            if howWin != None:
                if howWin == 0:
                    pygame.draw.line(screen, BLUE, (0, 100), (WIDTH, 100), 5)
                elif howWin == 1:
                    pygame.draw.line(screen, BLUE, (0, 300), (WIDTH, 300), 5)
                elif howWin == 2:
                    pygame.draw.line(screen, BLUE, (0, 500), (WIDTH, 500), 5)
                elif howWin == 3:
                    pygame.draw.line(screen, BLUE, (100, 0), (100, HEIGHT), 5)
                elif howWin == 4:
                    pygame.draw.line(screen, BLUE, (300, 0), (300, HEIGHT), 5)
                elif howWin == 5:
                    pygame.draw.line(screen, BLUE, (500, 0), (500, HEIGHT), 5)
                elif howWin == 6:
                    pygame.draw.line(screen, BLUE, (0, 0), (WIDTH, HEIGHT), 5)
                elif howWin == 7:
                    pygame.draw.line(screen, BLUE, (0, HEIGHT), (WIDTH, 0), 5)
            if win == 1:
                font = pygame.font.Font(None, 36)
                text = font.render("Guanya el jugador 1!", True, BORDER_COLOR)
                text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
                pygame.draw.rect(screen, WHITE, text_rect.inflate(10, 10))
                pygame.draw.rect(screen, BORDER_COLOR,
                                 text_rect.inflate(10, 10), 5)  # Border
                screen.blit(text, text_rect)
                print(howWin)
                running = False
            elif win == 2:
                font = pygame.font.Font(None, 36)
                text = font.render("Guanya el jugador 2!", True, BORDER_COLOR)
                text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
                pygame.draw.rect(screen, WHITE, text_rect.inflate(10, 10))
                pygame.draw.rect(screen, BORDER_COLOR,
                                 text_rect.inflate(10, 10), 5)  # Border
                screen.blit(text, text_rect)
                print(howWin)
                running = False
            elif win == 9:
                font = pygame.font.Font(None, 36)
                text = font.render("Ningu guanya: Empat", True, BORDER_COLOR)
                text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
                pygame.draw.rect(screen, WHITE, text_rect.inflate(10, 10))
                pygame.draw.rect(screen, BORDER_COLOR,
                                 text_rect.inflate(10, 10), 5)  # Border
                screen.blit(text, text_rect)
                print(howWin)
                running = False

            pygame.display.flip()
        else:
            screen.fill(BG_GRAY)
            font = pygame.font.Font(None, 36)

            text = font.render("Tria el mode de joc", True, BLUE)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//4))
            screen.blit(text, text_rect)

            splayer_b = pygame.Rect(WIDTH*0.25 - 100, HEIGHT//2 - 25, 200, 50)
            mplayer_b = pygame.Rect(WIDTH*0.75 - 100, HEIGHT//2 - 25, 200, 50)

            pygame.draw.rect(screen, BLUE, splayer_b)
            pygame.draw.rect(screen, BORDER_COLOR, splayer_b, 1)
            pygame.draw.rect(screen, BLUE, mplayer_b)
            pygame.draw.rect(screen, BORDER_COLOR, mplayer_b, 1)

            splayer_text = font.render("1 Jugador", True, WHITE)
            mplayer_text = font.render("2 Jugadors", True, WHITE)

            screen.blit(splayer_text, (splayer_b.x + (splayer_b.width - splayer_text.get_width()) //
                        2, splayer_b.y + (splayer_b.height - splayer_text.get_height()) // 2))
            screen.blit(mplayer_text, (mplayer_b.x + (mplayer_b.width - mplayer_text.get_width()) //
                        2, mplayer_b.y + (mplayer_b.height - mplayer_text.get_height()) // 2))

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            if splayer_b.collidepoint(mouse_pos) and mouse_click[0]:
                useBot = True
                ready = True
                pygame.time.wait(100)

            elif mplayer_b.collidepoint(mouse_pos) and mouse_click[0]:
                useBot = False
                ready = True
                pygame.time.wait(100)

            pygame.display.flip()

    else:
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()


def ButtonPressedFunc(_button):
    global GameBoard, currentPlayer, useBot
    # print(_button)
    if GameBoard[int(_button[0])][int(_button[1])] == 0:
        GameBoard[int(_button[0])][int(_button[1])] = currentPlayer
        currentPlayer = 1 if currentPlayer == 2 else 2
        print("Placed: ", _button, currentPlayer)
        if useBot and currentPlayer == 2:
            bot_move()


def checkIfWin():
    global GameBoard
    # Rows
    for a, row in enumerate(GameBoard):
        if row[0] == row[1] == row[2] != 0:
            return row[0], a
    # Columns
    for col, a in enumerate(range(3)):
        if GameBoard[0][col] == GameBoard[1][col] == GameBoard[2][col] != 0:
            return GameBoard[0][col], a+3

    # Diagonals
    if GameBoard[0][0] == GameBoard[1][1] == GameBoard[2][2] != 0:
        return GameBoard[0][0], 6
    if GameBoard[0][2] == GameBoard[1][1] == GameBoard[2][0] != 0:
        return GameBoard[0][2], 7

    # Draw
    if not any(0 in row for row in GameBoard):
        return 9, 9
    return 0, None


def main():
    global running, useBot
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
                if event.key == pygame.K_b:
                    useBot = not useBot
                    print("Bot mode:", "ON" if useBot else "OFF")

        if running:
            True
            # print("aa")

        draw()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
