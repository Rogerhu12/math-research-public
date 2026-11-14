# R143：惰性平方自由混合层的实际 CM 扭曲全部中心值消失

日期：2026-11-12。

本篇处理固定 $A:y^2=x^3-x$ 的完整水平同余曲线，特别包含 O6 剩余 $g=1$、$g=3$ 对应的水平 $p$、$3p$。结论是：加入完整三水平不能在这类曲线的 Jacobian 中产生一个中心 $L$ 值非零的商。证明同时处理非范数 Cartan 角色、一维下降角色以及模形式有 CM 时可能进一步分裂的例外。**中心值为零不等于已证明 Mordell–Weil 秩正；本篇不作后一个断言，也不把这个方法边界当作主问题完成。**

## 1. 精确结论与各个配对分支

令 $m\ge3$ 为平方自由奇整数，且每个素因子 $\ell\mid m$ 都满足 $\ell\equiv3\pmod4$。设
$$
K=\mathbb Q(i),\qquad \mathcal O=\mathbb Z[i],\qquad
C_m=(\mathcal O/m\mathcal O)^\times.
$$
对每个 Weil 配对乘子 $u\in(\mathbb Z/m\mathbb Z)^\times$，令 $X_A^u(m)$ 为参数化 $A[m]\simeq E[m]$ 且乘子为 $u$ 的光滑射影完整水平扭曲。平方倍乘子给同构曲线，但在合数水平不把所有乘子压成仅两个类别。

**定理 143.1。** 对任何正维、定义于 $\mathbb Q$ 的阿贝尔簇商
$$
\operatorname{Jac}(X_A^u(m))\twoheadrightarrow B,
$$
其完整 Hasse–Weil $L$ 函数在 $s=1$ 全纯且
$$
\boxed{L(B,1)=0.} \tag{143.1}
$$
更准确地，它的绝对不可约兼容系统因子可以取为以下两种，每个因子的酉中心根数均为 $-1$：

1. 权二新形式的一个有限阶 Dirichlet 扭曲；
2. 权二新形式与一个不可约二面体 Artin 表示的张量积，等价于 $K$ 上一个有限阶 Hecke 扭曲的基变换 $L$ 函数。

第二种张量积本身仍绝对不可约；这包括原权二新形式有 CM 的情况。因此不会仅知道一个可分裂四维因子的乘积在中心为零，却把其正根数子因子遗漏。

对 $m=3$ 曲线亏格为零，定理的正维商断言为空。对实际 O6 中的 $p>37$，R128 给 $p\equiv3\pmod4$ 及 $E[p]\simeq A[p]$；若 $3\mid g$，还有 $E[3p]\simeq A[3p]$。所以定理分别适用于 $m=p$ 与 $m=3p$，没有关于 $p\bmod3$ 的额外条件。

## 2. 用完整不连通曲线作分解，再取实际配对分支

先保留所有乘子的并
$$
\mathscr X_A(m)=\coprod_{u\in(\mathbb Z/m\mathbb Z)^\times}X_A^u(m),\qquad
\mathscr J_A(m)=\prod_u\operatorname{Jac}(X_A^u(m)). \tag{143.2}
$$
这是未规定配对的完整同余模问题。每个分支定义于 $\mathbb Q$，所以它的 Tate 模是整个乘积的实际 $G_{\mathbb Q}$ 直和项。这样处理不假定某个非几何的正规化子元素是单个分支上的甲板变换。

取标准主同余紧子群
$$
U(m)=\ker\bigl(\mathrm{GL}_2(\widehat{\mathbb Z})\longrightarrow
\mathrm{GL}_2(\mathbb Z/m\mathbb Z)\bigr).
$$
使用完整模曲线的等变 Eichler–Shimura 分解。其权二自守表示 $\pi$ 满足
$$
W_\pi=\pi_f^{U(m)}\ne0;\qquad
W_\pi=\bigotimes_{\ell\mid m}\pi_\ell^{1+\ell M_2(\mathbb Z_\ell)}.
\tag{143.3}
$$
在 $\ell\nmid m$，$\pi_\ell$ 未分歧。全体 $\pi$ 保留各系数嵌入与所需重数。

这里采用如下互相配套的规范：$V_\pi$ 的算术 Frobenius $L$ 函数是 $L(\pi,s-1/2)$；$W_\pi$ 是自守表示的有限右作用型。若某个有限 Dirichlet 角色 $b$ 的未分歧素数值是 $b(q)$，则它在导子处的单位值为 $b_\ell(a)=b(a)^{-1}$。特别 $W_\pi$ 的标量单位角色是 $\omega_{\pi,\ell}$，不是把经典 nebentypus 的单位值不取逆直接填入。

