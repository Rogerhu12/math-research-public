# R248 附录：真实对数噪声相似的尖锐平方可和阈值

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf；根代理提出以实际归一化幂 $N_j$ 的收缩乘积测试必要性。

状态：完整证明。[前一相似附录](R248-appendix-square-summable-log-noise-and-bounded-similarity.md)已经证明 $a=-\log\delta\in\ell^2$ 时整个实际表示有界相似。本稿在含 R248 原强阻尼的明确局部变形类中证明反向必要性，并给有限头相似条件数的真实乘积下界。不从相似失败推出慢符号有核。

## 1. 局部变形的明确范围

设
$$
0<\delta_j\le1,\qquad
\delta_j\ge c(j+2)^{-s}
\quad(j\ge0),
\qquad 0<c\le1,\quad 0\le s<\infty.
\tag{1.1}
$$
写
$$
a_j=-\log\delta_j\ge0,\qquad
D_\delta\chi_F=\delta_F\chi_F,\qquad
\delta_F=\prod_{j\in F}\delta_j.
$$
这里不预设 $a\in\ell^2$。
$D_\delta$ 仍为有界、单射、稠密像的正收缩。

原实际归一化幂满足
$$
N_j=\frac{A^{2^j}}{d_j},\qquad \|N_j\|=1,
\qquad
N_j=\sum_{r\ge j}\frac{\alpha_r}{\alpha_j}
E_j^*\cdots E_{r-1}^*E_r,
$$
$$
\frac{\alpha_r}{\alpha_j}
=\prod_{\ell=j}^{r-1}\eta_\ell
\le e^{-770\,16^{r-1}}\quad(r>j).
\tag{1.2}
$$
$E_j$ 是原物理单个位的秩一平方零矩阵。

按 R248 §3 对 (1.2) 的每个局部项作有限位噪声相似。
长度 $r-j+1$ 的条件数至多
$$
\prod_{\ell=j}^{r}\delta_\ell^{-1}
\le c^{-(r-j+1)}(r+2)^{s(r-j+1)}.
\tag{1.3}
$$
(1.2) 支付所有这些成本，故得到真实有界 $N_{j,\delta}$，满足
$$
D_\delta N_j=N_{j,\delta}D_\delta.
\tag{1.4}
$$
特别，$A_\delta=d_0N_{0,\delta}$ 有界。
由 (1.4)、$D_\delta$ 稠密像以及原归一化幂关系，
$$
\boxed{
N_{j,\delta}=A_\delta^{2^j}/d_j.
}
\tag{1.5}
$$
所以这些真实变形算子两两交换。
没有另改 $d_j$，也没有用纯模型替代实际幂。

## 2. 每位纯范数准确为 $\cosh a_j$

在 Walsh 单个位基 $(1,\chi_j)$ 中，
$$
E_j=\frac12
\begin{pmatrix}
1&1\\-1&-1
\end{pmatrix}.
$$
因此原局部噪声给
$$
E_{j,\delta}
=\frac12
\begin{pmatrix}
1&\delta_j^{-1}\\
-\delta_j&-1
\end{pmatrix}.
\tag{2.1}
$$
它是秩一矩阵，可写成
$\frac12(1,-\delta_j)^{\mathsf T}(1,\delta_j^{-1})$。
其算子范数准确为
$$
\boxed{
n_j:=\|E_{j,\delta}\|
=\frac12\sqrt{(1+\delta_j^2)(1+\delta_j^{-2})}
=\frac{\delta_j+\delta_j^{-1}}2
=\cosh a_j\ge1.
}
\tag{2.2}
$$

这些纯位算子分别作用在不同张量因子上。
对每个有限位集 $F$，
$$
\boxed{
\left\|\prod_{j\in F}E_{j,\delta}\right\|
=\prod_{j\in F}\cosh a_j.
}
\tag{2.3}
$$
这里选用实际 $N_j$ 的纯主项。
普通固定参数预解式并没有 (2.2) 所需的单位基准，不能替换这个测试。

## 3. 实际 carry 的可和相对误差

由 (1.2)--(1.3)，可取
$$
\varepsilon_j=
\sum_{r\ge j+1}
c^{-(r-j+1)}(r+2)^{s(r-j+1)}
e^{-770\,16^{r-1}},
$$
使
$$
\|N_{j,\delta}-E_{j,\delta}\|\le\varepsilon_j.
\tag{3.1}
$$
不需要这些误差在低位已经小；只需支付其尾。

