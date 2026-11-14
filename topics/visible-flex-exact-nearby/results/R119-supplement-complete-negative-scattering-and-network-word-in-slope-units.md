# R119 续篇：完整负段散射及正负网络算子乘积的斜率费用

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇给下述真正完整算子结论，
不把单段高输出界直接相乘。固定第55束同一个实际
$\Gamma^*(a,\Omega)$，记

$$
J=j+5,\qquad \delta=\delta_j={2\over25}2^{-j},\qquad
\lambda=2^{32}\sqrt J\,\delta^{-9/4},\qquad
L=2^{6000}\lambda,\qquad g={4\over3}.
\tag{W.1}
$$

对一个完整内部负分量，$S_-$ 是原 Airy 波单位的真实双端散射，
$S_-^{(1)}$ 是第2节明确构造的完整酉 principal 加首相位算子乘积。
准确有

$$
\boxed{\quad
\|S_--S_-^{(1)}:H^0\to H^g\|<2^{9000}\lambda^g,
\qquad
\|S_--S_-^{(1)}:H^{-g}\to H^0\|<2^{9000}\lambda^g.
\quad}
\tag{W.2}
$$

均值、全部低模、两个 Fourier 锥、真实 root graphs、全部中间
频带和两端源均保留。输入没有频率截断。这里给两个真实基础窗，
不由一个窗暗中授予所有 $|s|\le1$。

与[完整 positive 斜率界](R119-supplement-positive-full-Airy-remainder-in-root-slope-units.md)
合成后，完整内部网络相对于 $I+S_-^{(1)}$ 的每行余项在这两个
窗中小于 $2^{9020}\lambda_i^g$，见第9节。这个算子乘积保留真实
角图和第一次相位。尚未在本篇把它改名为标量
$1+\exp i(n\omega_i+\beta_i^0/n)$，也不据此宣布新的全网络 inverse。

## 1. 全部实际依赖和同一个完整状态

使用以下已经付清的、同参数实际定理：

* [root 高输出 Volterra](R119-supplement-root-high-output-Volterra-without-low-frequency-condition-number.md)
  及[完整第一次相位](R119-supplement-complete-root-first-phase-in-slope-units.md)：
  完整 interaction $U_e$、模型 $e^{B_e}$、高输出同阶门2和
  强余项 $2^{4098}b_e^g$。
* [完整自由两行端架及勘误](R119-supplement-complete-free-Airy-two-row-frame-and-low-frequency-erratum.md)：
  $\Phi_e^{\pm1}$ 同阶小于 $2^{64}b_e$，正逆强余项
  $2^{64}b_e^g$，且它们准确 Fourier 对角。
* [完整 root graph](R119-supplement-complete-root-graph-two-order-slope-budget.md)：
  实际 graph、完整高度恢复及两条 mean；其强余项
  $2^{700}b_e^g$，完整同阶正逆界小于4。
* [完整 strict 高输出](R119-supplement-complete-strict-high-output-in-root-slope-units.md)：
  $U_{\rm st}$ 的高输出同阶门2、相对于 $e^{B_{\rm st}}$ 的
  强余项 $2^{1400}\lambda^g$，以及同参数径向完整 generator 差。

每个 $b_e<\lambda$。本篇所需所有同阶和输出指数位于
$0\le r\le g<2$，已有完整窗口足够。实际辅助状态
$\mathcal W_r=\mathbb C^2\oplus(H^r_0)^2$ 与两振幅的常矩阵
转换是自由端架勘误 (A.20)，其条件数至多2。这个固定因素随
每次转换明确保留，不产生新的 $b$ 幂。

物理根处恢复始终使用[联合根图 (J.38)–(J.40)](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)：

$$
h_e=\alpha_e^{-1/2}u_e,\qquad
p_e=\varsigma_e\sqrt{\alpha_e}
                  (u_\xi-\tfrac12\ell_\xi u)_e .
\tag{W.3}
$$

$\varsigma_-=1,\ \varsigma_+=-1$。原 raw height 与 conormal 的
两个非径向 mean 不被 canonical 的纯零模替代。固定材料角仍为
$\mathbb T_{\pi/2}$，所有 Sobolev 权都是 $\langle m\rangle$，
$m\in4\mathbb Z$。

## 2. 真传递与明确的完整酉模型

从左根向右根，有序经过以下准确因素：左 root interaction、
左自由端架、左 graph 和其物理角恢复、完整 strict evolution
和其 principal 角恢复、右 graph 的逆、右自由端架的逆、右
root interaction 的逆，以及右根的准确两行交换。
把 graph/strict 的 principal 恢复单独列出后至多12个因素。
记其完整有序乘积为