等变分解后进行 Galois 下降，给出的 Cartan 字符块如下。若 $\varphi$ 是 $W_\pi|C_m$ 中的字符，则在 $G_K$ 上出现
$$
V_\pi|G_K\otimes\alpha_\varphi,\qquad
\alpha_\varphi(\mathrm{Frob}_{\mathfrak q})
 =\varphi(\pi_{\mathfrak q}\bmod m), \tag{143.4}
$$
其中 $\mathfrak q\nmid2m$，$\pi_{\mathfrak q}$ 为 $\mathfrak q$ 的 primary 高斯生成元，满足 $\pi_{\mathfrak q}\equiv1\pmod{(1+i)^3}$。实际 Frobenius 使用算术方向。

下面把所用的全部左右作用、对偶及转置写出，以区分一般的全水平扭曲和实际的同余模问题。

写 $b=(P,Q)$ 为水平基的行向量，$r=r_A$ 由 $\sigma(b_A)=b_A r(\sigma)$ 定义。先在未扭曲完整模曲线上采用**左作用**
$$
T_g(E,b)=(E,b\,{}^tg).
$$
它确实是左作用，因为 $T_gT_h$ 把 $b$ 送到 $b\,{}^th\,{}^tg=b\,{}^t(gh)$。若将这个左作用转成上同调上的左表示，所用的是 $(T_{g^{-1}})^*$；在协变 Tate 模上则直接使用 $(T_g)_*$。二者是对偶表示，不是把同一个矩阵的逆任意省去。

还要验证这个逆拉回左作用确实是 $W_\pi$ 的有限右正则作用，包含行列式不为 $1$ 的元素。下面在所有分量上直接计算。令 $\nu\in(\mathbb Z/m\mathbb Z)^\times$，$D_\nu=\operatorname{diag}(\nu,1)$，用
$$(E_z,\nu z/m,1/m)$$
表示 Weil 分量 $\nu$ 的复点。若 $d=\det g$，比较两个水平基给
$$
T_g(z,\nu)=(\gamma z,\nu d),\qquad
\gamma=D_{\nu d}^{-1}gD_\nu\in\mathrm{SL}_2(\mathbb Z/m\mathbb Z),
$$
其中取任一 $\mathrm{SL}_2(\mathbb Z)$ 提升计算 $\gamma z$；不同提升只差 $\Gamma(m)$。在标准 adelic 商中，为分量 $\nu$ 选有限代表 $r_\nu=D_\nu^{-1}$，计算均可模 $U(m)$ 进行。右乘 $g$ 后的新分量为 $\nu/d$，而用于重新写成分量代表的矩阵是
$$
\delta=r_\nu g r_{\nu/d}^{-1}
=D_\nu^{-1}gD_{\nu/d}\in\mathrm{SL}_2(\mathbb Z/m\mathbb Z).
$$
强逼近将无限分量送到 $\delta^{-1}z$；这里
$$
\delta^{-1}=D_{\nu/d}^{-1}g^{-1}D_\nu
=\gamma_{g^{-1},\nu}.
$$
故有限 adelic 右平移在微分上的作用，恰为 $(T_{g^{-1}})^*$，连同分量 $\nu\mapsto\nu/d$ 完全一致。$r_\nu=D_\nu^{-1}$ 的反向标签不可省略；这个计算覆盖了整个 $\mathrm{GL}_2$，没有从行列式为 $1$ 的情形猜测中心作用。

在这个规范中，完整模曲线的等变 Eichler–Shimura 分解为
$$
H^1_{\mathrm{et}}[\pi]=V_\pi^\vee\otimes W_\pi,
\qquad
V_\lambda(J)[\pi]=V_\pi\otimes W_\pi^\vee.
\tag{143.4a}
$$
第一式的有限型使用上段规定的逆拉回左作用；第二式的有限型使用协变 $T_g$。这就是 Virdol (2006), §2.4–§2.6 的等变分解在此左作用下的写法：其印刷 p.95 先给出有限作用的逆，p.96 给出 ${}^t\rho_{\pi,\lambda}^{-1}$ 的 Galois 作用，再以 $H^1_{\mathrm{et}}=V_\lambda(J)^\vee$ 转到协变 Tate 模。区别必须连同有限作用一起转换。以标量 $aI$ 检查，第一式的有限型为 $\omega_{\pi,\ell}(a)$，第二式为其逆；不能只转换 Galois 因子。等变 Eichler–Shimura 的 Hecke–Frobenius 关系锁定 $V_\pi$ 的 Euler 因子为上述 $L(\pi,s-1/2)$，不再额外作 Dirichlet 扭曲。

