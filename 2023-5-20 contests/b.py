# jackie0214 さんのコード、参考に勉強させていただいています
# URL=https://atcoder.jp/contests/abc302/submissions/41602179

import sys
import math
import numpy as np
 
def main(lines):
    H, W = list(map(int, lines[0].split()))
    Si = [lines[i] for i in range(1, H+1)]
    dx = [1, -1, 0]
    dy = [1, -1, 0]
    snuke = ['s', 'n', 'u', 'k', 'e']
    Spos = []
    for h in range(0, H):
        for w in range(0, W):
            if Si[h][w] == 's':
                Spos.append([h,w])
    # Sposでsの場所を記録している            
    
    for s in range(0, len(Spos)):
        x, y = Spos[s]
        for ix in range(0, 3):
            for iy in range(0, 3):
                tmp = ['s']
                pos = [[x, y]]
                for l in range(1,5):
                    if x+l*dx[ix] < 0 or x+l*dx[ix] >= H or y+l*dy[iy] < 0 or y+l*dy[iy] >= W:
                        break
                    else:
                        tmp.append(Si[x+l*dx[ix]][y+l*dy[iy]])
                        pos.append([x+l*dx[ix], y+l*dy[iy]])
                    # tmpには、sunkeの文字をあてはめに行って、posにはそのあてはめる文字の場所を入れていく
                if tmp == snuke:
                    print('Yes')
                    for i in range(0,5):
                        print(str(pos[i][0]+1)+' '+str(pos[i][1]+1))
                    exit()
                    
    print('No')
 
if __name__ == '__main__':
    lines = []
    # linesの初期化
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
        # linesに文字を入れている
#           sys.stdinは、標準入力からの入力を取得するためのストリームオブジェクトです。
#           for l in sys.stdin:は、sys.stdinからの入力を行ごとに反復処理するためのループです。反復ごとに、変数lには入力の1行が代入されます。
#           l.rstrip('\r\n')は、入力の各行の末尾から改行文字（\rと\n）を削除します。
#           lines.append(l.rstrip('\r\n'))は、改行文字を削除した行をlinesリストに追加します。append()メソッドは、リストの末尾に要素を追加するために使用されます。
    main(lines)
