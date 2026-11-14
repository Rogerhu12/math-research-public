# R271 附录：任意远尾 primitive 出生的回缩与实际两费用源删除

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；boundary_resume_2220 提供采用原两已付费用正交投影的接口。

状态：**已证明。** 本稿把[原强位回缩](R271-appendix-original-tail-strong-bit-boson-retraction-and-same-source-high-schur-bound.md)的远尾真空列换成任意原 primitive 空间的短 canonical 列，费用使用已经证明的 $HP\delta$ 界。模型没有高输入时，得到原闭源子空间上的 $\lambda\le C\alpha$。

随后使用[真正负源图与实际窗口归约](R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)的原两费用度量，对该具体源子空间作真正正交投影。这样删去的是原实际源中的一小部分，原源和新残源的混合 $\lambda_{\rm flat}$ 均已支付；不要求移动模型源自身逼近固定缺陷向量，也不把投影后的约束改写成物理坐标为零。

## 1. 保留整个远尾 primitive 空间的短回缩

保留原 $m\ge5,d=2^m,A=A_m,D=D_m$ 和合法 $q$。取非负整数
$$
k,n,b,t,\qquad q=n+b+t.
\tag{1.1}
$$
前 $k$ 个真实尾位保持为强位，随后 $n$ 个原相邻暗对占据 $n$ 孔，远尾起点为
$$
J=m+k+2n.
$$
在完整原远尾上记
$$
D_J=\sum_{j\ge J}(j+1)^{-2}E_j,\quad
S=S_J,\quad
K_b^{(J)}=\ker D_J\cap\mathcal H_b^{(J)},\quad
\delta_J\le\frac3{J+1}.
$$
这个 $K_b^{(J)}$ 是整个原 Hilbert primitive 空间，不选某条对称线，也不要求其向量是暗对乘积。

设
$$
H=t+d+1,\qquad P=b+t+d,\qquad
\boxed{\theta=\frac{12HP}{J+1}<\frac12.}
\tag{1.2}
$$
于是 $4\delta_JHP\le\theta$。使用[短核 canonical Fock 塔](R271-appendix-short-canonical-fock-flags-and-q-over-d-prefix-window.md)，置
$$
\boxed{
\kappa^2=\frac{1-\theta}{1-2\theta},\qquad
R=\exp\!\frac2{m+k+1},\qquad C=R\kappa.
}
\tag{1.3}
$$

对 $0\le r\le t+d$ 定义真正的远尾分析行及截面
$$
T_{b,r}=
\frac{P_{K_b^{(J)}}D_J^r}{\sqrt{r!S^r}}
:\mathcal H_{b+r}^{(J)}\to K_b^{(J)},
$$
$$
B_{b,r}f=
\sqrt{r!S^r}\,
D_{J,b+r}^{\dagger}\cdots D_{J,b+1}^{\dagger}f.
\tag{1.4}
$$
$r=0$ 时分别为 $P_{K_b^{(J)}}$ 与包含。所有单步逆均在原完整物理孔层上取；(1.4) 的乘积不称为真幂 MP 逆。

它们满足
$$
\boxed{
T_{b,r}B_{b,r}=I,\quad
T_{b,r-1}D_J=\sqrt{rS}\,T_{b,r},\quad
D_JB_{b,r}=\sqrt{rS}\,B_{b,r-1}.
}
\tag{1.5}
$$
而且
$$
\boxed{\|T_{b,r}\|\le1,\qquad \|B_{b,r}\|\le\kappa.}
\tag{1.6}
$$
分析行界来自原创建列
$(D_J^*)^r/\sqrt{r!S^r}|_{K_b^{(J)}}$：它是真玻色等距创建列的平方自由正交压缩，故为收缩。截面正是原短 canonical 塔的出生 $b$ 列；最高创建高度 $r<H$，最高物理孔数不超过 $P$，所以 (1.2) 支付整个使用窗口。

