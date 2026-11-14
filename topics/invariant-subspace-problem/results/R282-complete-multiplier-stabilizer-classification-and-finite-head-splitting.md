# R282：全部可测乘法稳定代数、有限头分裂与无限位排除

日期：2026-11-14。作者：Astra-ISP-789f / normal_annihilator。AI-assisted：ChatGPT，GPT-6 Astra Pro。

**状态：完整证明。** 这是 R280 加权因子/逐点子格类别之外的投影结构约束。§§1–5 首先独立证明：若原 $A$ 的不变闭子空间是某个固定头之后全部可测乘法的模，则它平凡，允许头纤维为任意有限维子空间。§§6–8 完整分类每个未知不变投影所交换的可测乘法代数：对非零真空间，它恰为某个有限低头代数，且原空间在该头上精确分裂为完整头张量尾空间。§9 用实际限制稠密性和 Prüfer 角色的有限阶进一步证明：任何单向保持该空间的复乘子都自动减少它，因而全部单向稳定乘子也正是同一个有限头代数。特别，任意无限个物理位指标均保持该空间，或任何非有限柱的复乘子保持它，都迫使空间平凡。结论不排除一般不变投影。

## 1. 原进位块与假设

固定 $m\ge1$，置 $q=2^m$。写 $y=r+qz$，$0\le r<q$；Haar 测度给

$$
H=\mathbb C^q\otimes L^2(\mathbb Z_2,\mu).
$$

对原径向权 $w(y)=a_{v_2(y)}$，$a_j>0$，有准确块公式

$$
A=J\otimes I+e_{0,q-1}\otimes T_m,
\quad J=\sum_{r=1}^{q-1}c_r e_{r,r-1},
\quad c_r=a_{v_2(r)}>0,
\tag{1.1}
$$

$$
(T_mf)(z)=a_{m+v_2(z)}f(z-1).
\tag{1.2}
$$

在零测点 $z=0$ 沿用原权为零。记

$$
\mathcal D_m=\{I_q\otimes M_b:b\in L^\infty(\mathbb Z_2,\mu)\}.
$$

**定理。** 若闭子空间 $M\subset H$ 满足

$$
AM\subset M,\qquad \mathcal D_m M\subset M,
\tag{1.3}
$$

则 $M=0$ 或 $H$。

## 2. 尾乘法模给出真实有限投影场

令 $P$ 为到 $M$ 的正交投影。$\mathcal D_m$ 自伴，所以其不变性使 $M$ 同时减少该代数，故 $P\in\mathcal D_m'$。

按头矩阵写 $P=(P_{rs})$，每个 $P_{rs}$ 都与全部尾乘法交换。下面自含说明它必为乘法：若 $B\in B(L^2(\mu))$ 与所有指标乘法交换，置 $b=B1$，则对简单函数 $s$ 有 $Bs=bs$。又

$$
\|\mathbf1_Eb\|_2=\|B\mathbf1_E\|_2\le\|B\|\sqrt{\mu(E)}
$$

对全部可测 $E$ 成立，故 $|b|\le\|B\|$ 几乎处处；由简单函数稠密性，$B=M_b$。

因此 $P$ 是可测矩阵投影场 $P(z)\in M_q(\mathbb C)$。有限多个条目允许在同一满测集合逐点保证

$$
P(z)=P(z)^*=P(z)^2.
\tag{2.1}
$$

不要求 $P(z)$ 的秩起初常数。

## 3. 一个完整进位周期迫使投影场为常值

由原 (1.1) 的一个完整循环，或者逐点相乘 $q$ 个真实权，得到

$$
A^q=\beta_m I_q\otimes T_m,
\qquad \beta_m=\prod_{r=1}^{q-1}c_r>0.
\tag{3.1}
$$

这是准确等式，不是忽略尾进位的近似。$A^qM\subset M$ 和 (2.1) 给

$$
(I-P(z))P(z-1)=0\quad\text{几乎处处},
\tag{3.2}
$$

因为 (1.2) 的权非零几乎处处，可以从对应加权复合算子零式中消去该标量乘子。