实际模问题 $\alpha:A[m]\simeq E[m]$ 在这组基中的下降为
$$
b\longmapsto \sigma(b)r(\sigma)^{-1}
=T_{\rho(\sigma)}(\sigma(b)),\qquad
\rho(\sigma)=r(\sigma)^{-t}. \tag{143.4b}
$$
所以在 Proposition 2.2 的一般左作用下降中输入的是对偶表示 $\rho=r^{-t}$。这个扭曲的配对分量作用是
$$\chi_m(\sigma)\det\rho(\sigma)=\chi_m(\sigma)\det r(\sigma)^{-1}=1.$$
故它恰为 (143.2) 中每个配对乘子都单独定义于 $\mathbb Q$ 的实际同余曲线；不是凭 p.96 Remark 2 将任意全水平扭曲认成 Wiles 的单分支曲线。

将 (143.4b) 代入 (143.4a)，实际有限表示是 $W_\pi^\vee\circ r^{-t}$。令 $\iota(g)=g^{-t}$，则逐矩阵有
$$
W_\pi^\vee(\iota(g))={}^tW_\pi({}^tg).
$$
每个 $\mathrm{GL}_2(\mathbb F_\ell)$ 矩阵与其转置相似（例如二者有相同的有理标准形）；平方自由 CRT 给出 $\mathrm{GL}_2(\mathbb Z/m\mathbb Z)$ 上同样的结论。于是上式的字符等于 $W_\pi(g)$ 的字符，特征零半单性给
$$
\boxed{W_\pi^\vee\circ\iota\simeq W_\pi.} \tag{143.4c}
$$
这证明实际有限因子为 $W_\pi\circ r$，即 (143.4) 的正向 primary 值。此论证是在**整个 $\mathrm{GL}_2$** 上作的：对于标量 $aI$，两个逆明确抵消；对于复共轭 $n={}^tn=n^{-1}$，其 $\pm1$ 本征值不变。在 Cartan 的乘法矩阵上，$r^{-t}$ 对应 $\bar r^{-1}$，所以相应字符只是 $\varphi$ 与 $\bar\varphi$ 的交换，完整正规化子块及范数型反射标量均不改变。这里没有把仅在 $\mathrm{SL}_2$ 中成立的固定共轭关系误用于整个 $\mathrm{GL}_2$。

Virdol 的 p.96 Remark 2 明确允许任意整数水平；本文另以上述配对计算识别实际的所有分支。这里使用等变 Tate 模，而**不采用把张量积的惯性不变量写成两个不变量张量积的简式**：完整坏 Euler 因子必须由整个表示 $(V_\pi\otimes W)^{I_q}$ 计算。

R139 已独立证明 $r(G_K)=C_m$。复共轭可选为同一 CM 基上的 $n:z\mapsto\bar z$，它一次同时作用于所有 CRT 因子。因此：

- 若 $\varphi\ne\bar\varphi$，相应 $G_{\mathbb Q}$ 块是
  $$V_\pi\otimes\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\alpha_\varphi; \tag{143.5}$$
- 若 $\varphi=\bar\varphi$，它在 $W_\pi$ 中的一维字符空间由 $n$ 保持，且 $n$ 的实际标量决定它的唯一 $G_{\mathbb Q}$ 延拓。

平方自由水平下每个 Cartan 字符在 $W_\pi$ 中至多出现一次。这可逐处由有限 $\mathrm{GL}_2(\mathbb F_\ell)$ 的主系列、Steinberg、尖点表示的限制看出；§6 给出所需的完整列表。 更具体地，写 $C_\ell=\mathbb F_{\ell^2}^\times$、$Z_\ell=\mathbb F_\ell^\times$，有限型的限制分别为
$$
\operatorname{Ind}_{Z_\ell}^{C_\ell}(\mu_1\mu_2),\qquad
\operatorname{Ind}_{Z_\ell}^{C_\ell}(\mu^2)-\mu\circ N,\qquad
\operatorname{Ind}_{Z_\ell}^{C_\ell}(\xi|Z_\ell)-\xi-\xi^\ell.
\tag{143.5a}
$$
第一式也包括未分歧主系列的有限型；后二式的减号表示恰删去列出的字符。主系列由 $C_\ell$ 在射影直线上的传递性得到；尖点式在标量上的迹是 $(\ell-1)\xi(z)$、在非标量上的迹是 $-\xi(c)-\xi(c^\ell)$，故与字符表逐类相等。CRT 张量积保持这些重数为一。

