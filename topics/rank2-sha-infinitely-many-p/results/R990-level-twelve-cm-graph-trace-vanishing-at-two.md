# R990 — level12 新 CM 图族的实际 dyadic trace 为零

日期：2026-11-26。会话：`Astra-rank2-Sha-0b097461-20261127`。

**状态：已证明。R988(35)–(38) 给出的 degree17 CM 图族，在取到原 $H/K$ 的 trace 后已在有理 Chow 群中为零；任取兼容的 level12 结构、任取18个循环17子群及三个原 $\eta_j$ 均如此。证明使用实际二同源、全二级结构的甲板 transposition 和一个指定的局部 Artin 元，不从 $L$ 值或一般 regulator 注入推出。R988 的 Chow 双逆及其全 AJ 交换图保持成立；本篇限制的是它新定义的这一族循环，不涉及 R854 的旧 canonical 循环或 R831 的原生成曲线端点。**

下文先给实际循环的 Chow 零证明，再单独付清相应的全局部表示 Hom 消失。第二个证明不被当作从局部表示到 Chow 群的未经证明的桥。

## 1. 固定原对象与一个真实二同源

沿 R862、R988，固定
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad E_0:y^2=x^3+1,
$$
以及原 $H/K$、$[H:K]=18$、三个 $\eta_j$ 和
$\lambda_j=\eta_j^{-1}\psi_0^3$。
原角色的完整导子为
$$
\mathfrak f_{\psi_0}=(2\delta),\qquad
\mathfrak f_{\eta_j}=(34),\qquad
\eta_j(\delta)=-1.
\tag{1}
$$
这里 $\psi_0$ 是原 $E_0$ 的角色，而非另一条 $j=0$ 曲线的角色。

令 $S$ 为 R988 的光滑极小椭圆 K3，模群的正确 SL lift 为
$$
\Gamma=\Gamma_0(12)\cap\Gamma_1(3).
$$
一个非 cusp 模点可以写成 $(E,C_4,P_3)$，其中 $C_4$ 为循环四阶子群，
$P_3$ 为三阶点。这与 R988 的 $(E,C_{12},P_6)$ 等价。
令 $C_2=2C_4$，并作实际商同源
$$
q:E\longrightarrow \widetilde E=E/C_2.
\tag{2}
$$
设 $A$ 是 $q(E[2])$ 的唯一非零点；若 $P$ 生成 $C_4$，令 $B=q(P)$。
由于 $q(-P)=q(P)$，$B$ 不依赖 $P$ 的正负选择。
又 $B\notin\{0,A\}$，故 $(A,B)$ 是 $\widetilde E[2]$ 的有序基。
置 $\widetilde P_3=q(P_3)$。

这给模问题的同构
$$
(E,C_4,P_3)\longmapsto
(\widetilde E,A,B,\widetilde P_3).
\tag{3}
$$
其逆由 $\widetilde E\to\widetilde E/\langle A\rangle$ 的对偶二同源给出：
$C_4$ 是 $\langle B\rangle$ 的逆像，三阶点由同源在三挠点上的逆恢复。
若用复解析群，(3) 对应
$$
D\Gamma D^{-1}=\Gamma(2)\cap\Gamma_1(3)=:\Gamma',
\qquad D=\begin{pmatrix}2&0\\0&1\end{pmatrix}.
\tag{4}
$$
确实 $D\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}D^{-1}
=\begin{psmallmatrix}a&2b\\c/2&d\end{psmallmatrix}$；
$12\mid c$ 恰变成下左项被6整除，另外两项模3仍为1。
在(4)中显式保留 $\Gamma_1(3)$，从而 $-I$ 不在 lift 中。

