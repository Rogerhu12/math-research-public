# R471 — 原 norm-two 整组合的六 sigma 因式及完整八输入 carry

日期：2026-11-14。**状态：R466 整组合已在原 R311 连接内精确
化为六个独立 sigma 与两个独立 Theta 的乘积；原连接、全部质量、
同一 ordinary ray 的真实八输入深域及输出 carry 已证明。**
这里不在 principal 中央观察内免费除掉 $\Theta(4z)^2$，
也不把新曲线投影等同于未投影的八输入来源。

## 1. 原两伴随的整组合正是既有纯倍点行

保留 $E_b:y^2=x^3+b$、$X=x^3$、$\Theta=x\sigma^2$、$b=17$ 的
共同物理框。R311 的真实原函数为
$$
C_X=C_1+\frac{C_3}{336b}-\frac{C_5}{840b}
 =\frac{\Theta(z)\Theta(2z)^2\sigma(4z)}{2240b}.
\tag{1}
$$
R460 的 $C_{13}=C_1-a_{13}C_3$、
$C_{15}=C_1-a_{15}C_5$ 中，
$$
a_{13}=-\frac{37}{33936b},\qquad a_{15}=-\frac{37}{53760b}.
$$
因此整个来源准确满足
$$
\boxed{101C_{13}-64C_{15}=37C_X.}\tag{2}
$$
这是实际同一连接中的身份，系数 $101,64,37$ 没有只在原点比较。
等价地，$\sigma^{34}y$ frame 中的多项式为
$$
C_X=\sigma^{34}y\,P_X(X),\qquad
P_X=-\frac{X(X-8b)^2(X^2+20bX-8b^2)}{560b}.
\tag{3}
$$

