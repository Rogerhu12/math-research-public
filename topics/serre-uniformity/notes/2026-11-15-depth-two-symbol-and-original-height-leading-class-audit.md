# 原深度二符号与固定 CM 首项的核对

日期：2026-11-15。性质：研究核对，**不另立新 R 号，也不登记新的非消失结论**。已全文复读 R634、R682、R699、R724、R785，并直接核对 Besser–Müller–Srinivasan 原文 Theorem 7.9、Lemma 7.12 及证明。此次没有进行任何新数学数值运算。

目前得到的边界是：原每个 $E_{ij}$ 逐盘非恒零已经由 R634 完成；本次没有从深度二符号、极化或除子结构推出原 $\mathscr T_p\ne0$。下面记录所核的准确蕴含和仍须判定的同一原等式，供后继真实高度输入使用。

## 1. 非恒零不是新的缺口

在 R616 的同一实际非消失前提内，R634 定理 634.3 已对每个 $i<j$、每对真实坏处靶值证明
$$
 E_{ij}^{\omega,\omega_0}\not\equiv0
$$
且它在每个局部盘上均非恒零。

这里用的是原有理 NS 类 $q^*[\mathcal L_h]$ 的独立性及实际拉回平凡线丛。原 Picard 零次修正不改变 NS 类；但其规范局部值及 $-2\ell_h(P_Y)$ 在函数中始终保留。将后者减去只是全纯一重积分变量的三角变换，不是删掉原项。R634 的形式多项式对 $\Lambda_i,\Lambda_j$ 的偏导分别为 $-V_j,V_i$，因此它确实是非零多项式，能使用 BMS 的代数独立性结论。这不是仅凭中心维数或抽象稠密性推断指定函数非零。

