# R364：真实局部角商与五行有限频率根支付完整 P–Z 对称乘积

日期：2026-11-15。**完整有限纸面构造；没有运行求积、符号程序、参数扫描、人工测试或研究计算。**

[R361](R361-even-weak-circles-and-three-oscillation-shapes-pay-the-negative-three-square.md) 已在 R360 的同一全偶弱圆构造线上支付完整 $P^2$ 与 $PW$ 对称乘积。本稿处理 $PZ$ 的最后一个外矩。这里有两个不同问题：原 $\theta=\pi/2$ 值含真正的三阶平方，而另外一个完整角系数是有真实系数的局部 $C^2$ 四次量。只扩充高频主锥不能支付后者。

本稿先从原两次右积分和合法复矩推导那个准确角商，再以 R357 两个实际母形自由度和 R359 同权商共同构造五维低层正锥。在同一个最终弱圆上保全部18面积并清此角商后，原成对反射控制器可升级成五行有限频率精确根。最终 $PZ$ 的三条完整外矩、全部相位同时为零，原 $P^2,PW$、$\Psi$ 与三条 directed 行均保持。

来源：
[R267](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、
[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)、
[R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、
[R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)、
[R325](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)、
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)、
[R357](R357-genuine-mother-fibers-and-a-three-dimensional-ordered-profile-cone.md)、
[R359](R359-exact-same-weight-quotient-and-four-dimensional-cone-pay-the-Gaussian-PY-zero-moment.md)、
[R360](R360-complete-positive-negative-second-self-and-six-dimensional-middle-cone.md)及 R361。

## 1. 同一个弱圆、实际门与规范

固定原小共振参数
$$
0<\kappa^2<1/100,\qquad \kappa>0,\qquad
\varepsilon=\kappa^2/4.
$$
原基本算子及 Gaussian 组合仍为
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2},
$$
$$
W=aR+bS,\qquad Z=dL+eU.
$$
$a,b,d,e$ 是 R359 的同一实际系数；尤其
$$
a\ne0,\quad e\ne0,\quad d\ne0,\quad
d+e=\frac{\kappa(9\kappa^2-1)}{4h_e}\ne0,\quad
d+7e=-\frac{\kappa(81\kappa^2+7)}{4h_e}\ne0.
\tag{1}
$$

设
$$
\phi=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-\phi\odot\phi.
$$
$f,g$ 为实际全偶实紧函数；保原三矩圆、弱单 hook、完整第二／第三 range 和真实 derivative rank-two 核。没有将第二 hook 加成一般条件。

继续使用 normalized 对称外矩
$$
\mathcal Q_{XY,j}
=-I_j(XD,YD)+I_j\{\phi,X(\phi,YD)+Y(\phi,XD)\}.
\tag{2}
$$
$X\ne Y$ 的原 history 系数另有非零常数与因子2；本稿保(2)的准确规范。$I_2$ 始终包含 $2u'v'$。

全部18反对称面积和 R361 所用 $\Psi,F_0,F_1,F_2$ 是必须共同保留的旧条件。本稿从 R360 最后控制器以前、全部18面积为零且 $\Psi<0$ 的实际入口重新选择末控制器；不假设任意冻结母函数都 regular，也不继承另一条几何的 whole-pure、whole-self、Morse 或全部 period。

## 2. 额外角系数必须先准确辨出

R294 的四次槽代数适用于一般 $f,g$，不要求在弱核心内 rank-one。记
$$
\mathcal B_j(A,B)=\frac12\{I_j(XA,YB)+I_j(YA,XB)\},
$$
$$
\mathcal C_j(u^2,B)
=I_j\{u,X(u,YB)+Y(u,XB)\},\qquad
\mathcal K_j=\mathcal B_j+\mathcal C_j,
$$
第二式对 outer 二次槽作真实极化。原十二完整副本清掉 angular odd 系数后，
$$
\mathcal Q_{XY,j}(\theta)
=\sin^2\theta\,\mathcal Q_{XY,j}(\pi/2)
+\sin^2\theta\cos^2\theta\,\Xi_{XY,j},
\tag{3}
$$
$$
\Xi_{XY,j}
=\mathcal K_j(f^2-g^2,f^2-g^2)-4\mathcal K_j(fg,fg).
$$
若 $q=f+ig$，这准确等于
$$
\Xi_{XY,j}=\operatorname{Re}K_{XY,j}(q),
$$
$$
K_{XY,j}(q)
=I_j(Xq^2,Yq^2)
+I_j\{q,X(q,Yq^2)+Y(q,Xq^2)\}.
\tag{4}
$$
这里复记号只是原实四次多项式的极化；没有换 seed 或删 whole mixed 项。

