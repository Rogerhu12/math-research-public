# R292：真实零平台的二次 period、有序三矩核与未付自历史

日期：2026-11-15。**完整纸面推导；未执行新的符号运算、profile 求积、秩计算、开发检查或科学运行。**

[R288](R288-cross-packet-third-locality-and-automatic-canonical-first-end-layers.md)已在当前不交 compact 微包圆上消去 canonical 零端的一次指数层。本稿继续处理其真实零平台。局部 $Y_\phi=0$ **不能**删除第四 range 中从右方积累的 $P_{YW}$；该尾会直接进入平台二次系数。

本稿证明一个准确的有序表达：跨两个不同微包的全部平台贡献，只依赖两组三矩和同一真实二阶 history；单包自身的第四尾另保留。由此得到每个平台的两个必要递推式，以及最右两包的一个明确双线性 history 门。没有宣称该门自动为零，也没有用全局三矩为零替代各个真后缀的条件。

## 1. 固定对象与实际 pure 假设

固定一条已经真实安装的闭几何，全部桥、初值和共同右锚保持不变。假设
$$
M_B=0,\qquad T_B=\kappa\mathfrak H,\quad \kappa\ne0,
\qquad \pi V_B=0.
\tag{1}
$$

最后一项是 [R210 §7.3](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md)式(17)及后续安装所给的**实际 universal whole-period pure 身份**；不是 pure 像或半群等号本身。使用 [R213](R213-two-mixed-sources-and-gauge-invariant-platform-obstructions-after-pure-closure.md)、[R227](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md)、[R241](R241-complete-sigma-four-layer-and-resonant-exceptional-germs.md)保留该实际身份的版本。

取从左至右排列、具有正间隙的紧支撑微包 $u_1,\ldots,u_n$，全部在同一合法 $I$ 内，令
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
\phi_\theta=\cos\theta f+\sin\theta g.
\tag{2}
$$
当前 R277—R287 类有 $a_i\ne0$；以下递推在此前提下陈述。若某 $a_i=0$，该外槽整行须保原零因子，不能对它除法。