原文的 $D_2$ 是迭代积分深度的张量算子，**不是**局部参数 $z$ 的二阶导数。BMS Lemma 7.12 将其模全纯二次张量的像与原 Chern 类联系；Theorem 7.9 经 shuffle 张量论证排除恒等多项式关系。它不提供指定点的非零 Taylor 系数或赋值。[BMS，2021；v4，2026，§7.2](https://arxiv.org/html/2112.03873v4#S7.SS2)。

因此，不能把已证的非恒零性再包装为一个新的高度排除结果。R699/R703/R716 已将其接到有限首阶及完整尾的接口；这些也不重做。

## 2. 在原 $c_1$ 重基点后，所需二阶外积看见什么

保持原 $z=a-1$、$\beta=q[c_1-c_0]$、加权迹坐标和 R696 的同一零靶。只在共同 Abel 首阶已证明为 $m=1$ 的范围内写
$$
 t_i=1+T_i z+O(z^2),\qquad
 \Lambda_i=d_i+g_i z+O(z^2).
$$
于是
$$
 v_i=T_i-T_g,\qquad s_i=2d_iT_i-g_i,\qquad
 [z^2]E_{ij}=2(s_iv_j-s_jv_i).
 \tag{1}
$$
R785 已定义
$$
 \mathscr T_p=[s]\in K^r/Kv,\qquad r=g-1,
 \tag{2}
$$
这里 $K$ 可取所需的有限 $p$ 进坐标分裂域。R634 的 $v\ne0$ 已足够定义它；R682 在同一前提内还给每个 $T_i$ 非零且两两不同。后一个加强只保证相关分母非零，不决定式 (1)。

R699 的原函数分解直接说明，为什么深度二符号并未决定式 (1)。用其固定 $c_0$ 的不变规范，准确有
$$
 \begin{aligned}
 \Lambda_i(x)=d_i
 &+\int_{c_1}^x\left(
       \sum_b\omega_{ib}\int_{c_1}^{(\cdot)}\eta_{ib}
                      +\gamma_i^{\rm inv}\right)\\
 &+\sum_b P_{ib}^{(2)}\int_{c_1}^x\omega_{ib}
   +\sum_j c_{ij}^Y\int_{\phi(c_1)}^{\phi(x)}\upsilon_j,
 \qquad
 P_{ib}^{(2)}=\int_{c_0}^{c_1}\eta_{ib}.
 \end{aligned}
 \tag{3}
$$
所有被积微分在原 $c_1$ 盘正则。式 (3) 中重新以 $c_1$ 归零的双重积分属于 $z^2K[[z]]$，它乘 $V_j\in zK[[z]]$ 后只从外积的三阶开始贡献。因此原一次高度系数是
$$
 \boxed{\;
 g_i=
  (\gamma_i^{\rm inv}/dz)(c_1)
 +\sum_b P_{ib}^{(2)}(\omega_{ib}/dz)(c_1)
 +\sum_j c_{ij}^Y(\phi^*\upsilon_j/dz)(c_1).
 \;}
 \tag{4}
$$
这只是对原 R699 (699.27i)–(699.27k) 求导，没有改动高度或设置任意新常数。

式 (4) 并不是说曲率与首项无关：$\gamma_i^{\rm inv}$ 的代数构造来自原曲率。它说明真正的首项还含固定点间的第二类周期和原全纯规范差，而 $D_2$ 的类没有提供这些边界值。用只在 $c_1$ 归零的双重积分取代整个式 (3)，会准确漏掉后两项及原 $d_i$。

## 3. 留下的是同一个明确的周期等式

取 R682 的原代数 Lie 基，写
$$
 L_i=\omega_i(\log_p\beta)\ne0,\qquad
 a_i=\omega_i(u_1)\in\overline{\mathbb Q}^{\times},
 \qquad T_i=a_i/L_i.
$$
这里 $u_1$ 是原有理映射 $j_A-\beta$ 的一阶 Lie 系数，不是另一个 CM 点的微分系数。将式 (1) 乘以确切非零分母 $L_iL_jL_g$ 得
$$
 \begin{aligned}
 &(2d_i a_i-g_iL_i)(a_jL_g-a_gL_j)\\
 &\hspace{10mm}
 -(2d_j a_j-g_jL_j)(a_iL_g-a_gL_i)=0.
 \end{aligned}
 \tag{5}
$$
**原 $\mathscr T_p=0$ 当且仅当式 (5) 对全部 $i<j$ 成立。** 这里仍是原 $d_i,g_i,L_i$，没有引入可任选的高度。

固定一个 $v_{i_0}\ne0$ 后，也可只检验 R785 的 $r-1$ 个商坐标
$$
 \varepsilon_i=
  2d_iT_i-g_i-
  \frac{T_i-T_g}{T_{i_0}-T_g}(2d_{i_0}T_{i_0}-g_{i_0})
 \quad(i\ne i_0).
 \tag{6}
$$
这没有减少 R785 已登记的输入，只将同一等式保留为可清对数分母的形式。

R682 的解析子群论证排除的是代数系数对 $\log_p\beta$ 的非零线性关系。式 (5) 含原规范高度值、第二类周期及全局 Picard 配对；即使清去 $L_i$ 分母，它也没有变成该定理所排除的代数线性关系。没有已证的约化可以把这些原系数视为代数数或独立自由变量。

若改用 R785 的实际 Rosati 压缩，则仍必须同时代入
$$
 d_i=\lambda_{i,0}-2\Theta_{i,0},\qquad
 g_i=\lambda_{i,1}-2\Theta_{i,1},
$$
$$
 \Theta_{i,k}=
 \sum_\alpha\operatorname{Tr}\!\left(
  \mathfrak c_\alpha\boldsymbol\xi_{i,\alpha}^{*t}
  M_\alpha\mathbf z_{\alpha,k}\right).
 \tag{7}
$$
尤其
$$
 s_i=2T_i\lambda_{i,0}-\lambda_{i,1}
       +2\Theta_{i,1}-4T_i\Theta_{i,0}.
 \tag{8}
$$
原 $P_Y(c_1)$ 的常数列 $\mathbf z_{\alpha,0}$ 和切向列 $\mathbf z_{\alpha,1}$ 都在。仅证明某个原 $\eta_h$ 非零、某个极除子不平凡或某个 $g_i\ne0$，均没有直接否定式 (5)。

## 4. 极化及原除子规范的作用没有被扩大

R785 的 Rosati 关系保证原高度参数满足 $\mathfrak c_\alpha^*=\mathfrak c_\alpha$，并固定实际拉回极化 $M_\alpha$ 的次序。这给结构压缩，但不对这些 $\mathbb Q_p$ 值提供正负号或非零性。原次数零的 $h\in\ker\operatorname{Tr}(\kappa h)$ 也不构成一族全正方向。故不能用实极化或实 Néron–Tate 正定性否定式 (5)。

目前正在恢复的原 $\eta$、极理想和主函数数据是 R724 的真实局部求值所必需的代数输入；它们能固定原截面和刚性化常数，却不等于已求得式 (4)、(7) 的 $p$ 进对数与配对。原 Picard 因子、第二类周期、非 $p$ 项及因子 $2$ 仍必须在同一次源绑定的求值中保留。

允许的 $Y$ splitting 变化在整个 $\Lambda$ 内抵消；允许的 $F$ 相容 $A$ splitting 变化将 $s$ 加上 $Kv$ 中的向量。因此式 (2)、(5) 不变。这个不变性也不允许只调整高度矩阵而固定局部 $\lambda$，来人为改变式 (5) 的真伪。

## 5. 三层结论的准确边界

| 结论 | 当前依据 | 尚不能推出 |
|---|---|---|
| 原每个 $E_{ij}$ 逐盘非恒零 | R634 定理 634.3，原 NS 类与 BMS 深度符号 | 原 $c_1$ 二阶系数非零 |
| 某个 $[z^2]E_{ij}\ne0$ | 当且仅当原式 (5) 至少一式不成立，即 R785 的 $\mathscr T_p\ne0$ | $p$ 单位或整个深盘无根 |
| 原 $v_p(z)\ge4$ 非中心无共同零 | 需 R724 的有限 Bézout 不等式和原完整误差尾，或其他同等强的真实证书 | 不能只凭首项非零或固定 $p$ 有限性 |

文献中的算法也把简单根核验作为独立步骤；BDMTV Algorithm 3.12 与 Remark 3.14 没有把其通用有限性论证升级成指定点横截性定理。这个观察不证明本题有多重根，只说明不能从所核来源补出缺失的非零蕴含。

本次最终留下的实际问题正是式 (5)/(6)，连同其原来源表达式 (4)/(7)。没有得到新的 $\mathscr T_p$ 非零、赋值界、整盘 Bézout 证书或全 $p$ 排除。

## 核对来源

- [R634](../results/R634-CM-calibration-eliminates-actual-height-matrix.md)，§§5–8。
- [R682](../results/R682-common-CM-Abel-order-and-saturated-QC-jets.md)，§§2–4、§6。
- [R699](../results/R699-actual-height-finite-jets-and-complete-exterior-tail.md)，§§2、4、5.1–5.2、8。
- [R724](../results/R724-original-Chow-Heegner-height-matrices-and-canonical-jet-evaluation.md)，§§2、5–9。
- [R785](../results/R785-original-Rosati-block-height-compression-and-leading-exterior-class.md)，§§5–7。
- Amnon Besser, J. Steffen Müller, Padmavathi Srinivasan, *p-adic adelic metrics and Quadratic Chabauty I*, arXiv:2112.03873，2021；v4，2026-01-16。Theorem 7.9、Lemma 7.12、§7.3.1；[作者原文](https://arxiv.org/html/2112.03873v4)。
- Jennifer S. Balakrishnan, Netan Dogra, J. Steffen Müller, Jan Tuitman, Jan Vonk, *Quadratic Chabauty for modular curves: algorithms and examples*, Compositio Mathematica **159** (2023), 1111–1152，Algorithm 3.12、Remark 3.14；[原出版物](https://doi.org/10.1112/S0010437X23007170)。