原三矩圆给三个复双线性矩
$$
I_j(q,q)=0,\qquad j=0,1,2.
\tag{5}
$$
因此原 $Pq^2,Lq^2,Uq^2,Yq^2$ 的全部左尾确实为零。这个紧性来自整个 $q$ 的三矩，不适用于各个单微包。

再记
$$
S_{XY,j}(q)=2I_j\{q,[X,Y](q;q^2)\}.
$$
全部相位的面积为零迫 $S_{XY,j}(q)=0$：原面积角多项式的 $e^{-4i\theta}$ 系数是同一 self 的固定非零倍数，不能被其二次角项抵消。特别，本稿随后使用
$$
S_{PY,0}(q)=0,\qquad S_{PZ,2}(q)=0.
\tag{6}
$$
这只从当前已付的18个完整面积提取，不增设额外 pure 假设。

## 3. 从原 Φ 二导求完整 P–Z self

本节先对任意满足(5)的紧复函数 $q$ 计算。写
$$
v=q',\quad r=q'',\quad
P_q=J(r^2),\quad S_q=J(xr^2),
$$
$$
C_2=\int x^2r^4,\quad
N=\int xvr^3,\quad
V_2=\int v^2r^2,\quad
U_3=\int qr^3,\quad A_2=\int P_q^2.
\tag{7}
$$
所有积分和配对均为双线性，不取复共轭。

