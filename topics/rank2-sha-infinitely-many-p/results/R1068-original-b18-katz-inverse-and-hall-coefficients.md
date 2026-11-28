# R1068 — 原 B18 共同因子、逐 p² 字的 Katz 整逆及同一 Hall 首 jet

日期：2026-11-28。会话：Astra-rank2-Sha-0b097461-20261127。

**状态：本文证明原 canonical S34 与两个三挠词完整相加所得 D102 之间的一条实际来源关系。它给逐同一几何 p² 挠点的整 Katz 逆、原 Hall 总来源的全部有限系数乘法式，以及完整 Cartier 分量关系。没有由该恒等式推出某一 canonical 低矩为单位，也没有把一个依赖挠点的逆移出 Hall 和。**

原 S34 首阶为六；首阶为二的是 Dold=C34，不是 S34。下文 Q7 是来自七同源的二次多项式，数字 7 不是其次数。所有数学恒等式为手推，没有新增计算作业。

## 1. 原两个完整来源及其共同因子

保持 [R1063](R1063-original-tame-zero-hall-and-five-layer-miller-return.md)(H1)–(H4) 的共同模型、微分与规范：
$$
 E_1:y^2=x^3+1,\quad X=x^3,\quad \delta^2=-3,\quad D=d/dz,
$$
$$
 S=\sigma^{34}x^2(X+1)(X-8)\frac{7X^2-4X+16}{7},
 \qquad S=z^6+\cdots .
 \tag{B1}
$$
原负来源 D102 始终是
[原 psi4 来源注](../notes/2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md)
(20)–(28) 的两个实际三挠 Weyl 词经 delta 拉回后的完整和，按既定首四次项归一。写
$$
 D_{102}=\sigma^{102}xP_{16}(X),\qquad \deg P_{16}=16,
 \qquad P_{16}\text{ 首一},\qquad D_{102}=z^4+\cdots .
 \tag{B2}
$$
为核定本文所用的额外因子，保留该注的完整原式。置
$$
 (r_1,r_4,r_7,r_{10},r_{13},r_{16})
 =(256,1376,1216,58,-37,1).
$$
则
$$
\begin{aligned}
301056\,xP_{16}(X)
=\sum_{a\in\{1,4,7,10,13,16\}}r_a x^a
\big\{&
(-2\delta)^a(y+\delta)^a(y-\delta)^{34-2a}\\
&+(2\delta)^a(y-\delta)^a(y+\delta)^{34-2a}\big\}.
\end{aligned}
\tag{B3}
$$
这包括原两条三挠词，未删其任一项。其作为原 normalized D102 的身份、首系数 301056，以及 raw 幅度与 coherent 变量中的 delta 费用，仍沿原来源注，不重选相位。

两词中的有理坐标准确为
$$
 x_\pm=\mp2\delta x\,\frac{y\pm\delta}{(y\mp\delta)^2},
 \qquad
 R_{\rm old}(x)=x(X+1)(X-8)(X^3-30X^2-144X-32).
 \tag{B4}
$$
当 X=-1、y=0 时，两个 x_\pm 都为 -2x，故 x_\pm^3=8。
当 X=8、y=\pm3 时，两个 x_\pm 都为 x；例如
(3-\delta)^2=6(1-\delta)、3+\delta=\delta(1-\delta)
逐项给出该等式。上述点的 y\pm delta 均非零，因而完整两词的 multiplier 在此正则；Rold 的 X-8 因子分别使两词为零。

因此
$$
 P_{16}(X)=(X+1)(X-8)P_{14}(X),
 \qquad P_{14}\in\mathbf Z[1/2,1/3,1/7][X]
 \text{ 首一，次数十四}.
 \tag{B5}
$$
整分母结论直接由(B3)及两次 monic 多项式除法成立。本文不声称这些因子是全部公因子，也不需要额外的零点重数断言。

定义三条**由原来源确定**的 section：
$$
\begin{aligned}
 B_{18}&=\sigma^{18}x(X+1)(X-8),\\
 C_{84}&=\sigma^{84}P_{14}(X),\\
 C_{16}&=\sigma^{16}x(7X^2-4X+16)/7 .