令模型为 $k$ 个真实强位、一个标准玻色模式和 Hilbert 系数空间 $K_b^{(J)}$：
$$
\mathsf D=
\left(\sum_{i=m}^{m+k-1}(i+1)^{-2}E_i
+\sqrt S\,\mathfrak b\right)\otimes I_{K_b^{(J)}}.
\tag{1.7}
$$
模型的 active 孔数不计固定的 primitive 出生 $b$；源 active 孔数为 $t$。原孔数与它相差固定的 $n+b$。

将 (1.4) 与原中间暗对泛函及单位暗向量张量，得到
$$
\boxed{
\mathsf T\mathsf B=I,\quad
\|\mathsf T\|\le R,\quad \|\mathsf B\|\le\kappa,
}
$$
$$
\boxed{
\mathsf TD=\mathsf D\mathsf T,\qquad
D\mathsf B=\mathsf B\mathsf D.
}
\tag{1.8}
$$
原层低于 $n+b$ 时，$\mathsf T$ 为零。所有强位、原头及完整核旗均保留。与真空回缩相同，不宣称这两个非酉映射与正交核投影交换。

## 2. 没有高输入的整个原闭源子空间

模型的首源旗为
$$
\widehat{\mathscr R}_t
=\bigoplus_{i=0}^{d-2}
e_i\otimes
\bigl(\ker\mathsf D^{d-i-1}\cap\mathsf H_t\bigr).
$$
定义原源中的闭子空间
$$
\boxed{
\mathscr E=\mathsf B_t\widehat{\mathscr R}_t
\subseteq\mathscr R_q.
}
\tag{2.1}
$$
它是闭的，因为 $\mathsf T_t\mathsf B_t=I$，故截面在该源域上下方有界。

假设
$$
\boxed{k\le t+1.}
\tag{2.2}
$$
有限的“强位＋单模式”层在 active 孔数至少 $k$ 后恒为 $2^k$ 维。其
$$
\mathsf D^{j-1}:\mathsf H_{t+j}\to\mathsf H_{t+1}
$$
在每个右段上是方形可逆矩阵张量 $I_{K_b^{(J)}}$，所以
$\ker\mathsf D^{j-1}|_{\mathsf H_{t+j}}=0$。这个论证先在有限矩阵上成立，再张量整个 $K_b^{(J)}$；没有在无限维中用“同维满射”冒充可逆。

因此模型高输入为零，$\widehat\lambda=\widehat\alpha$。上一稿的保高域距离论证遂给
$$
\boxed{\lambda(r)\le C\alpha(r)\qquad(r\in\mathscr E).}
\tag{2.3}
$$
它控制同一个原首源的真正完整和裸最小费，保留整个原 $A_m$。等价地，
$$
\boxed{
\lambda(r)^2-\alpha(r)^2
\le(C^2-1)\alpha(r)^2,\qquad r\in\mathscr E,
}
\tag{2.4}
$$
左边仍是原同源新 $H_2^\circ$ 能量。

还有一个对任意原源的准确算子界。令
$\mathcal P_{\rm alg}=\mathsf B_t\mathsf T_q$ 为源上的有界幂等回缩投影。反向分析任意原完整可行链、再使用同一距离论证，给
$$
\widehat\alpha(\mathsf T_qr)\le R\alpha(r).
$$
由模型高输入为零及截面上界，
$$
\boxed{\lambda(\mathcal P_{\rm alg}r)\le C\alpha(r)
\qquad(r\in\mathscr R_q).}
\tag{2.5}
$$
$\mathcal P_{\rm alg}$ 不被称为原两费用正交投影。下一节使用的投影不同。

## 3. 在原两已付费用中取真正投影

按[实际负源图稿 §§1、4](R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)的原定义，写
$$
L=J_{\rm left}^{-1},\qquad
B=J_{\rm bare}^{-1},\qquad
G=J_{\rm right},\qquad
\mathfrak M=B+LGL.
$$
三个最小费和原混合费为
$$
\mu(r)^2=\langle Lr,r\rangle,\quad
\alpha(r)^2=\langle Br,r\rangle,\quad
\lambda(r)^2=\langle G^{-1}r,r\rangle,
$$
$$
\lambda_{\rm flat}(r)^2=\langle GLr,Lr\rangle,\qquad
\boxed{\Xi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2
=\langle\mathfrak Mr,r\rangle.}
\tag{3.1}
$$
固定窗口中这些正度量都有界，$\mathfrak M$ 严格正，因此其范数与原源范数等价。

