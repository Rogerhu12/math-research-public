# Centered 文献复核与极小向量像的全指数非紧性

日期：2026-11-12（UTC+8）。会话分工：`centered_literature`，母会话 `Astra-ISP-e2cb8f94`。

**可信度与范围。** §§1–3 是来源状态与适用性核查。[R14](../results/R14-backward-minimal-images-all-exponents.md) 给出完整自含证明：对 R9 的具体正权 odometer，任意非零目标、任意固定相对误差的 backward-minimal-vector images 没有范数收敛子列，且允许所有趋于无穷的整数指数。本结论排除一个具体方法所需的强紧性；不证明该算子有或没有普通不变子空间，不算完成一般 ISP，也不声称文献新颖性。

## 1. JKP 2019 的准确获取状态

I. B. Jung, E. Ko, C. Pearcy, *Hyperinvariant subspaces for a class of quasinilpotent operators*, **Studia Mathematica 245** (2019), 289–296，DOI [10.4064/sm171209-18-1](https://doi.org/10.4064/sm171209-18-1)。

本轮复核了[出版社页](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/245/3/111414/hyperinvariant-subspaces-for-a-class-of-quasinilpotent-operators)及其正常 Download 链接。出版社明确要求机构订阅；本环境中下载链接重定向主页，没有取得文章。Ewha 的[机构记录](https://pure.ewha.ac.kr/en/publications/hyperinvariant-subspaces-for-a-class-of-quasinilpotent-operators/)仍只有书目和摘要。[ResearchGate 文章记录](https://www.researchgate.net/publication/327215654_Hyperinvariant_subspaces_for_a_class_of_quasinilpotent_operators)明确标注无全文。未向作者发送请求。

因此，**完整附加条件仍未核实，不能写成已适用或已排除**。摘要只说明使用 Paulsen–Pearcy–Petrović 1995 的 weakly-centered 结构定理，处理一个拟幂零子类；“centered”单独不等于全文的全部假设。1995 年原文的出版社摘要本身也说明存在额外技术假设。没有用其他来源的推测补写条件。

## 2. 两篇 2025–2026 一手资料的具体适用边界

### 2.1 Budzyński 2025 的不变子空间判据不适用于本模型

P. Budzyński, *Weakly centered weighted composition operators in $L^2$-spaces*, [arXiv:2510.19768](https://arxiv.org/abs/2510.19768)，[已核对正文](https://arxiv.org/html/2510.19768v1)，§5 **Proposition 22** 和 **Theorem 27**。

正文的有界判据需要

$$
E_{\phi,w}(h_{\phi,w})=h_{\phi,w},\qquad
h_{\phi,w}\circ\phi\le h_{\phi,w}
\quad\mu_w\text{-a.e.}
$$

后一个条件在该命题中用于推出 hyponormality，不能省略。同文 Theorem 27 给相应无界版本。注意引言中指向“Proposition 11”的旧编号与已读取正文编号不一致；此处使用正文实际编号。

以下是本模型内的直接计算，而不是外文定理的推测性套用。设

$$
(Af)(y)=w(y)f(y-1),\quad \phi(y)=y-1,
\quad w(y)=a_{v_2(y)}.
$$

Haar 保测性给

$$
h_{\phi,w}(y)=w(y+1)^2,
\qquad h_{\phi,w}\circ\phi(y)=w(y)^2.
$$

由于 $\phi$ 可逆，条件期望是恒等，所以第一个条件成立。第二个条件要求 $w(y)^2\le w(y+1)^2$。但当 $y$ 为奇数且 $y\ne-1$ 时，$w(y)=a_0$，$v_2(y+1)\ge1$，故

$$
w(y)^2=a_0^2>a_{v_2(y+1)}^2=w(y+1)^2.
$$

奇数集有测度 $1/2$，且 $w>0$ 几乎处处，所以不等式确实在正 $\mu_w$ 测度上失败。直接地，

$$
AA^*=M_{w(y)^2},\qquad A^*A=M_{w(y+1)^2};
$$

在奇数、偶数两集分别取支持向量，可见二者之差同时有正、负方向，$A$ 既非 hyponormal 也非 cohyponormal。

### 2.2 Type IV centered 不是可直接拆解的移位结论

P. Budzyński, *Centered weighted composition operators on $L^2$-spaces revisited*, [arXiv:2603.03594v2](https://arxiv.org/abs/2603.03594v2)，[已核对正文](https://arxiv.org/html/2603.03594v2)，§4、**Proposition 11**。

其分类中 type IV 指极分解相位是酉算子；Proposition 11 说明单射且值域稠密的有界 weighted-composition 算子属于此类。本文引言明确将 type IV 描述为向量值函数空间上的加权平移，不能改述成全部都是可数个经典双边加权移位的直和。

本模型的极分解是

$$
A=U M_{w(\cdot+1)},\qquad(Uf)(y)=f(y-1),
$$

且 $U$ 酉。因此 $A$ 本身就是 type IV。此命名与 R9 的单射、稠密值域性质相容，不额外给出非平凡闭不变子空间。

## 3. 最新来源状态与 Rosenblum 路线

- L. W. Marcoux, H. Radjavi, B. R. Yahaghi, Y. Zhang, *Fully non-zero matrices and generators of full algebras of operators*, [arXiv:2608.21154](https://arxiv.org/abs/2608.21154)，2026-08-21，注明将刊于 *Linear Algebra and its Applications*，DOI [10.1016/j.laa.2026.08.020](https://doi.org/10.1016/j.laa.2026.08.020)。其摘要仍明确把复可分无穷维 Hilbert 空间的 ISP 称为未解。
- M. T. Garayev, *On the solution of Kim, Pearcy and Shields problem and its consequences*, [arXiv:2607.16373v2](https://arxiv.org/abs/2607.16373v2)。2026-08-19 撤回说明明确说主定理 3.1 不正确；不是一般 ISP 的可用解答。
- J. Fang, B. Hou, C. Jiang, Y. Zhang, *The invariant subspace problem and Rosenblum operators II*, [arXiv:2610.11202](https://arxiv.org/abs/2610.11202)，2026-10-08。本轮取得原始 arXiv 搜索摘要，直接打开正文未成功，故不虚构正文定理编号。摘要报告 Sobolev disk algebra 的条件性不变子空间判据、ideal-property 归约、逆算子的一类秩一耦合情形；没有声称一般 ISP 已解决。

对本模型，可自含证明一个限制：若

$$
F_{f,g}(z)=\sum_{n\ge0}\langle A^n f,g\rangle z^n
$$

为有理函数，则 $F_{f,g}\equiv0$。事实上拟幂零性使它是整函数，整有理函数是多项式，因此存在 $N$ 使矩在 $n\ge N$ 时消失。R12 的 $A^{2^k}/\|A^{2^k}\|\to I/2$ 于 WOT，给任意固定 $j\ge0$：

$$
0=\lim_k\frac{\langle A^{2^k+j}f,g\rangle}{\|A^{2^k}\|}
=\frac12\langle A^jf,g\rangle.
$$

所以所有矩都为零。该结论没有构造非零 $f,g$；把目标改写为“找有理生成函数”在此不绕开全部矩消失的问题。

## 4. 本轮已证结果的完整证明

极小像的全指数定理、定量正距离、变化目标/误差的稳健形式、dyadic 精确弱极限与边界情形，已移至 [R14](../results/R14-backward-minimal-images-all-exponents.md)。该结果替换旧 open 中“任意目标/误差/非 dyadic 指数仍未处理”的状态。
