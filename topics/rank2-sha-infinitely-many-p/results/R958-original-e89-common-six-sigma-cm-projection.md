# R958 — 原同六 sigma 中的 E89 完整 CM 投影与五伴随中央行

日期：2026-11-26。**已证明并完成原输入公开检查：run45809854198，首候选的完整投影系数为 $\alpha=(273+156\omega)/185\ne0$。** 本篇使用原 R465 的六个独立 sigma 输入，同一次运行重新生成原 degree178 的完整 CM7/13 矩阵，并核完整秩一投影；不是新的自由 theta 向量。

本文的目标是把 R943 的原 $E_{89}$ 中央落实在既有六输入联合上。
此结论不使所有混合单位条件或所有来源乘积的中央为零；
主目标的无穷素数量词仍需后续消费。

## 1. 原六输入、全部尺度与一个实际 degree178 候选

先在共同模型
$$
E_1:y^2=x^3+1,\qquad dz=dx/(2y),\qquad
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad\sigma=z+\cdots
$$
上固定
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma_7=3+\omega,\quad\bar\gamma_7=2-\omega,\quad
\gamma_{13}=4+\omega.
$$
使用六个**未缩放**的独立输入 $\boldsymbol\xi=(\xi_1,\ldots,\xi_6)$，置
$$
\rho_{\rm raw}=-\frac1{84}\nu_\sigma^{\otimes6}.
\tag{1}
$$
这只是 R465(2) 在前四个输入缩放之前的记法；其原两个输出行是
$$
a_S=(\delta,2\delta,\gamma_7,\bar\gamma_7,1,2),\qquad
a_T=(\delta,2\delta,\gamma_7,\bar\gamma_7,3\delta,4).
\tag{2}
$$
因此仍然准确有
$$
(a_S)_*\rho_{\rm raw}=\nu_S,\qquad
(a_T)_*\rho_{\rm raw}=6\delta\,\nu_T.
\tag{3}
$$
第二式的 $6\delta$ 没有被删去。

优先取
$$
u=\gamma_{37}=7+3\omega=\frac{11+3\delta}{2},\qquad Nu=37,\qquad a=1.
$$
候选输出及实际来源为
$$
a_{a,u}=(\delta,2\delta,\gamma_7,\bar\gamma_7,a,2u),
$$
$$
F_{a,u}(z)=-\frac{1}{84au}
 \sigma(\delta z)\sigma(2\delta z)\sigma(\gamma_7z)
 \sigma(\bar\gamma_7z)\sigma(az)\sigma(2uz).
\tag{4}
$$
这准确是 $(au)^{-1}(a_{a,u})_*\rho_{\rm raw}$ 的生成来源。原六输入、
原 $-1/84$、最后两个 CM 乘法及 $1/(au)$ 均固定。首项乘积为
$-84au\,z^6$，所以 $[z^6]F_{a,u}=1$。

reader 按以下顺序检查，首个非零投影成功即停止：
$$
\begin{array}{c|c|c|c}
a&Na&u&Nu\\ \hline
1&1&7+3\omega&37\\
5&25&6+\omega&31\\
11+3\omega&97&4+\omega&13\\
9+\omega&73&5+2\omega&19
\end{array}
\tag{5}
$$
每行都满足 $Na+4Nu=149$。四个前项的范数总和为29，因此全部候选
的实际 degree 都为178。没有在观察投影输出后自由改变候选或加入
一个已知的 $W$ 系数表。

### 1.1 半特征与全部准周期

对原奇 sigma，若 $\lambda=m\lambda_1+n\lambda_2$，半特征为
$$
\epsilon(\lambda)=(-1)^{m+n+mn}.
\tag{6}
$$
它在 $\mathcal O_K/2\simeq\mathbf F_4$ 的三个非零类上均为 $-1$。
奇范数 CM 元在这三个类上置换，故
$\epsilon(v\lambda)=\epsilon(\lambda)$；偶 CM 元属于 $2\mathcal O_K$，
故其半特征为一。不能用 CM 系数之和模二替代这个二次半特征。

(4) 中 $\delta,\gamma_7,\bar\gamma_7,a$ 四项为奇范数，另外两项
为偶，故完整半特征为一，恰与 $\sigma^{178}$ 相同。
准周期中的 Gaussian 由
$\eta_{v\lambda}=\bar v\eta_\lambda$ 和 $\sum N(a_{a,u})_i=178$
准确支付。共同旋转六个 sigma 给 $\zeta^6=1$，故来源属于完整
degree178 的 principal 30维块。下面还给出完整函数域恒等式，独立
核实该归属，而不是只凭 degree 和六次首项推断。

## 2. 完整除法多项式身份

对 $Nv\equiv1\pmod6$ 的非零 CM 元 $v$，原 division 函数为
$$
r_v(z)=\frac{\sigma(vz)}{\sigma(z)^{Nv}}
      =v\,R_v(X),\qquad X=x^3,
\tag{7}
$$
其中 $R_v$ 是首一多项式，次数 $(Nv-1)/6$。