## 3. 同一个全局 Hecke 角色及中心相容性

令 $\chi_\varphi$ 为 (143.4) 的有限阶 Hecke 角色：在未分歧素理想处的 Euler 因子使用
$$\chi_\varphi(\mathfrak q)=\varphi(\pi_{\mathfrak q}\bmod m).$$
它在无穷处平凡，有限导子支撑于 $2m$。以下中心关系是处处的关系，包含一致化元，而不只是单位群上的相等：
$$
\boxed{\chi_\varphi|\mathbb A_{\mathbb Q}^\times
=\omega_\pi^{-1}.} \tag{143.6}
$$

证明如下。$\varphi$ 在标量子群上的值是 $\prod_{\ell\mid m}\omega_{\pi,\ell}$，而权二及全局中心角色在 $-1$ 上平凡给
$$\varphi(-1)=\prod_{\ell\mid m}\omega_{\pi,\ell}(-1)=1.$$
对奇素数 $q\nmid m$，理想 $(q)$ 的 primary 生成元为 $q$ 或 $-q$，二者给相同 $\varphi$ 值。因此 $\chi_\varphi$ 限制到有理有限 idèle 的 $q$ 分量时，值为 $\varphi(q)$。另一方面，由全局中心角色在主 idèle $q$ 上平凡、以及 $\pi$ 在 $m$ 外未分歧，
$$\omega_{\pi,q}(q)=\left(\prod_{\ell\mid m}\omega_{\pi,\ell}(q)\right)^{-1}
=\varphi(q)^{-1}.$$
这证明两个有限阶 Hecke 角色在几乎所有有理素数处相等，故处处相等，给 (143.6)。在无穷处两者均平凡。

在 $\ell\mid m$ 处，实际 CM 好约化的局部互反给
$$
\chi_{\varphi,\ell}^{-1}|\mathcal O_{K_\ell}^\times
=\varphi_\ell. \tag{143.7}
$$
可直接用 $A$ 的 CM 形式群核对此方向：$K_\ell/\mathbb Q_\ell$ 未分歧二次，$[-\ell]$ 在特殊纤维是二次 Frobenius；形式群为 $\mathcal O_{K_\ell}$ 的 Lubin–Tate 形式群，算术互反把单位 $a$ 在 $\ell$ 挠点上送为 $a^{-1}$。其他 $m$ 挠点分量在 $\ell$ 未分歧。所以 (143.4) 的算术角色在单位上是 $\varphi_\ell^{-1}$，即 (143.7)。

这里尤其不能把 $\chi_{\varphi,\ell}$ 随意换成同单位值但一致化元值不同的角色。因为 $K_\ell/\mathbb Q_\ell$ 未分歧，
$$K_\ell^\times=\mathbb Q_\ell^\times\mathcal O_{K_\ell}^\times,$$
故 (143.6)、(143.7) 已唯一锁定整个局部角色。

## 4. 非范数字符块的全局根数

先不假设 (143.5) 不可约；其不可约性在 §8 单独证明。它的 $L$ 函数是
$$
L(\pi_K\otimes\chi_\varphi,s-1/2). \tag{143.8}
$$
对 $\ell\mid m$，$W_\pi$ 中的 $\varphi_\ell$ 向量，借 (143.6)、(143.7)，确实给完整环面上的
$$
\operatorname{Hom}_{K_\ell^\times}
(\pi_\ell,\chi_{\varphi,\ell}^{-1})\ne0. \tag{143.9}
$$
这里可以在紧商 $K_\ell^\times/\mathbb Q_\ell^\times$ 上平均得到一个非零等变线性泛函；单位向量与中心关系一起保证平均不为零。

在 $2$ 处，$K_2/\mathbb Q_2$ 分歧，但 $\pi_2$ 未分歧主系列。对任何中心相容的角色 $\Omega$，主系列限制到非分裂 $K_2^\times$ 都包含 $\Omega$：$K_2^\times$ 在 $\mathbb P^1(\mathbb Q_2)$ 上传递、稳定子为 $\mathbb Q_2^\times$，诱导模型直接给从中心角色诱导的表示。因此 (143.9) 在 $2$ 也成立。这个论证保留 $\chi_{\varphi,2}$ 的真实一致化元值，不从其单位限制猜出它。

