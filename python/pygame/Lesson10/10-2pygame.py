import pygame
import sys

# 10-2pygameのシステム
# リアルタイム処理と画面の更新
WHITE = (255,255,255)
BLACK = (0, 0, 0)

def main():
  pygame.init() #pygameモジュールの初期化
  pygame.display.set_caption('初めてのpygame') #ウィンドウに表示されるタイトルを指定
  screen = pygame.display.set_mode((800,600)) #
  clock = pygame.time.Clock()
  font = pygame.font.Font(None, 80)
  tmr = 0

  while True:
    tmr += 1
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    txt = font.render(str(tmr), True, WHITE)

    screen.fill(BLACK)
    screen.blit(txt, [300, 200])
    pygame.display.update()
    clock.tick(10)

if __name__ == '__main__':
  main()