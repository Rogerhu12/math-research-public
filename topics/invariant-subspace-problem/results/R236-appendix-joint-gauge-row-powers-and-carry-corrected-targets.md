# R236 附录：联合 gauge 高幂的统一度量与进位修正目标

- 日期：2026-11-13（UTC）
- 作者：AI 辅助研究；normal_complex
- 状态：已证明；root 已独立全文核验对角度量、全部高幂块、目标修正、完整源及实际理想费用
- 范围：原迟首二次行的同一个 gauge、同一个正常见证；全部矩阵为真实有限头。未证明临界慢尾可付。

本文继续
[实际头 MP 与容错目标 §4.9](../results/R236-appendix-exact-head-vacuum-column-and-carry-cost.md)。
先前一次行的 $35/48$ 上界可降至 $35/96$：
全部显式源在同一个对角度量中相乘，只付一次条件数。
同时给出任意合法高幂的完整原像。
高幂相位准确覆盖 $r$ 个方向；其余方向所需的目标修正
只含真实 carry，具有统一的超快范数界。

## 1. 记号与主结论

取原文的
$$
T=X^2-B_0+Y,\qquad
X=\sum a_jQ_j,\quad Y=\sum c_jQ_j,\quad
B_0=\sum a_j^2Q_j^2,\quad a,c\in\ell^1.
$$
固定一个 dyadic $\zeta$，满足 $\zeta^r\ne1$，
其中 $t_rz^r$ 是 $T$ 的稳定形式首项。
共同正态稿允许在同一次有限排除中选择这样的 $\zeta$；
同一个正常泛函遂同时湮灭 $TA'$ 与 $\gamma_\zeta(T)A'$。
不跨不同 gauge 更换见证。

置
$$
p=m+1,\quad H=2^m,\quad
\zeta^H=1,\quad d=rq<H,\quad q\ge1.
\tag{1.1}
$$
$m$ 总取足够大，固定低阶系数已稳定，且 $c_m\ne0$。
沿用真实物理权 $W_k,d_m$ 与锋利低头圆
$$
\rho=\rho_m=e^{-\lambda_m},\qquad
\lambda_m=(100+2^{-m/2})8^{m-1},
$$
$$
F(k)=\lambda_mk+\log W_k,\qquad
F_* =F(H-1)=(35/6+o(1))16^m.
\tag{1.2}
$$
原 bit 权证明准确给 $0\le F(k)\le F_*$。

设 $P_d$ 投影到低头末 $d$ 个坐标，$P_{\rm b}$ 投影到末
$d-r$ 个坐标；当 $q=1$ 时 $P_{\rm b}=0$。
存在显式线性目标算子
$$
\mathcal P_{m,q}=
\begin{pmatrix}
I-P_{\rm b}&K_{m,q}\\
0&I-P_d
\end{pmatrix}
\tag{1.3}
$$
与完整联合源算子 $\mathcal U_{m,q}$，使
$$
[T_p^{q*},\gamma_\zeta(T_p)^{q*}]\,\mathcal U_{m,q}
=\mathcal P_{m,q}.
\tag{1.4}
$$
其中
$$
\boxed{
\|K_{m,q}\|
\le 4^q e^{F_*}\chi_m,\qquad
\chi_m=d_m\rho^{-H}.
}
\tag{1.5}
$$
一致于全部 $rq<H$，
$$
\log(4^q e^{F_*}\chi_m)
=-(245/3+o(1))16^m.
\tag{1.6}
$$
这不是把 carry 直接删除，而是把它准确保在目标中。

另有固定 $C\ge1$ 及一个明确的固定维费用 $b_m(\rho)$，满足
$$
b_m(\rho)\le
\frac{C}{|c_m|}
\sum_{\ell=0}^{r-1}
\left[C\left(1+\frac{|a_m|}{|c_m|}\right)\rho\right]^\ell,
\tag{1.7}
$$
并有完整源上界
$$
\boxed{
\|\mathcal U_{m,q}\|
\le C^{q+1}(q+1)^2(1+b_m(\rho))
\exp\!\left[F_*+(d+r)\lambda_m\right].
}
\tag{1.8}
$$
这个上界已包含两个行源及全部低头 carry。对于 $q>1$，$\mathcal P_{m,q}$ 是秩为 $2H-2d+r$ 的指定目标投影；本稿不声称完整 row 像的每个目标都享受该上界。$q=1$ 的目标才覆盖整个 row 像。