\end{aligned}
\tag{B6}
$$
准确有
$$
 \boxed{D_{102}=B_{18}C_{84},\qquad S=B_{18}C_{16},}
 \qquad
 \operatorname{ord}_0(B_{18},C_{84},C_{16})=(4,0,2),
 \quad C_{84}(0)=1.
 \tag{B7}
$$
它们分别是 L18、L84、L16 的全局 section，其中
L_N=O_E(NO)。例如 P14(x^3) 的唯一极在 O，极阶84，
而 x(7X²-4X+16) 的极阶14。

共同因子也有准确 sigma 形式：
$$
 B_{18}(z)=\frac{\sigma(z)^2\sigma(2z)\sigma(2\delta z)}{4\delta}.
 \tag{B8}
$$
这是 [R430](R430-original-integral-second-output-division-and-degree18-mixed-rows.md)
(1) 中旧 G16 的 sigma² 倍。这里复用其固定 theta 恒等式；
不把该文普通素数上的 Amice 反卷积搬到当前惰性素数。

## 2. 一个实际的非零 Cartier 非对角系数

给出一项小的精确证书，以免把(B7)误作标量乘法。
在(B3)中，只有 a=1、4 对 x49 有贡献；对 x46 只有
a=1、4、7、10 有贡献。相应未除 301056 的系数如下。

| a | x49 系数 | x46 系数 |
|---|---:|---:|
| 1 | -95232 | 39616512 |
| 4 | 396288 | -263927808 |
| 7 | 0 | 327794688 |
| 10 | 0 | -28864512 |

例如 a=1 的两项来自
-372·256·x(X+4)(X+1)^15 和
161820·256·x(X+4)(X+1)^14；
a=4 的两项系数为 396288·27 与 -396288·693。
故
$$
 [X^{15}]P_{16}=1735/7,\qquad [X^{13}]P_{14}=1784/7.
 \tag{B9}
$$
原 sigma 与 x 的展开为
sigma=z(1+z6/210+...)、x=z^-2-z4/7+...。
由(B6)、(B9)逐项得
$$
\begin{aligned}
 B_{18}&=z^4(1-277z^6/35+\cdots),\\
 C_{16}&=z^2(1-157z^6/105+\cdots),\\
 C_{84}&=1+8724z^6/35+\cdots,\\
 D_{102}&=z^4(1+8447z^6/35+\cdots),\\
 S&=z^6(1-988z^6/105+\cdots).
\end{aligned}
\tag{B10}
$$
因此
$$
 \frac{S}{D_{102}}
 =\frac{C_{16}}{C_{84}}
 =z^2\left(1-\frac{26329}{105}z^6+\cdots\right).
 \tag{B11}
$$
该系数非零。它并非一次数值测试，也不赋任何随 p 变化的高系数为单位。

## 3. 同一完整 LT 框架中的四条来源

取原惰性 p>211，置 q=p²、Delta=q-1、d=p+1，沿用
R1063(H3) 的严格整参数 v：
$$
 P(v)=[p](v)=pv-v^q,\qquad z(v)=v+O(v^q).
$$
令
$$
 \mathscr T(v)=T_{\rm g}(w(v)),\qquad h(v)=v/\mathscr T(v).
$$
这里是原完整 T_g，不只保第一 Gaussian。
对任意上述整数 N，保整线丛框架
$$
 e_N=h^{-N}s_N^0,\qquad s_N^0=\sigma^N.
$$
写
$$
\begin{aligned}
 b&=h^{18}x(X+1)(X-8),\\
 c_{84}&=h^{84}P_{14}(X),\\
 c_{16}&=h^{16}x(7X^2-4X+16)/7,\\
 f_{102}&=h^{102}xP_{16}(X),\qquad f_{34}=h^{34}R_S .
