# R646 — 原完整目标的分歧合流单位块与全部 Smith 指数上界

日期：2026-11-15。**状态：已证明。**

本篇继续 R620/R631/R633 的同一个原来源 $\mathcal W_D$ 和完整目标 $\mathcal C_p$。在原条件 $f_D<p$ 下，完整评价在特征零中全列单射，且每个 Smith 指数都有明确有限上界。因而 R633 中暂合并计算的“赋值至少二或零方向”现在全部是真正的有限 $p$ 幂因子。

证明只作一次辅助的完全分歧基扩张。全部原列在较小圆盘上的首项成为按 $s$ 余类分组的合流 Vandermonde 族，原 $q_n$、$g/t$ 和 $U_0$ 的全部高尾均严格更高阶；没有将这些高尾设成零，也没有把补齐的合流列加入原来源。

结果仅属于原**完整** $\mathcal C_p$。旧三块 $M$、原 $D_\psi^+$、同一个 $R$ 和两组十三行的第二障碍仍须另解。

## 1. 同一原矩阵与目标的单指数基

设
$$
p=6s-1>101,\qquad
f_D=\lfloor9D/2\rfloor+4<p.
\tag{1}
$$
沿用 R633 的整来源、全部角帽及原标准列
$$
C_{n,k}=Y^nq_n(t)t^k,\quad
0\le n\le D,\quad0\le k\le e_{n+1},
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\quad
h_7=7+4t+16t^2,\quad d=1+8t,
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
e_{n+1}=f_n-3A_n-B_n+C_n,\quad
b_n=A_n+e_{n+1}.
\tag{2}
$$
记 $N_D=\sum_{n=0}^D(e_{n+1}+1)$。真实完整评价仍为
$$
\Phi(P)=c_*w^{13}U_0(w)e^{40a\epsilon}
P(t(w),g(w)e^{a\epsilon}),
\tag{3}
$$
其中 $a,c_*,U_0(0)$ 均是原单位，$t(w)=\tau_0w+O(w^2)$、$\tau_0$ 为原单位，$g(0)=1$。原 $P_{134}$ 及共同 charge 四十完全保留。

目标是原有限自由环
$$
\mathcal C_p=\mathcal O[w,\epsilon,\Upsilon]/
(w^s-p\epsilon,\epsilon^6-w\Upsilon,
w^{s-1}\epsilon^5-p\Upsilon,\Upsilon^s).
\tag{4}
$$
在 $\mathcal C_p\otimes K=K[w]/w^{ps}$ 中令
$$
v(m)=\lfloor6m/p\rfloor,\qquad
\gamma_m=p^{-v(m)}w^m,\quad0\le m<ps.
\tag{5}
$$
这些 $\gamma_m$ 正是 (4) 的原标准基重新排序。具体地，若
$m=jp+r+ts$，其中 $0\le j<s$、$0\le r<s$、$0\le t\le5$ 且 $(r,t)\ne(s-1,5)$，则
$v(m)=6j+t$，故 $\gamma_m=\Upsilon^jw^r\epsilon^t$。因此 (5) 没有在目标中免费除以 $p$；它只是原格在其有理化内的准确表示。

记 $M_{\mathcal C}$ 为 (3) 关于原列及 (5) 的整矩阵。R620/R631 已支付其整性。

## 2. 辅助分歧换元保留所有真实高尾

取辅助扩张
$$
\mathcal O'=\mathcal O[\pi],\qquad \pi^s=p,
$$
按 $\pi$ 赋值归一化 $v_\pi(\pi)=1$。这是完全分歧 DVR，剩余域仍为 $k$。只在证明矩阵性质时使用它；最终 Smith 结论仍在原 $\mathcal O$ 上。

令 $w=\pi z$。原第二盘估计 R618 给 $g,t/w,U_0$ 等固定 regular 单位的系数界
$$
v_p(h_m)\ge-\lfloor6m\tau_2\rfloor,\qquad
\tau_2=\frac{2p-1}{p(p^2-1)}.
\tag{6}
$$
对任何 $m\ge1$，
$$
v_\pi(h_m\pi^m)
\ge m-s\lfloor6m\tau_2\rfloor
\ge m(1-6s\tau_2)>0,
\tag{7}
$$
因为
$$
6s\tau_2=\frac{2p-1}{p(p-1)}<1.
$$
所以在所需的整个次数 $<ps$ 窗口内，$g(\pi z)$、$t(\pi z)/(\tau_0\pi z)$、$U_0(\pi z)/U_0(0)$ 都是整系数单位，模 $\pi$ 等于 $1$。原有限角单位 $h_7(t)/7$、$1-t$、$d(t)$ 及其逆亦然。它们的任意原整数幂仍保持这一性质。

第一 Gaussian 不使用 (6) 删除。它准确变为
$$
e^{a w^s/p}=e^{a z^s}.
\tag{8}
$$
目标只读 $z$ 次数 $<ps$，所以 (8) 只需指数 $0,\ldots,p-1$；所有阶乘都为单位。相同事实适用于共同的 $e^{40a z^s}$。

