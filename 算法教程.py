#2024算法教程
def search(l,r):
      mid = (l+r)//2
      if l>r:return 'MEIYOU!!!'
      if li[mid]==n:
        return mid
      else:
        if li[mid]>n:
          return search(l,mid-1)
        elif li[mid]<n:
          return search(mid+1,r)
#lie=[8,8,8,8,8,8,8,8,8,8,9,9,10,11,11]
lie=[1,1,1,1,2,3,4,8,8,8,8,8,8,8,8,8,8]
target=8
def search_end(l,r):
      mid = (l+r)//2
      if(l>r):return l-1
      if(lie[mid]==target):
            return search_end(mid+1,r)
      elif(lie[mid]>target):
            return search_end(l,mid-1)
def search_start(l,r):
      mid = (l+r)//2
      if(l>r):return r+1
      if(lie[mid]==target):
            return search_start(l,mid-1)
      elif(lie[mid]<target):
            return search_start(mid+1,r)
a=[0,2,2,15,88,59,11]
n=4
#r=search(0,5)
#print(r)
####今天不刷题，做个小游戏：好汉米诺塔####
def hnt(n,p,g):
    if p=='A' and g=='C' or p=='C' and g=='A':
        _g='B'
    if p=='B' and g=='C' or p=='C' and g=='B':
        _g='A'
    if p=='A' and g=='B' or p=='B' and g=='A':
        _g='C'
    #移走障碍物
    if n==1:
        print(p,"->",g)
        return
    hnt(n-1,p,_g)
    #移动自身
    print(p,"->",g)
    hnt(n-1,_g,g)
#hnt(5,'A','C')
def test(i):
    if i==1:
        return 1
    else:
         print(f"第{test(i-1)}层函数返回辣！！！")
         return i
#test(10)
def quicksort(l,r):
      if(l>r):return
      i,j=l,r
      base=a[l]
      while i!=j:
            #i,j谁先动？   假设i先动，那么，指针最后停止位置必然是i所在的位置。而i位置必定指大于base的数，故指针停止点必指向大于base的数。相当于将大于base的数放在左边。
            while a[j]>=base and i!=j: #加上i<j的目的：内while不会管外while(while的滞后性)
                  j-=1     
            while a[i]<=base and i!=j:
                  i+=1
            if(i<j):a[j],a[i]=a[i],a[j] 
      a[i],a[l]=a[l],a[i]
      quicksort(l,i-1)
      quicksort(i+1,r)
#quicksort(0,5)
def s():
    for i in range(0,10):
          if (i*10+3)*6528==(30+i)*8256:return i
#print(s())
def s2():
      total=0
      for i in range(0,10):
                      for j in range(0,10):
                              for k in range(0,10):
                                    for a in range(0,10):
                                          for b in range(0,10):
                                                for c in range(0,10):
                                                      for x in range(0,10):
                                                            for y in range(0,10):
                                                                  for z in range(0,10):
                                                                        book=[a,b,c,i,j,k,x,y,z]
                                                                        #print("total:",total)
                                                                        if i*100+j*10+k+a*100+b*10+c==x*100+y*10+c and len(list(set(book)))==len(book):
                                                                              total+=1
      return total/2
#print(s2())
def mat(m):
      ms=[6,2,5,5,4,5,6,3,7,6]
      result=0
      for i in range(111):
            for j in range(111):
                  for k in range(11111):
                        a,b,c=i,j,k
                        get=0
                        while i!=0:
                              get+=ms[i%10]
                              i//=10
                        while j!=0:
                              get+=ms[j%10]
                              j//=10
                        while k!=0:
                              get+=ms[k%10]
                              k//=10
                        if a+b==c and get==m-4:
                              result+=1
      return result
#print(mat(24))
m=[0,0,0]
v=0
#题目描述：对于输入的不重复数组，给出全排列的数组。
#笨法：失败（为什么？）
def A(n):
      global v
      for i in range(1,4):
            if i not in m:
                  m[n-1]=i
            else:
                  continue
            A(n-1)
            if n==1:
                  print(m)
                  v+=1
#other原创：三循环全排列算法（迭代法）！
def _1A(n):
      n=list(n)
      if len(n)==1:return n
      l=[[n[0],n[1]],[n[1],n[0]]]
      for i in n[2:]:
            for j in l[:]:#知识点解析：[:]写法
                  for k in range(len(j)+1):                        
                        m=j.copy()
                        m.insert(k,i)
                        l.append(m)
                  l.remove(j)
      return l
#递归法：
'''
最费脑子的一集
'''
l=[1,2,3,4]
t=len(l)
def _2A(L):
      if L==t:   #L永远不可能大于t，因为不可能拉起一个函数，使得L>=t
            print(l)
            #return
      for i in range(L,t):#隐含条件：L>=t时不会再拉起函数了,因此递归无需刻意地打断
            l[i],l[L]=l[L],l[i]
            _2A(L+1)
            l[i],l[L]=l[L],l[i]