$$
T=A_N\cdots A_1,\qquad N\le12.
\tag{W.4}
$$

这些因素在共同两振幅空间读取；所有中间的常矩阵、mean 恢复
和 (W.3) 都是同一准确坐标的变换。原物理密度因子不是在一侧
被设为1，而是在相同两迹间的复合中准确抵消。

模型 $M_k$ 按以下明确规则选择。

1. root interaction 用其真实 $e^{B_e}$；自由端架用勘误
   (A.14)，含 $\pi/4$ 和 $-5b_e/(48H^{3/2}M)$；右根仍交换。
2. graph 和 strict 的同支演化用已定义的 $e^{B_g}$、
   $e^{B_{\rm st}}$，所有两个 mean 上模型取恒等。
3. principal 角图用旧完整余项篇 (H.20) 的满射 unitary
   $U_K$。在波振幅上是准确的 branch/cone 分块作用，mean 取
   恒等；在原物理两迹上仍是
   $F_e\operatorname{diag}(U_K,U_K)F_e^{-1}$。
   原图的跨锥和完整 mean 恢复差全部进入余项，不删除它们。

这里 $U_K$ 是 signed-density 压缩的 polar 校正，不是裸
$C_K$。每个 $M_k$ 在 $H^0$ 上是普通酉；它还与 wave Green
$\mathsf J$ 交换，右根交换除外。其 $H^r$ 正逆 norm小于2，
$|r|\le2$；真实角小量的四阶窗口已经在第55束 (N.16) 支付。
于是

$$
M=M_N\cdots M_1=
       \begin{pmatrix}0&M_B\\M_C&0\end{pmatrix},
\qquad M_B,M_C\text{ 都是满射 unitary}.
\tag{W.5}
$$

有限个常矩阵如另列成因素，可把全部模型子乘积的 $H^r$ norm
统一宽放为 $2^{64}$。模型各因素均准确保持 mean 子空间；
整个模型在 mean 上只保留右根交换。实际 mean 仍由 (W.4) 给出。
定义

$$
S_-^{(1)}=\begin{pmatrix}0&M_B^*\\M_C&0\end{pmatrix}.
\tag{W.6}
$$

这是本篇明确的完整散射模型，普通酉性没有用实际 Cauchy 的
一个可能条件数很大的块来定义。

## 3. 一个额外的真实全层预算

第55束固定

$$
N_j^c=2^{200}h_j^{-5}{\zeta_j\over\mu_j\delta_j^2},
\qquad
(N_j^c)^\#=N_j^c+\mathbf1_{j\ge130}N_{j-1}^c,
\qquad n_i=4(N_j^c)^\#\mathcal X,\qquad
\mathcal X\le2^{-262144}.
\tag{W.7}
$$

