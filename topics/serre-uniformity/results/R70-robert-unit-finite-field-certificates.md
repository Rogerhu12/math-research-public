# R70：Robert 单位的有限域实算与一阶导数退化证书

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的有限域公式及完成的精确计算；主目标仍未解决。**
对 $A:y^2=x^3-x$，证明其 CM 导子和模 $p$ 除法域为
$$
\mathfrak f_A=(1+i)^3,\qquad
T=K(A[p])=K(\mathfrak f_Ap),\qquad K=\mathbb Q(i),
$$
并把 R65 基 Robert 单位在候选素数的局部值化为
$\mathbb F_{q^2}$ 中 $p^2-1$ 次除法多项式求值。

实际计算 $p=43$ 得到
$$
\operatorname{loc}_{(859)}\kappa_0\ne0,\qquad
\operatorname{loc}_{(1031)}\kappa_0\ne0,\qquad
\operatorname{loc}_{(49019)}\kappa_0=0.
\tag{70.1}
$$
所以 R65 的一阶导数退化确实发生。这些结论由整系数模运算和完整
$1848$ 项求和给出，不是浮点近似，也没有构造次数 $3696$ 的数域。
下文保留全部基选择；坐标值依赖这些选择，零／非零是所用不变量。

## 1. 精确导子和 Artin 取向

置 $\mathcal O_K=\mathbb Z[i]$、$\pi=1+i$。CM 自同构取
$$[i](x,y)=(-x,iy).$$
对微分 $\omega=dx/(2y)$，有 $[i]^*\omega=i\omega$。

### 1.1 在 $K$ 上有理的全部 $\pi^3$ 挠点

令
$$P_2=(i,1-i).$$
直接用椭圆曲线加法得到
$$
P_2\xmapsto{[1+i]}(1,0)
\xmapsto{[1+i]}(0,0)
\xmapsto{[1+i]}O.
\tag{70.2}
$$
所以 $\operatorname{ann}_{\mathcal O_K}(P_2)=(\pi^3)$。
它生成的 $\mathcal O_K$ 模恰有八个点，即全部 $A[\pi^3]$。
明确地，这些点为
$$O, (0,0), (1,0), (-1,0), \pm P_2, \pm[i]P_2.$$
全部属于 $A(K)$。

### 1.2 Frobenius 的 primary 生成元

对每个不除 $2$ 的理想 $\mathfrak a$，存在唯一生成元
$\alpha_{\mathfrak a}$ 满足
$$
\mathfrak a=(\alpha_{\mathfrak a}),\qquad
\alpha_{\mathfrak a}\equiv1\pmod{\pi^3}.
\tag{70.3}
$$
理由是 $K$ 的类数为一，而四个单位到
$(\mathcal O_K/\pi^3)^\times$ 的映射为同构。
乘积仍满足 (70.3)，所以 $\mathfrak a\mapsto\alpha_{\mathfrak a}$
为理想上的乘法特征。

它正是当前模型的 CM Hecke 特征，以下说明取向。
若有理素数 $\ell\equiv1\bmod4$，在 $\mathfrak l\mid\ell$
约化后，$[i]$ 已定义于 $\mathbb F_\ell$，故
$\ell$ 次幂 Frobenius 与 $[i]$ 交换。椭圆曲线约化的
endomorphism algebra 中 $\mathbb Q(i)$ 的中心化子仍为
$\mathbb Q(i)$：在二次域情形如此，在四元数情形也如此。
Frobenius 因而是某个 $\alpha\in\mathbb Z[i]$，其范数为 $\ell$。
其微分为零，而 $[\alpha]^*\omega=\alpha\omega$，所以
$\alpha\in\mathfrak l$，从而 $(\alpha)=\mathfrak l$。
(70.2) 的挠点在良约化下保持互异，Frobenius 固定它们，
故 $\alpha\equiv1\bmod\pi^3$。这确定 $\alpha=\alpha_{\mathfrak l}$。