#深度优先搜索：
n=4
boxes=[]
pads=[1,2,2,4]
used=[0,0,0,0]
def _3A(step):
      if step==n:
            print(boxes)
            return
      for t,i in enumerate(pads):
            #核心步骤之：尝试
            #if i in shoutou:
            if used[t] or (t>0 and pads[t-1]==pads[t] and not used[t-1]):
                  continue
            boxes.append(i)
            pads.remove(i)
            used[t]=1
            _3A(step+1)
            boxes.pop()#核心步骤之：拉起下一步
            pads.append(i)
            used[t]=0#注意还书
##深度优先法巧解三位数相加的那道题
answ = [0,0,0,0,0,0,0,0,0]
#shoutou=[1,2,3,4,5,6,7,8,9 ]
def dfs(step):
      if(step==9 and
      answ[0]*100+answ[1]*10+answ[2]+answ[3]*100+answ[4]*10+answ[5]==answ[6]*100+answ[7]*10+answ[8]):
            print(answ)
            return
      else:
            for i in range(1,10):
                  if i in shoutou:
                        answ[step]=i
                        shoutou.remove(i)
                        dfs(step+1)
                        shoutou.append(i)
            return
def flood():
      pass
ways='''..#.
...#
.#..
.#*.'''.split('\n')
ways=[[j for j in i] for i in ways]
done = []
def find(x,y,le):                                                            #当前应该怎么办？需要维护的变量?
      for pos in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if(3>=pos[0]>=0 and 3>=pos[1]>=0):
                  if ways[pos[0]][pos[1]]=="*":
                        print(pos,f"le={le-1}")
                  elif ways[pos[0]][pos[1]]=="." and pos not in done:
                        done.append(pos)
                        le+=1
                        find(pos[0],pos[1],le)
            else:continue
      return
done=[]
found=[(0,0)]
def wfs():                                                                  #wfs
      for i in found:
            for j in [(i[0]-1,i[1]),(i[0]+1,i[1]),(i[0],i[1]-1),(i[0],i[1]+1)]:
              if 3>=j[0]>=0 and 3>=j[1]>=0:
                  if ways[j[0]][j[1]]=='*':
                        print(j)
                        continue
                  elif ways[j[0]][j[1]]=="." and j not in found:
                        found.append(j)
dt='''#..#.
.J.J.
J#J.#
...#.
J..#.'''.split("\n")
dt = [[i for i in j] for j in dt]
print(dt)
def kill_jp():
      m=0
      for y1,i in enumerate(dt):
            for  x1,j in enumerate(i):
                  s=0
                  print("-")
                  if j==".":
                        x,y=x1,y1
                        while  x>=0:
                              if dt[x][y]=='#':break
                              if dt[x][y]=='J':s+=1
                              x-=1
                        x=x1
                        while x<5:
                              if dt[x][y]=='#':break
                              if dt[x][y]=='J':s+=1
                              x+=1
                        x=x1
                        while y>=0:
                              if dt[x][y]=='#':break
                              if dt[x][y]=='J':s+=1
                              y-=1
                        y=y1
                        while y<5:
                              if dt[x][y]=='#':break
                              if dt[x][y]=='J':s+=1
                              y+=1
                        y=y1
                  if s>m:
                        m=s
                        p=x,y
      print(m,p)
#shift/unshift push/pop
def uncode(l):
      r=[]
      while(len(l)>0):  
          r.append(l.pop(0))
          if(len(l)>0):           #while的滞后性导致需要再加一个if
              l.append(l.pop(0))
      return r
#栈思想与现代语言数组 ahaha ahha
def backstr(s):
      m=len(s)//2
      stack=[]
      for i in range(m):
            stack.append(s[i])
      if len(s)%2!=0:#分奇偶讨论
          for j in range(m+1,len(s)):
            if stack.pop()!=s[j]:          
                  return 'FALSE'
      else:
            for j in range(m,len(s)):
               if stack.pop()!=s[j]:
                  return 'FALSE'
      return 'TRUE'
l=[2,4,1,2,5,6]
r=[3,1,3,5,6,4]
#末尾
#先复习一下栈与队列的指令：
#栈：append/pop 队列：append/pop(0)
def pull_train(l,r):
      stack=[]
      n=l
      while (len(l)!=0 and len(r)!=0):
          stack.append(n.pop(0))
          if(stack[-1] in stack[:-1]):
             for i in stack[stack.index(stack[-1]):]:
                   n.insert(0,i)
             stack =stack[:stack.index(stack[-1])]
          n=r if n==l else l
      print(stack)
