# 实际慢边界核上的伴随下界与强制正的混合压缩

日期：2026-11-12（UTC）。作者：boundary_next。状态：已证明，中间结论。

本稿续接 [首位小图附录](../results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)。
对两个实际慢核 $M=\ker T_N,\ker T_Y$，证明
$$
\|T^*w\|\ge\frac78\|w\|\quad(w\in M),
$$
以及
$$
\operatorname{Re}\langle P_MBT^*w,w\rangle
\ge\frac56\alpha_0\|w\|^2\quad(w\in M).
$$
因此 $P_MBT^*|_M$ 是有界可逆算子。这些预像来自 $T^*M\subseteq M^\perp$，没有成为 $BM$ 的原像；故尚未推出 $N=M$。

## 1. 精确输入与统一常数

采用首位附录的原定义。按最低位真空／占满分解，
$$
B=\alpha_0\begin{pmatrix}0&I\\R&0\end{pmatrix},
\qquad R=\eta Z,\qquad
\alpha_0=e^{-20},\quad\eta=e^{-1070},\quad\|Z\|=1.
$$
两个实际模型分别有
$$
H_N=S_N,\qquad H_Y=(I-R)S_Y-R,
$$
以及
$$
\widetilde T=\begin{pmatrix}H&I\\R&H\end{pmatrix}.
$$
对 $N$ 模型，$\widetilde T=T$；对 $Y$ 模型，
$$
\widetilde T=UT,\qquad
U=\operatorname{diag}(I-R,I-R),\qquad \|I-U\|\le\eta.
\tag{1.1}
$$
所有 $T,H,R$ 均是实际有界算子；原统一界 $\|T\|\le6$ 足够。

令 $L=\ker(H^2-R)$，$C=H|_L$。首位附录已经给
$$
M=\{Jx:x\in L\},\qquad Jx=(x,-Hx),
$$
$$
C^2=\eta Z|_L,\qquad
\|C\|\le r<\frac1{\sqrt{12}},\qquad
\|H\|<1,
\tag{1.2}
$$
$$
\|x\|^2\le\|Jx\|^2\le(1+r^2)\|x\|^2.
\tag{1.3}
$$
其中 $\|H\|<1$ 也直接来自已付清的
$H=A_{\rm pure}+E$、$\|A_{\rm pure}\|<2/3$、$\|E\|\le2\eta$。
不把 $C^*$ 与环境 $H^*$ 混同。

由 (1.1)，
$$
\boxed{\|T-\widetilde T\|\le6\eta}
\tag{1.4}
$$
在两模型中都成立；$N$ 型左侧实际为零。

## 2. $T^*$ 在真实核上的统一下界

固定 $w=Jx\in M$。真正的矩阵给
$$
\widetilde T^*w=
\begin{pmatrix}
H^*x-R^*Hx\\
x-H^*Hx
\end{pmatrix}.
\tag{2.1}
$$
虽然 $H^*Hx$ 不必在 $L$，与 $x$ 的环境配对仍准确成立：
$$
\langle x-H^*Hx,x\rangle
=\|x\|^2-\|Hx\|^2
\ge(1-r^2)\|x\|^2.
$$
Cauchy–Schwarz 及 (1.3) 给
$$
\|\widetilde T^*w\|
\ge(1-r^2)\|x\|
\ge\frac{1-r^2}{\sqrt{1+r^2}}\|w\|
>\frac{11}{\sqrt{156}}\|w\|
\quad(w\ne0).
\tag{2.2}
$$
最后使用 $r^2<1/12$；函数 $(1-u)/\sqrt{1+u}$ 在 $u\ge0$ 递减。

再由 (1.4)，
$$
\|T^*w\|\ge
\left(\frac{11}{\sqrt{156}}-6\eta\right)\|w\|
\ge\frac78\|w\|.
\tag{2.3}
$$
这个有余量的常数可不用小数核验：
$11/\sqrt{156}>22/25$，而
$22/25-7/8=1/200$，且 $6\eta<6\cdot10^{-6}<1/200$。

因此
$$
\boxed{\|T^*w\|\ge\frac78\|w\|\qquad(w\in M).}
\tag{2.4}
$$
特别 $T^*M$ 是环境空间的闭子空间，并且
$$
T^*M\subseteq M^\perp
\tag{2.5}
$$
来自 $M=\ker T$，不是额外的约化假设。

