# R37：第三类积分互易式给出的原始提升与 CM 反对称高度非零

**可信度：已证明。** 日期：2026-11-12。

本结果使用已发表的 $p$-adic analytic subgroup theorem（下称 AST）、
Coleman–Gross 高度及其积分比较，不使用新的 rank-two BSD 预印本，
也不假设 Sha 有限。

固定
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad
P=(-1,4),\quad Q=(9,24),\quad \omega=\frac{dx}{2y}.
$$
R4 已证 $E(\mathbb Q)$ 的秩为 $2$，且 $P,Q$ 独立。
目标素数仍为 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$。

## 1. 结论和它没有给出的结论

令 $G=E^\natural$ 为 universal vectorial extension。
用第三类微分
$$
\eta_R=\frac{y+y(R)}{x-x(R)}\omega
\tag{1}
$$
表示 $R\ne O$、$y(R)\ne0$ 的代数提升 $g_R\in G(\overline{\mathbb Q})$。
在固定代数的 de Rham 基 $\omega,\beta$ 中写
$$
\Psi_p(\eta_R)=a_{R,p}\omega+\ell_{R,p}\beta,
\qquad \ell_{R,p}=\log_E(R).
\tag{2}
$$
其中 $\beta$ 是 $x\omega$ 的一个固定非零有理倍数，
使商空间坐标与 $\omega$ 给出的椭圆对数一致。

**定理。** 对每一个目标 $p$：

1. 两个指定提升满足
   $$
   D_p^\natural:=a_{P,p}\ell_{Q,p}-a_{Q,p}\ell_{P,p}\ne0.
   \tag{3}
   $$
   同样结论适用于 $P,Q$ 的任意代数提升。
   因而它们在 $G(\mathbb Q_p)$ 中生成子群的 $p$-adic 闭包维数为 $2$
   （提升定义在有限扩域时取相应局部域中的 $\mathbb Q_p$-线性对数秩）。
2. 令 $h_{\mathfrak p}$ 为只在 $\mathfrak p\mid p$ 分歧的标准 CM 高度，
   用 ordinary unit-root 补空间，令
   $$
   h^-=h_{\mathfrak p}-h_{\bar{\mathfrak p}},
   \qquad j_p=h^-([i]P,Q).
   $$
   则
   $$
   j_p\ne0.
   \tag{4}
   $$
3. $h^-$ 在 $E(K)\otimes\mathbb Q_p$ 上非退化；在基
   $P,Q,[i]P,[i]Q$ 中其行列式为 $j_p^4$。

这里的高度可整体改乘一个固定非零规范化因子；非零和非退化结论不变。
本结果没有证明 cyclotomic 高度的 $2\times2$ 行列式非零，
没有证明 strict Mordell–Weil 核向量的自高度非零，
也没有给出整个 Selmer 空间的维数上界。

与早先工作笔记相比，(3) 是一个实质加强：
仅对 $G^2$ 使用 AST 确实不能把线性独立直接升级成行列式非零；
下面引入一个固定广义 Jacobian，并用高度互易式把这个**特定**行列式
重新写成线性 period。抽象的“线性独立仍可有零行列式”例子
不再是 (3) 的实际障碍。

## 2. 已证外部输入和两个必要接口

### 2.1 AST