\end{aligned}
\tag{B12}
$$
这里 x、X 均在同一严格参数中代入。因为 h/v 整可逆、
x∈v^-2O[[v]]，准确有
$$
\begin{gathered}
 b\in v^4(1+v^6O[[v^6]]),\quad
 c_{84}\in1+v^6O[[v^6]],\quad
 c_{16}\in v^2(1+v^6O[[v^6]]),\\
 f_{102}=b\,c_{84},\qquad f_{34}=b\,c_{16}.
\end{gathered}
\tag{B13}
$$
可逆性目前只是在 O[[v]] 中；不据 c84(0)=1 就宣称 c84
或其逆属于 Katz 测度像。

置完整比值
$$
 \mathcal Q(v)=c_{16}(v)c_{84}(v)^{-1}\in v^2O[[v]],
 \qquad f_{34}=\mathcal Q f_{102}.
 \tag{B14}
$$
R660(3)、R1063(H21) 给
$$
 h=\sigma(z(v))\,\frac{v}{z(v)}E_{\rm c}(z(v))^{-1},
 \quad E_{\rm c}=\exp\bigl(\Pi_0\log(\sigma/z)\bigr).
$$
故(B14)含有 charge -68 的完整框架差
(h/sigma)^-68，不把它省掉。由于 E_c=1+O(z^d)、
z(v)=v+O(v^q)，当前 p>211 时(B11)确切给
$$
 \mathcal Q(v)=v^2\left(1-\frac{26329}{105}v^6+O(v^{12})\right).
 \tag{B15}
$$

## 4. 逐同一个几何 p² 点的实际 theta lift

固定一个实际 T∈E[p²]，Q=[p]T≠O，并取包含全部实际点、
原中心及固定非 p 系数的有限 F/L。所有以下乘法均指
**同一个几何点 T**；不能把正、负 Schrödinger 模中相同坐标的
字认作同一个点。若起点是 R1054 的坐标，须先分别通过
R1061 的 beta+、beta- 映射返回该 T。

对每个偶 N∈{16,18,34,84,102}，在 [p]*L_N 上取原对称
order-p² theta lift W_N(T)。R1061(E4)–(E8)的唯一性保证它与
原解析 Weyl 字相认。说明其乘法方向如下：两个这样的 lift
的 tensor 在 [p]*L_(N+M) 上仍覆盖同一 T，仍满足
i(g)=g^-1、g^(p²)=1。给定 T 的这种 lift 唯一：
两个 lift 的比 c 为中心元，两个条件分别迫 c²=1、
c^(p²)=1；p² 为奇数，所以 c=1。因此
$$
 W_{N+M}(T)=W_N(T)\otimes W_M(T).
 \tag{B16}
$$
这是给定点的唯一性，不声称 T↦W_N(T) 是群同态。
它也说明取 dual line bundle 时的 lift 为逆；不能另外选择
一个方便的 p² 次根相位。

按 R1065(W5)–(W8) 的**实际 [p] 拉回框架**定义：
$$
\begin{aligned}
 A_{102,T}&=m_{102,T}\,f_{102}(P(v)\oplus Q),\\
 A_{18,T}&=m_{18,T}\,b(P(v)\oplus Q),\\
 A_{84,T}&=m_{84,T}\,c_{84}(P(v)\oplus Q),\\
 A_{16,T}&=m_{16,T}\,c_{16}(P(v)\oplus Q),\\
 A_{34,T}&=m_{34,T}\,f_{34}(P(v)\oplus Q).
\end{aligned}
\tag{B17}
$$
这些 m 的原中心均保留。W 的整 theta-group 证明对上述
L_N 逐字成立，故每个 m_N,T 是 O_F[[v]] 的单位。
(B16)及 e_(N+M)=e_N e_M 给
m_(N+M),T=m_N,T m_M,T，不仅首值相等。

结合(B13)，得到
$$
 \boxed{
 A_{102,T}=A_{18,T}A_{84,T},\qquad
 A_{34,T}=A_{18,T}A_{16,T}.
 }
 \tag{B18}
$$
常数项中的 Klein/Miller 因子也按同一 N 相乘；
这正是原全部中心的返回，没有把它们改成1。

## 5. A84 的逆确实是原 Katz 范畴中的整来源

