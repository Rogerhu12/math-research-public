# R101. Compact Selmer 特化余核与真实秩四检验

## 控制箭头保留的实际余核

Castella 的 *Generalised Kato classes on CM elliptic curves of rank 2*
v3，Proposition 6.2.1 将 compact 特化列为同构，但 §6.3
最后一步实际只使用注入。两者不能混同。

记大 compact 模为 $M$、基层模为 $M_0$，
$\Lambda=\mathcal O[[S]]$、$R=\Lambda_{(S)}$、$k=\operatorname{Frac}\mathcal O$。
原文的大模秩一结论和 $H^0(K,T_\psi)=0$ 给
\[
M_R\simeq R,\qquad\dim_k(M/SM)\otimes k=1.
\]
基层全局对偶则给
\[
\dim_k M_0\otimes k
=\dim_{\mathbb Q_p}\operatorname{Sel}(\mathbb Q,V_pE)-1.
\]
正秩保证所需的局部化非零。
对原 E17，两式及 compact 注入准确给
\[
\boxed{\dim_k\operatorname{coker}(r\otimes k)
=\operatorname{corank}_{\mathbb Z_p}\Sha(E17/\mathbb Q)[p^\infty].}
\]
因此把这条箭头当成有理同构，已经额外断言了所求初级有限性。
正确交换特化的 Selmer 复形中，缺项位于 $H^2[S]$；
实际局部修正也必须检查，不能仅写形式长正合列就宣布它为零。

## 独立有限域证书给出真实秩四曲线

令 $B=635318657=158^4+59^4=134^4+133^4$，
$E_*:y^2=x^3-Bx$，取
\[
(-24964,549998),\quad(-3481,-1472876),\quad
(-17956,2370326),\quad(-17689,2388148).
\]
在 $q=11,23,47,59$，点数分别为 $12,24,48,60$。
乘 $\#E_*(\mathbb F_q)/3$ 后的四个坐标行是
\[
\begin{pmatrix}1&2&0&2\\0&1&1&1\\1&2&0&0\\0&0&1&1\end{pmatrix},
\]
行列式模三为 $2$。又 $\#E_*(\mathbb F_5)=10$ 排除有理三挠点。
任何整数关系除去系数的最大共同三次幂后，会与此可逆矩阵矛盾；
故 $\operatorname{rank}E_*(\mathbb Q)\ge4$。

该曲线为正根数 CM 曲线，正秩给中央复值零；
$p=13$ 时点数 $20$、$a_{13}=-6$，为好普通素数。
因此同一 compact 箭头的源维数为一，目标至少三。
这直接排除该处“同构”的字面解释，不以无限 Sha 的存在为前提。

## 最后非零判据仍保留

特征理想平方只比较 DVR 长度，不自动给 coinvariants 的完整
数值秩等式；正文给出明确代数检验。
但秩一模的最小 coinvariant 维数与特征理想无中心零点的
等价成立。配合 compact 注入，论文最终所需的
$\kappa_p\ne0$ 判据仍可保留。
本结果没有否定这个最终判据，也没有证明原曲线的 Sha 有限。

[完整论证与原文位置](../notes/2026-11-12-compact-control-defect-and-rank-four-witness.md)
已经两位研究者全文独审；
[精确证书脚本](../scripts/check-compact-control-rank-four-witness.py)
及另一份独立有限域计算均通过。
