# R119 续篇：实际严格段的全输入高输出与根斜率单位余项

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 对[控制后同参数实际尾](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md)
的每个完整内部负分量，在两个原 fixed radial strict cuts 之间，取较深
胞元编号 $j$，置

$$
J=j+5,\quad \delta=\delta_j,\quad
\lambda_j=2^{32}\sqrt J\,\delta^{-9/4},\qquad
L_j=2^{4200}\lambda_j,\qquad P_j=\mathbf1_{\{|m|\ge L_j\}}.
\tag{S.1}
$$

令 $U_{\rm st}(t,s)$ 为两条真实特征流拉回后的完整密度演化，
包括两个独立 mean；在非mean上采用
$|D_\theta|^{-1/2}Z_\sigma$ 的平衡，与第51束 (H.11) 相同。
同支反自伴 generator 的准确积分记为 $B_{\rm st}$。
在相同完整空间 $\mathcal W_s=\mathbb C^2\oplus(H^s_0)^2$ 中，
对 $|s|\le1$ 有

$$
\boxed{\quad
\|P_jU_{\rm st}(t,s):\mathcal W_s\to\mathcal W_s\|<2,
\qquad
\|P_j(U_{\rm st}-e^{B_{\rm st}}):
       \mathcal W_s\to\mathcal W_{s+2}\|<2^{2048}\lambda_j^2,
\quad}
\tag{S.2}
$$

$$
\boxed{\quad
\|P_j(U_{\rm st}-e^{B_{\rm st}}):
       \mathcal W_s\to\mathcal W_{s+4/3}\|
 <2^{1400}\lambda_j^{4/3}.
\quad}
\tag{S.3}
$$

第一式对任意两个 strict 截面成立，两个方向均可；余项式对整个
strict 段及其任意子段均成立。输入未截断，mean、跨锥和低到高列
全部保留。实际 principal 密度角图在输出端准确恢复；
这不是裸 pullback 的同阶小差估计。
本篇仍不把这些单段结论当作整个两根—正型网络已经重新复合的定理。

## 1. 同一实际 profile 给更精确的势积分

严格区的真实径向参考使用同一个最终 $\Gamma^*(a,\Omega)$ 和同一个
径向控制 $\Omega$，不是旧零标签参数。写 $a_e=\eta_e/\sqrt{12}$ 为
某条真实 log-quintic 的 $t$ 长度，$B_e=\Delta_e/a_e$。
实际几何和两 bump 复盒给

$$
a_e={\delta_e^{3/2}\over8\sqrt6},\quad
80<\Delta_e<4J,\quad B_e>2^{190},\quad
a_e\Delta_e<1,\quad
{\sqrt{B_e}\over a_e}<\lambda_j,\quad b_e<\lambda_j .
\tag{S.4}
$$

根斜率的最后一式是原参考根公式
$b_e<2^{16}\sqrt J\,\delta_j^{-9/4}$。
其余式来自 $1/a_e<2^5\delta_e^{-3/2}$、
$B_e<2^7J\delta_e^{-3/2}$、$\delta_e\ge\delta_j$；
所有相关指标至少为128，$J<2^j$ 足以给 $a_e\Delta_e<1$。
原平移只互换等长的 $Q=7$ 平台，不改变以下积分。

在未改下降坡上 $Q=7+Bf(x)$，在上升坡的两个负型翼上
$Q=7-Bf(x)$，其中

$$
f(x)=30x^2(1-x)^2,\qquad dt=a\,dx.
\tag{S.5}
$$

在 $0\le x\le1/2$，

$$
{15\over2}x^2\le f(x)\le30x^2,\quad
|f'(x)|\le60x,\quad |f''(x)|\le60,\quad |f'''(x)|\le360.
\tag{S.6}
$$

