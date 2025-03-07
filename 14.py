import pygame
import sys
# Game Config
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_RADIUS = 10
FPS = 60

WHITE = (255, 255, 255)
BLUE = (128, 131, 255)
BG_GRAY = (200, 200, 200)
BORDER_COLOR = (40, 40, 40)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")

# PreFunctions

def genTopBars(nBarsV, nBarsH, BarH, BarV):
    __Bars = []
    for i in range(nBarsV):
        for j in range(nBarsH):
            __Bars.append((j*BarH + BarH/2, i*BarV + BarV/2))
    return __Bars

# Vars
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 4
ball_speed_y = -4
VarnBarsV = 5
VarnBarsH = 10
BarV = 20
BarH = WIDTH // VarnBarsH

diff = 0

topBars = genTopBars(VarnBarsV, VarnBarsH, BarH, BarV)
print(topBars)


running = False

def draw():
    global diff, topBars, BarH, BarV, VarnBarsH, VarnBarsV
    if diff == 0:
        screen.fill(BG_GRAY)
        font = pygame.font.Font(None, 36)
        
        text = font.render("Tria la dificultat", True, BLUE)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//4))
        screen.blit(text, text_rect)        
        
        easy_button = pygame.Rect(WIDTH//4 - 50, HEIGHT//2 - 25, 100, 50)
        normal_button = pygame.Rect(WIDTH//2 - 50, HEIGHT//2 - 25, 100, 50)
        hard_button = pygame.Rect(3*WIDTH//4 - 50, HEIGHT//2 - 25, 100, 50)
        
        pygame.draw.rect(screen, BLUE, easy_button)
        pygame.draw.rect(screen, BORDER_COLOR, easy_button, 1)
        pygame.draw.rect(screen, BLUE, normal_button)
        pygame.draw.rect(screen, BORDER_COLOR, normal_button, 1)
        pygame.draw.rect(screen, BLUE, hard_button)
        pygame.draw.rect(screen, BORDER_COLOR, hard_button, 1)
        
        easy_text = font.render("Easy", True, WHITE)
        normal_text = font.render("Normal", True, WHITE)
        hard_text = font.render("Hard", True, WHITE)
        
        screen.blit(easy_text, (easy_button.x + (easy_button.width - easy_text.get_width()) // 2, easy_button.y + (easy_button.height - easy_text.get_height()) // 2))
        screen.blit(normal_text, (normal_button.x + (normal_button.width - normal_text.get_width()) // 2, normal_button.y + (normal_button.height - normal_text.get_height()) // 2))
        screen.blit(hard_text, (hard_button.x + (hard_button.width - hard_text.get_width()) // 2, hard_button.y + (hard_button.height - hard_text.get_height()) // 2))

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if easy_button.collidepoint(mouse_pos) and mouse_click[0]:
            diff = 1
            VarnBarsH = 6
            VarnBarsV = 1
            BarV = 20
            BarH = WIDTH // VarnBarsH
            topBars = genTopBars(VarnBarsV, VarnBarsH, BarH, BarV)
        elif normal_button.collidepoint(mouse_pos) and mouse_click[0]:
            diff = 2
            VarnBarsH = 8
            VarnBarsV = 2
            BarV = 20
            BarH = WIDTH // VarnBarsH
            topBars = genTopBars(VarnBarsV, VarnBarsH, BarH, BarV)
        elif hard_button.collidepoint(mouse_pos) and mouse_click[0]:
            diff = 3            
            VarnBarsH = 10
            VarnBarsV = 3
            BarV = 20
            BarH = WIDTH // VarnBarsH
            topBars = genTopBars(VarnBarsV, VarnBarsH, BarH, BarV)
        pygame.display.flip()
    else: 
        screen.fill(BG_GRAY)
        pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, BORDER_COLOR, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT), 1)

        pygame.draw.circle(screen, BORDER_COLOR, (ball_x, ball_y), BALL_RADIUS+1)
        pygame.draw.circle(screen, BLUE, (ball_x, ball_y), BALL_RADIUS)


        for bar in topBars:
            pygame.draw.rect(screen, BLUE, (bar[0] - BarH/2, bar[1] - BarV/2, BarH, BarV))
            pygame.draw.rect(screen, BORDER_COLOR, (bar[0] - BarH/2, bar[1] - BarV/2, BarH, BarV), 1)
        pygame.display.flip()
        
        if topBars == []:
            screen.fill(BG_GRAY)
            font = pygame.font.Font(None, 74)
            text = font.render("Has Guanyat!", True, BLUE)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(5000)
            pygame.quit()
            sys.exit()

def main():
    global running, paddle_x, ball_x, ball_y, ball_speed_x, ball_speed_y

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True

        if running:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and paddle_x > 0:
                paddle_x -= 5
            if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
                paddle_x += 5

            ball_x += ball_speed_x
            ball_y += ball_speed_y

            # Walls
            if ball_x <= BALL_RADIUS or ball_x >= WIDTH - BALL_RADIUS:
                ball_speed_x = -ball_speed_x
            if ball_y <= BALL_RADIUS:
                ball_speed_y = -ball_speed_y
            if ball_y >= HEIGHT - BALL_RADIUS:
                ball_y = HEIGHT // 2
                ball_x = WIDTH // 2
                running = False

            # Paddle
            if (paddle_y < ball_y + BALL_RADIUS < paddle_y + PADDLE_HEIGHT) and (paddle_x < ball_x < paddle_x + PADDLE_WIDTH):
                ball_speed_y = -ball_speed_y
                
            # TopBars     
            for bar in topBars[:]:  
                if (bar[0] - BarH/2 < ball_x < bar[0] + BarH/2) and (ball_y <= bar[1] + BALL_RADIUS):
                    ball_speed_y = -ball_speed_y
                    ball_y = bar[1] + BarV/2 + BALL_RADIUS
                    topBars.remove(bar)
                    print(bar)
                    print(topBars)
                    break
            


        draw()
        clock.tick(FPS)

if __name__ == "__main__":
    main()