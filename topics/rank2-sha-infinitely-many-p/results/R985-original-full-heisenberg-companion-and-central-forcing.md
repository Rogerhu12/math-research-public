# R985 — 原完整 Heisenberg 伴随、全22生成与有限中央强迫式

日期：2026-11-26。**已证明：R977 的同一个原六 sigma 全张量允许一族明确的伴随挠点操作，其第一边际生成全部 $V_{130}$；完整 Heisenberg 平均把 R978 的真实非零 old 差写成同一固定 $E_{260}$ 来源的有限挠点变换，并给出准确非零中央强迫式。** 每个相位来自原 sigma，第一 principal 投影的次序始终保留。实际 mixed 测试的对偶由完整有限矩核给出；原共同 carry 也给交换子总和的准确非零读数。挠点变换后的中央泛函与原泛函不同；下文没有把它们免费置零，也没有把此结论当成通常 $\Sha$ 的无穷素数门。

## 1. 同一原 sigma、完整 theta 群与规范

先在原复嵌入写出恒等式，随后用第4节的代数 lift 回到原普通测度格。
令 $\Lambda=\Omega\mathbf Z[\omega]$ 是同一模型的晶格，
$\omega^2+\omega+1=0$、$\delta=1+2\omega$。
原 odd sigma 的准确准周期为

$$
\sigma(z+m)=\chi(m)
 \exp\!\bigl(\eta(m)(z+m/2)\bigr)\sigma(z),\qquad m\in\Lambda.
\tag{1}
$$

这里 $\eta$ 是原准周期的实线性延拓，$\chi$ 是原 odd 半特征。
若 $m=(r+s\omega)\Omega$，则

$$
\chi(m)=(-1)^{r+s+rs}.
\tag{2}
$$

equianharmonic 身份 $\sigma(\omega z)=\omega\sigma(z)$ 给
$\eta(\omega m)=\omega^{-1}\eta(m)$，所以对 $a\in K=\mathbf Q(\omega)$ 有
$\eta(\bar a m)=a\eta(m)$。

对偶数 $N$ 和 $u\in N^{-1}\Lambda$，定义带完整指数因子的算子

$$
\boxed{(T_{N,u}f)(z)=
\exp\!\bigl(-N\eta(u)(z+u/2)\bigr)f(z+u).}
\tag{3}
$$

在整个标准 degree $N$ theta 空间 $\mathcal S_N$ 上它满足

$$
T_{N,u}T_{N,v}
=\exp\!\left(\frac N2(\eta(u)v-\eta(v)u)\right)T_{N,u+v},
\quad T_{N,u}^{-1}=T_{N,-u}.
\tag{4}
$$

若 $m,n\in\Lambda$，Legendre 身份给

$$
E(m,n)=\frac{\eta(m)n-\eta(n)m}{2\pi i}\in\mathbf Z,
$$

故 $T_{N,m/N}$ 与 $T_{N,n/N}$ 的交换子是
$\exp(2\pi iE(m,n)/N)$。式 (1) 又给 $T_{N,m}=I$，因为 $N$ 偶，
所以 $T_{N,u}^{N}=I$。这些绝对相位已固定，不是在证明中为方便重新选根。

## 2. 原 $L_{11}$ 的显式挠点 lift 与全部伴随操作

采用 R977 的真实整框架 $L=L_{11}$，第一行为

$$
a_{11}=(2+\omega,2+\omega,1,\omega^2,1,11),
$$

并且

$$
L\bar L^t=G=\operatorname{diag}(130,1170,54,18,6,2).
\tag{5}
$$

记这些六个数为 $N_0,\ldots,N_5$。原来源为

$$
\mathcal F(Y,Z)=\frac{28}{11\omega}(L_*)\rho,
\qquad\rho=-\nu_\sigma^{\otimes6}/84,
$$

其生成函数是同一固定常数乘
$\prod_{j=0}^5\sigma((L^t(Y,Z))_j)$；第一边际是 R977 已完整构造的 $F_{11}$。

原输入的第4列（从零计数）的第一行系数为一。对任意 $m\in\Lambda$，取

$$
k(m)=L^{-t}e_4m.
$$

