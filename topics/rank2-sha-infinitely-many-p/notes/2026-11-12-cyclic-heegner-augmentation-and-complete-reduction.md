# 实际循环 Heegner 增广商与完备好约化证书

日期：2026-11-12。状态：以下命题均已证明。
本篇加强单素数 Heegner 点判据的实际整数点接口，
没有证明该判据对无穷多个 $p$ 成立。

沿用 [单素数点判据](2026-11-12-one-prime-heegner-class-and-explicit-points.md)
中的固定 $E:y^2=x^3-17x$、辅助虚二次域 $F$、环类域 $F[\ell]$、
实际 Heegner 点 $P[\ell]$ 和整数导出点 $Y_\ell$。
$2,17$ 在 $F$ 分裂，$F\ne\mathbb Q(i)$，
$h=h_F$ 固定。目标素数 $p\ge5$ 在 $F$ 与 $\mathbb Q(i)$ 均分裂，
且 $p\nmid17\operatorname{disc}(F)$。

## 1. 分裂 CM 素数的好约化证书实际是完备的

Creutz–Lu（2023），Theorem 1.2(1)(a)，证明：若 $p$ 分裂于椭圆曲线的
CM 域且不除 CM order 的导子，那么对任意数域 $L$ 和任意 $M\ge1$，
$$
\ker\left(H^1(L,E[p^M])\longrightarrow
      \prod_{v\notin S}H^1(L_v,E[p^M])\right)=0
\tag{1}
$$
对每个有限位集合 $S$ 都成立。这里没有 $[L:\mathbb Q]$ 的上界。
本题 CM order 是 $\mathbb Z[i]$，因此全部目标普通素数都满足该定理。
原文 Definition 1.1 明确使用完整 $H^1$ 的局部核；
Lemma 2.2、Lemma 2.5 和 Theorem 1.2 的证明给所需比较。

若 $R\in E(L)$ 且 $v\nmid p$ 为好约化位，光滑约化的核是 residue
characteristic 的 pro-$\ell_v$ 群，乘 $p^M$ 在这个核上为同构。
约化满射遂给
$$
E(L_v)/p^M E(L_v)\simeq
\widetilde E(k_v)/p^M\widetilde E(k_v).
\tag{2}
$$
将 (1) 用于 $R$ 的 Kummer 类，得到
$$
R\notin p^ME(L)
\quad\Longleftrightarrow\quad
\text{在任意预先删去的有限位集合外，存在好位 }v\nmid p
\text{ 使 }\bar R\notin p^M\widetilde E(k_v).
\tag{3}
$$
所以单素数稿中的好约化充分证书在这里可以升级为完备证书。
这说的是 $E[p^M]$ 的 Kummer 类，不是声称
$H^1(L,E)[p^M]$ 中的 Sha 类必有非零局部像。

### 1.1 本题环类域上的更强、直接证明

令 $L=F[\ell]$，其中 $\ell$ 是单素数稿允许的辅助素数。
$L/\mathbb Q$ 在 $p$ 和 $2$ 不分歧。
对每个 $M\ge1$，令
$$
T=E[p^M],\quad K=L(T),\quad G=\operatorname{Gal}(K/L).
$$
在 CM 基底中，$G$ 恰为完整分裂 Cartan 的正规化子：
$$
G=N\bigl((\mathbb Z/p^M\mathbb Z)^\times
            \times(\mathbb Z/p^M\mathbb Z)^\times\bigr),
\qquad |G|=2\varphi(p^M)^2.
\tag{4}
$$

证明如下。$p$ 处的 CM 幂等元把整 $p$-divisible group 分成两个
高度一因子；其中一个为 étale 因子，另一个为连通因子。
好普通约化使前者在惯性上平凡；Weil 配对使后者在惯性上为
cyclotomic 特征。因此 $p$-惯性像包含全部
$\operatorname{diag}(a,1)$，$a\in(\mathbb Z/p^M\mathbb Z)^\times$。
$L$ 在 $p$ 不分歧，所以这一完整惯性仍包含于 $G_L$。
另一方面，$\mathbb Q(i)$ 在 $2$ 分歧，而 $L$ 在 $2$ 不分歧，
故 $G_L$ 中有交换两条 CM 线的元素。共轭前述惯性像得到全部
$\operatorname{diag}(1,a)$。两类元素生成完整 Cartan，再加交换线元素
得到整个正规化子。CM 作用又使全部像都包含于该正规化子，证明 (4)。