这里保留了 leading constant $v$。完整证明如下：
$r_v$ 的除子为 $[v]^*(O)-(Nv)(O)$；奇范数时半特征无遗留
平坦扭转，Gaussian 相消，故它是原椭圆函数。它为偶函数，非零
核点按 $\pm$ 配对，各 x 坐标为简单零。共同三次 CM 旋转以及
$Nv\equiv1\bmod6$ 使它属于 $K[x^3]$。原点首项
$v z^{1-Nv}$ 固定 (7)，不容再任取一个根单位。

R465(4) 的全 sigma 恒等式给
$$
S=\sigma^{34}x^2P_S(X),\qquad
P_S(X)=X^4-\frac{53}{7}X^3-\frac{12}{7}X^2
                   -\frac{80}{7}X-\frac{128}{7}.
\tag{8}
$$
写 $Nu=6h+1$、$R_u(X)=\sum_{j=0}^h r_{u,j}X^j$。原倍点式
$$
\sigma(2z)=-2y\sigma(z)^4,\qquad
X(2z)=\frac{X(X-8)^3}{64(X+1)^3}
\tag{9}
$$
于是准确给
$$
J_u(X)=\sum_{j=0}^h r_{u,j}\,64^{h-j}
 X^j(X-8)^{3j}(X+1)^{3(h-j)},
\tag{10}
$$
$$
\boxed{F_{a,u}=\sigma^{178}x^2P_S(X)R_a(X)J_u(X).}
\tag{11}
$$
证明是将 (7) 先应用于 $az$，再应用于 $u(2z)$，并在原
$-1/84$ 六乘积 (8) 中代入 (9)；指数恰为
$34+(Na-1)+4(Nu-1)=178$。每个分母均在 (10) 中完整消去。
$J_u$ 首一、次数 $4h$，故 (11) 的 X 多项式首一、次数28。
完整30维向量的第28坐标为一、第29质量坐标为零。

### 2.1 reader 如何从实际 CM 群律重建 $R_v$

代码不输入 $R_v$ 系数表。它在 $K(x)$ 中把点表示为
$$
(X(x),\,yG(x)),\qquad y^2=x^3+1.
$$
原椭圆加法与倍点给
$$
L=\frac{G_2-G_1}{X_2-X_1},\qquad
L_{\rm dbl}=\frac{3X_1^2}{2(x^3+1)G_1},
$$
$$
X_3=(x^3+1)L^2-X_1-X_2,\qquad
G_3=-G_1+L(X_1-X_3).
\tag{12}
$$
$[\omega](X,yG)=(\omega X,yG)$。通过整数倍点和一次实际加法，
得到 $[m+n\omega]$，并在整个函数域逐项检查
$$
(x^3+1)G_v^2=X_v^3+1,\qquad X_v'=vG_v.
\tag{13}
$$
约去全部公因子并使 $X_v=N_v/D_v$ 的分母首一后，完整检查
$$
\deg N_v=Nv,\quad \deg D_v=Nv-1,\quad
\operatorname{lc}(N_v)=v^{-2},\qquad D_v=P_v(x)^2.
\tag{14}
$$
最后一个首一平方根按最高系数递推构造，随后对整个多项式回乘；
并检查 $P_v\in K[x^3]$。由已证明的完整除子与首项，
$r_v=vP_v$，因而这就是 (7) 的原 division 函数。
这不是数值拟合或有限 Taylor 截断。

## 3. 同一次运行中的原完整 CM 投影

原完整基和算子一概沿用 R943：
$$
e_j=\sigma^{178}x^2X^j\quad(0\le j\le29),\qquad
N_\gamma=\gamma^{-1}[\gamma]_*[\bar\gamma]^*.
\tag{15}
$$
原 producer 不改源码、不改规范、不改固定哈希。它在本次公开 run
重生 norm7、norm13 的 $a=1,\ldots,32$ 全纤维，前30个做完整
Vandermonde 读取，后两个检查每一列；norm13 的每个同纤维另保原
$S_{34}$ 绝对锚。所有178次 carrier、原 division leading constant
及目标 $a^{-2}$ 保持。reader 在内存中取得这一次产生的完整矩阵
$A_7,A_{13}$，完整读取旧 JSON 报告，继续核对原有接受门与旧矩阵哈希，没有把以前
的29项 $W$ 坐标当输入。

R943 的原质量观察核同时在本次重建，得到
$$
w_{28}=1,\quad w_{29}=0,\quad
A_7w=(1+\omega)w,\quad A_{13}w=\omega w.
\tag{16}
$$
还检查全部 $w_j\in\mathbf Q$，以及完整30维身份
$$
A_7\overline{A_7}=I,\qquad A_{13}\overline{A_{13}}=I.
\tag{17}
$$

这里只能使用真正算子的多项式投影，不能任取一个线性投影。
代码按 $c=0,\ldots,29$ 检查
$$
B_c=A_7+cA_{13},\qquad e_c=1+\omega+c\omega,\qquad
q_c(X)=\frac{\det(XI-B_c)}{X-e_c}.
\tag{18}
$$
选择第一个满足 $q_c(e_c)\ne0$ 的 $c$，并定义
$$
\boxed{\Pi=\frac{q_c(B_c)}{q_c(e_c)}.}
\tag{19}
$$
特征多项式由完整 Faddeev–LeVerrier 递推及 Cayley–Hamilton 回乘
得到。代码再独立检查
$$
\Pi^2=\Pi,\quad\operatorname{rank}\Pi=1,\quad\Pi w=w,
$$
$$
A_7\Pi=\Pi A_7=(1+\omega)\Pi,\qquad
A_{13}\Pi=\Pi A_{13}=\omega\Pi.
\tag{20}
$$
如果有限搜索没有满足这些条件的投影，run 必须失败；
“共同零质量核一维”本身没有被当作简单本征值。