记
$$
c_i=a_i\cos\theta+b_i\sin\theta,\quad
d_i=a_i^2-c_i^2,\quad R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,
$$
于是
$$
d_i=R_i\sin^2\theta-2T_i\cos\theta\sin\theta.
\tag{3}
$$
令
$$
\mu_i=(\mu_{i0},\mu_{i1},\mu_{i2})
=\left(\int(u_i'')^2,\ \int x(u_i'')^2,\
\int[x^2(u_i'')^2+2(u_i')^2]\right).
\tag{4}
$$
**不要求单个 $\mu_i=0$。** 整圆的三复矩和完整第三 ruling 仍按原完整包装支付；本稿不重新建立或改变它们。

以下 $H(U,V)$ 是 R56 的对称双线性 forcing，$\mathscr P H(U,V)$ 是按同一原 range 和全 $s$ 周期得到的 period。写
$$
Z_i=\operatorname{Range}H(Y_{u_i},Y_{u_i}),\qquad
C_{ij}=\operatorname{Range}H(Y_{u_i},Z_j).
\tag{5}
$$
这些单项是原 canonical 分解项，可以有真实左尾，不把它们当作各自双 collar 的实际控制路径。

在不交 compact 包上，标准 hook $\mathfrak H$ 的全部三槽限制为零：内槽不同包时 $P,R,S$ 的局部乘积为零；同一内包的 $P,S$ 左尾为常数、$R$ 左尾为仿射，进入另一外包的所需二阶导数为零；同一包使用 $\mathfrak H(u;u,u)=0$。这里 $P=J(u''v'')$、$R=u'v'+xJ(u''v'')$、$S=J(xu''v'')$，$\mathfrak H=[P,S]-3[P,R]$。因此(1)使所用 $Z_i,C_{ij}$ 的真实 $s$ history 周期；不会为了分包重置它们。

## 2. 零平台上必须保留的第四累计常数

用 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)的记号
$$
z=x+\omega,\quad e=hz-k,\quad
\gamma=h_s,\quad \nu=\omega_s=\frac{k_s}{2h},
$$
$$
K_0=kz^2-\frac{k^2+1}{h}z,\qquad
\lambda=\frac{\gamma z-h\nu}{h^2}.
\tag{6}
$$
在一个共同零平台上，真实二阶分子必为
$$
V_{Z_D}=xU(s)+V(s).
\tag{7}
$$
第四 forcing 是 $-H(Z_D,Z_D)-2H(Y_\phi,W_\theta)$。第二项局部为零，但其右积分一般没有消失。R56 的真实第四 $P_4$ 在该平台满足
$$
P_4=A_4x+B_4,\qquad A_4=\frac{|U|^2}{2h},
\tag{8}
$$
其中 $B_4$ 是由**完整右方 forcing**给出的实际累计值，包含 $Z^2$ 和 $YW$，不是可另选的积分常数。

局部分子为
$$
J_4=-|xU+V|^2,\qquad
T_{s,4}=-|x\nabla_sU+\nabla_sV|^2,\qquad B_H=\frac{J_4}{2h}.
$$
把这些量与(8)代入原完整式
$$
\mathcal R_4=\frac{T_{s,4}}{2h^2}
+K_0P_4-\lambda(P_4)_s
+\frac{K_0}{z}B_H-\frac{\gamma}{h^2}(B_H)_s
\tag{9}
$$
时，$x^3$ 项准确抵消。又因 $K_0$ 的一次系数与 $K_0/z$ 的常数系数之差为 $k\omega$，而两项 $\gamma(A_4)_s/h^2$ 相消，得到
$$
\boxed{
[x^2]\,\mathscr P H_{4,\theta}
=\int\left\{
k\left[B_4+\omega A_4-\frac{U\cdot V}{h}\right]
-\frac{|\nabla_sU|^2}{2h^2}
\right\}ds.}
\tag{10}
$$
这是逐原式收集后的真实平台二次系数。特别，即使 $U=V=0$，仍有 $\int kB_4\,ds$；不能从局部场零推出 period 零。

## 3. 真二阶左尾只依赖三个矩

对任意单包矩向量 $\mu$，设 $d=h\omega-k$、$Q_d=1+d^2$。由 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)式(2)、(10)、(12)，该包左外区间的原二阶量为
$$
p_\mu=\frac{Q_d\mu_0+2hd\mu_1+h^2\mu_2}{8h},
\qquad
W_\mu(s,x)=\Phi_{m(s)}(u,u)\big|_{\rm left},
\qquad m(s)=\int_{s_0}^sM.
\tag{11}
$$
$W_\mu$ 是二次 $x$ 多项式，三个系数均对 $\mu$ 线性；采用真实 $m(s_0)=0$。

为避免与包幅 $a_i,b_i$ 混淆，把该左尾写为
$$
\Pi_\mu=
(\mathfrak a_\mu z+t_\mu,\ p_\mu z,\ \eta_\mu z+q_\mu)
=xU_\mu+V_\mu.
\tag{12}
$$
其中
$$
U_\mu=(\mathfrak a_\mu,p_\mu,\eta_\mu),\qquad
V_\mu-\omega U_\mu=(t_\mu,0,q_\mu).
$$
若 $W_\mu=\mathfrak a_\mu x^2+\mathfrak b_\mu x+\mathfrak c_\mu$，其余量按原恢复式确定：
$$
t_\mu=\frac{\mathfrak b_\mu}{2}-\omega\mathfrak a_\mu-\frac{(p_\mu)_s}{2h},
$$
$$
\eta_\mu=-ht_\mu-k\mathfrak a_\mu-(p_\mu)_s,\qquad
q_\mu=-kt_\mu-h(\mathfrak c_\mu-\omega\mathfrak b_\mu+\omega^2\mathfrak a_\mu).
\tag{13}
$$
不能把这些量独立指定。

置 $\tau_\mu=(t_\mu)_s-\gamma t_\mu/h$。原齐次平台方程给
$$
(\mathfrak a_\mu)_s=kp_\mu,\quad
(\eta_\mu)_s-p_\mu=h\tau_\mu,\quad
(q_\mu)_s-\gamma q_\mu/h=-k\tau_\mu.
\tag{14}
$$
故有准确简式
$$
\boxed{\nabla_sU_\mu=(0,-ht_\mu,h\tau_\mu).}
\tag{15}
$$
至此只使用真实二阶累计 history 和同一原初值。

## 4. 跨包第四右尾的准确三矩闭合

设 $i<j$。在整个第 $i$ 包上，$Z_j$ 恰为(12)；不把这个真实仿射尾置零。R288 已证明 $C_{ij}$ 的整个场局域在第 $i$ 包。若 $i>j$，$Z_j$ 在第 $i$ 包上为零，故 $C_{ij}=0$。

以下固定 $j$，暂略下标，写 $u=u_i$。原 $Y_u$ 分子为
$$
V_Y=(-u'/2,0,hu-eu'/2).
$$
由于 $(\Pi_\mu)_x=U_\mu$ 不依赖 $x$，右锚积分准确给
$$
P_C=-\frac{V_Y\cdot U_\mu}{2h}
=\frac{\mathfrak a+e\eta}{4h}u'-\frac{\eta}{2}u,
$$
$$
(zP_C+B_C)=\frac q2u-\frac{t+eq}{4h}u'.
\tag{16}
$$
利用(14)在 R56 的完整 $\eta_0$ 式中收集 $u'',u',u$，得到
$$
\boxed{
\eta_{0,C}=\tau\left(\frac{1+e^2}{8h}u''
-\frac e4u'+\frac h4u\right).}
\tag{17}
$$
这里 $\nabla_s\Pi$ 的三个分量分别为
$$
\tau+\mathfrak a\nu+\gamma t/h,\qquad
-htz+p\nu+kt+q,\qquad
e\tau+\eta\nu+\gamma q/h.
$$
将它们直接代入
$-\!T_{s x}/(2h)+e_sP_x/(2h)+\gamma B_x/(2h)-P_s/2$
即得(17)；尤其没有删去 $P_s$ 或真实连接段项。

[R283](R283-canonical-end-layer-three-history-moments-and-pure-symmetry-cancellation.md)的原交叉计算在此为完整身份，而不只是渐近一次层：
$$
W_C=\beta(s,x)u'-\beta_x(s,x)u,\qquad \beta(s_0,x)=0,
$$
$$
\beta_s=\frac14\left[
\left(t-kq-\frac{\gamma\tau}{h}\right)\frac{1+e^2}{h^2}
-\tau\partial_s\left(\frac{1+e^2}{h^2}\right)\right].
\tag{18}
$$
$\beta$ 是二次 $x$ 多项式，其系数对 $\mu_j$ 线性。它的 $s$ 初值和全部累计积分均按(18)保留。

由 R56 恢复，令 $A_C$ 为新分子的第一分量，则
$$
A_C=\left(\frac{\beta}{2}+\frac{\tau(1+e^2)}{8h^2}\right)u''
-\frac{\tau e}{4h}u'
+\left(-\frac{\beta_{xx}}2+\frac{\tau}{4}\right)u,
$$
$$
(A_C)_x=
\left(\frac{\beta}{2}+\frac{\tau(1+e^2)}{8h^2}\right)u'''
+\frac{\beta_x}{2}u''-\frac{\beta_{xx}}2u'.
\tag{19}
$$
最后一个简式使用 $\beta_{xxx}=0$，保留了所有局部项。第三分量是 $eA_C-hW_C$。

因此
$$
V_{Y,x}\cdot V_{C,x}
=\frac12\left[
(he\,u'-(1+e^2)u'')(A_C)_x
+h(hu'-eu'')(A_C-(W_C)_x)\right].
$$
对整个第 $i$ 包积分。只使用 $u,u'$ 在包端为零，准确得到
$$
\boxed{
\int V_{Y,x}\cdot V_{C,x}
=\frac14\int\left[
\mathcal A_\beta(u'')^2+\mathcal A_\beta''(u')^2
\right],\qquad
\mathcal A_\beta=he\beta-\frac{1+e^2}{2}\beta_x.}
\tag{20}
$$

为核清此处没有隐藏尾，$\beta$ 部分在一次分部积分后分别给
$he\beta-(1+e^2)\beta_x/2$ 和
$h^2\beta_x-he\beta_{xx}$。$\tau$ 部分的 $(u'')^2$、$u'u''$ 项各自抵消；余量为
$$
\frac{\tau}{8}\int[-he(u')^2+h^2uu'-heuu'']=0.
$$
于是(20)没有借用 $\mu_i=0$。

$\mathcal A_\beta$ 的三次项相消，且
$\mathcal A_\beta''=h^2\beta_x-he\beta_{xx}$。若
$\beta=\beta_0+\beta_1x+\beta_2x^2$，则其二次系数向量为
$$
\mathbf a_\beta=
\left(
hd\beta_0-\frac{Q_d}{2}\beta_1,\
h^2\beta_0-Q_d\beta_2,\
\frac{h^2}{2}\beta_1-hd\beta_2
\right).
\tag{21}
$$
故(20)恰为 $\langle\mu_i,\mathbf a_\beta\rangle/4$。

记
$$
Q_{ij}(x)=\mathscr P H(Y_{u_i},C_{ij})(x)
$$
在第 $i$ 包左侧的二次尾。其 forcing 局域第 $i$ 包，真实 $P$ 左常数为(20)除以 $2h$。所有实际 $s$ 量周期，所以
$$
\boxed{
Q_{ij}(x)=\frac18\int
\frac{K_0(s,x)+\lambda_s(s,x)}{h(s)}
\,\langle\mu_i,\mathbf a_{\beta_{\mu_j}}(s)\rangle\,ds,
\qquad i<j.}
\tag{22}
$$
这是一条同一几何给出的真实三矩双线性式：
$$
Q_{ij}(x)=\mu_i^{\mathsf T}\mathcal M(x)\mu_j,
\qquad \deg_x\mathcal M\le2.
\tag{23}
$$
没有逐包重锚，没有新增研究评价，也不预宣该 $3\times3$ 矩阵的秩或零性。

## 5. actual pure 身份给完整有序平台公式

定义自项
$$
Q_{ii}(x)=\mathscr P H(Y_{u_i},C_{ii})(x)\big|_{\rm left}.
\tag{24}
$$
它也是二次多项式，但(20)不适用于它：$Z_i$ 在自己的包内不是仿射。其真实表达是
$$
Q_{ii}(x)=\frac12\int\frac{K_0+\lambda_s}{h}\,
\left(\int V_{Y_i,x}\cdot V_{C_{ii},x}\,dx'\right)ds.
\tag{25}
$$
保留的内积分、三阶场和初值都是原 canonical 对象。

还记 $Q^Z_{ij}=\mathscr P H(Z_i,Z_j)$。实际 universal pure 身份为
$$
-\mathscr P H(Z_{q^2},Z_{q^2})
-4\mathscr P H(Y_q,C(q;q^2))=0
\quad\text{对全部共同右锚紧 }q.
\tag{26}
$$
将 $q=\sum z_i u_i$ 代入并比较真实多项式系数。在任一共同零平台，若 $k\ne i$，则
$$
\mathscr P H(Y_{u_k},C_{ij})=0.
\tag{27}
$$
当 $i\ne j$，这是 R288 的整个 $C_{ij}$ 局域性。若 $i=j$ 且 $k<i$，$C_{ii}$ 在第 $k$ 包上有真实仿射分子，故其 $x$ 导数为常向量；完整 $P$ 尾正比于
$\int V_{Y_k,x}=0$，而 $B,T_s$ 在包外为零。若 $k>i$，该第三场在第 $k$ 包上本来为零。这逐项支付(27)，并未删除包内的真实 forcing。

由(26)、(27)，对共同左平台有
$$
Q^Z_{ii}=-4Q_{ii},\qquad
Q^Z_{ij}=-2Q_{ij}\quad(i<j).
\tag{28}
$$
canonical 第四 period 则按原规范为
$$
V_\theta^0=-\mathscr P H(Z_D,Z_D)
+4\mathscr P H(Y_\phi,C(\phi;D)).
$$
在任一零平台，只保该平台**右方**的微包。代入(27)、(28)准确得到
$$
\boxed{
V_\theta^0(x)=
4\sum_{\substack{i\le j\\i,j\ {\rm 在平台右方}}}
a_i^2d_j(\theta)\,Q_{ij}(x).}
\tag{29}
$$
对角合并用的是 $d_i^2+c_i^2d_i=a_i^2d_i$；交叉合并用
$d_i d_j+c_i^2d_j=a_i^2d_j$。这同时核清外槽 $i$ 与 $D$ 槽 $j$ 的指标及因子四。

式(29)保留了真正的顺序：只有外包在内包左方的 $Q_{ij}$ 出现。它不是仅由全部后缀矩的无序平方决定，更不能用完整圆的总矩为零删除。

## 6. 二次交叉系数只需原二阶 history

式(22)给整个交叉平台多项式。其二次系数还能免去额外的第三 $\beta$ 表示，直接写成 R73 的原二阶 history。

对 $i<j$，在两个包左方，$Z_j$ 的 $x$ 导数为 $U_j$。在第 $i$ 包及其左方皆如此，而 $Z_i$ 在第 $i$ 包右方为零。因此完整右锚式是
$$
P[H(Z_i,Z_j)](s,x)
=-\frac{V_{Z_i}(s,x)\cdot U_j(s)}{2h(s)}.
\tag{30}
$$
这不是重置常数，而是把原积分
$(2h)^{-1}\int_x^r V_{Z_i,x}\cdot V_{Z_j,x}$
准确积完。

把(30)、$B=V_{Z_i}\cdot V_{Z_j}/(2h)$ 代入 R56。与第2节相同，三次项以及 $\gamma$ 导数项相消，得到
$$
[x^2]Q^Z_{ij}
=\frac12\int\left[
\frac{\nabla_sU_i\cdot\nabla_sU_j}{h^2}
+\frac{k}{h}\,U_i\cdot(V_j-\omega U_j)
\right]ds.
\tag{31}
$$
再用(15)、(28)，定义真实有序双线性型
$$
\boxed{
\mathcal T_B(\mu,\widetilde\mu)
=-\frac14\int\left[
t_\mu t_{\widetilde\mu}+\tau_\mu\tau_{\widetilde\mu}
+\frac{k}{h}
\left(\mathfrak a_\mu t_{\widetilde\mu}
+\eta_\mu q_{\widetilde\mu}\right)
\right]ds.}
\tag{32}
$$
于是
$$
[x^2]Q_{ij}=\mathcal T_B(\mu_i,\mu_j),\qquad i<j.
\tag{33}
$$
该型的两个槽不能未经证明互换。它由同一个实际 $m(s)$、当前几何、原初值和全周期积分决定；没有把九个矩阵条目当作九个独立可调参数。

式(22)与(32)是同一原量的两种准确表示。前者给全部三项平台系数；后者把逆算子的关键二次项压到一个明确 $3\times3$ 二阶 history 矩阵。两式的相等在此由 actual pure 的交叉系数支付，不另假设某个规范形式完整。

自项二次系数仍为
$$
q_i:=[x^2]Q_{ii}
=\frac12\int\frac{k}{h}
\left(\int V_{Y_i,x}\cdot V_{C_{ii},x}\,dx'\right)ds.
\tag{34}
$$
它是一个指定单包的真实第四右尾 history。whole pure 只给(28)，没有给 $q_i=0$。

## 7. 全部零平台的准确递推及一个两包必要门

从最右平台向左逐包加入。由(29)，跨过第 $i$ 包时增加
$$
4a_i^2\left[d_iQ_{ii}+\sum_{j>i}d_jQ_{ij}\right].
\tag{35}
$$
最右平台恒为零。故全部共同零平台的二次系数均为零，当且仅当对每个 $i$ 有
$$
\boxed{
R_iq_i+\sum_{j>i}R_j\mathcal T_B(\mu_i,\mu_j)=0,\qquad
T_iq_i+\sum_{j>i}T_j\mathcal T_B(\mu_i,\mu_j)=0.}
\tag{36}
$$
这里使用 $a_i\ne0$。若有零外幅，保留(35)而不对该行除以 $a_i^2$。

因此最右包必有
$$
q_n=0,
\tag{37}
$$
因为非零 $(a_n,b_n)$ 不可能同时满足 $R_n=T_n=0$。若最右两包的双角向量不共线，即
$$
R_{n-1}T_n-T_{n-1}R_n\ne0,
\tag{38}
$$
则第二个平台再准确强迫
$$
\boxed{
q_{n-1}=0,\qquad \mathcal T_B(\mu_{n-1},\mu_n)=0.}
\tag{39}
$$
这是固定当前几何、同一圆的一个具体必要门。它不需要先判所有单包自项，也不由全局有限差分的总矩自动推出。

同理，消掉任一行的 $q_i$ 给
$$
\sum_{j>i}(T_iR_j-R_iT_j)\mathcal T_B(\mu_i,\mu_j)=0.
\tag{40}
$$
不称这些行独立，不把现有模板的有限符号类型冒作其全部秩。

若需要整个平台 period 自身为零，而不仅二次系数，(35)—(36)可直接按 $x^0,x^1,x^2$ 三个真实系数使用；其中跨包项用(22)，自项用(25)。这仍保留所有三阶 history 和第四右累计。

## 8. 三矩锥有内点，但不足以删掉自历史

三矩的真实开集性质可以完整支付。固定一个非零偶紧 $u$，令
$$
u_{\zeta,c,w}(x)=\zeta w^{3/2}u((x-c)/w),\qquad
\zeta>0,\ w>0.
$$
只在一个预留开包络内作小参数变化。置
$$
m=\int(u'')^2>0,\qquad
\nu_*=\frac{\int[y^2(u'')^2+2(u')^2]}{m}>0.
$$
则
$$
\mu=\zeta^2m\,(1,c,c^2+\nu_*w^2).
\tag{41}
$$
以 $(\mu_0,\mu_1/\mu_0,\mu_2/\mu_0-(\mu_1/\mu_0)^2)$ 为坐标，此映射是
$(\zeta^2m,c,\nu_*w^2)$，Jacobian 非零。因此一个固定自由开区间内的合法真实单包矩像包含 $\mathbb R^3$ 的开集。两个固定不交包络给相应的积开集。

所以，如果另已证明(32)对这些全部配对为零，确可推出其九条矩阵系数全零。这一步不需新的 profile 采样。

但 current whole pure 身份是(26)，其左平台结论为
$Q^Z_{ii}+4Q_{ii}=0$。它没有把(25)变成仅依赖 $\mu_i$ 的某个已知二次型，更没有证明该自项为零。式(10)中的真 $B_4$ 正是原先不能略过的另一部分。因此不能从(41)直接宣称全部平台已经支付。本稿给出的(32)、(34)、(36)保留了这一准确差别。

## 9. 与真实全局 gauge、端芽逆解及剩余工作的关系

R181 的原 $L_f$ 身份（见 [R213 §3](R213-two-mixed-sources-and-gauge-invariant-platform-obstructions-after-pure-closure.md)所用完整全局版本）在 $f=0$ 的开平台上给
$$
(L_fw)''=0
$$
对任意允许的**全 $I$**光滑二阶 gauge 都成立。它不要求 $w$ 支撑该平台，也不把其右尾设为零。第三齐次 gauge 在 $M_B=0$ 下不改变第四 period。因此(36)—(40)的二次平台门不能由所允许的二、三阶 gauge 修掉。

对于 R281 的解析零端，R288 已付真正的一次指数层。结合 [R276](R276-canonical-fourth-periods-at-analytic-zero-ends-and-finite-first-layer-conditions.md)，还必须实际支付这里的二次平台条件和正确的端通量分支，才可调用相应光滑逆 germ。平台的仿射部分、内部退化匹配、全局交叉矩与同一个 $w_\theta$ 的 ruling 条件继续分别保留。

本稿未评价(32)或(34)，未证明它们非零，也没有把已付七十二个 Gaussian 面积、六个能量或若干对称乘积自动当作这些真实 history 的消去证书。已经完成的是：

- 完整第四零平台二次系数(10)，保全部 $YW$ 右尾；
- 跨包尾的原三矩双线性式(22)，及只含真实二阶 history 的准确矩阵(32)；
- actual pure 身份下的整个有序平台公式(29)和必要充分的二次递推(36)；
- 对最右两包的明确必要门(39)，以及真实矩开集的合法性(41)。

下一可消费目标已经具体到同一几何的 $\mathcal T_B$ 及指定单包的 $q_i$。它们若能由原真实 identity 消掉，应逐式说明；若需要新实际求值，应只消费这些明确原源，不重跑旧 pure、Gaussian 或已付能量目标。
