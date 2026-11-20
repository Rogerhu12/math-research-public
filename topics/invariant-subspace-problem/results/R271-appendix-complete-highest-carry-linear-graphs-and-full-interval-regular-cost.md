# R271 补录：完整最高 carry 真核的线性图、全实参数投影导数与正则部分明确界

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / r271_cost；AI-assisted GPT-6 Astra Pro。

状态：**完整真核/余核图及全实区间正则部分上界已证明；最终费用预算仍开放。**

## 0. 范围

本条补齐“固定参数存在解析展开”与“原最高 carry 已进入某个有效区”之间的区别。
对原偶强段、奇高度的最高 carry 块，本条给出完整真核及余核的精确线性图。
由此，物理核投影导数和完整 Galerkin 源导数在整个 $0<t\le1$ 上有明确界；
原完整 MP 解减去最高极点后的正则部分也有全区间上界。

所用父结论为：

- [R271-appendix-odd-height-highest-carry-full-mp-simple-pole.md](R271-appendix-odd-height-highest-carry-full-mp-simple-pole.md) 的精确物理剪切；
- [R271-appendix-complete-galerkin-highest-carry-pole-and-cancellation-criterion.md](R271-appendix-complete-galerkin-highest-carry-pole-and-cancellation-criterion.md) 的完整源与最小范数；
- [R271-appendix-median-strong-tail-scaling-four-power-condition-and-full-odd-height-cost.md](R271-appendix-median-strong-tail-scaling-four-power-condition-and-full-odd-height-cost.md) 的原强尾常数。

本条的明确上界可能仍大于原费用门可承受的预算。
它不声称原代表费用已经变小，不把局部有限头结果称为普通 Hilbert ISP 的解。

## 1. 完整物理最高块

固定旧完整头 $A$、偶数 $R$ 个完整强位和奇数 $r\ge1$。
令
$$
D=A+D_R,\quad Z=D^r,\quad b=b_{m-1},
$$
$$
C_t=\begin{pmatrix}D&bI+tV\\0&D\end{pmatrix},
\quad
X_t=C_t^r=
\begin{pmatrix}Z&B_0+tT\\0&Z\end{pmatrix},
\tag{1.1}
$$
其中
$$
B_0=rbD^{r-1},\qquad
T=\sum_{j=0}^{r-1}D^jVD^{r-1-j}.
\tag{1.2}
$$
这些都是原物理内积中的整个矩阵。
最高位只可能通过一次，所以 $X_t$ 确实对 $t$ 线性。

旧头维数为偶数；偶强段的 Boolean 尾链长为奇数。
因此 $D$ 的所有 Jordan 链长为偶数，奇 $r$ 不等于任何链长。
这精确保证
$$
P_{\ker Z^*}B_0|_{\ker Z}=0.
\tag{1.3}
$$
(1.3) 的伴随也成立。
它不要求选一个非正交 Jordan 基来计算物理投影。

## 2. 完整真核与余核的精确线性图

置
$$
U=\ker Z,\qquad U_*=\ker Z^*,
$$
$$
V_0=U\cap\ker(P_{U_*}T),\qquad
W_0=U_*\cap\ker(P_UT^*).
\tag{2.1}
$$
这些子空间与 $t$ 无关。

### 定理 2.1

对每个 $t>0$，整个真核为正交直和
$$
\boxed{
\ker X_t=
(U\oplus0)\ \mathbin{\perp}\ 
\{(-Z^\dagger(B_0+tT)v,v):v\in V_0\}.
}
\tag{2.2}
$$
整个余核为正交直和
$$
\boxed{
\ker X_t^*=
(0\oplus U_*)\ \mathbin{\perp}\ 
\{(u,-(Z^*)^\dagger(B_0^*+tT^*)u):u\in W_0\}.
}
\tag{2.3}
$$