若
$$
\log^+(|c_m|^{-1})=o(16^m),\qquad q=o(H),
\tag{1.9}
$$
则
$$
\limsup 16^{-p}\log^+\|\mathcal U_{m,q}\|
\le\frac{35}{96}.
\tag{1.10}
$$
特别，$q=1$ 时 $\mathcal P_{m,1}$ 正是删去全头最后 $r$
个目标坐标的投影。因此 (1.10) 是完整一次联合 row 的 MP
右逆上界，改进原 §4.9 的乘积估计。
不声称它是精确型或最小费用下界。

## 2. 一个准确对角相似，条件数只付一次

令
$$
\mathcal D_m=\operatorname{diag}(e^{F(k)})_{0\le k<H}.
$$
$J_H$ 为普通前移矩阵，$J_He_k=e_{k+1}$，末坐标映为零。
因为 $A_m=\operatorname{diag}(W_k)J_H
\operatorname{diag}(W_k)^{-1}$，准确有
$$
\boxed{
\mathcal D_m A_m^*\mathcal D_m^{-1}=\rho J_H^*,
\qquad
\|\mathcal D_m\|\,\|\mathcal D_m^{-1}\|=e^{F_*}.
}
\tag{2.1}
$$
对算子或矩形块使用相应的 $\mathcal D_m$ 直和，并记该相似后的
算子为 $\widetilde B$。
所有最后源与目标之间的估计均在这一固定度量中进行，
最后才乘一次 $e^{F_*}$。

若 $h$ 在 $|z|\le\rho$ 附近解析，令
$h^\#(z)=\overline{h(\overline z)}$，则
$$
\widetilde{h(A_m)^*}=h^\#(\rho J_H^*),\qquad
\|\widetilde{h(A_m)^*}\|
\le\sup_{|z|=\rho}|h(z)|.
\tag{2.2}
$$
后一个界可直接由解析乘法算子的有限多项式压缩与 Parseval 得到；
等价地，$J_H^*$ 是单边移位伴随的有限压缩，解析 Toeplitz
压缩的范数不超过边界乘子的范数。
这一步不需要给不同因子各乘一次条件数。

定义低行
$$
x_m(z)=\sum_{j<m}a_jq_j(z),\qquad f_m(z)=z^rg_m(z)
$$
如原 §4.9。锋利圆证明给
$$
|t_r|/2\le |g_m(z)|\le2|t_r|
\quad(|z|\le\rho).
\tag{2.3}
$$
原证明在圆上给 $g_m/t_r$ 一致趋于一；
Rouché 与最大模原理同时支付内部非零和逆的界。

设 $S_q=(T_0^{q*})^\dagger$，其中 $T_0=f_m(A_m)$。
这里 $T_0^{q*}$ 的核为低头前 $d$ 个坐标，像为末 $d$ 个坐标的正交补。
准确最小源在该核的正交补中；对角相似保持这些坐标空间。
直接写出右逆：
$$
\widetilde S_q=
P_{[d,H)}
\,g_m^\#(\rho J_H^*)^{-q}\rho^{-d}J_H^d.
$$
于是
$$
\boxed{\|\widetilde S_q\|\le
s_q:=(2/|t_r|)^q\rho^{-d}.}
\tag{2.4}
$$
插入 $P_{[d,H)}$ 只删去自由核分量，不改变右逆方程；
$J_H^d$ 又使它在目标末 $d$ 个坐标上为零。

定义低行比值
$$
C_m=\left(\zeta^r\frac{g_m(\zeta z)}{g_m(z)}\right)(A_m).
$$
始终使用低行 $g_m$，不是完整最高行 $g_p$。
由 (2.2)--(2.3)，
$$
\boxed{\|\widetilde{C_m^{q*}}\|\le4^q.}
\tag{2.5}
$$

## 3. 完整高幂块与准确的 rank-r 相位接口

按最高位分块，令
$$
E=N_m^{[p]}=\begin{pmatrix}0&0\\I&0\end{pmatrix}.
$$
$E^2=0$ 且它与全部参与的有限头多项式交换。
置
$$
\ell_m(z)=-4a_mx_m(z)-2c_m,\qquad
T_p=f_m(A_p)+E\ell_m(A_p).
$$
则
$$
T_p^q=f_m(A_p)^q+
qE f_m(A_p)^{q-1}\ell_m(A_p).
\tag{3.1}
$$
写为
$$
T_p^q=\begin{pmatrix}T_0^q&0\\L_{0,q}&T_0^q\end{pmatrix},
\qquad
\gamma_\zeta(T_p)^q=
\begin{pmatrix}T_1^q&0\\L_{1,q}&T_1^q\end{pmatrix},
$$
其中 $T_1=f_m(\zeta A_m)$。
全部 carry 均保留于下左块。