特别地，$-I\in G$，且 $-2$ 在 $\mathbb Z/p^M\mathbb Z$ 中可逆。
这里可直接证明
$$
H^1(G,T)=0.
\tag{5}
$$
若 $c:G\to T$ 为 cocycle，中心元素 $z=-I$ 给
$$
(z-1)c(g)=(g-1)c(z).
$$
取 $b=(z-1)^{-1}c(z)$，则 $c(g)=(g-1)b$，故为 coboundary。
这是 Sah 引理在本题中的完整一行证明。

若 $R\notin p^M E(L)$，(5) 和 inflation–restriction 使其 Kummer
类在 $G_K$ 上仍非零。取一个 $p^M$ 倍点 $Z$，$p^MZ=R$，并置
$B=K(Z)$。由于 $K$ 已包含全部 $T$，$B/L$ 是有限 Galois 扩张，
$$
W=\operatorname{Gal}(B/K)\hookrightarrow T
\tag{6}
$$
为非零平移群。$W\setminus\{0\}$ 在
$\operatorname{Gal}(B/L)$ 中是共轭稳定集合。
Chebotarev 因此给一组正密度的好位，满足
$$
v\text{ 完全分裂于 }K/L,
\qquad \bar R\notin p^M\widetilde E(k_v).
\tag{7}
$$
第二式成立是因为 Frobenius 在全部 $p^M$ 倍点上作用为非零平移，
所以没有一个倍点在 $k_v$ 有理。
这组 $L$ 的素理想的密度准确为
$$
\frac{|W|-1}{|W|\,|G|}>0.
\tag{8}
$$
因此允许额外要求全部 $p^M$ 挠点在约化域中有理，且可避开任意有限位集合。
这没有给出一个在证明 $R$ 不可除之前就已保证成功的位；
Chebotarev 使用的是已知非零的实际平移群 $W$。

## 2. 把实际导出点降到次数恰为 $p^M$ 的循环域

以下进一步取 $\ell$ 在 $\mathbb Q(i)$ 也惰性，并排除固定有限集合
$p\mid h$。记
$$
q=\ell+1=nu,\qquad n=p^M,\qquad p\nmid u,
\qquad M=v_p(\ell+1).
\tag{9}
$$
这时 $a_\ell(E)=0$，Heegner 范数关系准确给
$$
\operatorname{Tr}_{F[\ell]/F[1]}P[\ell]=0.
\tag{10}
$$
本节只处理这一方便的辅助素数子族，未把单素数判据的必要性
未经证明收窄到这个子族。

环类 Galois 群 $\Gamma=\operatorname{Gal}(L/F)$ 是阶 $hnu$ 的有限交换群。
因为 $p\nmid h$，其 $p$-Sylow $\Gamma_p$ 是 $G_\ell$ 中的唯一阶 $n$
子群，所以是循环群。设 $A$ 为 $\Gamma$ 的全部 prime-to-$p$ 部分，
从而
$$
\Gamma=\Gamma_p\times A,\qquad |A|=hu,
\qquad L_p=L^A,\qquad \operatorname{Gal}(L_p/F)\simeq C_n.
\tag{11}
$$
定义真实整数迹点
$$
Q_{\ell,p}=\operatorname{Tr}_{L/L_p}P[\ell]
          =\sum_{a\in A}aP[\ell]\in E(L_p).
\tag{12}
$$
不除以 $|A|$，不在 $E(L_p)\otimes\mathbb Q$ 中改变点。
令 $\tau$ 为 $\sigma_\ell$ 在 $\Gamma_p$ 上的像，仍是生成元，置
$$
D_n=\sum_{j=1}^{n-1}j\tau^j,
\qquad N_n=\sum_{j=0}^{n-1}\tau^j.
$$
由 (10)，有 $N_nQ_{\ell,p}=0$。

**命题。** 在 $E(L)/nE(L)$ 中准确有
$$
Y_\ell\equiv D_nQ_{\ell,p}\pmod{nE(L)}.
\tag{13}
$$
因此
$$
Y_\ell\notin nE(L)
\quad\Longleftrightarrow\quad
D_nQ_{\ell,p}\notin nE(L_p).
\tag{14}
$$

证明：$\Gamma/G_\ell$ 的代表可选在 $A$ 中，因为
$G_\ell\cap A$ 阶为 $u$，商阶为 $h$。
取这些代表定义 $Y_\ell$，则
$$
\operatorname{Tr}_A Y_\ell=hD_qQ_{\ell,p}.
$$
按指数模 $n$ 分组，得
$$
D_q Q_{\ell,p}
=uD_nQ_{\ell,p}
 +\frac{nu(u-1)}2 N_nQ_{\ell,p}