任取一个已知必须保留的原闭源空间 $\mathscr D\subseteq\mathscr R_q$。可取全部源空间，也可取真正负图
$$
\mathscr N_q=\ker[\iota_0^*(L+B)],
$$
或负源图稿中已经得到的闭余空间。置
$$
\boxed{\mathscr Z=\mathscr E\cap\mathscr D.}
\tag{3.2}
$$
这是闭交。对 $r\in\mathscr D$ 定义
$$
\boxed{
p=P_{\mathscr Z}^{\mathfrak M}r,\qquad
r_{\rm rem}=r-p.
}
\tag{3.3}
$$
于是两者仍在 $\mathscr D$，并且准确有
$$
\boxed{
\Xi(r)^2=\Xi(p)^2+\Xi(r_{\rm rem})^2.
}
\tag{3.4}
$$
这是两费用总平方和的收缩；不宣称残源的每一个分量分别不超过原来对应的分量。

若需要显式投影，令
$$
\widehat{\mathscr Z}
=\{\widehat r\in\widehat{\mathscr R}_t:
                  \mathsf B_t\widehat r\in\mathscr D\},
\qquad B_Z=\mathsf B_t|_{\widehat{\mathscr Z}}.
$$
此域闭，$B_Z$ 到 $\mathscr Z$ 为有界同构，且
$$
\boxed{
P_{\mathscr Z}^{\mathfrak M}
=B_Z(B_Z^*\mathfrak MB_Z)^{-1}B_Z^*\mathfrak M.
}
\tag{3.5}
$$
中间逆在这个真正域上有界。剩余条件准确为
$$
\boxed{
r_{\rm rem}\in\mathscr D,\qquad
B_Z^*\mathfrak Mr_{\rm rem}=0.
}
\tag{3.6}
$$
不能把它改成模型强位坐标、远尾创建坐标或物理源头坐标为零。

## 4. 删除量的全部实际费用已付

对任意源，原正逆 Cauchy 不等式给
$$
\mu(r)^2
=\operatorname{Re}\langle G^{-1/2}r,G^{1/2}Lr\rangle
\le\lambda(r)\lambda_{\rm flat}(r).
\tag{4.1}
$$
对 $p\in\mathscr Z\subseteq\mathscr E$ 使用 (2.3)，得到
$$
\mu(p)^2
\le C\alpha(p)\lambda_{\rm flat}(p)
\le\frac C2\Xi(p)^2.
$$
因此
$$
\boxed{
\begin{aligned}
&\mu(p)\le\sqrt{C/2}\,\Xi(p)
                 \le\sqrt{C/2}\,\Xi(r),\\
&\lambda(p)\le C\alpha(p)\le C\Xi(p)\le C\Xi(r),\\
&\Xi(r_{\rm rem})\le\Xi(r).
\end{aligned}
}
\tag{4.2}
$$
尤其
$$
\boxed{
\|E_q^\dagger r-E_q^\dagger r_{\rm rem}\|
=\mu(p)\le\sqrt{C/2}\,\Xi(r),
}
$$
$$
\boxed{
|\lambda(r)-\lambda(r_{\rm rem})|
\le\lambda(p)\le C\Xi(r).
}
\tag{4.3}
$$
这些界支付原同一窗口内的左像差、完整右费用差，以及新残源的**真正混合** $\lambda_{\rm flat}$。没有把
$\mathcal P_{\rm alg}$ 作用于旧 flat 源之后所得的量冒认成新残源 flat。

若在 (3.6) 的余空间上另外证明
$\mu(z)^2\le C_{\rm rem}\Xi(z)^2$，则由左最小映射的线性、三角不等式及 (3.4)，
$$
\boxed{
\mu(r)^2\le(C/2+C_{\rm rem})\,\Xi(r)^2
\qquad(r\in\mathscr D).
}
\tag{4.4}
$$
这是比较常数的准确运输；本稿没有给出剩余 $C_{\rm rem}$ 的上界。

