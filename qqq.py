import random
import pygame

#1
pygame.init()

#2
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Seat Arrangement")

#3
white = (255, 255, 255)
black = (0,0,0)
gray = (128,128,128)

#4
font = pygame.font.Font(None, 30)

def draw_seats(seat_numbers,rows,columns):
  #5
    seat_width = width//columns
    seat_height = height//rows

  #6
    for i in range(rows):
        for j in range(columns):
            seat_number = seat_numbers[i][j]
            seat_x = j * seat_width
            seat_y = i * seat_height

      #7
            seat_text = font.render(str(seat_number),True, black)
            seat_text_rect = seat_text.get_rect()
            seat_text_rect.center = (seat_x + seat_width // 2, seat_y + seat_height // 2)
            screen.blit(seat_text, seat_text_rect)

      #8
            seat_rect = pygame.Rect(seat_x, seat_y, seat_width, seat_height)
            pygame.draw.rect(screen, gray, seat_rect, 2)

#9
def seat_arrangement():
    number = int(input("번호를 입력하세요: "))
    rows = int(input("행의 개수를 입력하세요: "))
    columns = int(input("열의 개수를 입력하세요: "))

  #10
    numbers = random.sample(range(1, number+1), rows*columns)

  #11
    seats = []
    for i in range(rows):
        row = numbers[i*columns : (i+1)*columns]
        seats.append(row)

#13
    running = True
    while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)
        draw_seats(seats, rows, columns)
        pygame.display.flip()

    pygame.quit()

#14
seat_arrangement()