对 (5) 每个实际向量 $f_{a,u}$，完整30个坐标检查
$$
\boxed{\Pi f_{a,u}=\alpha_{a,u}w,\qquad
\alpha_{a,u}=(\Pi f_{a,u})_{28}.}
\tag{21}
$$
公开 run45809854198 的首候选已经成功：
$$
\boxed{a=1,\quad u=7+3\omega,\quad c=0,\quad
q_0(1+\omega)=15-15\omega,\quad
\alpha=\frac{273+156\omega}{185}\ne0.}
\tag{21a}
$$
完整30坐标、秩一幂等及两个方向的 CM 交换均已通过；另外三个候选没有执行。
无需保存生成矩阵或全部系数表；源码、原矩阵哈希、投影哈希、
精确 $\alpha$ 及每一项完整恒等式足够使证书可重建。

## 4. 一个同时容许 CM7、CM13 的完整整六轴框架

以下 $a_{a,u}$ 简记为行向量 $A$，各坐标范数记为 $n_i$。
构造整行矩阵 $L$，第一行就是 $A$。对当前未删指标集 $I$
及要删的 $i\in I$，置
$$
R_I=\sum_{j\in I}n_j,\qquad
v_i=R_I e_i-\overline{A_i}\,A|_I.
\tag{22}
$$
将 $v_i$ 作为下一行后删去 $i$。所有系数都在
$\mathcal O_K$，且
$$
\langle v_i,A\rangle=0,\quad
\langle v_i,v_j\rangle=0\ (i\ne j),\quad
\langle v_i,v_i\rangle=R_I(R_I-n_i).
\tag{23}
$$
第二个等式用较早行在后来的未删坐标上恰是 $A|_I$ 的一个标量倍。

对优先候选 $(a,u)=(1,\gamma_{37})$，按零起始指标
$1,0,4,2,3$ 删除，留下指标5。准确的剩余范数链是
$$
178,\ 166,\ 163,\ 162,\ 155,\ 148,
\tag{24}
$$
所以
$$
L\bar L^t=
\operatorname{diag}\left(
178,\ 178\cdot166,\ 166\cdot163,\ 163\cdot162,\
162\cdot155,\ 155\cdot148\right).
\tag{25}
$$
特别
$$
N(\det L)=148(178\cdot166\cdot163\cdot162\cdot155)^2
\tag{26}
$$
与 $7\cdot13$ 互素。整逆明确为
$$
(L^{-1})_{ji}=\frac{\overline{L_{ij}}}{N_i},
\qquad (N_0,\ldots,N_5)=\operatorname{diag}(L\bar L^t).
\tag{27}
$$
reader 回乘两边逆及全部 Gram。对备选，先试同一个顺序，必要时
只在六个指标的有限排列中选全剩余范数素于 $7,13$、
全部相邻范数乘积为偶的第一个顺序，并同样核完整身份。

每行的偶 theta 半特征都单独核验：它的奇 CM 系数个数为偶。
由 (6) 得完整半特征一，由 (25) 得所有 Gaussian 交叉项零。
因此若新第一物理输出记为 $Y$，另外五个记为 $\mathbf Z$，
$$
\mathcal F_{a,u}:=(au)^{-1}L_*\rho_{\rm raw}
\in\mathcal S_{178}\otimes\mathcal S_{N_1}\otimes\cdots
                          \otimes\mathcal S_{N_5}.
\tag{28}
$$
这保全部六个输入。普通处整性由原 sigma 整有界、固定整线性
换元、各 theta 基互异的首阶单位逐项消元得到。没有除去随
$N_i$ 增长的大阶乘。

以后只排除原固定坏集、(26) 的素因子，以及本次固定
$\Pi,\alpha,a,u$ 的分子分母所需的有限素集。
这些排除不随 $p$ 改变；没有通过自由选列或自由选来源处理每个 $p$。

## 5. 全有限 CM 纤维、奇 sigma 绝对相位与五伴随转移

### 5.1 奇 sigma 的真实相位

norm7、norm13 都使用原
$$
N_\gamma G=\gamma^{-1}\sigma^N
 \operatorname{Tr}_{[\gamma]}
 \left[(r_{\bar\gamma}/r_\gamma)^N
       (G/\sigma^N)\circ[\bar\gamma]\right].
\tag{29}
$$
这包含原半特征与中心，不能重新选取一个 Weil 标量。
对奇 degree1 的 sigma，(29) 的迹只可能在 $O$ 有至多一阶极点，
所以商为常数。reader 从 §2 的实际 CM 群律重建 division 函数，
先核它们与旧 norm7、norm13 的全多项式一致，再在目标
$x=1,2,3$ 的**完整**纤维读出
$$
N_{\gamma_\ell}\sigma=\eta_\ell\sigma,\qquad
N_{\bar\gamma_\ell}\sigma=\bar\eta_\ell\sigma,\qquad
\eta_\ell^6=1\quad(\ell=7,13).
\tag{30}
$$
每个全纤维先核可分性。代码对13还保旧绝对锚
$\eta_{13}=-1$；norm7 的实际值为 $\eta_7=1$，norm13 为 $\eta_{13}=-1$，两者的共轭方向分别相同；本次完整纤维检查全部通过。

