# R1108 — 原CM首对数的模4513²除子读取与固定留数代数

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
**状态：已证明读取公式、整来源提升和有限算法；本篇尚未给出新的CM首对数数值。**

## 1. 要读的是同一条原曲线的实际对数

仍取原 $Y=X_{\mathrm{ns}}^+(47)$，$J=\operatorname{Jac}(Y)$，
$q=4513$，$R=\mathbf Z/q^2\mathbf Z$，
$\mathcal L=\Omega_Y^1(C_\infty)$，$d=167$、$g=73$。
原好模型、95个logarithmic sections、73维Hodge核及
$V_n=H^0(\mathcal L^n)$、$n\le5$ 均沿R1090、R1104。
本篇的所有提升发生在这个模型内。

设$D$是实际整模型上的度零除子，
特别可以取
$$
u_y=23y-C_\infty
$$
的真实除子。R1089已经认证
$$
N=\#J(\mathbf F_q),\qquad N\bmod q=551.
$$
所以$[N]D$落入原形式核，且
$$
\lambda_D(\omega)=q^{-1}\log_J[D](\omega)\pmod q
$$
可以从$R$上的除子运算准确读取。
这里只需模$q^2$；没有把约化点类直接冒称为首对数。

主要公式见(1108.9)。
其中包括一个必须执行的终点归一：
$N[D]=0$在剩余Jacobian上只给线性等价，
不意味着Miller链的末端有效除子等于固定基除子。

## 2. 一个固定的约化、无重数基除子

R1104的前两原section $s_0,s_1$ 无共同零，
给可分degree167的映射 $\pi=[s_0:s_1]:Y\to\mathbf P^1$。
选择
$$
f_0=s_0+c s_1,\qquad f_1=s_1,\qquad D_0=\operatorname{div}f_0
$$
使$D_0$避开全部23cusps和八个原CM点，且$D_0$约化。

这种$c\in\mathbf F_q$存在：可分degree167小于$q$，
因此所有ramification tame；Riemann–Hurwitz给ramification degree
$2g-2+2d=478$。至少只排除478个分支值，
上述31个指定几何点另外最多排除31个常数。
$478+31<4513$，故有可用$c$。
实际实现逐个检验所选$c$，不只使用存在性。

### 2.1 原836-jets中的Wronskian

在标准cusp的原标架
$\ell=47\,dt/t$下写$f_i=F_i\ell$。
对原section pencil，真正Wronskian是
$$
W=f_1\,df_0-f_0\,df_1\in H^0(\Omega^1\mathcal L^2).
$$
式中局部标架导数相消。经自然包含
$\Omega^1\mathcal L^2\hookrightarrow\mathcal L^3$，
它的原系数为
$$
W_0=\frac{t}{47}(F_0'F_1-F_0F_1').
\tag{1108.1}
$$
这由原836项的乘法和$t\,d/dt$直接取得；
乘$t$使读取第835系数不要求第836系数。
所得全局section仍由同一注入jet空间确定。

在$D_0$上$f_1$为单位。原cusps已避开，
自然包含$\Omega^1\hookrightarrow\mathcal L$在这里是同构。
令
$$
A=H^0(D_0,\mathcal O_{D_0}),\qquad
w=W/f_1^3\in A.
$$
若 $z=f_0/f_1$，则准确有
$$
w=dz/f_1\quad\text{于 }D_0.
\tag{1108.2}
$$
所以$w$为单位当且仅当$z$在全部$D_0$点为简单参数，
也就是$D_0$约化。实际unit检验同时支付有限étale性。

### 2.2 完整有限留数代数的原RR表示

因为$H^1(\mathcal L)=0$，限制序列给
$$
A\simeq V_2/(f_0V_1),\qquad \dim A=262-95=167,
\tag{1108.3}
$$
这里用$f_1^2$平凡化纤维。
乘法只需$V_4/(f_0V_3)$：
先乘两个$V_2$代表，再用乘$f_1^2$的同构搬回(3)。
这个同构成立是因为$f_1$在$D_0$无零，
而对应两侧都由完整限制序列识别为同一个$A$。

$w$从$V_3/(f_0V_2)$读出，再通过乘$f_1$接回(3)。
对原holomorphic微分$\omega_i=G_i\ell$，
$G_i/f_1$通过$G_if_1\in V_2$读入同一$A$。
所有操作至多用$V_4$，未要求一个新的平面模型。