由原已返回的完整逆矩阵得到准确六个坐标

$$
\boxed{k(m)=\left(
\frac m{130},\ -\frac{11m}{1170},\
\frac{(\omega^2-1)m}{54},\
\frac{(\omega^2-1)m}{18},\ -\frac m6,\ -\frac{\omega^2m}{2}
\right).}
\tag{6}
$$

这里 $L^t k=e_4m$ 在全部六个坐标上成立，不只在第一行成立。每个
$N_i k_i$ 都属于 $\Lambda$；所有实际中心的阶均整除
$\operatorname{lcm}(N_i)=3510$。

对全张量同时作 (6) 的平移，原六个 sigma 中恰有第4个增加完整周期 $m$。
于是 (1) 给

$$
\mathcal F(z+k)=\chi(m)
 \exp\!\left(\eta(m)((L^t z)_4+m/2)\right)\mathcal F(z).
\tag{7}
$$

式 (3) 的六个指数恰好消掉 (7) 的整个指数。确实
$k_i=\overline{L_{i4}}m/N_i$，故

$$
N_i\eta(k_i)=L_{i4}\eta(m),\qquad
\sum_i\frac{|L_{i4}|^2}{N_i}=1.
\tag{8}
$$

第二式是 $L^tG^{-1}\bar L=I$ 的第 $(4,4)$ 项。因此完整身份为

$$
\boxed{\left(\prod_{i=0}^5T_{N_i,k_i(m)}\right)\mathcal F
=\chi(m)\mathcal F.}
\tag{9}
$$

令 $u=m/130$，并定义只在五个伴随上作用的真实算子

$$
\mathscr R_m=\chi(m)\prod_{i=1}^5T_{N_i,-k_i(m)}.
$$

则 (4)、(9) 给

$$
\boxed{\mathscr R_m\mathcal F=T_{130,u,Y}\mathcal F.}
\tag{10}
$$

式 (6)、(2)、(3) 已给全部中心、指数因子和绝对符号。它不是一个只在 projective theta 群商上成立的“相差某标量”关系。

## 3. 保持 $\Pi_0T_u$ 次序的全22维生成

令 $\Pi_{0,Y}$ 为第一轴完整 $\mu _6$ principal 平均。
原六 sigma 在六输出同时旋转下不变，所以

$$
\mathcal G:=\Pi_{0,Y}\mathcal F=R_{0,Z}\mathcal F,
\qquad \operatorname{im}\Pi_{0,Y}
=V_{130}=\sigma^{130}x^2K[X]_{\le21}.
\tag{11}
$$

$R_{0,Z}$ 是五个伴随的同时 principal 平均。它保持第一边际 $F_{11}$。
由 (10) 及不同输出上的算子交换，得到

$$
\boxed{\mathscr R_m\mathcal G
=\Pi_{0,Y}T_{130,u,Y}\mathcal F.}
\tag{12}
$$

其第一边际准确为 $\Pi_0T_{130,u}F_{11}$。这里必须保持显示的次序；
一般不能把它换成 $T_{130,u}\Pi_0F_{11}$。

完整 finite Heisenberg 作用在 $\mathcal S_{130}$ 上不可约，这一点可在此直接证明。
取定向周期基 $m_1,m_2$，使 $E(m_1,m_2)=1$。两个生成元 $U,V$ 满足
$U^{130}=V^{130}=1$、$UV=\zeta_{130}VU$。
取 $U$ 的任一非零本征向量；其 $V^j$ 轨道有130个互异本征值，因而线性独立。
而椭圆曲线上正 degree130 线丛的全截面空间维数恰为130，故该轨道已经是全基。
这也证明任何非零向量的完整 Heisenberg 轨道张成全空间。

$F_{11}\ne0$，故对 $m$ 遍历 $\Lambda/130\Lambda$ 的固定 $130^2$ 个代表，有

$$
\operatorname{span}\{T_{130,m/130}F_{11}\}=\mathcal S_{130}.
$$

再作完整 principal 投影，得到

$$
\boxed{\operatorname{span}\left\{
\text{第一边际}(\mathscr R_m\mathcal G):m\in\Lambda/130\Lambda
\right\}=V_{130}.}
\tag{13}
$$

