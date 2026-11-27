# 原 R275 平方分解的定量返回与六位出生二统一 319/320 首边

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f / stable_kernel_return。

**状态：全文已证明。** 对六个任意独立正权，原九维出生二 primitive 空间上有
$$
\boxed{
\Gamma_{1,2}^{(6)}
\bigl(\Gamma_{2,2}^{(6)}\bigr)^{-1}
\Gamma_{1,2}^{(6)}
\preceq\frac{319}{320}I.
}
\tag{1}
$$
常数与六个权的大小及相对比值无关，不声称最优。证明把新五位统一 S2 余量返回到原 $H_0$；没有将辅助三块矩阵的正定性直接当作原相邻比的统一界。

## 1. 保留原三个完整正块

使用 [R275 §§1–4](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) 的全部原符号，$t=a^2>0$，
$$
F=C_1^2-C_2,\quad
Q=B^*L_2,\quad
E_1=\Delta L_3^{-1}L_2,\quad
A=C_1Q-E_1,
$$
$$
Z_1=\begin{pmatrix}L_1&L_2\\L_2&L_3\end{pmatrix},
\quad
R_1=[E_1,\Delta].
$$
原平方分解使用
$$
\mathcal B_0=
\begin{pmatrix}
C_1&A&0\\
A^*&I&L_1\\
0&L_1&L_2
\end{pmatrix},
\qquad
\mathcal B_1=
\begin{pmatrix}
F&R_1\\
R_1^*&Z_1
\end{pmatrix}.
\tag{2}
$$
若对某些 $0<\varepsilon\le1$、$0\le\kappa,\rho,\sigma<1$ 有
$$
F\succeq\varepsilon C_1^2,\qquad
\Delta L_3^{-1}\Delta^*\preceq\kappa F,
$$
$$
A^*G_1A+L_1L_2^{-1}L_1\preceq\sigma I,\qquad
L_2L_3^{-1}L_2\preceq\rho L_1,
\tag{3}
$$
则这些都是同一旧上下来源的完整费用，不要求任何矩阵交换。

## 2. 原块的统一归一化下界

把 $\mathcal B_0$ 的第一、第三坐标合为一侧，第二坐标为另一侧。以 $\operatorname{diag}(C_1,I,L_2)$ 归一后，其非对角行的平方恰为
$$
A^*C_1^{-1}A+L_1L_2^{-1}L_1\preceq\sigma I.
$$
标准二块范数界因而给
$$
\mathcal B_0\succeq
(1-\sqrt\sigma)\operatorname{diag}(C_1,I,L_2).
\tag{4}
$$

由最后一条 (3)，
$$
Z_1\succeq
(1-\sqrt\rho)\operatorname{diag}(L_1,L_3)\succ0.
$$
令 $S_1=[0,\Delta L_3^{-1}]$。原准确关系是
$$
R_1=S_1Z_1,\qquad
R_1Z_1^{-1}R_1^*=\Delta L_3^{-1}\Delta^*\preceq\kappa F.
$$
因此先以 $\operatorname{diag}(F,Z_1)$ 归一，再用上式，得到
$$
\mathcal B_1\succeq
(1-\sqrt\kappa)\operatorname{diag}(F,Z_1)
\succeq
(1-\sqrt\kappa)(1-\sqrt\rho)
\operatorname{diag}(F,L_1,L_3).
\tag{5}
$$
这里的逆都在已付正定块上，未交换压缩与逆。

记
$$
\alpha=\min\{1-\sqrt\sigma,\ (1-\sqrt\kappa)(1-\sqrt\rho)\}>0.
\tag{6}
$$
原 R275 的 $P(t)$ 正是 (2) 经两个指定分块同余后的和。所以 (4)–(5) 逐块返回
$$
P(t)\succeq
\alpha\,\operatorname{diag}(F+tC_1,\ I+tL_1,\ L_2+tL_3).
\tag{7}
$$

## 3. 同一真实 Schur 补与原 $H_0$