若 $\ell\equiv3\bmod4$，点数的二次特征和在 $x\mapsto-x$
下反号，故 $a_\ell(A)=0$。Frobenius 方程给
$\operatorname{Frob}_\ell^2=[-\ell]$，且
$-\ell\equiv1\bmod\pi^3$。因此在剩余度二的素理想
$(\ell)$ 上，Frobenius 同样等于 (70.3) 的生成元。

于是采用**算术 Frobenius** 的 Artin 约定时，
$$
\rho_p(\operatorname{Artin}(\mathfrak a))
=\alpha_{\mathfrak a}\bmod p.
\tag{70.4}
$$
这里不是它的逆。等式先在所有良素理想成立，再乘法延拓。
这也证明 Hecke 特征的导子整除 $\pi^3$；它不能整除 $\pi^2$，
因为 $-1\equiv1\bmod\pi^2$，而无穷型一会要求
$\psi((-1))=-1$，与单位理想的值为一矛盾。因此
$$\boxed{\mathfrak f_A=\pi^3.} \tag{70.5}$$

### 1.3 除法域恰为完整射线类域

令 $p>37$、$p\equiv3\bmod4$，并置
$\mathfrak m=\pi^3p$。由于所有 CM 自同态都定义于 $K$，
$\rho_p|_{G_K}$ 为取值于
$\mathbb F_{p^2}^\times$ 的一维特征。
(70.4) 说明它由
$$
\operatorname{Cl}_{\mathfrak m}(K)
\longrightarrow\mathbb F_{p^2}^\times,\qquad
[\mathfrak a]\longmapsto\alpha_{\mathfrak a}\bmod p
\tag{70.6}
$$
给出。此映射是同构：核的 primary 生成元同时模 $\pi^3,p$
为一，即是射线主理想；任意非零模 $p$ 元素都能用 CRT
提升为模 $\pi^3$ 为一的生成元。
同样，射线类数公式直接给
$$
\#\operatorname{Cl}_{\mathfrak m}(K)
=\frac{\varphi(\pi^3)\varphi(p)}4=p^2-1.
$$
由 Frobenius 的相等和类域论，
$$\boxed{T=K(A[p])=K(\pi^3p).} \tag{70.7}$$
这与 R60 的 $T=\mathbb Q(A[p])$ 相同。

导子也不能在 $2$ 处缩短：用 CRT 取
$\beta\equiv-1\bmod\pi^3$、$\beta\equiv1\bmod p$。
它模 $\pi^2p$ 为一，但其 primary 生成元为 $-\beta$，
在 (70.6) 下的像是 $-1\ne1$。在 $p$ 处亦不可删去该因子，
因为 (70.6) 的像非平凡，而 $K(\pi^3)=K$。
因此 $\operatorname{cond}(T/K)$ 恰为 $\pi^3p$。

## 2. Robert 函数与 $\psi_{11}$ 的准确关系

取 $A(\mathbb C)=\mathbb C/L$，微分为 $dx/(2y)$，故
$$x=\wp_L(z),\qquad y=\wp'_L(z)/2,\qquad\Delta(L)=\Delta_A=64.$$
Rubin (1991)，印刷页 28 的函数乘积为
$$
\Theta_0(z;(11))=
\delta\prod_{U\in(A[11]\setminus\{O\})/\{\pm1\}}
\bigl(x(z)-x(U)\bigr)^{-1},\qquad
\delta^{12}=\frac{\Delta(L)^{121}}{\Delta(11^{-1}L)}.
\tag{70.8}
$$
这里 $[11^{-1}L:L]=121$，且
$\Delta(11^{-1}L)=11^{12}\Delta(L)$，所以
$$\delta^{12}=\frac{\Delta_A^{120}}{11^{12}}.$$
标准除法多项式满足
$$
\psi_{11}(P)=11
\prod_{U\in(A[11]\setminus\{O\})/\{\pm1\}}
\bigl(x(P)-x(U)\bigr).
\tag{70.9}
$$
两式相乘时，前导系数 $11$ 正好消去 $\delta$ 中的 $11^{-1}$。
Robert 的规范函数和 (70.8) 是同一函数的十二次根；
该定义比较可见 Bley–Hofer (2020), §2.1，均对应
de Shalit, Chapter II.2 的 $\Theta$。因此
$$
\boxed{\Psi(P;L,11^{-1}L)=
\zeta_{12}\frac{\Delta_A^{10}}{\psi_{11}(P)},\qquad
\zeta_{12}^{12}=1.}
\tag{70.10}
$$
这也说明必须保留 $\psi_{11}$ 的**倒数**。
在模 $p$ Kummer 群中，十二次单位根为零；
常数 $\Delta_A^{10}\in K^\times$ 的非平凡 $C$ 特征投影亦为零。
因此计算所需的 $\chi_0=\rho^p$ 分量时，
$$e_{\chi_0}[\Psi(P)]=-e_{\chi_0}[\psi_{11}(P)]. \tag{70.11}$$