原一次行恒等式为
$$
\gamma_\zeta(T_p)-C_m^{[p]}T_p=E U_m,
$$
$$
U_m=2c_m(C_m-I)+4a_m(C_mX_m-X_{m,\zeta}).
$$
因全部因子交换且 $E^2=0$，高幂准确给
$$
\boxed{
\gamma_\zeta(T_p)^q-(C_m^{[p]})^qT_p^q
=E U_{m,q},
}
\tag{3.2}
$$
$$
U_{m,q}=qC_m^{q-1}T_0^{q-1}U_m
=q\zeta^{r(q-1)}
 A_m^{d-r}g_m(\zeta A_m)^{q-1}U_m.
\tag{3.3}
$$
若 $(C_m^{[p]})^q$ 的下左块为 $F_{m,q}$，则
$$
L_{1,q}=C_m^qL_{0,q}+F_{m,q}T_0^q+U_{m,q}.
\tag{3.4}
$$
这些式子没有要求 $\zeta^{rq}\ne1$。

令
$$
J_d=\operatorname{span}\{e_{H-d},\ldots,e_{H-d+r-1}\},\qquad
K_r=\operatorname{span}\{e_{H-r},\ldots,e_{H-1}\}.
$$
$P_d=P_{J_d}+P_{\rm b}$。
(3.3) 的准确阶为 $d-r$，所以
$$
P_{\rm b}U_{m,q}^*=0,\qquad
W_{m,q}=U_{m,q}|_{J_d}:J_d\longrightarrow K_r
$$
是可逆的 $r\times r$ 映射。
这说明相位只覆盖 $r$ 个边界方向，而非 $rq$ 个。

在同一对角度量中，$W_{m,q}^*$ 是
$\rho^{d-r}$ 倍的坐标移位，后接固定 $r$ 维解析矩阵。
该坐标移位在两个标准坐标空间之间等距。
因此准确有
$$
\boxed{
\|(\widetilde{W_{m,q}^*})^{-1}\|
\le
\beta_q:=
\frac{(2/|t_r|)^{q-1}}{q\rho^{d-r}}\,b_m(\rho).
}
\tag{3.5}
$$
这里同样以 $U_m(z)$ 表示 (3.2) 中 $U_m$ 的解析标量芽；
$b_m(\rho)$ 是 $U_m^\#(\rho J_r^*)$ 的逆范数。
$U_m(0)=2c_m(\zeta^r-1)$，
且其前 $r$ 个系数均为 $a_m,c_m$ 的固定线性组合。
非恒定部分在 $\rho J_r^*$ 上的范数至多
$C(|a_m|+|c_m|)\rho$，其 $r$ 次幂为零。
有限 Neumann 和遂给 (1.7)。

在原指数系数中，$(1+|a_m/c_m|)\rho\to0$，
于是更简单地 $b_m(\rho)\le C/|c_m|$。
但主定理只使用完整的 (1.7)。
(3.5) 已显式支付两个边界带之间的 $\rho^{d-r}$；
没有把原物理权跳跃隐藏在局部条件数中。

## 4. carry 角块在同一度量中的准确费用

