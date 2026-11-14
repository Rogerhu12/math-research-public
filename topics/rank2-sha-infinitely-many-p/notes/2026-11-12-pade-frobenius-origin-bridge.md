# 从固定周期截断到单位元：无精度损失的 Padé 桥

**可信度：以下重构及公式已证明。** 日期：2026-11-12。本文继续 R29。它补充的是一个必要的变量范围转换：R29 的仿射多项式近似不能直接在 $X=\infty$ 取倒数，但可以先重构同源的分子、分母，再合法地恢复 $t=-1/X$ 在 $O$ 处的全部形式系数。

## 1. 为什么需要重构

设 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$。R29 使用
$$
\varphi_p(X)=X\circ[\pi],\qquad
\mathscr L(X)=\int_0^X(1+u^4/68)^{-1/2}\,du.
$$
其多项式模同余成立在 $X$ 仿射部分的 $p$-进完备化。无穷远恰是核点在特殊纤维中合并的位置；把一个多项式近似直接代入 $X=-1/t$ 再取倒数，不能保证它仍具有真实同源的 $t$-进展开。例如真实 $[\pi](t)$ 的线性项为 $\pi t$，而仿射多项式的无穷远最高次项并不直接保留这一信息。

R29 已证明真实同源有唯一规范化表示
$$
\varphi_p=N/D,\qquad D(0)=1,\qquad
\deg N\le p,\quad\deg D\le p-1,
$$
$$
N\equiv X^p\pmod p,\qquad D\equiv1\pmod p.
\tag{1}
$$
本文利用这些 degree 信息恢复分母，而不是对仿射近似直接求倒数。

## 2. 一个模 p 为恒等矩阵的重构

写真实 Taylor 展开
$$
\varphi_p(X)=\sum_{n\ge0}a_nX^n.
$$
给定任意精度 $s\ge1$，只需知道 $a_n\bmod p^s$ 至 $n=2p-1$。写
$$
D(X)=1+\sum_{j=1}^{p-1}d_jX^j.
$$
由 $\deg(D\varphi_p)\le p$，有方程
$$
\sum_{j=1}^{p-1}a_{p+i-j}d_j=-a_{p+i},
\qquad 1\le i\le p-1.
\tag{2}
$$
其系数矩阵
$$
M_{ij}=a_{p+i-j}
$$
满足
$$
M\equiv I_{p-1}\pmod p,
\tag{3}
$$
因为 $\varphi_p\equiv X^p\bmod p$。因此 $M\in\operatorname{GL}_{p-1}(\mathbb Z_p)$，式 (2) 唯一确定 $D\bmod p^s$，没有除以 $p$ 或其他精度损失。随后
$$
N=[D\varphi_p]_{\le p}\pmod{p^s}
\tag{4}
$$
恢复分子。

这里只需前 $2p-1$ 次系数，不必将 R29 的仿射近似全部保留到约 $5p$ 次。因为真实 $N,D$ 已存在并满足 (2)，模 $p$ 可逆性也保证重构出的解就是它们的所需近似，而不是某个无法控制的其他 Padé 解。

## 3. CM 对称性将矩阵降到 $(p-1)/4$ 维

令 $r=(p-1)/4$。$[i]$ 在四次模型上作用为 $X\mapsto-iX$，所以
$$
\varphi_p(-iX)=-i\varphi_p(X).
$$
规范化的分子分母互素且 $D(0)=1$，其唯一性给出
$$
D(-iX)=D(X),\qquad N(-iX)=-iN(X).
$$
于是
$$
D=1+\sum_{j=1}^r d_jX^{4j},
$$
而 $N$ 只含次数 $1\bmod4$ 的项。重构方程现在准确变成
$$
\sum_{j=1}^r a_{p+4(i-j)}d_j=-a_{p+4i},
\qquad1\le i\le r.
\tag{5}
$$
这个 $r\times r$ 矩阵仍模 $p$ 为恒等矩阵。

## 4. 模 p4 只需要 R29 的一个固定级数

当只保留次数 $n\le2p-1$ 时，$\mathscr L$ 的特殊分母项 $X^p/p$ 在任意乘积中至多出现一次。故
$$
v_p([X^n]\pi^5\mathscr L^5/680)\ge4.
$$
R29 的更高奇次项也达到至少同样的精度。因此
$$
\boxed{\quad
a_n\equiv\eta_p\pi[X^n]\mathscr L(X)\pmod{p^4},
\qquad 0\le n\le2p-1.
\quad}
\tag{6}
$$
模 $p^5$ 时需要加上 $\eta_p\pi^5\mathscr L^5/680$，仍只用 R29 的两个固定级数。结合 §2–3，式 (6) 已经足以恢复整个 $N,D\bmod p^4$，从而恢复整个同源在 $O$ 处的形式展开模 $p^4$。

### 4.1 分母的明确三项式，且其中的 $\pi$ 完全消去