对原列 $(n,k)$ 置
$$
r_{n,k}=13+A_n+k.
\tag{9}
$$
由 (3)、(6)–(8)，归一化的**整个实际列**
$$
\widetilde F_{n,k}(z)=\pi^{-r_{n,k}}\Phi(C_{n,k})(\pi z)
\in\mathcal O'[z]/z^{ps}
\tag{10}
$$
整，且
$$
\overline{\widetilde F}_{n,k}(z)
=\lambda_{n,k}\,z^{r_{n,k}}
\exp\!\left(\bar a(n+40)z^s\right),
\quad\lambda_{n,k}\in k^\times.
\tag{11}
$$
这里 $\lambda_{n,k}=c_*U_0(0)\tau_0^{A_n+k}7^{A_n}(-1)^{B_n}$ 的约化。全部高尾仍在 (10) 中；(7) 证明它们只在 (11) 的约化中消失。

## 3. 每个余类的真实合流族均独立

写
$$
r_{n,k}=u+js,\qquad0\le u<s.
$$
按 $z$ 次数模 $s$ 将 (11) 分组，置 $X=z^s$。固定 $u$ 后的实际列是
$$
X^j e^{\bar a(n+40)X}\quad\text{于 }k[X]/X^p,
\tag{12}
$$
其中 $j$ 必须由原区间
$$
13+A_n\le u+js\le13+b_n
\tag{13}
$$
给出。没有忽略任何下帽或上帽。