这给原全张量上的实际有限伴随操作，而不是把 $H$ 当作外加生成元。
它也解释为什么 R980 的好位 Hecke 模只有19维并不限制 (13)：这些挠点操作不是
$K[B_7,B_{19}]$ 的标量角色操作。某个块的第一边际为零，也不意味着它的完整伴随张量为零。

## 4. 原相位的代数性、Miller 全矩阵与整测度

第1–3节的精确解析规范可以完全代数化。对非零 $u\in E[N]$，取唯一归一的实际 Miller 函数

$$
\operatorname{div}(r_u)=N[-u]-N[O],\qquad
r_u(z)=z^{-N}+\cdots\quad(z\to0).
\tag{14}
$$

它存在，因为 $Nu=0$；归一把常数固定为一。系数属于一个固定的代数 torsion 域。
若 $f=\sigma^N R$，则直接由 (3) 得

$$
\boxed{T_{N,u}(\sigma^N R)
=c_u\sigma^N r_u\,(R\circ\tau_u),\qquad
c_u=e^{-N\eta(u)u/2}\sigma(u)^N.}
\tag{15}
$$

右边的全部极点在整式中抵消到 $O$，极阶至多 $N$，因为左边属于同一个全
$\mathcal S_N$。式 (15) 因而给整个 $N\times N$ 矩阵的有限计算：使用完整曲线群律计算
$R(P+u)$，乘完整 $r_u(P)$，再在全 $L(NO)$ 基上返回所有系数。它不以有限若干 Taylor 行外推整个算子。

这里 $c_u$ 也是代数数，不能把这个环节留成未经证明的 CM 周期猜测。置

$$
A_u=\prod_{j=0}^{N-1}(r_u\circ\tau_{ju}).
$$

全部除子准确望远镜相消，故 $A_u$ 是非零代数常数。迭代 (15)，再用
偶数 $N$ 的 $T_{N,u}^{N}=I$，给

$$
\boxed{c_u^{N}A_u=1.}
\tag{16}
$$

所以 (15) 的原 $c_u$ 为代数；其准确根由原 sigma 的 (15) 固定，不是在后续
$p$-进比较时任择一个 $N$ 次根。对 $u=0$ 直接使用恒等算子；周期代表的改变按 (4) 的已付相位处理。

本篇所用中心、$N_i$ 及算子都只有固定有限多个。将它们的全部坐标、$c_u$ 和矩阵系数加入一个固定有限域，清掉固定整数 $D$，则全部实际算子和逆都保持原全 theta 整格。在与原 sigma 对应的 ordinary Amice 实现中，它们因此是有界测度算子，适用于每个
$p\nmid D$ 的原普通 ray。这里的 $D$ 与 $p$ 无关；未声称已经计算了它的最小值。

式 (15) 还确定每个中央泛函的真正有限变换。若 $M_{N,u}$ 是这个完整矩阵，
$\ell_p$ 是原空间上的任意线性测度泛函，则其对偶严格为

$$
\boxed{T_{N,u}^{\dagger}\ell_p=\ell_p\circ T_{N,u},
\qquad [T_{N,u}^{\dagger}\ell_p]=M_{N,u}^{t}[\ell_p].}
\tag{17}
$$

这包含原指数因子及完整 torsion 平移。它不是在物理测度变量中擅自作
$x\mapsto x+u$。实际单位 cut 或 logarithm 的变换必须通过同一个全算子的对偶完成。

## 5. 一条固定秩二来源的完整有限分解

令

$$
P=\Pi_{260}\Pi_0:\mathcal S_{130}\longrightarrow K\Phi_{260,1}.
\tag{18}
$$

这里 $\Pi_{260}$ 是 R973/R976 已付全部有限角色后确定的完整 CM 投影，
$P$ 在全 $\mathcal S_{130}$ 上的秩为一、迹为一；它的定义包括第一 principal 投影。
写

$$
P(v)=\Phi_{260,1}\,\ell(v),\qquad\ell(\Phi_{260,1})=1.
$$