若 $r(z)=\operatorname{rank}P(z)$，(3.2) 给 $r(z-1)\le r(z)$。$r$ 为取值 $0,\ldots,q$ 的可积函数；Haar 保测性使两边积分相等，故秩相等几乎处处。相同有限维数的子空间包含必为相等，于是

$$
P(z-1)=P(z)\quad\text{几乎处处}.
$$

尾 odometer 遍历；对有限个矩阵条目分别应用遍历性，得到存在常值投影 $P_0\in M_q(\mathbb C)$ 使

$$
P(z)=P_0\quad\text{几乎处处}.
\tag{3.3}
$$

到此尚未声称 $P_0$ 为对角投影。

## 4. 原单步进位排除所有常值真头子空间

取真实尾的最低位角色

$$
b(z)=(-1)^{z\bmod2},\qquad B=I_q\otimes M_b.
$$

有 $B^2=I$、$M_bT_mM_b=-T_m$，所以

$$
\frac{A+BAB}{2}=J\otimes I,\qquad
\frac{A-BAB}{2}=e_{0,q-1}\otimes T_m.
\tag{4.1}
$$

按 (1.3)，$A$、$B$ 都保持 $M$，因此 (4.1) 的两个算子都保持 $M$。不涉及缩放小误差或逆掉 $T_m$。

由 (3.3)，$M=V\otimes L^2(\mu)$，其中 $V=\operatorname{Ran}P_0$。第一式给 $JV\subseteq V$。由于 $J$ 是所有次对角权均非零的单个 Jordan 块，其全部不变子空间为

$$
V_k=\operatorname{span}\{e_k,\ldots,e_{q-1}\},
\quad 0\le k\le q,
\tag{4.2}
$$

其中 $V_q=0$。为核对 (4.2)，若 $V\ne0$，取其向量可能非零的最小坐标 $k$，并选该坐标非零的 $v\in V$。向量 $v,Jv,\ldots,J^{q-1-k}v$ 在尾坐标上的矩阵为对角非零的三角矩阵，因此张成全部 $V_k$。按 $k$ 的最小性又有 $V\subseteq V_k$，故相等。

若 $V_k\ne0$，则 $e_{q-1}\in V_k$。在第二式 (4.1) 中取某个 $T_mf\ne0$ 的 $f$，得到

$$
e_0\otimes T_mf\in V_k\otimes L^2(\mu).
$$

因此 $e_0\in V_k$，只能 $k=0$，即 $V=\mathbb C^q$。定理得证。$\square$

## 5. 等价的物理高位投影表述

对第 $j$ 位的原物理指标投影记为 $P_j^0,P_j^1$。若某个普通 $A$ 不变闭子空间在每个 $P_j^0$（$j\ge m$）下不变，则它也减少这些自伴投影。有限乘积和有限线性组合生成所有高位柱乘法；其强闭包为 $\mathcal D_m$，闭子空间对一致有界强极限保持不变，故满足 (1.3)。因此同样只能是 $0$ 或 $H$。

也就是说，任何尚未知的非零真普通不变投影都不可能只在固定有限头上偏离对全部物理位投影的交换；它必须在任意远处仍有真实的尾非对角结构。

本文只处理固定 $m$ 下的准确尾乘法模。没有把近似交换、小缺陷、压缩的有限维近似或某个移动头序列升级为这一准确假设。R30 对任意投影的压缩问题、一般正常见证及 ordinary ISP 仍未解决。

## 6. 任意未知不变空间的乘法稳定代数

本节起使用原模型的额外已证事实 [R12 §5](R12-normalized-powers-and-compact-commutant.md)：

$$
AM\subset M,\ M\text{ 闭}
\quad\Longrightarrow\quad\overline{AM}=M.
\tag{6.1}
$$

为保持证明自含，回顾其直接来源：实际 $N_j=A^{2^j}/\|A^{2^j}\|$ 一致有界且 $N_j\to I/2$ 于 WOT。对固定 $f\in M$，$N_jf\in AM$，而 $N_jf\rightharpoonup f/2$。线性空间 $AM$ 的范数闭包亦弱闭，故 $f\in\overline{AM}$。这没有把全 $H$ 的稠密像无条件搬到未知限制。