令
$$
b_r=c^{-(r+1)}(r+2)^{s(r+1)}e^{-770\,16^{r-1}}
\quad(r\ge1).
$$
由于 $c\le1$、$s\ge0$，有
$$
\varepsilon_j\le\sum_{r\ge j+1}b_r,
\qquad
\sum_{j\ge0}\varepsilon_j
\le\sum_{r\ge1}r\,b_r<\infty.
\tag{3.2}
$$
最后收敛由
$-\!770\,16^{r-1}+O(r\log r)$ 的指数给出。

更一般，下文只需要
$$
\sum_j\frac{\|N_{j,\delta}-E_{j,\delta}\|}{\cosh a_j}<\infty
\tag{3.3}
$$
及实际关系 (1.5)；(1.1) 是一个可直接检验且保证这些条件的范围。
本稿不把 (3.3) 免费扩到任意已定义的有界变形。

取足够大的固定 $J$，使
$$
\sum_{j\ge J}\frac{\varepsilon_j}{n_j}
\le\log(3/2).
\tag{3.4}
$$
对任意有限 $F\subseteq[J,\infty)$，按固定次序展开乘积差，
无需实际因子与纯因子混合交换，就有
$$
\begin{aligned}
\left\|
\prod_{j\in F}N_{j,\delta}
-\prod_{j\in F}E_{j,\delta}
\right\|
&\le
\prod_{j\in F}(n_j+\varepsilon_j)-\prod_{j\in F}n_j\\
&=
\left(\prod_{j\in F}n_j\right)
\left[\prod_{j\in F}
\left(1+\frac{\varepsilon_j}{n_j}\right)-1\right]\\
&\le\frac12\prod_{j\in F}n_j.
\end{aligned}
\tag{3.5}
$$
结合 (2.3)，得到保全部 carry 的准确两向乘积预算
$$
\boxed{
\frac12\prod_{j\in F}\cosh a_j
\le
\left\|\prod_{j\in F}N_{j,\delta}\right\|
\le
\frac32\prod_{j\in F}\cosh a_j
\quad(F\subseteq[J,\infty)\text{ 有限}).
}
\tag{3.6}
$$
误差相对于整个纯乘积支付，而不是把可和的单项绝对误差在长乘积中免费相加。

## 4. 相似必要性与尖锐充要条件

若存在任意有界可逆 $B$，满足
$$
A_\delta=B^{-1}AB,
$$
则由 (1.5)，
$$
\prod_{j\in F}N_{j,\delta}
=B^{-1}\left(\prod_{j\in F}N_j\right)B.
$$
原每个 $\|N_j\|=1$，故
$$
\left\|\prod_{j\in F}N_{j,\delta}\right\|
\le\|B^{-1}\|\|B\|=:\kappa(B).
\tag{4.1}
$$
这里不要求 $B$ 固定真空、为乘积算子，或属于任何交换子。

由 (3.6)--(4.1)，
$$
\boxed{
\kappa(B)\ge
\frac12\exp\!\left(\sum_{j\in F}\log\cosh a_j\right)
\quad(F\subseteq[J,\infty)\text{ 有限}).
}
\tag{4.2}
$$
因此相似存在必须满足 $\sum_j\log\cosh a_j<\infty$。

对任意非负序列，
$$
\boxed{
\sum_j\log\cosh a_j<\infty
\Longleftrightarrow
a\in\ell^2.
}
\tag{4.3}
$$
确实，$\log\cosh x\le x^2/2$ 给充分性。
反向，和有限先迫 $a_j\to0$；
对 $0\le x\le1$，
$$
\log\cosh x\ge\log(1+x^2/2)\ge x^2/3,
$$
故平方和有限。
这也包含 $a_j$ 不趋零或无界的情况：此时左侧必发散。

结合前一附录已经支付的充分性，得到：

**定理4.1。** 对满足 (1.1) 的原真实局部噪声变形，
$$
\boxed{
A_\delta\text{ 与 }A\text{ 有界相似}
\Longleftrightarrow
(-\log\delta_j)\in\ell^2.
}
\tag{4.4}
$$
在成立时，同一个有界单位实现整个 $A'$ 的实际噪声表示。
在不成立时，甚至只要求 $A_\delta$ 与 $A$ 相似也不可能；
这不只是某个指定热构造的条件数失控。


