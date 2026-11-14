# R105：PPP1995原文条件与原子表示障碍

主会话已全文核验；完整ISP未解决。

日期：2026-11-12。作者分工：literature / 0c。拟登记 R105。

**状态：** §2–6 中关于当前算子的命题均已证明。PPP1995 的条件和定理编号已经直接对照作者公开上传的完整原文；本稿新增的是对当前算子的逐项核验和原子表示障碍。Jung–Ko–Pearcy2019 的完整条件仍未取得，§7 明确保留这一文献缺口。

## 1. 原文、取得方式与精确位置

Vern Paulsen、Carl Pearcy、Srdjan Petrović，*On Centered and Weakly Centered Operators*，Journal of Functional Analysis **128** (1995), 87–101，DOI [10.1006/jfan.1995.1024](https://doi.org/10.1006/jfan.1995.1024)。

核验所用的是 [Vern Paulsen 公开上传的完整论文](https://www.researchgate.net/publication/251423632_On_Centered_and_Weakly_Centered_Operators)，页面标明上传日期为 2017-11-11。这次通过该页面的普通 Download full-text PDF 按钮成功取得，正文有期刊页码 87–101。它是扫描 PDF；OCR 只用于定位，关键定理的公式和条件已经对照原图。

临时原始文件位于：

    /opt/codex/downloads/eec8d81e-b29b-45f0-8f84-460470d1b68c/f3fa456f-6439-4e33-953b-cf7ccacace90

文件大小 580353 字节，SHA-256：

    e3fd597609baa95650a2fc0bb3fae437e40f9855b69a9f662baa5700b354d96b

临时 OCR 和关键页图在 /tmp/isp_centered_sources/；这些第三方全文、OCR 和图像不进入仓库。以下使用期刊印刷页码：

| 原文位置 | 本稿使用的内容 |
|---|---|
| p.94，Theorem 2.9 | 谱包含单位圆的 centered、power bounded 算子具有非平凡不变子空间 |
| p.95，Proposition 3.4 | 一个由单个模算子生成的 von Neumann 代数条件 |
| p.96，Corollary 3.5 | 模算子具有循环向量时的充分条件 |
| p.97，Conjecture 3.8、Proposition 3.9 | MASA 自同构条件；纯点谱足以保证该条件 |
| pp.97–99，Theorem 3.10 | 带额外酉因子的加权复合表示 |
| pp.99–100，Corollary 3.11 | 纯点模算子的置换矩阵与额外酉因子表示 |

此表列的是原文内容定位；下面对本算子的判断给出独立证明。

## 2. 当前算子及其单个模算子的谱重数

设

$$
H=L^2(\mathbb Z_2,\mu),\qquad
(Uf)(y)=f(y-1),\qquad
w(y)=
\begin{cases}
a_{v_2(y)},&y\ne0,\\
0,&y=0,
\end{cases}
$$

其中 $\mu$ 为 Haar 概率测度，$a_0>a_1>\cdots>0$ 且 $a_j\to0$。当前仓库中的权满足这些条件，并且 $a_0=e^{-20}$。研究算子为

$$
A=M_wU=UP,\qquad P=|A|=M_{w(\,\cdot+1)}.
\tag{2.1}
$$

因 $w>0$ 几乎处处，$A$ 和 $A^*$ 都单射，$A$ 有稠密值域；所以这里的极分解相位 $U$ 是酉算子。记

$$
C_j=\{y:v_2(y+1)=j\},\qquad
Q_j=M_{\mathbf1_{C_j}}\quad(j\ge0).
$$

这些集合两两不交，$\mu(C_j)=2^{-j-1}$，并在略去单点 $-1$ 后穷尽空间。因此

$$
P=\sum_{j=0}^{\infty}a_jQ_j
\tag{2.2}
$$

在算子范数下收敛，且

$$
H=\bigoplus_{j\ge0}L^2(C_j,\mu).
\tag{2.3}
$$

每个 $L^2(C_j,\mu)$ 都无限维。因此：

1. $P$ 有纯点谱，含义是其特征向量线性张成一个稠密子空间；特征值为 $a_j$。
2. 每个非零特征值 $a_j$ 的重数都是无穷。
3. $0\in\sigma(P)$，但 $0$ 不是特征值。
4. $P$ 不紧；例如在任一固定 $L^2(C_j)$ 中取正交单位向量列，$P$ 在这列上恒为非零倍数。
5. $P$ 没有循环向量。对任何 $f$，所有 $p(P)f$ 在 $L^2(C_j)$ 上的分量都属于至多一维空间 $\mathbb C Q_jf$，不可能稠密于无限维的 $L^2(C_j)$。

此外，

$$
UPU^*=M_w.
\tag{2.4}
$$

由单个 $P$ 生成的 unital von Neumann 代数是

$$
W^*(I,P)=
\left\{\sum_{j\ge0}c_jQ_j:(c_j)\in\ell^\infty\right\}.
\tag{2.5}
$$

证明式 (2.5) 时，一方向来自有界 Borel 演算，另一方向来自各特征值的谱投影。这个代数在每个 $L^2(C_j)$ 上仅作用为标量，故不是 MASA。

尤其

$$
UPU^*\notin W^*(I,P).
\tag{2.6}
$$

确实，在 $C_0=\{y:y\text{ 为偶数}\}$ 上，$P$ 恒等于 $a_0I$，而 $UPU^*=M_w$ 至少分别在 $v_2(y)=1$ 和 $v_2(y)=2$ 的正测度集合上取不同值 $a_1,a_2$。式 (2.5) 中的算子在整个 $C_0$ 上必须为常数，产生矛盾。

所以 PPP Proposition 3.4 的特定假设和 Corollary 3.5 的循环模算子假设对当前 $A$ **不成立**；不能因为 $A$ 已知 centered 就反向宣称这些充分条件成立。

## 3. PPP 的 MASA 技术假设确实满足

这里 MASA 指 $B(H)$ 中的极大交换 von Neumann 代数。

PPP Conjecture 3.8 / Theorem 3.10 所用的附加条件可写为：

$$
P,UPU^*\in\mathcal D_0,\qquad
\Phi:\mathcal D_0\longrightarrow\mathcal D_0
\text{ 是 *-automorphism},\qquad
\Phi(P)=UPU^*,
\tag{3.1}
$$

其中 $\mathcal D_0$ 为一个 MASA。原文 Proposition 3.9 证明：如果 $P$ 有纯点谱，条件 (3.1) 可实现。由 §2，当前算子符合这个充分条件。

我们还有更直接、无需选择特征基的实现。令

$$
\mathcal D=\{M_h:h\in L^\infty(\mathbb Z_2,\mu)\}.
\tag{3.2}
$$

该代数是 MASA。一个自含证明如下。若 $S\in B(H)$ 与所有 $M_h$ 交换，令 $g=S1$。对于有界 $h$，

$$
Sh=SM_h1=M_hS1=hg.
$$

对任意可测集合 $E$，有

$$
\|\mathbf1_Eg\|_2=\|S\mathbf1_E\|_2
 \le\|S\|\mu(E)^{1/2}.
$$

从而 $g\in L^\infty$ 且 $\|g\|_\infty\le\|S\|$。有界函数在 $L^2$ 中稠密，故 $S=M_g$，即 $\mathcal D'=\mathcal D$。

现在设

$$
\Phi(M_h)=UM_hU^*=M_{h(\,\cdot-1)}.
\tag{3.3}
$$

平移保持 Haar 测度，故这是 $\mathcal D$ 的 *-automorphism，并且式 (2.4) 给出 $\Phi(P)=UPU^*$。所以 (3.1) 对实际 $A$ 已经直接验证。

PPP Theorem 3.10 的表示形式为

$$
WTW^{-1}=S\Theta M_{\Gamma(P)},
\tag{3.4}
$$

其中 $S$ 是由相应 nonsingular 变换和 Radon–Nikodym 因子得到的酉加权复合算子，$\Theta$ 是与 $M_{\Gamma(P)}$ 交换的酉算子；$\Gamma$ 为所选 MASA 的 Gelfand 表示。原文底空间是该 MASA 的紧 Hausdorff 最大理想空间，不能不加说明将其等同于原来的 $\mathbb Z_2$。

对我们选择的 **无原子乘法 MASA** (3.2)，实际相位 $U$ 本身已经实现 $\Phi$。因此本来的 Haar 加权复合实现 (2.1) 中，额外酉因子可取为

$$
\Theta=I.
\tag{3.5}
$$

这并未提供新的不变子空间：它重新表达已有的 $M_wU$ 结构。不能把下节原子表示中额外酉因子必不可消的结论错误地套到这个无原子实现上。

## 4. 所有平移模算子的联合代数是无原子 MASA

**命题 4.1。** 对当前严格递减径向权，

$$
\mathcal D=
W^*\bigl(I,\ U^nPU^{-n}:n\in\mathbb Z\bigr).
\tag{4.1}
$$

特别地，右侧是无原子 MASA，尽管每个单独的 $U^nPU^{-n}$ 都有纯点谱。

**证明。** 每个

$$
P_n=U^nPU^{-n}=M_{w(\,\cdot+1-n)}
$$

都是乘法算子，所以右侧包含于 $\mathcal D$。反过来，对任意 $m\ge1$，其 Borel 谱投影满足

$$
\mathbf1_{[0,a_m]}(P_n)
 =M_{\mathbf1_{\{y:y+1-n\equiv0\pmod{2^m}\}}}.
\tag{4.2}
$$

这里严格递减保证 $w(z)\le a_m$ 等价于 $z\equiv0\pmod{2^m}$；$z=0$ 处同样成立。

让 $n$ 变化，式 (4.2) 给出模 $2^m$ 的所有剩余类乘法投影。再让 $m$ 变化，得到全部 dyadic cylinder 投影。有限 cylinder 函数生成 $\mathbb Z_2$ 的 Borel $\sigma$-代数；对任意 $h\in L^\infty$，它的 dyadic 条件期望 $h_m$ 一致有界并在 $L^2$ 中趋于 $h$。于是 $M_{h_m}\to M_h$ 强收敛：先对有界测试函数用 $L^2$ 收敛，再利用一致算子范数界扩展至全部 $L^2$。所以右侧包含 $\mathcal D$，证明 (4.1)。

最后，任意非零乘法投影 $M_{\mathbf1_E}$ 都可被分裂。取 $m$ 使 $2^{-m}<\mu(E)$，必有一个模 $2^m$ 剩余类 $C$ 满足 $\mu(E\cap C)>0$，并且

$$
0<\mu(E\cap C)\le2^{-m}<\mu(E).
$$

因此 $M_{\mathbf1_{E\cap C}}$ 是其非零真子投影。故 $\mathcal D$ 无非零极小投影，即无原子。$\square$

这也解释了一个容易混淆的层次：

- 每个单独模算子的谱测度是纯点的；
- 整个可交换族的联合谱表示却是无原子的。

前者不蕴含整个族具有共同正交特征基。这里的后者由式 (4.1) 明确证明。

## 5. 原子 MASA 与标量置换加权移位表示的障碍

**定理 5.1。** 不存在原子 MASA $\mathcal E\subset B(H)$ 同时满足

$$
P\in\mathcal E,\qquad U\mathcal EU^*=\mathcal E.
\tag{5.1}
$$

**证明。** 假设存在这样的 $\mathcal E$。由归一化条件，所有 $U^nPU^{-n}$ 都属于 $\mathcal E$。命题 4.1 给出 $\mathcal D\subseteq\mathcal E$。又因 $\mathcal E$ 交换，

$$
\mathcal E\subseteq\mathcal D'=\mathcal D.
$$

故 $\mathcal E=\mathcal D$，与 $\mathcal E$ 原子而 $\mathcal D$ 无原子矛盾。$\square$

此处“原子 MASA”包括任意可数正交基上的全部对角算子代数；其一维坐标投影是极小投影。

**推论 5.2。** 当前 $A$ 不酉等价于任何标量 weighted-permutation 矩阵。即不存在正交基 $(e_j)_{j\in J}$、双射 $\pi:J\to J$ 和非零有界复权 $b_j$，使

$$
Ae_j=b_je_{\pi(j)}.
\tag{5.2}
$$

**证明。** 若存在，则 $P$ 在此基中为对角算子，

$$
Pe_j=|b_j|e_j,
$$

而极分解相位满足

$$
Ue_j=\frac{b_j}{|b_j|}e_{\pi(j)}.
$$

因此 $U$ 归一化此基的原子对角 MASA，违反定理 5.1。$\square$

该结论也排除可数个经典标量双边加权移位的正交直和的酉表示。更一般，若声称表示为各种经典标量 unilateral/bilateral/truncated shifts 的直和，则单射与稠密值域已经排除非零单边或截断移位分量：向前单边移位值域不稠密，向后单边移位有核，截断分量也有核。双边部分再由推论 5.2 排除。

**这里仅断言酉表示不可能，没有断言任意相似变换后的表示也不可能。** 相似变换不保留极分解模算子及其联合 von Neumann 代数；本证明不覆盖它。

### 5.1 PPP Corollary 3.11 的额外因子为何不可删

原文 Corollary 3.11（pp.99–100）在 $P$ 纯点谱条件下给出

$$
A=U_1U_2P,
\tag{5.3}
$$

并存在一个正交基，使 $P$ 对角、$U_1$ 为置换矩阵，且

$$
U_2P=PU_2.
\tag{5.4}
$$

因为 $P$ 的值域稠密，式 (2.1)、(5.3) 强制

$$
U=U_1U_2.
\tag{5.5}
$$

在该基中，$U_2$ **不可能也为对角矩阵**。否则 $U_1U_2$ 归一化该基的原子对角 MASA，而 $P$ 属于此 MASA，违反定理 5.1。特别地，$U_2$ 不可能是 $I$，也不可能是任何 $P$ 的有界 Borel 函数。

因此以下两项同时成立而不矛盾：

- 选择原来的无原子乘法 MASA 时，加权复合表示中的 $\Theta$ 可取 $I$。
- 选择 Corollary 3.11 的原子置换矩阵表示时，与 $P$ 交换的额外因子 $U_2$ 不能再对角化或删掉。

无限谱重数正是允许 $U_2$ 在每个 $P$ 特征空间内仍有非标量作用的空间。原文没有把这一作用宣布消失。

## 6. 已核条件逐项对照与真正适用范围

当前 $A$ 的 centered 性也可直接验证。设

$$
w_n(y)=\prod_{r=0}^{n-1}w(y-r).
$$

则

$$
A^n=M_{w_n}U^n,\qquad
A^nA^{*n}=M_{w_n^2},\qquad
A^{*n}A^n=M_{w_n(\,\cdot+n)^2}.
\tag{6.1}
$$

因此所有双侧模平方都是乘法算子，整个族两两交换。此处 $w$ 为实非负；若改写一般复权，则相应地使用绝对值平方。

结合 §§2–5，可得以下精确对照：

| PPP1995 的条件或结论 | 当前 $A$ 的判断 | 证明或原文位置 |
|---|---|---|
| quasi-invertible、weakly centered | 满足 | §2 单射稠密、式 (6.1) |
| centered、power bounded | 满足 | 式 (6.1)，且 $\|A\|=a_0<1$ |
| Theorem 2.6 的 similar to contraction 结论 | 满足，但本算子本身已是严格收缩 | 原文 pp.93–94 |
| Theorem 2.9 另外要求 $\sigma(A)\supseteq\mathbb T$ | 不满足 | 已证 $\sigma(A)=\{0\}$；任意非零标量重缩放也不能修复 |
| Proposition 3.4 要求 $UPU^*\in W^*(I,P)$ | 不满足 | 式 (2.6) |
| Corollary 3.5 要求 $P$ 有循环向量 | 不满足 | §2 每个非零特征值重数无穷 |
| Proposition 3.9 的纯点谱充分条件 | 满足 | 式 (2.2)–(2.3) |
| Theorem 3.10 的 MASA 自同构条件 | 满足 | 式 (3.2)–(3.3) 直接验证 |
| Corollary 3.11 的置换因子分解 | 可用，但额外因子不能删 | §5.1 |
| 由此直接推出普通不变子空间或超不变子空间 | 未得出 | Theorem 3.10 / Corollary 3.11 是结构表示；Theorem 2.9 的附加谱条件失败 |

最后一行并不声称 $A$ 没有不变子空间，而是限定本次已经验证的文献结论究竟提供了什么。

## 7. JKP2019 的获取结果与仍未核实的条件

Il Bong Jung、Eungil Ko、Carl Pearcy，*Hyperinvariant subspaces for a class of quasinilpotent operators*，Studia Mathematica **245** (2019), 289–296，DOI [10.4064/sm171209-18-1](https://doi.org/10.4064/sm171209-18-1)，期刊标注在线发表日期 2018-08-24。

本轮重新检查了以下公开入口：

1. [期刊正式文章页](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/245/3/111414/hyperinvariant-subspaces-for-a-class-of-quasinilpotent-operators)。普通 Download 入口在浏览器中进入付费结算页，显示当前访问环境没有 Studia Mathematica 2019 的访问权限；没有执行购买。
2. [作者 ResearchGate 记录](https://www.researchgate.net/publication/327215654_Hyperinvariant_subspaces_for_a_class_of_quasinilpotent_operators)。实际页面显示 No full-text available 和向作者请求全文的按钮；没有发送请求。
3. [Ewha 原始机构库记录](https://dspace.ewha.ac.kr/handle/2015.oak/248118)。Files in This Item 明确显示没有附属文件。
4. [Ewha 研究成果页面](https://pure.ewha.ac.kr/en/publications/hyperinvariant-subspaces-for-a-class-of-quasinilpotent-operators/) 只链接 DOI。
5. Ewha 官方研究所页面所列 [Eungil Ko 个人主页](http://home.ewha.ac.kr/~eiko/) 在本环境普通访问显示 Forbidden，没有取得作者稿。

因此，尽管 PPP1995 这一层已经由原文闭合，**JKP2019 自身的完整附加条件仍未核实**。不得把 §3 已验证的 PPP 技术假设充当 JKP 的全部条件，也不得用 §5 排除标量加权移位表示来替代 JKP 的实际假设。

本稿不将 JKP 标记为“适用”或“不适用”；还需合法取得其正文后逐项对照。现有 source record 的缺口是真实全文缺口，不是计算中已经发现的反例。