因此(2)给实际椭圆模曲面间的次数2有理映射
$$
q:S\dashrightarrow S',\qquad S'=E(\Gamma')^{\rm min}.
\tag{5}
$$
可用图的解消解释所有 Chow 推拉。它是 $S$ 上通用二挠点平移的商。
该平移保持纤维微分及基底微分的楔积，是 symplectic involution；
商的极小解消 $S'$ 仍为 K3。
它也就是 [LY, Table2 第2项] 的正抛物 lift，纤维为
$I_6,I_6,I_6,I_2,I_2,I_2$。
由(5)在 transcendental cohomology 上的单射和 $S$ 的 transcendental rank2，
$S'$ 的 transcendental rank 也为2，故 $\rho(S')=20$。
[TY, §2.3 开头] 给出了这两个模群通过次数2同源联系的同一几何关系。

令 $M=t_2(S)$、$M'=t_2(S')$。
R988 已支付 $S$ 的 finite-dimensional Chow motive 以及 symplectic involution
在 $t_2(S)$ 上作用为恒等。故解消后的图对应满足
$$
q_*q^*=2\,1_{M'},\qquad q^*q_*=2\,1_M,
\qquad q_*^{-1}=\tfrac12q^*.
\tag{6}
$$
特别地 $M'$ 有限维。这里的(6)是 Chow 等式。
异常曲线只给 Tate summand，投到 $t_2$ 后消失。

## 2. 全二级结构的 transposition 在 Chow 的 $t_2$ 上等于 $-1$

$S'$ 的模问题具有定义于 $\mathbf Q$ 的甲板群
$$
G=\mathrm{GL}_2(\mathbf F_2)\simeq S_3,
\tag{7}
$$
只改变 $(A,B)$，不改变 $\widetilde E$、其纤维点或 $\widetilde P_3$。
模群方面，这是 $\Gamma'\triangleleft\Gamma_1(3)$ 的商；
CRT 给 $\Gamma_1(3)$ 模2的满像。
甲板有理自同构延伸为光滑极小 K3 的自同构。

商 $S'/G$ 双有理于带三阶点的通用 Tate 曲面
$$
y^2+xy+t y=x^3.
\tag{8}
$$
该曲面为有理曲面，因为在 $y\ne0$ 的稠密开集上
$t=(x^3-y^2-xy)/y$，函数域是 $\mathbf Q(x,y)$。
故 $H^{2,0}(S')^G=0$。
另一方面 $H^{2,0}(S')$ 一维，$S_3$ 的一维特征只有平凡特征与 sign。
因此其特征必为 sign。
由于 $t_2(S')$ 的 Betti realization 恰为
$H^{2,0}\oplus H^{0,2}$，每个 transposition $\tau$ 在这个 realization 上为 $-1$。

选择 $G$-不变的 Chow–Künneth projector。
可以从零截面上的次数1零循环和全 NS 的交矩阵构造：
零截面是有理曲线，其上的点均给同一有理 Chow 类；$G$ 保持零截面，
NS projector 用交矩阵的逆，故与 $G$ 交换。
于是 $\tau$ 是 $M'$ 的真实 involution，
$$
e_+=\frac{1+\tau}{2}\in\operatorname{End}(M')
$$
是 homologically trivial 的幂等对应。
finite-dimensional nilpotence 使 $e_+$ 幂零；幂等且幂零只能为零。
我们因而得到
$$
\boxed{\tau=-1\quad\text{in }\operatorname{End}_{\rm Chow}(t_2(S')).}
\tag{9}
$$
这一步使用的不是“纯 Hodge 类型自动决定混合循环”。
实际有限群幂等子与已经支付的有限维性是从 realization 到 Chow 等式的理由。

对(5)的推拉，可以使用同样的零截面零循环和 NS projector。
零截面点的逆像由零截面与二挠截面上的点组成，二者均为有理曲线。
选一个 $I_n$ cusp 纤维，其分量是连通的有理曲线链/圈，连接两个截面；
逐条在这些有理曲线上作有理等价，两个截面上的点给同一个次数1类。
故 $q^*o_{S'}=2o_S$、$q_*o_S=o_{S'}$。
在 divisor 部分，$q_*$、$q^*$ 保持 NS 且彼此为交配对的伴随。
这些等式使 $t_2$ projector 与 $q$ 的推拉相容。
所以后面“先投原 $t_2$ 再推前”与“推前真实图再投新 $t_2$”确实相同，
没有遗漏一个未控制的 Tate-to-transcendental Chow 对应。

## 3. 指定局部 Artin 元与完整全局兼容

取有限 idèle $x$，其2分量为
$$
u=1+2\omega=\delta\in\mathcal O_{K,2}^{\times},
\tag{10}
$$
其余所有有限分量及无穷分量为1。
令 $\sigma=\operatorname{Art}_K(x)$，采用 R862 的同一 reciprocity 方向。
这是一个**只在2处支撑的 idèle**，不是对角嵌入的全局元素 $\delta$。
因此不能用“$u=\delta$ 是全局元素”把 $\sigma$ 误删掉。

首先 $u\equiv1\pmod2$。
由(1)，$\eta_j$ 的2局部分量在 $1+2\mathcal O_{K,2}$ 上平凡，故
$$
\eta_j(\sigma)=1\quad(j=4,10,16),\qquad \sigma|_H=1.
\tag{11}
$$
这里 $\eta_{10}$ 忠实，故后三角色条件确实固定整个 $H$。
若将 $x$ 乘以对角 principal idèle $\delta^{-1}$，2分量变为1，
但3分量成为 $\delta^{-1}$，17分量也成为单位 $\delta^{-1}$，
而无穷分量也相应改变。
原 $\eta_j(\delta)=-1$ 的3处值和17处单位值相互抵消；
这正是完整全局角色对 principal idèle 平凡的关系。
不能只保留3处因子，也不能删除原17处有限角色。

对 $E_0$ 使用 CM 主定理的 Tate-module 版本
（[Si, ChapterII §§8–9]；原主理想公式为 R862(7)之前的公式）。
$\psi_0$ 的2处光滑有限分量在 $1+2\mathcal O_{K,2}$ 上平凡。
故对于任何 $m$ 与2互素，
$$
\sigma|_{E_0[m]}=1.
\tag{12}
$$
在二进 Tate module 上还须乘 CM 型给出的2分量的逆，因而
$$
\rho_{E_0,2}(\sigma)=u^{-1}.
\tag{13}
$$
若整体采用相反 Artin 方向，(12)不变而(13)改为 $u$；
本篇实际只用
$$
u^{-1}\equiv u\equiv1+2\omega\pmod4,
\tag{14}
$$
所以这个方向变化不改变任何后续几何作用。
等式(13)是二进 Tate module 的公式；不能把(12)的 prime-to-2 公式误用于 $E_0[4]$。

从(12)–(14)得到全部所需固定数据：
$$
\sigma|_{E_0[17]}=1,\quad
\sigma|_{E_0[3]}=1,\quad
\sigma|_{E_0[2]}=1,
\quad
\sigma(P)=P+[\omega](2P)\quad(P\in E_0[4]).
\tag{15}
$$
这也直接证明所选 idèle 并未被全局 principal 关系杀掉：
它在 $E_0[4]$ 上非平凡。

可以统一取包含 $K(E_0[204])$ 的一次有限 Galois 扩张 $M_0/K$ 来定义全部图与 level 数据。
R862 已证明 $H\subset K(E_0[17])$。
若 R988 的初始定义域更小，先放大到这样的 $M_0$；
对原已定义循环的 trace 只乘一个非零整数，故下面的有理 Chow 零结论仍下降到原定义域。

## 4. 它对实际图循环恰给一个甲板 transposition

固定 R988(35) 的循环17子群 $C_{17}\subset E_0[17]$、实际同源
$$
\varphi:E_0\longrightarrow E'=E_0/C_{17},
$$
以及任意 $C_4\subset E_0[4]$ 和三阶点 $P_3$。
在 $E'$ 上使用它们经 $\varphi$ 运输的 level。
由(15)，$\sigma$ 固定 $C_{17}$、$\varphi$、$P_3$ 以及 $2C_4$。
因此也固定实际二次商
$$
q_\varphi:E'\longrightarrow E''=E'/\varphi(2C_4),
\qquad q_\varphi\varphi:E_0\longrightarrow E''.
\tag{16}
$$

若 $P$ 生成 $C_4$，则在(3)的全二级结构中
$$
A=q_\varphi\varphi(R),\quad
B=q_\varphi\varphi(P),
\qquad R\in E_0[2]\setminus 2C_4.
$$
$E_0[2]$ 是 $\mathbf F_4$ 上的一维空间，$\omega$ 的乘法在
它的三个非零向量上循环。
故 $2P$ 和 $[\omega](2P)$ 线性无关，后者不在 $2C_4$ 中。
使用(15)即得
$$
\sigma(A)=A,\qquad \sigma(B)=B+A,
\qquad \sigma(q_\varphi\varphi(P_3))=q_\varphi\varphi(P_3).
\tag{17}
$$
因此 $\sigma$ 对全二级模点的作用恰为
$$
\tau:(A,B)\longmapsto(A,B+A),
\tag{18}
$$
这是 $S_3$ 中的 transposition。
它在纤维 $E''$ 本身及实际同源(16)上没有另加一个未计的 CM automorphism。
原因是(12)固定了原 $\varphi$，而 $q_\varphi$ 是固定子群的规范商；
只改变的是全二级结构的标记。

令 $G_\varphi\subset S\times E_0$ 是 R988 的图。
其在 $q\times1$ 下的推前正是
$$
\widetilde G_\varphi
=\{(q_\varphi\varphi(Q),Q):Q\in E_0\}
\subset S'\times E_0.
\tag{19}
$$
由于保留外部坐标 $Q$，图到图的次数为1，推前没有多出2的系数。
(17)给真实循环等式
$$
\sigma\widetilde G_\varphi=(\tau\times1)_*\widetilde G_\varphi.
\tag{20}
$$
所有图、同源、有限群作用以及所用 projectors 在固定有限扩张内定义；
(20)不是仅在 cohomology 中的等式。

## 5. 原 trace 为零，三个有限角色均不能恢复它

在 $S'\times E_0$ 上令
$$
c_\varphi=(\pi_{\rm tr}^{S'}\otimes\pi_1^{E_0})_*
                                      [\widetilde G_\varphi].
$$
它在 $\mathrm{CH}^2_{\rm hom}$ 中，因为该 projector 只有次数3 realization。
由(9)、(20)及 projector 的 $K$ 定义性，
$$
\sigma c_\varphi=-c_\varphi.
\tag{21}
$$
因为 $\sigma\in\operatorname{Gal}(M_0/H)$，trace 的置换不变性给
$$
\begin{aligned}
\operatorname{Cor}_{M_0/H}(c_\varphi)
 &=\operatorname{Cor}_{M_0/H}(\sigma c_\varphi)\\
 &=-\operatorname{Cor}_{M_0/H}(c_\varphi).
\end{aligned}
$$
因此
$$
\boxed{\operatorname{Cor}_{M_0/H}(c_\varphi)=0
       \quad\text{in }\mathrm{CH}^2((S'\times E_0)_H)_{\mathbf Q}.}
\tag{22}
$$
由(6)和§2末的实际 projector 相容，(22)拉回给
$$
\operatorname{Cor}_{M_0/H}
  \bigl((\pi_{\rm tr}^{S}\otimes\pi_1)_*[G_\varphi]\bigr)=0.
\tag{23}
$$
R988 的 $\Pi_S^+$ 定义于 $K$，从而与 corestriction 交换。
对(23)再施加 $\Pi_S^+$ 和三个 $e_{\eta_j}$，便得到
$$
\boxed{Z_j^S=0,\qquad Z_j^E=0\quad(j=4,10,16).}
\tag{24}
$$
等式对任意 degree17 循环子群与兼容 level 选择成立。
因此扩大这个固定有限族、取它们的线性组合、或只换一个 level 标记，均不解除本 trace 消失。
所有 $\ell$-adic AJ 图像及其 ordinary/local 对数自然同时为零。
本篇不声称整个 $\mathrm{CH}^2(E_0^3)^{\Pi_3^+,\eta_j}$ 为零；
(24)仅适用于 R988 定义的新图族，绝不应用于此前的原端点或 canonical 循环。

## 6. 独立核算完整局部 Hom，包含所有平移

这里单独解释(24)对应的局部表示障碍。
取 $F=\mathbf Q_2$、$L=K\otimes\mathbf Q_2$，后者是非分歧二次扩张。
置 $G_2=\mathrm{GL}_2(F)$、$K_2=\mathrm{GL}_2(\mathbf Z_2)$、
$T=L^\times$、$Z=F^\times$。
R988 的 $f_{12}=\theta(\psi_0^2)$ 在2处为 depth-zero supercuspidal，
其有限型是
$$
\tau_0:\mathrm{GL}_2(\mathbf F_2)\simeq S_3
                 \xrightarrow{\rm sign}\{\pm1\}.
\tag{25}
$$
确实 $\psi_0^2$ 的单位型为 $\mathbf F_4^\times$ 的非平凡三次特征，
其 Frobenius 共轭为另一个非平凡特征；这是 regular admissible pair。
对应 finite cuspidal 的维数为 $q-1=1$，且无 unipotent 固定向量，故恰为 sign。
在延伸中央特征后
$$
\pi_2=\mathrm{c\!-!Ind}_{ZK_2}^{G_2}\tau_0.
\tag{26}
$$
[Kn, §5.1, pp.388–389] 的构造明确包含偶数 $q$；
这里不将只在奇素数下表述的 test-vector 公式硬用于2。
可能的非分歧 rectifier 不改变以下单位群计算。

保原 $\lambda_j$ 的 Rankin 环面角色（及其逆，依配对方向）是
$$
\chi_j=\eta_j\psi_0^{-1}.
\tag{27}
$$
其单位部分在 $1+2\mathcal O_L$ 上平凡，在 $\mathbf F_4^\times$ 上非平凡。
例如，R862 的主理想公式给
$\psi_{0,2}|_{\mathbf F_4^\times}=\epsilon_2$、
$\eta_{j,2}|_{\mathbf F_4^\times}=\epsilon_2^{-1}$，
故(27)的单位型为 $\epsilon_2$。
用 $\chi_j^{-1}$ 则为 $\epsilon_2^{-1}$，结论相同。
适当非分歧范数归一使中央特征相配；若不相配，Hom 更直接为零。

现证明任何具有这种单位型的 $\chi$ 都满足
$$
\boxed{\operatorname{Hom}_{T}(\pi_2,\chi)=0.}
\tag{28}
$$
令 $v_0$ 是 Bruhat–Tits 树中 $\mathcal O_L$ 对应的顶点。
$T/Z$ 固定 $v_0$，并在每个距离 $n\ge1$ 的球面上传递。
可以直接核其稳定子：以 $(1,\omega)$ 为基，取
$$
g_n=\begin{pmatrix}1&0\\0&2^n\end{pmatrix}.
$$
顶点 $g_nv_0$ 的 $\mathcal O_L^\times$ 稳定子是
$\mathbf Z_2^\times(1+2^n\mathcal O_L)$，其指数为
$3\cdot2^{n-1}$，恰为球面的顶点数。
因此 $T\backslash G_2/(ZK_2)$ 的代表正是全部 $g_n$，$n\ge0$。

对 $n=0$，sign 限制到 $\mathbf F_4^\times=C_3$ 是平凡特征，
而 $\chi$ 非平凡，故 Mackey 的这一项无 Hom。
对任意 $n\ge1$，取 $t_n=1+2^n\omega$。
它在交稳定子中，且 $\chi(t_n)=1$。
乘法矩阵及共轭为
$$
t_n=\begin{pmatrix}1&-2^n\\2^n&1-2^n\end{pmatrix},\qquad
g_n^{-1}t_ng_n
 =\begin{pmatrix}1&-2^{2n}\\1&1-2^n\end{pmatrix}
 \equiv\begin{pmatrix}1&0\\1&1\end{pmatrix}\pmod2.
\tag{29}
$$
最后一个矩阵是 transposition，故其 sign 为 $-1$。
于是每个 $n\ge1$ 的交稳定子上两角色仍不相配。
Mackey 分解逐项给(28)，涵盖全部局部平移，不仅是标准 newvector。

§§1–5 已用实际图和实际 Galois 元支付局部障碍到所选循环的关系；
(28)本身不被滥用为任意 motivic class 的零判据。

## 7. 本结论消除的方向与保留的目标

R988 的 $t_2(S)\simeq t_2(E_0^2)$ 及三次 projector 的 Chow 双逆保持有效。
本篇排除的是“在这个 level12 通用族上取与2互素的原 degree17 图，
然后 trace 到原 $H$”作为新增非零输入的方案。
原 $H$ 在2处只承载 tame 三次角色，无法承载(21)的 principal-unit 反号。

继续研究须改变实际辅助模对象或循环构造，使2处没有此 sign 阻碍，
并逐处重付原 $\lambda_j$ 的有限扭曲；增加同一族的样本不能解决(24)。
本篇不把新来源的仅有纯表示识别或一个 $L$ 因子的非零值登记为 AJ 非零。
原唯一 v8 的生产源、参数和数学门没有改变，本篇没有发新计算作业。

## 8. 出处

- R862，原 $E_0$、完整 Hecke 主理想公式、$H\subset K(E_0[17])$。
- R988，实际 level12 K3、finite-dimensional Chow 双逆、(35)–(38) 新图族。
- [LY] Ron Livné, Noriko Yui, *The modularity of certain non-rigid Calabi–Yau threefolds*,
  Journal of Mathematics of Kyoto University45 (2005), 645–665，Table2、Proposition4；
  [arXiv:math/0304497v2](https://arxiv.org/abs/math/0304497v2)。
  本文用(4)明确写出不含 $-I$ 的 SL lift，不依赖省略 lift 的群记号。
- [TY] Jaap Top, Noriko Yui, *Explicit equations of some elliptic modular surfaces*,
  Rocky Mountain Journal of Mathematics37 (2007), 663–687，§2.3；
  [作者原文](https://www.math.rug.nl/~top/top-yu.pdf)。
- [P] Claudio Pedrini, *On the finite dimensionality of a K3 surface*,
  Manuscripta Mathematica138 (2012), 59–72，Theorems2–3；
  [arXiv:1106.1115](https://arxiv.org/abs/1106.1115)。
- [K] Shun-Ichi Kimura, *Chow groups are finite dimensional, in some sense*,
  Mathematische Annalen331 (2005), 173–201，Proposition7.5；
  [DOI](https://doi.org/10.1007/s00208-004-0577-3)。
- [Si] Joseph H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*,
  GTM151, Springer1994，ChapterII §§8–9，CM 主定理及关联 Grössencharacter；
  [作者书页](https://www.math.brown.edu/johsilve/ATAECHome.html)。
- [Kn] Andrew Knightly, *Counting locally supercuspidal newforms*,
  Essential Number Theory4 (2025), 349–438，§5.1, pp.388–389；
  [DOI](https://doi.org/10.2140/ent.2025.4.349)，
  [作者预印本 §5.1](https://arxiv.org/html/2310.17047v2#S5.SS1)。
  已直接核对 compact induction、维数 q−1、无 unipotent 固定向量及偶数 q 的(5.1)。
