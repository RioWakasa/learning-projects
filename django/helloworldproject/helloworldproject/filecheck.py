from pathlib import Path

print(Path(__file__).resolve().parent.parent)
# __file__ このファイル .resolve() 絶対パス(/Users/からこのファイルまで) .parent ひとつ前のディレクトリ