(26) 使 $L$ 在 $E[\gamma]^6$ 及 $E[\bar\gamma]^6$ 上都是双射。
因此六输入同时施加 (29) 时可以完整重排六重有限纤维；
(25) 消去交叉 Gaussian，逐行的 (6) 保中心半相位；
两边规范都是 $\gamma^{-6}$。六个输入的 (30) 之积为一，故
$$
\boxed{N_{\gamma,Y}\prod_{\ell=1}^5N_{\gamma,Z_\ell}
       \mathcal F_{a,u}=\mathcal F_{a,u}}
\quad(\gamma=\gamma_7,\bar\gamma_7,\gamma_{13},\bar\gamma_{13}).
\tag{31}
$$
这是整个六变量身份，不是单个第一边际的身份。

### 5.2 原第一轴的逆及完整转移

原 Heisenberg 对称 lift 为
$$
(\mathsf T_v^{(N)}G)(z)=e^{-N\eta_v(z+v/2)}G(z+v).
\tag{32}
$$
沿用 R300(15)–(16) 的模 $2N$ 中心规范。因为 $7,13$ 都素于
$2\cdot178$，$N_\gamma N_{\bar\gamma}$ 实现 Heisenberg 恒等
自同构；不可约性使其为整个 $\mathcal S_{178}$ 的标量。
$W$ 的有理系数、(16) 和两本征值的范数一把该标量定为一。
(17) 另外在完整 principal 块回乘确认同一规范：
$$
N_\gamma N_{\bar\gamma}=I\quad\hbox{on }\mathcal S_{178}.
\tag{33}
$$
它不是只在 $KW$ 上随意定义一个逆。

定义只作用于五伴随的真实算子
$$
B_7=\prod_{\ell=1}^5N_{\bar\gamma_7,Z_\ell},\qquad
B_{13}=\prod_{\ell=1}^5N_{\bar\gamma_{13},Z_\ell}.
\tag{34}
$$
六个奇 sigma 的共同角型为零，故第一轴 principal 平均
$\Pi_{0,Y}$ 在此来源上等于五伴随同时平均 $\Pi_{\mathbf Z}$。
用 (31) 的共轭方向和 (33)，对全部 $j,k\ge0$ 得
$$
\boxed{N_{7,Y}^jN_{13,Y}^k\Pi_{0,Y}\mathcal F_{a,u}
       =B_7^jB_{13}^k\Pi_{\mathbf Z}\mathcal F_{a,u}.}
\tag{35}
$$
两边都保物理 $Y$ 本身。

于是令
$$
\mathcal C_W=\frac{q_c(B_7+cB_{13})}{q_c(e_c)}\Pi_{\mathbf Z}.
\tag{36}
$$
它是固定的有限五伴随算子。由完整第一轴秩一像 (20) 先得到
唯一张量分离，再用真实第一边际 (21) 取质量：
$$
\boxed{\mathcal C_W\mathcal F_{a,u}=W_1\otimes\Lambda,\qquad
                  \Lambda(0)=\alpha.}
\tag{37}
$$
不能由一个边际等式直接推 (37)；这里的原因是 (19)–(20) 的完整
第一轴秩一投影与 (35)。

在原普通整格中，(36) 的有限 CM trace 和平均在上述固定坏集外
整。对第一变量取六阶矩并除以 $720\Omega_p^6$：
$$
\nu_\Lambda=\frac{1}{720\Omega_p^6}
          \int Y^6\,d\nu_{\mathcal C_W\mathcal F_{a,u}},
\tag{38}
$$
得到整有界五变量测度。由本次已证明的 $\alpha\ne0$，在另外排除
其固定分子素因子后，$\nu_\Lambda$ 的 Amice 级数常数为单位，
所以它是完整五变量加法卷积单位。此语句不删除任何混合 cut。

## 6. 同原 $b=17$ 输入到真实 $E_{89}$ 的周期比较

(4)、(11)、(28) 都可在 R465 的原 $E_{17}$ 模型上读取。
对任意固定 $b\ne0$，选相容六次根 $\theta_b^6=b$，则
$$
\sigma_b(z)=\theta_b^{-1}\sigma_1(\theta_bz),\qquad
x_b(z)=\theta_b^2x_1(\theta_bz),
$$
$$
F_{a,u,b}(z)=b^{-1}F_{a,u,1}(\theta_bz),\qquad
W_b(z)=b^{-1}W_1(\theta_bz).
\tag{39}
$$
完整 degree178 块可用齐次基
$b^{28-j}\sigma_b^{178}x_b^{2+3j}$、$0\le j\le29$；
质量列的 $b^{-1}$ 也是固定的，当前普通处为单位。
(15)–(21) 的矩阵与投影系数在这同一基中不变。

