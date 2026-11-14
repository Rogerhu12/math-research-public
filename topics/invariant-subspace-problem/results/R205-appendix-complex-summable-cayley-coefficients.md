# R205 附录：任意复可和 Cayley 系数的二阶孔次数刚性

日期：2026-11-12（UTC）。作者：l2_moments。

本附录将 R205 的二阶结论推广到任意非零复系数列 $a\in\ell^1$。主稿处理具体慢列；这里独立补齐退化系数和最低非零物理位的处理。次数范围仍为边界孔次数不超过二。

## A.1. 结论

沿用 R205 的 $B,\mathsf N_j,\mathsf Y_j,\mathcal F_m,\mathcal H^-_{\le2}$。令
$$
T_a=\sum_{j\ge0}a_j\mathsf Y_j,\qquad
0\ne a\in\ell^1,\qquad s=\min\{j:a_j\ne0\}.
\tag{A.1}
$$
该和按算子范数绝对收敛。

**定理A.1。** 若
$$
x\in\mathcal H^-_{\le2},\qquad T_ax\in\mathcal F_m
$$
对某个 $m\ge0$ 成立，则 $x$ 属于一个有限头。因此
$$
\boxed{
\ker T_a\cap\mathcal H^-_{\le2}
=\mathcal F_s\cap\mathcal H^-_{\le2}.
}
\tag{A.2}
$$
结论不要求系数同相位，也不要求无限支撑。

## A.2. 首系数非零时的统一真实方程

先设 $a_0\ne0$。按 R205 第2节分解最低物理位，令
$$
\beta=\alpha_0,\quad Q=C/\beta,\quad
b_j=\frac{a_{j+1}}{a_0},\quad
D=\sum_{j\ge0}b_j\widehat{\mathsf Y}_j.
$$
将整个输出除以 $a_0$ 后，实际矩阵式恰为
$$
\frac{T_a}{a_0}
=(I-Q)^{-1}
\begin{pmatrix}(I-Q)D-Q&I\\Q&(I-Q)D-Q\end{pmatrix}.
\tag{A.3}
$$
所以对于 $x=(u,v)$ 及 $f=T_ax/a_0$，仍有
$$
u\in\widehat{\mathcal H}^-_{\le2},\qquad
v=c_*e_0+\sum_{j\ge0}c_je_{2^j},\qquad c\in\ell^2,
\tag{A.4}
$$
以及
$$
Qu=Qv-Dv+QDv+(I-Q)f_1.
\tag{A.5}
$$
若 $g=Dv$，在 $\nu(n)\ge3$ 且 $n-1$ 超过 $f_1$ 头部的坐标，有
$$
g_n-\frac\beta{w_n}g_{n-1}=0.
\tag{A.6}
$$
主稿的实际系数公式对这些复系数原样成立：
$$
t_k=\sum_{l:\,2^l\mid k}
b_l(-1)^{k/2^l-1}\widehat d_l^{-k/2^l},
\qquad
g_n=\frac1{\widehat W_n}
\sum_{j:\,2^j>n}c_j\widehat d_jt_{2^j-n}.
\tag{A.7}
$$
第二式先由有界矩阵行及 Cauchy–Schwarz 得到绝对收敛；以下拆开的尾和也分别绝对收敛。

## A.3. 两个最低尾系数的全部分支

先假设 $b_0\ne0$。取 $r\ge\max(4,m)$，用主稿两行
$$
n=2^r-1,\qquad n'=2^r-5.
$$
它们都满足 (A.6)，且共享同一源集合 $j\ge r$。
设
$$
U_r=\sum_{j\ge r}c_j\widehat d_j\widehat d_0^{-2^j},
\qquad
V_r=\sum_{j\ge r}c_j\widehat d_j\widehat d_1^{-2^{j-1}}.
$$
得到
$$
A_nU_r-B_nV_r=0,
\qquad
A_n=b_0(1+\beta/\widehat d_0)\widehat d_0^n,
\quad B_n=\beta b_1\widehat d_1^{(n-1)/2}.
\tag{A.8}
$$
因为 $\beta,\widehat d_0>0$，$1+\beta/\widehat d_0\ne0$，所以 $A_n\ne0$。

若 $b_1\ne0$，两行的比例分别为 $\widehat d_0^4$ 和 $\widehat d_1^2$，仍不相等，故 $U_r=V_r=0$。
若 $b_1=0$，单行已经给 $U_r=0$。
无论哪一分支，逐个 $r$ 相减给 $c_r=0$ 对所有 $r\ge\max(4,m)$ 成立。

这里完全没有使用 $b_0,b_1$ 的实部或相位；只有实际权的严格不等式用于判别两行矩阵可逆。

## A.4. 最低尾系数位于任意高层时的单行消元

现在设 $b_0=0$，但 $b\ne0$。令
$$
q=\min\{l\ge1:b_l\ne0\}.
$$
对
$$
r\ge r_*:=\max(4,m,q+2)
$$
选择
$$
n=2^r-(2^q-1)=2^r-2^q+1.
\tag{A.9}
$$
此时 $2^{r-1}<n-1<n<2^r$，
$$
\nu(n)=r-q+1\ge3,\qquad
n-1=2^r-2^q\ge2^{\max(m-1,0)}.
$$
所以 (A.6) 成立，且 $g_n,g_{n-1}$ 的源集合都是 $j\ge r$。

