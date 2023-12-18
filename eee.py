import pygame
import random

pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Random Number Visualization")

# 폰트 설정
font = pygame.font.Font(None, 100)

def generate_random_number(n, excluded_numbers, previous_numbers):
    available_numbers = list(set(range(1, n+1)) - set(excluded_numbers) - set(previous_numbers))
    if not available_numbers:
        return None
    return random.choice(available_numbers)

# 사용자로부터 숫자 입력 받기
screen.fill((0, 0, 0))
f_text = font.render("What is the max?", True, (255, 255, 255))
f_text_rect = f_text.get_rect(center=(screen_width // 2, screen_height // 2))
screen.blit(f_text, f_text_rect)
pygame.display.flip()
number = int(input("숫자를 입력하세요: "))

# 제외할 숫자 입력 받기
excluded_numbers = []
screen.fill((0, 0, 0))

text_lines = ["Enter the number to exclude", "(press q and enter if none)"]
line_height = font.get_linesize()

for i, line in enumerate(text_lines):
    line_text = font.render(line, True, (255, 255, 255))
    line_rect = line_text.get_rect(center=(screen_width // 2, screen_height // 2 + i * line_height))
    screen.blit(line_text, line_rect)

pygame.display.flip()

while True:
    
    excluded_number = input("제외할 숫자를 입력하세요. (완료하려면 'q' 입력): ")
    if excluded_number == 'q':
        break
    excluded_numbers.append(int(excluded_number))

previous_numbers = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 랜덤 숫자 생성
            random_number = generate_random_number(number, excluded_numbers, previous_numbers)
            if random_number is not None:
                previous_numbers.append(random_number)
            else:
                running = False  # 숫자를 뽑을 수 없을 때 종료

    # 화면 색상 설정 (검은색)
    screen.fill((0, 0, 0))

    # 랜덤 숫자 출력
    if previous_numbers:
        current_number = previous_numbers[-1]
        text = font.render(str(current_number), True, (255, 255, 255))
    else:
        text = font.render("Click to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()

# "끝" 출력
screen.fill((0, 0, 0))
end_text = font.render("end", True, (255, 255, 255))
end_text_rect = end_text.get_rect(center=(screen_width // 2, screen_height // 2))
screen.blit(end_text, end_text_rect)
pygame.display.flip()

pygame.time.wait(2000)  # 2초 동안 "끝" 텍스트를 보여줌

pygame.quit()