取相容普通周期
$$
\Omega_{p,b}=\theta_b^{-1}\Omega_{p,1}.
\tag{40}
$$
这些是同微分、同正式群同构的运输；六次根改变时必须同时改
微分和周期，不能只改 Taylor 系数。把 (39) 代入完整 Amice
变换，准确得到
$$
\nu_{W_{17},p}=\frac{89}{17}\nu_{89,p},
\tag{41}
$$
其中右边正是 R943(27)、(29) 的原 $\Phi_{89}=W_{89}$ 测度。
原2、3、89处 Schwartz 与 primitive Hecke 角色一律由 R943 的
全局识别继承；不是凭 (16) 的两个 CM 值重新猜测角色。

因此在原 $b=17$ 六输入中，(37) 成为
$$
\mathcal C_W\mathcal F_{a,u,17}=W_{17}\otimes\Lambda_{17},
\qquad \Lambda_{17}(0)=\alpha,
\tag{42}
$$
且 (41) 的 $89/17$ 固定单位不可省去。

## 7. 真正给出的中央行，以及所有有限支的单位域

令 $d=p-1$，并以实际物理测度定义
$$
J_{89,p}(v)=\int_{\mathbf Z_p^\times}
                   \langle Y\rangle^{dv}\,d\nu_{89,p}(Y).
$$
对任意完整连续五伴随测试 $h(\mathbf Z)$，(41)–(42) 给
$$
\boxed{\int_{Y\ {\rm unit}}\langle Y\rangle^{dv}h(\mathbf Z)\,
 d\nu_{\mathcal C_W\mathcal F_{a,u,17}}
 =\frac{89}{17}J_{89,p}(v)\nu_{\Lambda_{17}}(h).}
\tag{43}
$$
R943 已证明 $J_{89,p}(0)=0$ 及完整通常 Selmer 桥。
所以在原反证输入 $J'_{89,p}(0)=0$ 下，(43) 对全部独立伴随测试
的中央行均为零。若 $h=h_v$ 解析依赖 $v$，乘积导数的第二项
由同一 $J_{89,p}(0)=0$ 消掉；没有遗漏质量乘尺度对数。

### 7.1 每一条有限 CM 分支

把 $q_c(X)=\sum_{r=0}^{29}q_rX^r$ 代入 (36)。其完整展开系数为
$$
\frac{q_r}{6q_c(e_c)}
          \binom rj c^{r-j},\qquad
0\le j\le r\le29,\quad\zeta\in\mu_6.
\tag{44}
$$
对该项置 $\beta=\gamma_7^j\gamma_{13}^{r-j}$。
原 canonical trace 的全部伴随分支是
$$
\boxed{\nu_{B_7^jB_{13}^{r-j}\mathcal F}
 =\bar\beta^{-5}[I_Y,\bar\beta^{-1}I_5]_*
     \sum_{\mathbf t\in E[\bar\beta]^5}
                     \nu_{\mathcal F_{\beta,\mathbf t}}.}
\tag{45}
$$
这里 $\mathcal F_{\beta,\mathbf t}$ 在第 $\ell$ 个伴随变量中
准确保原
$(\mathsf T_{\beta t_\ell}^{(N_\ell)}\mathcal F)(Y,\beta\mathbf z)$
的对称中心与平移；(32) 的指数及 division 规范一概保留。
(45) 的合成沿同一取向的 CM 素数幂进行，混合的
$\beta,\bar\beta$ 核互素，完整纤维换元无重复或遗漏。
它与 R546(28) 是同一个规范，不把原 trace 变成未定标平均。

因此任何完整测试，包括每个紧开输入域和每个对数，逐支必须读为
$$
\boxed{f(Y,\mathbf Z)\longmapsto
                 f(Y,\zeta\mathbf Z/\bar\beta).}
\tag{46}
$$
此处 $Y$ 本身不缩放，故没有额外的第一轴
$\langle\beta\rangle^{-dv}$。另一方面，凡是混合 $Y$ 与
$\mathbf Z$ 的实际条件，都不能保持原写法或从 (43) 中删掉。

### 7.2 原输入与 $S,T$ 条件逐项返回

完整原未缩放输入是
$$
\boldsymbol\xi=L^{-1}(Y,\mathbf Z)^t.
\tag{47}
$$
所以原任意行输出 $r\boldsymbol\xi$ 在 (45)–(46) 的该支上是
$$
(rL^{-1})_0Y+
       \frac{\zeta}{\bar\beta}
       \sum_{\ell=1}^5(rL^{-1})_\ell Z_\ell.
\tag{48}
$$
所有“单位”“深度至少 $n$”和原 Schwartz 支撑条件均作用于
(48) 的完整表达式；reader 检查
$(a_SL^{-1})L=a_S$、$(a_TL^{-1})L=a_T$，并输出两条精确行。

例如优先候选的第一轴系数准确为
$$
(a_SL^{-1})_0=\frac{26-3\delta}{89},\qquad
(a_TL^{-1})_0=\frac{73-9\delta}{178}.
\tag{49}
$$
它们均非零。因此原 $S$-unit、$T$-deep 等条件仍真实地混合
$Y$。即使 $\nu_{\Lambda_{17}}$ 是加法卷积单位，也不能把这些
条件当作独立伴随测试，更不能把 (43) 的结论赋给任意混合域。

## 8. 公开执行入口、证书及后续消费