$\ell$ 可以具体取“施 $P$ 后读 $V_{130}$ 第20坐标”，所以不是新选择的未知线性泛函。

有限 Heisenberg 的完整共轭平均给

$$
\boxed{\frac1{130}\sum_{u\in E[130]}T_uPT_u^{-1}=I_{\mathcal S_{130}}.}
\tag{19}
$$

证明如下：和式与全部 $T_v$ 交换；由第3节的不可约性，它为标量。
每项迹为一，项数为 $130^2$，总空间维数为130，故标量是130。各中心的标量
lift 在共轭中完全抵消，因此 (19) 与第1节的原精确 lift 一致。

对任意全来源 $v$，得到准确有限公式

$$
\boxed{v=\frac1{130}\sum_{u\in E[130]}
 c_u(v)\,T_u\Phi_{260,1},\qquad
c_u(v):=\ell(T_u^{-1}v).}
\tag{20}
$$

本式中的 $c_u(v)$ 是 (15)、(18) 的固定有限代数计算；它们不依赖素数 $p$。
这里 $c_u(v)$ 是一个带参数的系数记号，勿与 (15) 单算子的指数标量 $c_u$ 混同。

式 (19) 也能直接作用到原**整个六变量张量**。由 (10)，

$$
P_YT_{-u,Y}\mathcal F
=P_Y\mathscr R_{-m}\mathcal F
=\Phi_{260,1}\otimes\Lambda_m.
\tag{21}
$$

于是

$$
\boxed{\mathcal F=\frac1{130}\sum_{m\bmod130\Lambda}
(T_{m/130}\Phi_{260,1})\otimes\Lambda_m.}
\tag{22}
$$

全部 $\Lambda_m$ 都是原输入上的确定五伴随来源。其质量为
$\ell(T_{-u}F_{11})$，允许为零；仅 $m=0$ 已由 R977 实际返回
$\Lambda_0(0)=1400/33$，不能把这个单位性挪给所有 $m$。
对 (22) 左右作第一 principal 投影，得到原 $\mathcal G$ 的完整分解，右边各项须保持
$\Pi_0T_{m/130}\Phi_{260,1}$ 的顺序。

## 6. 由原 old 差得到准确非零中央强迫

沿原 ordinary ray，置 $d=p-1$，记

$$
j_p(v)=\left.\frac{d}{ds}\right|_{s=0}
\int_{\mathbf Z_p^\times}\langle x\rangle^{ds}\,d\nu_v(x).
\tag{23}
$$

单位域及其 logarithm 都对 $\mu _6$ 不变，所以 $j_p=j_p\Pi_0$。
R973 已付的是：$j_p(\Phi_{260,b})\ne0$ 蕴含该固定曲线的通常全
$\Sha[p^\infty]$ 有限。其值为零只是研究联合坏素数时的假设，不能由曲线秩至少二推出；即使作这个假设，也不能给
$j_p(T_u\Phi_{260,b})$ 免费赋零。

取 R978/R980 的同一真实来源

$$
V_{\rm old}:=\Pi_{5,4}H-\frac{11}{23625}\Pi_{5,4}F_{11}
=\frac{\delta}{1701000}
 \bigl(\Psi_{10}(\pi_{13}z)-\Psi_{10}(\bar\pi_{13}z)\bigr),
\tag{24}
$$

其中 $\Psi_{10}=\sigma^{10}x^2(X+10)$、$\pi_{13}=(7+\delta)/2$。
在共同物理模型 $b=17$、同一原周期与测度格中，R978 给

$$
j_p(V_{{\rm old},b})
=\frac{\delta d}{1701000b}
\log_p\!\left(\frac{\pi_{13}}{\bar\pi_{13}}\right)
 (1-\chi_{10}\lambda)\ne0.
\tag{25}
$$

在相同物理规范下把 (20) 应用于 $V_{{\rm old},b}$，得到本篇的具体有限强迫式

$$
\boxed{\sum_{u\in E_b[130]}
\ell_b(T_u^{-1}V_{{\rm old},b})\,
j_p(T_u\Phi_{260,b})
=\frac{130\delta d}{1701000b}
\log_p\!\left(\frac{\pi_{13}}{\bar\pi_{13}}\right)
 (1-\chi_{10}\lambda)\ne0.}
