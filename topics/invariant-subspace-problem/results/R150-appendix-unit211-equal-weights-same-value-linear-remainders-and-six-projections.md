# R150：一般等权原 N/P 的同一值线性余式与完整六投影

日期：2026-11-27（Asia/Taipei）；会话 Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**状态：已证明的原方程归约和六个参数条件；没有排除整个等权图。**

## 1. 原图和同一个值变量

接[两参数首一值二次式](R150-appendix-unit211-equal-weights-two-parameter-monic-value-quadratic.md)。沿用
$$
v=2y-1,\quad \kappa=(1-Q)v^2,\quad \omega=zv,\quad
A=\kappa+\omega^2-2\omega,\quad
m_n=(\omega-1)(\omega-\kappa),\quad m=m_n/A.
$$
原两均值方程等价于同一
$$
E=\alpha v^2+\beta=0,\qquad
2\alpha=(\omega-1)AR,\quad
R=\kappa^2+(\omega-1)^2\kappa-\omega^2.
$$
$\alpha,R$ 的非零已有原理想单位恒等式；并非一次特化后猜测首项非零。所有原物理单位及 $D_{\rm val}\ne0$ 保留，$v=-1$ 尚未排除。

记[原均值图](R150-appendix-unit211-equal-weights-original-mean-leading-zero-exclusion.md)中三条必要分子为
$$
F_N=\frac{P_{02}N_v-4LJ_0}{m^2(m-1)^2},\quad
F_S=\frac{P_{02}^2N_{\rm wt}-2(m-1)LP_{02}^2+4LJ_0P_{02}-4L^3}
 {m^2(m-1)^2},
$$
$$
F_P=\frac{P_{02}^2P_{\rm wt}-(m-1)P_{02}^3+3J_0P_{02}^2-4L^3}
 {m(m-1)^2}.
$$
这些恰为原源的 N1、Ns、Ps 行，不将它们冒称未清分母的 $N_H,N_S,P_S$。代入
$$
Q=1-\kappa/v^2,\quad z=\omega/v,\quad y=(v+1)/2,\quad m=m_n/A
$$
之后，令
$$
\mathcal F_N=A^2v^6 F_N,\qquad
\mathcal F_S=A^5v^9 F_S,\qquad
\mathcal F_P=A^6v^9 F_P.
\tag{1.1}
$$
所有外因子皆为已付单位。原齐次清分母中仅再剥 $v^2,v^4,v^4$，实际得到的完整三元多项式数据是：

| 原行 | $(\deg_\kappa,\deg_\omega,\deg_v)$ | 项数 |
|---|---:|---:|
| $\mathcal F_N$ | $(5,6,6)$ | 62 |
| $\mathcal F_S$ | $(10,12,9)$ | 446 |
| $\mathcal F_P$ | $(11,14,9)$ | 595 |

各完整系数由本页附源从已提交的原 Gram 源再生，不储存可重算的大展开。

## 2. 完整原组合的线性余式

对任意 $\mathcal F=\sum_j f_jv^j$，令 $L=\lfloor\deg_v\mathcal F/2\rfloor$，定义
$$
a_0=\sum_{q\ge0}f_{2q}(-\beta)^q\alpha^{L-q},\qquad
a_1=\sum_{q\ge0}f_{2q+1}(-\beta)^q\alpha^{L-q}.
\tag{2.1}
$$
这是多项式公式，不在未付的线性首项处作除法。对每个 $j=2q+\varepsilon$，使用差幂恒等式
$$
\alpha^L v^j-\alpha^{L-q}(-\beta)^qv^\varepsilon
=
E\,\alpha^{L-q}v^\varepsilon
\sum_{h=0}^{q-1}\alpha^{q-1-h}v^{2(q-1-h)}(-\beta)^h.
\tag{2.2}
$$
乘 $f_j$ 后求和，给出完整原关系
$$
\alpha^L\mathcal F-(a_0+a_1v)=E\,C_{\mathcal F}.
\tag{2.3}
$$
源逐项构建右侧 $C_{\mathcal F}$，并将整个多项式乘回，不只在商中比较余式。

从每对 $(a_0,a_1)$ 共同剥除的因子全部是已付单位，再统一整数化，记结果为 $A_i+B_iv$。准确规范是
$$
\begin{aligned}
\alpha^3\mathcal F_N-\frac{\omega(\kappa-1)}8(A_N+B_Nv)&=E C_N,\\
\alpha^4\mathcal F_S-\frac{(\omega-1)(\omega-\kappa)}{32}(A_S+B_Sv)&=E C_S,\\
\alpha^4\mathcal F_P-\frac{(\omega-1)(\omega-\kappa)^2}{32}(A_P+B_Pv)&=E C_P.
\end{aligned}
\tag{2.4}
$$
所有三条完整身份均已实际乘回。于是，在本已付图中，原三条必要式与这三个**同一个 $v$** 的一次式完全等价。