可以选择一个实际元素$a\in A$，构造其乘法矩阵，
核特征多项式$F$平方自由且
$[1,a,\ldots,a^{166}]$可逆，再转成
$A\simeq\mathbf F_q[X]/F$。
这样迹由$F$的Newton identities或实际乘法矩阵读出。
这只是一个实际核过的计算表示；不预设某个低次section必为primitive。
即使不选primitive元素，(3)的有限代数和其trace仍完整定义。

## 3. 原格的模q²提升，没有任意搬用特征零系数

### 3.1 原95源和全部级数

把原primitive47次根 $2\bmod q$ Hensel提升到$R$中唯一
$\zeta^{47}=1$、$\zeta\equiv2\bmod q$ 的根。
R1090的weight-one/完整两phase Reynolds式在$47$及其群阶可逆的原好模型上整，
所以同一95描述子、同一Tate参数和同一$\zeta$给$R$上真实sections。
这里不是把任意有限域坐标整数代表当成新的global形式。

R1104每级已经固定的产品索引在$R$上照原式提升。
$H^1(\mathcal L^n)=0$、$n\ge1$，
使各$V_n$自由且base change成立。
其模$q$基已认证，因此Nakayama保证这些实际提升仍为$R$基。
若需要holomorphic提升，必须解全部23个真实留数的整核，
使用原unit22 minor；任意整数lift的旧73行不自动holomorphic。

836项仍在$R$上注入：
若section的836项为零，先模$q$用负degree除子界得section模$q$为零；
于是section为$q$乘另一个整section。
再对后者的模$q$应用同一界，得到原section为$q^2$倍，即零。
因此模平方的全局乘法与等式仍由原有限jet准确检测。

### 3.2 unit-pivot线性代数

所有后继RR空间的预定rank由原相对Riemann–Roch确定。
实际运算先在模$q$上选择unit minor，然后在$R$上解。
若$\bar B=\bar A^{-1}$，任取矩阵lift $B_0$，则
$$
B=B_0(2I-AB_0)
\tag{1108.4}
$$
是模$q^2$的真逆，直接核$AB=BA=I$。
矩形像/核也沿同一unit minor计算，并核全部余下列的关系。
不从“mod$q$ rank正确”单独推一个任意矩阵在$R$上平坦；
这里平坦性来自真实除子空间的degree和$H^1=0$，
完整关系另逐项核实。

[原有限Miller方法](../notes/2026-11-27-full-p47-finite-third-kind-method.md)
的degree167 AddFlip、初始closed-point校正及全部colon
除子恒等式因此可在$R$上使用；实现的线性代数须改用上述unit-pivot，
不能直接把有限域rank/kernel函数搬到非域$R$。
每个选中section模$q$避开所需点就保证在$R$上为单位；
residual-gcd在special fiber无交，亦保证相对colon没有额外基点。
所有乘法至多$V_5$，不增长到$N$倍的大除子空间。

特别，在$R$上实现两个无基点pencil条件时，必须直接取
$
\{s:s\,s_0\in Z,\ s\,s_1\in Z\}
$
的同时核；它由上述相对Riemann–Roch保证平坦。
单个pencil条件的中间space可能因special-fiber交点跳维，
不应在尚未支付平坦性时先单独提升再取第二次colon。
对试选section的residual-gcd也先在模$q$检验最小维数；
有额外gcd则换section，不能假该跳维空间已经平坦。

## 4. 末端的必要有效除子归一

在$R$上按实际 signed 链求得
$$
[E_N-D_0]=\epsilon N[D],\qquad \epsilon\in\{\pm1\}.
$$
模$q$只能推出$\bar E_N\sim D_0$。
先用原pencil/colon求一维
$H^0(\mathcal L(-\bar E_N))$，
取$\bar h$，于是$\operatorname{div}\bar h=\bar E_N$。

把该代表与**真正的零点代表**$D_0$作一次AddFlip。
其space
$$
U_R=H^0(\mathcal L^3(-E_N-D_0))
$$
自由rank95，base change完整。
强制选择两截面，其模$q$准确为
$$
\bar s=\bar h\,\bar f_0^2,\qquad
\bar u=\bar h\,\bar f_0\bar f_1.
\tag{1108.5}
$$
它们属于$U_R$的约化；用已证unit坐标提升到真正的$U_R$。
模$q$去掉共同固定部分$\bar E_N+D_0$后，
两residual除子分别是$D_0$和$D_1=\operatorname{div}f_1$。
原pencil无基点，故residual gcd确为零；
原colon严格读出新的有效度167除子$E'$，并有
$$
\bar E'=D_0,\qquad [E'-D_0]=-\epsilon N[D].
\tag{1108.6}
$$
这一步不能被省略为“末端点类已中性”。
$\bar E_N$有无重数均不影响(5)，因为强制residual仍是已经选定的约化$D_0$。