**证明。** $X_t(u,v)=0$ 先给 $Zv=0$，再给
$Zu=-(B_0+tT)v$。
由 (1.3)，该方程的兼容性恰为
$tP_{U_*}Tv=0$，即 $v\in V_0$。
全部解为
$$
u=-Z^\dagger(B_0+tT)v+u_0,\qquad u_0\in U.
$$
$Z^\dagger$ 的像在 $U^\perp$，所以两族列物理正交。
伴随方程同理，得到 (2.3)。证毕。

把 (2.2)–(2.3) 的 $t$ 置为 $0$，得到 $t\downarrow0$ 的真核与余核极限；
它们一般严格小于 $\ker X_0$ 与 $\ker X_0^*$。
本条不把这两类空间混同。

记这些连续真核投影为
$$
\Pi_t=P_{\ker X_t},\qquad
Q_t=P_{\ker X_t^*},\qquad 0<t\le1,
$$
并按上述图在 $t=0$ 延拓。令
$$
\boxed{
L=\max\{\|Z^\dagger T\|,\ \|TZ^\dagger\|\}.
}
\tag{2.4}
$$

### 推论 2.2

在整个 $0\le t\le1$ 上，
$$
\boxed{
\|\Pi_t'\|\le2L,\qquad
\|Q_t'\|\le2L.
}
\tag{2.5}
$$
特别地
$$
\|\Pi_t-\Pi_0\|,\ \|Q_t-Q_0\|\le2Lt.
\tag{2.6}
$$