[原完整标签定义 (C.2)、(C.25)、(C.32)](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
给出以下三个实际而非渐近的界：

$$
N_j^c\le
\begin{cases}
2^{220}\delta_j^{7/4},&129\le j\le4096,\\
2^{185}\delta_{4096}^{-3/2}\delta_j^{827/256},
                                      &4097\le j\le8192,\\
2^{185}\delta_{4096}^{-3/2}\delta_{8192}^{-485/4}
          \delta_j^{31867/256},&j\ge8193.
\end{cases}
\tag{W.8}
$$

这里的邻项严格沿用第55束 (N.2)：在 $j=129$ 时为0，
没有额外的 $N_{128}^c$ 端项；最外未覆盖的分量保留为真实外端口。
第一行只宽放 $(100/9)^5<2^{20}$。后两行的 $2^{185}$ 来自
$h_j^{-5}=2^{-15}\delta_j^{-5/256}$，所以两个旧全局逆幂都保留。
本篇需要并现在直接证明

$$
\boxed{\quad
\sum_{j\ge129}2^{5000}(j+5)^{20}\delta_j^{-30}(N_j^c)^\#
 <2^{240000}.
\quad}
\tag{W.9}
$$

由于 $j+3<-\log_2\delta_j<j+4$、$j+5<2^{14}$ 于
$j\le8193$，先不加邻项的三段逐项二进制上界可分别取

$$
\begin{array}{c|c}
129\le j\le4096&5000+280+220+(30-7/4)4100<122000\\
4097\le j\le8192&5000+280+185+6150+27\cdot8196<233000\\
j=8193&5000+280+185+6150+(109/4)8196-94<235000.
\end{array}
\tag{W.10}
$$

第二行用了 $827/256>3$；第三行用了
$31867/256-30>94$ 和 $\delta_{8193}=\delta_{8192}/2$。
从8193起，相邻项比不超过
$(1+1/(j+5))^{20}2^{30-31867/256}<2^{-90}$。
全部有限前缀项数小于 $2^{14}$；邻项 $N_{j-1}^c$ 重新编号后
增加的权比小于 $2^{31}$。这些因素的和仍小于
$2^{235050}<2^{240000}$，证明 (W.9)。因此

$$
\sum_{j\ge129}2^{5000}J^{20}\delta_j^{-30}(N_j^c)^\#\mathcal X
 <2^{-22144}.
\tag{W.11}
$$

这是一条完整初等不等式证明，包含129–8192的全部真实前缀；
没有把只有最深层才小的幂当成整个尾的门。

## 4. root 和 graph 的真正低输入到高输出

### 4.1 实际 root 的复角比较

在[联合根图 (J.25)–(J.31)](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)
的原复域，把实际 potential 换为
$V_z(\xi,\phi)=V(\xi,\phi+z)$，$|\operatorname{Im}z|\le1/256$。
径向 $V_0$ 不变。完整乘子差在 $|r|\le2$ 上小于
$2^{56}n_i$。在原完整 $Y$ 平衡中，径向 propagator
$K_R<2^{2184}$；准确相对 Volterra 积分因此小于

$$
H K_R^2\,2^{56}n_i=2^{4418}n_i<1/64.
\tag{W.12}
$$

故这个真实复角算子族的正逆 $Y$ 演化仍小于 $2^{2185}$。
用原 Airy 到 $Y$ 的两个 $2^{16}b^{1/3}$ 转换，得到

$$
\|U_e(z)^{\pm1}\|_{H^r\to H^r}<2^{2217}b_e^{2/3}.
\tag{W.13}
$$

这里没有声称一般 strict 的复角演化也有此界。根区成立是因为
真实 principal 在角方向为常系数，复平移只改变已付的 order-zero
potential。包含 mean 和两个 Fourier 锥的矩阵准确满足
$U_e(z)_{mn}=e^{i(m-n)z}U_e(0)_{mn}$。

分开输出两个符号，令 $z=-i\operatorname{sgn}(m)/256$。
把指数放在输出和低输入两侧，$\langle m\rangle^g$ 用半个剩余
指数吸收，即对 $M\ge64$ 有

$$
\|P_{\ge M}U_e^{\pm1}P_{\le M/4}:H^0\to H^g\|
 <2^{2300}\lambda\exp(-M/2^{12}).
\tag{W.14}
$$

这是完整 Hilbert 算子分解；不以各个矩阵条目的 supremum
代替行列求和。相同证明对 $e^{\pm B_e}$ 更容易：径向平均准确
酉移走，其余角部分在此复条带小于已付 $2^{128}b_en_i$，
故复角族 norm小于2。于是 (W.14) 也控制 root error 的远带，
至多再乘2。

### 4.2 完整 graph 的有序路径

原根图 (G.18)–(G.20) 给每一有序三态路径的真实输入角

$$
F(\phi)=\phi+q(\phi)\int_0^1
       \epsilon(s)c(H+s q(\phi))\,ds,\qquad |\epsilon|\le1.
\tag{W.15}
$$

其解析域和导数界与路径次数无关；完整系数乘积求和小于
$2^{64}\exp(2^{20}bD_e)<2^{66}$。同一个真实域上
$|F'-1|<1/4$。对每个 $a(\phi)e^{inF(\phi)}$ 的 Fourier
积分，把 $\phi$ 移到
$\phi-i\operatorname{sgn}(m)/1024$。当 $|n|\le|m|/4$ 时，
振荡项留下至少 $|m|/2048$ 的负实指数。

完整图密度因子、原始 primitive 和 wave 半阶平衡至多加入固定
多项式权。将该权及两个 Fourier 求和用再半个指数支付，得到
graph、其逆及其完整 principal 模型的共同远带门

$$
\|P_{\ge M}A P_{\le M/4}:H^0\to H^g\|
 <2^{1024}\exp(-M/2^{14}),\qquad M\ge64.
\tag{W.16}
$$

完整 mean 输入列来自同一 (W.15) 的实际高度恢复，角解析且
有相同系数门；mean 输出在高投影下为0。这里使用所有路径和
所有 source 位置的同一个可和级数，没有假设 graph 的高输出
只来自高输入。

### 4.3 principal 角图及 polar 差

对纯 density 角图同样使用 Fourier 相位
$nK(\phi)-m\phi$。真实 $K'-1$、所需26阶角导、mean 恢复及
相应有限主系数均由第55束 (N.16) 的

$$
\epsilon_i^c=2^{8192}J^{16}\delta^{-16}(N_j^c)^\#\mathcal X,
\qquad \sum_i\epsilon_i^c<2^{-102096}
\tag{W.17}
$$

支付。径向平移部分不会产生跨频率。
同一真实 contour 给非polar部分的 (W.16)。对 polar 差不需要
宣称存在一个未证的复角 functional calculus：旧 (H.20) 的
双侧 signed-Green 恒等式和24次真实角分部积分直接给

$$
\|R_{\rm ang}:H^r\to H^{r+20}\|<2^{4096}\epsilon_i^c,
\qquad r=0,
\tag{W.18}
$$

以及同一个 adjoint 门。此处已分离只在 mean 到 mean 的有限
块；该块在每个左侧模型乘积后仍为 mean，高输出投影准确杀掉它。

具体地，跨锥 kernel 在两个非零频率上被
$2^{1024}\epsilon_i^c(|m|+|n|)^{-24}$ 乘半阶平衡因子控制；
付20个输出导数后，剩余行列幂仍可和。两侧
$V_K^*V_K-I$、$V_KV_K^*-I$ 都是这些跨锥块的二次式。
展开 $(I+F)^{-1/2}-I$ 的绝对可和幂级数，首个 $F$ 付20阶，
其余因子付同阶小 norm；外面的 $V_K$ 只需同一26阶角界内的
20阶 chain rule。因此 (W.18) 的 $2^{4096}$ 有充分余量。
mean 与非mean间的真实有限行列按解析 Fourier 系数同样求和。

于是所有 principal 模型、实际 principal 图及其差，除刚才的
mean-only 块外，所需远带可统一宽放为

$$
\|P_{\ge M}A P_{\le M/4}:H^0\to H^g\|
 <2^{4096}\left[e^{-M/2^{14}}+M^{g-20}\right].
\tag{W.19}
$$

同支 $e^{B_g},e^{B_{\rm st}}$ 的复角族也小于2：移走真正径向
平均后，搬移实际角图还可能把大径向 phase 乘上角小量，
因此这里明确支付 $\lambda_i\epsilon_i^c$，不能只用
$\epsilon_i^c<1$。由 (W.11) 准确有

$
\frac{\lambda_i\epsilon_i^c}
 {2^{5000}J^{20}\delta_j^{-30}(N_j^c)^\#\mathcal X}
 =2^{3224}J^{-7/2}\delta_j^{47/4}<2^{3224}.
$

按胞元 $j$ 求和小于 $2^{-18920}$；每层至多两个内部负分量，
故按分量 $i$ 求和小于 $2^{-18919}$，以下安全使用
$\sum_i\lambda_i\epsilon_i^c<2^{-18918}$。
复角 nonradial generator 所需有限乘子/chain-rule 常数至多
$2^{2048}$，仍有小于 $2^{-16800}$ 的完整积分费用。
径向大平均与 Fourier 权准确交换，Duhamel 因而给复角族
norm小于2。它们满足更强的指数远带门。自由端架及其逆则
准确没有远带：它们保持每个 Fourier 模。

对不超过12个模型因素的任何子乘积，逐次插入四倍间隔的投影，
并使用 $H^0$ 酉性和 $H^g$ norm小于 $2^{64}$，从 (W.19) 得

$$
\|P_{\ge M}M_{\rm sub}P_{\le M/4^{12}}:H^0\to H^g\|
 <2^{8192}M^{g-20},\qquad M\ge2^{100}.
\tag{W.20}
$$

指数项已由 $M^{g-20}$ 控制。这个完整有限频带分解同时支付行、
列与全部频率，不是单个 dyadic shell 的断言。

## 5. strict 低输入门：只乘实际单根前缀

strict 的复角 propagator 不在本篇假设中。采用新 strict 篇
(S.12)–(S.13) 的准确全 generator 差及完整 Cauchy：

$$
\int\|\mathcal A-\mathcal A_0\|_{H^r\to H^r}
 <E_i=2^{300}J^3\delta^{-5}n_i,
\qquad
\|U\|,\|U_0\|<G_i=2^{1024}J^5\delta^{-10},
\tag{W.21}
$$

$0\le r\le g$。这里 $U_0$ 是同一个最终参数的真实径向对象。
全空间 Duhamel 直接给绝对差 $\|U-U_0\|<G_i^2E_i$。
同支 generator 是完整 generator 的 block/cone 压缩，故
$\|B-B_0\|\le4E_i$；指数 Duhamel 再用已付同阶 norm2。
因此，写 $E_{\rm st}=U-e^B$、$E_{{\rm st},0}=U_0-e^{B_0}$，有

$$
\|E_{\rm st}-E_{{\rm st},0}\|_{H^r\to H^r},\quad
\|U-U_0\|_{H^r\to H^r}
 <\epsilon_{\rm st}:=2^{2500}J^{13}\delta^{-25}n_i.
\tag{W.22}
$$

不能在这一绝对差后再误乘一个全 strict Cauchy 条件数。
径向 $U_0,E_{{\rm st},0}$ 准确 Fourier 对角，包括原两 mean。
所以跨四倍隔带的真实输入输出只需 (W.22)。

到达唯一 strict 因素之前，真实前缀只含一侧 root、自由端架、
graph 与 principal 恢复。由上述已付门，正向和逆向都可取

$$
\|A_{\rm in}\|_{H^r\to H^r}<2^{2300}\lambda^{5/3}.
\tag{W.23}
$$

这不是 $\lambda^{12}$ 的整个负段。将 (W.22) 乘 (W.23)，再
用 $\lambda^{5/3}=2^{160/3}J^{5/6}\delta^{-15/4}$ 及
$n_i=4(N_j^c)^\#\mathcal X$，逐项有

$$
\epsilon_{\rm st}\|A_{\rm in}\|
 <2^{5000}J^{20}\delta^{-30}(N_j^c)^\#\mathcal X
 <2^{-22144}.
\tag{W.24}
$$

对 $M\le L$，先在低输入上乘真实 $H^g$ 权、再使用 (W.22)，
得到需要的完整 strong 低输入门

$$
\|P_{\ge M}E_{\rm st}P_{\le M/4}A_{\rm in}:H^0\to H^g\|
 \le\epsilon_{\rm st}\langle M/4\rangle^g\|A_{\rm in}\|
 <2^{-14000}\lambda^g.
\tag{W.25}
$$

最后一步用 $L=2^{6000}\lambda$，所以 $L^g=2^{8000}\lambda^g$。
同阶版本用于完整前缀的高输出归纳。全部 mean 输入在
$P_{\le M/4}$ 中，未被排除。

## 6. 完整有限乘积的高输出传递误差

首先重付所用的粗同阶前缀，避免沿用有错误中间端架的旧论证。
两侧 root 各 $2^{2217}\lambda^{2/3}$，两自由端架各
$2^{64}\lambda$，graph/角恢复各至多16；strict 为
$2^{1024}J^5\delta^{-10}<2^{1024}\lambda^6$。
最后一式使用 $J^2\delta^{7/2}<1$。
因此对任何实际连续子乘积及其逆都可取

$$
\|A_{\rm sub}\|_{H^r\to H^r}
 <G_{\rm all}:=2^{8192}\lambda^{12},\qquad 0\le r\le g.
\tag{W.26}
$$

实际 principal 恢复的独立 mean 还含光学长度，但
$\int\sqrt Q\,dt<2^8\sqrt J\,\delta^{1/4}<1/8$；其有限
两态矩阵 norm小于2。非mean的 Jacobian/chain-rule 费用由
(W.17) 的角小量控制。因而上面统一的16同时覆盖这些完整因素。

下面所有插入阈值都留在

$$
2^{-100}L\le M\le L.
\tag{W.27}
$$

即使四倍 buffer 连续穿过全部12个因素、再为误差两侧各留一组，
最小阈值仍大于 $L/4^{36}>2^{-100}L$。
因此所有 root/strict 高输出门都确实可用：
$2^{-100}L=2^{5900}\lambda>2^{4200}b_e$。
没有让某个中间频带掉到已证门的下方。

### 6.1 实际前缀的高输出门

对 $A_k\cdots A_1$，在 $A_k$ 前插入
$P_{\ge M/4}+P_{<M/4}$。第一项使用该因素的完整高输出同阶界，
宽放为16；高输入前缀使用同一个归纳门。
第二项若为 root 或 graph，用 (W.14)、(W.16) 乘 (W.26)；
若为 principal，使用 (W.19) 的同阶版本；若为自由端架，准确
为0；唯一 strict 项使用 (W.24) 的实际单根前缀。

所有非strict的泄漏都严格小于1。例如多项式项满足

$$
2^{4096}M^{-20}G_{\rm all}
 \le2^{12288-118000}\lambda^{-8}<2^{-10000},
\tag{W.28}
$$

而指数项更小。可用 $e^x\ge x^{32}/32!$、$32!<2^{160}$
直接将它们化为同样的幂门；不需数值拟合指数尾。
strict 泄漏小于 $2^{-22144}$。
从恒等前缀开始，$C_k\le16C_{k-1}+1$，$N\le12$，故

$$
\|P_{\ge M}A_k\cdots A_1:H^0\to H^0\|<2^{64}
\tag{W.29}
$$

于所需全部 buffered 阈值。逆向同样成立；它在到达 strict
之前仍只经过右侧单根，故继续用 (W.23)，不消费整个旧条件数。

### 6.2 一次有序 telescoping，保留所有低输入

写 $E_k=A_k-M_k$。准确恒等式是

$$
T-M=\sum_{k=1}^N
      M_N\cdots M_{k+1}\,E_k\,A_{k-1}\cdots A_1.
\tag{W.30}
$$

左侧全是模型，右侧是实际前缀，不重复乘多个实际全 Cauchy。
对每项先在左模型乘积前后按 (W.20) 插入至多12个四倍 buffer。
所有低输出穿过左模型变成高输出的部分，由 (W.20) 乘

$$
\|E_kA_{k-1}\cdots A_1\|_{H^0\to H^0}
 \le\|A_k\cdots A_1\|+\|M_kA_{k-1}\cdots A_1\|
 <2G_{\rm all}
\tag{W.31}
$$

支付；常矩阵如单列，宽放为 $2^{65}G_{\rm all}$ 亦足够。
注意 (W.31) 不是 $\|E_k\|G_{\rm all}$ 再收一次多余的
$\lambda$ 幂。

需要的高输出 $E_k$ 再在右侧插四倍输入 buffer。高输入前缀由
(W.29) 支付；每个真正 root/graph/strict/free 强余项至多
$2^{4100}\lambda^g$。左模型的 $H^g$ norm小于 $2^{64}$。
低输入部分分别使用第4节真正远带或 (W.25)，不能从高输出
同阶门猜测其平滑性。

新增 principal/polar 差用 (W.18) 的20阶门与 (W.26)，故也
落在同一余量内。被分离的 mean-only 块在所有左模型后仍仅有
mean 输出，$P_{\ge L}$ 准确杀掉它；它在最终的实际散射低块中
仍完整保留。

为列清常数，最多12个局部强项的总费小于
$12\cdot2^{64}\cdot2^{4100}\cdot2^{64}\lambda^g
<2^{4232}\lambda^g$。所有角图/polar 的远带和左模型远带均
被下列更宽的共同项覆盖：

$$
2^{20000}\lambda^{12}(2^{-100}L)^{g-20}
 <2^{-10000}\lambda^g.
\tag{W.32}
$$

指数远带同样可用32次幂的初等比较支付。strict低输入强项在
(W.25) 之后再乘 $12\cdot2^{64}$ 仍小于 $\lambda^g$。
因此得到真正全输入高输出的

$$
\boxed{\quad
\|P_{\ge L}(T-M):H^0\to H^g\|<2^{6000}\lambda^g.
\quad}
\tag{W.33}
$$

同一完整证明对反向物理传递和逆模型成立：

$$
\|P_{\ge L}(T^{-1}-M^{-1}):H^0\to H^g\|
 <2^{6000}\lambda^g.
\tag{W.34}
$$

尤其 (W.33) 没有把 $P_{\ge L}T$ 与 $P_{\ge L}M$ 的差当成
已知强余项，也没有先把输入低模设为0。

## 7. 真正双端散射：准确通量消去低条件数

(W.3) 的原密度 Green pairing、原两列共同 Wronskian
$-2ic^2/\pi$ 及右根方向给完整恒等式

$$
T^*\mathsf JT=-\mathsf J,
\qquad T\mathsf JT^*=-\mathsf J,
\qquad T^*=-\mathsf JT^{-1}\mathsf J.
\tag{W.35}
$$

第二式来自已付的完整 onto Cauchy inverse；未假设 Fourier
某个截块满射。模型 $M$ 也满足 (W.35)。因此若 $E=T-M$，
(W.34) 准确给

$$
\|P_{\ge L}E^*:H^0\to H^g\|<2^{6000}\lambda^g.
\tag{W.36}
$$

写 $T=(A,B;C,D)$。由 (W.35)，
$B^*B\ge I,\ BB^*\ge I$，以及 $C^*C\ge I,\ CC^*\ge I$。
前两式同时证明 $B$ 有闭像且满射，后两式同理；故
$B^{-1},C^{-1}$ 都是全空间 onto contraction。
令左、右 incoming 分别为 $a_L,a_R$，outgoing 为 $b_L,b_R$。
由 $(a_R,b_R)=T(a_L,b_L)$ 准确解得

$$
\binom{b_L}{b_R}
 =S_-\binom{a_L}{a_R},\qquad
S_-=\begin{pmatrix}
-B^{-1}A&B^{-1}\\
C-DB^{-1}A&DB^{-1}
\end{pmatrix}.
\tag{W.37}
$$

完整 Green 等式说明 $S_-$ 等距；对任意 outgoing，由 $C^{-1}$
作反向同一解法得到 incoming，所以它满射并普通酉。这个结论
包括两个 mean，不从有限 Fourier 数值矩阵的酉性外推。

输出强界使用[准确散射代数 (F.17)–(F.21)](R46-supplement-actual-strong-scattering-and-return-operator-word.md)
的恒等式本身，不移用那个不同有限帽的数值常数：

$$
B^{-1}A=D^*(C^*)^{-1},\qquad
DB^{-1}=(C^*)^{-1}A^*,
$$
$$
B^{-1}=B^*-D^*(DB^{-1}),\qquad
B^{-*}=B-A(A^*B^{-*}).
\tag{W.38}
$$

模型 (W.5) 准确反对角，所以
$A,D,B-M_B,C-M_C$ 及其 adjoint 的高输出强界都小于
$R_T=2^{6000}\lambda^g$。
从 (W.37)–(W.38)，$S_--S_-^{(1)}$ 四块高输出界为

$$
\begin{pmatrix}R_T&2R_T\\2R_T&R_T\end{pmatrix}.
\tag{W.39}
$$

例如左反射用 $-D^*(C^*)^{-1}$，上 transmission 差为
$(B^*-M_B^*)-D^*(DB^{-1})$；所有最右因素只是 contraction
或真实散射块，L2 norm不超过1。没有让 $B^{-1}$ 左乘一个强
余项并索取它未付的 $H^g$ norm。

adjoint 同样直接成立：左反射 adjoint 用 $-A^*B^{-*}$，
右反射 adjoint 用 $A C^{-1}$，上 transmission adjoint 用
$(B-M_B)-A(A^*B^{-*})$，另一个用
$(C^*-M_C^*)-A^*(B^{-*}D^*)$。
这些表达式的最右括号仍是真实散射块。
所以

$$
\|P_{\ge L}(S_--S_-^{(1)})\|_{H^0\to H^g},\quad
\|P_{\ge L}(S_--S_-^{(1)})^*\|_{H^0\to H^g}
 <3\cdot2^{6000}\lambda^g.
\tag{W.40}
$$

最后才处理全部低输出。因为 $S_-$ 和 $S_-^{(1)}$ 真正酉，

$$
\|P_{<L}(S_--S_-^{(1)}):H^0\to H^g\|
 \le2\langle L\rangle^g<4L^g
 =2^{8002}\lambda^g,
\tag{W.41}
$$

adjoint同理。高低输出正交，甚至直接相加也小于
$2^{9000}\lambda^g$。由对偶即得到 (W.2) 的两个窗口。
这里所有中间频率 $|m|<L$ 都经过实际完整散射的酉性支付；
没有要求它们属于某个尚未证明的低 incoming cone。

## 8. 负段完整 ordinary、weak 和参数仿射源

若准确传递关系为

$$
\binom{a_R}{b_R}
 =T\binom{a_L}{b_L}+\binom{f_A}{f_B},
\tag{W.42}
$$

完整散射仿射列准确为

$$
q_-=
\binom{-B^{-1}f_A}{f_B-DB^{-1}f_A},\qquad
\|q_-\|_{H^0}<2\|(f_A,f_B)\|_{H^0}.
\tag{W.43}
$$

因此也没有以全 Cauchy 条件数再粗乘仿射端口输出。
需要强输出时，(W.38) 和 (W.2) 给一个直接充分门

$$
\|q_-\|_{H^g}
 <2^{65}\|(f_A,f_B)\|_{H^g}
       +2^{9002}\lambda^g\|(f_A,f_B)\|_{H^0}.
\tag{W.44}
$$

它要求右端确实已有显示的原端口正则性，不从一个没有径向图迹
的体源 norm 免费取得 $H^g$ 端点资料。

$f_A,f_B$ 本身仍是实际有序 particular：在每一 root、strict
及 graph 中先使用原 canonical/Piola/密度变换，沿完整 Cauchy
作 Duhamel，再通过其余真实因素。原符号约定
$Ph=f-\operatorname{div}F$ 下，root 使用 total 状态

$$
\partial_\xi\binom uP
 =\begin{pmatrix}0&1\\-(\xi D^2/b^2+V)&0\end{pmatrix}\binom uP
   +\binom{-F^\xi}{f_c-\partial_\phi F_c^\phi},
\qquad P=u_\xi+F^\xi.
\tag{W.45}
$$

没有微分 weak 的径向分量。graph 上使用完整
$\widehat Y_\sigma=Y_\sigma-g'(cF_d^\xi+\sigma F_d^\phi)/2$；
body source、这两个端点荷及独立 mean 均保留。
回到裸 physical flux 时，再按原合同提供并减去真实法向端点迹。
源的实际 Jacobian、$\alpha^{-1/2}$、normal shear 与物理平均
继续使用原定义，不换成方便的 canonical bare 单位。

两列 $D\Gamma^*$ 以及所有参数响应只是 (W.45) 和 strict/graph
原完整源中的指定列；本篇的投影和散射消元不使它们为零。
若参数端图也变化，它的真实微分同时进入原 graph 仿射列，
不能只微分一个 Fourier 对角首模型。

## 9. 两真实 positive cross 与整个内部网络算子乘积

在所有已覆盖内部负分量上取 direct sum 的真正 $S_-$。
两个相邻 positive 元件按照原端口 wiring 取其完整酉 $R_+$；
每个都包括两个 mean 和实际两端 transmission。
若实际 incoming/outgoing 约定使连接读作 $R_+^*$，以下取该
adjoint；其同一个 defect 门由真实 unitarity 和已有 $H^r$ 界
支付，不会更改源的号数。

固定连接约定，写

$$
b=S_-a+q_-,\qquad a=R_+b+q_+.
\tag{W.46}
$$

于是准确网络方程及其源是

$$
(I-R_+S_-)a=q_++R_+q_-,
\tag{W.47}
$$

并有完整恒等式

$$
(I-R_+S_-)-(I+S_-^{(1)})
 =-(R_++I)S_-+(S_--S_-^{(1)}).
\tag{W.48}
$$

第一项的右边是实际酉散射，所以 forward strong 窗只收
$\|S_-\|_{H^0}=1$，不是 $G_{\rm all}$。
取 adjoint 后，把它写为
$S_-^*(R_+^*+I)$ 时，不能假设 $S_-^*$ 在 $H^g$ 上仍为1。
应先用准确改写

$$
S_-^*(R_+^*+I)
=S_-^{(1)*}(R_+^*+I)
 +(S_-^*-S_-^{(1)*})(R_+^*+I),
\tag{W.49}
$$

第一项只用模型的 $H^g$ norm小于 $2^{64}$，第二项用
(W.2) 的 adjoint强门和 $\|R_+^*+I\|_{H^0}\le2$。
故两基础窗都仍只有 $\lambda^g$，没有相乘出 $\lambda^{2g}$。

相邻胞元满足 $\lambda_{j+1}/\lambda_j<8$；两端正片的
$b_*^g$ 因而至多乘16。每个完整内部行所接端口数、每列的
输出行数均至多8。加上 (W.2)、positive 的
$2^{5700}b_*^g$、(W.49) 的 $2^{64}$ 以及有限常矩阵，得到

$$
\boxed{\quad
\|\mathcal E_i^{\rm word}:H^0(\text{全部相邻端口})\to H^g\|,
\quad
\|\mathcal E_i^{\rm word}:H^{-g}(\text{全部相邻端口})\to H^0\|
 <2^{9020}\lambda_i^g.
\quad}
\tag{W.50}
$$

在 (W.49) 中模型常数只乘 positive 的 $2^{5700}$，远低于
$2^{9000}$；它不乘负段的强误差。列向反向窗同样按相邻尺度和
有限度数读取。最外未覆盖的完整分量、finite connector 和其
外响应继续作为真实外端口；本篇没有给它们补造一个虚假的
$-I$ 反射。进入内部的实际 positive cross 属于
$R_++I$ 的完整平滑列，仍由 (W.50) 消费。

正段 source 按原两端 total-DN/Poisson/Cayley 列给出 $q_+$；
特别其完整 mean 荷满足
$\langle(q_{\mathcal F})_-+(q_{\mathcal F})_+\rangle
=\int\langle\widehat s\rangle$。
(W.47) 的 $q_++R_+q_-$ 是实际共同参数上的有序源，不是可任意
指定的理想误差。原 weak 端点迹、ordinary mean、两列
$D\Gamma^*$ 及整个真实外响应都在它或未消去的外端口中。

## 10. 证明权限与下一项尚需支付的量

(W.2)、(W.50) 解决的是完整 negative scattering 和完整
positive/negative 算子乘积的斜率幂；低模、中间频带和 mean
已经在这两个结论中支付。它们不要求某个近核先落入低 incoming
包，也没有使用只对径向逐模成立的 positivity 代替混频算子。

模型仍保留真实 principal 角映射及各段 $e^B$ 的准确次序。
要把 (W.50) 消费到新的标量算术高块，尚须在同一 wave 表示中
逐项付 KAM、首相位同调、所有有限 ordering 差和最后的两行
预条件，证明这些新增强余项也只有 $\lambda^g$。
旧更宽的 $\delta^{-100}$ 界不能直接证明这个改进。

即使随后取得那个新的高块，原单位的全部低/高反馈、三个外部
响应以及 moving mixed clusters 的共同参数选择仍须实际闭合。
本篇不把尚未闭合的量词写成已证存在或完整 inverse。