若 $\mathfrak m=(\gamma)$，对格子同时缩放
$\Psi(1;\mathfrak m,11^{-1}\mathfrak m)$，得到
(70.10) 在一个原始 $\mathfrak m$ 挠点的值。
原始点可取
$$P=P_2+P_p,\qquad0\ne P_p\in A[p]. \tag{70.12}$$
这是因为所有原始 $\pi^3$ 挠点在单位群 $\{\pm1,\pm i\}$ 下传递，
而其余的非零 $p$ 分量在 (70.6) 下传递。
乘以 $i$ 不改变 (70.10) 的函数值：$\psi_{11}$ 的根在
$x\mapsto-x$ 下稳定，次数为 $60$ 且前导系数不变，
故 $\psi_{11}(-x)=\psi_{11}(x)$。
因此 (70.12) 给原 Robert 单位的某个 Galois 共轭，
其正确特征分量仅相差非零标量。

这里 $\mathfrak m$ 已有 $2,p$ 两个不同素因子，故对应 Robert
值本身为全局单位。R65 为统一选择加入的 $(7)$ 不再是本例
保证整单位所必需的条件，但仍可严格保留它的归一化。
令
$$
v=\Psi(1;\mathfrak m,11^{-1}\mathfrak m),\qquad
u_1=N_{K(7\mathfrak m)/T}
\Psi(1;7\mathfrak m,11^{-1}7\mathfrak m).
$$
R65 的范数关系给
$$
e_{\chi_0}[u_1]
=\left(1-\chi_0(\sigma_{(7)})^{-1}\right)e_{\chi_0}[v]
=\frac87e_{\chi_0}[v],
\tag{70.13}
$$
因为算术 Frobenius 在 $(7)$ 的 CM 值是 $-7$。
它是非零因子；$p=43$ 时 $8/7=38$。

## 3. 完全在有限域中的局部投影

设 $q$ 为素数且 $q\equiv-1\bmod4p$。
因为 $\operatorname{Frob}_q^2=[-q]$，且
$-q\equiv1\bmod\pi^3p$，所有 $\mathfrak m$ 挠点都定义于
$$k_q=\mathbb F_q[i]=\mathbb F_{q^2},\qquad i^2=-1.$$
在该域中选取 $0\ne P_p\in A[p]$，固定 $P_2=(i,1-i)$，并记
$$Q_a=P_2+[a]P_p,\qquad a\in\mathbb F_{p^2}^\times. \tag{70.14}$$
具体地，若 $a=u+vi$，则
$[a]P_p=[u]P_p+[v][i]P_p$。

这里的 Artin 标签没有省略 primary 条件：由 CRT 取
$\alpha_a\equiv1\bmod\pi^3$、$\alpha_a\equiv a\bmod p$，
则 $\sigma_a=\operatorname{Artin}((\alpha_a))$ 固定 $P_2$，
并将 $P_p$ 送到 $[a]P_p$。
所以 $\rho(\sigma_a)=a$、$\chi_0(\sigma_a)=a^p$。

