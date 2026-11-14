# O5 续进：有限谱靶集的真实可达分量

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

本笔记接续 R54 的有限靶集，未修改同步中的旧结果或共享 HANDOFF。完整新证明为 [R55](../results/R55-rational-bad-components-and-larger-qc-kernel.md)。它把“实际可达坏分量”从一个未识别的子集确定为素域超奇异不变量，并据此得到更大的真实零坏高度方向格。

## 1. 模型核对后的关键改变

最初考虑的充分性方案是：对每个 $\mathbb F_p$ 超奇异椭圆曲线作 $\mathbb Q_p$ 好约化提升，利用 Serre 的完整非分裂惯性 Cartan 得到模曲线局部点，再证明落在对应分量。核对 Edixhoven–Parent 原文后，采用了更直接的模型证明。

实际阅读原刊 Theorem 3.4（pp.1038–1039）、例外自同构的证明（pp.1040–1042）、Corollary 3.2 与 Figure 7 及证明（pp.1042–1044）。这给出以下完整链条。

1. 在未分歧基底的正规交叉模型中，每个超奇异 $j$ 恰有一个保留的重数 $1$ 末端 $F_j\simeq\mathbb P^1$。
2. 将被收缩的分量并集与每个 $F_j$ 只有一个交点。收缩到最小正则模型后，所有被收缩部分落到共同点 $P$，而 $F_j$ 去掉这个点同构到 $U_j$。
3. 因此每个几何 $U_j\simeq\mathbb A^1$。保留分量可能是正则化新增的例外曲线，不能称作分歧稳定模型中的原始 Drinfeld 尾分量。
4. 忘却 $j$ 在正规交叉模型上沿原构造延伸；在每条水平支链上常值。收缩在 $U$ 上是同构，所以 $j$ 在 $U_j$ 上仍常值为该标号，Frobenius 对分量的作用恰为 $j\mapsto j^p$。
5. R33 的 $p\in\mathfrak m_P^\rho$、$\rho>1$ 排除 $\mathbb Z_p$ 截面经过 $P$。所以全部 $\mathbb Q_p$ 点特化到这些光滑开集。

原文对 $j=0,1728$ 给不同支链，但每种最后仍只保留一个重数 $1$ 的末端，且只有一个边界点；没有遗漏其额外自同构。

## 2. 可达性现在是等价关系

设 $S_p$ 为 $\mathbb F_p$ 中的超奇异 $j$ 集。一个 $\mathbb F_p$ 光滑点只能落在 Frobenius 稳定的几何分量上，所以可达性推出 $j\in S_p$。

反过来，对 $j\in S_p$，正规化后的几何 $\mathbb P^1$ 及其唯一边界点下降到 $\mathbb F_p$。边界点唯一，故为有理点，正规化于是确为 $\mathbb P^1_{\mathbb F_p}$，且
$$U_j\simeq\mathbb A^1_{\mathbb F_p}.$$
其 $p$ 个有理点全部由光滑 Hensel 提升到 $\mathbb Q_p$ 点。因此
$$I_p=S_p,\qquad |U(\mathbb F_p)|=p|S_p|.$$
没有用某个未知高维局部函数判断可达性；它直接来自真实正则模型的几何。

## 3. 靶集数由类数控制

为核查素域超奇异计数，读取 Treneer (2017) 原刊 §3 的 equation (3.2)、Proposition 3.1、Theorem 3.2 及证明。该文用 Hilbert 类多项式给
$$H_{-4p}\equiv(S_p^{\rm lin})^2\pmod p$$
当 $p\equiv1\pmod4$；当 $p\equiv3\pmod4$ 时左边换为 $H_{-p}H_{-4p}$。比较次数，再计算导子 $2$ 的类群核，得到
$$s_p=|S_p|=
\begin{cases}
h(-4p)/2,&p\equiv1\pmod4,\\
2h(-p),&p\equiv3\pmod8,\\
h(-p),&p\equiv7\pmod8.
\end{cases}$$
R55 另用经典 Dirichlet 类数公式与一个周期后的 Abel 求和给出有效的 $O(\sqrt p\log p)$ 上界，不使用任何无效下界。

这使 R54 的坏靶集精确写成
$$\mathcal B_p=\{\beta_j:j\in S_p\},\qquad|\mathcal B_p|\le s_p.$$
不同分量的谱向量可能相同，所以只对向量数给上界；分量标签本身全部局部可达。

## 4. 真正增加的 QC 方程

R45 的原核令全部几何分量的 $k_j(F)$ 相等，保证整个 $U$ 的积分平凡化。QC 全局必要方程在坏 $p$ 处只会评价实际 $\mathbb Q_p$ 点，所以可以改为只要求
$$k_j(F)=k_{j_0}(F)\quad(j\in S_p),\qquad j_0\in S_p.$$
这个整数格记作 $\mathcal K_{p,\mathbb Q_p}$，完整证明给
$$\mathcal K_A\subseteq\mathcal K_{p,\mathbb Q_p},\qquad
\operatorname{rank}\mathcal K_{p,\mathbb Q_p}\ge a-s_p.$$
对这些方向，沿用 R54 的真实截面归一化、R47 的完整辅助高度和全局迹表示，所有非辅助局部项仍在实际局部点上恒零。因此它们给实际有理点必须满足的新增方程。R49 的真实 NS 与局部高度独立性对它们仍适用。

用 R54 的谱坐标表示，新的共同零点条件为
$$\Delta_\ell(x)\in\operatorname{span}\{\beta_j:j\in S_p\},$$
其右侧维数至多 $s_p-1$。完整离散目标仍为
$$\Delta_\ell(x)\in-\log_\ell(p)\mathcal B_p.$$
从新的核恢复这项离散条件，只需至多 $s_p-1$ 个补充方向。原来的全几何积分核也因 Frobenius 轨道数 $t_p=(n+s_p)/2$ 获得 $\operatorname{rank}\mathcal K_A\ge a-t_p$ 的下降改善。

没有声称两个核在每个水平都严格不同，也没有声称某个新方程已经排除一个已知非 CM 候选。它们的准确意义是：此前为取得“全几何积分平凡化”施加的一部分条件，在真正的 $\mathbb Q$ 上 QC 点值方程中不需要，可以保留更多真实独立方向。

## 5. 剩余共同根问题

每个坏分量都在 $\mathbb Q_p$ 上可达，这只说明有限靶集具有实际局部来源。辅助素数 $\ell$ 处的 $\Delta_\ell$ 仍含完整局部高度和全局 Mordell–Weil 数据。尚未证明其有限靶逆像只含 CM，也未证明跨素数或全局 Galois 约束能消去其余候选。O5 继续保持开放；R55 是完整的新局部算术接口，不能作为 Serre 一致性的收尾依据。

## 核验来源

- Edixhoven–Parent，*Documenta Mathematica* **29** (2024), 1017–1058，[原刊全文](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)，Theorem 3.4、Corollary 3.2、Figure 7、Remark 3.5。
- Treneer，*Research in the Mathematical Sciences* **4**, article 25 (2017)，[原刊全文](https://link.springer.com/article/10.1186/s40687-017-0115-z)，§3、Theorem 3.2。
- Burde，[作者数论讲义](https://homepage.univie.ac.at/Dietrich.Burde/papers/burde_71_ant.pdf)，§5.2，Corollary 5.2.5，核对类数公式的 $\pi$ 与单位因子；R55 自行证明余下有效估计。

最初检索到的 Deuring 1941 原文和其他二手类数计数只用于定位来源；R55 的计数输入直接落在上述可核对的已发表多项式恒等式上。
