import pygame
import sys

#メイン処理を行う関数の定義
def main():
  pygame.init() #pygameモジュールの初期化
  pygame.display.set_caption('初めてのPygame 画像表示') #ウィンドウに表示されるタイトルを指定
  screen = pygame.display.set_mode((640, 360)) #描画面(スクリーン)を初期化する
  clock = pygame.time.Clock() #clockオブジェクトを作成
  #背景画像の読み込み
  img_bg = pygame.image.load('./py_samples/Chapter10/pg_bg.png')
  #キャラクター画像の読み込み
  img_chara = [pygame.image.load('./py_samples/Chapter10/pg_chara0.png'),
  pygame.image.load('./py_samples/Chapter10/pg_chara1.png')]
  tmr = 0 #時間を管理する変数tmrの宣言

  while True:
    tmr += 1
    for event in pygame.event.get(): #pygameのイベントを繰り返しで処理する
      if event.type == pygame.QUIT: #ウィンドウのxボタンをクリックした時
        pygame.quit() #pygameモジュールの初期化を解除
        sys.exit() #プログラムを終了する
      if event.type == pygame.KEYDOWN: #キーを押すイベントが発生した時
        if event.key == pygame.K_1: #1キーなら
          screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN) #フルスクリーンモードにする
        if event.key == pygame.K_2 or event.key == pygame.K_ESCAPE: #2キーかEscキーなら
          screen = pygame.display.set_mode((640, 360)) #通常表示に戻す

    x = tmr%160 #背景スクロール用の値をtmrから求める 背景画像の横幅が160
    for i in range(5): #繰り返しで横に5枚分の
      screen.blit(img_bg, [i*160-x, 0]) #背景画像を描画

    screen.blit(img_chara[tmr%2], [224, 160]) #キャラクターをアニメーションさせて描画
    #screen.blit(画像を読み込んだ変数, [x座標, y座標])
    pygame.display.update() #画面を更新する
    clock.tick(5) #フレームレートを指定

if __name__ == '__main__':
  main()