=uD_nQ_{\ell,p}.
\tag{15}
$$
另一方面，单素数下降已经证明 $Y_\ell\bmod nE(L)$ 为 $\Gamma$ 不变，
所以 $\operatorname{Tr}_A Y_\ell\equiv huY_\ell\pmod{nE(L)}$。
$hu$ 与 $n$ 互素，故可约去，得到 (13)。
换用其他陪集代表不改变 $Y_\ell\bmod nE(L)$；
这也直接由 $(\sigma_\ell-1)D_q=q-N_q$ 和 (10) 得到。

由于 $[L:L_p]=hu$ 与 $n$ 互素，
$$
E(L_p)/nE(L_p)\longrightarrow E(L)/nE(L)
$$
为单射。确切地，若 $R=nZ$ 且 $R\in E(L_p)$，则
$n\operatorname{Tr}_{L/L_p}Z=huR$；用 Bezout 等式
$a hu+bn=1$ 得
$R=n(a\operatorname{Tr}Z+bR)$，括号内是真实 $L_p$-点。
这证明 (14)。

## 3. 缺少的条件成为真实整数点群的增广商

令
$$
\mathcal M_{\ell,p}
=\ker\bigl(N_n:E(L_p)\to E(F)\bigr),
\qquad \Delta=\tau-1.
\tag{16}
$$
这是实际 Mordell–Weil 点群的子群，$Q_{\ell,p}\in\mathcal M_{\ell,p}$。
$E(L_p)[p]=0$ 已由 $E(L)[p]=0$ 得到。

**命题。** 对任意 $Q\in\mathcal M_{\ell,p}$，
$$
D_nQ\in nE(L_p)
\quad\Longleftrightarrow\quad
Q\in\Delta\mathcal M_{\ell,p}.
\tag{17}
$$

若 $D_nQ=nZ$，使用 $\Delta D_n=n-N_n$ 得
$n\Delta Z=nQ$。没有 $n$ 挠点，故 $\Delta Z=Q$。
又 $N_nD_nQ=n(n-1)N_nQ/2=0$，所以 $nN_nZ=0$。
$E(F)[n]=0$ 使 $N_nZ=0$，即 $Z\in\mathcal M_{\ell,p}$。
反向若 $Q=\Delta Z$ 且 $N_nZ=0$，则
$D_nQ=(n-N_n)Z=nZ$。这证明 (17)。

因 $n=D_n\Delta$ 在 $\mathcal M_{\ell,p}$ 上成立，
$\mathcal M_{\ell,p}/\Delta\mathcal M_{\ell,p}$ 是被 $n$ 杀掉的有限群。
有限性也可直接看出：在该群的有理化上，$N_n=0$ 排除了平凡特征，
所以 $\Delta$ 可逆；实际点群有限生成。
(17) 给一个实际单射
$$
\mathcal M_{\ell,p}/\Delta\mathcal M_{\ell,p}
\hookrightarrow E(L_p)/nE(L_p),\qquad [Q]\longmapsto[D_nQ].
\tag{18}
$$
结合 (14)，本子族中的成功条件准确为
$$
\boxed{\quad
[Q_{\ell,p}]\ne0
\quad\text{于}\quad
\mathcal M_{\ell,p}/(\tau-1)\mathcal M_{\ell,p}.
\quad}
\tag{19}
$$
也可将 (3) 用于 $D_nQ_{\ell,p}$，得到只在次数 $n$ 的实际循环域
$L_p$ 上寻找好约化位的完备证书。
$L_p$ 仍在 $p,2$ 不分歧且不包含 $\mathbb Q(i)$，
故 §1.1 的完全分裂及正密度加强也同样适用。

## 4. 这个实际商内的范数点部分与 Weil–Châtelet 部分

仍写 $\mathcal M=\ker N_n$、$\Gamma_p=\langle\tau\rangle$。
循环群上同调给 $H^1(\Gamma_p,E(L_p))=\mathcal M/\Delta E(L_p)$。
因此本题存在准确短正合列
$$
0\longrightarrow
\frac{N_nE(L_p)}{nE(F)}
\xrightarrow{\ j\ }
\frac{\mathcal M}{\Delta\mathcal M}
\longrightarrow H^1(\Gamma_p,E(L_p))
\longrightarrow0,
\qquad j([N_nZ])=[\Delta Z].
\tag{20}
$$
注意 $N_nE(L_p)\subset E(F)$ 且包含 $nE(F)$。
若两个 $Z$ 的范数相同，它们相差 $\mathcal M$，所以 $j$ 良定义。
将范数改动 $nR$ 可用 $Z\mapsto Z+R$ 实现，而 $\Delta R=0$。
若 $\Delta Z\in\Delta\mathcal M$，则 $Z$ 与某个 $\mathcal M$ 中的点
相差 $E(F)$ 中的点，所以 $N_nZ\in nE(F)$，证明 $j$ 单射。
其像恰为 $\Delta E(L_p)/\Delta\mathcal M$，证明全部正合性。