对任意此类 $j$，记 $k=2^j-n$。$k$ 为奇数，且
$$
v_2(k+1)=v_2(n-1)=q.
$$
因为 $b_0=\cdots=b_{q-1}=0$，(A.7) 精确给
$$
t_k=0,\qquad
t_{k+1}=b_q\widehat d_q^{-(k+1)/2^q}.
\tag{A.10}
$$
第二个符号是正号，因为 $(k+1)/2^q$ 为奇数。
因此 (A.6) 化为
$$
-\beta b_q\widehat d_q^{(n-1)/2^q}\,V_{q,r}=0,
\qquad
V_{q,r}:=\sum_{j\ge r}c_j\widehat d_j\widehat d_q^{-2^{j-q}}.
\tag{A.11}
$$

为完整验证该尾和，将 $\widehat d_j$ 中的权按长度 $2^q$ 分块。每块内部的权相同，只有块末端改变：第 $l$ 块的末权为 $\alpha_{q+1+v_2(l)}$。
奇数块的乘积等于 $\widehat d_q$；偶数块至多是 $\widehat d_q\alpha_{q+2}/\alpha_{q+1}$。
所以对 $j\ge q+1$，
$$
0<\frac{\widehat d_j}{\widehat d_q^{2^{j-q}}}
\le\left(\frac{\alpha_{q+2}}{\alpha_{q+1}}\right)^{2^{j-q-1}}.
\tag{A.12}
$$
右边属于关于 $j$ 的 $\ell^2$，与 $c\in\ell^2$ 配对即得 (A.11) 的绝对收敛。

(A.11) 的外部系数非零，故 $V_{q,r}=0$ 对所有 $r\ge r_*$ 成立。相减相邻尾和，得到
$$
0=V_{q,r}-V_{q,r+1}
=c_r\widehat d_r\widehat d_q^{-2^{r-q}},
$$
所以 $c_r=0$ 对所有 $r\ge r_*$ 成立。

两类分支已经涵盖全部非零 $b$。由 (A.5) 与主稿第7节，
$$
\boxed{x\in\mathcal F_{r_*+2}}
\tag{A.13}
$$
其中 $b_0\ne0$ 时可取 $r_*=\max(4,m)$。

## A.5. 没有尾项的分支

若 $b=0$，则 $T_a=a_0\mathsf Y_0$。从
$$
a_0\mathsf N_0x=(I+\mathsf N_0)T_ax
$$
可见 $Bx\in\mathcal F_m$，因为右边属于同一有限头。
实际后移的每个权均非零，因此 $x_n=0$ 对所有 $n\ge2^m+1$ 成立，特别 $x\in\mathcal F_{m+1}$。
这一步不需要任何孔次数假设。

## A.6. 最低非零位之前的有限块对角分解

回到一般 $s=\min\operatorname{supp}a$。
按最低 $s$ 位将空间分解为 $2^s$ 个尾副本：
$$
e_{2^sn+h}\leftrightarrow e_h\otimes e_n,
\qquad0\le h<2^s.
\tag{A.14}
$$
令 $C_s$ 为尾实际后移，其权为 $\alpha_{s+v_2(n)}$。
在每个长度 $2^s$ 的实际权乘积中，低于 $s$ 的权组成一个与 $h$ 无关的固定因子，剩余的唯一高位权为 $\alpha_{s+v_2(n)}$。
因此对 $j\ge s$，归一化时该固定因子完全约掉，给出精确式
$$
\mathsf N_j=I_{2^s}\otimes\mathsf N^{(s)}_{j-s},
\qquad
\mathsf Y_j=I_{2^s}\otimes\mathsf Y^{(s)}_{j-s}.
\tag{A.15}
$$
由于 $a_j=0$ 对 $j<s$，
$$
T_a=I_{2^s}\otimes
\left(\sum_{l\ge0}a_{s+l}\mathsf Y^{(s)}_l\right).
\tag{A.16}
$$
尾符号的首系数 $a_s$ 非零。移位后的实际权仍严格递减且满足同样的逆界，故 A.2—A.5 的证明适用。

若 $x\in\mathcal H^-_{\le2}$，则每个非零头分量 $x_h$ 的尾次数为至多 $2-\nu(h)$，尤其不超过二。
若 $T_ax\in\mathcal F_m$，则每个尾输出都属于
$$
\widehat{\mathcal F}_{m_s},\qquad m_s=\max(m-s,0).
$$
当 $m<s$ 时，只是若干头分量的真空标量，其余为零，仍满足这个统一头界。
因此每个 $x_h$ 都在同一明确有限头内；有限个分量合并后，$x$ 在原空间也有有限头。
例如非零尾项分支可以取原头界 $s+r_*+2$，其中 $r_*$ 用 $m_s$ 和移位后系数计算。

## A.7. 精确核与未解决范围

$T_a$ 在任意足够大的有限头上都是 $B$ 的多项式。其最低非零形式阶为 $2^s$，首系数为 $a_s/d_s\ne0$：较高位从更大的幂开始，而最低位的 Cayley 级数首项不会被其他项抵消。
因此有限头上
$$
T_a=B^{2^s}U,
$$
其中 $U$ 是可逆且与 $B$ 交换的有限矩阵。故有限头核恰为 $\mathcal F_s$。
结合已经证明的反向有限头性质，得到 (A.2)。

本附录没有证明 $p\ge3$ 的类似刚性，也没有证明有限次数输出即可迫使输入有限头。尤其不从 $\mathcal H^-_{\le2}$ 在某些方向的稠密性推断未知闭核中的域密度。
关于 $\overline{B\ker T_a}=\ker T_a$，本稿没有新增结论。

内部依据为 R205 主稿第2—7节的实际分块和坐标式；本附录已经单独补齐所有零系数分支、复相位、任意首非零位以及共享尾和的绝对收敛。