## 5. 一个统一常数小于二的原参数族

给定任意 $k\ge1$，取
$$
t=k-1,\qquad
0\le b\le\left\lfloor\frac q{192(d+k)}\right\rfloor,
\qquad
n=q-b-k+1,
$$
并要求
$$
\boxed{q\ge128(d+k)^2.}
\tag{5.1}
$$
则 $n\ge0$、$J+1\ge q$。现在
$$
H=d+k,\qquad P=b+d+k-1,
$$
故
$$
\theta\le\frac{12(d+k)(b+d+k-1)}q
\le\frac1{16}+\frac3{32}
=\frac5{32}<\frac14.
$$
于是
$$
\kappa^2\le\frac32,\qquad
R\le e^{1/3},\qquad
\boxed{C=R\kappa<2.}
\tag{5.2}
$$
(4.2)--(4.3) 在这个整个原参数族中可统一写为
$$
\boxed{
\mu(p)\le\Xi(r),\qquad
\lambda(p)\le2\Xi(r),\qquad
\Xi(r_{\rm rem})\le\Xi(r).
}
\tag{5.3}
$$
此范围允许完整的远尾出生
$b=O(q/(d+k))$，没有退回只取远尾真空或单一 primitive 向量。
保留下来的前 $k$ 个强位也一直使用其真实不同权。

## 6. 对实际缺陷族及全部窗口的合法应用

[实际源比例稿](R271-appendix-actual-source-two-form-ratios-and-legal-window-summation-threshold.md)中原 $w\in W$ 的源满足
$$
\alpha(r_q)\le b_{m,q}(w),\qquad
\lambda_{\rm flat}(r_q)\le b_{m,q}(w),
$$
其中
$$
b_{m,q}(w)=\|P_{[q+1,q+d]}^{(m)}w\|
          +2e^{-55d^4}\|w\|.
$$
故 $\Xi(r_q)\le\sqrt2\,b_{m,q}(w)$。如果还须保留负图或既有闭余图，先使用[负源图稿 §§5–6](R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)已经支付的同一顶层前驱截断，取得其中的真正实际源族，再在那个 $\mathscr D$ 内使用 (3.2)。

一般地，对任何已合法取得的族
$$
r_m\in\mathscr D_m,\qquad
E_{q_m}^\dagger r_m\longrightarrow w,\qquad
\Xi_m(r_m)\longrightarrow0,
$$
只要 $C_m$ 有统一上界，(4.2)--(4.3) 准确给
$$
\boxed{
E_{q_m}^\dagger r_{{\rm rem},m}\longrightarrow w,\qquad
\Xi_m(r_{{\rm rem},m})\longrightarrow0,\qquad
|\lambda_m(r_m)-\lambda_m(r_{{\rm rem},m})|\longrightarrow0.
}
\tag{6.1}
$$
残源同时满足 (3.6)。并未声称不同窗口的残源继续组成一条共同的逐孔源流。

同头全部窗口也不另付窗数：若各 $C_{m,q}\le C_0$，则逐窗平方后求和即得
$$
\boxed{
\sum_q\mu_q(p_q)^2\le\frac{C_0}{2}\sum_q\Xi_q(r_q)^2,\quad
\sum_q\lambda_q(p_q)^2\le C_0^2\sum_q\Xi_q(r_q)^2,
}
$$
$$
\boxed{
\sum_q\Xi_q(r_{{\rm rem},q})^2
\le\sum_q\Xi_q(r_q)^2.
}
\tag{6.2}
$$
右侧沿用真实未来带的既有重叠预算，没有多乘原合法窗口的数量。

这与[回缩左像来源分离](R271-appendix-retraction-left-localization-and-fixed-source-separation.md)完全相容。那里排除把一个移动模型源族直接当作固定非零 $W$ 的近似；这里删去的 $p_m$ 的左像趋零，真正实际来源由余源继续保留。剩余高费用、实际窄源比较及无权 $N=M$ 仍开。
