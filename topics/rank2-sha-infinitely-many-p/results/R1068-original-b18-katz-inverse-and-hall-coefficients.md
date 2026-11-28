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

## 10. 原三同源上的同次数比值：完整有理函数与有限极

本节固定(B1)–(B5)的同一个 \(S=S_{34}\) 和原两个三挠词的完整和
\(D=D_{102}\)。仍令 \(X=x^3\)、\(\delta=1+2\omega\)；
\(\delta^2=-3\)、\(N\delta=3\)，且 \(\delta\equiv1\bmod2\)。
这里使用真正的全局三同源，不另换一份同角色 theta 向量。

原 psi4 来源注(24)–(25)已经给出
$$
 \sigma(\delta z)=\delta x(z)\sigma(z)^3,\qquad
 x_\delta=-\frac{X+4}{3x^2},\qquad
 X_\delta=-\frac{(X+4)^3}{27X^2}.
 \tag{C1}
$$
置
$$
 \begin{aligned}
 A_3(X)&=X^3+228X^2+48X+64,\\
 Q_6(X)&=7(X+4)^6+108X^2(X+4)^3+11664X^4 .
 \end{aligned}
 \tag{C2}
$$
直接代入(B1)，逐因子得到
$$
 \begin{aligned}
 X_\delta+1&=-\frac{(X+1)(X-8)^2}{27X^2},\\
 X_\delta-8&=-\frac{A_3(X)}{27X^2},\\
 7X_\delta^2-4X_\delta+16&=\frac{Q_6(X)}{729X^4},\\
 S(\delta z)&=-\frac{27}{7}\sigma(z)^{102}
 X^2(X+4)^2(X+1)(X-8)^2 A_3(X)Q_6(X).
 \end{aligned}
 \tag{C3}
$$
常数的符号也固定：\(\delta^{34}=(-3)^{17}\)，所以最后一式
在原点首项为 \(-27z^6=\delta^6z^6\)。

(B3)还允许消去两份真实公因子，而不扩大既有共同因子结论。
每一项都含 \((y-\delta)(y+\delta)=X+4\)；在 \(y=\delta\)
或 \(y=-\delta\) 时，只有 \(a=1\) 的一支贡献一阶项，系数非零。
故 \(X+4\) 是 \(P_{14}\) 的简单因子。

\(A_3\) 的几何消去也可直接由原两词证明。若
\(x(\delta P)^3=8\)，则 \(R=\delta P\) 是原 \(x^3=8\) 的六挠点。
倍点公式给 \([2]R=\pm q_3\)，其中 \(q_3=(0,1)\)。
因此 \(R+q_3,R-q_3\) 中，一点为非零二挠点，另一点为 \(-R\)。
原 \(D_{\rm old}\) 在前者有二重零，在后者有一重零：
这是其完整因子
\(x(X+1)(X-8)(X^3-30X^2-144X-32)\) 的直接结果。
两个真实 Weyl multiplier 在这些点都正则且非零。
三同源为 étale，故两词之和在每个这样的 \(P\) 恰有一重零，
没有两份一次项可相消。它们正好是 \(A_3(X)=0\) 的全部点。
于是
$$
 P_{14}(X)=(X+4)A_3(X)J_{10}(X),\qquad
 J_{10}\in\mathbf Z[1/2,1/3,1/7][X]\text{ 首一，次数十}.
 \tag{C4}
$$
这只用 monic 除法及原两词；不另存一个拟合多项式。

因此同一次数线丛中的准确比值为
$$
 \boxed{
 \mathscr R_\delta(P):=\frac{D(z)}{S(\delta z)}
  =-\frac7{27}\,
       \frac{xJ_{10}(X)}
         {X^2(X+4)(X-8)Q_6(X)}
       \in\mathbf Q(E_0).
 }
 \tag{C5}
$$
它不是一份仅在原点定义的 formal 比值。
在 \(O\) 的完整前两项由(B10)给
$$
 \mathscr R_\delta(z)
 =-\frac1{27}z^{-2}
      \left(1-\frac{89}{7}z^6+O(z^{12})\right).
 \tag{C6}
$$
原点的极准确为二。其余有限极仍由(C5)保留，不能删掉：

- 在 \(q_3,-q_3\)，极准确为五。
- 在 \(X=-4\) 的六点，极准确为一。
- 在 \(X=8\) 及 \(Q_6(X)=0\) 的点，(C5)给至多一阶极；
  若 \(J_{10}\) 有额外共同零，则按(C5)真实相消，不预设互素。
- 没有表外的极。