原 cubic 密度准确为
$$
F_{P,2}(q):=I_2(q,Pq^2)
=\int\left(\frac43xr^3-2vr^2\right).
$$
故对真实紧方向 $w$，
$$
DF_{P,2}(q)[w]
=\int\{4r(xr-v)w''-2r^2w'\}.
\tag{8}
$$
本节的 $Lq^2,Uq^2$ 因(5)真紧，所以这里是合法变分；没有沿一个带尾的 formal 方向偷用只对紧域成立的公式。

原完整导数为
$$
\begin{aligned}
(Lq^2)'&=(q-xv)r-\frac{xP_q}{2},\\
(Lq^2)''&=(q-xv)r'-\frac{xr^2+P_q}{2},\\
(Uq^2)'&=2xvr+S_q-\frac32x^2r^2,\\
(Uq^2)''&=(2xv-3x^2r)r'+2vr-2xr^2.
\end{aligned}
\tag{9}
$$
代(8)，只在整个合法复函数上 IBP。其中两个线性三导项准确为
$$
\int4r(xr-v)(q-xv)r'
=\frac43C_2-\frac83N+\frac23U_3,
$$
$$
\int4r(xr-v)(2xv-3x^2r)r'
=\frac73C_2-\frac{16}3N+4V_2.
$$
将它们与(9)的其余完整项合并，得到
$$
\boxed{
D_L:=DF_{P,2}[Lq^2]
=-\frac23C_2+\frac43N-\frac43U_3+V_2-\frac12A_2,
}
\tag{10}
$$
$$
\boxed{
D_U:=DF_{P,2}[Uq^2]
=-\frac83C_2+\frac{20}3N-4V_2+A_2.
}
\tag{11}
$$

为明确原 primitive 的端项，(10)中的中间项是
$\int P_q(2vr-xr^2)$。
原右锚与(5)准确给
$$
\int2P_qvr=\int v^2r^2,\qquad
-\int xP_qr^2=-\frac12\int P_q^2.
$$
(11)中的剩余项为 $-2\int S_qr^2$，而
$$
\int S_qr^2=-\frac12\int P_q^2.
$$
最后两式都先保 $[xP_q^2]$ 或 $[S_qP_q]$，再用整个复矩零消去。没有将 nonlegal 单包的端常数直接置零。

由合法 cubic 变分，
$$
K_{PZ,2}(q)
=\frac12\{DF_{P,2}[Zq^2]+DF_{Z,2}[Pq^2]\}.
$$
两项之差恰为 $S_{PZ,2}$。所以在(6)下
$$
K_{PZ,2}(q)=dD_L+eD_U.
\tag{12}
$$

## 4. 两个已付面积准确消去非局部 primitive

原 P–Y 第零 self（R257/R359 的同一规范）为
$$
S_{PY,0}
=-C_2+\frac83N-V_2-\frac43U_3-\frac12A_2.
\tag{13}
$$
原 R267 两个真实三次导数给
$$
[P,L](q;q^2)'=\frac{x r^3}{3},
$$
$$
[P,U](q;q^2)'
=-2vr^2+\frac73xr^3-\frac23J(r^3).
$$
把它们代入完整 $I_2$ 两项，得到
$$
S_{PZ,2}
=-\frac56(d+7e)C_2+\frac43(d+11e)N
-8eV_2-\frac83eU_3.
\tag{14}
$$
例如 $\int vJ(r^3)=\int qr^3$ 使用的是紧 outer $q$，不是要求 $J(r^3)$ 左尾为零。

定义两个真实局部四次量
$$
\mathfrak j(q)=3V_2+U_3-2N,\qquad
\mathfrak k(q)=V_2-\frac25N.
\tag{15}
$$
它们分别就是 R357 母函数上的 $\mathcal J,\mathcal K$，不是 R325 弱核中另一个带 $\theta$ 的 $\mathcal J_\theta$。

由(14)及 $S_{PZ,2}=0$，
$$
C_2=\frac85N-\frac{16e}{5(d+7e)}\mathfrak j.
\tag{16}
$$
先用(13)消 $A_2$，再用(16)及
$$
V_2=\mathfrak k+\frac25N,\qquad
U_3=\mathfrak j-3\mathfrak k+\frac45N,
$$
(10)—(12)准确化为
$$
K_{PZ,2}
=(d-2e)S_{PY,0}
+2(d+e)\left\{\mathfrak k-\rho_\kappa\mathfrak j\right\},
\qquad
\rho_\kappa=\frac{28e}{15(d+7e)}.
\tag{17}
$$
$N$ 的系数准确为零；不是小宽度近似。

于是，对当前全部18面积为零的真实弱圆，
$$
\boxed{
\Xi_{PZ,2}=2(d+e)\,\mathcal T(f,g),\qquad
\mathcal T(f,g)=
\operatorname{Re}\{\mathfrak k(f+ig)-\rho_\kappa\mathfrak j(f+ig)\}.
}
\tag{18}
$$
这是完整额外角项，包含由原 true tail 产生的全部项。
$\mathcal T$ 是局部、四次、连续的 $C^2$ 泛函；它不含未知 Volterra 余量。
但(18)没有说它已由18面积推出零，下面确实另行支付它。

## 5. 新同权低层的两个真实形状方向

继续使用 R359 的四行
$$
(\mathcal B_{1,p},\mathcal B_{1,04},
\mathcal P_{0,p},\mathcal P_{0,04}),
$$
并增加第五行 $\mathcal T$。前四行仍采用原 $2I$ 的 even 系数；第五行使用(18)的规范，不混淆两个非零因子。

R357 的每个真实普通／伴随原型，全部细原子、宽度和原四次幅权保留。对它的同一个实际偶母 $u$，精确有
$$
\mathcal T
=W_{\rm act}\{\mathcal K(u)-\rho_\kappa\mathcal J(u)\}.
\tag{19}
$$
原因不是把伴随 profile 假成一条整体比例：在其最细、取值本身不交的原子上，伴随只改变整原子的符号。因此每个局部四次密度的实部都乘同一个
$\operatorname{Re}(a_i+ib_i)^4$；所有原值、导数及宽常量过渡一并包含。
对真实宽度 $w$ 的
$\eta_{w,\xi}=w^{3/2}u((x-\xi)/w)$，
三个局部量 $V_2,U_3,N$ 在偶母上都准确乘 $w$。
$N$ 的中心项是 $\xi\int u'u''{}^3=0$，所以没有漏 center。
于是(19)的 $W_{\rm act}$ 正是 R359(10)—(11)的真实权，而非新任选参数。

该原型同时有准确同权商
$$
\ell:=\mathcal B_{1,p}+k_G\mathcal P_{0,p}
=W_{\rm act}\left(R_J\mathcal J-\frac G2\mathcal K\right),
\qquad k_G=\frac{db}{2}-ea,
\tag{20}
$$
$$
G=d(3a-b)+2ae>0,
$$
$$
R_J=
\frac{5d^2(a-b)+de(47a-19b)+4e^2(12a-5b)}
{15(d+7e)}.
$$
(19)、(20)使用同一个 $u$ 和同一个 $W_{\rm act}$。

R359 已证明所有本稿使用的有限原型均有
$$
W_{\rm act}
=\mathcal W\delta\,n(1-q_w^2)(H^2-6H+1)>0,
\tag{21}
$$
包括两斜率及第三斜率 gap 原型；$q_w$ 是真实宽度比，不是复函数 $q$。
ordinary 和 companion 的四次实数据相同。这里保留全部 copy 权 $\mathcal W$、真实主宽 $\delta$ 与母形导致的方差修正。

两形 quotient 的 determinant 不是假设：
$$
\boxed{
R_J-\frac{G\rho_\kappa}{2}
=\frac{(a-b)(d^2+de+4e^2)}{3(d+7e)}\ne0.
}
\tag{22}
$$
因为 $a-b\ne0$、$d+7e\ne0$，且
$d^2+de+4e^2=(d+e/2)^2+15e^2/4>0$。
这正是同时保旧同权商并调新角商需要的独立性。

## 6. 十个实际列给低五维全正锥

先取 R357 的六个真实共同锥列，令实际母
$\mathcal J=\mathcal K=0$。
它们的 $(Q,S,V)$ 严格正锥是 $\mathbb R^3$。
由 R359 原 common 式，前四行是
$$
(-k_GQ,-k_G(S+V),Q,S),
$$
第五行 $\mathcal T=0$。
故这六列给
$$
\ker\ell\cap\ker\mathcal T\subset\mathbb R^5
$$
的完整正锥及严格正 kernel；这是一个真正三维空间。

在 R357 同一个真实有限母宽和局部纤维内，再取四个小非零形状值
$$
(\mathcal J,\mathcal K)
=(\pm h\eta,0),\qquad (0,\pm h\eta),
\tag{23}
$$
其中 $\eta>0$ 足够小。R357 的正则母构造确实实现这些数值，不将它们当作自由积分常数。
每个新列都完成原三矩／方差回补、有限 gap、八／十二副本及原 $\mathcal F_\kappa=0$；
不重加此前未要求的旧能量根。

在商坐标 $(\ell,\mathcal T)$ 中，(19)—(23)给两对严格反向射线；每列自己的正 $W_{\rm act}$ 只改变长度。
由(22)，它们张成 $\mathbb R^2$，有严格正四列 balance。
先取这个正 balance，再用前六列的三维正锥消去其剩余三个实际坐标，最后加前六列的严格正 kernel，得到全部十列严格正 kernel。因商秩2、核内秩3，遂有
$$
\boxed{
L_5:\ (\mathcal B_1,\mathcal P_0,\mathcal T),\qquad
\operatorname{rank}L_5=5,\quad
\ker L_5\cap\mathbb R^{10}_{>0}\ne\varnothing,\quad
\operatorname{cone}_+(L_5)=\mathbb R^5.
}
\tag{24}
$$

四个小形状值可选在一次紧参数邻域内；R357 已付的有限 $n,A,N$、严格 gap 和容量选择对该邻域统一使用，随后取实际有限正 $\delta$。
没有另作 $n$ 与容量尺度相互依赖的极限。
所有中心、内部原子和 copy 权先固定，再读取十个真实列。

这五行对本类完整原型共同平移不变。旧四行由 R359 给出；新行由(19)和偶母的中心项为零给出。
对每列加其完整空间镜像，五个目标都为反射偶，列共同乘2，(24)保持。
M/A 三外矩及其余旧 reflection-odd 外矩继续逐列为零。
每列的真实 $\Psi$ 成本仍为有限正数。

## 7. 接回全部18面积：十三行、二十六列

不能为支付 $\mathcal T$ 重开旧同权 $\mathcal B_1$ 或 $\mathcal P_0$。
继续采用 R360 的真实 middle 六行十二列
$$
M_6:\quad(\mathcal D_1,\mathcal C_0,\mathcal P_2)
$$
及 R349 的 $\mathcal C_2$ 两行四列。
所有列取完整镜像，逐列原尾及所有真实旧成本保留。

本稿新行 $\mathcal T$ 的完整伸缩权恰为 $-5$：
$V_2,U_3$ 的每项都是六次导数加一次积分，$xvr^3$ 亦给同一权。
它不是 principal 权。所以准确权表为
$$
(\mathcal B_1,\mathcal P_0,\mathcal T):-5,\qquad
(\mathcal D_1,\mathcal C_0,\mathcal P_2):-3,\qquad
\mathcal C_2:-1,\qquad \Psi:-7.
\tag{25}
$$
$P_2,C_2$ 的原 $I_2$ 两项均已计入这些权。

先把十二个 middle 列整体伸缩 $H$、第四幅权乘 $H^3$。
在五低行／六中行的分块下，真实矩阵趋于
$$
\begin{pmatrix}L_5&0\\ D_6&M_6\end{pmatrix}.
$$
两个对角块都为全正锥，故极限满秩11且有全部分量严格正 kernel。
固定一个真非零 minor，取足够大但有限的 $H$，其性质保持。
这里 $D_6$ 以及低列的 $\mathcal C_2$ 成本全部保留；后者不是小量。

再对四个高列作另一个有限伸缩 $H_2$、第四幅权乘 $H_2$。
低行按 $H_2^{-4}$、中行按 $H_2^{-2}$ 趋零，高两行保其实际二维正锥。
同一正核／minor 开性给
$$
\boxed{
L_{13}:\quad
(\mathcal B_1,\mathcal P_0,\mathcal T;\
 \mathcal D_1,\mathcal C_0,\mathcal P_2;\
 \mathcal C_2),
\quad
\operatorname{rank}L_{13}=13,\quad
\ker L_{13}\cap\mathbb R^{26}_{>0}\ne\varnothing .
}
\tag{26}
$$
列数为 $10+12+4=26$。这个13是该具体实际矩阵的行秩，不是把所有未付函数位置当成独立秩。

现在取 R360 最后控制器以前的偶弱基线：全部18面积为零，
$\Psi=-\Delta\sin^2\theta$、$\Delta>0$。
其原弱幂段、局部常量、宽 cutoff、补矩及全部最终中心都固定。
设其实际 $\mathcal T$ 值为 $t_*$。

用(26)选一个固定严格正向量 $c$，使旧十二面积行的增量为零、新 $\mathcal T$ 行为 $-t_*$。
把26个真实列共同伸缩 $S$、第四幅权取 $S^5c_i$。
由(25)，五低行保持原增量，中、高行只是乘 $S^2,S^4$ 的准确零。
因此
$$
\boxed{\text{全部18面积保持零},\qquad \mathcal T_{\rm total}=0.}
\tag{27}
$$
新增 $\Psi$ 成本准确为 $S^{-2}\sum_i c_i\psi_i$。
选一个足够大但有限 $S$，令它小于 $\Delta/2$，并使新正负包络与原弱基线不交。
旧中心不移动，所有原 copy 的内方差及低项仍为实际值。

$\mathcal T$ 是局部量，跨完整块直接相加。
原面积的跨完整块加法则继续用 R325 的真尾证明：
每个完整 $D$ 三矩零，inner 输出真紧；同块嵌套输出的二次左尾与另一紧 outer 的完整三个 $I_j$ 准确正交。
没有将微包自身冒作三矩零。

## 8. 从起点显式保新的局部商

末端强控制器必须保持(27)，不能只复用一个未包含新量的冻结纤维。
从起点采用
$$
\mathcal F_{\rm new}
=\left(\mathcal F_\star,\ 
[t^j]\mathfrak j(u(\,\cdot-t\,)),\
[t^j]\mathfrak k(u(\,\cdot-t\,)):
j=0,1\right).
\tag{28}
$$
新增两项的真实平移次数至多1，密度只含 $u,u',u''$，所以是有限、连续的 $C^2$ 多项式。
允许冗余；没有声称它们必已属于旧 $\mathcal F_\star$。

R280 型控制器的每个等背景 base 仍有原准确关系
$$
\operatorname{Re}(a_i+ib_i)^4=R_i^2-4T_i^2
=\frac{7B_0}{2}R_i,\qquad
\sum_iR_i x_i^j=0\quad(0\le j\le10).
$$
因此初选同一个母包时，该 base 的 $\mathfrak j,\mathfrak k$ 复四次实和均为零。
保持(28)后，各个真实微包在原位置的值仍是同一个母平移多项式的准确值，所以此零逐参数保持。
全部八／十二复制、正幅及镜像仅乘其实际正四次因子。
由此末控制器始终有
$$
\mathcal T=0.
\tag{29}
$$
旧 $\mathcal F_\star$ 部分继续保它自己的全部72面积与 quartic $C$。

在固定支撑的偶 Banach 域取(28)的实际最大微分秩，
用原 $\psi$ 乘偶多项式稠密性选一个非零最大 minor 及固定光滑纠正方向。
再沿 R361 明确正 finite-jet 见证到该见证的多项式线选择同一个母，
既保最大 minor 非零，又保全区正 prefactor 和
$$
\frac{-r^2r_2+2ur_2^2-ur r_4}{24r^3}\ne0.
\tag{30}
$$
最大秩为零时不需要纠正。
这是真正同母选择，不把任意预给母函数默认成 regular。
R361 的三个实际偶 $\chi$ 可继续在这个母上选出，并可取为 $\psi$ 乘有限偶多项式。

先给这个全72零、$\mathcal T=0$ 的强宏块及其镜像一个静态正幅，准确支付(27)之后仍负的 $\Psi$。
这个幅度和全部实际最终位置此时固定。
其后三导扰动保持(28)，故 $\Psi$ 与所有面积和新 $\mathcal T$ 均不变。

## 9. 第五 principal 行确实增加一个实际方向

只在强控制器的真实 rank-one 微包上变动，弱核不动。
记
$$
\lambda_i=-a_i^2(a_i^2-b_i^2).
$$
四个已用目标
$(\mathcal Q_{PP,0},F_0,F_1,F_2)$ 的 principal 在
$(H_0,H_a,H_b,H_d)$ 上仍是 R361 的非退化矩阵，行列式 $128ad\ne0$。

新增目标 $\mathcal Q_{PZ,2}(\pi/2)$ 按原 R285 全式分裂给 principal
$$
\boxed{
\lambda_i\int
\{-2d x^2ur+2(d-2e)x^3vr+6e x^4r^2\}(u''')^2 .
}
\tag{31}
$$
因为
$\alpha_P=-2r$、
$\alpha_Z=du+(-d+2e)xv-3ex^2r$，
(31)就是原 $x^2\alpha_P\alpha_Z$，没有漏掉 $I_2$ 的低阶项；它们保在完整 $C^2$ 基线中。

对一个固定偶 $\chi$ 和全部实际完整 copy，新的位置多项式次数4，
首系数是
$$
6e\left(\sum_\nu\omega_\nu\right)\int r_0^2\chi^2\ne0.
\tag{32}
$$
原四行位置次数至多2。
先用(32)的最高次系数取得一个独立的新坐标方向，
再用原二次位置系数及 R361 三个 $\chi$ 的三个独立常向量，得到真正五维 span。
全部 copy 的有限 $d_\nu,\omega_\nu$ 都在此位置多项式里；没有把它们换成理想同心包。

仍让三个 $\chi$ 各占原编码的一层，并各用十二个实际交替索引。
真实 Vandermonde 权
$\beta_i=1/\prod_{k\ne i}(X_i-X_k)$
满足 $\beta_i/\lambda_i>0$。
现在每行次数至多4，仍低于十二列的消矩阶数，故每组有严格正 kernel。
三组共36列的正锥于是恰为 $\mathbb R^5$，且全体列有严格正 kernel。
没有从 signed span 单独推出可实现的正幅控制。

## 10. 同一个有限 N 的完整五行根

对选中母包用原
$$
u_{N,z}
=u_0+N^{-3}z\chi\cos Ny+\sum_\ell a_\ell(N,z)e_\ell,
$$
准确解
$\mathcal F_{\rm new}(u_{N,z})=\mathcal F_{\rm new}(u_0)$。
最大秩／局部常秩论证保持整个有限映射。
纠正系数、参数一导及固定方向的三导贡献为 $O(N^{-1})$。

在一次固定的有限正幅盒上，五条完整目标满足
$$
\mathbf G_N(\mathbf z)
=\mathbf G_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1),
$$
$$
\mathbf G_N=
(\mathcal Q_{PP,0},F_0,F_1,F_2,\mathcal Q_{PZ,2})(\pi/2).
\tag{33}
$$
基线包括实际弱核心、新旧全部面积模块、真实 right histories、
所有已固定 copy 位置权及强控制器静态原值。
R285 的降阶只把余项确认为真实 $C^2$；没有把它们删掉或先设为零。

完整块之间的对称项也准确相加：
$XD_i,YD_i$ 真紧，异块的一阶嵌套因点乘为零，同块嵌套的二次左尾由完整 $I_j$ 与异块紧 outer 正交。
因此(33)没有漏一个依弱核心变化的跨块三导项。

由第9节的五维全正锥，给 $-\mathbf G_{\rm base}$ 一个全部列严格正的平方幅表示。
选五个独立列并固定其余正幅，极限 Jacobian 为 $2z_i v_i$，可逆。
一致 $C^1$ 收敛及非退化零稳定性给足够大但实际有限的整数 $N$ 和精确正幅根
$$
\boxed{\mathbf G_N=0.}
\tag{34}
$$
不把离散 $1/N$ 当作光滑参数，也不只消 principal。

原十二完整副本保持 angular odd 系数为零。
(27)—(29)及完整面积一直保
$\Xi_{PZ,2}=0$；故(3)、(34)给
$$
\mathcal Q_{PZ,2}(\theta)=0\quad\text{对全部 }\theta .
$$
旧 $PZ$ 第0矩等于 $F_2$ 加已零面积，第1矩由空间反射为零。
R361 的整个 $P^2,PW$ 也由(34)、面积及同一反射保持。最终
$$
\boxed{
\mathcal Q_{PP,j}=\mathcal Q_{PW,j}=\mathcal Q_{PZ,j}=0
\quad(j=0,1,2),\quad\text{全部相位}.
}
\tag{35}
$$
原全部18面积、完整第三、$\Psi$、三条 directed 行及指定的一层组合仍准确为零。

同一五维根也允许只把最后一个目标指定为任意固定有限 $\tau$，其余四个为零。
由(3)、(18)得到
$\mathcal Q_{PZ,2}(\theta)=\tau\sin^2\theta$。
所以新 gate 不是由 R361 条件自动推出；本稿确实增加了真实控制。

## 11. 有限选择顺序与严格范围

所有选择保持原实际顺序：

1. 固定 $\kappa$，以去掉共同非零 $h_e$ 行因子的归一算子读完整式。先选 R357 的有限母族、两形小值及实际三排序，给十列低库。
2. 固定 middle 十二列和高四列的真实位置、copy 权与有限宽度，依次选择有限 $H,H_2$ 得十三行实际库；保全部左下成本。
3. 在固定弱基线上取有限 $S$ 和真正正四次幅，支付(27)，保旧18面积并留负 $\Psi$。不在此后整体移动旧圆。
4. 从起点为(28)选择同一个最大秩正母、三个真实 $\chi$、固定纠正方向及成对反射强控制器；先固定其静态 $\Psi$ 幅度、最终包络和有限幅盒，再取同一个足够大的有限 $N$ 及(34)。
5. 共同正归一化保所有齐次零式。全部有限支撑，包括负半轴镜像，确定以后，再按 R354 选实际 $\omega$ 下界、共同物理区间与足够小的初始 $h_e$，安装同一 $M=0,T=\kappa_H\mathfrak H$ 闭 hook 和指定共振芽。

新 $\rho_\kappa$ 不随 $h_e$ 变化；$PZ$ 行只多一个非零 $h_e^{-1}$ 因子。
旧 Gaussian 行、三 directed 行仍按原固定行尺度变化，所有零保持。
没有把本稿解释成一个任意已冻结旧窄区间／旧几何的免费扩域。

完成(35)以后仍有12个反射允许的对称外矩函数位置：
$$
PY:0,2;\quad Z^2:0,2;\quad ZW:1;\quad
ZY:0,2;\quad W^2:0,2;\quad WY:1;\quad Y^2:0,2.
$$
它们不是已证明独立的12个 scalar，也没有被旧 strong 圆的32量结论代替。

其余完整零／一 Gaussian history 函数、真实闭路径其他曲段、
canonical 第四 period、平台／退化通量／端芽、同一个二阶 gauge 的 joint 匹配仍未由本稿支付。
R354 这条新几何不无证继承旧 wholeE、Morse 或全部 period。
本稿新增的是一个完整对称 Gaussian 乘积及其真正非principal角商的实际联合支付。