设原连接为 $q=17\Theta'/\Theta$，并记
$$
H_X=\frac{5H_3-2H_5}{3},\quad H_X(0)=1,\qquad
c_X=-\frac1{560b}.
$$
则 R311 的全部来源式可整理为
$$
\boxed{
G_X:=C_X'-qC_X=S-c_XH_X
=S+\frac{H_3}{336b}-\frac{H_5}{840b},\qquad
C_X'(0)=G_X(0)=\frac1{560b}.
}\tag{4}
$$
证书用原完整微分算子
$$
\nabla_q(\sigma^{34}yP)
 =\frac{\sigma^{34}}x
   \{6X(X+b)P'-(31X+34b)P\}
\tag{5}
$$
核定 (4)，没有删去原 $q$ 连接项或把 $H_X$ 当成新的单条
Hecke 特征线。

## 2. 六 sigma 因式保留真实独立输入

R466 的同一
$$
R_2=\frac{48by}{x(X-8b)},\qquad W_i=R_2 C_i(2z)
$$
给
$$
W_*:=101W_{13}-64W_{15}=37R_2 C_X(2z).
\tag{6}
$$
实际倍点符号为
$$
\Theta(2z)=x(X-8b)\sigma(z)^8,\qquad
\sigma(2z)=-2y\sigma(z)^4.
$$
于是先在全纯来源中约去真正相同的因子，
$$
R_2(z)\Theta(2z)=48by\sigma(z)^8,
$$
再代入 (1)，得到
$$
\boxed{
W_*(z)=-\frac{111}{280}\,
\sigma(z)^4\sigma(2z)\sigma(8z)\Theta(4z)^2 .
}\tag{7}
$$
两边都属原 untwisted $\mathcal S_{136}$：
六个 sigma 的次数为 $4+4+64=72$，
两个 $\Theta(4z)$ 各为次数 $32$。
这里 $\sigma(z)^4$ 是四个同来源的独立输入，不能把其总输出
深度改写为四个输入分别深。

令
$$
\mathcal F_{72}=\sigma(z)^4\sigma(2z)\sigma(8z),\qquad
\mathcal U_{64}=\Theta(4z)^2.
$$
则
$$
\mathcal F_{72}=16z^6+O(z^{12}),\quad
\mathcal U_{64}=1+O(z^6),\quad
\boxed{W_*=-\frac{222}{35}z^6+O(z^{12}).}\tag{8}
$$
这是未投影来源的首项。R466 新算术线的首项为
$$
P_+W_*=-\frac{3848}{5}S_{\rm new},\qquad
P_+=\frac{I+N_7^3+N_7^6}{3}
\quad\text{仅作用于已付的 }N_7^9=1\text{ 块}.
\tag{9}
$$
数 $-222/35$ 和 $-3848/5$ 不相等；余下六维来源补偿两者，
不能忽略它们。

### 2.1 无有理函数分母的可复核多项式

若需纯代数表示，置
$$
D_2=X^2+20bX-8b^2,\qquad
A_5=32(X+b)^2D_2-27X(X+4b)^3.
$$
标准除法递归和已付 sigma 符号给
$$
\frac{\Theta(4z)}{\sigma^{32}x}
 =16(X+b)D_2^2-3(X+4b)A_5,
\tag{10}
$$
$$
\frac{\mathcal F_{72}}{\sigma^{72}}
 =8(X+b)D_2\{27X(X+4b)^3(A_5-4D_2^2)-A_5^2\}.
\tag{11}
$$
右边次数分别为五和十一，首系数分别为一和十六。
因此 (7) 可与 R466 的两条完整二十一度多项式直接相等，
无需在局部截断级数中尝试“还原”隐藏因子。

## 3. 整测度、全部原输入与其真实 core 范围

沿当前固定 ray，保持
$$
\lambda=-\bar\pi_0^{-1},\qquad
\beta=-\lambda=\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad d=p-1.
\tag{12}
$$
这里 $\pi_0$ 是共同基曲线 $E_0$ 的指定 CM Frobenius。
R316 的两条完整低次 core 在此 ray 上同为
$$
\nu_\sigma|_{p\mathbf Z_p}=\beta[\kappa]_*\nu_\sigma,\qquad
\nu_\Theta|_{p\mathbf Z_p}=\beta[\kappa]_*\nu_\Theta .
\tag{13}
$$
这是从 R316 的 $\varepsilon=-1$ 和实际
$\pi_0=\varepsilon\pi_{17}$ 代入得到，保留了 sigma 的真实
半特征。R466 则给
$$
\boxed{\nu_{W_*}|_{p^n\mathbf Z_p}
       =\beta^n[\kappa^n]_*\nu_{W_*}\quad(n\ge0).}\tag{14}
$$
全纯乘法 (7) 不用于证明 (14)；它由整个 $\mathcal S_{136}$
真实 core 的定标得到。

取原完整八输入
$$
\mu=\nu_\sigma^{\otimes6}\otimes\nu_\Theta^{\otimes2},
\qquad
w=x_1+x_2+x_3+x_4+2x_5+8x_6+4t_1+4t_2,
\tag{15}
$$
则准确有
$$
\boxed{\nu_{W_*}=-\frac{111}{280}\,w_*\mu.}\tag{16}
$$
所有系数 $1,2,8,4$ 在本题普通素数处为单位；每个因子是
R300/R316 的完整整 Amice 测度。故 (16) 整且有界。
六阶单位矩还准确为
$$
\int_{\mathbf Z_p^\times}w^6\,d\nu_{W_*}
 =(1-\beta\kappa^6)\,6!\Omega_p^6
       \left(-\frac{222}{35}\right).
\tag{17}
$$
在现有 $p\equiv7\bmod64,\ p\ge71$ 的 ray 上它是单位。
这仍不是其对数中央导数的非零证明。

分别对八输入应用 (13)，得到**同一完整张量**的全深关系
$$
\mu|_{(p^n\mathbf Z_p)^8}
  =\beta^{8n}[\kappa^n,\ldots,\kappa^n]_*\mu .
\tag{18}
$$
相比之下，(14) 只控制总输出 $w$；不能将 (14) 带上任意
未运输的七个隐藏测试。

定义实际进位域
$$
\Gamma_n=\{w\in p^n\mathbf Z_p\}
          \setminus(p^n\mathbf Z_p)^8,\qquad n\ge1 .
$$
因为 $\kappa^n\mathbf Z_p=p^n\mathbf Z_p$，完整减去 (18) 后，
$$
\boxed{
-\frac{111}{280}
(w/\kappa^n)_*(\mathbf1_{\Gamma_n}\mu)
 =(\beta^n-\beta^{8n})\nu_{W_*}.
}\tag{19}
$$
这里 $n>1$ 保留输入共同赋值从零到 $n-1$ 的全部情形，
不把它错误缩为“至少一个输入单位”。若再要求
$v_p(w)=n$，右侧准确限制到 $\mathbf Z_p^\times$。

令 $J_{W_*}(u)$ 是原 principal 单位 Mellin。
归一为 $w/\kappa^n$ 的整条进位行是
$$
(\beta^n-\beta^{8n})J_{W_*}(u). \tag{20}
$$
若改用 $w/p^n$，必须再乘
$\langle\kappa/p\rangle^{ndu}$。
本行的质量恰为零（$W_*(0)=0$ 及 (14)），所以其一阶中央
尺度项在这里为零；这一事实只适用于本行，不适用于下节
的原连接行。

## 4. Theta 单位只允许来源反卷积，不免除原单位条件

$\Theta(0)=1$ 保证
$$
\Theta(4\Omega_p\log(1+T))^2\in1+T\mathcal O[[T]]
$$
是整 Iwasawa 代数的单位。故存在唯一整反卷积测度
$\nu_{\mathcal U}^{-1}$，并有完整来源等式
$$
\nu_{\mathcal F_{72}}
  =-\frac{280}{111}\,\nu_{W_*}*\nu_{\mathcal U}^{-1}.
\tag{21}
$$
若除以 $111$，仅另删固定素数 $3,37$；现有 ray 已不包含它们。

但是，对 $f_u(y)=\mathbf1_{y\in\mathbf Z_p^\times}
\langle y\rangle^{du}$，实际观察是
$$
J_{W_*}(u)=-\frac{111}{280}
\int f_u(a+t)\,d\nu_{\mathcal F_{72}}(a)\,d\nu_{\mathcal U}(t).
\tag{22}
$$
反卷积时必须准确运输这个相加单位条件及其全部对数测试。
同一输出方向的乘法因子不与“限制在 $p\mathbf Z_p$”交换，
所以 (14) 也不自动成为 $\mathcal F_{72}$ 的 scalar core。
本篇没有将 $\mathcal F_{72}$ 认作原 $E_{24}$ 来源，
没有从它的次数七十二或零质量推导曲线身份。

## 5. 原连接中央行与必须保留的对数质量

同一 ray 上，R311、R316 的原 $C_X$ 与 $G_X$ 满足
$$
\nu_{C_X}|_p=\beta[\kappa]_*\nu_{C_X},\qquad
\nu_{G_X}|_p=\lambda[\kappa]_*\nu_{G_X}.
\tag{23}
$$
定义原 tame-one 行
$$
D_X(u)=\Omega_p^{-1}\int_{\mathbf Z_p^\times}
 y\langle y\rangle^{du}\,d\nu_{C_X}(y)
$$
及同一个相加卷积来源 $\mathcal Q_X=qC_X=C_X'-G_X$ 的
principal 行 $Q_X(u)$。则 (4) 给整条等式
$$
\boxed{
Q_X(u)=D_X(u)-J_S(u)-\frac1{560b}J_{H_X}(u).
}\tag{24}
$$
它的质量完全已知：
$$
D_X(0)=\frac{1+\lambda\kappa}{560b},\qquad
J_{H_X}(0)=1-\lambda,\qquad
\boxed{Q_X(0)=\frac{\lambda(1+\kappa)}{560b}.}\tag{25}
$$
特别 $\mathcal Q_X(0)=0$ 这个**总质量**事实，不允许删除
非零的单位质量 (25)。

其原来源已有完全无逆 frame 的四输入式：
$$
qC_X=\frac{17}{2240b}\Theta'(z)\Theta(2z)^2\sigma(4z).
\tag{26}
$$
若 $\nu=\nu_\Theta(x_1)\otimes\nu_\Theta(x_2)
\otimes\nu_\Theta(x_3)\otimes\nu_\sigma(x_4)$，
$y=x_1+2x_2+2x_3+4x_4$，则
$$
\nu_{G_X}=\frac1{2240b\Omega_p}\,
y_*\{(y-17x_1)\nu\}.
\tag{27}
$$
这是 R311 的实际权，不能把 $G_X$ 改成未加权的四因子乘积。

因此中央导数始终保留
$$
Q_X'(0)=D_X'(0)-J_S'(0)-\frac1{560b}J_{H_X}'(0).
\tag{28}
$$
例如若某个后续全域恒等式把归一输出由 $\kappa^n$ 改成
$p^n$，在这一行上必须增加
$$
nd\log_p\langle\kappa/p\rangle\,
   \frac{\lambda(1+\kappa)}{560b},
\tag{29}
$$
而不能援用 (20) 的零质量将它一并删掉。

## 6. 可复核证书与后续接口

[check-r471-original-six-sigma-normtwo-factor.py](../scripts/check-r471-original-six-sigma-normtwo-factor.py)
及同名 JSON 精确核定 (2)–(5)、完整除法递归 (10)–(11)、
原八输入来源 (7) 和两种不同首项 (8)–(9)。所有多项式先在
$b=1$ 核定，再由显示的完整齐次式恢复一般 $b$；不依赖目标
素数样本。

依赖 R311 的原四输入连接、R316 的两条完整低次 core、
R466 的全部原二倍来源与完整 $\mathcal S_{136}$ core。
新增可用接口是 (7)、(15)、(18) 的同一真实输入张量和
(19) 的完整进位测度；后续 Riemann 变换必须运输这个张量的
全部域、权与输出。新曲线的中央零即使作为反证假设成立，
也不能据此给 (19)、(22) 或六个外谱另赋中央零。

