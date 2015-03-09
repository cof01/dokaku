def get_oppsite(n):
  if n == '1':
    ret = ['6','S']
  elif n == '2' or n == 'D':
    ret = ['5']
  elif n == '3' or n == 'T':
    ret = ['4']
  elif n == '4':
    ret = ['3','T']
  elif n == '5':
    ret = ['2','D']
  elif n == '6':
    ret = ['1']
  else:
    ret = ['1','2','D','3','T','4','5','6','S']
  return ret

def get_rest(dice):
  ret = ['1','2','D','3','T','4','5','6','S']
  if '1' in dice:
    ret.remove('1')
  if ('2' in dice) or ('D' in dice):
    ret.remove('2')
    ret.remove('D')
  if ('3' in dice) or ('T' in dice):
    ret.remove('3')
    ret.remove('T')
  if ('4' in dice):
    ret.remove('4')
  if ('5' in dice):
    ret.remove('5')
  if ('6' in dice) or ('S' in dice):
    ret.remove('6')
  return ret

'''
def get_neighboor_address(i):
  if i == 0:
    return [('side',1),('opposite',2),('long',3),('long',4)]
  elif i == 1:
    return [('side',0),('side',2),('long',3),('opposite',4),('side',5)]
  elif i == 2:
    return [('opposite',0),('side',1),('long',3),('long',4),('long',5)]
  elif i == 3:
    return [('long',0),('long',1),('long',2),('side',4),('opposite',5)]
  elif i == 4:
    return [('long',4),('opposite',1),('long',2),('side',3),('side',5)]
  elif i == 5:
    return [('side',1),('long',2),('opposite',3),('side',4)]
  else:
    return []
'''
def get_neighboor_address(i):
  if i == 0:
    return [('side',1),('opposite',2)]
  elif i == 1:
    return [('side',0),('side',2),('opposite',4)]
  elif i == 2:
    return [('opposite',0),('side',1),('long',3)]
  elif i == 3:
    return [('long',2),('side',4),('opposite',5)]
  elif i == 4:
    return [('opposite',1),('side',3),('side',5)]
  elif i == 5:
    return [('opposite',3),('side',4)]
  else:
    return []

def search(dice,i):
  ret = set(['1','2','D','3','T','4','5','6','S'])
  ret &= set(get_rest(dice))
  for cdn in get_neighboor_address(i):
    direction, n = cdn[0], dice[cdn[1]]
    if direction == 'side':
      ret &= set(get_from_side(n))
    elif direction == 'long':
      ret &= set(get_from_long(n))
    elif direction == 'opposite':
      ret &= set(get_oppsite(n))
  if len(ret) == 1:
    ret = ret.pop()
  return ret

def get_from_side(n):
  if n == '1':
    return ('2','T','4','5')
  elif n == '2':
    return ('1','S')
  elif n == 'D':
    return ('3','4')
  elif n == '3':
    return ('D','5')
  elif n == 'T':
    return ('1','6')
  elif n == '4':
    return ('1','D','5','6')
  elif n == '5':
    return ('1','3','4','S')
  elif n == '6':
    return ('2','T')
  elif n == 'S':
    return ('4','5')
  else:
    return ('1','2','D','3','T','4','5','6','S')

def get_from_long(n):
  if n == '1':
    return ('D','3','4','5')
  elif n == '2':
    return ('T','4')
  elif n == 'D':
    return ('1','S')
  elif n == '3':
    return ('1','S')
  elif n == 'T':
    return ('4','T')
  elif n == '4':
    return ('1','2','5','S')
  elif n == '5':
    return ('1','T','4','6')
  elif n == '6':
    return ('5','D')
  elif n == 'S':
    return ('3','4')
  else:
    return ('1','2','D','3','T','4','5','6','S')

def get_ans_dict(input):
   return {input[i]:i for i in range(len(input)) if input[i] in 'wxyz'}