另一半由 $x\mapsto1-x$ 处理。下降坡因此有
$|Q_t|\le32\lambda_j\sqrt Q$、
$|Q_{tt}|\le64\lambda_j^2$。
上升负型翼只使用 $Q>q_0=1/128$ 的部分，其长度在 $x$ 中
小于 $B^{-1/2}$，且
$|Q_t|\le32\lambda_j\sqrt7$、
$|Q_{tt}|\le64\lambda_j^2$。

原两个 bump 和新增 $C^4$ 形状的所有支集均在
$[1/8,7/8]$ 内，且互不重叠。
实际参数盒、$\Delta>80$、
$\|[64z^3(1-z)^3]^{(4)}\|_\infty\le4608$、
两个尺度8和32，以及 $\|\Xi\|_{C^4}<2^{-64}$ 逐项给

$$
Q\ge B/8,\qquad Q<4B,\qquad
|\partial_x^kQ|<2^{20}B\quad (1\le k\le3)
\tag{S.7}
$$

于这些支集。这个宽界同时覆盖原两个有实际跳幅的 $C^2$ bump；
新增形状的零延拓为 $C^4$，不增加所需的 $Q_{tt}$ 跳原子。
所有真实光滑片和接缝总数仍小于32。

完整 wave 势为

$$
V_w={Q_t\over2Q}-{(1+Q)^2\over4Q}
              +{5Q_t^2\over16Q^3}-{Q_{tt}\over4Q^2}.
\tag{S.8}
$$

其积分按真实 optical 长度 $d\ell=\sqrt Q\,dt$ 取。
下面给每类项的实际尺度，而不是把径向导数 supremum 乘整段长度：

* 下降坡的 $Q_{tt}$ 项用
  $\int_0^\infty(7+(15/2)Bx^2)^{-3/2}dx=[7\sqrt{(15/2)B}]^{-1}$，所以
  $\int |Q_{tt}|Q^{-3/2}dt<2^{10}\lambda_j$。
  $Q_t^2$ 项在两个单调半坡分别换元 $Q$，也小于
  $2^{10}\lambda_j$。
* 上升负型翼用其真实长度 $a/\sqrt B$ 和 $Q>q_0$。
  同样两项分别小于 $2^{18}\lambda_j$ 和
  $2^{20}\lambda_j$；第一导数项直接为
  $\int Q^{-1/2}|dQ|$。
* 下降坡 reaction 的最大尺度是
  $aB^{3/2}=(\sqrt B/a)\,a^2B=(\sqrt B/a)\,a\Delta<\lambda_j$。
  这一步是不能丢失的真实短坡长度；平台和上升翼的 reaction 更小。
* 在 (S.7) 的各支集上直接代入，最坏项是
  $2^{48}/(a\sqrt B)\le2^{48}\lambda_j$。
  其它项是 $C\sqrt B$、$CaB^{3/2}$ 或
  $C/(a\sqrt B)$，均已由 (S.4) 支付。

加所有片，安全地得到

$$
I_1:=\int |V_w|\,d\ell<2^{256}\lambda_j .
\tag{S.9}
$$

同样保留完整 BV 费用。每片准确有

$$
(V_w)_t={Q_{tt}\over2Q}-{Q_t^2\over2Q^2}
 -{1-Q^{-2}\over4}Q_t+{9Q_tQ_{tt}\over8Q^3}
 -{15Q_t^3\over16Q^4}-{Q_{ttt}\over4Q^2}.
\tag{S.10}
$$

在未改坡上，统一可用
$Q_t^2<2^{20}\lambda_j^2 Q$。含 $Q_tQ_{tt}$ 和 $Q_t^3$
的积分在各单调片换元 $Q$，由
$\int_{q_0}^\infty Q^{-3}dQ=2^{13}$ 控制。
$Q_{ttt}$ 项在下降坡用
$\int(7+(15/2)Bx^2)^{-2}dx<C B^{-1/2}$，
在上升翼用其 $B^{-1/2}$ 长度；所得尺度为
$\sqrt B/a^2\le B/a^2\le\lambda_j^2$。
前两项同理小于固定常数乘 $\lambda_j$，reaction 的总变差
小于固定常数乘 $B\le\lambda_j^2$。