复用原
$\texttt{check-original-e89-angular-profile.py}$ 及其现有
$\texttt{rank2-sha-e89-angular-profile.yml}$。
新增 helper
$\texttt{check-original-e89-six-sigma-projection.py}$
在同进程内调用**未修改**的原 degree178 producer 一次，
捕获其实际矩阵。Python3.14 runner 使用明确的
$\texttt{multiprocessing.get_context('fork')}$ 上下文继承已载入的
动态模块；只在这一次 producer 调用期间包裹 executor，退出时恢复，
原四个 worker 与完整数学算法不改。旧完整质量核、旧矩阵哈希、旧角 gcd/导子报告
继续原样检查。reader 只在指定公开 Actions 仓库执行数学，
不在本地执行，不保存生成矩阵或系数文件。

本次已亲读公开作业完整日志，以下接受门全部通过：

1. 原完整矩阵哈希仍为
   $\texttt{6ee0222d90db6add172d6d6e650a2f8186b1776072661594a242b4e65c78d665}$；
2. (13)–(14)、(11) 的全函数域恒等式与候选30坐标；
3. 原实际投影 (18)–(20)、选中候选的精确非零 $\alpha$ 及 (21)；
4. (30) 的两个方向完整奇 sigma 相位及其六次方；
5. (23)–(27) 的全 Gram、两边逆、半特征计数与原 $S,T$ 返回；
6. reader 和源提交、公开 run 标识，不以函数名或状态标签代证书。

本次公开 PASS 实际增加的是：原 $E_{89}$ 的完整中央行在
既有同六 sigma 联合上有一个明确固定的五伴随算子，且伴随质量
是已知非零代数数。它可直接并入旧有限支比较，因为输入、相位、
周期与 (48) 的全单位域都固定。尚须用该新增行连同旧行消费实际
混合余域；没有证明中央泛函对乘积可乘，也没有完成无穷素数结论。

## 依赖

- [R300：原完整 CM trace、Heisenberg 中心与整测度](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)。
- [R465：原共同六 sigma、全部尺度与五伴随来源](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R546：全部五伴随 CM 转移、有限支与真实单位域](R546-original-third-sigma-full-five-companion-cm-transfer.md)。
- [R943：原 E89 全有限角色、Schwartz、完整30维来源与通常 Selmer](R943-original-e89-fifth-central-full-selmer-and-five-axis-gate.md)。

### 首次公开请求的固定源码

- 新 helper：17867 B，SHA256 `954c2855e1f9fcf8ffb1b0f1b172bd18c1732c793fbd71ae4a368dfdb6ac9c87`。
- 既有 angular reader 的接口扩充：11308 B，SHA256 `d6671a67637192b6868fa7ebc487fadca5a8f701064d69cc79ddda6778f3b285`。
- 请求仍只调用这个既有 reader，显式 `--workers=4`，固定 python-flint0.9.0；既有15分钟 workflow 只增新 helper 的触发路径。原 R943 producer 及两个旧 CM 依赖不改。
- 显式 fork 是因同一公开 workflow 的先前 job `139752282740` 已实际使用 Ubuntu26.04 / CPython3.14；Python3.14 默认进程启动方式已经改变，动态载入的同一 producer 模块必须准确继承。[Python3.14 官方说明](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor)。只在本次调用期间选择进程上下文，不修改数学算法或源数据。

### 实际公开回执