选本原 $p$ 次单位根 $\zeta\in k_q$，定义 $\ell_q(a)\in\mathbb F_p$：
$$
\psi_{11}(Q_a)^{(q^2-1)/p}=\zeta^{\ell_q(a)}.
\tag{70.15}
$$
每个 $Q_a$ 的整数阶为 $4p$，与 $11$ 互素，故
$\psi_{11}(Q_a)\ne0$；(70.15) 总有意义。

现在定义实际计算的量
$$
\boxed{S_q=
\sum_{a\in\mathbb F_{p^2}^\times}a^{-p}\ell_q(a)
\in\mathbb F_{p^2}.}
\tag{70.16}
$$
权是 $a^{-p}$，不是 $a^{-1}$：前者来自
$e_{\chi_0}=|C|^{-1}\sum_a\chi_0(a)^{-1}\sigma_a$。
在 $a=u+vi$ 的坐标中，它可以无歧义地计算为
$$a^{-p}=\frac{u+vi}{u^2+v^2}. \tag{70.17}$$
这里分母在 $\mathbb F_p$ 中非零，因为 $p\equiv3\bmod4$。
$k_q$ 中的 $i$ 与系数域 $\mathbb F_{p^2}$ 中的 $i$ 都标记
同一个 CM 自同态；这不表示存在两个不同特征有限域之间的嵌入。

在所选 $P_p,\zeta$ 及素理想的基下，
$e_{\chi_0}[\psi_{11}(P)]$ 的局部坐标为
$|C|^{-1}S_q$。
由于 $|C|=p^2-1\equiv-1\bmod p$，其逆也是 $-1$；
再用 (70.11) 的逆号，两个负号相消。因此
$$
e_{\chi_0}[v]\text{ 的局部坐标}=S_q,\qquad
e_{\chi_0}[u_1]\text{ 的局部坐标}=\frac87S_q.
\tag{70.18}
$$
这是 $[T:K]^{-1}$、Robert 倒数、判别式常数和 $(7)$ Euler 因子
全部纳入之后的公式。

由于 $q\ne p$，单位的局部 Kummer 类由剩余域的 $p$ 次剩余类
精确检测；$\mathfrak q=(q)$ 又在 $T/K$ 完全分裂。
张量正确的 $V(-1)$ 后，R65 的识别给
$$
\boxed{\operatorname{loc}_{\mathfrak q}\kappa_0=0
\quad\Longleftrightarrow\quad S_q=0.}
\tag{70.19}
$$

### 3.1 哪些数值依赖基，哪些结论不依赖

若改 $P_p$ 为 $[b]P_p$，则 (70.16) 变为 $b^pS_q$。
若改 $\zeta$ 为 $\zeta^t$，则它变为 $t^{-1}S_q$。
换原始 $\pi^3$ 分量也只带来非零单位标量；换 CM 嵌入可以再带来共轭。
这些变化都不改变零／非零。
因此下表的具体数值是**附带已记录基选择的坐标**，
不是一个未作基选择的规范全局标量，也不是 R60 的矩阵条目。

### 3.2 一个独立的 Frobenius 检查

计算中选择 $P_p\in A(\mathbb F_q)$。
于是 $P_2^{(q)}=[i]P_2$、$P_p^{(q)}=P_p$，且
$\zeta^q=\zeta^{-1}$。
由 $\psi_{11}([i]P)=\psi_{11}(P)$ 得
$$\ell_q(-i\overline a)=-\ell_q(a).$$
代入 (70.16) 并换元，得到
$$S_q=i\overline{S_q}. \tag{70.20}$$
所以在 $\mathbb F_{43}[i]$ 中两个坐标必须相同。
脚本逐个检查了这个由 Frobenius 产生的关系。

## 4. 精确计算结果

所有有限域元素均以 $(a,b)$ 表示 $a+bi$，坐标在相应素域中取
$0,\ldots,q-1$ 或 $0,\ldots,42$。
下列 $P_p$ 坐标在 $\mathbb F_q$ 中；
脚本验证 $P_p\ne O$、$[43]P_p=O$。
$\zeta$ 均取 $(2+i)^{(q^2-1)/43}$，并验证其阶恰为 $43$。