记 $A=P_MT:\mathcal H_-\to M$，则 $A^*=T^*|_M$。
由闭值域定理，(2.4) 等价于 $A$ 满射，并有取值于 $T^*M$ 的右逆
$$
\boxed{
R_T=T^*|_M\,(P_MTT^*|_M)^{-1},
\qquad P_MTR_T=I_M,\qquad \|R_T\|\le\frac87.
}
\tag{2.6}
$$
这些是投影后的原像，不是 $T$ 的右逆到其完整目标，也不是核内原像。

## 3. 混合压缩的准确正主项

仍取 $w=Jx$。由 (2.1) 和 $B$ 的真实两行，
$$
B\widetilde T^*w
=\alpha_0\begin{pmatrix}
x-H^*Hx\\
RH^*x-RR^*Hx
\end{pmatrix}.
$$
故采用内积对第一变量线性的约定，
$$
\begin{aligned}
\langle B\widetilde T^*w,w\rangle
=\alpha_0\bigl(
&\|x\|^2-\|Hx\|^2\\
&-\langle RH^*x,Hx\rangle
+\langle RR^*Hx,Hx\rangle
\bigr).
\end{aligned}
\tag{3.1}
$$
最后一项是实非负数。第三项绝对值满足
$$
|\langle RH^*x,Hx\rangle|
\le\eta\|H\|\|x\|\|Hx\|
\le\eta r\|x\|^2.
$$
于是由 $\|H\|<1$、$r<1$，
$$
\operatorname{Re}\langle B\widetilde T^*w,w\rangle
\ge
\alpha_0(1-r^2-\eta r)\|x\|^2
\ge\alpha_0\left(\frac{11}{13}-\eta\right)\|w\|^2.
\tag{3.2}
$$
这里把正主项除以 $1+r^2$，而误差使用 $\|x\|\le\|w\|$。
没有把正交压缩后的自交换子换成环境自交换子。

$\|B\|=\alpha_0$，所以 (1.4) 再给
$$
\left|
\langle B(T^*-\widetilde T^*)w,w\rangle
\right|\le6\alpha_0\eta\|w\|^2.
$$
因此
$$
\operatorname{Re}\langle BT^*w,w\rangle
\ge\alpha_0\left(\frac{11}{13}-7\eta\right)\|w\|^2
\ge\frac56\alpha_0\|w\|^2,
\tag{3.3}
$$
因为 $11/13-5/6=1/78>7\cdot10^{-6}$。

令
$$
Q=P_MBT^*|_M.
$$
则最终有
$$
\boxed{
\operatorname{Re}\langle Qw,w\rangle
\ge\frac56\alpha_0\|w\|^2\qquad(w\in M).
}
\tag{3.4}
$$
同一界也对 $Q^*$ 成立，因为二者的实部二次型相同。
故 $Q,Q^*$ 均有下界 $5\alpha_0/6$；$Q$ 像闭、像正交补为 $\ker Q^*=0$，因而满射。于是
$$
\boxed{Q\text{ 有界可逆},\qquad
\|Q^{-1}\|\le\frac6{5\alpha_0}.}
\tag{3.5}
$$

还可以把 $Q$ 写成真正的压缩交换子：
由于 $BM\subseteq M$，对 $w\in M$ 有 $T^*Bw\in M^\perp$，故
$$
\boxed{
Q=P_M[B,T^*]|_M.
}
\tag{3.6}
$$
(3.6) 没有删除交换子压缩的额外块；(3.1) 已逐项支付它们。

## 4. 闭横向空间中的 $B$ 原像与剩余边界

由 (3.5)，
$$
\boxed{
R_{B,T}=T^*Q^{-1}:M\to T^*M\subseteq M^\perp,
\qquad P_MBR_{B,T}=I_M.
}
\tag{4.1}
$$
可取粗界 $\|R_{B,T}\|\le36/(5\alpha_0)$。
此外 $P_MB|_{T^*M}:T^*M\to M$ 本身是一一满射；
因为 $T^*|_M$ 一一，且其与该限制的复合就是 $Q$。

这强化了首位附录中 $P_MB$ 满到 $M$ 的环境结论：
现在原像可限定在明确的闭横向空间 $T^*M$ 中。
它仍然没有把原像放进 $M$。目标
$$
N=\overline{BM}=M
$$
要求核内原像的稠密性，而 (4.1) 的非零原像位于与核正交的方向。

例如对 $d\in M\ominus\overline{BM}$，有
$P_MB^*d=0$，但 $B^*d,T^*d$ 均可为非零的 $M^\perp$ 向量，
且 (3.4) 正是它们配对实部的统一正下界。这与缺陷定义相容，
不能由此宣称缺陷消失。
