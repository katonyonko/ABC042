from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="042"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc058_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  mod=10**9+7
  H,W,A,B=map(int,input().split())
  F=[1]
  for i in range(H+W):
    F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(H+W):
    I.append(I[-1]*(H+W-i)%mod)
  I=I[::-1]
  ans=0
  for i in range(H-A):
    ans=(ans+F[B-1+i]*I[i]*I[B-1]*F[H+W-B-i-2]*I[H-1-i]*I[W-1-B])%mod
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])