| $q$ | $P_p$ | $\zeta$ | $(q^2-1)/43$ | $S_q$ | $\frac87S_q$ |
|---:|---|---|---:|---|---|
| $859$ | $(209,268)$ | $97+829i$ | $17160$ | $40+40i$ | $15+15i$ |
| $1031$ | $(808,263)$ | $825+475i$ | $24720$ | $27+27i$ | $37+37i$ |
| $49019$ | $(11536,29305)$ | $19416+40301i$ | $55880520$ | $0$ | $0$ |

三行分别从有理剩余域点
$$R=(2,404),\quad(2,359),\quad(4,20853)$$
用 $P_p=[(q+1)/43]R$ 得到；乘数分别为 $20,24,1140$。
每行枚举了全部 $43^2-1=1848$ 个非零 $a$。

作为可手工定位的样点，取 $a=1$：

| $q$ | $Q_1$ 的 $x$ 坐标 | $\psi_{11}(Q_1)$ | (70.15) 的值 | $\ell_q(1)$ |
|---:|---|---|---|---:|
| $859$ | $263+270i$ | $612+44i$ | $551+200i$ | $17$ |
| $1031$ | $1012+554i$ | $227+879i$ | $252+866i$ | $9$ |
| $49019$ | $26333+40067i$ | $17554+16264i$ | $19416+40301i$ | $1$ |

特别地，退化行的单个样值并不是 $p$ 次幂；退化来自完整特征投影
的精确抵消，不能用某一个未经投影的值代替 (70.16)。

程序还按递增顺序枚举 $q\equiv-1\bmod172$。
在 $q\le49019$ 的全部 $57$ 个素数中，前 $56$ 个 $S_q$ 非零，
第 $57$ 个为表中的零。这只是已经完成的有限范围陈述；
R65 的 $1/p$ 密度是另一个已有证明，未由这个样本推断。
全部 $57$ 对 $(q,S_q\text{ 的第一坐标})$ 保存在小型 JSON 中。

## 5. 证书、算法和复算方式

代码和输出：

- [标准库 Python 脚本](../notes/verify_r70_elliptic_unit_residues.py)。
- [三个完整证书及有限搜索摘要](../notes/r70_elliptic_unit_residue_certificates.json)。

从仓库根目录执行：

```bash
python3 topics/serre-uniformity/notes/verify_r70_elliptic_unit_residues.py
```

默认重算表中的三个素数。加参数 `--search` 会从最小候选开始，
完整重算直到首个零投影；也可在命令末尾指定单个 $q$。
整个算法只用 Python 标准库，没有 Sage、PARI、浮点数或未证明的
素性判断。素性由试除至平方根确定。

$\psi_n$ 从
$$
\psi_0=0,\quad\psi_1=1,\quad\psi_2=2y,\quad
\psi_3=3x^4-6x^2-1,\quad
\psi_4=4y(x^6-5x^4-5x^2+1)
$$
和标准递推精确求值：
$$
\psi_{2m+1}=\psi_{m+2}\psi_m^3-\psi_{m-1}\psi_{m+1}^3,
$$
$$
\psi_{2m}=\frac{\psi_m}{2y}
\left(\psi_{m+2}\psi_{m-1}^2-\psi_{m-2}\psi_{m+1}^2\right).
\tag{70.21}
$$
这里各 $Q_a$ 的阶为 $172$，所以 $y(Q_a)\ne0$，递推中的除法合法。
每个 $q$ 的三处样点还使用直接椭圆曲线加法计算 $[11]Q_a$，
核对
$$
x([11]Q_a)=x(Q_a)-
\frac{\psi_{10}(Q_a)\psi_{12}(Q_a)}{\psi_{11}(Q_a)^2}.
$$
程序同时逐点验证曲线方程、$1848$ 个点互异、
$\psi_{11}$ 非零、剩余值落入所列全部 $43$ 个单位根，以及 (70.20)。

完整离散对数表按 $(u,v)$ 字典序存为三字节行
`u,v,ell`，跳过 `(0,0)`；其长度为 $5544$ 字节。
为避免把可再生表重复写入仓库，证书保存以下 SHA-256：