第一项可直接核常数，而不只数除子：(B3)在 \(x=0,y=1\)
的 \(x\) 系数给
\(P_{16}(0)=-2^{31}/49\)，故
\(P_{14}(0)=2^{28}/49\)、\(J_{10}(0)=2^{20}/49\)。
(C5)遂在两点均为
\(\mathscr R_\delta=(8/1323)x^{-5}+\cdots\)。
\(Q_6\) 的根为原 \(7X^2-4X+16\) 的三同源逆像；
该目标不在 \(x^3=-1\) 或无穷，故这些根简单。
本节所有 formal 整性只使用固定分母 \(2,3,7\)，当前 \(p>211\)
时无新坏位。

## 11. 实际 delta 拉回框架、p² lift 与完整中心

使用(B12)的严格参数 \(v\)、\(h(v)=v/T_{\rm g}(w(v))\)，
\(P(v)=[p](v)=pv-v^q\)。记
$$
 \mathscr H(v)=\frac{\sigma(z(v))}{h(v)},\qquad
 K_\delta(v)=
       \frac{\mathscr H(v)^{102}}{\mathscr H([\delta]v)^{34}} .
$$
由(C1)消去 sigma，得到完全整的表达
$$
 \boxed{
 K_\delta(v)=
 \left(\frac{h([\delta]v)}{\delta x(v)h(v)^3}\right)^{34}
       \in1+v\mathcal O_L[[v]],\qquad K_\delta^{-1}\in\mathcal O_L[[v]].
 }
 \tag{C7}
$$
确切地，
\(V_\delta=\delta x(v)v^3/[\delta]v\) 是首值1的整单位，
所以(C7)也等于
\(\{T_{\rm g}(w(v))^3/
[T_{\rm g}(w([\delta]v))V_\delta]\}^{34}\)。
这里保留完整 \(T_{\rm g}\)；不只比较第一 Gaussian。

原 \(E_{\rm c}\) 和 \(z(v)/v\) 都按 \(\mu_d\) 不变，
\([\delta]\) 与该群交换，故
$$
 K_\delta(v)=k_\delta(W),\qquad W=v^d,\qquad
 k_\delta\in1+W\mathcal O_L[[W]] .
 \tag{C8}
$$

令 \(T\in E[p^2]\)、\(Q=pT\ne O\)。
原对称 order-\(p^2\) theta lift 的唯一性
R1062(G52)–(G54)用于
\([\delta]^*\mathcal L_{34}\simeq\mathcal L_{102}\)，给
$$
 m_{102,T}(v)=m_{34,\delta T}([\delta]v)\,
   \frac{K_\delta(P(v)\oplus Q)}{K_\delta(P(v))}.
 \tag{C9}
$$
这是整 theta group 上的恒等式，不只在 generic 点成立：
三同源及线丛识别均在原 good 模型上整，
刚性化首值由(C7)为1；两个 lift 覆盖同一点且满足同一
对称/order条件，其比同时平方为1、\(p^2\) 次方为1，所以为1。
配对也完全匹配，因为 \(34N\delta=102\) 是整数等式，
不是只模 \(p\) 的同余。