由(B13)，c84(P(v)⊕Q) 的常数项是单位，整个级数整。
故
$$
 V_{84,T}:=A_{84,T}^{-1}\in O_F[[v]]^\times .
 \tag{B19}
$$
现在才支付其 Katz 性质。对于 R∈E[p]，W 的完整核 character
给
$$
 A_{N,T}(v\oplus R)=\chi_{N,T}(R)A_{N,T}(v),
 \quad
 \chi_{N+M,T}=\chi_{N,T}\chi_{M,T}.
 \tag{B20}
$$
在共同几何点标记中，chi_N 是由 L_N 的实际 Weil pairing
取得的 N 次 character；不在原 beta 坐标的 W10 上再额外乘 N。
Q≠O、p∤N 保证上述每个 character 都非平凡。

因此 V84 在核上按 chi84^-1 变换。对整个 p 核求和，
$$
 \boxed{\psi A_{N,T}=0,\qquad \psi V_{84,T}=0.}
 \tag{B21}
$$
第二式是完整平均的实际结果，未将一般形式逆宣称为
psi-integral。Laurent Berger, *Galois measures and the Katz map* (2025), [arXiv:2504.20558v3](https://arxiv.org/html/2504.20558v3), Theorem A，按 R1065(K9)/(W13) 的同一
整 Galois–Katz dual，遂给唯一
$$
 \nu_{84,T}\in\operatorname{Hom}_{O}
   (\mathscr C,O_F),\quad
 \mathcal K^*\nu_{84,T}=V_{84,T},\quad
 \|\nu_{84,T}\|\le1,\quad
 \operatorname{supp}\nu_{84,T}\subset\mathbb T^\times .
 \tag{B22}
$$
它的质量 V84(0) 为单位，所以范数准确为1。
同样有 mu102,T、mu18,T、mu16,T、mu34,T；
mu102、mu34 恰是 W13 中沿相同几何点读取的原来源，
另外两份来自(B6)的指定固定 section。

完整来源身份现在成为
$$
 \boxed{A_{34,T}=A_{102,T}\,V_{84,T}\,A_{16,T}.}
 \tag{B23}
$$
这里先后两个实际乘积仍分别为 A18,T 和 A34,T，因而它们都
是已证明的整 psi=0 来源。本文不需要假定任意两个
Galois-dual 测度之间都有无损的普通 Cp 测度卷积。
下节仅使用已存在的这些来源和每个 universal character
系数的有限乘法式。

Q=O 的 old 字必须另保。此时 m=1，(B23)作为形式恒等式仍是
phi f34=phi f102·phi(c84^-1)·phi c16；但
psi phi(c84^-1)=c84^-1，没有证明其全部迭代整。
所以(B21)–(B22)仅用于真正新字，不能借此删除 R1065(W17)
的 old 项或给 old 逆免费添加 Katz 范围。

## 6. 原整 Hall 总来源的完整有限系数行

令 I_r 是 R716 的原 Norm r 轨道，T_i 是其真正 p² lifts；
用 lambda_i 表示原表达中尚在字外的有限角色/中心系数。
若已把某个 chi 相位吸收在既定字的标记中，就不再在 lambda_i
中乘第二次。保持原正根 sqrt(d) 归一，写原整 Hall 来源为
$$
 P_{\rm Hall}(v)=\frac1{\sqrt d}\sum_{i\in I_r}
                         \lambda_i A_{34,T_i}(v),
 \qquad a_m=[v^m]P_{\rm Hall}.
 \tag{B24}
$$
它是同一个 [p]-pull-frame 总来源，不是裸 f34，也不是一个单字。
各 lambda_i 及 T_i 保留 R716/R1067 的原完整有限字。
实际 non-p 谱在这里已先回到 canonical S；
本文不把(B23)反向套到未投影的任意 rank-one theta 来源。

由(B23)，对每个 m≥0，准确有
$$
\boxed{
 a_m=\frac1{\sqrt d}\sum_{i\in I_r}\lambda_i
 \sum_{\substack{j+k+l=m\\j,k,l\ge0}}
 \mu_{102,T_i}(c_j)\,
 \nu_{84,T_i}(c_k)\,
 \mu_{16,T_i}(c_l).
}
\tag{B25}
$$
这里 c_j 是 R1065(K9) 的**第 j 个 universal character
系数**。式中没有 j!，也不将高 c_j 改成 c1^j/j!。
三项先在同一有限 F 中相乘，再按原 Hall 行求和。
每个内和有限且整，未引入新的 p 分母。

特别，已正式发布的
[R1067](R1067-original-first-wild-rubin-even-multiplicity.md)(49)
给出原 exact Hall 零下的真实新行。代入(B25)，准确得到
$$
\boxed{
 \mathcal T_{34,T_r}=0\ \Longrightarrow\
 \frac1{\sqrt d}\sum_{i\in I_r}\lambda_i
 \sum_{j+k+l=\Delta}
 \mu_{102,T_i}(c_j)\nu_{84,T_i}(c_k)\mu_{16,T_i}(c_l)
 \in p^2\mathcal O_F.
}
\tag{B25a}
$$
同一前提还给(B25)在 m=0 的完整有权和为零。
这是原真正 $P_H$ 的新行，未替换成裸 $f_{34}$ 或普通
sigma 系数。
它们不逐字迫任何一项为零。
V84,T 依赖 T，其 character 也已在(B20)锁定，
所以不能从(B25)将它移出 Hall 和或只留下它的单位质量。
本文没有将 canonical 中央坏条件单独升级为 a0=0 或上述
p² 同余；这类前提仍须沿原 Rubin/Hall 桥逐项支付。

连接也保持完全相同。若采用 R1065(W20) 的物理 sigma frame，
alpha_N,p=a_N([p]v)，a_N=(h/sigma)^N，则
$$
 \alpha_{34,p}=\alpha_{102,p}\alpha_{84,p}^{-1}\alpha_{16,p}.
 \tag{B26}
$$
故完整协变导数 alpha D alpha^-1 对(B23)作真正 Leibniz
展开，保全部 strict-coordinate、Gaussian 与物理 p^-m 费用。
(B25)特意留在原整拉回框架中，未将其当成删除连接后的
负二值或斜率。

## 7. E17 与 E1 的同一个首 q-1 行

以下给从 R716 原模型送回本文共同模型时的低窗费用。
保 vartheta^6=17，并令 j:E17→E1 满足 z1=vartheta z17。
sigma 的实际同构为
sigma17(z)=vartheta^-1 sigma1(vartheta z)。
R660(3)定义
Pi0 F(z)=d^-1 sum_(zeta∈mu_d)F(zeta z)，故它逐项与
vartheta 缩放交换，完整地给
$$
 E_{\rm c,17}(z)=E_{\rm c,1}(\vartheta z).
 \tag{B27}
$$
这不是仅首 Gaussian 的比较。

两个严格参数之间是同一整 CM 形式同态
$$
 v_1=\iota(v_{17})
      =\vartheta v_{17}+t_qv_{17}^q+O(v_{17}^{q+1}),
 \quad t_q\in O_F.
$$
由 h=sigma(v/z)Ec^-1，两个整框架的精确比为
$$
 \frac{j^*e_{N,1}}{e_{N,17}}
     =\left(\frac{\vartheta v_{17}}{\iota(v_{17})}\right)^N.
 \tag{B28}
$$
在 [p] 拉回框架中须将右边再代 P(v)。
其首个可能非恒定项在 v^Delta，系数为
-N(t_q/vartheta)p^Delta；全部后继项次数更高。
所以，由 S17=vartheta^-6 j*S1 及原 lifts 的自然性，
$$
 \boxed{
 a_{\Delta,17}
 =\vartheta^{\Delta-6}a_{\Delta,1}
   -34\vartheta^{-7}t_qp^\Delta a_{0,1}.
 }
 \tag{B29}
$$
这里 t_q 只需整，不预称它是单位。
若原 Hall 精确为零，则最后一项严格为零；只读模 p² 时它也
深于所需精度。模型同构不将原 degree34 的 Norm r 改成
Norm17r；后者属于 R1067 的 degree2 参考，是另一条已明写的
标记选择。全严格形式群中不声称 iota(v)=vartheta v。

## 8. 完整 Cartier 行及不能省掉的相邻角分量

把(B14)按同一个 v/W 分解，W=v^d：
$$
 f_{102}(v)=\sum_{r=0}^{d-1}v^r D_r(W),\qquad
 \mathcal Q(v)=\sum_{j=0}^{d-1}v^j Q_j(W).
 \tag{B30}
$$
这是 O[[v]] 在 O[[W]] 上的完整自由分解。
原 mu6 型给 D_r=0 除非 r≡4 mod6，
Q_j=0 除非 j≡2 mod6。因 f34 的常数项为零，
其零角部分为 W B34(W)。
可能有 r+j≡0 mod d 的项中只有 r+j=d，故准确有
$$
 \boxed{
 \mathcal B_{34}(W)
   =Q_2(W)\mathcal B_-(W)
      +\sum_{\substack{4\le r\le d-8\\r\equiv4\ (6)}}
                  Q_{d-r}(W)D_r(W).
 }
 \tag{B31}
$$
其中 D_(d-2)=B_- 正是 R1063(H19) 的原有限负行。
(B15)给
$$
 Q_2(0)=1,\qquad Q_8(0)=-26329/105.
 \tag{B32}
$$
所以当前长 W 窗并没有把(B31)变成一个标量单位倍：
最靠近的另一个实际角行 D_(d-8) 已带这个固定非零系数。
即使使用完整 p-1 层，仍需保其余 d/6-1 个角分量及完整
Q_j 卷积。这是对原实际来源的精确式，不是按维数猜测的
自由补项。

若要返回负二 Hall，仍使用 R1063(L7)的原连接修正
$$
 \mathcal P_-(W)
 =\mathcal B_-(W)
   -\frac{2(p-1)b_{-,0}}{102\kappa_*}W^{p-2}
       \pmod{(p,W^{p-1})}.
 \tag{B33}
$$
不能在(B31)未替换(B33)时把 B_- 直接叫负二读数。
真正成对来源还保 B34(hat3 W)、两个独立 Hall 和、
原 d/p² Haar、全部 non-p/h/Artin 及外权导数。
(B31)只重写其中同模型的正角行，不把相反 beta 坐标
或相关点值当成两个独立 Hall 和。

## 9. 对主缺口的准确意义

本篇的新增内容是(B5)–(B7)的指定共同因子、
(B19)–(B23)在实际新字上的整 Katz 逆、
(B25)同一 Hall 总来源的完整有限行，以及(B31)的全角矩阵。
它使原 a_Delta 的实际额外 p 条件可以回到完整
102/84逆/16 来源，而不是重新引入一个自由四轴或一个未标定
theta 向量。

本文没有证明(B25)的某项或总和为单位，没有把 a0=0 或
a_Delta∈p² 当作 canonical 中央坏的无条件后果，
也没有用 C84(0)=1 取消全部 Cartier 分量。
主目标所需的严格单 Hall 界 vHall<2/(p-1) 及其无穷素数量词
仍需真正新的非消失输入。后续若得到这样的低行，仍沿
R716/R1067 的原通常全 Sha 桥返回，不把这些辅助 section
另称为 rank-two elliptic canonical 来源。

### 后继范围收紧（R1067 §14.1）

R1067(52)以同一实际共同中心、完整有限 jet 和首挠点域的 $\mu_d$ 下降证明，不假设 Hall 为零就有 $M_1-M_0\in p\mathcal O_F$，即 $U_q a_\Delta-pa_0\in p^2\mathcal O_F$。因此(B25a)在精确零分支的额外一个 $p$，对本题完整来源已由旧域下降强制，不能再算独立新增的 canonical 坏约束。本文(B23)–(B25)的实际整逆和同点有限系数式仍全部成立；它们负责将原行准确返回，尚未给更深组合或全和非零。