\tag{26}
$$

右端非零由不同13素理想的赋值和原 $1-\chi_{10}\lambda$ 单位性支付。
左端系数由固定有限的 Miller／CM 全算子确定；无遗漏的非 $\mu _6$ 或 old 分量。
$u=0$ 的系数为零，因为 $V_{\rm old}$ 与 $(4,5)$ 是不同的完整共同块。

因此不可能把所有实际挠点变换后的中央测试同时置零。特别地，在这固定有限族中至少有一个变换测试对无穷多个原普通 ray 素数非零。这个有限族结论只使用 (26) 和普通 ray 的无穷性；它不把变换后的测试混称为原通常 Selmer 比较所需的未变换算术分支。

## 7. 同一共同 carry 与全 mixed 域的保留

R977 已返回原 $C,F$ 均正交于第一观察 $a_{11}$。因此它们在 $(Y,Z)$ 坐标中只读
$Z$，而 (10)、(18)、(21) 的第一轴算子只读 $Y$。
R968 的 carry 是先推前到 $\ker C\cap\ker F$ 的**整个四输出**后的测度身份，故可以在该四输出身份两侧施
$T_u$、$\Pi_0$、$P$。式 (21) 的来源及其在 (22) 中的组合在作这同一个四输出推前后，都保留该 carry；这里没有给原六变量含全部五伴随的来源断言加权前后成比例。

这不是声称单独的伴随算子 $\mathscr R_m$ 与任意 cut 交换。
它是先用已付 (10) 将 $\mathscr R_m$ 在原全张量上的作用写回第一轴，再对完整 carry 身份施同一线性算子。

下面把 (17) 的抽象矩阵对偶写成实际测试的完整有限核，因而无需把 mixed 域留成一个未定义的“变换”。对 $N=130$ 的全空间取原曲线上的基

$$
B_j\in\{\sigma^N x^a:0\le a\le N/2\}
\ \cup\ 
\{\sigma^N x^a y:0\le a\le (N-4)/2\},
$$

按各自不同首阶 $r_j$ 递增排列。首阶集准确为

$$
\{r_j\}=\{0,1,\ldots,N-2,N\}.
$$

首项对角为原 $x,y,\sigma$ 规范给出的非零数。令

$$
J_{ij}=[z^{r_i}]B_j(z),\qquad
q_{j,p}(Y)=\sum_i(J^{-1})_{ji}
 \frac{Y^{r_i}}{r_i!\,\Omega_p^{r_i}}.
\tag{27}
$$

$J$ 是可逆三角矩阵。原 Amice 规范
$\mathcal A_{\nu_f}(T)=f(\Omega_p\log(1+T))$ 给
$\nu_f(Y^r)=r!\Omega_p^r[z^r]f$，所以

$$
\nu_f(q_{j,p})=[f]_{B_j}.
\tag{28}
$$

这里使用原实际 $\Omega_p$；没有把不同微分或 period 的因子归一掉。
有限多个 $r_i!$ 只增加固定有限坏素数。对任意连续 mixed 测试
$\tau(Y,Z)$，定义

$$
\boxed{(T_{u,Y}^{\dagger}\tau)(Y,Z)=
\sum_j q_{j,p}(Y)
 \int_{\mathbf Z_p}\tau(y,Z)\,d\nu_{T_uB_j}(y).}
\tag{29}
$$

各 $\nu_{T_uB_j}$ 是第4节同一有限代数 lift 的有界测度；积分作为 $Z$ 的函数连续。若
$\mu=\sum_j\nu_{B_j}\otimes\mu_j$ 是全 $\mathcal S_N$ 第一轴来源，式 (28) 逐基给

$$
\boxed{\langle T_{u,Y}\mu,\tau\rangle
=\langle\mu,T_{u,Y}^{\dagger}\tau\rangle.}
\tag{30}
$$

这是真正的完整测试转置，不要求原测试本身是一个有限多项式。
例如对任意旧观察的完整行 $aY+bZ$，若