固定任意闭 $A$ 不变空间 $M$，令 $P=P_M$，定义

$$
\mathcal Z_M
=\{b\in L^\infty(\mu):[P,M_b]=0\},
\qquad
\mathcal F_M=\{E:[P,M_{\mathbf1_E}]=0\}.
\tag{6.2}
$$

这里 $\mathcal Z_M$ 是**减少** $M$ 的乘法代数；对实 $b$，因 $M_b$ 自伴，只要求 $M_bM\subseteq M$ 就已经等价于减少。

$\mathcal F_M$ 是按零测集完成的 $\sigma$-代数：补集、有限交由指标算子的代数运算得到，可数并由有界指标的强极限得到。另一方面，$\mathcal Z_M$ 为自伴代数；其任意实函数的谱指标仍与 $P$ 交换。因此

$$
\mathcal Z_M=L^\infty(\mathcal F_M,\mu).
\tag{6.3}
$$

**引理 6.1。** $\mathcal F_M$ 为 odometer 的双向 Haar 因子。

**证明。** 取 $E\in\mathcal F_M$。真实加权复合恒等式为

$$
A M_{\mathbf1_E}=M_{\mathbf1_{\tau^{-1}E}}A,
\qquad \tau(y)=y-1.
\tag{6.4}
$$

左端将 $M$ 映入 $M$，所以右端说明 $M_{\mathbf1_{\tau^{-1}E}}$ 将 $AM$ 映入 $M$。由 (6.1) 与该乘法算子的有界性，它保持整个 $M$。它自伴，故也减少 $M$，即 $\tau^{-1}E\in\mathcal F_M$。

置 $K=L^2(\mathcal F_M,\mu)$。由指标的结论，$UK\subset K$。和 R280 中相同，$U^{2^k}\to I$ 强，故对 $f\in K$，

$$
U^{-1}f=\lim_k U^{2^k-1}f\in K.
$$

因此 $K$ 减少 $U$，其指标关系也给因子的逆向稳定性。$\square$

## 7. 全部减少乘子的精确分类与有限头分裂

由 R280 §4 已给出的自含 Fourier 证明，odometer 的每个 Haar 因子由 Prüfer 群 $\mathbb Z[1/2]/\mathbb Z$ 的一个子群确定。该子群只有两类：整个群，或唯一的某个有限循环子群

$$
\Gamma_m=2^{-m}\mathbb Z/\mathbb Z,\qquad m\ge0.
$$

后一类恰为模 $2^m$ 的完整低头因子，而非任意另选的有限分割。

若 $\mathcal F_M$ 为完整 Haar 因子，则 $P$ 与全部乘法交换。按 §2 的标量交换子证明，$P=M_{\mathbf1_E}$ 为支持投影；$AM\subset M$ 和 $w>0$ 几乎处处给 $\tau^{-1}E\subset E$，保测性升级为等号，再由遍历性得 $P=0$ 或 $I$。

因此，对非零真 $M$，存在唯一有限 $m\ge0$，使

$$
\boxed{
\mathcal Z_M
=\{b:b(y)\text{ 只依赖 }y\bmod2^m\}.}
\tag{7.1}
$$

其中 $m=0$ 表示只有标量。

还能把这个有限头从原空间中精确拆出。设 $q=2^m$，按 (1.1) 分头；由 (7.1)，$P$ 与每个低头坐标投影交换，故

$$
M=\bigoplus_{r=0}^{q-1}(e_r\otimes V_r)
\tag{7.2}
$$

其中 $V_r$ 为闭尾子空间。原单步公式与 $AM\subset M$ 给

$$
c_rV_{r-1}\subseteq V_r\quad(1\le r<q),\qquad
T_mV_{q-1}\subseteq V_0.
$$

现在投影 (6.1) 到每个低头坐标。对 $r\ge1$，得到

$$
V_r=\overline{c_rV_{r-1}}=V_{r-1},
$$