| 行 | $(\deg_\kappa A_i,\deg_\omega A_i)$ | $(\deg_\kappa B_i,\deg_\omega B_i)$ | 项数 $(A_i,B_i)$ |
|---|---:|---:|---:|
| N | $(14,20)$ | $(13,20)$ | $(124,124)$ |
| S | $(22,30)$ | $(21,30)$ | $(308,310)$ |
| P | $(22,31)$ | $(21,31)$ | $(333,332)$ |

## 3. 保全部首项零的六个参数条件

定义
$$
M_{ij}=A_iB_j-B_iA_j\quad(i<j),\qquad
K_i=\alpha A_i^2+\beta B_i^2.
\tag{3.1}
$$
在每个固定复参数点上，$\alpha\ne0$ 时，
$$
E(v)=0,\quad A_i+B_iv=0\ (i=N,S,P)
\quad\Longleftrightarrow\quad
K_N=K_S=K_P=M_{NS}=M_{NP}=M_{SP}=0
$$
这里左侧指“存在一个共同复数 $v$”。

证明：必要性直接代入。反向若某 $B_i\ne0$，取 $v=-A_i/B_i$；$K_i=0$ 给 $E=0$，两两子式给所有其他一次式。若所有 $B_i=0$，则 $K_i=0$ 和 $\alpha\ne0$ 迫所有 $A_i=0$；任取二次式的一个复根即可。后者完整保留了所有线性首项同时为零的纤维。

这只是这四条等式的准确投影。返回原解时仍须同点恢复 $v,x,y,t,\lambda,T$、原值条件与物理非零条件；没有把六个参数多项式的公共根自行宣布为原解。

## 4. 实际参数多项式和已付内容

由于 $v\ne0$、$Q\ne0$ 和原 $P_{02}\ne0$，在同一均值商中，
$$
\beta,\quad \beta+\kappa\alpha,\quad
J_P=(2m_n-A)\beta+3\kappa A\alpha
\tag{4.1}
$$
均为单位。最后一个由
$$
A\{(2m-1)v^2-3\kappa\}
=-J_P/\alpha
$$
得到。源只对原已付单位和 (4.1) 作整因子试除，每次完整乘回。下面“规范乘数”指剥除已付因子后乘的非零有理常数。

| 原条件 | 剥除的完整已付因子 | 规范乘数 | 余式 $(\deg_\kappa,\deg_\omega)$ | 项数 |
|---|---|---:|---:|---:|
| $K_N$ | $(\omega-1)(\kappa-1)AR$ | $2$ | $(27,39)$ | 435 |
| $M_{NS}$ | $\kappa-1$ | $1$ | $(34,50)$ | 762 |
| $M_{NP}$ | $(\omega-1)(\kappa-1)$ | $1$ | $(34,50)$ | 762 |
| $M_{SP}$ | $\omega^2(\kappa-1)^3J_P$ | $1/2$ | $(35,51)$ | 776 |
| $K_S$ | $\kappa-1$ | $2$ | $(46,65)$ | 1354 |
| $K_P$ | $(\omega-1)(\kappa-1)$ | $2$ | $(46,66)$ | 1405 |

没有剥 $\alpha+\beta$：它也覆盖尚未关闭的 $v=-1$。没有将某个值条件关于 $v$ 的范数当成已付单位，因为该范数还涉及另一个根，另一个根未必满足同一原物理条件。

## 5. 源、运行和准确范围

新增源位于 notes：

- 2026-11-27-unit211-equal-weight-three-parameter-original-NP-8542.js：对已提交 regular-original-chart 源的输出调用函数体，生成 $\mathcal F_S,\mathcal F_P$。
- 2026-11-27-unit211-equal-weight-same-v-linear-remainder-8542.js：输入上述三条原行和已提交 monic-value-original-unit 源的输出，返回 (2.4) 全部原迹。
- 2026-11-27-unit211-equal-weight-same-v-six-projections-8542.js：输入一次式、同一 $\alpha,\beta$ 及行名列表，构建并乘回第 4 节的条件。

它们均为精确 BigInt 的 Function body，以 new Function(source)(...inputs) 调用；不是声称它们独立作为 Node 脚本执行。所有依赖的原重建定义已在前述正文和源中登记，不需要 scratch 缓存。小执行回执给出精确源 SHA-256、调用参数、规范 JSON 输出哈希和实际时长。

原 NP 新重建实际 5.657 秒；线性余式分 N / S,P 两次实际 0.315 / 4.758 秒；六个投影分五次实际 9.330、5.174、13.790、22.560、23.613 秒。全部调用正常返回；V8 不暴露 OS 进程退出码或 RSS，回执没有填造这些数值。

这六个双参数必要条件尚未排空。下一继续它们的原同点有限覆盖或更低度组合，不能从一两个模素数计算直接宣告特征零为空。普通 ISP 与完整算子桥仍未完成。