若原标记使用另一个实际 \(T'\) 且 \(pT'=\delta Q\)，
令 \(R=T'-\delta T\in E[p]\)，保实际物理点的 Weil pairing
\(E_q=e_{p^2}\)，并定义
$$
 \epsilon_{\delta,T}=E_q(\delta T,R)^{17}.
 \tag{C10}
$$
R1062(G54)的方向为
\(s_N(T+R)=E_q(T,R)^{-N/2}s_N(T)s_N(R)\)，
而 \(s_N(R)\) 是原 \([p]\)-pull 的核线性化。
故(C9)换成 \(T'\) 时恰多乘(C10)，没有任意重选的根单位。

写 \(f_{102}=h^{102}R_-\)、\(f_{34}=h^{34}R_S\)。
由(C5)与(C7)，
\(f_{102}=K_\delta^{-1}\mathscr R_\delta\, f_{34}\circ[\delta]\)。
于是实际整来源准确满足
$$
 \boxed{
 A_{102,T}(v)=
   \epsilon_{\delta,T}A_{34,T'}([\delta]v)\,
       \frac{\mathscr R_\delta(P(v)\oplus Q)}{K_\delta(P(v))}.
 }
 \tag{C11}
$$
右端的 meromorphic 因子单独有极；
整性来自其与同一个 \(A_{34,T'}\) 的实际乘积，
不把 \(\mathscr R_\delta\) 自身称为整 Katz 单位。

按 R1065(W20)–(W22)的全部连接，
\(A_{N,T}(v)=a_N(P(v))\mathscr F_{N,T}(pz(v))\)，
\(a_N=(h/\sigma)^N\)。
(C7)恰使这两份完整连接相消，给物理变量中的全式
$$
 \boxed{
 \mathscr F_{102,T}(u)
   =\epsilon_{\delta,T}\,
       \mathscr F_{34,T'}(\delta u)\,
              \mathscr R_\delta(v(u)\oplus Q).
 }
 \tag{C12}
$$
所有 \(Z_Q\)、\(\Gamma\)、Miller 高项及原中心都包含在(C12)。
它不是从局部主项猜出的关系。

## 12. 原 Haar-dual Hall 字的 delta 返回

以下只重标原负 Hall covector，不把负模型改成另一条正模型。
在 R716 的 physical 标签中，以
$$
 h_N(x+y\omega)=((x+y)/3,\,(3N/2)(x-y))
$$
记录完整 Heisenberg 位移；\(\det h_N=-N\)。
因此
$$
 M_\delta=h_{34}[\delta]h_{102}^{-1}\in{\rm SL}_2(\mathbf Z_p).
 \tag{C13}
$$
原 Weil 作用在 Heisenberg 参数上是逆转置，所以实际元素为
\(g_\delta=M_\delta^{-{\rm t}}\)。
它固定原标准球：整 unipotent、单位对角及 self-dual Fourier
的原公式分别固定球，给整个 \({\rm SL}_2(\mathbf Z_p)\) 的
准确相位1。这与 R1062(G80)相同，未另选 splitting。

负模型取完整 contragredient，故(C13)在原负 Hall 基上也给
唯一的绝对运输；改代表的相位是对应正模相位的逆。
原字符 \(\chi_r\) 为 \(p\) 阶、anticyclotomic、tame-zero，
而 \(\delta/\bar\delta=-1\)，所以
\(\chi_r(\delta)^2=\chi_r(-1)=1\)，进而
\(\chi_r(\delta)=1\)。
同时
\(102\,N(v)=34\,N(\delta v)\)，
故负 Norm \(r/3\) 轨道准确送到 Norm \(r\) 轨道，原 wild 字不变。

设原负字为 \(\lambda^-_T A_{102,T}\)。
把 Haar-dual covector 按(C13)完整 push 到 degree34，所得标签记作
\(\lambda^{\vee}_{T'}\)。由 R716(24)–(25)的代表变更及(C10)，
准确有
$$
 \boxed{\lambda^-_T\epsilon_{\delta,T}
             =\lambda^\vee_{T'},\qquad pT'=\delta pT.}
 \tag{C14}
$$
这个 \(\vee\) 是原实际 Haar bilinear dual：
并未将其认成原正 Hall 向量，亦未额外再共轭一次。
原反 CM 图此时仍是
\(\gamma_{34}=\omega\,c\)，它只固定两侧点的标记关系；
R1063(I16)–(I18)中的两个 Hall 和仍相互独立。

原两个 coherent 参数的尺度也相同地返回。
R1063(I13)准确给
\(\delta\ell_-=\ell_+\)，在 \(E_0\) 模型亦有
\(\delta L_-=L_+\)。
故(C12)的参考函数 \(\mathscr F_{34,T'}(\delta u)\) 在负槽中
确实使用同一个 canonical \(S_{34}\) coherent 参数；
原负来源与正来源的固定 raw 幅度仍是 I11/I18a 的原数，
没有因(C14)删除。

## 13. 原负二读者的全部 shifted canonical 槽

对 \(Q\ne O\)，由(C5)的 monic 形式和固定分母，
$$
 \mathscr R_\delta(v)=-\frac1{27}v^{-2}
                  (1+v^6\mathcal O_L[[v^6]]) .
$$
定义
$$
 r_Q=\mathscr R_\delta(Q),\qquad
 \frac{\mathscr R_\delta(v(u)\oplus Q)}{r_Q}
       =\sum_{k\ge0}h_{Q,k}u^k,\qquad h_{Q,0}=1 .
 \tag{C15}
$$
在每个严格 \(|u|\le R<R_E=p^{-1/\Delta}\) 上，该比及逆均为
norm1 的解析单位。因为所有固定非原点极在 formal 单位盘之外，
只需保 \((v(u)\oplus Q)/v_Q\) 的实际二极；
该比在严格内盘可逆。原 \(u\leftrightarrow v\) 在此等距，
所以对全部 \(k\)
$$
 v_p(r_Q)=-2/\Delta,\qquad
 v_p(h_{Q,k})\ge-k/\Delta.
 \tag{C16}
$$
这是普通 Taylor 系数界，无额外 \(k!\)。

取原 \(\Pi^\Delta=p^p\)、\(b=p/\Pi\)。
按 R1062(G70)–(G72)保全部 \(\Delta\) 块，
\(m_r(t)=r+\Delta t\)。
参考块 \(\mathbf G^\delta_{S,T'}\) 在非负整数权读
\(b^mD_u^m\mathscr F_{34,T'}(\delta u)|_0\)；
其全 germ 使用原
\(B_{34,T'}(b\,34\delta Z_{\delta Q})^{[r]}(m)
 \mathcal F_{34,\delta Q}(m)\)。
\((b\,34\delta Z_{\delta Q})^\Delta\) 是
\(1+\mathfrak m^\eta\) 的主单位，沿 R1062/R1066 的共同原分量，
不另开根单位方向。

唯一写 \(r-k=r_k-\Delta l_k\)，\(0\le r_k<\Delta\)。
(C12)的完整 Leibniz 式于是给
$$
 \boxed{
 G_{D,T,r}(t)=\epsilon_{\delta,T}r_Q
  \sum_{k\ge0} b^kh_{Q,k}(r+\Delta t)_k
       G^\delta_{S,T',r_k}(t-l_k).
 }
 \tag{C17}
$$
第 \(k\) 项至少获得 \(k\eta\)，故在闭单位 \(t\) 盘一致收敛，
并可逐项求导。逆比给同样的反向算子。
证明先用每个非负整数权的有限 Leibniz 和，
再逐块用真正的原 Tate 函数和一致尾；没有调用已撤的
usual-depleted 正权延拓。

取 \(r=\Delta-2,t=-1\)，原 physical 负二值准确为
\(b^2G_{D,T,\Delta-2}(-1)\)。
记 \(r_{Q,k}=r_Qh_{Q,k}\)，消去同一个 \(b\) 后得到
$$
 \boxed{
 \begin{aligned}
 &\frac{B_{102,T}}{(102Z_Q)^2}\mathcal F_{102,Q}(-2)\\
 &\quad=\epsilon_{\delta,T}
    \sum_{k\ge0}(-1)^k(k+1)!\,r_{Q,k}\,
       \delta^{-2-k}
       \frac{B_{34,T'}}{(34Z_{\delta Q})^{2+k}}\,
                         \mathcal F_{34,\delta Q}(-2-k).
 \end{aligned}
 }
 \tag{C18}
$$
所有负整数都按(C17)指定的块解释。
\((-2)_k=(-1)^k(k+1)!\) 是原未除幂导数产生的准确因子。
它没有把负二 primitive 换成 \(r_Q\) 乘一个正槽值。

按原 \(d^{-1/2}\) 规范对(C18)求和，并用(C14)，得到原负 Hall
的完整返回
$$
 \boxed{
 H_{-,r}^{[-2]}=
 \frac1{\sqrt d}\sum_{T'}\lambda^\vee_{T'}
  \sum_{k\ge0}(-1)^k(k+1)!\,r_{Q,k}\delta^{-2-k}
   B_{34,T'}(34Z_{\delta Q})^{-2-k}
                 \mathcal F_{34,\delta Q}(-2-k).
 }
 \tag{C19}
$$
其中 \(Q=\delta^{-1}pT'\) 是原实际非零点；
不存在另选的三除点，因为 \(\delta\) 在 \(E[p]\) 上可逆。
R1063(I18a)中的 whole 值仍将(C19)乘**另一份独立**的
\(H_{+,r}^{[0]}\)，并保
\(c_0^{(0)}\Omega_A^3/(p^2\rho_A^2L_-^2)\)。
在整个临界列中，(C17)取代负槽后，
\(\Lambda'(\cdot)\)、\(\Lambda(\cdot)\)、所有 shifted 参考导数、
\(\log U_*\) 和全 Maass \(E\) 项照原顺序一起求导；
不把 ordinary Amice 斜率当已经完成的 Maass 斜率。
这些费用分别仍由 R1063(I20)、R1065(T20)、
R1066(Z20)–(Z22)的同一个 full reader支付。

若回到未施 Hall 投影的 R1065(W17)，\(Q=O\) 的 old 字也必须留。
此时(C12)作为乘积仍成立，因为 \(S(\delta u)\) 六重零消去
\(\mathscr R_\delta\) 的二极；但(C15)–(C19)的非零点归一不适用。
不能用这一消极把 old 项从原完整来源删除。

## 14. 全首 Hall 窗的同一个 canonical Cartier 矩阵

(C12)还给一条不依赖负权延拓的完整有限行。
保 \(W=v^d\)，按所有实际角分量分解
$$
 \begin{aligned}
 \mathscr R_\delta(v)
   &=\sum_{\substack{0\le a\le d-6\\a\equiv0\ (6)}}
                     v^{a-2} R_a(W),\\
 f_{34}([\delta]v)
   &=\sum_{\substack{0\le r\le d-6\\r\equiv0\ (6)}}
                     v^r S_r^\delta(W),\qquad
 S_0^\delta(W)=W B_+^\delta(W).
 \end{aligned}
 \tag{C20}
$$
所有 \(R_a,S_r^\delta\) 整；
(C6)在当前 \(p>211\) 直接给
$$
 R_0(0)=-1/27,\qquad R_6(0)=89/189.
 \tag{C21}
$$
第二个数对全部当前 \(p\) 都是单位。
由 \(f_{102}=K_\delta^{-1}\mathscr R_\delta(f_{34}\circ[\delta])\)，
取角 \(d-2\) 得精确式
$$
 \boxed{
 k_\delta(W)\mathcal B_-(W)
   =R_0(W)B_+^\delta(W)
     +\sum_{\substack{6\le a\le d-6\\a\equiv0\ (6)}}
                    R_a(W)S_{d-a}^\delta(W).
 }
 \tag{C22}
$$
\(a=0,r=0\) 的一项之所以也进入该行，是因为
\(v^{-2}S_0^\delta=v^{d-2}B_+^\delta\)；
没有遗漏这一次负指数 carry。

严格坐标的全 \(\mu_\Delta\) 等变给
\([\delta]v=\delta vG_\delta(v^\Delta)\)，
\(G_\delta(U)\in1+U\mathcal O_L[[U]]\)。
因此在原已付的完整 \(p-1\) 层窗中，
$$
 B_+^\delta(W)\equiv
       \delta^d\mathcal B_{34}(\delta^dW)
          \pmod{W^{p-1}},\qquad
 \overline{B_+^\delta(W)}
     =3\,\overline{\mathcal B}_{34}(3W)
       \pmod{W^{p-1}} .
 \tag{C23}
$$
这里只在所示整系数模 \(p\) 窗使用 \(\delta^d\equiv3\)；
挠点上的全精度值仍用 R1063(H24)的 \(\widehat3\)。
原 \(\mathcal B_-\) 到真正负二 Hall 的修正仍是(B33)，
即 R1063(L7)的唯一末槽 transvection。
在 canonical 坏所给
\(\overline{\mathcal B}_{34}(0)=0\) 下，与另一独立正 Hall 相乘时，
该末槽修正才在当前窗消失。没有在乘法前直接删除它。

(C22)的新增作用是：原负行现在准确返回**同一个 canonical
S34 的全部角行**，而非一组自由补来源。
它含固定有理核和真正三同源/中心，不再有一个任意选的局部比值。
但(C21)也显示不能把它缩成
\(\mathcal B_-\) 是 \(\mathcal B_{34}(3W)\) 的单位倍：
最邻近的 \(S_{d-6}^\delta\) 真实出现，系数为单位，
其余角行同样须保。原 canonical 坏只约束指定中央读数，
并不同时赋这些 \(d/6-1\) 个角行为零。
所以本节没有据(C22)宣称整个固定连接的 \(p\)-曲率消失，
没有将原单 Hall 非零替成严格上界，
也尚未给主目标所需的无穷素数量词。


### 14.1 一个实际二阶 Darboux 候选的准确极费用

令
\(F_\delta=S(\delta z)/\sigma(z)^{102}\)。
(C3)表明，在 \(q_3,-q_3\) 处以 \(x\) 为局部参数，准确有
\(\operatorname{ord}F_\delta=6\)；此处 \(Dx=2y\) 是单位。
因此
$$
 \operatorname{ord}_{\pm q_3}(D^2F_\delta)=4,\qquad
 \operatorname{ord}_{\pm q_3}(xF_\delta)=7,\qquad
 \operatorname{ord}_{\pm q_3}(D_{102}/\sigma^{102})=1 .
 $$
最后一项用(C6)前已核的 \(P_{16}(0)=-2^{31}/49\)。
所以原 \(D_{102}\) 不属于
\(\sigma^{102}\operatorname{Span}_{\overline{\mathbf Q}}
       \{D^2F_\delta,xF_\delta\}\)。
更一般，若 \(a_j\) 在这两个实际点都正则，则
\(\operatorname{ord}(a_jD^jF_\delta)\ge6-j\)。
所以任何至多四阶的词
\(\sum_{j=0}^4a_jD^jF_\delta\) 仍至少二重零，不能给出所需一重零；
全系数正则时，微分阶数至少为五。
这不是在某个有限 jet 上作维数计数，而是同一三挠点的完整局部除子约束。
若只使用带极的二阶词相认，至少一项必须补偿三阶零差；
相应三挠极必须进入完整 adjoint/Hall 读者。
原点最高两项相配并不足以给这种全来源身份。

## 15. 两个实际三角色的完整 Lamé 系统

本节继续(C1)–(C23)，没有换负来源或另选一个 genus-one cover。
为避免与原点 \(Q=pT\) 混淆，记三同源靶上的坐标为
$$
 (t,u)=(x(\delta P),y(\delta P)),\qquad
 U=t^3,\qquad u^2=t^3+1,\qquad
 \partial=\frac{d}{dz_{\rm base}}=\delta^{-1}D_P .
$$
原两个三挠 Weyl 字的代数因子准确是
$$
 a=-\frac{y(P)-\delta}{\delta x(P)},\qquad
 b=-\frac{y(P)+\delta}{\delta x(P)},\qquad
 a^3=-(u+1),\quad b^3=-(u-1),\quad ab=t .
 \tag{C24}
$$
这些是原 psi4 来源注(24)中已按首 \(1/z_{\rm base}\) 刚性化的
\(g_+,g_-\)，没有重新开三次根。

令原 \(q_3=(0,1)\)。在 \(P\to O\) 时，
\(a,b\sim1/(\delta z_P)\)；在 \(P+q_3\) 处用
\(x(P+q_3)=2z_P+\cdots\)、\(y(P+q_3)=1+\cdots\)，得到
$$
 a(P+q_3)=\omega a(P),\qquad
 b(P+q_3)=\omega^2 b(P).
 \tag{C25}
$$
两边之比的立方为1，首项即固定该比。这支付的是原正 \(q_3\)
的方向，不将“两个非平凡角色”留作未定的交换标签。

逐项微分(C24)给
$$
 \frac{\partial a}{a}=\frac{u-1}{t},\qquad
 \frac{\partial b}{b}=\frac{u+1}{t},\qquad
 \partial^2a=2ta,\quad\partial^2b=2tb,\qquad
 a\partial b-(\partial a)b=2 .
 \tag{C26}
$$
例如 \(\partial u=3t^2\)、\(\partial t=2u\)；
\(\partial[(u-1)/t]+[(u-1)/t]^2=2t\)。
所以这是真实、固定的 Lamé \(n=1\) 系统，
不是对若干 Taylor 项拟合的高阶方程。

可取另一个完整基
$$
 g=a-b=\frac2{x(P)},\qquad
 g'=\partial g=-\frac{4y(P)}{\delta x(P)^2},
 \qquad
 \partial\binom g{g'}=
     \begin{pmatrix}0&1\\2t&0\end{pmatrix}\binom g{g'} .
 \tag{C27}
$$
另一解为 \(a+b=ug-tg'\)。
在 \(P=O\)，\(g\) 准确二重零、\(g'\) 准确一重零；
在 \(P=\pm q_3\)，二者分别有准确一阶、二阶极。
这些极不能从后续 differential word 中删除。

原 deck generator 在此非特征基上的完整矩阵是
$$
 \binom{g(P+q_3)}{g'(P+q_3)}
 =
 \frac12
 \begin{pmatrix}
 \delta u-1&-\delta t\\
 \delta t^2&-\delta u-1
 \end{pmatrix}
 \binom g{g'} .
 \tag{C28}
$$
其迹为 \(-1\)、行列式为1、立方为单位矩阵。
矩阵随 \(t,u\) 变化；它与(C27)的联络满足真实的水平相容，
不能在原有理基中把它另改成一份常矩阵。
(C25)则给其准确对角化和完整 trace-zero 两角色。

## 16. 原 D102 的显式带极一阶词，不丢任一三挠支

保持(B3)的原六个 \(r_j\)，以及
$$
 R_{\rm old}(t)=t(U+1)(U-8)(U^3-30U^2-144U-32).
$$
在三同源靶上，原加法公式给
$$
 t_+=x(R+q_3)=\frac{2(1-u)}{t^2},\qquad
 t_-=x(R-q_3)=\frac{2(1+u)}{t^2}.
$$
原 \(c_{q_3}=-2^{-1/3}\) 与 raw 规范准确合成
$$
 \frac{2^{1/3}}{147}c_{q_3}^{34}
       =\frac1{301056}.
$$
所以两词**完整相加**给
$$
 \begin{aligned}
 D_{102}(P)&=\sigma(z_{\rm base})^{34}
                         \{A(t,u)a+B(t,u)b\},\\
 A(t,u)&=-\frac{(u+1)^{11}R_{\rm old}(t_+)}{301056},\\
 B(t,u)&=-\frac{(u-1)^{11}R_{\rm old}(t_-)}{301056}.
 \end{aligned}
 \tag{C29}
$$
这保留原(23)的 Weyl 指数及 \(c_{q_3}^{34}\)，
不能将两个 ordinary translate 代入(C29)。

看似有分母的 \(A,B\) 实际都在
\(\mathbf Z[1/2,1/3,1/7][t,u]/(u^2-t^3-1)\) 中。
对原指数 \(j=1,4,7,10,13,16\)，利用
\((u-1)(u+1)=t^3\)，有
$$
 A=-\frac1{301056}
       \sum_j r_j(-2)^jt^j(u+1)^{11-j}.
 \tag{C30}
$$
其中 \(j=13,16\) 的两项分别用
\(t^{13}/(u+1)^2=t^7(u-1)^2\)、
\(t^{16}/(u+1)^5=t(u-1)^5\) 消分母；
\(B\) 同理。具体地，写 \(A=E(t)+uO(t)\)，则
\(B=-E(t)+uO(t)\)，且
$$
 \begin{aligned}
 E(t)&=\frac{t}{588}(U+1)(U-8)
                    (U^3+60U^2+144U-320),\\
 O(t)&=\frac{t}{588}(U-8)
                    (-33U^3-36U^2+432U+192).
 \end{aligned}
 \tag{C31}
$$
这里 \(588=2^2\cdot3\cdot7^2\)。
可直接按 \(u^2=U+1\) 验算：从(C30)取偶、奇部分，乘回 \(588/t\)，
分别得到
$$
 \begin{aligned}
 E_{\rm num}&=U^5+53U^4-284U^3-1808U^2+1088U+2560,\\
 O_{\rm num}&=-33U^4+228U^3+720U^2-3264U-1536 .
 \end{aligned}
$$
这两个有限等式与(C31)相同；不靠首项去指定整来源。

用 \(a+b=ug-tg'\) 改写(C29)，定义
$$
 C(t)=E(t)+(U+1)O(t),\qquad
 B_1(t,u)=-ut\,O(t).
$$
于是有准确全源式
$$
 \boxed{
 D_{102}(P)=C(t)\,\mathscr U_0(P)
                    +B_1(t,u)\,\mathscr U_1(P),
 \quad
 \begin{cases}
 \mathscr U_0=\sigma(z_{\rm base})^{34}g
                      =2\delta^{34}\sigma(z_P)^{102}x(P)^{33},\\
 \mathscr U_1=\sigma(z_{\rm base})^{34}g'
                      =-4\delta^{33}\sigma(z_P)^{102}x(P)^{32}y(P).
 \end{cases}
 }
 \tag{C32}
$$
这是一阶词作用于**指定的 Lamé 解**，不是被§14.1排除的
正则二阶词作用于 \(S(\delta z)\)。
若用 base sigma 的协变导数
\(\nabla_{34}=\partial-34\zeta(z_{\rm base})\)，则
$$
 \nabla_{34}\mathscr U_0=\mathscr U_1,\qquad
 \nabla_{34}\mathscr U_1=2t\mathscr U_0 .
 \tag{C33}
$$
这项共同 sigma/连接不能从(C32)删去；
在实际 translated 读者中，(C33)始终按
R1065(W20)–(W22)或 R1066(N8)–(N17)运输全部连接。

### 16.1 全局极和原点阶的完整支付

在 base 原点，\(C\) 的极阶准确为32，\(B_1\) 的极阶准确为31；
在 base 其它点它们都正则。
拉回后，可能的有限极只在 \(\pm q_3\)：
\(\mathscr U_0,\mathscr U_1\) 在这两点分别有33重、32重零，
准确抵消上述极并留下至少一重零。
在 \(P=O\)，两条 \(\mathscr U_i\) 的首阶分别为36、35，
所以两份乘积都从四次项开始。

更精确地，设
\(\mathscr D_0=C\mathscr U_0\)、\(\mathscr D_1=B_1\mathscr U_1\)，则
$$
 \boxed{
 \mathscr D_0,\mathscr D_1\in H^0(E_0,\mathcal L_{102}),\qquad
 [z_P^4]\mathscr D_0=\frac{16}{49},\quad
 [z_P^4]\mathscr D_1=\frac{33}{49},\quad
 D_{102}=\mathscr D_0+\mathscr D_1 .
 }
 \tag{C34}
$$
例如 \(C\) 的首项为 \(-32t^{16}/588\)，
\(B_1\) 的首项为 \(33ut^{14}/588\)，
且 \(z_{\rm base}=\delta z_P\)、\(\delta^2=-3\)；
它们给(C34)，两数之和恰为1。
代(C1)的 \(t,u\) 后，两份乘积都是
\(\sigma(z_P)^{102}xP_i(x^3)\)，多项式首系数如(C34)，
系数分母只涉及 \(2,3,7\)。
所以这里没有由若干 meromorphic 项的未付高极相消来宣称整性。
当前 \(p>211\) 时，两条首系数均为单位。

这些 \(\mathscr U_i,\mathscr D_i\) 是由原两词唯一指定的辅助
section，不是新分配的 elliptic canonical 类。
(C34)不授权把原 bad 条件分别施于 \(\mathscr D_0,\mathscr D_1\)。

## 17. 同一点、同一中心和全 Hall 转置

对原每个 \(T\in E[p^2]\)、\(Q=pT\ne O\)，取原
\(\mathcal L_{102}\) 对称 theta lift；\(\mathscr U_0,\mathscr U_1\)
和 \(D_{102}\) 使用完全同一个 lift 与中心。
令 \(R=\delta Q\)，并在物理变量 \(s\) 中写
$$
 C_Q(s)=C(x(R+\delta s)),\qquad
 B_{1,Q}(s)=B_1(x(R+\delta s),y(R+\delta s)).
$$
乘一个固定有理函数时，实际 Weyl 字只把该函数按同一个点平移。
因此(C32)在全部 Miller/连接后准确成为
$$
 \boxed{
 \mathscr F_{D,T}(s)=
       C_Q(s)\mathscr F_{\mathscr U_0,T}(s)
       +B_{1,Q}(s)\mathscr F_{\mathscr U_1,T}(s).
 }
 \tag{C35}
$$
若读原整 \(p\)-pull 坐标，则 \(s=pz(v)\)，右边的有理函数
在 \(\delta(P(v)\oplus Q)\) 上评价。
两个乘积各自都是(C34)的真正整新字，故完整核 character、
\(\psi=0\) 和 R1065(W13) 的 Katz 返回均逐项成立。
不把孤立的 \(C_Q\) 或 \(B_{1,Q}\) 说成整 Katz 单位。

写
\(c_{Q,k}=[s^k]C_Q(s)\)、\(e_{Q,k}=[s^k]B_{1,Q}(s)\)。
在每个严格 \(|s|<R_E\) 盘，原有理式和固定极给
$$
 v_p(c_{Q,k})\ge-\frac{32+k}{\Delta},\qquad
 v_p(e_{Q,k})\ge-\frac{31+k}{\Delta}.
 \tag{C36}
$$
\(\mathscr U_0,\mathscr U_1\) 的实际质量估值分别为
\(36/\Delta,35/\Delta\)，其原全阶
\(\mathcal F_{\mathscr U_i,Q}\) 仍由 R1062(G1)–(G8)给出，
并对全部整数块保持原一致界。
因此(C35)可按(C17)保全部 \(\Delta\) 个 shift；
第 \(k\) 项仍严格增益 \(k\eta\)，可逐项求导。

特别记
$$
 \mathcal J_{\mathscr U_i,T}(-2-k)
   =B_{\mathscr U_i,T}
        (102Z_Q)^{-2-k}\mathcal F_{\mathscr U_i,Q}(-2-k)
$$
为相同原 Teich/深主单位分量的完整 physical 读数。
负二值精确为
$$
 \boxed{
 \mathcal J_{D,T}(-2)=
   \sum_{k\ge0}(-1)^k(k+1)!
       \{c_{Q,k}\mathcal J_{\mathscr U_0,T}(-2-k)
           +e_{Q,k}\mathcal J_{\mathscr U_1,T}(-2-k)\}.
 }
 \tag{C37}
$$
这里不再另乘 \(\delta^{-2-k}\)：
\(C_Q,B_{1,Q}\) 已使用 \(R+\delta s\)，
而 \(\mathscr U_i\) 已是在原 \(P\) 变量和 charge102 中的实际 section。
这与(C18)使用 base charge34 参考的另一种记账严格不同。

原负 Hall 对(C37)施加同一个
\(d^{-1/2}\sum_T\lambda_T^-\)；所有
\(c_{Q,k},e_{Q,k}\) 留在该和内，不能提出。
另一份正 Hall 仍是原独立和。
如果改回(C18)的 degree34 标签，才使用(C10)/(C14)的完整
half pairing 和 dual covector；不再在(C37)重乘一次。
原 non-\(p\)/\(h\)/Artin 外权、旧字和
\(\Lambda'\mathcal M+\Lambda\mathcal M'\) 中的完整 Maass 项，
均沿(C19)后所列同一 reader保留。
各辅助项不另外获得一条可自由赋零的 automorphic 角色。

## 18. 此固定三角色系统的准确曲率范围

(C26)由度三 étale isogeny 上的两个实际代数解平凡化。
所以其 rank-two 连接、以及加入平凡角色后的完整 rank-three
pushforward，在所有当前好位的 \(p\)-曲率本来就是零。
这不是 canonical bad 的新推论；
其复单值群本来就是有限的三角色群。
在 \(a,b\) 基中该事实即(C25)，在 \(g,g'\) 基中是(C28)。

原来源还乘共同 \(\sigma(z_{\rm base})^{34}\)，
并在(C33)、(C35)中保原连接、Lie/coherent 尺度和整个有限读者。
没有将 \(\zeta\) 或 \(T_{\rm g}\) 换成一条新固定有理 connection。
因此不能把上述有限子系统的零 \(p\)-曲率当作原 Hodge/heat
对象的零 \(p\)-曲率，也不能拿其有限单值群给主门的反证。

本节的实质返回是(C29)–(C37)：原两个三挠字准确给一个固定
Lamé 系统的明确多项式词，全部极由(C34)支付，
同一个 p² 中心和完整 shifted Hall 仍在。
真正尚待的行依旧是这些指定有权和中不由原 source 已自动强制的
非消失或严格赋值上界；不以(C34)的单项单位首系数替代它。
