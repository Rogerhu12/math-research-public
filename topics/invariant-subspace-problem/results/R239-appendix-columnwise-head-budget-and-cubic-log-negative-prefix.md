# R239 附录：逐列真实头费用与三分之一次对数增长负前缀

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文继续锐化已证全尾前缀的近共同右费用，只对每列的实际 D 次数付头费用。由原四次列增长，得到 $K_m$ 为 $(\log m)^{1/3}$ 阶的全部物理源前缀，而负图校正系数仍为 $O(1/m)$。所有原尾核阶、同一个未来带与原完整平坦费保持；未把增长负图当成源坐标消失，余费用仍开。

依赖：[全尾小前缀近共同右费](R239-appendix-near-common-full-tail-prefix-and-growing-negative-head-graph.md)、[全尾低头源带](R239-appendix-full-tail-low-head-source-strip-and-bare-to-complete-right-bound.md)。

## 1. 对任意整数前缀使用相容链基

固定原 $m\ge5,d=2^m$ 和所有原合法窗口，记 $\nu=\|D_m\|\le1/m$。原无缩放相似为
$$
A_m=V_mJ_dV_m^{-1},\qquad V_m=1\oplus V_{m,+}.
$$
对任意整数 $2\le K\le d$，令 $S_K=V_m|_{H_K}$。上三角性给
$$
A_m|_{H_K}=S_KJ_KS_K^{-1},\qquad S_K=1\oplus S_{K,+}.
$$
它与任何更大的真实头在共同前缀上完全一致，不需要 $K$ 本身为二的幂。

若原源 $r$ 支持前 $K$ 物理头，仍保原尾阶 $E_{d-i-1,q}$，则已证真正完整候选可写为
$$
c_t=(-1)^{t-1}\left[e_0u_{t-1}
+\sum_{j=1}^{K-t}(V_me_j)D^ju_{t+j-1}\right],
$$
$$
u_i=e_0^*(D^{i+1})^\dagger A_m^ir,\qquad
\sum_i\|u_i\|^2\le\alpha(r)^2.
\tag{1.1}
$$
每个 $V_me_j$、$j\ge1$ 正交于第零物理头，故无 D 的第一项与整条其余链物理正交。

## 2. 正次 D 项的整链卷积估计

对每个固定 $j\ge1$，映射
$$
(u_i)_i\longmapsto
\bigl((V_me_j)D^ju_{t+j-1}\bigr)_t
$$
从原直和到完整链直和的范数至多 $\|V_me_j\|\nu^j$。这是因为不同 $t$ 属于不同物理孔层，每个输入项只出现一次。

在整个链 Hilbert 空间中先对这些 $j$ 求和，得到
$$
\boxed{\Psi_{K,m}:=\sum_{j=1}^{K-1}\|V_me_j\|\nu^j,\qquad
\lambda(r)^2\le(1+\Psi_{K,m}^2)\alpha(r)^2.}
\tag{2.1}
$$
这里没有把 $\nu^j$ 全部粗放成 $\nu$，也没有给每个输入重复支付段数。

## 3. 每列的实际四次成本

原 $Ae_1=e_0$ 与首行列归一给 $V_me_1=e_1$。对 $j\ge2$，令 $H_j$ 为不小于 $\max(8,j+1)$ 的最小二进制维数。因 $j\le d-1$，有
$$
H_j\le d,\qquad H_j\le4j.
$$
前缀一致性与既有 $221$ 条件数界（此处小头位数至少三）给
$$
\boxed{
\|V_me_j\|\le e^{221H_j^4/16}
\le e^{3536j^4}\quad(j\ge2).
}
\tag{3.1}
$$
因此
$$
\Psi_{K,m}\le\frac1m+
\sum_{j=2}^{K-1}\exp(3536j^4-j\log m).
\tag{3.2}
$$
此式是同一个原链基的逐列预算，不是重选相似矩阵后的费用比较。

## 4. 明确增长宽度与 O(1/m) 缺陷

定义
$$
\boxed{K_m=\max\left\{2,\ 1+
\left\lfloor\left(\frac{\log m}{7072}\right)^{1/3}\right\rfloor\right\}.}
\tag{4.1}
$$
对 $m\ge5$ 有 $K_m\le m\le d$，且 $K_m\to\infty$。当和中存在 $j\ge2$ 时，(4.1) 保证
$3536j^4\le(j/2)\log m$。所以
$$
\boxed{
\Psi_{K_m,m}
\le\frac1m+\sum_{j=2}^{\infty}m^{-j/2}
=\frac1m+\frac1{m(1-m^{-1/2})}
\le\frac2{m(1-m^{-1/2})}\longrightarrow0.
}
\tag{4.2}
$$
若 $K_m=2$，空和使同一界仍成立。

## 5. 原整个前缀负图的同未来带校正

在原源归一中令
$$
u=B^{1/2}r,\quad H=B^{-1/2}LB^{-1/2},\quad
C=B^{1/2}GB^{1/2},\quad
W_{K_m}=B^{1/2}\mathscr X_{K_m,q}.
$$
由 (2.1)，$C^{-1}-I$ 在 $W_{K_m}$ 上的压缩不超过
$\Psi_{K_m,m}^2I$。同一个真实未来带 $y$ 的角恒等式给
$$
\|P_{W_{K_m}}(I+H)u\|\le\Psi_{K_m,m}\|y\|.
$$
令 $t=B^{-1/2}(I+H)^{-1}P_{W_{K_m}}(I+H)u$。则
$$
\boxed{\langle(L+B)(r-t),s\rangle=0
\quad(s\in\mathscr X_{K_m,q}),}
\tag{5.1}
$$
$$
\boxed{\chi(t)^2+2\mu(t)^2\le\Psi_{K_m,m}^2\|y\|^2,
\qquad\mu(t)\le\tfrac12\Psi_{K_m,m}\|y\|.}
\tag{5.2}
$$

为自含记录累计界，原同未来关系可写为
$$
C^{1/2}Hu=(I-C)^{1/2}z-C^{1/2}u,
\qquad\|u\|^2+\|z\|^2\le\|y\|^2.
$$
行算子 $[-C^{1/2},(I-C)^{1/2}]$ 是余等距，所以
$\chi(r)^2=\|u\|^2+\|C^{1/2}Hu\|^2\le2\|y\|^2$。
故对全部原窗口的同一旧顶部族，若原左误差和每窗未来量至多
$\beta_m\|w\|$，且 $\sum_q\|y_q\|^2\le d\beta_m^2\|w\|^2$，则
$$
\sup_q\|E_q^\dagger(r_q-t_q)-w\|
\le(1+\Psi_{K_m,m}/2)\beta_m\|w\|,
$$
$$
\sum_q\chi(r_q-t_q)^2
\le(\sqrt2+\Psi_{K_m,m})^2d\beta_m^2\|w\|^2.
\tag{5.3}
$$
没有删除窗口，也没有假定 $\beta_m$ 的额外下降速率。校正族不被宣称仍是共同顶部的逐孔源流。

## 6. 所改进的范围与余问题

这次只把近共同、全窗口可付的前缀增长尺度改进为 $(\log m)^{1/3}$，并将缺陷系数保到 $O(1/m)$。它与此前约 $d^{3/4}$ 的有费 M 源图是两种不同预算。

负图 (5.1) 仍须通过原完整 $L+B$ 交叉块重建前缀源；其条件数和高头反馈没有因此消失。增长源空间也随 $m,q$ 变化，因此不能仅由 $K_m\to\infty$ 推出 $w=0$。余费用比较继续保持为明确未闭问题。