## 5. 从真正相同的约化除子读取形式对数

现在$W_{E'}=H^0(\mathcal L^2(-E'))$自由rank95，
其模$q$恰为$f_0V_1$。
选择实际$h_{E'}\in W_{E'}$，强制
$$
h_{E'}\equiv f_0f_1\pmod q,\qquad
\delta h=(h_{E'}-f_0f_1)/q\bmod q\in V_2 .
$$
差在真实$V_2(R)$基中逐坐标被$q$整除，故$\delta h$定义明确。
记
$$
\delta=(\delta h)/f_1^2\in A,\qquad
r_i=(G_i/f_1)\,w^{-1}\in A.
\tag{1108.7}
$$

### 定理：原第一层Abel对数的有限trace式

准确有
$$
q^{-1}\log_J[E'-D_0](\omega_i)
   =-\operatorname{Tr}_{A/\mathbf F_q}(\delta r_i)\pmod q .
\tag{1108.8}
$$
因此，保留(1108.6)的符号，
$$
\boxed{\quad
\lambda_D(\omega_i)
 =\frac{\operatorname{Tr}_{A/\mathbf F_q}(\delta r_i)}
        {\epsilon N}\pmod q.
\quad}
\tag{1108.9}
$$

**证明。**
在$D_0$的每个几何点，$z=f_0/f_1$是简单参数；
$h_{E'}/f_1^2=z+q\delta+O(q^2)$。
同一分支上的$E'$点因此具有位移
$z(E')=-q\delta$。
又由(1108.2)，
$$
\omega_i/dz=(G_i/f_1)w^{-1}=r_i.
$$
对应的Abel积分首项是$-q\delta r_i$。
好约化形式群的log在线性层与微分配对一致；
对整微分积分，次数$n$的分母至多贡献$n$；
$n-v_q(n)\ge2$（$n\ge2,q>2$）使所有二次及以上项在$q^2$中，
故除$q$后正得到每个几何分支的$-\delta r_i$。
把完整未分歧共轭分支求和就是有限étale代数$A$的trace，
证明(8)。再用(6)除$-\epsilon N$，得到(9)的**正号**。

若改变$h_{E'}$但保相同$E'$及规定的模$q$值，
$\delta h$之差来自$W_{D_0}=f_0V_1$，在$A$中为零。
所以读数不依section提升的选择。
基$pencil$、有限代数表示或primitive元素的改变也不改(8)：
右边已经等于同一个原Abel积分。
这里既没有删$N$、$\epsilon$，也没有把$u_y$中的23遗漏。证毕。

## 6. 原47挠点的有限模平方提升

为了在$R$上评价原sections，只需提升已认证的实际CM模型和47挠点。
取旧field modulus的任意系数lift，
$$
R_f=R[\theta]/\widetilde F(\theta),
$$
其中$\widetilde F\bmod q$是旧实际不可约多项式。
其导数mod$q$可逆，故这是同一个未分歧扩张的模平方整数环。

### 6.1 Frobenius与primitive根必须真的提升

$\theta\mapsto\theta^q$在$R_f$上一般**不是**所需ring automorphism。
应先把$\bar\theta^q$任意lift到$r$，再作一次Hensel：
$$
\theta^{(\sigma)}=r-\widetilde F(r)/\widetilde F'(r).
$$
把$\theta$送到这个根定义真正的未分歧Frobenius lift。
实际核$\widetilde F(\theta^{(\sigma)})=0$和$\sigma^f=1$。
同样$\zeta_{47}$用$x^{47}-1$的真实Hensel根，
不把整数2直接当模$q^2$的47次根。

本篇的CM模型采用同一有理$j$的原短模型在$R$中的值；
Gaussian保$A=343,B=0$，cubic保$A=0,B=1$。
generic模型的分母$1728-j$在$q$为单位。
因此提升的$j$是给定有理CM $j$的真实模平方值。

### 6.2 每个非零47挠点的一步精确修正

旧点$\bar P=(\bar x,\bar y)$不是二挠点，$\bar y\ne0$。
任意lift$x$后，先用$2y$为单位的一步Hensel使
$P=(x,y)$落在真实$R_f$曲线上。

沿旧 $1,2,4,5,10,11,22,23,46$ 链计算
$P_{46}=(x_{46},y_{46})$。
每个中间斜率分母mod$q$非零；
最后$P_{46}\equiv-P$。令
$$
s=\frac{x_{46}-x}{y_{46}-y}\in qR_f,\qquad \tau=-s/47.
$$
在形式参数$T=-x/y$中，最后相加的逆斜率展开给
$T([47]P)=s\bmod q^2$。
平移一个形式参数为$\tau$的点，精确到模平方为
$$
\boxed{\quad
P^\sharp=(x+2y\tau,\ y+(3x^2+A)\tau).
\quad}
\tag{1108.10}
$$
因为$\omega_E=dx/(2y)$在无穷远的首项为$dT$，
该平移将$[47]P$的形式参数改为$s+47\tau=0$。
故$[47]P^\sharp=O$，且$P^\sharp$是旧点的唯一47挠提升。
全过程只除unit，未在最后的近竖直斜率上除$q$。

实际实现还直接核曲线方程、$[46]P^\sharp=-P^\sharp$，
并按真实Frobenius矩阵与原Cartan标记核提升。
其余2208个点由该基按同一加法重建。
原Eisenstein值仍用同一47斜率链，所以权、Weil/根和Reynolds来源均保持。

## 7. 八个CM类只需四个基本输入

原八点按CM判别式记为$u_{-3},u_{-4},u_{-7},u_{-8},
u_{-12},u_{-16},u_{-27},u_{-28}$，均使用$23y-C_\infty$的同一尺度。
原完整Hecke cycles给
$$
\begin{aligned}
T_2u_{-4}&=u_{-4}+2u_{-16},\\
T_2u_{-3}&=3u_{-12},\\
T_3u_{-3}&=u_{-3}+3u_{-27},\\
T_2u_{-7}&=2u_{-7}+u_{-28}.
\end{aligned}
\tag{1108.11}
$$
第一式已由R1096付款；其余三式的完整理由如下。

对最大CM序$\mathcal O$，$\ell$-isogeny的kernel是
$\mathcal O/\ell\mathcal O$这二维$\mathbf F_\ell$空间中的一条线。
稳定于整$\mathcal O$的线数在split/ramified/inert时为2/1/0。
非稳定线的稳定子恰是标量子代数：
任何非标量元素都生成二维代数，否则该线本来就是$\mathcal O$稳定。
因此下降目标的endomorphism序正是$\mathbf Z+\ell\mathcal O$。

$\ell=2$在$-3$域惰性，故三条kernel全下降到判别式$-12$；
$\ell=3$在$-3$域分歧，给一条水平和三条$-27$下降；
$\ell=2$在$-7$域分裂，给两条水平和一条$-28$下降。
相应CM序都class number one：reduced primitive正定二元型，
按$|b|\le a\le c$及$a\le\sqrt{|D|/3}$逐项列出，
分别唯一为
$$
(1,1,1),\ (1,0,1),\ (1,1,2),\ (1,0,2),\
(1,0,3),\ (1,0,4),\ (1,1,7),\ (1,0,7)
$$
（按上述八个判别式顺序）。
所以各类全部kernel目标均是原对应的那个CM $j$。
$\ell=2,3$与47互素，isogeny运输
$\mathcal O\otimes\mathbf F_{47}$确定的canonical Cartan，
故目标还是原指定necklace。
原coarse Hecke cycle按全部kernel数保multiplicity；
不再除以CM自同构阶。

另外$T_\ell C_\infty=(\ell+1)C_\infty$，
由原23cusps的Galois单轨道及Hecke总degree取得。
因此点cycle关系准确成为(11)的同一degree-zero类关系。

所以只需实际读取四个基本类的73维首log：
$-3,-4,-7,-8$。
其它四列从原$T_2,T_3$矩阵按(11)取得，分母2、3为$q$单位。
这些关系提供完整八列；它们本身不宣称任何新log值非零。

## 8. 后继执行与范围

实现须输出真实模平方源、unit-pivot、$D_0$ étale、
末端归一和(1108.9)的实际回执，再将所得列放入R1103的原QC系数。
数值尚未执行时，本篇只登记完整公式和有限源；
不能把“有算法”写成八盘唯一性。

原全局高度沿R1102、角作用沿R1106、八coarse来源沿R1105。
本篇给它们缺少的同一原CM类坐标读取，不更换对象或周期。
全$p$的Serre完成标准仍未达到，后继继续实际数值与一般$p$的原障碍。
