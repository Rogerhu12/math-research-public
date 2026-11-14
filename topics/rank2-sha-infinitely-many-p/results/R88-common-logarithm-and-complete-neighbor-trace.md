# R88：共同对数规范下的完整邻点迹

日期：2026-11-12。状态：明确延拓、对数消去及全部常数已根端独审。
完整证明见[邻点的共同对数与零迹](../notes/2026-11-12-normalized-neighbor-logarithmic-traces.md)。

固定惰性 $p\ge7$，记全部真实邻点为 $K(r_j)=0$。
原点归一原函数 $E'=M_e/(sK)$ 的留数为

$$
R_j=-L(r_j)M_e(r_j),\qquad R_{-j}=-R_j.
$$

取包含全部 $r_j$ 而无其他 $K,L$ 零点的稍大开盘，定义

$$
A(t)=\frac{M_e(t)}{s(t)K(t)}-\sum_j\frac{R_j}{t-r_j},
\qquad E_{\rm an}(t)=\int_0^tA(t)\,dt.
$$

$A$ 解析且偶，$E_{\rm an}$ 解析且奇。
所有项共用一个 $p$ 进对数，令

$$
E_{\log}(t)=E_{\rm an}(t)+\sum_jR_j\log(1-t/r_j).
$$

它与原点 Taylor germ 准确一致，且 $E_{\log}(-t)=-E_{\log}(t)$。
对实际分支 $K(t_j)=\xi L(t_j)$，各支唯一的对数奇项是
$R_j\log\xi$；其和为零。因此
$T(\xi)=\sum_jE_{\log}(t_j(\xi))$ 在 $\xi=0$ 解析。
真实 Hecke 迹给

$$
T'=-\xi^{-2}\sum_jK(t_j)M_e(t_j)=0.
$$

分支满足 $t_{-j}(-\xi)=-t_j(\xi)$，故 $T$ 同时为奇函数，准确得到

$$
\sum_jE_{\log}(t_j(\xi))=0.
$$

原点解析部分、每支的 $\log(-t_j'(0)/r_j)$ 常数及所有交叉极点常数
也均已逐项配对核定；没有为不同分支重设积分常数。
结论对任何共同的 $\log(p)$ 成立。

这是一个明确规范中的完整零迹。
与外部 Coleman/Frobenius 积分或完整中央 Stokes 泛函的认同仍须证明。
更高 $H_o$ 的对数平方首项已固定，但较低对数项和迭代积分常数不能略去。
本结果不计算中央导数的零阶，也不能把独立范数常数移入中央行。