为证明这些实际列独立，令
$$
J_n(u)=\left\lfloor\frac{b_n+13-u}{s}\right\rfloor,\qquad
C_u=\sum_{n=0}^D (J_n(u)+1)_+.
\tag{14}
$$
仅在这个线性独立性证明中，把同节点缺失的低 $j$ 补齐到 $j=0,\ldots,J_n(u)$。补齐后的首 $C_u$ 个 Taylor 行形成完整的合流 Vandermonde 矩阵。各节点 $\bar a(n+40)$ 两两不同，因为 $D<p$；若 $C_u\le p$，所用阶乘亦均为单位。其行列式为一个单位阶乘因子乘
$$
\prod_{n<n'}\{\bar a(n'-n)\}^{(J_n(u)+1)(J_{n'}(u)+1)},
$$
其中只取正重数的节点。因此补齐族独立，原族作为其子族也独立。

这一步不把补齐列送入 $\mathcal W_D$，不扩大原列数，也不赋予新中央条件。

由 $C_u\le C_0$，只需证明
$$
\boxed{C_0=\sum_{n=0}^D\left(1+\left\lfloor\frac{b_n+13}{s}\right\rfloor\right)\le p.}
\tag{15}
$$
原十二余类公式给
$$
b_{n+12}=b_n+50,\quad
(b_0,\ldots,b_{11})=(4,8,13,15,21,24,30,32,37,41,47,48),
$$
故 $b_n\le25n/6+16/3$。由 (1)，$D<2(p-4)/9$。于是
$$
\begin{aligned}
C_0
&\le(D+1)\left(1+\frac{25D+220}{2(p+1)}\right)\\
&\le\frac{(2p+1)(68p+1798)}{162(p+1)}
\le p\qquad(p\ge137).
\end{aligned}
\tag{16}
$$
最后一不等式等价于
$26p^2-3502p-1798\ge0$；在 $p=137$ 为 $6422>0$，此后严格递增。

剩下 $101<p<137$、$p\equiv5\bmod6$ 的素数只有 $107,113,131$。在 (1) 允许的最大 $D$ 处，直接由上述十二余类表得到：

| $p$ | $s$ | 最大 $D$ | 各 $j\ge0$ 的计数 $\#\{n:b_n+13\ge js\}$ | $C_0$ |
|---|---:|---:|---|---:|
| $107$ | $18$ | $22$ | $23,22,18,14,9,5,1$ | $92$ |
| $113$ | $19$ | $24$ | $25,24,19,15,11,6,1$ | $101$ |
| $131$ | $22$ | $28$ | $29,27,22,17,11,7,1$ | $114$ |

随 $D$ 减小计数只减小，故 (15) 对全部范围成立。这是有限参数边界的整数求和，不是以素数扫描替代跨素数证明。

## 4. 实际整矩阵的单位左逆

把每个 $0\le m<ps$ 唯一写成
$$
m=u+hs,\quad0\le u<s,\quad0\le h<p.
$$
由 $6s=p+1$，
$$
\omega_m:=m-sv(m)
=u-s\left\lfloor\frac{6u+h}{p}\right\rfloor.
\tag{17}
$$
其中 $0\le6u+h<2p$，而取值 $-s$ 不可能：若取下一个 floor，必须有 $u\ge1$。因此
$$
\boxed{1-s\le\omega_m\le s-1.}
\tag{18}
$$

定义辅助矩阵
$$
\boxed{
\mathsf A=
\operatorname{diag}(\pi^{\omega_m})\,
M_{\mathcal C}\,
\operatorname{diag}(\pi^{-r_{n,k}}).
}
\tag{19}
$$
(5)、(9)–(10) 表明它正是 $\widetilde F_{n,k}(z)$ 的普通 $z$ 系数矩阵。因此 $\mathsf A$ 整。第 3 节证明其模 $\pi$ 全列独立，故它有一个单位的 $N_D\times N_D$ 子式，并有整左逆
$$
\mathsf L\mathsf A=I_{N_D},\qquad
\mathsf L\in\operatorname{Mat}_{N_D\times ps}(\mathcal O').
\tag{20}
$$

(19) 是证明用的分歧对角缩放，**不是**原目标上的整基变换：部分 $\omega_m$ 为负，也确实使用了 $\pi^{-r_{n,k}}$。结论来自 (20) 和精确权界，不能把 (19) 直接称为原矩阵整等价。

特别，$M_{\mathcal C}$ 在分式域中全列独立，故其原 $\mathcal O$ 核为零。原 $w^{13}$ 并未被约去为单位；它在每一条 (9) 和 (14) 中均真实保留。

## 5. 全部 Smith 指数的统一有限界

**定理。** 在 (1) 的整个原范围内，$M_{\mathcal C}$ 的 $N_D$ 个 Smith 因子全非零。若其中一个为 $p^e$（单位因子对应 $e=0$），则
$$
\boxed{
e\le B_D:=\left\lceil\frac{b_D+13}{s}\right\rceil.
}
\tag{21}
$$
因而 $\operatorname{coker}M_{\mathcal C}$ 的 torsion 被 $p^{B_D}$ 杀掉，自由秩为 $ps-N_D$。

**证明。** 由原 DVR 上的 Smith 分解，存在原整 primitive 向量 $P$ 使 $M_{\mathcal C}P\in p^e\mathcal O^{ps}$。取相应 Smith 向量即可覆盖每个指数。由 (18)–(20)，
$$
\operatorname{diag}(\pi^{r_{n,k}})P
=\mathsf L\operatorname{diag}(\pi^{\omega_m})M_{\mathcal C}P
\in\pi^{se+1-s}\mathcal O'^{N_D}.
$$
$P$ 有一个原单位坐标，而 $r_{n,k}\le b_D+13$，故
$$
se+1-s\le b_D+13.
$$
因此
$e\le\lfloor(b_D+13+s-1)/s\rfloor
=\lceil(b_D+13)/s\rceil$。证毕。

从 (16) 使用的同一帽界，
$$
b_D+13\le\frac{25p+395}{27}.
$$
该量不超过 $7s$ 对所有 $p>101$ 成立，故
$$
\boxed{B_D\le7.}
\tag{22}
$$
当 $p\ge185$ 时它不超过 $6s=p+1$。余下 $137\le p<185$ 的相关素数在最大 $D$ 处分别为
$$
(p,D,b_D)=(137,29,124),(149,32,137),(167,36,154),
(173,37,158),(179,38,163);
$$
它们也满足 $b_D+13\le6s$。所以有更明确的统一结论
$$
\boxed{p\ge137\Longrightarrow B_D\le6.}
\tag{23}
$$
这不声称上界在每个参数处达到，也不区分中间各个高指数的准确数目。

## 6. 与原 Hilbert 函数和首 Bockstein 的接续

R620 的同一原首核维数
$$
k_m=\sum_r(m_r-(p-78-6r)_+)_+
$$
继续给出准确的单位因子数 $N_D-k_m$。

在 R633 的早阶条件 (E) 下，同一真实首 Bockstein 核维数为
$$
\kappa_D=\sum_r
\left(j_r-\bigl(h_r-m_r\bigr)_+\right)_+,\quad
h_r=(p-78-6r)_+,\quad
j_r=\#\{n:b_n\ge s+r\}.
$$
结合本篇，原完整矩阵的分布准确收紧为：

- $N_D-k_m$ 个单位因子；
- $k_m-\kappa_D$ 个恰为 $p$ 的因子；
- $\kappa_D$ 个真正属于 $p^2,\ldots,p^{B_D}$ 的因子；
- 没有零方向。

特别，R633 的 $\kappa_D$ 不再含特征零核。更高各指数的细分仍是新的问题；本篇只付清其有限性和统一上界。

旧三块 $M$ 只见其中一个很短的原截断。第 3 节合流独立性实际使用每个余类最多 $C_u$ 个 Gaussian 行，不能把它们压到旧目标的两长行和一短行。故 (20) 不给旧 $\bar J_A$ 的左逆，也不判定旧 $D_\psi^+$ forcing 或同一修正 $R$ 的 $d_2$。原两组十三行、完整中央和旧小预算问题均保持原状。


## 7. 依赖与证明范围

所用完整整目标和原格来自 [R620](R620-full-original-weighted-hilbert-function-and-thirteen-row-smith-window.md)；全部 regular 高尾估计来自 [R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)；原首 Bockstein 的整性与像锥分别见 [R631](R631-original-first-bockstein-weight-band-and-exact-boundary-kernel.md)、[R633](R633-original-image-cone-and-complete-confluent-first-bockstein.md)。本篇新增的是分歧小盘中的全列单位块、完整原矩阵无零方向以及 (21)–(23) 的全部高 Smith 上界，不新增任何算术中央零。