在修改支集上，(S.10) 的最大尺度是
$2^{72}/(a^2B)\le2^{72}\lambda_j^2$。
每个原接缝的实际跳变来自 $-Q_{tt}/(4Q^2)$；
以全部小于32片的两侧迹求和，费用仍小于
$2^{100}\lambda_j^2$。同一逐项界也支付 $V_w$ 的 supremum。
因此

$$
I_2:=\|V_w\|_\infty+\operatorname{Var}V_w
                         <2^{512}\lambda_j^2 .
\tag{S.11}
$$

变换 $t\mapsto\ell$ 严格单调，不改变总变差。
没有对新的 $C^4$ profile 索取第五阶或更高统一导数。

## 2. 从径向高输出到实际全输入高输出

保留[完整严格密度篇](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
的精确重建
$w=c_0+\alpha(S_+-S_-)-i\sum C_{S_\sigma}D^{-1}Z_\sigma$，
包括两个独立 mean。
令 $\mathcal A$ 为真实固定标签 generator，$\mathcal A_0$ 为同一
$Q_{\Gamma^*,\Omega}$ 的径向 generator。
该篇 (S.22) 已经证明的是一个**完整同阶 generator 差**；
它不是裸 $C_H-C_{H_0}$ 的同阶界。
作本篇的半阶平衡、使用已重新实例化的 $N_j^c$ 后，可安全取

$$
n_i=4(N_j^c)^\#\mathcal X,\quad
\int\|\mathcal A-\mathcal A_0\|_{\mathcal W_r\to\mathcal W_r}dt
 <E_i:=2^{300}J^3\delta^{-5}n_i,\qquad |r|\le3 .
\tag{S.12}
$$

半阶平衡在非mean上只是同一个 Sobolev 指数移动；
mean 与非mean间的解析列再消费一个固定角余宽，其费用包含在
$2^{300}$ 中。旧完整正逆界仍是

$$
\|U_{\rm st}(t,s)\|_{\mathcal W_r\to\mathcal W_r}
 <G_i:=2^{1024}J^5\delta^{-10},\qquad |r|\le3 .
\tag{S.13}
$$

同参数径向 $U_0$ 按 Fourier 模对角。对
$M\ge2^{1024}\lambda_j$，(S.9) 给真实两行高频 wave 能量
$e^{I_1/M}<4/3$；wave 到 $y_\pm$ 的常矩阵是一个标量乘酉矩阵，
故其条件数为1。径向两个 mean 与非mean没有耦合。于是

$$
\|P_{\ge M}U_0(t,s)\|_{\mathcal W_r\to\mathcal W_r}<4/3 .
\tag{S.14}
$$

现在用准确全空间 Duhamel，并且只对最后的完整 $U_{\rm st}$ 消费
旧界：

$$
P_{\ge M}U_{\rm st}(t,s)
 =P_{\ge M}U_0(t,s)
  +\int_s^tP_{\ge M}U_0(t,\tau)
       [\mathcal A-\mathcal A_0](\tau)U_{\rm st}(\tau,s)\,d\tau .
\tag{S.15}
$$

这里 $P_{\ge M}$ 与径向 $U_0$ 准确交换，未与实际 $U_{\rm st}$
或真实角图交换。
全输入的新增费小于 $(4/3)E_iG_i$。
原[控制后全层预算](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md)
(N.3) 给
$\sum_j(K_j^{\rm ref})^2N_j^c<2^{160016}$，
$K_j^{\rm ref}=2^{5000}(j+4)^5\delta_j^{-10}$。
把 (S.12)–(S.13) 相乘，剩余的
$J^8\delta^{-15}$ 被同一个
$(j+4)^{10}\delta^{-20}$ 严格支配。包含相邻胞元和两个负分量后，

$$
\sum_i(4/3)E_iG_i<2^{160040}\mathcal X
 \le2^{-102104}<1/16 .
\tag{S.16}
$$

因此对所有 $M\ge2^{1024}\lambda_j$，

$$
\boxed{\quad
\|P_{\ge M}U_{\rm st}(t,s)\|_{\mathcal W_r\to\mathcal W_r}<2,
\qquad |r|\le3 .
\quad}
\tag{S.17}
$$

mean 输入和全部低输入已在 (S.15) 中；没有假设它们的输出为0。
反向 Duhamel 使用相同的两个旧双向界，故同样成立。

## 3. 实际跨支原函数的斜率尺度

采用第51束完整恒等式 (H.8)–(H.9)：
$K_{\rm cross}=\partial_t\mathcal L-\mathcal Z$，
其准确系数为 $R=\kappa/\nu$。
在同参数径向参考上恰有
$R_0=V_w$；$\mathcal Z_0$ 的系数为 $(V_w)_t$，
其真实两射线复合仍保留。因而 (S.9)–(S.11) 可以直接消费。

为说明非径向差不会重新引入旧的 $\delta^{-24}$ 费用，
使用原实际 $\kappa$ 商式和第51束 (H.10) 前的状态 jet 证明。
各光滑片的前三阶实际状态差的完整角界为

$$
2^{256}(1+Q)n_i,\quad
2^{256}[(1+Q)^2+|Q_t|]n_i,\quad
2^{256}[(1+Q)^3+(1+Q)|Q_t|+|Q_{tt}|]n_i .
\tag{S.18}
$$

真实 $J_{\rm state},D_{\rm state}$ 分母大于 $1/2$，
严格 $Q>1/128$。
从 $\kappa/\nu$ 减去 $V_w$ 的每一项都含一个实际状态差或其导数；
从其 $t$ 导减去 $(V_w)_t$ 同理。
例如

$$
R-V_w={\kappa-\sqrt Q\,V_w\over\sqrt Q\,v}
                         +V_w(v^{-1}-1).
\tag{S.19}
$$

原 $\kappa-\kappa_0$ 的完整展开为严格密度篇 (S.12)；
再微分一次只使用 (S.18) 和 $Q_{ttt}$。
第51束 (H.10) 的商法则账已包含至多 $Q_t^3$、$Q^{-9}$、
32片及全部 BV 跳幅；现在保留这些展开中本来的一个 $n_i$ 因子。
真实 Jacobian 的差由原 (S.19) 的 $2^{32}Jn_i$ 界给出。
对所需至多8阶角导再消费固定条带，所有系数差可共同放宽为

$$
\varepsilon_{2,i}
 =2^{1200}J^{13}\delta^{-24}n_i .
\tag{S.20}
$$

这里仅比较这些有限系数及其 BV 费用；没有比较两个不同 FIO 的
裸同阶算子差。原完整严格密度篇 (S.29)–(S.31) 已支付
$2^{1280}J^{13}\delta^{-25}N_j^\#\mathcal X$ 的全层和；
控制后 $N_j^c$ 只增加原已记的 $2^{16}$。
所以 $\sum_i\varepsilon_{2,i}<2^{192016}\mathcal X<1$。
这精确保留有限8192层和两个全局规范因子。

用真实角图的有限 Sobolev 费用和半阶平衡后，可以取

$$
\int\|K_{\rm all,nonmean}:H^r\to H^{r+1}\|dt<2^{512}\lambda_j,
\quad
\sup_t\|\mathcal L:H^r\to H^{r+2}\|
 +\int\|\mathcal Z:H^r\to H^{r+2}\|dt<2^{768}\lambda_j^2 .
\tag{S.21}
$$

这里的 nonmean 只说明 order-one 记号不用 $m^{-1}$ 作用于零模；
完整 mean 行列仍在 $K_{\rm sm}$ 中，见下一节。
本篇所用 $r$ 和输出阶均在原完整密度窗内。

## 4. 真解析隔带，保留所有低输入

需要的远频带估计可以在完整 Fourier 核上直接证明。
$\mathcal L,\mathcal Z,K_{\rm cross}$ 的每一非mean块均是有限个

$$
M_a C_F D_\theta^{-d},\qquad d=2,2,1,
\tag{S.22}
$$

的半阶平衡及真实 mean 投影，$F$ 为实际两射线复合。
在固定角条带上，$F$ 是一个实平移加解析小量，
$|F'-1|<1/4$；系数的 supremum 或径向积分分别由 (S.21) 支付。
其 Fourier 元含
$\int a(\theta)e^{inF(\theta)-im\theta}d\theta$。
当 $|m|\ge M$、$|n|\le M/4$，把圆周移到
$\operatorname{Im}\theta=-\operatorname{sign}(m)/1024$，有
$|\operatorname{Im}F|\le(5/4)/1024$。
因此真实指数包含一个严格的
$e^{-c(|m|+M)}$；输入、输出的所有有限 Sobolev 权和两侧 Schur 和
由该指数支付。反向隔带同理。可以统一放宽为

$$
\|P_{\ge M}T P_{\le M/4}:H^r\to H^{r+2}\|,
\quad
\|P_{\le M/4}T P_{\ge M}:H^r\to H^{r+2}\|
 \le2^{1024}C_T e^{-M/2^{14}},
\tag{S.23}
$$

其中 $C_T$ 是 (S.21) 对应的已付系数尺度。
此处常数宽裕地包含半阶平衡和 $|r|\le1$ 的全部权。
没有从单列衰减直接断言全算子界：两个完整几何 Fourier 和都已使用。

同支演化 $U_d$ 与 $e^{B_{\rm st}}$ 的实际 angular 非mean generator
总量已由控制后 (N.16) 支付。径向角平均准确酉移走，故其较小复平移族
在所有所需 $H^r$ 上双向范数小于2。
对这个完整复算子族作同样的指数权共轭，得到 (S.23) 型的隔带界，
其中 $C_T=1$。
其余 $K_{\rm sm}$ 的高输出仅有两类：解析的 mean 出列和两个
相反 Fourier 锥之间的核。两类都给

$$
\int\|P_{\ge M}K_{\rm sm}: \mathcal W_r\to\mathcal W_{r+2}\|dt
 <2^{1024}\lambda_j e^{-M/2^{14}}.
\tag{S.24}
$$

mean 的入行和 mean–mean块仍存在，但同支模型在 mean 上为恒等，
它们不会直接给高输出。没有把它们从完整 $U_{\rm st}$ 中删掉。

## 5. 对完整 Duhamel 作固定 cut 分解

第51束 (H.13) 的准确有序恒等式给端项
$U_d\mathcal L U_{\rm st}|_{\rm ends}$，以及

$$
-\int U_d[\mathcal Z+[\mathcal L,K_d]
                  +\mathcal L K_{\rm cross}
                  +\mathcal L K_{\rm sm}]U_{\rm st}
       +\int U_dK_{\rm sm}U_{\rm st}.
\tag{S.25}
$$

在完整表达式左侧只乘一次 $P_j$。
在 $\mathcal L,\mathcal Z$ 后插入固定阈值 $L_j/64$；
在两个 generator 乘积后插入 $L_j/256$。
所有这些阈值均大于 $2^{1024}\lambda_j$。
高输入部分的 $U_{\rm st}$ 因而由完整 (S.17) 控制：
$\mathcal L,\mathcal Z$ 各给 (S.21) 的两阶增益，输入仍是全空间。
三个 $\mathcal L K$ 或 $K_d\mathcal L$ 项总共降三阶；
把输入 cut 上的一阶权换成 $256/L_j$，其费用至多
$2^{1292}\lambda_j^3/L_j<\lambda_j^2$。

低输入部分必须保留，并使用 (S.23)–(S.24)。
若中间频率变大，准确分解到第一个跨隔带的真实因素；
若没有变大，最左的 $U_d$ 自身跨隔带。
每条有序积至多含三个这样的因素；在输出 $L_j$ 与输入
$L_j/256$ 之间再插入 $L_j/4,L_j/16,L_j/64$，
至少一个真实因素跨过已付的四倍隔带。
把公共指数再放宽为 $e^{-L_j/2^{20}}$。
其余有限因子及旧完整 $U_{\rm st}$ 仍照原顺序保留。
由

$$
G_i\le2^{1024}\lambda_j^6,\qquad
e^{-L_j/2^{20}}
 \le32!\,(2^{20}/L_j)^{32},
\tag{S.26}
$$

所有远带项相加小于
$2^{4096}\lambda_j^9e^{-L_j/2^{20}}<2^{-10000}\lambda_j^2$。
最后一个不等式只需
$32!<2^{160}$、$L_j=2^{4200}\lambda_j$、$\lambda_j>1$。
这明确支付低输入的实际条件数；没有把它删除。

两个端项和 $\mathcal Z$ 项合计小于 $2^{774}\lambda_j^2$。
同支真实有序传播减去 $I+B_{\rm st}$，以及
$e^{B_{\rm st}}-I-B_{\rm st}$，各自用两次完整积分；
因同支正逆范数<2和 (S.21)，合计小于
$2^{1026}\lambda_j^2$。
加上述实际所有项，宽放为 $2^{2048}\lambda_j^2$，得到 (S.2)
的完整强二阶界。

这个论证是固定输入 Hilbert 空间到整个高输出 Hilbert 空间的界；
它没有只取 shell supremum。又
$\|P_j(U_{\rm st}-e^{B_{\rm st}})\|<4$。
在两个输出空间间作参数 $2/3$ 的插值，得到

$$
4^{1/3}(2^{2048}\lambda_j^2)^{2/3}
          =2^{1366}\lambda_j^{4/3}<2^{1400}\lambda_j^{4/3},
\tag{S.27}
$$

证明 (S.3)。

## 6. 完整源、物理两迹与接下来仍需付的复合

普通与 weak 源仍先做实际密度共轭
$F_d=m_0F$、
$f_d=m_0(f-\tfrac12\nabla\log\Lambda\cdot F)$。
真实两支源和独立高度源为

$$
\mathcal S_\sigma={\sigma f_d\over2}
 -\tfrac12\partial_\theta[(\nu+\sigma d)F_d^t+\sigma F_d^\theta],
\qquad
(c_0')_{\rm weak}=-\langle\nu F_d^t\rangle,
\tag{S.28}
$$

加原完整 mean 及标签恢复的其余项。
对这些**准确**组成后的完整固定标签源 $\mathcal S(t)$，
(S.17) 直接给

$$
\left\|P_j\int U_{\rm st}(t,\tau)\mathcal S(\tau)d\tau\right\|_{\mathcal W_s}
 \le2\int\|\mathcal S(\tau)\|_{\mathcal W_s}d\tau.
\tag{S.29}
$$

原物理源是否满足该 norm，仍按严格密度篇 (S.32)–(S.39) 的实际
乘子、端点 total/bare 荷和 mean 行核查；本篇未将它们变成自由数据。
原始 physical $(h,p)$ 由真实 $\Lambda,d,\nu$、normal shear 和
两条实际角图恢复。
$\Gamma^*$ 两参数列包括所有 profile、源以及端图导数，
仍作为完整已给 source 列相加，不能设零。

本篇为纯解析改进，没有新的数值运行，也没有改变实际参数盒、
标签球、profile 或 cutoff 所对应的物理对象。
两根的自由 Airy frame、根图和负段 scattering 的全部有序复合，
再接完整正型 Cayley、原单位源以及全网络 high feedback，仍须
逐项完成后才能宣布新的全网络 $T_j$。