记
$$
\ell_n=[X^n]\mathscr L(X),\qquad
\ell=p\ell_p\in\mathbb Z_p^\times.
$$
在以下范围内，除了 $\ell_p$ 以外，所有 $\ell_n$ 都 integral。定义
$$
A_{ij}=
\begin{cases}
\ell_{p+4(i-j)},&i\ne j,\\
0,&i=j,
\end{cases}
\qquad
b_i=\ell_{p+4i},
\qquad 1\le i,j\le r.
\tag{7}
$$
$A$ 与 $b$ 的所有项都属于 $\mathbb Z_p$。$\ell$ 是单位，因为
$$
\ell=\frac{(-1)^r\binom{2r}{r}}{272^r}
$$
的二项式分子没有 $p$ 因子。

以式 (6) 的近似代入 (5)，其矩阵和右侧分别为
$$
\eta_p\pi\left(\frac{\ell}{p}I_r+A\right),
\qquad-\eta_p\pi b.
$$
共同因子可以准确消去。得到一个整且可逆的归一化系统
$$
\left(I_r+\frac p\ell A\right)d=-\frac p\ell b.
$$
这里消去 $\pi$ 不损失最终精度：所构造近似矩阵与真实矩阵相差 $p^4$，两者均为整单位矩阵；其解相差 $p^4$。等价地，可先在 $\mathbb Q_p$ 中准确求近似系统的解，再用 §2 的整可逆性比较。

将逆矩阵按 $pA/\ell$ 展开，并注意右侧已有一个 $p$ 因子，得到
$$
\boxed{\quad
d\equiv-\frac p\ell b
+\frac{p^2}{\ell^2}Ab
-\frac{p^3}{\ell^3}A^2b
\pmod{p^4}.
\quad}
\tag{8}
$$
因此模 $p^4$ 的分母只需要固定 $\mathscr L$ 的系数及两次有限 Toeplitz 矩阵乘法；不需要未知的同源系数，也不需要先知道 $\pi$。

分子可用 §2 的整系数公式准确恢复。等价地，对于任意 $D\bmod p^4$ 的整提升 $\widetilde D$，
$$
N\equiv\eta_p\pi[\widetilde D\mathscr L]_{\le p}\pmod{p^4}.
\tag{9}
$$
在这里需要的次数内，$\pi\mathscr L$ 的系数均整，特殊的分母 $p$ 已被 $\pi$ 抵消。因此更换 $\widetilde D$ 的模 $p^4$ 提升不会损失精度。

## 5. 现在可以无损地回到 t=0

取通过上文得到的任意整提升 $\widetilde N,\widetilde D$，仍保持所需次数界。真实 $t$-同源为
$$
[\pi](t)=-\frac{D(-1/t)}{N(-1/t)}
=-\frac{t^pD(-1/t)}{t^pN(-1/t)}.
\tag{10}
$$
分母 $t^pN(-1/t)$ 在 $t=0$ 的常数项是 $(-1)^p$ 乘 $N$ 的最高次系数；由 (1)，它是 $\mathbb Z_p$ 单位。分子因 $\deg D\le p-1$ 而被 $t$ 整除。

因此在整形式级数环 $\mathbb Z_p[[t]]$ 中，除法合法且对系数的 $p$-进精度连续：
$$
\boxed{\quad
[\pi](t)\equiv
-\frac{t^p\widetilde D(-1/t)}
{t^p\widetilde N(-1/t)}
\pmod{p^s}.
\quad}
\tag{11}
$$
所有阶数的系数均保持同一个模 $p^s$ 精度，不会因为无穷远处的线性项含 $\pi$ 而再次除以 $p$。

于是，原固定 $\Phi(t)$ 的复合 $\Phi([\pi](t))$ 及其有理对数导数可在 $O$ 处准确恢复。若再计算 Coleman 差
$p^{-1}\log(\Phi(t)^p/\Phi([\pi](t)))$，其中显式的除以 $p$ 当然需要提前多保留一位；本文的“无精度损失”专指 Padé 重构与式 (11) 的坐标转换，不把这另一次除法免费忽略。

## 6. 得到的计算输入和未得到的跨素数结论

R29 的仿射公式现在有一条完整、合法的回到单位元的通路。模 $p^4$ 的同源本身只需要一个固定 D-finite 级数，矩阵始终模 $p$ 为恒等矩阵，分母还有式 (8) 的三项展开。

但矩阵大小 $r=(p-1)/4$ 仍随 $p$ 增长，且原 $\Phi$ 的两个目标矩还需要经过复合、对数及规定次数的系数提取。本文没有把同源的确定性重构当作 $\lambda_p$、$\lambda_{2p-1}$ 的跨素数非零证明，也没有把这些量的已知首层相消删除。下一算术问题仍是原始 $\Phi$ 的归一化常数项与一次项是否在无穷多个 $p$ 不同时落入 R24–R26 给出的理想。

## 依赖

- R29：两个固定级数的低阶估值与真实同源的 degree 界。
- 原始 $\Phi$ 及 Coleman 差采用 R19 和完整范数塔笔记的规范。
- 本文 §2–5 已给出重构矩阵、可逆性、精度与原点坐标转换的完整证明。