此外，(4.4) 等价于存在一个常数 $C<\infty$，使全部标量多项式满足
$$
\|p(A_\delta)\|\le C\|p(A)\|.
\tag{4.5}
$$
充分方向由已证共同相似给出；必要方向对
$p_F(z)=z^{\sum_{j\in F}2^j}/\prod_{j\in F}d_j$
使用 (3.6) 以及 $\|\prod_{j\in F}N_j\|\le1$ 即得。
因此当 $a\notin\ell^2$ 时，连原多项式范数到变形多项式范数的一致控制也不存在。

## 5. 有限头逼近也付出同一条件数

对 $p>J$，定义有限头噪声
$$
\delta_j^{[p]}=
\begin{cases}
\delta_j,&j<p,\\
1,&j\ge p.
\end{cases}
$$
其对角算子有有界逆，故 $A_{\delta^{[p]}}$ 确实与 $A$ 相似。
但每个实现该相似的有界单位 $B_p$ 都受到定量下界。

因为 $\delta_j^{[p]}\ge\delta_j$，用于 (3.1) 的每项局部条件数上界不增加，所以同一个 $\varepsilon_j$ 仍控制实际 carry 误差；而对 $j<p$，纯范数 $n_j$ 保持不变。
所以 (3.4) 的同一 $J$ 对所有 $p$ 和 $F=[J,p)$ 仍足够，得到
$$
\boxed{
\log\kappa(B_p)
\ge
\sum_{j=J}^{p-1}\log\cosh a_j-\log2.
}
\tag{5.1}
$$
所以当 $a\notin\ell^2$ 时，任何有限头相似实现的条件数都必须趋于无穷。
不能通过改选有限头基、真空或相似矩阵消除这项成本。

例如：

- 若 $\delta_j=e^{-(j+2)^{-\sigma}}$、$\sigma>0$，则有界相似恰在 $\sigma>1/2$ 时成立。在临界 $\sigma=1/2$，$\log\cosh a_j=a_j^2/2+O(a_j^4)$ 给 $\kappa(B_p)\ge C\sqrt p$，其中 $C>0$ 与 $p$ 无关。
- 原强阻尼 $\delta_j=(j+2)^{-s}$、$s>0$ 满足
  $\sum_{j<p}\log\cosh a_j=s\,p\log p+O(p)$，故 (5.1) 至少付出该阶的对数条件数。此例的 $A_\delta$ 对所有有限 $s$ 都已按 §1 定义；原慢和的绝对范数级数仍须另外支付其系数和，例如 $s<1$ 时已足够。

## 6. 对原正常见证路线的意义与边界

本稿把整个实际表示的噪声相似问题在 (1.1) 中完全分类。
因此原 R248 的多项式强阻尼无法通过任何有界单位直接恢复原表示；
这比仅指出指定 $D_\delta^{-1}$ 无界更强。

但有界相似失败不等于 $S_\delta$ 有非零核，
也不排除只对某个指定正常矩向量完成撤阻尼或其他配对估计。
旧 R248 的特殊实际核与完整正常矩条件仍须分别处理。
普通 Hilbert ISP 没有由此完成。

## 7. 去掉全部噪声增长假设的普遍相似阈值

本节不再要求 (1.1) 的多项式下界，也不预设 R248 的局部无穷级数已经有界。
仅设
$$
0<\delta_j\le1,\qquad
D\chi_F=\delta_F\chi_F,\qquad
a_j=-\log\delta_j\ge0.
\tag{7.1}
$$
$D$ 是有界、单射、稠密像的正收缩。

**定理7.1。** 下列两条等价：

1. $a\in\ell^2$。
2. 存在有界可逆 $B$，使原全空间有界算子恒等式
   $$
   \boxed{DA=(B^{-1}AB)D}
   \tag{7.2}
   $$
   成立。

因此，如果自然共轭 $DAD^{-1}$ 在 $\operatorname{Ran}D$ 上有有界全域延拓 $A_\delta$，
那么这个唯一延拓与原 $A$ 有界相似，当且仅当 $a\in\ell^2$。
当没有已付的有界延拓时，本定理不预先宣称其存在。

充分性已经由前一附录的准确热分解证明，且该证明本来就不需要任何增长假设。
下面给完全一般的必要性。

### 7.1 仅使用有限位恒等式与稠密像