(18) 后的 Kummer 下降也有明确符号。对 $Q\in\mathcal M$，
选 $Z\in E(\overline F)$ 满足 $nZ=D_nQ$。若 $g$ 在 $\Gamma_p$ 中的像
为 $\tau^k$，定义
$$
r_Q(g)=\sum_{j=0}^{k-1}\tau^jQ,
\qquad
c_Q(g)=gZ-Z-r_Q(g)\in E[n].
\tag{21}
$$
$N_nQ=0$ 使 $r_Q$ 与 $k\bmod n$ 的选取无关，并使其为 cocycle。
$gD_nQ-D_nQ=nr_Q(g)$ 保证 $c_Q(g)$ 确实在 $E[n]$ 中。
它在 $G_{L_p}$ 上限制为 $D_nQ$ 的 Kummer 类，故由无 $n$ 挠点的
唯一下降，正是 (18) 对应的全局类。
在 $H^1(F,E)$ 中，这个类的像为
$$
[c_Q]\longmapsto-\operatorname{inf}[r_Q]
=-\operatorname{inf}[Q].
\tag{22}
$$
若 $Q=\Delta Z_0$，则
$$
D_nQ=nZ_0-N_nZ_0,
\qquad [c_Q]=-\delta_n(N_nZ_0).
\tag{23}
$$
因此 (20) 的左端准确映到基域 Mordell–Weil 的 Kummer 子群，
右端记录限制到 $L_p$ 后消失的 Weil–Châtelet 类。

对实际 $Q=Q_{\ell,p}$，单素数稿已经证明 $c_Q$ 在 $F$ 上满足全部
通常 Selmer 局部条件，且为复共轭正特征。
所以 (22) 的实际像落在 $\Sha(E/F)[n]^+$，并对应
$\Sha(E/\mathbb Q)[n]$。若能构造一个真实整数点 $Z_0\in E(L_p)$
使 $\Delta Z_0=Q_{\ell,p}$，则 (23) 把它完全接回基域点
$N_nZ_0$；成功条件是这个范数不在 $nE(F)$。
其正特征的模 $n$ 类可以与已知 $P,Q$ 比较，正好恢复单素数稿的
Mordell–Weil 归属判据。
这里没有先假定右端 Sha 部分为零，也没有把任意 $Q\in\mathcal M$
产生的类都声称为 Selmer 类。

## 5. 与现有高度原始性的精确差别

[高度笔记](2026-11-12-heegner-height-and-augmentation-primitivity.md)
已经证明：对所有充分大的目标 $p$，可选合法 $\ell$ 使
$P[\ell]\notin pE(F[\ell])$。
现在 (12)、(19) 指出还需通过两个实际整数映射：先取
$\operatorname{Tr}_A$，再投到 norm-zero 群的增广商。
高度结果没有证明这两个映射后的像非零。

特别地，(19) 中被除的是真实 $\Delta Z$，且 $Z$ 还必须满足
$N_nZ=0$；不能把它换成 $Q/n$，也不能只要求 $Q$ 自身不被 $p$ 除。
§1 提供完整的成功检测，§2–4 缩小实际点群及分离范数点与可能的 Sha 部分；
它们没有把需要证明的非零性写入 Chebotarev 的输入后再当作输出。

## 来源

- B. Creutz、S. (Victor) Lu（2023），
  *The local-global principle for divisibility in CM elliptic curves*，
  Journal of Number Theory **250**, 139–154，
  DOI [10.1016/j.jnt.2023.03.005](https://doi.org/10.1016/j.jnt.2023.03.005)。
  [作者全文](https://www.math.canterbury.ac.nz/~b.creutz/Papers/CMdivisibility.pdf)：
  Definition 1.1、Theorem 1.2(1)(a)、Lemma 2.2、Lemma 2.5。
  发表信息亦见[作者目录](https://www.math.canterbury.ac.nz/~b.creutz/Research.html)。
- 原 Heegner 范数、实际导出点、全 $p^M$ 下降和 $E(F[\ell])[p]=0$：
  [单素数点判据](2026-11-12-one-prime-heegner-class-and-explicit-points.md)，
  其中逐项列明 Howard（2004）和 BCGS（2026）的输入。
- §1.1、§2–4 的额外比较均在本文给出证明；
  §3 使用真实点群，不以任意抽象格例子替代实际对象。