| $q$ | 完整离散对数表的 SHA-256 |
|---:|---|
| $859$ | `9619ef6d5db83421a808e52df8c21f8cf8264289ab2e03dea71cde86b38659b1` |
| $1031$ | `e374e194986c695449c4d425834dc70a4f5c0271630ae408e247471f507d8778` |
| $49019$ | `eb1107954809bee9edfe7dbc9f41148b2f4b585220ebb7af6a714b996e23f7dc` |

这些哈希用于复算一致性；数学结论来自已写明的完整有限枚举，
不以哈希代替证明。

## 6. 对 R65 的实际推进与保留的缺口

R65 的有限—奇异关系现在给出具体结论：
对 $q=859,1031$，原始一阶导数在作 $p$ 处校正之后非零，
可以生成对应单素数 Selmer 直线。
对 $q=49019$，该一阶导数在作 $p$ 校正之后严格为零；
此处须使用 R65 的辅助素数和原始二阶导数。

本次已经计算了**实际基 Robert 单位的局部投影**。
尚未计算 $\kappa_q$ 本身、$p$ 处 Hilbert 符号校正、
退化情形的第二辅助条件或 R60 的非对角矩阵条目。
尤其不能仅因 $859$ 的基投影非零，就断言它已满足
$q=49019$ 的第二辅助条件；后者还要求对应 $c_{859}$
在 $49019$ 的局部值非零。

本计算仍没有构造实际非 CM 的模 $43$ 同余曲线，
也没有给 R19 的整数解或变化 $p$ 的统一排除。

## 7. 已核验的来源

- K. Rubin, *The “main conjectures” of Iwasawa theory for imaginary quadratic fields*,
  Inventiones Mathematicae **103** (1991), 25–68，
  [DOI](https://doi.org/10.1007/BF01239508)，
  [Göttingen 原刊档案](http://resolver.sub.uni-goettingen.de/purl?PPN356556735_0103)。
  印刷页 28 的 $\Theta_0$ 乘积给 (70.8)，页 29 的单位构造、
  页 31 的 Proposition 2.4 和页 35 的 Theorem 3.3 已在 R65 核对。
- H. Oukhaba and S. Viguié, *On the Gras Conjecture for Imaginary Quadratic Fields*,
  Canadian Mathematical Bulletin **56** (2013), 148–160，
  [期刊全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0148F81E2EC11C708E2769B9AF48720C/S000843950000062Xa.pdf/on-the-gras-conjecture-for-imaginary-quadratic-fields.pdf)。
  §4 的 Robert 范数约定和 Remark 4.3；§5 的有限—奇异关系。
- W. Bley and M. Hofer, *Construction of elliptic $\mathfrak p$-units*,
  Advanced Studies in Pure Mathematics **86** (2020), 79–111，
  [作者全文](https://www.math.lmu.de/~bley/ImagSolRank2.pdf)，§2.1。
  本文只使用其中对 Robert 规范函数与 $\Theta$ 十二次根的定义比较；
  卷页和发表状态核对于作者论文目录，未使用其后面的新构造定理。
- J. H. Silverman, *The Arithmetic of Elliptic Curves*, second edition,
  Springer, 2009：椭圆曲线自同态环、有限域 Frobenius 与除法多项式的
  标准理论。计算用递推亦逐式核对于 A. Sutherland,
  [18.783 Lecture 5, §5.5、Theorem 5.21、Lemma 5.22](https://math.mit.edu/classes/18.783/2025/LectureNotes5.pdf)，2025。
- [R60](R60-selmer-matrix-kummer-residue-symbols.md) 与
  [R65](R65-elliptic-unit-first-second-derivatives.md)：
  正确的 $V(-1)$ 分量、基单位原始性、局部校正和退化补救。

导子及射线类域的特定模型计算已在 §1 给出；没有直接引用未经核实的
网络表格，也没有把别的四次扭曲的 Hecke 特征移植到当前模型。