假设 (7.2) 成立，记
$$
K=\|B\|\|B^{-1}\|,\qquad
T_j=B^{-1}N_jB.
$$
由 $N_j=A^{2^j}/d_j$ 与 (7.2)，
$$
DN_j=T_jD,\qquad
\|T_j\|\le K.
\tag{7.3}
$$
对每个有限 $F$，还有更强的同一单位乘积预算
$$
\boxed{
\left\|\prod_{j\in F}T_j\right\|
=\left\|B^{-1}\left(\prod_{j\in F}N_j\right)B\right\|
\le K.
}
\tag{7.4}
$$
这里不是逐因子付 $K^{|F|}$。

原 $E_j$ 及其通常伴随只作用在一个物理位。
相对于 Walsh 基，定义两个真实有限位共轭
$$
E_{j,\delta}
=\frac12\begin{pmatrix}
1&\delta_j^{-1}\\-\delta_j&-1
\end{pmatrix},
\qquad
\widetilde E_{j,\delta}
=\frac12\begin{pmatrix}
1&-\delta_j^{-1}\\\delta_j&-1
\end{pmatrix}.
\tag{7.5}
$$
第二个是原 $E_j^*$ 的有限位噪声共轭，一般并非 $E_{j,\delta}^*$。
两者均有准确范数
$$
\|E_{j,\delta}\|
=\|\widetilde E_{j,\delta}\|
=\cosh a_j=:n_j.
\tag{7.6}
$$
将其张量尾恒等后，逐有限 Walsh 柱、再由有界性延拓，得到
$$
DE_j=E_{j,\delta}D,\qquad
DE_j^*=\widetilde E_{j,\delta}D.
\tag{7.7}
$$

原实际递推 $N_j=E_j+\eta_jE_j^*N_{j+1}$，
连同 (7.3)、(7.7)，给
$$
[T_j-E_{j,\delta}-\eta_j\widetilde E_{j,\delta}T_{j+1}]D=0.
$$
括号内对每个固定 $j$ 是有界算子，而 $\operatorname{Ran}D$ 稠密，所以
$$
\boxed{
T_j=E_{j,\delta}+\eta_j\widetilde E_{j,\delta}T_{j+1}.
}
\tag{7.8}
$$
从而
$$
\boxed{
\frac{\|T_j-E_{j,\delta}\|}{n_j}\le K\eta_j.
}
\tag{7.9}
$$

这一步没有展开任何受噪声放大的无限 carry 级数，
没有作用未经定义的全局 $D^{-1}$，
也不需要另外假定 $T_{j+1}$ 与第 $j$ 位的矩阵交换。
有限位等式及稠密像已足够。

### 7.2 相对乘积误差直接迫平方可和

因为 $\sum_j\eta_j<\infty$，
可以选 $J=J(K)$，使
$$
K\sum_{j\ge J}\eta_j\le\log(3/2).
$$
按 §3 相同的排序乘积差估计，
对任意有限 $F\subseteq[J,\infty)$，
$$
\left\|
\prod_{j\in F}T_j-\prod_{j\in F}E_{j,\delta}
\right\|
\le
\left(\prod_{j\in F}n_j\right)
\left[\prod_{j\in F}(1+K\eta_j)-1\right]
\le\frac12\prod_{j\in F}n_j.
$$
纯位仍在互不相交的张量因子上，所以
$$
\frac12\prod_{j\in F}\cosh a_j
\le\left\|\prod_{j\in F}T_j\right\|\le K.
$$
因此
$$
\sum_{j\ge J}\log\cosh a_j\le\log(2K)<\infty.
$$
每个前 $J$ 位的 $a_j$ 都有限，§4 的初等等价 (4.3) 遂给
$a\in\ell^2$。
必要性完成。

### 7.3 两种定量范围保留区别

定理7.1把相似的充要条件扩到任意实正噪声 $\delta$。
它仅在假设一个候选相似条件数 $K$ 后选择 $J(K)$。

此前 §§1--5 在已付的局部 carry 变形类中更进一步：
误差预算与固定起点 $J$ 直接由噪声下界给出，不依赖未知相似单位，
因此保留有限头条件数的明确增长率 (5.1)。
不能用本节依赖 $K$ 的起点，免费声称同样的无条件速度。

对没有任何增长控制的 $\delta$，
本节既不自动构造有界 $A_\delta$，
也不判断某个非相似慢变形是否有核；
其完整结论就是 (7.2) 的存在性恰由 $-\log\delta\in\ell^2$ 决定。