$$
\tau_v(Y,Z)={\bf1}_{aY+bZ\in\mathbf Z_p^\times}
 \langle aY+bZ\rangle^{(p-1)v}h(Z),
$$

式 (29) 的第 $j$ 个内核准确为

$$
h(Z)\int_{ay+bZ\in\mathbf Z_p^\times}
\langle ay+bZ\rangle^{(p-1)v}\,d\nu_{T_uB_j}(y).
\tag{31}
$$

其 $v=0$ 导数就在同一个域内插入
$(p-1)\log_p\langle ay+bZ\rangle$。多个单位、深管或其补域的指标直接同时留在
$\tau$ 中，式 (29) 原样适用。原 torsion 支的中心也完整留在原行中。

因此 (22) 给任意原 mixed 测试的真实全分解

$$
\langle\mathcal F,\tau\rangle
=\frac1{130}\sum_m
\left\langle\nu_{\Phi_{260,1}}\otimes\nu_{\Lambda_m},
 (T_{m/130,Y}^{\dagger}\tau)\right\rangle.
\tag{32}
$$

这里 $T^{\dagger}$ 的每个内核就是 (29)，因此指数因子、原 $S,T,W^\pm,Z$ 的所有单位或深域条件以及 logarithm 都已完整保留。式 (32) 不把某个变换后来源的中央零传播到未变换的旧 cut。

而且对于任何只读原 $C,F$ 的连续有界测试 $q(C,F)$，它在上述坐标中只读 $Z$，从 (29) 直接得到

$$
T_{u,Y}^{\dagger}(q(C,F)\tau)
=q(C,F)T_{u,Y}^{\dagger}\tau.
\tag{33}
$$

这是实际测试上的交换关系，涵盖 R968 的完整加权 carry；不要求先删掉其补域。

## 8. 共同 carry 下交换子的准确非零总和

对 (24) 的两个原观察，各取实际四输出映射

$$
\eta_i=(Y_i,Z_{i,1},Z_{i,2},Z_{i,3}),\qquad i=H,11,
\tag{34a}
$$

其四条整行在清固定分母后构成同一 $\ker C\cap\ker F$ 的一组坐标。
$Y_{11}$ 是原 $a_{11}$ 观察；$i=H$ 取 R961 的真实轴
$Y_H=A_{65}=(\delta,2\delta,\gamma_7,\bar\gamma_7,a,18)$，其中
$a=\gamma_{37}=7+3\omega$。本节明确选择如下完整 lift，而不把它和另一条跨项的整个联合测度认同。

R961 的原规范化是 $(9a)^{-1}\eta_{H,*}\rho$；其第一轴真实投影满足

$$
\Pi_ZF=\alpha_Z Z,\qquad
\alpha_Z=\frac{25\omega}{72a}=\frac{-25+175\delta}{5328}.
$$

在全来源上，R961 已付 $\Pi_Z\mathcal F=Z\otimes\Lambda_Z$ 且
$\Lambda_Z(0)=\alpha_Z$。令

$$
S(X)=\frac{X(X-8)}{7X^2-4X+16},\qquad
A_H=T_{\delta,130}\circ M_S\circ
\alpha_Z^{-1}\Pi_Z\circ(9a)^{-1},\qquad
A_{11}=\frac{28}{11\omega}.
\tag{34c}
$$

$M_S$ 在这里**只作用于已经投到 $Z$ 的像**。R962(11) 的完整身份
$P_Z=X(X+1)(7X^2-4X+16)R_{60}$ 消掉了 $S$ 的全部有限极点，
所以 $M_S(Z\otimes\Lambda_Z)=SZ\otimes\Lambda_Z$ 是整个无极来源。
没有将 $M_S$ 当作全 $\mathcal S_{390}$ 上的无极自同态。
随后 $T_{\delta,130}$ 是 R972 的全部66列→22列原 trace，因此这个特定
$A_H\eta_{H,*}\rho$ 的第一边际准确为 $T_{\delta,130}(SZ)=H$。
全部算子都在 $\eta_{H,*}$ **之后**只作用于第一轴。
从而定义