写
$$
V_0=I+tL_1,\qquad V_2=L_2+tL_3,\qquad
D_0=\operatorname{diag}(C_1^2,V_0).
$$
原三块矩阵为
$$
M(t)=P(t)+W_tW_t^*,\qquad
W_tx=(tx,\sqrt t\,Q^*x,0).
$$
由 $F\succeq\varepsilon C_1^2$ 和 (7)，对第一、第二坐标 $(x,y)$ 固定，取第三坐标的真实变分最小值，得到
$$
\mathscr S(t):=\operatorname{Schur}_{V_2}M(t)
\succeq
\alpha\varepsilon D_0+\widehat W_t\widehat W_t^*,
\qquad
\widehat W_tx=(tx,\sqrt t\,Q^*x).
\tag{8}
$$
理由是 (7) 对每个第三坐标 $z$ 都给至少
$\alpha\varepsilon\langle D_0(x,y),(x,y)\rangle
+\|\widehat W_t^*(x,y)\|^2+\alpha\langle V_2z,z\rangle$；
因此最小化不能损失前两项。

设 $\overline H_0$ 是 R275 中将原 $H_0$ 依次作首剪切和 $\operatorname{diag}(P_1^{-1},I)$ 同余所得矩阵。它的准确二次型为
$$
\langle\overline H_0(x,y),(x,y)\rangle
=
\|(C_1+tI)x+\sqrt t\,Qy\|^2+\|V_0^{1/2}y\|^2.
$$
保留同一个 $Qy$，使用一次两项平方不等式即得
$$
\overline H_0
\preceq
2\bigl(D_0+\widehat W_t\widehat W_t^*\bigr).
\tag{9}
$$
因 $0<\alpha\varepsilon\le1$，(8)–(9) 给
$$
\boxed{\mathscr S(t)\succeq
\frac{\alpha\varepsilon}{2}\overline H_0.}
\tag{10}
$$
$\mathscr S(t)$ 恰是同一原首边差在上述可逆同余后的矩阵。故返回原真实 primitive 空间，得到一般定量蕴含
$$
\boxed{
\Gamma_1^{\rm new}(\Gamma_2^{\rm new})^{-1}\Gamma_1^{\rm new}
\preceq
\left(1-\frac{\alpha\varepsilon}{2}\right)I.
}
\tag{11}
$$
这是 (3) 四项全部实际支付后的条件定理；不把它用于尚未付这些费用的更高出生。

## 4. 六个独立正权的实际常数

把任意六个正权中的一个选作新位，旧五位上出生二为高度一硬端，因此
$$
C_2=0,\qquad F=C_1^2,\qquad \varepsilon=1.
$$
[R298](R298-five-independent-positive-weights-birth-two-hard-top-strengthened-s1.md)给
$\kappa=743/782$；[旧低源严格 half 末边](R271-appendix-four-five-sites-birth-one-half-first-last-edges.md)给
$\rho=1/2$；[新同源 S2 统一余量](R271-appendix-five-site-full-s2-uniform-three-sixteenths-square-budget.md)给
$$
\sigma=(2+\sqrt3)/4.
$$
可以使用简单的公共有理下界 $\alpha=1/160$。确切地，
$$
\frac{743}{782}<\left(\frac{39}{40}\right)^2,\qquad
1-\frac1{\sqrt2}>\frac14,
$$
所以
$$
(1-\sqrt\kappa)(1-\sqrt\rho)>\frac1{160}.
$$
另一方面 $\sqrt3<7/4$ 给
$\sigma<15/16<(39/40)^2$，所以
$1-\sqrt\sigma>1/40>1/160$。
将该公共下界代入 (10)–(11) 即得 (1)。

全部来源仍为旧五位完整上、低源和新九维 $K_2^{(6)}$。此统一有限维首边预算可用于后续真实 joint 递推；它不支付任意位数/出生的四项 (3)，不替代原边界物理头 Gram 或同 $W$ 的实际 Green/范围费用，也不声称普通 ISP 完成。
