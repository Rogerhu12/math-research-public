# $E:y^2=x^3-17x$ 的根数与 CM 周期输入

会话：Astra-rank2-Sha / explicit_curve，2026-11-12（UTC+8）。本笔记给 CM 路线补齐两个可无条件使用的输入；代数秩的完整证明在 `results/R4-cm-rank-two-curve.md`。

## 1. 根数为 $+1$

该方程的判别式为 $\Delta=2^6\cdot17^3$，所以只需考虑 $2,17,\infty$；其余有限处为好约化，局部根数为 $+1$。

**在 $2$ 处。** 使用 Julie Desjardins, *Root number of twists of an elliptic curve*, Journal de théorie des nombres de Bordeaux **32** (2020), no. 1, 73–101，Lemma 3.8（公式在期刊 p.90；Lemma 3.9 是等价的周期性重述）。该公式专门用于 $y^2=x^3+tx$，其中 $v_2(t)=0$ 且 $t\equiv15\pmod{16}$ 时，局部根数为 $-1$。取 $t=-17$ 正好满足，故
$$
w_2(E)=-1.
$$

**在 $17$ 处。** $v_{17}(\Delta)=3<12$，该模型在 $17$ 处最小；$j(E)=1728$，故是潜在好约化。适用于剩余特征至少 $5$ 的局部公式给出
$$
w_{17}(E)=\left(\frac{-2}{17}\right)=1.
$$
也可直接应用 Desjardins 上述论文 Theorem 4.8 的证明中对 $v_p(t)\equiv1,3\pmod4$ 的公式；这里 $v_{17}(-17)=1$。最后一个 Legendre 符号为 $1$，例如 $7^2\equiv-2\pmod{17}$。

**在无穷处。** $w_\infty(E)=-1$。因此
$$
w(E)=w_\infty(E)w_2(E)w_{17}(E)=(-1)(-1)(1)=1.
$$
由椭圆曲线的模性及完成 $L$ 函数的函数方程，$\operatorname{ord}_{s=1}L(E,s)$ 为偶数。这已足以与 R4 的 $\operatorname{rank}E(\mathbb Q)=2$ 配合，满足 CLS Theorem 2.2 的奇偶条件；**这里没有推断解析秩恰为 $2$**。

原始发表全文：<https://www.numdam.org/item/JTNB_2020__32_1_73_0.pdf>；DOI：<https://doi.org/10.5802/jtnb.1112>。已直接核查 Lemma 3.8 和 Theorem 4.8；没有通过数据库根数字段替代证明。

## 2. 周期系数可取 $\alpha(E)=1$

沿用 Coates–Liang–Sujatha, *The Tate–Shafarevich group for elliptic curves with complex multiplication*（arXiv:0901.3832，2009）的记号：
$$
\mathcal L=\Omega_\infty\mathbb Z[i],\qquad
\Omega_\infty^+=\alpha(E)\Omega_\infty.
$$
该文 §3，式 (53) 后（原文 p.16），明确写出：对 $E_D:y^2=x^3-Dx$，当 $D>0$ 时可取 $\alpha(E_D)=1$；当 $D<0$ 时则取 $1+i$。因此这里 $D=17$，$\alpha(E)=1$，没有额外要排除的素数。原始全文：<https://arxiv.org/pdf/0901.3832>。

这里也可给出直接的周期格说明。对实微分 $\omega=dx/(2y)$，其周期格 $\mathcal L$ 同时在乘 $i$ 和复共轭下稳定。由于 $\mathbb Z[i]$ 是主理想环，写 $\mathcal L=\Omega\mathbb Z[i]$，且 $\bar\Omega=u\Omega$，其中 $u\in\{\pm1,\pm i\}$。三个非零二阶点的横坐标为 $0,\sqrt{17},-\sqrt{17}$，全部为实数，所以共轭在 $\mathcal L/2\mathcal L$ 上为恒等。

在 $\mathbb Z[i]/2\mathbb Z[i]$ 上，共轭本身为恒等，而共轭作用在上述基底中还须乘 $u$；若 $u=\pm i$，则它会交换 $1$ 和 $i$，不为恒等。因此 $u=\pm1$，乘以一个高斯单位后可令 $\Omega>0$ 为实数。这时
$$
\mathcal L\cap\mathbb R=\Omega\mathbb Z,
$$
所以最小正实周期正好是 $\Omega$，即 $\alpha(E)=1$。

## 3. 可供后续直接使用的素数范围

结合 R4、根数与周期系数，对所有
$$
p\equiv1\pmod4,\qquad p\ne17,
$$
CLS Theorem 2.2 中关于好约化、$p$ 与单位根数 $4$ 互素、$p$ 在 $\mathbb Q(i)$ 分裂、$p\nmid\alpha(E)$ 及解析/代数秩同奇偶的条件均已满足。

剩下的是该定理要求的特殊值估计
$$
v_p\!\left((\Omega_\infty^+)^{-p}L(\bar\psi_E^{\,p},p)\right)<4.
$$
本笔记没有证明这个不等式对无穷多个 $p$ 成立，不能把有限范围计算补成无穷结论。