$$
\mathcal H^{(4)}=A_H\eta_{H,*}\rho,\qquad
\mathcal F_{11}^{(4)}=A_{11}\eta_{11,*}\rho.
\tag{34b}
$$

每个对象都已是四输出测度。为不把两个不同实际观察误当作同一物理轴，保留这两个四输出来源的有序直和，再分别施第一轴 old 投影：

$$
\mathcal G_{\rm old}
=\left(\Pi_{5,4}\mathcal H^{(4)},
 -\frac{11}{23625}\Pi_{5,4}\mathcal F_{11}^{(4)}\right).
$$

记“第一边际”为各自取边际后相加的映射，则它恰好给 (24)；没有断言两条不同观察的完整联合测度相等。
第一轴算子在这个有序直和上分别作用。每项都经过完整 $\Pi_{5,4}$，故
$P_Y\mathcal G_{\rm old}=0$ 是全来源身份，而不只是一条边际零。

使用 $[P,T_u^{-1}]=PT_u^{-1}-T_u^{-1}P$，由 (19) 得

$$
\boxed{\sum_{u\in E[130]}
 T_u[P,T_u^{-1}]\mathcal G_{\rm old}
=130\mathcal G_{\rm old}.}
\tag{34}
$$

全算子的定义与 (15)–(18) 相同；所有 old 重数、非 $\mu_6$ 中间分量和补域均在等式内。令
$\mathcal G_{\rm old}^{[n]}$ 表示在 (34b) 中将每个
$\eta_{i,*}\rho$ 替成 $\eta_{i,*}(\mathfrak q_{n,p}^{\rm new}\rho)$，
然后作相同的 $A_i$、第一轴 old 投影及有序直和。
R968 的真实接口逐项给

$$
\eta_{i,*}(\mathfrak q_{n,p}^{\rm new}\rho)
=\upsilon_p^n\eta_{i,*}\rho.
\tag{35a}
$$

第一轴算子与忘掉另两输出的推前交换；(33)也说明其真实测试对偶保该加权次序。因此只在这个已推前的四输出有序直和中得到

$$
\mathcal G_{\rm old}^{[n]}
=\upsilon_p^n\mathcal G_{\rm old},\qquad
\upsilon_p=\chi_{10}\lambda.
\tag{35}
$$

在共同物理模型 $b=17$ 上，对 (34) 的加权版本取第一边际和原中央导数，得到

$$
\boxed{\sum_u j_p\!\left(
 \text{第一边际}\bigl(T_u[P,T_u^{-1}]
 \mathcal G_{{\rm old},b}^{[n]}\bigr)\right)
=\frac{130\upsilon_p^n\delta(p-1)}{1701000\cdot17}
\log_p\!\left(\frac{\pi_{13}}{\bar\pi_{13}}\right)
(1-\upsilon_p)\ne0.}
\tag{36}
$$

因此共同 carry 的存在并不能使全部这些实际交换子中央读数同时为零。
这条准确非零关系把需要控制的非交换部分落实在固定的完整有限族上；它不把未付的交换子消去作为假设。

本篇给出的新增输入是：显式中心 (6)、全相位 (9)、全22伴随生成 (13)、原代数 lift (15)–(17)、整个六变量有限分解 (22)、实际非零的固定有限中央关系 (26)、完整 mixed 测试核 (29)–(33) 以及原共同 carry 下的非零交换子式 (36)。要由这些关系完成原课题，仍须把 (26) 中足够多的变换测试接入已付的通常 Selmer／真实 forcing 机制；单凭它们来自同一固定算术来源的挠点轨道，不会自动满足该机制。

## 依赖

- R977：原 $L_{11}$ 全整 Gram、双逆、$F_{11}$、$1400/33$ 实际投影及共同 $C,F$。
- R973/R976：$E_{260}$ 的完整有限角色、原秩至少二证明与 rank-one 全 CM 投影。
- R978/R980：原两 old 拉回、式 (24) 的全来源身份和明确非零的普通 Mellin 差。
- R968：保全部四输出及其任意 mixed 条件的原共同 carry。

这里没有新增数值试验或读取生成矩阵；完整 theta 群和有限平均身份由原实际框架、sigma 准周期及全空间维数直接证明。