在其他未分歧惰性素数处，球向量给同样的 Hom；在分裂素数处 $\pi$ 与 $\chi$ 均未分歧，局部基变换根数直接等于 $1$。

采用加性角色 $\psi_{K_v}=\psi_{\mathbb Q_v}\circ\operatorname{Tr}_{K_v/\mathbb Q_v}$。Saito (1993), §1 的原刊定理（包括剩余特征 $2$）给：当 $\Omega|\mathbb Q_v^\times=\omega_{\pi,v}$ 且环面 Hom 非零时，
$$
\epsilon\left(\tfrac12,\pi_{K_v}\otimes\Omega^{-1},\psi_{K_v}\right)
=\Omega(-1)=\omega_{\pi,v}(-1). \tag{143.10}
$$
取 $\Omega=\chi_{\varphi,v}^{-1}$，乘遍有限处。由于 $\omega_{\pi,\infty}(-1)=1$，有限处的乘积是 $1$。在复无穷处，权二离散系列基变换为角角色次数 $1$ 与 $-1$，两个局部常数的乘积为 $-1$。于是
$$
\boxed{\epsilon(\pi_K\otimes\chi_\varphi)=-1.} \tag{143.11}
$$

这是 $K$ 上的完整基变换根数。若改写成 $\mathbb Q$ 上的 Rankin 张量积，局部还出现二次扩张的诱导常数；其全局乘积为 $1$，不能只在某一个有限处添入或删除它。

由 (143.6) 有 $\chi_\varphi\bar\chi_\varphi=\omega_\pi^{-1}\circ N_{K/\mathbb Q}$，故这个诱导块自对偶至 Tate 扭曲。其函数方程与 (143.11) 迫中心值为零。所用自守延拓为已知的二次基变换及有限阶 Hecke 扭曲；两种无穷型不允许中心出现极点。

## 5. 范数字符必须保留实际的共轭标量

现在 $\varphi=\bar\varphi$。逐个 CRT 因子可唯一写成
$$
\varphi_\ell=\beta_\ell\circ N_{\mathbb F_{\ell^2}/\mathbb F_\ell},
\qquad \varphi=\beta\circ N, \tag{143.12}
$$
其中 $\beta:(\mathbb Z/m\mathbb Z)^\times\to\mathbb C^\times$。令 $b$ 为满足 $b(q)=\beta(q)$ 的全局有限 Dirichlet 角色。则
$$\chi_\varphi=b\circ N_{K/\mathbb Q},\qquad
\pi'=\pi\otimes b$$
有平凡中心角色。在导子处 $b_\ell|\mathbb Z_\ell^\times=\beta_\ell^{-1}$，所以 $\pi'_\ell$ 的有限型有非零的 **平凡 Cartan 固定线**。