Fuchs–Pham，*The $p$-adic analytic subgroup theorem revisited*，
$p$-Adic Numbers, Ultrametric Analysis and Applications **7** (2015), 143–156，
Theorem 2.2；
[原文](https://arxiv.org/pdf/1502.00768)，
[DOI](https://doi.org/10.1134/S2070046615020065)。

其形式为：若交换代数群 $A/\overline{\mathbb Q}$ 的代数点
$z\in A(\mathbb C_p)_f$ 具有非零对数，且该对数位于一个
$\overline{\mathbb Q}$-定义的 Lie 子空间 $V$，
则存在正维代数子群 $H$，使 $z\in H$ 且 $\operatorname{Lie}H\subset V$。
定理没有 semi-abelian 限制。

### 2.2 Coleman 积分与代数群对数是同一接口

Zarhin，*P-adic abelian integrals and commutative Lie groups*，
[arXiv:alg-geom/9603006v4](https://arxiv.org/pdf/alg-geom/9603006)，
§3，第8–9页，给出固定极点集合的 semi-abelian Albanese：
第三类微分是其 invariant differential 的 pullback。

这里还须确认使用的是高度中的 Coleman 积分。
Besser，*The $p$-adic height pairings of Coleman–Gross and of Nekovář*，
CRM Proceedings & Lecture Notes **36** (2004), 13–25，
[原文](https://arxiv.org/pdf/math/0209006)，§2，
Proposition 2.3 和 Corollary 2.4，明确给出：积分与代数映射相容，且
$$
\int_0^z\theta=\theta_0(\log_A z)
\tag{5}
$$
对交换代数群的 invariant differential $\theta$ 成立。
紧前段说明所用积分在好约化曲线上与 Coleman 积分一致。
因此本结果用 (5) 来识别高度的第三类积分，
不是仅由两套积分都满足一个局部微分方程就假定它们相等。

### 2.3 Lie 识别是固定代数识别

Coleman，*Vectorial extensions of Jacobians*，AIF **40** (1990), 769–783，
[原文](https://www.numdam.org/article/AIF_1990__40_4_769_0.pdf)，§1–§2，
把 $G$ 解释为度零线丛加连接的模空间，
其代数点是第三类微分模 $d\log$ 有理函数。

在平凡线丛和平凡连接处，以双数 $\varepsilon^2=0$ 作一阶变形。
局部过渡函数和连接分别写成
$$
1+\varepsilon f_{ab},\qquad d+\varepsilon\alpha_a.
$$
相容条件为 $\alpha_b-\alpha_a=df_{ab}$；换局部平凡化给出
de Rham Čech coboundary。
所以切空间就是代数定义的 $H^1_{\mathrm{dR}}(E)$。
向量核对应全纯微分，忘去连接对应投影到 $H^1(E,\mathcal O_E)$。
这个识别在 $K$ 上定义，不包含任何 $p$-adic period 的换基系数。

Coleman–Gross 的 $\Psi_p$ 正是这个识别后的群对数；
参见 Besser，*p-adic heights and Vologodsky integration*，
[原文](https://arxiv.org/pdf/1711.06957)，导言及 Theorem 3.7。
因此 (2) 的 $a_{R,p}$ 是代数 Lie 基下的真实对数坐标。

### 2.4 高度性质

我们使用 Coleman–Gross 高度的以下已证性质：
全局和下降到 $E$；一维 isotropic 补空间给对称配对；
分歧位的局部项是正规化第三类微分的积分；
未分歧位的局部项是该字符在 uniformizer 的值乘有理交数。

可核的统一表述见 Bianchi–Kaya–Müller，
*Algorithms for p-adic Heights on Hyperelliptic Curves of Arbitrary Reduction*，
ANTS XVI (2024)，[原文](https://antsmath.org/ANTSXVI/papers/BianchiKayaMuller.pdf)，
§2，尤其式 (2.2) 及其后的定义。
这里“未分歧”包括位于 $p$ 上方但局部字符未分歧的位；
因此下面的 $\bar{\mathfrak p}$ 处不能误用一个斜率为零的分歧积分公式。
关于 ordinary unit-root 选择与 Mazur–Tate 高度的比较，见
Balakrishnan–Besser，
[arXiv:1201.6016v2](https://arxiv.org/pdf/1201.6016)，
Assumption 2.2、Corollaries 4.2–4.3。

## 3. 广义 Jacobian 的对数非零引理

设 $T_1,\ldots,T_m\in E(K)$ 在 $\mathbb Z$ 上独立，
取 reduced modulus
$$
\mathfrak m=(O)+(T_1)+\cdots+(T_m)
$$
及广义 Jacobian
$$
0\longrightarrow\mathbb G_m^m\longrightarrow J_{\mathfrak m}
\xrightarrow{\operatorname{pr}}E\longrightarrow0.
\tag{6}
$$
其 $m$ 个 torus 特征所给扩张类为 $T_1,\ldots,T_m$
（同时取相反符号也不影响证明）。
故
$$
\operatorname{Hom}(J_{\mathfrak m},\mathbb G_m)=0.
\tag{7}
$$
确实，特征 $(n_1,\ldots,n_m)$ 延拓到整个群的必要充分条件是
$\sum n_iT_i=0$，即相应 pushout 扩张分裂。
独立性迫使特征为零；从 $E$ 到 $\mathbb G_m$ 也没有非零同态。
半阿贝尔群到 $\mathbb G_a$ 没有非零同态，因此
$J_{\mathfrak m}^2$ 没有非零连通 affine 商。

若两个代数点 $b_1,b_2\in J_{\mathfrak m}(\overline{\mathbb Q})$
的像 $R_1,R_2\in E(\overline{\mathbb Q})$
在 $\operatorname{End}^0(E)$ 上独立，则 $(b_1,b_2)$ 的代数群包
是整个 $J_{\mathfrak m}^2$。
证明：其恒等分支 $H$ 的像满射 $E^2$，否则会给 $R_1,R_2$
一个非零 endomorphism 关系。
于是 $J_{\mathfrak m}^2/H$ 被 torus 核满射，因而 affine；
由 (7) 只能为零。

### 3.1 对数分支与紧性，不省略小素数处的问题

设局部域 $L$ 包含全部定义数据，并选定一个代数 uniformizer
$\varpi$ 的对数分支，使 $\log(\varpi)=0$。
任意 $b\in J_{\mathfrak m}(\overline{\mathbb Q})$
在某个有限局部扩域中都有如下修正：存在正整数 $N$ 和
$$
t=(\varpi^{r_1},\ldots,\varpi^{r_m})\in\mathbb G_m^m(\overline{\mathbb Q}),
\qquad r_i\in\mathbb Q,
$$
使 $Nb-t\in J_{\mathfrak m}(\mathbb C_p)_f$，且
$$
\log(Nb-t)=N\log b.
\tag{8}
$$

取一个紧开子群 $U$；其在紧群 $E(L)$ 中的像是开子群。
故某个 $N\operatorname{pr}(b)$ 有提升 $u\in U$，
并有 $Nb-u\in\mathbb G_m^m(L)$。
选择 $r_i$ 抵消各坐标的赋值，
则 $Nb-t$ 是 $u$ 与一个 torus 单位的和，属于紧子群。
$\varpi^{r_i}$ 是代数数；换所选根只乘根单位，不改变对数。
最后 $\log(t)=0$，故 (8) 成立。
这个证明只用紧开群和 torus 赋值；
也与 Zarhin 原文 §1 对扩展对数分支的构造相同。

对两个点同时取一个 $N$。
修正后投影为 $NR_1,NR_2$，仍然独立，群包仍为全群。
所以 AST 推出：
$$
\boxed{\ L\bigl(\log b_1,\log b_2\bigr)\ne0
\quad\text{对每个非零代数 Lie 线性形式 }L.\ }
\tag{9}
$$
这里先把 (8) 后的紧代数点用于 AST，再除以 $N$。
不能对未进入 $J(\mathbb C_p)_f$ 的任意扩展分支对数直接略过这一步。

在有限多个素数外，固定点本已在固定整数模型中，
此修正不需要进行；于是这一论证也保留了固定有限 period 对象的解释。

## 4. 远离 p 的高度项可以吸收入固定 torus 提升

取固定的
$$
R=2P+2Q,\qquad B_P=(R+P)-(R),\quad B_Q=(R+Q)-(R).
\tag{10}
$$
它们分别线性等价于 $(P)-(O)$、$(Q)-(O)$，
支集不含 $O,P,Q,[i]P,[i]Q$。
对后三个非有理点不相等可用复共轭；其他相等会给出 $P,Q$ 的有理关系。

对 (6) 中的每个 $T_i$，以 $\eta_{T_i}$ 为第三类微分，
并令 $\theta_i$ 是其在 $J_{\mathfrak m}$ 上的 invariant differential。
与 $\omega^{\mathrm{inv}}$ 合在一起，它们构成一组代数基。
我们按留数选 torus 坐标，使
$$
\theta_i|_{\mathbb G_m^m}=d\log u_i,
\qquad \omega^{\mathrm{inv}}|_{\mathbb G_m^m}=0.
\tag{11}
$$
令 $b_j=[B_j]_{\mathfrak m}$，则
$$
I_{ij,p}:=\int_{B_j}\eta_{T_i}
=\theta_i(\log b_j),
\qquad \omega^{\mathrm{inv}}(\log b_j)=\ell_{j,p}.
\tag{12}
$$

所有远离分歧位的高度项之和都形如
$$
C_{ij,p}=\sum_\mathfrak q c_{ij,\mathfrak q}
\log(\alpha_\mathfrak q),
\qquad c_{ij,\mathfrak q}\in\mathbb Q,
\tag{13}
$$
其中只有有限多个项非零。
在 $\mathbb Q$ 情形 $\alpha_q=q$；在 $K=\mathbb Q(i)$ 情形
$\alpha_\mathfrak q$ 选为相应素理想的一个生成元。
符号吸收入 $c_{ij,\mathfrak q}$。
由于所有曲线和除子固定，除有限多个 $p$ 外，
这里的有限集合、生成元和有理交数全部固定。

选代数数
$$
u_{ij,p}=\prod_\mathfrak q\alpha_\mathfrak q^{c_{ij,\mathfrak q}}
$$
并将 $b_j$ 加上 torus 点 $(u_{ij,p})_i$，得到 $b'_j$。
选取的根仅使点改变一个 torus 挠点，对数不变。
由 (11)–(13)，
$$
\mathcal B_{ij,p}:=I_{ij,p}+C_{ij,p}
=\theta_i(\log b'_j),
\qquad \operatorname{pr}(b'_j)=j.
\tag{14}
$$
因此 $\mathcal B_{ij,p}$ 不是泛指“对数的表达式”，
而是一个实际代数提升的准确线性对数坐标。
在固定有限集外这些 $b'_j$ 也能一次固定。
若小素数处不紧，使用 §3.1，不改变 (14) 所需的非零结论。

## 5. 原始 universal-extension 行列式非零

在 $\mathbb Q$ 上取标准 cyclotomic 全局 log，
在 $p$ 处取 $W=\mathbb Q_p\beta$。
其正规化微分为
$$
\eta_i-a_{i,p}\omega.
$$
令 $H_{ij,p}$ 为全局高度在 $P,Q$ 上的矩阵。
定义和 (12)–(14) 给出
$$
H_{ij,p}=\mathcal B_{ij,p}-a_{i,p}\ell_{j,p}.
\tag{15}
$$
因高度对称，
$$
D_p^\natural=\mathcal B_{PQ,p}-\mathcal B_{QP,p}.
\tag{16}
$$

现在令 $\mathfrak m=O+P+Q$。
$P,Q$ 在 $\mathbb Z$ 上独立；它们也在 $\mathbb Q(i)$ 上独立：
将一个 CM 关系与其复共轭相加、相减即可归约到 R4 的有理独立性。
因此 §3 适用于 $(b'_P,b'_Q)$。
(16) 右端对应于 $J_{\mathfrak m}^2$ 上的代数 Lie 线性形式
$$
L(z_1,z_2)=\theta_P(z_2)-\theta_Q(z_1).
\tag{17}
$$
其在 torus 上的限制非零，所以 $L\ne0$。
由 (9)，(16) 非零，证明 (3)。

若改用任意代数提升，则相应微分代表可写成
$\eta_P+c_P\omega$、$\eta_Q+c_Q\omega$，其中 $c_P,c_Q$ 为代数数。
行列式变为
$$
D_p^\natural+c_P\ell_{Q,p}-c_Q\ell_{P,p}.
$$
这只是给 (17) 加上
$c_P\omega^{\mathrm{inv}}(z_2)-c_Q\omega^{\mathrm{inv}}(z_1)$。
它在 torus 上仍与 (17) 相同，故仍是非零代数线性形式。
再次由 (9) 得非零。

群对数在足够小的开子群上是局部解析同构；
两列非零行列式使它们的 $\mathbb Q_p$-线性张成二维。
取整数倍后，其 $\mathbb Z_p$-张成是闭包的一个开子群，
所以闭包维数也为 $2$。

## 6. 单 π 全局字符、CM 对称性及两点高度线性化

### 6.1 不遗漏另一个 p 进位

固定 $\mathfrak p=(\pi)$ 以及 $\iota_\mathfrak p:K\hookrightarrow\mathbb Q_p$。
因 $K$ 的类数为 $1$，对每个有限素理想
$\mathfrak q$ 选生成元 $\alpha_\mathfrak q$，并取 $\alpha_\mathfrak p=\pi$。
定义单 $\mathfrak p$ 的全局 log：
$$
\begin{aligned}
\chi_{\mathfrak p,\mathfrak p}(x)
&=\log_p\iota_\mathfrak p(x)
-v_\mathfrak p(x)\log_p\iota_\mathfrak p(\pi),\\
\chi_{\mathfrak p,\mathfrak q}(x)
&=-v_\mathfrak q(x)\log_p\iota_\mathfrak p(\alpha_\mathfrak q)
\qquad(\mathfrak q\ne\mathfrak p).
\end{aligned}
\tag{18}
$$
主 idèle 的各项相消，因为 $\mathcal O_K^\times=\mu_4$ 的对数为零。
因此 (18) 确实下降到 idèle class group。
它在 $\mathfrak p$ 的单位上是标准对数，所用分支满足 $\log(\pi)=0$；
在 $\bar{\mathfrak p}$ 未分歧，其局部项按交数定义。
这正是 §4 中 (13) 的来源。

在 $\mathfrak p$ 的 ordinary unit-root 补空间为 $\mathbb Q_p[x\omega]$。
因为
$$
[i]^*\omega=i\omega,\qquad [i]^*(x\omega)=-i(x\omega),
\tag{19}
$$
该补空间在 $[i]^*$ 下稳定。
高度因而满足
$$
h_{\mathfrak p}([i]U,[i]V)=h_{\mathfrak p}(U,V).
\tag{20}
$$
此处无需另引用一个未核的 CM 配对定理：
正规化微分在曲线自同构下 pullback，
分歧积分由变量替换不变，未分歧交数也由自同构不变，故 (20) 直接成立。
结合对称性、双线性和 $[i]^2=[-1]$，得到
$$
h_{\mathfrak p}([i]P,Q)=-h_{\mathfrak p}([i]Q,P).
\tag{21}
$$

### 6.2 关键的精确代数恒等式

由 (1) 直接代入 $[i](x,y)=(-x,iy)$ 得
$$
[i]^*\eta_{[i]R}=\eta_R.
\tag{22}
$$
$\Psi$ 的 functoriality、(19) 和 (22) 因而给出
$$
a_{[i]R,p}=-i\,a_{R,p},
\qquad \ell_{[i]R,p}=i\,\ell_{R,p}.
\tag{23}
$$

这里取
$$
\mathfrak m=O+P+Q+[i]P+[i]Q,
$$
仍使用 (10) 的两个列除子。
对行 $P,Q,[i]P,[i]Q$ 定义 (14) 的矩阵元素，
并用单 $\mathfrak p$ 字符计算远离 $\mathfrak p$ 的项。
由同一个正规化公式，有
$$
\begin{aligned}
h_{\mathfrak p}([i]P,Q)
&=\mathcal B_{[i]P,Q,p}+i a_{P,p}\ell_{Q,p},\\
h_{\mathfrak p}([i]Q,P)
&=\mathcal B_{[i]Q,P,p}+i a_{Q,p}\ell_{P,p}.
\end{aligned}
$$
单 $\mathfrak p$ 高度在 $P,Q$ 上的对称性同样给
$\mathcal B_{PQ,p}-\mathcal B_{QP,p}=D_p^\natural$。
相减并用 (21)，得到准确的线性 period 恒等式
$$
\boxed{
2h_{\mathfrak p}([i]P,Q)
=\mathcal B_{[i]P,Q,p}-\mathcal B_{[i]Q,P,p}
+i\mathcal B_{PQ,p}-i\mathcal B_{QP,p}.
}
\tag{24}
$$
正规化中的对数乘积不是被忽略，而是经互易式全部转成右端的线性项。

$P,Q,[i]P,[i]Q$ 在 $\mathbb Z$ 上独立，仍由 R4 和复共轭得出。
所以这个 $J_{\mathfrak m}$ 满足 §3，
并且两列投影 $P,Q$ 的 CM 独立性使群包满。
(24) 右边是
$$
\theta_{[i]P}(z_2)-\theta_{[i]Q}(z_1)
+i\theta_P(z_2)-i\theta_Q(z_1)
\tag{25}
$$
在 $(\log b'_P,\log b'_Q)$ 的值。
四个不同留数向量保证 (25) 是非零代数 Lie 线性形式。
由 (9)，(24) 非零。

定义 $h_{\bar{\mathfrak p}}(U,V)=h_{\mathfrak p}(\bar U,\bar V)$。
因 $\bar P=P,\bar Q=Q,\overline{[i]P}=-[i]P$，
$$
j_p=2h_{\mathfrak p}([i]P,Q)\ne0.
\tag{26}
$$
这证明了 (4)，无须把不可取的 Bertrand 原章 Corollary 3 当作黑箱。

## 7. 反对称方向在整个 Mordell–Weil 空间的矩阵

复共轭的 $+1$ 子空间是 $E(\mathbb Q)\otimes\mathbb Q_p$；
乘 $[i]$ 把它同构到 $-1$ 子空间。
故 $P,Q,[i]P,[i]Q$ 是 $E(K)\otimes\mathbb Q_p$ 的基。

$h^-$ 在两个同号子空间上的限制为零。
(20) 又给 $h^-(R,[i]R)=0$，以及
$h^-(P,[i]Q)=-j_p$、$h^-(Q,[i]P)=j_p$。
因此上述基中的矩阵为
$$
\begin{pmatrix}
0&0&0&-j_p\\
0&0&j_p&0\\
0&j_p&0&0\\
-j_p&0&0&0
\end{pmatrix},
\qquad\det=j_p^4\ne0.
\tag{27}
$$
这是 Mordell–Weil 配对的非退化性，确实比单点高度非零更强。

## 8. 与待解决的 Selmer 命题之间仍有哪一步

式 (27) 只控制 Kummer 像
$E(K)\otimes\mathbb Q_p$。
整个 Bloch–Kato Selmer 空间仍有正合列
$$
0\longrightarrow E(K)\otimes\mathbb Q_p
\longrightarrow H_f^1(K,V_pE)
\longrightarrow V_p\Sha(E/K)\longrightarrow0.
\tag{28}
$$
尚未证明最后一项为零。
一个已知子空间上的非退化配对允许更大空间中存在非零正交补，
所以 (27) 没有给整个空间的维数上界。
特别地，不能先用需要 $V_p\Sha=0$ 的 leading-term 公式，
再用 $j_p\ne0$ 反推该前提。

同样，cyclotomic 矩阵仍为
$H=\mathcal B-\mathbf a\boldsymbol\ell^t$，其行列式
$$
\det H=\det\mathcal B
-\boldsymbol\ell^t\operatorname{adj}(\mathcal B)\mathbf a
$$
保留真正的高次 period 项；
strict 自高度
$\boldsymbol\ell^t\operatorname{adj}(H)\boldsymbol\ell$
也未由 (24) 消去。
本结果没有推出 $G_p(p)\ne0$、$G_p\notin(p,T)^2$
或主课题的无穷素数 Sha 有限性。

### 文献核查记录

Calonge Fabregat，
[arXiv:2611.09192v1](https://arxiv.org/pdf/2611.09192)，§2.3，
确实把 $j_p=2h_{\mathfrak p}([i]P,Q)\ne0$
引为 Bertrand (1984), Corollary 3；该章 DOI 为
[10.1007/BFb0099438](https://doi.org/10.1007/BFb0099438)。
本轮只取到该章前两页的合法 preview，没有亲读 Corollary 3，
故没有宣称核实其全部原始假设。
本结果 §2–§7 独立证明本曲线所需的断言，
不依赖该新预印本中的引用或其 BSD 推导。