因为 $c_r>0$ 且各 $V_{r-1}$ 闭。第零坐标给 $\overline{T_mV_{q-1}}=V_0$。所以存在同一个闭尾空间 $V$ 满足

$$
\boxed{
M=\mathbb C^{2^m}\otimes V,\quad
T_mV\subseteq V,\quad\overline{T_mV}=V,\quad
P=I_{2^m}\otimes P_V.}
\tag{7.3}
$$

$m=0$ 时按 $q=1$ 解释，没有非空头和 $c_r$ 链。

此外，尾投影 $P_V$ 所交换的可测尾乘法只有标量。否则一个非恒定 $b(z)$ 给原 $P$ 所交换的乘子 $b(\lfloor y/2^m\rfloor)$；这种函数同时只依赖低 $m$ 位只能为常数，与 (7.1) 矛盾。

这不是声称 $V$ 必为零或全尾空间。它是每个可能的真不变空间的准确有限头归一形，留下一个没有非平凡乘法减少结构的真实尾问题。

## 8. 无限物理位与非有限柱实乘子全部排除

**推论 8.1。** 若存在无限位集 $J\subseteq\mathbb N_0$，对每个 $j\in J$，原物理位指标 $P_j^0$ 都保持闭 $A$ 不变空间 $M$，则 $M=0$ 或 $H$。

**证明。** 各 $P_j^0$ 自伴，所以其乘子属于 $\mathcal Z_M$。若 $M$ 非零真，由 (7.1) 它们必须全是同一个有限低头的函数。但对 $j\ge m$，第 $j$ 位指标不等于任何只依赖低 $m$ 位的函数；它在每个低 $m$ 位柱中都取 $0,1$ 各半。无限 $J$ 不可能有界，矛盾。$\square$

该结论不要求 $J$ 连续、余有限或有任何正密度。

更精确地，若 $M$ 非零真且 (7.1) 的最大头为 $m$，则保持 $M$ 的物理位指标的指标集恰为 $\{0,\ldots,m-1\}$；不存在有孔的另一有限集合。因此，只要一个第 $j$ 位指标保持 $M$，整个低 $j+1$ 位的完整矩阵代数都减少 $M$，且 $M$ 可按该头精确写成完整头张量尾空间。这一结论仍允许有限头之后留下未知的真尾空间。

**推论 8.2。** 若有一个实 $b\in L^\infty(\mu)$，不等于任何有限低位柱函数，而 $M_bM\subseteq M$，则 $M=0$ 或 $H$。

到本节为止，对复 $b$ 的同一结论需要 $M_b$ 和 $M_{\bar b}$ 同时保持 $M$；不能把一般正规乘子的单向不变性无理由当作减少。§9 将利用当前系统的有限阶 Fourier 结构真正证明这个缺失步骤，从而去掉实值限制。

于是 §§1–5 的完整高尾模假设是推论 8.1 的特例。不过原有限纤维证明仍有独立范围：它只用真实全周期、正权和遍历性，不使用本节原算子专属的 $N_j\to I/2$ 与 (6.1)。

所有新增结论都要求准确的乘法稳定关系。R164 的高位强*渐近交换、任意小误差、有限头近似或 WOT 极限均不自动提供 (6.2) 中任何一个非平凡精确乘子。一般 ordinary 不变空间仍未被排除。

## 9. 单向复乘法稳定在本系统中自动为减少

定义真正的单向稳定代数

$$
\mathfrak B_M=\{b\in L^\infty(\mu):M_bM\subseteq M\}.
\tag{9.1}
$$

它显然是幺复代数。它还在 $L^\infty=L^1{}^*$ 的弱*拓扑下闭：若 $b_\alpha\to b$ 弱*，对任意 $f\in M$、$g\in M^\perp$，有 $f\bar g\in L^1$，因而

$$
\langle M_bf,g\rangle
=\lim_\alpha\langle M_{b_\alpha}f,g\rangle=0.
\tag{9.2}
$$

与 (6.4) 相同，实际协变关系和 $\overline{AM}=M$ 给