**证明。** 对固定子空间上的图框架
$J_t v=(A_0v+tA_1v,v)$，底部为恒等映射，故
$$
J_t^*J_t\ge I,\qquad \|J_t^\dagger\|\le1.
$$
其范围投影满足
$$
P_t'=(I-P_t)J_t'J_t^\dagger+
(J_t^\dagger)^*(J_t')^*(I-P_t),
$$
所以 $\|P_t'\|\le2\|A_1\|$。
(2.2) 的斜率为 $-Z^\dagger T|_{V_0}$；
(2.3) 的斜率为
$-(Z^*)^\dagger T^*|_{W_0}=-(TZ^\dagger)^*|_{W_0}$。
各自的固定自由核块与图始终正交，加入它们不改变导数界。
证毕。

这里没有“需要 $t$ 小于某未知半径”的条件。

## 3. 完整 Galerkin 源的全区间导数

固定源 $f$ 和 $S>0$，置
$$
H_t=\sum_{j=0}^{r-1}
\frac{(C_t^*)^jC_t^j}{j!S^j}\ge I.
\tag{3.1}
$$
令 $a_t\in\operatorname{Ran}\Pi_t$ 是完整物理 Galerkin 解，
$$
\Pi_tH_ta_t=\Pi_tf,\qquad
\xi_t=f-H_ta_t.
\tag{3.2}
$$
在 $t=0$ 使用真核极限 $\operatorname{Ran}\Pi_0$；
因 (2.2)，这就是完整原 Galerkin 解的真极限。

设整个区间上
$$
\|H_t\|\le h,\qquad \|H_t'\|\le h_1.
\tag{3.3}
$$
由于 $H_t\ge I$，有
$$
\|a_t\|\le\|f\|,\qquad
\|\xi_t\|\le(h+1)\|f\|.
\tag{3.4}
$$

### 定理 3.1

对全部 $0\le t\le1$，
$$
\boxed{
\|a_t'\|
\le[\,h_1+(4h+4)L\,]\|f\|,
}
\tag{3.5}
$$
$$
\boxed{
\|\xi_t'\|
\le(h+1)[\,h_1+4hL\,]\|f\|.
}
\tag{3.6}
$$

**证明。** 在整个物理空间中引入
$$
M_t=\Pi_tH_t\Pi_t+I-\Pi_t.
$$
它在 $\operatorname{Ran}\Pi_t$ 上为正定 Galerkin 算子，
在正交补上为恒等，故 $M_t\ge I$ 且
$$
a_t=M_t^{-1}\Pi_tf,\qquad \|M_t^{-1}\|\le1.
$$
微分并用 (2.5)：
$$
\|M_t'\|\le(2h+1)\|\Pi_t'\|+h_1
\le(4h+2)L+h_1.
$$
因此
$$
\|a_t'\|\le\|M_t'\|\|a_t\|+\|\Pi_t'\|\|f\|,
$$
给 (3.5)。再由
$\xi_t'=-H_t'a_t-H_ta_t'$
得到 (3.6)。证毕。

若 $\|C_t\|\le c_0$、$\|C_t'\|=\|V\|\le v_0$，可明确取
$$
h=\sum_{j=0}^{r-1}\frac{c_0^{2j}}{j!S^j},
\qquad
h_1=\sum_{j=1}^{r-1}
\frac{2jv_0c_0^{2j-1}}{j!S^j}.
\tag{3.7}
$$
这里没有压缩原核或省略物理 Gram 混合项。

## 4. 固定物理剪切给出一个精确解

令
$$
P=Z^\dagger D^{r-1},\qquad
Q=(I-ZZ^\dagger)D^{r-1}Z^\dagger.
$$
由 $D$ 没有长度 $r$ 的链，
$$
D^{r-1}=ZP+QZ.
\tag{4.1}
$$
取固定剪切
$$
\mathcal L=\begin{pmatrix}I&-rbQ\\0&I\end{pmatrix},
\qquad
\mathcal R=\begin{pmatrix}I&-rbP\\0&I\end{pmatrix}.
$$
于是
$$
\mathcal LX_t\mathcal R=
\begin{pmatrix}Z&tT\\0&Z\end{pmatrix}
=G_tX_{\rm ref}G_t^{-1},
$$
$$
G_t=\operatorname{diag}(tI,I),\qquad
X_{\rm ref}=\begin{pmatrix}Z&T\\0&Z\end{pmatrix}.
\tag{4.2}
$$
$X_{\rm ref}$ 正是删除最高 Boolean 项、最高参考 carry 取 $1$ 的完整 $r$ 次幂。

记
$$
K=(X_{\rm ref}^*)^\dagger,\qquad
K=\begin{pmatrix}K_{11}&K_{12}\\K_{21}&K_{22}\end{pmatrix}.
$$
因为 $\xi_t\perp\ker X_t$，向量
$$
\widetilde q_t=
\mathcal L^*G_t^{-1}KG_t\mathcal R^*\xi_t
\tag{4.3}
$$
满足整个方程 $X_t^*\widetilde q_t=\xi_t$。
原完整最小范数解为
$$
q_t=(I-Q_t)\widetilde q_t.
\tag{4.4}
$$

定义固定矩阵与线性矩阵
$$
A_*=\mathcal L^*
\begin{pmatrix}0&K_{12}\\0&0\end{pmatrix}\mathcal R^*,
$$
$$
B_t=\mathcal L^*
\begin{pmatrix}K_{11}&0\\tK_{21}&K_{22}\end{pmatrix}\mathcal R^*.
\tag{4.5}
$$
则
$$
\widetilde q_t=t^{-1}A_*\xi_t+B_t\xi_t.
\tag{4.6}
$$
置
$$
\boxed{
K_0=\|\mathcal L\|\,\|\mathcal R\|\,\|X_{\rm ref}^\dagger\|.
}
\tag{4.7}
$$
对全部 $0\le t\le1$，
$$
\|A_*\|\le K_0,\qquad \|B_t\|\le2K_0.
\tag{4.8}
$$
最终投影 $I-Q_t$ 很重要；(4.3) 本身一般不是物理最小范数解。

## 5. 完整最高极点与全实参数正则界

由 (4.4)–(4.6)，极点系数精确为
$$
\boxed{
q_{-1}=(I-Q_0)A_*\xi_0.
}
\tag{5.1}
$$
这也等于完整 Schur 极点方程的最小物理范数解。

### 定理 5.1

对每个 $0<t\le1$，
$$
\boxed{
\|q_t-t^{-1}q_{-1}\|
\le K_0(h+1)
[\,h_1+(4h+2)L+2\,]\,\|f\|.
}
\tag{5.2}
$$
因此，原实际 $t$ 无需先落入一个未知解析邻域，就有
$$
\boxed{
\|q_t\|\le
t^{-1}\|q_{-1}\|
+
K_0(h+1)[\,h_1+(4h+2)L+2\,]\|f\|.
}
\tag{5.3}
$$

**证明。** 记 $P_t=I-Q_t$。
准确拆分
$$
q_t-t^{-1}q_{-1}
=
t^{-1}(P_t-P_0)A_*\xi_t
+t^{-1}P_0A_*(\xi_t-\xi_0)
+P_tB_t\xi_t.
$$
第一项用 (2.6)、(3.4)、(4.8)；
第二项用全区间源导数 (3.6)；
第三项用 $\|P_t\|=1$ 和 (4.8)。
相加即为 (5.2)。证毕。

若后续有更好的实际源界，完全相同证明给更精细的接口
$$
\|q_t-t^{-1}q_{-1}\|
\le K_0\bigl[(2L+2)M_\xi+M_{\xi'}\bigr],
\tag{5.4}
$$
其中
$$
M_\xi=\sup_{0\le u\le t}\|\xi_u\|,\qquad
M_{\xi'}=\sup_{0\le u\le t}\|\xi_u'\|.
$$
这些都是原完整源，没有改动代表或真核旗。

## 6. 原强段的全部明确常数

取原 $m\ge4$、偶 $R\ge d=2^m$、奇 $1\le r\le m+R$，
$$
n=d/2,\qquad a=16^{m-2},\qquad y=m+R/2.
$$
使用已证旧头与参考头条件数
$e^{221a}$、$e^{441a}$，以及中位强尾归一化 $4^R$。

旧 $Z=D^r$ 的完整物理 MP 可取
$$
\boxed{
Z_{\rm bd}=
e^{221a}4^R
\frac{y^{2n+2r-2}}{(n-1)!\,r!},
\qquad
\|Z^\dagger\|\le Z_{\rm bd}.
}
\tag{6.1}
$$
由 $\|D\|<8$、$\|V\|\le6$，
$$
\|T\|\le6r\,8^{r-1},
$$
因此
$$
\boxed{L\le6r\,8^{r-1}Z_{\rm bd}.}
\tag{6.2}
$$
已证物理剪切和参考 MP 给
$$
\boxed{
K_0\le
e^{883a}64^R(1+rb)^2 8^{2r-2}
\frac{y^{4d+6r-6}}
{((n-1)!)^2(d-1)!(r!)^3}.
}
\tag{6.3}
$$
这正是最高简单极点完整 MP 的显式常数；没有再把 Jordan 相似漏掉。

从块式可统一取
$$
\|C_t\|\le16,\qquad \|C_t'\|\le6
\quad(0\le t\le1).
$$
因而可在 (3.7) 取 $c_0=16,v_0=6$。
特别对 $r=3$，
$$
h=1+256/S+32768/S^2,
$$
$$
h_1=192/S+49152/S^2,\qquad
L\le1152Z_{\rm bd}.
\tag{6.4}
$$
将 (6.1)、(6.3)、(6.4) 直接代入 (5.2)，便是原完整三孔正则部分、
对全部真实 $0<t\le1$ 的明确上界。

若旧权按最大旧 carry 重标度，且原逆芽与输入权上界保持，
同样可用这些常数；否则用其实际有限头条件数替代。
所有强段 $R$、高度 $r$、远尾 $S$ 成本都已列出。

## 7. 尚需改善的实际费用

本条已经给出全实区间的正则估计，故不能再把未知有效半径作为这条估计的前提。
但 (5.2) 的粗源控制以及 (6.2) 的最坏矩阵范数可能非常大；
对增长强段，其显式上界含至多又一次 $4^R$ 与旧头条件数。
把这个上界与纯 far-height 归一化相乘，目前仍未证明满足原倒数费用门。

可继续改进的具体项是 (5.4) 中的原完整
$M_\xi,M_{\xi'}$，或者直接利用
$(P_t-P_0)A_*\xi_t$ 的孔支撑，
而不是分别取三个最大范数。
本条保留这些缺口；没有据有限矩阵上界声称 $N=M$。