设 $n_\ell:z\mapsto z^\ell$ 是 $\mathbb F_{\ell^2}/\mathbb F_\ell$ 的共轭，在固定的 CM 基中为 $\operatorname{diag}(1,-1)$。它在这条固定线上的标量记为 $e_\ell\in\{\pm1\}$。同一复共轭同时在各处作用，因此实际延拓是
$$
V_{\pi'}\otimes\eta,\qquad
\eta|G_K=1,\qquad
\eta(c)=s:=\prod_{\ell\mid m}e_\ell. \tag{143.13}
$$
所以 $\eta=1$ 当 $s=1$，$\eta=\chi_{-4}$ 当 $s=-1$。两个延拓不能任意选择。吸收 $b$ 的同时有限型也扭了 $\beta_\ell^{-1}\det$，故 (143.13) 已包括 $\beta(-1)$；没有额外遗漏一个二次符号。

## 6. 逐处计算固定线、反射及导子

以下 $q$ 是任意奇素数；最后只用 $q\equiv3\pmod4$。设 $\sigma$ 是 $\mathrm{GL}_2(\mathbb Q_q)$ 的不可约 generic 表示，中心角色平凡，且 $\sigma^{K(q)}$ 有非零非分裂 Cartan 固定向量。平方自由主同余层的全部可能性如下。

| $\sigma$ 的类型 | Cartan 固定线 | 反射标量 $e_q$ | 导子指数 |
|---|---:|---:|---:|
| 未分歧主系列 | 一维 | $1$ | $0$ |
| 主系列 $\mu\boxplus\mu^{-1}$，$\mu$ 驯分歧 | 一维 | $\mu(-1)$ | $2$ |
| 未分歧二次角色的 Steinberg 扭曲 | 零维 | 不出现 | $1$ |
| 分歧二次角色 $\delta$ 的 Steinberg 扭曲 | 一维 | $\delta(-1)$ | $2$ |
| 深度零超尖点，有限参数 $\xi:\mathbb F_{q^2}^\times\to\mathbb C^\times$，$\xi|\mathbb F_q^\times=1$、$\xi\ne\xi^q$ | 一维 | $-\xi(t)$，$t^q=-t\ne0$ | $2$ |

这里每一出现的行都有
$$\boxed{e_q=\epsilon(\tfrac12,\sigma,\psi_q).} \tag{143.14}$$
由于中心平凡，根数不依赖 $\psi_q$ 的缩放。

**主系列。** 有限型为从上三角群诱导的 $\bar\mu\otimes\bar\mu^{-1}$。非分裂 Cartan 在 $\mathbb P^1(\mathbb F_q)$ 上单传递，故固定线一维。把诱导函数在单位元处正规化为 $1$，$n=\operatorname{diag}(1,-1)$ 给值 $\bar\mu(-1)^{-1}=\mu(-1)$。Tate 的一维局部常数恒等式 $\epsilon(\mu)\epsilon(\mu^{-1})=\mu(-1)$ 给同一个值。未分歧时是 $1$。

**Steinberg。** 有限 $\mathrm{St}$ 是 $\mathbb C[\mathbb P^1(\mathbb F_q)]/\mathbb C$。其 Cartan 限制恰缺平凡字符，故未分歧扭曲无固定线。若 $\delta$ 分歧二次，则固定线来自 $\mathrm{St}$ 中的 Cartan 字符 $\delta\circ N$。直接对 $nC$ 取字符平均：$nc$ 的两个本征线在 $N(c)$ 为平方时有理，有限 Steinberg 的迹为 $1$；非平方时迹为 $-1$。乘上 $\delta(N(c))$ 后全部为 $1$，故 $\mathrm{St}$ 的这条字符线反射标量为 $1$；再乘 $\delta(\det n)=\delta(-1)$，得到表值。分歧扭曲的 Weil–Deligne 惯性不变量为零，局部常数是 $\epsilon(\delta)^2=\delta(-1)$。

**超尖点。** 有限尖点表示 $\tau_\xi$ 的正则半单字符为：分裂时 $0$，非分裂特征根 $z,z^q$ 时为 $-\xi(z)-\xi(z^q)$。在 $nc$ 中，$N(c)$ 为非平方的恰占一半；其特征根均为 $t\mathbb F_q^\times$ 中的 trace-zero 元素，且 $\xi|\mathbb F_q^\times=1$。因此
$$
e_q=\frac1{q^2-1}\sum_{c\in\mathbb F_{q^2}^\times}
\operatorname{tr}\tau_\xi(nc)=-\xi(t). \tag{143.15}
$$
深度零局部常数的已发表 Gauss 和公式给
$$
\epsilon(\tfrac12,\sigma,\psi_q)
=-\frac1q\sum_{z\in\mathbb F_{q^2}^\times}
\xi(z)\,\psi(\operatorname{Tr}z). \tag{143.16}
$$
把和按迹分组可直接消除求和：迹零非零项之和是 $(q-1)\xi(t)$；每个固定非零迹的和相同，记为 $S$；$\sum_z\xi(z)=0$ 给 $S=-\xi(t)$。因此 (143.16) 的内和为 $q\xi(t)$，得到 (143.14)。把 $\xi$ 换成逆角色不改变此处值，因为 $t^2\in\mathbb F_q^\times$。

有限尖点字符表与深度零公式见 Bushnell–Henniart (2006), §6.4 的 (6.4.1)、印刷 pp.157–159 的 §25.2、§25.4。具体地，取其 level-one 加性角色、$\mathcal A=M_2(\mathbb Z_q)$、$n=0$，(25.2.1) 的分母为
$$(\mathcal A:q\mathcal A)^{1/2}=q^2,$$
而 (25.4.1) 给 $\tau=-qG(\xi,\psi\circ\operatorname{Tr})$，所以恰得 (143.16) 的 $-G/q$。这一步不额外引入一个未分歧角色：有限型的延拓与一致化元作用已含于 $\sigma$；若仍用一个保持平凡中心的未分歧二次角色扭曲，它对导子指数 $2$ 的局部常数所添因子为 $\nu(q)^2=1$。从书中的 level-one 加性角色换至全局规范加性角色，在 $s=1/2$ 只乘 $\omega_\sigma(a)=1$。无穷处的 $-1$ 则在最后全局乘积单独计入，没有并进 (143.16)。

特别，$\pi'$ 的导子 $N'$ 是奇平方，而且
$$w(\pi')=-\prod_{\ell\mid m}e_\ell=-s.$$
扭以 $\chi_{-4}$ 时，所有奇坏处因导子指数为偶数而不改变根数；在 $2$ 处未分歧二主角色同扭 $\chi_{-4}$，两个局部常数的乘积为 $\chi_{-4}(-1)=-1$；无穷处权二离散系列的符号扭曲同构于自身。因此
$$w(\pi'\otimes\chi_{-4})=-w(\pi').$$
结合 (143.13)，实际选中的一维下降块总满足
$$\boxed{w(\pi'\otimes\eta)=-1.} \tag{143.17}$$

## 7. 非 CM 权二形式的不可约性

选择一个充分大的辅助系数素数 $\lambda$；这里只有有限多个 $\pi$ 和有限个 Artin 因子，所以可同时选择。若 $\pi$ 无 CM，Ribet (1985), Theorem 3.1（印刷 p.188）给出：在一个固定有限扩域上，$V_\pi$ 的 $\lambda$ 进像包含相应系数域整数环上的 $\mathrm{SL}_2$ 开子群。该定理的非 CM 假设见其 §1，精确像 $A_\lambda$ 在 §3 定义。

限制到任何进一步有限扩域，像的指数仍有限；$\mathrm{SL}_2$ 的任意有限指数子群仍绝对不可约。例如它的闭包包含上下三角幺幂子群各自的一个开子群，这两个子群不可能共同保持一条直线。因此所选 $V_\pi$ 在每个有限扩域上仍绝对不可约。这里只需要这个可任选辅助素数的版本，不从未核实的命题编号推断所有系数素数的结论。

于是 $V_\pi$ 与任何不可约有限 Artin 表示的张量积都不可约：限制到该有限表示的核，任何子模必为 $V_\pi\otimes W'$，再用 Artin 表示不可约即可。这个最后的张量论证仅用 Schur 引理与半单性。

当 $\varphi\ne\bar\varphi$，R139 的满 Cartan 像保证 $\alpha_\varphi\ne\bar\alpha_\varphi$，故 $\operatorname{Ind}_K^{\mathbb Q}\alpha_\varphi$ 不可约。于是 (143.5) 不可约，§4 的负根数作用于一个真正不可约块。

## 8. 有 CM 的权二形式：排除潜在的二次再分裂

设 $\pi$ 有 CM，CM 域为虚二次域 $F$。由于 $\pi$ 在 $2$ 未分歧，$D_F$ 为奇数且 $F\ne K$。并且 $D_F\mid N_\pi$，故存在 $q\mid m$ 在 $F$ 中分歧。记相应二次角色为 $\delta_F$。

写 $L=FK$。$V_\pi|G_K$ 由 $L/K$ 的一维代数 Hecke 角色诱导。它的两个共轭角色的比具有不同的无穷型，因而不是有限阶。由二次诱导表示的直接比较，其唯一非平凡有限自扭曲为 $\delta_F|G_K$。于是，在 $\alpha_\varphi\ne\bar\alpha_\varphi$ 时，(143.5) 若可约，必有
$$
\bar\alpha_\varphi/\alpha_\varphi=\delta_F|G_K. \tag{143.18}
$$

现在只看上面选定的 $q\mid D_F$。这里 $q\equiv3\pmod4$，$K_q/\mathbb Q_q$ 未分歧二次，$\delta=\delta_{F,q}$ 是分歧二次角色，其剩余角色为 Legendre 符号。由 (143.7)，(143.18) 在单位上迫
$$
\varphi_q^{q-1}=\delta\circ N. \tag{143.19}
$$
同时 $\pi_q\otimes\delta\simeq\pi_q$。逐类排除：

**主系列。** 自扭曲只能交换两诱导角色，故有限主系列参数为 $\gamma,\gamma\delta$。其中心在 $-1$ 上是 $\delta(-1)=-1$，所以 $\varphi_q(-1)=-1$。另一方面，取 $\mathbb F_{q^2}^\times$ 的生成元，将 $\varphi_q$ 写成指数 $a$ 的字符，(143.19) 给
$$a\equiv\frac{q+1}{2}\pmod{q+1}.$$
由于 $q\equiv3\pmod4$，$a$ 为偶数，故 $\varphi_q(-1)=1$，矛盾。

**Steinberg。** 一个 Steinberg 扭曲不能同构于其非平凡二次扭曲，故不出现。

**深度零超尖点。** 记有限尖点参数为 $\xi$。二次自扭曲给
$$\xi(\delta\circ N)=\xi^q.$$
与 (143.19) 相除，得 $\varphi_q/\xi=\gamma\circ N$。两字符在 $\mathbb F_q^\times$ 上的值都是有限型的中心角色，所以 $\gamma^2=1$。因此
$$\varphi_q\in\{\xi,\xi(\delta\circ N)\}=\{\xi,\xi^q\}.$$
然而有限尖点表示在非分裂 Cartan 上恰缺少这两个字符，矛盾。

三类涵盖具有 $K(q)$ 不变量的所有 generic 表示，故 (143.18) 不可能。于是 CM 情形的 (143.5) 也绝对不可约。范数型分支已在 §5–§6 化为权二新形式的扭曲，本来就是二维不可约表示，无需再排除什么四维分裂。

## 9. 从所有块回到每个实际商

§4、§6 给每一个实际块根数 $-1$，§7–§8 保证未把可分裂块的乘积误当作不可约因子。它们的 $L$ 函数均全纯于中心，故均在那里为零。

Tate 模半单性说明任何正维 $\mathbb Q$ 商的 Tate 模包含这些绝对不可约块中的至少一个，并且不含该列表以外的块。完整模曲线的等变分解及局部–全局相容性保证其 $L$ 函数等于相应完整因子的乘积。因此 (143.1) 成立。由 (143.2)，结论对每一个 Weil 乘子分支成立，而不仅对所有分支的总乘积成立。

本定理关闭的是特定的**中心值非零商构造**：无论增加完整三水平，还是增加任意平方自由、全惰性的固定组合，都不能在 $\mathscr J_A(m)$ 中找到一个 $L(B,1)\ne0$ 的正维商。它不排除在中心消失时仍有 Mordell–Weil 有限的特殊商；若要从消失进一步断言正秩，需要额外的算术定理。本篇亦未限制 $E$ 的分母大小，没有排除 O6 的 $g=1,g=3$ 或变化大素数分支。

## 10. 已发表输入与核对位置

- C. Virdol, *Zeta functions of twisted modular curves*, J. Aust. Math. Soc. **80** (2006), 89–103：[原刊](https://www.austms.org.au/Publ/JAustMS/V80P1/pdf/t56.pdf)。§2.4–§2.6、Propositions 2.2–2.3、p.96 Remark 2。使用等变 Tate 分解和任意整数水平的下降；坏 Euler 因子按整个张量积取惯性不变量。
- H. Saito, *On Tunnell's formula for characters of GL(2)*, Compositio Math. **85** (1993), 99–108：[原刊](https://www.numdam.org/item/CM_1993__85_1_99_0.pdf)。p.99, §1 未编号 Theorem，采用 $\psi_L=\psi_F\circ\operatorname{Tr}$，正文明确包括剩余特征 $2$。
- C. J. Bushnell and G. Henniart, *The Local Langlands Conjecture for GL(2)*, Grundlehren **335**, Springer (2006)，[DOI](https://doi.org/10.1007/3-540-31511-X)：§6.4 的有限尖点字符表、§25.2 和 §25.4 的深度零局部常数公式。本文 §6 独立完成反射平均及所需 Gauss 和的求值。
- K. A. Ribet, *On $l$-adic representations attached to modular forms. II*, Glasgow Math. J. **27** (1985), 185–194：[作者保存的原刊扫描](https://math.berkeley.edu/~ribet/Articles/rankin.pdf)。§1 的非 CM 假设、§3 Theorem 3.1（印刷 p.188）的充分大系数素数的大像定理；§7 已说明它如何给本文所需的强不可约性。§8 的局部缺失角色排除为本篇直接证明。
- [R139](R139-all-odd-cm-images-and-exact-cusp-orbits.md)：固定 $A$ 的满 Cartan 像与一次同时复共轭；[R128](R128-all-odd-congruence-depth-and-split-prime-power-exclusion.md)：实际 $p$、$3p$ 同余接口。

Studnia 的博士论文 §5.3–§5.4 可作素数水平结果的比较，未作为本篇混合层定理的前提。这里也没有借用其 submitted 文稿中关于 Jacobian 商的未发表断言。