把 $f_m(A_p)^q$ 的下左块记为 $E_{m,q}$。
由完整权比，其伴随条目为
$$
(E_{m,q}^*)_{i,k}
=d_m\frac{W_k}{W_i}\,
\overline{[z^{H+k-i}]f_m(z)^q}.
\tag{4.1}
$$
相似后，$(i,k)$ 条目是
$d_m\rho^{-H}$ 乘
$[z^{H+k-i}](f_m^\#(\rho z))^q$。
它准确是 $f_m^\#(\rho J_{2H}^*)^q$ 的一个角块，
乘同一个标量 $\chi_m=d_m\rho^{-H}$。
所以
$$
\boxed{
\|\widetilde{E_{m,q}^*}\|
\le\chi_m(2|t_r|)^q\rho^d.
}
\tag{4.2}
$$
并没有把 $E_{m,q}$ 假设为零。

对 $j<m$，原圆满足 $|z^{2^j}/d_j|<1/2$，
故 $|x_m(z)|\le C\|a\|_1$。因此
$$
L_m^\rho:=\sup_{|z|=\rho}|\ell_m(z)|
\le C(|a_m|+|c_m|).
$$
(3.1) 与 (2.2) 给
$$
\|\widetilde{L_{0,q}^*}\|,
\|\widetilde{L_{1,q}^*}\|
\le
q(2|t_r|)^{q-1}\rho^{d-r}L_m^\rho
+\chi_m(2|t_r|)^q\rho^d.
\tag{4.3}
$$

令 $\mathscr D_q(u,v)=L_{0,q}^*u+L_{1,q}^*v$，
并把 (4.3) 右侧乘 $\sqrt2$ 记为 $b_q$。
于是 $\|\widetilde{\mathscr D_q}\|\le b_q$。

## 5. 非坐标目标修正与完整原像

定义
$$
K_{m,q}=P_{\rm b}L_{0,q}^*S_q(I-P_d).
\tag{5.1}
$$
(3.1) 中纯最高位项有阶至少 $d-r$，所以
$$
P_{\rm b}\bigl(qT_0^{q-1}\ell_m(A_m)\bigr)^*=0.
$$
于是 (5.1) 准确等于
$$
P_{\rm b}E_{m,q}^*S_q(I-P_d).
$$
由 (2.4)、(4.2)，
$$
\|\widetilde K_{m,q}\|\le4^q\chi_m.
\tag{5.2}
$$
还原一次对角度量便得 (1.5)。

现在取任意 $f=(f_0,f_1)$，令 $y=\mathcal P_{m,q}f$，
其中 $\mathcal P_{m,q}$ 如 (1.3)。
写
$$
z_0=(S_qy_1,0),\qquad
a=P_d(y_0-\mathscr D_qz_0).
$$
由于 (5.1) 的准确修正，$P_{\rm b}a=0$，
故 $a\in J_d$。定义
$$
v=(W_{m,q}^*)^{-1}a\in K_r,\qquad
n=(-C_m^{q*}v,v),\qquad z=z_0+n,
$$
$$
x=(S_q(y_0-\mathscr D_qz),0).
\tag{5.3}
$$
若 $\mathscr R_q(u,v)=T_0^{q*}u+T_1^{q*}v$，
则 $n\in\ker\mathscr R_q$，而 (3.4) 给
$$
\mathscr D_qn=T_0^{q*}F_{m,q}^*v+U_{m,q}^*v.
$$
投到末 $d$ 坐标后，它准确等于 $W_{m,q}^*v=a$。
所以 (5.3) 合法，且
$$
\mathscr R_qz=y_1,\qquad
\mathscr R_qx+\mathscr D_qz=y_0.
$$
把源上下半重新合并，便得到 (1.4) 的完整联合源。
未遗漏未压缩的上半方程，也未舍去 $F_{m,q}$ 的作用；
后者在边界投影中消去，在全方程中由 $x$ 支付。

在同一度量中，令 $c_q=(1+16^q)^{1/2}$。
逐项估计 (5.3)，完整费用不超过
$$
\begin{aligned}
\|\widetilde{\mathcal U}_{m,q}\|
\le{}&(1+4^q\chi_m)\\
&\cdot\left\{
s_q+(1+b_qs_q)
 [s_q+c_q\beta_q(1+b_qs_q)]
\right\}.
\end{aligned}
\tag{5.4}
$$
这是未作渐近简化的准确充分预算。

对全部 $rq<H$，有 $4^q\chi_m\to0$ 一致。
$a,c$ 有界，故 (2.4)、(3.5)、(4.3) 推出
$$
1+b_qs_q\le C^{q+1}(q+1)\rho^{-r}.
$$
把它代回 (5.4)，得到
$$
\|\widetilde{\mathcal U}_{m,q}\|
\le C^{q+1}(q+1)^2(1+b_m(\rho))\rho^{-(d+r)}
$$
（增大一个与 $m,q$ 无关的 $C$）。
最后只乘一次 $e^{F_*}$，即为 (1.8)。

## 6. 目标锚与实际正常泛函的接合

由原权公式，
$$
-\log d_m
=100\,16^m-105\,8^m+(150m+25)2^m,
$$
$$
H\lambda_m=(25/2+o(1))16^m.
$$
结合 (1.2)，得到 (1.6)，一致于 $rq<H$。
所以 $\mathcal P_{m,q}$ 与其坐标投影部分之差范数趋零。

对真空，坐标投影部分删除 $2d-r$ 个坐标。
因此
$$
\|\mathcal P_{m,q}\Omega-\Omega\|
\le\sqrt{\frac{2d-r}{2H}}+4^q e^{F_*}\chi_m.
\tag{6.1}
$$
若 $d=oH$，这给强真空目标。
但不能仅由向量强收敛就免费宣称其实际乘子统一有界。

为直接接正常泛函，固定 dyadic $\theta\in(0,1)$，
在每个长度 $H$ 的物理块中删去末 $\theta H$ 个坐标，
记这个投影为 $Q_m^\theta$，并要求
$$
d\le\theta H.
\tag{6.2}
$$
取
$$
f=Q_m^\theta\Omega,\qquad
y=\mathcal P_{m,q}f.
$$
此时目标的坐标投影部分恰保留 $f$，所以
$$
\|y-f\|\le4^q e^{F_*}\chi_m.
\tag{6.3}
$$
原 §4.8 给统一有界的实际乘子
$$
\Theta_m=X_{Cf},\qquad
\Theta_m\longrightarrow(1-\theta)I\quad\mathrm{WOT}.
$$
本次真正目标对应的乘子满足
$$
\|X_{Cy}-\Theta_m\|
\le K_p\,4^q e^{F_*}\chi_m\longrightarrow0,
\qquad K_p=10^{p/2}.
\tag{6.4}
$$
因此非坐标修正同时保持实际非零正常锚。

设 $\widehat T_p$ 为原实际低行，
$\epsilon_p=\|\widehat T_p-T_p\|$，
$r_p=\|T-\widehat T_p\|$，
$D_p\le6p\eta_{p-1}K_p$，$M$ 统一控制实际和局部范数。
$\gamma_\zeta$ 是等距自同构，另一行费用相同。
把 (1.4) 的两个源记为 $u_p,v_p$。
原 §4.8 的准确乘法字典与差幂恒等式给某些实际右因子
$F_p,G_p\in\mathcal A$，且
$$
\begin{aligned}
\|TF_p+\gamma_\zeta(T)G_p-\Theta_m\|
\le{}&
K_p4^q e^{F_*}\chi_m+D_p\|y\|\\
&+\left[K_pr_p^q+M^qD_p+
qM^{q-1}\epsilon_pK_p\right]
(\|u_p\|+\|v_p\|).
\end{aligned}
\tag{6.5}
$$
所以若完整右侧趋零，便以同一个 $\rho$ 得到矛盾。
这仍是全实际理想恒等式，不把 $Q_m^\theta$ 当作 $A'$ 元素。

(6.4) 的目标修正对全部 $rq<H$ 都可付，不需要附加的系数下界。若另有 $\log^+(|c_m|^{-1})=o(16^m)$（特别包括原伸展指数族），则源放大后的真实 carry 项也在本节预算下可付；此处必须保留这一条件。
然而当原慢尾只有 $r_p\le Ce^{-\beta p^\alpha}$ 时，
把 (1.8) 代入 (6.5) 尚不能支付 $K_pr_p^q$ 项：
此处 $H=2^{p-1}$，$rq<H$，
而 $qp^\alpha=O(Hp^\alpha)=o(H^4)$。
这说明目前单层上界尚不够，不是对真实最小费用的下界，
更不构成临界联合路线的否定。

## 7. 可供继续递推的准确内容

本稿交付三个可以直接复用的对象：

1. 同一对角相似把所有实际低头伴随解析矩阵变成
   $\rho J_H^*$ 的函数，全部卷积只付一次 $e^{F_*}$。
2. 高幂相位覆盖恰为 $r$ 维；未覆盖方向的返回只含 carry，
   由 (5.1) 的非坐标目标修正准确处理，误差在全部合法 $q$ 下统一。
3. 完整联合源为 (5.3)，实际目标锚和全费用为 (6.4)--(6.5)。

它们没有证明多层组合仍保同一个小头条件数，
也没有把低行比值替换为完整最高行比值。
下一步须在完整联合 Schur 度量或等价的同时卷积中控制多层费用，
不能把本节一次相似的结论逐层相乘后忽略新的条件数。