$$
b\in\mathfrak B_M\quad\Longrightarrow\quad
b\circ\tau^n\in\mathfrak B_M\quad(n\ge0).
\tag{9.3}
$$

这一推理不使用 $\bar b$ 保持 $M$。

**定理 9.1。** 对当前原 $A$ 的任意闭不变空间 $M$，$\mathfrak B_M$ 自伴；故

$$
\boxed{\mathfrak B_M=\mathcal Z_M.}
\tag{9.4}
$$

**证明。** 固定 $b\in\mathfrak B_M$。对 $\gamma\in\Gamma=\mathbb Z[1/2]/\mathbb Z$，令 $\lambda_\gamma=e^{-2\pi i\gamma}$，取 Fourier–Cesàro 平均

$$
C_N^\gamma b
=\frac1N\sum_{n=0}^{N-1}\lambda_\gamma^{-n}
(b\circ\tau^n).
\tag{9.5}
$$

每个平均属于 $\mathfrak B_M$，且

$$
\|C_N^\gamma b\|_\infty\le\|b\|_\infty.
$$

由原 Haar Fourier 正交基及每个角色不同的特征值，有限角色和上直接求几何平均，再用 $L^2$ 稠密性，得到

$$
C_N^\gamma b\longrightarrow\widehat b(\gamma)\chi_\gamma
\quad\text{于 }L^2(\mu).
\tag{9.6}
$$

一致 $L^\infty$ 界把这个收敛升级为弱*收敛：对任意 $L^1$ 测试函数先用有界函数逼近，再对有界测试函数使用 $L^2$ 收敛即可。由 (9.2)，若 $\widehat b(\gamma)\ne0$，则 $\chi_\gamma\in\mathfrak B_M$。

此时使用当前系统的关键有限阶性质。每个 $\chi_\gamma$ 都满足 $\chi_\gamma^{2^r}=1$，某个有限 $r$ 即可；故

$$
\overline{\chi_\gamma}
=\chi_\gamma^{2^r-1}\in\mathfrak B_M.
\tag{9.7}
$$

常数角色单独由幺性处理。

令 $E_k$ 为到低 $k$ 位的 Haar 条件期望。它具有准确有限 Fourier 展开

$$
E_kb=\sum_{\gamma\in\Gamma_k}
\widehat b(\gamma)\chi_\gamma.
$$

每个非零项及其共轭角色都已由 (9.6)–(9.7) 进入 $\mathfrak B_M$，因此

$$
\overline{E_kb}\in\mathfrak B_M.
$$

又有 $\|E_kb\|_\infty\le\|b\|_\infty$，以及 $E_kb\to b$ 于 $L^2$，因为有限头柱空间递增稠密。所以 $\overline{E_kb}\to\bar b$ 弱*。弱*闭性给 $\bar b\in\mathfrak B_M$。

于是 $M$ 同时在 $M_b$ 与其伴随 $M_{\bar b}$ 下不变，故减少 $M_b$。这证明 $\mathfrak B_M\subseteq\mathcal Z_M$；反向包含由定义直接成立。$\square$

**最终结构结论。** 对每个非零真闭 $A$ 不变空间 $M$，存在唯一有限 $m\ge0$，使

$$
\boxed{
\{b\in L^\infty:M_bM\subseteq M\}
=L^\infty(y\bmod2^m),
\qquad M=\mathbb C^{2^m}\otimes V.}
\tag{9.8}
$$

其中 $T_mV$ 在 $V$ 中稠密，且尾 $V$ 的任何单向稳定有界乘子都是标量：若尾 $b$ 保持 $V$，则其提升保持 $M$，由 (9.8) 及头尾独立性只能为常数。

因此，任何不等于有限低位柱函数的**复** $b\in L^\infty$，只要单向保持某个 $A$ 不变 $M$，就迫使 $M$ 平凡。证明用到的是本系统的限制稠密性和全部角色的有限阶；没有宣称任意正规算子的不变子空间都自动减少，也不能把该结论移到具有无限阶角色的其他底动态。