- 源提交：`45522b1cbfbb7019945a9bf0b88496c4de5b6d69`。
- [run45809854198](https://github.com/Rogerhu12/math-research-public/actions/runs/45809854198)，job139874554129；2026-11-26 11:22:51 UTC 数学步骤成功结束，完整 angular reader 用时72.83121037483215秒，本篇新增部分51.67668867111206秒，退出码0。
- stdout6778 B，SHA256 `3e00fa429d9b113e48227ba676a608a6c23c319696037026261f5e254196e707`。已从实际报告重新串行化完整 JSON 加末换行，字节数与摘要都准确返回公开捕获值。
- 完整作业日志20541 B（保 UTF8 BOM），SHA256 `7d617af9be1405e29702390eebe8e0e335c5b25e857c715eda82098366398733`。
- 原完整 CM 矩阵摘要仍是上列固定值；q多项式摘要 `ef1b17517193b8713e23dc179d115c7ddc9661e1aa603df8c1d641e62a38fb1c`，完整投影矩阵摘要 `f891b28ec762384fa44b0bf20c2a9ad2c704feb79fba6a7bdc57279d6cf4df7f`。
- 实际候选完整向量摘要 `4363203f28d68044d873fb29f00d41907ee33b2183ce740025094551db704192`；六轴矩阵摘要 `c45442cdab230136b34b88ca0d6afcfa87f0b0a3ed9b0da344b24d5b5577861b`，整逆摘要 `da3d950b351937629df1df4b40123630118edfc313ecf29f1356ab2af809551d`。
- 全部除法函数由实际 CM 群律重建并完成曲线/微分/分母平方回乘；首候选完整30维投影、原两个 CM 逆、四条奇 sigma 相位、六轴 Gram/两边逆/原 S,T 回传全部通过。原矩阵和生成系数没有另存文件。

已付的是完整来源与明确非零投影，(43) 的中央零仍以原反证输入 $J'_{89,p}(0)=0$ 为条件。继续用该真行消费 (48) 的全部混合余域；通常全 Sha 的无穷素数结论尚未完成。


## 9. 同一个 E89 的共轭两轴、完整伴随关系与原三坐标

以下 $u=\gamma_{37}=7+3\omega$，$\bar u=4-3\omega$，
$\alpha=(273+156\omega)/185$，并沿用本篇已核的第一候选、
完整矩阵与原 $b=17$ 六输入。

### 9.1 原完整 rank-one 投影实际上定义在 $\mathbf Q$ 上

置 $A=A_7$、$e=1+\omega$。公开运行已核
$$
A\bar A=I,\qquad e\bar e=1,\qquad
q(e)=15(1-\omega)\ne0,\qquad
\Pi=q(A)/q(e).
\tag{50}
$$
这里 $e$ 是整个30维算子的简单本征值。故 $\Pi$ 是沿
$\operatorname{im}(A-eI)$ 投影到 $\ker(A-eI)$ 的唯一投影。
另一方面，
$$
\bar A-\bar eI=-\bar e A^{-1}(A-eI).
$$
它与 $A-eI$ 的核相同、像也相同。因此共轭后的谱投影满足
$$
\boxed{\bar\Pi=\Pi.}
\tag{51}
$$
完整基 $\sigma^{178}x^2X^j$ 定义在 $\mathbf Q$ 上，所以这是
该**整个矩阵**的有理性；没有只从像线 $KW$ 为有理线推出
投影有理。

候选完整多项式恒等式 (11) 在 $u\mapsto\bar u$ 下逐系数共轭。
由 (21)、(51) 及 $W_1$ 的有理系数，
$$
\boxed{\Pi F_{1,\bar u}=\bar\alpha W_1,\qquad
       \bar\alpha=(117-156\omega)/185\ne0.}
\tag{52}
$$
这是本次原完整矩阵证书的代数后果，不需要第二次数值运行。
$\alpha=39(1+\omega)/(5u)$，故两个质量在当前 $p>211$ 都是单位。

还可明确这里没有新增未显示的大素数分母。原 Heisenberg 共轭作用
在模 $356$ 的有限群上有有限阶 $d$，故 $N_7^d$ 是整个
$\mathcal S_{178}$ 的标量；原 $W$ 锚把它定为 $e^d$。
因此 $N_7^{6d}=I$，所有特征根都是整根单位，
$q\in\mathcal O_K[X]$。原好整格上的 $N_7$ 在
$p\ne2,3,7$ 整，(50) 的分母只添3、5，所以本篇 $\Pi$
在当前所有普通 $p>211$ 均整。

### 9.2 两个整框架和同一个实际五伴随算子

记优先候选的原整框架为 $L_+$，并置
$$
D=\operatorname{diag}(1,1,1,1,1,\bar u/u),\qquad
L_-=L_+D.
\tag{53}
$$
在 (22)、(24) 的构造顺序中，最后一列的每个系数都含有 $u$。
所以 $L_-$ 仍是整矩阵，不是直接容许一个37分母的有限纤维
换元。其首行是
$$
(\delta,2\delta,\gamma_7,\bar\gamma_7,1,2\bar u).
$$
$D\bar D^t=I$，因此
$$
L_-\bar L_-^t=L_+\bar L_+^t
 =\operatorname{diag}(178,29548,27058,26406,25110,22940).
\tag{54}
$$
两行列式的范数相同，均素于7、13；偶半特征的计数也不变，
因为 $u,\bar u$ 在 $\mathcal O_K/2$ 上都是单位。
原 p 处的整性、全部 finite CM 纤维、中心及逆由第4–5节逐项保留。

用原未缩放六输入定义
$$
\mathcal F_+=u^{-1}(L_+)_*\rho_{\rm raw},\qquad
\mathcal F_-=\bar u^{-1}(L_-)_*\rho_{\rm raw}.
\tag{55}
$$
两边的输出坐标都记为 $(Y,\mathbf Z)$，但拉回原六输入时
必须分别用 $L_+$、$L_-$。因为 (54) 的完整 theta 张量格相同，
同一个**坐标中的**五伴随算子
$$
\mathcal C_W=\frac{q(B_7)}{15(1-\omega)}\Pi_{\mathbf Z}
\tag{56}
$$
对它们分别给
$$
\boxed{\mathcal C_W\mathcal F_\pm
       =W_{17}\otimes\Lambda_\pm,\qquad
       \Lambda_+(0)=\alpha,\quad\Lambda_-(0)=\bar\alpha.}
\tag{57}
$$
两条 $\Lambda_\pm$ 都是完整五变量整 Amice 卷积单位。
(56) 相同不表示返回原输入后的两个 source projection 相同：
$L_-\ne L_+$，其第一物理输出也不同。

可进一步保留**整个伴随**的确切共轭关系。令 $Q$ 在原六输入中
同时反射第1、2项，并交换第3、4项，其他项不变。
sigma 奇性给 $Q_*\rho_{\rm raw}=\rho_{\rm raw}$。
$\bar L_+Q$ 的第一行正是 $L_-$ 的第一行。置
$$
M=L_-(\bar L_+Q)^{-1}.
$$
由两个完整 Gram 和相同第一行，
$$
M=\operatorname{diag}(1,M_5).
\tag{58}
$$
其两个方向都在当前 p 处整，因为逆只用 (54) 的固定单位分母。
在代数 theta 来源中先逐系数共轭、再取同一相容 p 周期，
$$
\mathcal F_-=M_*\overline{\mathcal F_+}.
$$
第一轴投影与 $M$ 交换，(51) 因而给
$$
\boxed{\Lambda_-=(M_5)_*\overline{\Lambda_+}.}
\tag{59}
$$
这里的横线先作用于原 $K$-系数；不是随意在
$\mathbf C_p$ 上指定一个共轭自同构。
(59) 也没有把两条伴随直接认成相等。

### 9.3 同一个坏中央给两条完整条件行

两个实际第一输出是
$$
Y_+=A+c+2u d_0,\qquad Y_-=A+c+2\bar u d_0,
\quad
A=\delta\xi_1+2\delta\xi_2+\gamma_7\xi_3+\bar\gamma_7\xi_4.
\tag{60}
$$
在 $J'_{89,p}(0)=0$ 的同一个反证条件下，对任意完整独立伴随
测试 $h_\pm$，准确有
$$
\boxed{
\int_{Y\ {\rm unit}}(p-1)\log_p\langle Y\rangle\,h_\pm(\mathbf Z)
\,d\nu_{\mathcal C_W\mathcal F_\pm}=0.}
\tag{61}
$$
完整 Mellin 恒等式仍各带 (41) 的 $89/17$。
也可以使用解析依赖 Mellin 参数的 $h_\pm$，因为原
$J_{89,p}(0)=0$ 消去其导数质量项。

(56) 的第 $j$ 项仍须完整展开为所有
$E[\bar\gamma_7^j]^5$ 分支，以及六个角支；其尺度
$\bar\gamma_7^{-5j}$、原对称 theta 中心、每个来源和每个
混合条件全部保留。对任何原行 $r$，第 $+$ 或第 $-$ 行的
实际分支切域分别是
$$
(rL_\pm^{-1})_0Y+
 \frac{\zeta}{\bar\gamma_7^j}
       \sum_{\ell=1}^5(rL_\pm^{-1})_\ell Z_\ell
 \quad\hbox{满足原单位或深度条件}.
\tag{62}
$$
所以 (61) 给两个已证明的有限来源和式；不能将其改写成
未投影 $\rho_{\rm raw}$ 上的两个裸对数积分为零。

### 9.4 与旧 S 管的真实单位三角及三坐标

这里的两个共轭轴与旧 $Y_s=A+c+2d_0$ 有特殊的精确关系：
$$
u=1-3\omega\delta,\qquad
\boxed{Y_s=(1+\omega)Y_+-\omega Y_-.}
\tag{63}
$$
令
$$
X=(1+\omega)Y_+,\qquad Z=-\omega Y_-.
$$
两系数都是 $\mu_6$ 单位。在普通 $p\equiv1\bmod6$ 时，
它们的 principal p 进对数为零；单位域也不变。
第一来源 $W$ 的角型为零，故这两个第一轴旋转保 (57) 的 $W$
及其首项规范。于是两条 (61) 可以准确在 $X$、$Z$ 上读取，
而
$$
\boxed{Y_s=X+Z.}
\tag{64}
$$
这是真实单位域中可用的加法关系，未声称中央 Mellin 可乘。

保旧 $W_t=A+3\delta c+4d_0$。从原 $(A,c,d_0)$ 到
$(X,Z,W_t)$ 的行列式准确为
$$
6\delta(3\delta-1),\qquad
N\{6\delta(3\delta-1)\}=3024=2^4\,3^3\,7.
\tag{65}
$$
因此当前 p 处三者是完整单位三坐标，反变换为
$$
d_0=\frac{-\omega X+\omega^2Z}{6\delta},\qquad
c=\frac{W_t-(X+Z)-2d_0}{3\delta-1},\qquad
A=X+Z-c-2d_0.
\tag{66}
$$
特别 R548 的
$$
L_{\rm mix}=(W_t-Y_s)/2
$$
在这同一坐标中是 $(W_t-X-Z)/2$；原
$u_j=cH^{-j}$、$q$ 及全部 $P_j$ 也必须把 (66) 代入完整表达式。

由 (64)，旧 $Y_s$-unit 管有准确的不交分割
$$
\begin{aligned}
\{Y_s\text{ unit}\}
={}&\{X\text{ unit},\,Z\in p\mathbf Z_p\}\\
&\sqcup\{X\in p\mathbf Z_p,\,Z\text{ unit}\}\\
&\sqcup\{X,Z,X+Z\text{ unit}\}.
\end{aligned}
\tag{67}
$$
但这三个域都还须分别经过 (62) 的真实 source projection 返回；
(67) 本身不把它们当成 (61) 中的独立伴随条件。

还有
$$
X=\frac{Y_s+\delta R}{2},\qquad
Z=\frac{Y_s-\delta R}{2},\qquad R=A+c+14d_0.
\tag{68}
$$
这里只把 $R$ 当作一个实际线性输出，未给它新的曲线中央身份。

这段已支付的是 (51)–(67) 的完整共轭行、两伴随关系和可用于旧
管的实际坐标。R548(40) 中的
$\mathcal J$、未投影的 $\rho_0((\Phi_1+\Phi_2)/2-\Phi_0)$、
以及 $h(\Phi_1-\Phi_2)$ 仍必须逐个与 (61) 的**投影后来源和式**
比较；没有将其中任何一项免费置零。
