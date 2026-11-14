# R48：Odometer 差异界、可测换权与双向增长的路线边界

日期：2026-11-12（UTC+8）。分工：`literature`，母会话 `Astra-ISP-0c017065`。

**可信度与范围。** §§1–2、§3.1 是一手来源核查；§§3.2–5 给出自含的已证明路线限制。没有得到当前 odometer 的普通不变子空间，也没有解决一般 Hilbert ISP。不主张下列初等命题具有文献新颖性。

## 1. 完整 ISP 状态与来源边界

本轮重新打开了 Laurent W. Marcoux、Heydar Radjavi、Bamdad R. Yahaghi、Yuanhang Zhang 的原始 arXiv 记录：*Fully non-zero matrices and generators of full algebras of operators*，[arXiv:2608.21154v1](https://arxiv.org/abs/2608.21154v1)，2026-08-21，关联 DOI [10.1016/j.laa.2026.08.020](https://doi.org/10.1016/j.laa.2026.08.020)。其摘要仍明确以未解决的 Hilbert ISP 为相关背景。结合旧核查，本轮没有找到可直接采用的完整解答。

这是检索范围内的状态报告，不是对所有可能文献的穷尽证明。OpenAI 的超不变子空间结论及指定有限因子内的不变投影结论，仍不能代替普通不变子空间问题。

Fang–Hou–Jiang–Zhang 的 *The invariant subspace problem and Rosenblum operators II*，此前记录的 [arXiv:2610.11202](https://arxiv.org/abs/2610.11202)，本轮再次尝试 abstract、PDF 和 HTML 入口，均未取得正文。因此没有新增任何据其全文定理作出的推论，也不改变旧笔记中“只核对摘要”的状态。

## 2. JKP 2019 的全文仍未取得

I. B. Jung、E. Ko、C. Pearcy，*Hyperinvariant subspaces for a class of quasinilpotent operators*，**Studia Mathematica 245** (2019), 289–296，DOI [10.4064/sm171209-18-1](https://doi.org/10.4064/sm171209-18-1)，在线发表日期 2018-08-24。

本轮具体检查了：

- [出版社文章页](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/245/3/111414/hyperinvariant-subspaces-for-a-class-of-quasinilpotent-operators)：明确列出机构订阅要求；其正常 Download 链接仍跳回网站首页。
- [Ewha 原始机构库](https://dspace.ewha.ac.kr/handle/2015.oak/248118)：明确无附属文件。
- [作者文章记录](https://www.researchgate.net/publication/327215654_Hyperinvariant_subspaces_for_a_class_of_quasinilpotent_operators)：仅提供索取全文入口，没有公开全文；本轮未向作者发送消息。
- Crossref 与 OpenAlex 的 DOI 元数据：未列出任何开放的作者稿或全文仓储位置。该项只用于记录获取状态，不作为定理条件的来源。

继续追溯其引用的 V. Paulsen、C. Pearcy、S. Petrović，*On centered and weakly centered operators*，**Journal of Functional Analysis 128** (1995), 87–101，DOI [10.1006/jfan.1995.1024](https://doi.org/10.1006/jfan.1995.1024)。[作者上传记录](https://www.researchgate.net/publication/251423632_On_Centered_and_Weakly_Centered_Operators)确实标有 Vern Paulsen 于 2017-11-11 上传的全文，但本环境取得的下载入口失败。旧作者稿地址 `http://homepages.wmich.edu/~petrovic/research/r3.pdf` 也返回连接错误；出版社的正文入口未取得原文。

**准确结论仍是：JKP 的完整附加条件未核实。** 既不宣称它适用于当前 $A$，也不宣称已经排除了它。不能把所有 centered 算子都说成可数个经典双边移位的直和。

## 3. 新核对的 discrepancy 定理

### 3.1 一手定理及其权假设

George Androulakis、Antoine Flattot，*Hyperinvariant subspaces for weighted composition operators on $L^p([0,1]^d)$*，**Journal of Operator Theory 66:1** (2011), 125–144；[出版社完整原文](https://www.theta.ro/jot/archive/2011-066-001/2011-066-001-004.pdf)。本轮读取原 PDF 文本，未将 PDF 加入仓库，也未逐页渲染。

其 **Theorem 2.1（p.127）** 假定 $\tau$ 是双射遍历变换，且权属于式 (2.1) 的有限广义多项式类：

$$
v(x)=C\prod_{i=0}^{l}\bigl(\sigma_i(x-x_i)\bigr)^{s_i},
\qquad s_i>0,
\qquad \sigma_i(t)=t\ \text{或}\ |t|.
$$

若轨道的统一 discrepancy 满足

$$D_n=O\bigl((\log n)^{-3-\varepsilon}\bigr)\qquad(\varepsilon>0),$$

则相应加权复合算子有非平凡超不变子空间。证明中的双向函数演算先除以正的谱半径，随后使用满足 $\sum \omega(n)/n^2<\infty$ 的 Beurling 权；这一归一化步骤就在同页。

下面分别核查当前模型的动态部分与权部分。它们不是一个含混的“正则性条件”。

### 3.2 Odometer 的统一 discrepancy 足够好

设 $y=\sum_{j\ge0}b_j(y)2^j\in\mathbb Z_2$，定义二进位倒序坐标

$$\xi(y)=\sum_{j\ge0}b_j(y)2^{-j-1}\in[0,1].$$

该坐标保 Haar 测度到 Lebesgue 测度；除去二进展开不唯一的零测集合后，它给出概率空间同构。令

$$
\mathcal D_N(y)=\sup_{0\le a<b\le1}
\left|\frac1N\#\{0\le k<N:\xi(y-k)\in[a,b)\}-(b-a)\right|.
$$

**命题 3.1。** 对所有 $y\in\mathbb Z_2$ 和 $N\ge1$，有

$$
\mathcal D_N(y)\le\frac{2s_2(N)}{N}
\le\frac{2(1+\lfloor\log_2N\rfloor)}{N},
$$

其中 $s_2(N)$ 是 $N$ 的二进位中 $1$ 的个数。

**证明。** 长度为 $2^m$ 的任意连续整数平移块，恰好经过模 $2^m$ 的每个剩余类一次。其倒序坐标在每个长度 $2^{-m}$ 的闭二进网格区间中各有一个带指定标签的样本。对任意 $t\in[0,1]$，计数 $\xi<t$ 与 $2^mt$ 的差的绝对值至多 $1$：全部严格位于 $t$ 左侧的网格单元必贡献一个样本，至多只有包含 $t$ 的单元以及端点归属需要决定。允许两个带标签的样本落在同一网格端点不改变这个界。对区间 $[a,b)$，两次初始区间计数相减，误差至多 $2$。

把 $N$ 写成互异二幂之和，并依次把长度 $N$ 的轨道块切成这些长度的连续块。每块的未归一化误差至多 $2$，共 $s_2(N)$ 块，得到结论。正向平移同样成立。证毕。

因此，在自然满测度的区间模型上，所需的 discrepancy 衰减没有障碍。这里给出了原概率空间上全部点的计数界，没有假设某个未指定的零测集合延拓会保持其他性质。

### 3.3 权假设严格失败

当前权由 [R9](../results/R9-radial-odometer-and-nilpotent-approximants.md)、[R13](../results/R13-all-normalized-powers-and-binary-cluster-set.md) 给出：

$$
w(y)=a_{v_2(y)},\quad a_j=e^{-L_j},\quad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3},
\quad w(0)=0.
$$

因为 $\mu\{v_2(y)=j\}=2^{-j-1}$，

$$\int\log w\,d\mu=-\sum_{j\ge0}2^{-j-1}L_j=-\infty.$$

但每个非零有限广义多项式权都有 $\log|v|\in L^1[0,1]$，因为对每个 $c\in[0,1]$，$\log|x-c|$ 的绝对值可积，有限线性组合仍可积。这与任何保测坐标变换下的当前权都不相容。

所以不能仅凭 odometer 的良好 discrepancy 应用 Theorem 2.1。下一节进一步排除了用任意可测乘法换权来修复这个假设。

## 4. 任意有限可测乘法换权都不能使对数可积

**命题 4.1。** 设 $(X,\mu)$ 为概率空间，$\phi$ 为可逆保测变换，$w>0$ 几乎处处，$w\in L^\infty$。设

$$Tf=w(f\circ\phi)$$

在 $L^2(\mu)$ 上拟幂零。不存在满足 $0<|h|<\infty$ 几乎处处的可测函数 $h$，使

$$v=w\frac{h\circ\phi}{h},\qquad\log|v|\in L^1(\mu).$$

**证明。** 置 $\ell=\log|h|$，它是几乎处处有限的实可测函数，不要求可积。对几乎所有 $x$，令

$$
w_n(x)=\prod_{k=0}^{n-1}w(\phi^kx),\qquad
s_n(x)=\frac1n\sum_{k=0}^{n-1}\log|v(\phi^kx)|.
$$

逐项相加给出

$$s_n(x)=\frac{\log w_n(x)}n+
\frac{\ell(\phi^nx)-\ell(x)}n.\tag{4.1}$$

由于 $\phi$ 可逆且保测，复合算子 $f\mapsto f\circ\phi^n$ 是酉的，并且

$$\|T^n\|=\|w_n\|_\infty.$$

于是拟幂零性给

$$\frac{\log w_n(x)}n\le\frac{\log\|T^n\|}{n}\longrightarrow-\infty,$$

并且右边与 $x$ 无关。

对每个 $\epsilon>0$，保测性与 $\ell$ 几乎处处有限给出

$$
\mu\{|\ell\circ\phi^n|>n\epsilon\}
=\mu\{|\ell|>n\epsilon\}\longrightarrow0.
$$

另有 $\ell/n\to0$ 几乎处处。因此 (4.1) 的最后一项在测度下趋零，故 $s_n\to-\infty$ 于测度。

另一方面，若 $\log|v|\in L^1$，保测性及三角不等式给

$$\|s_n\|_1\le\|\log|v|\|_1=:K\quad(n\ge1).$$

取 $R>2K$；Markov 不等式给 $\mu\{|s_n|>R\}<1/2$，但 $s_n\to-\infty$ 于测度迫使这个概率趋于 $1$，矛盾。证毕。

**说明。** 证明不使用遍历定理，也不要求 $\log|h|$ 可积或 $h,h^{-1}$ 有界。对当前遍历 odometer，若一个非零可测 $h$ 满足 $wh\circ\phi=vh$，且 $v$ 非零几乎处处，则其零集是模零不变集，从而 $h$ 自动非零几乎处处。于是连这种更宽的乘法交织也不能把当前 $A$ 与对数可积权联系起来。

该命题只排除乘法型换权。没有把它扩大成“任意有界交织均不存在”。

## 5. 双向 Beurling 控制在每个非零向量上都失败

**命题 5.1。** 若 $T$ 是非零 Hilbert 空间上的单射拟幂零算子，且

$$0\ne f\in\bigcap_{n\ge1}\operatorname{Ran}T^n,$$

则对任意 $c\ne0$，记 $S=cT$，有

$$\lim_{n\to\infty}\frac1n\log\|S^{-n}f\|=+\infty.$$

这里 $S^{-n}f$ 指唯一的逆像，不是声称 $S^{-1}$ 为处处定义的有界算子。

**证明。** 从 $f=S^n(S^{-n}f)$ 得

$$\|S^{-n}f\|\ge\frac{\|f\|}{|c|^n\|T^n\|}.$$

取对数并除以 $n$，拟幂零性使右侧趋于 $+\infty$。证毕。

特别地，不存在非零这样的 $f$ 与非负权 $\omega$，同时满足

$$\|S^{-n}f\|\le Ce^{\omega(n)},\qquad
\sum_{n\ge1}\frac{\omega(n)}{n^2}<\infty.$$

否则由上式可知所有充分大的 $n$ 有 $\omega(n)\ge n$，从而级数至少含一段调和级数而发散。对当前 $A$，R44 已证明各幂值域的交稠密；本命题说明其中任何非零向量都不能满足上述双向非拟解析控制。这是 Androulakis–Flattot 型函数演算在零谱半径情形的真实障碍，不能靠选一个更快衰减的逆像向量消除。

## 6. 保留的未解事项

1. JKP 2019 完整额外假设仍缺原文，没有判定它是否覆盖当前 $A$。
2. 本轮没有找到关于当前超快径向权、Haar 表示下的 scalar odometer 普通不变格的公认现成定理。
3. §§4–5 是具体路线的排除，既不证明 $\ker D$ 非零，也不证明 $D$ 单射或值域稠密；主线仍是直接解决 R43–R44 的实际核方程或一般矩消失问题。