def create_output(input, ans_dict, dice):
  ret = ''
  for k,v in ans_dict.items():
    #print k,v
    if k in 'wxyz' and len(dice[v]) == 1:
      ret += '%s=%s ' % (k,dice[v])
    elif len(dice[v]) == 0:
      ret = 'none'
      break
    elif len(dice[v]) > 1:
      ret = 'many'
      break
  ret = 'No: %s %s expected:%s' % (input[0], ret, input[2])
  return ret
  

def main(input):
  input[1] = input[1].replace('/','')
  dice = [x for x in input[1]]
  ans_dict = get_ans_dict(input[1])
  c = 0
  ans = ''
  while c < 5:
    for i in range(len(dice)):
      t = dice[i]
      if t in set(['w','x','y','z']) or len(t) > 1:
        dice[i] = search(dice,i)
    c+=1
  print dice
  print create_output(input, ans_dict, dice)

input_list = '''0	Tx4/5yz	x=1,y=S,z=2
1	14S/xyz	none
2	1w6/xyz	many
3	4w3/12S	w=5
4	4w3/S51	w=D
5	15S/wD4	w=3
6	54D/6Tw	w=1
7	S21/35w	w=4
8	w2x/354	w=S,x=1
9	wx1/54D	w=6,x=T
10	45w/12x	w=3,x=S
11	5w2/x14	w=S,x=T
12	Dw5/x41	w=3,x=6
13	w4x/1y6	w=D,x=5,y=T
14	15w/xy4	w=S,x=3,y=D
15	D35/wxy	w=6,x=4,y=1
16	4wx/51y	w=6,x=T,y=2
17	wTx/D4y	w=1,x=6,y=5
18	wxy/z3D	w=1,x=4,y=6,z=5
19	wx5/1yz	w=D,x=4,y=T,z=6
20	w53/xyz	w=4,x=1,y=2,z=S
21	wx1/yzD	w=6,x=T,y=5,z=4
22	wxS/3yz	w=1,x=5,y=D,z=4
23	wx2/y1z	w=5,x=S,y=T,z=4
24	4wx/2yz	w=1,x=T,y=S,z=5
25	T6w/xyz	w=4,x=2,y=1,z=5
26	Swx/yDz	w=5,x=1,y=4,z=3
27	wDx/yzS	w=3,x=4,y=1,z=5
28	wxy/5Sz	w=T,x=1,y=4,z=2
29	wSx/4yz	w=2,x=5,y=1,z=T
30	wxS/y5z	w=1,x=2,y=4,z=3
31	wxy/35z	w=S,x=2,y=1,z=4
32	wxy/T6z	w=2,x=1,y=5,z=4
33	wxD/yz1	w=5,x=4,y=6,z=T
34	1wx/yz5	w=T,x=6,y=D,z=4
35	wx3/y5z	w=4,x=D,y=S,z=1
36	6wx/y3z	w=4,x=1,y=D,z=5
37	5wx/4yz	w=1,x=2,y=6,z=T
38	wx4/Syz	w=3,x=5,y=2,z=1
39	w3D/xyz	w=5,x=1,y=4,z=6
40	w3x/6yz	w=D,x=5,y=4,z=1
41	wxy/z12	w=4,x=6,y=T,z=5
42	1wS/xyz	many
43	wxy/Dz5	many
44	3w4/xyz	many
45	wxy/5zD	many
46	wxy/Tz4	many
47	5wD/xyz	many
48	wDx/y5z	many
49	wxy/3z4	many
50	wxy/5z2	many
51	Dyz/S1x	none
52	w1z/xyS	none
53	15x/T6y	none
54	zy4/5x6	none
55	2xy/4Tz	none
56	xzS/y1w	none
57	Syx/4z5	none
58	xwS/Tzy	none
59	D5z/xwy	none
60	yxD/z35	none'''
for input in input_list.split('\n'):
  main(input.split('\t'))                  