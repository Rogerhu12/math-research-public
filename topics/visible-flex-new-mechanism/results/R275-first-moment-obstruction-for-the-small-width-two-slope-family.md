# R275：双斜率小母宽分支在另一 Gaussian 第一外矩上的严格余差

日期：2026-11-15。**完整纸面证明；未执行求积、符号计算程序、人工检查或研究计算。**

本稿消费 [R270](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)、[R271](R271-six-complete-blocks-pay-the-first-two-positive-negative-Gaussian-moments.md) 和 [R273](R273-reflection-densities-pay-the-minus-one-minus-two-zero-moment.md) 的同一个实际有限宽构造。R273 已证明 $A_{-1,-2}$ 的第零外矩准确为零；本稿证明：在原双斜率、$\rho=0,20$ 两种真实排序、普通/同源伴随、小母宽及正幅完整 block 混合的范围内，它的**第一外矩不能同时为零**。

这不推翻已付的六能量或其他面积等式。它指出这些有限条件仍不充分，并给出不能靠原排序、共同中心或增加同类正幅 block 修复的明确原因。一般多斜率、不同实平方质量分配、其他母形分支均不在排除范围内。

## 1. 原算子与不发生退化的系数

保持 R273 的记号

$$
L=\Phi_{p_0},\quad T=\Phi_{s_1},\quad R=\Phi_{r_1},\quad U=\Phi_{s_0},
\qquad B_{-1}=dL+eT,\quad B_{-2}=aR+bU.
$$

令

$$
k=\frac{db}{2}-ea,\qquad
p=\frac{d(a+b)+2e(4a+b)}3,\qquad
\mathfrak d=2d(a+b)+e(11a+5b).
\tag{1}
$$

这些是原 Gaussian 系数，不是新增可选权重。共振 $\varepsilon=\kappa^2/4$ 时，直接代入原 $a,b,d,e$ 给

$$
\boxed{
k=-\frac{\kappa\{1173\kappa^6+177\kappa^4+122\kappa^2+8\}}
{256h_e^3}\ne0
\qquad(\kappa\ne0).
}
\tag{2}
$$

特别，以下严格余差不能通过在共振小参数附近令 $k=0$ 来规避。各系数除以 $k$ 后对 $\kappa^2=0$ 有正常的光滑延拓；不把 $\kappa=0$ 本身当作实际安装。

外矩规范仍是

$$
I_1(u,w)=\int x u''w'',\qquad
S_{X,Y,1}(u)=2I_1\{u,[X,Y](u;u\odot u)\}.
$$

## 2. 四条单包第一外矩，保留真实左尾

对任意实紧 $u$，记 $v=u'$、$r=u''$、$A=J(r^2)$，并置

$$
\begin{gathered}
\mu=\int r^2,\quad \mu_1=\int xr^2,\quad
C_2=\int x^2r^4,\quad N_x=\int xvr^3,\\
U_3=\int ur^3,\qquad V_2=\int v^2r^2,\qquad
H_{\rm self}=\ell\mu^2+\int_\ell^{r_*}A^2.
\end{gathered}
\tag{3}
$$

$H_{\rm self}$ 对足够靠左的零 collar 锚 $\ell$ 不变；其 $\ell\mu^2$ 不是可删除的误差项。

R259 的原 cubic 密度递推给

$$
F_{L,1}=F_{T,1}=0,\qquad
F_{R,1}=\int\left(\frac{x r^3}{3}-vr^2\right),\qquad
F_{U,1}=\frac13\int xr^3.
\tag{4}
$$

前两个零对任意紧 $u$ 成立：相应 local 密度为 $v^2r$ 和 $-2v^2r$，均为总导数。用原 $L',L'',T',T''$ 及

$$
\begin{aligned}
DF_{U,1}[w]&=\int xr^2w'',\\
DF_{R,1}[w]&=\int\{(xr^2-2vr)w''-r^2w'\},
\end{aligned}
$$

再补

$$
\left[
x(X'''Y-X''Y'+X'Y''-XY''')+X''Y-XY''
\right]_{\rm left},
\tag{5}
$$

得到准确表

$$
\boxed{
\begin{aligned}
S_{L,R,1}&=\frac{C_2}{6}-\frac{N_x}{3}+\frac{U_3}{3}-\frac{V_2}{2},\\
S_{L,U,1}&=\frac{C_2}{6}-\frac{N_x}{3}+\frac{U_3}{3}
+\frac{H_{\rm self}}4-\frac{\mu\mu_1}{2},\\
S_{T,R,1}&=\frac{11C_2}{12}-\frac{8N_x}{3}+2V_2
+\mu\mu_1-\frac{H_{\rm self}}2,\\
S_{T,U,1}&=\frac{5C_2}{12}-\frac{2N_x}{3}.
\end{aligned}}
\tag{6}
$$

四对中，(5)仅对 $(L,U)$ 非零，等于 $-\mu\mu_1/2$。同时

$$
\int r^2J(xr^2)=\mu\mu_1-\frac{H_{\rm self}}2.
\tag{7}
$$

因此(6)没有将单包原二次输出假定为紧支撑，也没有通过“最终三矩为零”删去内部 $\mu$ 项。

## 3. 原 full circle：有序项是 $J(xD_\rho)$

用 R273 的真实不交微包表达

$$
f=\sum_i a_i u_i,\quad g=\sum_i b_i u_i,\quad
c_i=a_i\cos\theta+b_i\sin\theta,\quad d_i=a_i^2-c_i^2,
$$

并记

$$
D_\rho=f''{}^2-\phi_\theta''{}^2,\qquad
\phi_\theta=f\cos\theta+g\sin\theta.
$$

由(6)，单包的 $H_{\rm self}$ 系数为 $k/2$，$\mu\mu_1$ 系数为 $-k$。R259 原跨包核的第一外矩分量（$I_1$）为 $-k\mu_i\mu_{1,j}$。利用(7)共同合并，得到

$$
\boxed{
\begin{aligned}
2I_1\{\phi_\theta,[B_{-1},B_{-2}](\phi_\theta;D_\theta)\}
={}&\sum_i c_i^2d_i
\left\{
\frac{\mathfrak d}{12}C_2(u_i)-pN_x(u_i)
+\frac{d(a+b)}3U_3(u_i)
+\frac{a(4e-d)}2V_2(u_i)
\right\}\\
&-k\int\phi_\theta''{}^2J(xD_\rho).
\end{aligned}}
\tag{8}
$$

这是真实 full outer/inner 公式。最后一项不是独立可调常数，也不能用第零外矩中已经消失的 $J(D_\rho)$ 代替。

以下只需检验 $\theta=\pi/2$。记

$$
S=2I_0\{g,[P,Y](g;f\odot f-g\odot g)\},\quad
Z=2I_1\{g,[B_{-1},B_{-2}](g;f\odot f-g\odot g)\},
\tag{9}
$$

其中 $P=\Phi_{r_0}$、$Y=\Phi_{p_2}$。原 $A_{1,-3}$ 的完整第零外矩为零，必然给 $S=0$；相应 Gaussian 系数在实际小非零共振参数不为零。

## 4. 同一实际母包的有限宽准确式

对 R270 的 even 母包 $u$ 记

$$
\begin{gathered}
m=\int (u'')^2,\quad C=\int(u'')^4,\quad
\nu=\frac{\int(y^2(u'')^2+2(u')^2)}m,\\
X_2=\int y^2(u'')^4,\quad
N=\int yu'(u'')^3,\quad U_3=\int u(u'')^3,\quad
V_2=\int(u')^2(u'')^2,\\
\mathcal L=X_2-\frac83N+\frac43U_3+V_2,\qquad
\Delta=\iint|y-z|u''(y)^2u''(z)^2\,dy\,dz .
\end{gathered}
$$

定义

$$
\begin{aligned}
B_{\rm loc}&=C\nu-\mathcal L+\frac\Delta4,\\
H_1&=\frac{\mathfrak d}{12}(X_2-C\nu)-pN
+\frac{d(a+b)}3U_3+\frac{a(4e-d)}2V_2,\\
\mathcal R&=H_1+k(C\nu-\mathcal L).
\end{aligned}
\tag{10}
$$

这里所有量来自同一个实际母包，不能独立指定。

仍用原 $\alpha,\beta,q$，并以 $a_{\rm cell}=q(1-\alpha)>0$ 区分 cell 质量与 Gaussian 系数 $a$。原两个排序是 $\rho=0,20$，$n=2048$，low 间隔 $A$，high 间隔 $B$，满足

$$
(B-64A)(B+64A)(n^2-1)
=(4095-12\rho^2)A^2-12\nu(1-q^2).
\tag{11}
$$

记 $D_B=B-64A$。由完整有序计数，定义

$$
U_\rho=n a_{\rm cell}(64q+1)
\left\{\frac{16}{3}D_B(n^2-1)+A\left(\frac{3\rho^2}{2}-512\right)\right\}.
\tag{12}
$$

它是 R271 的准确 $U_{01}$，不是纯局部矩。对实际物理宽度 $\delta>0$，单个 base 的两个完整量准确为

$$
\boxed{
S=\delta n a_{\rm cell}
\left\{
m^2A[10928q-(32q+1)\rho^2]
+64(1-q^2)B_{\rm loc}
\right\},
}
\tag{13}
$$

$$
\boxed{
Z=-kS-km^2\delta U_\rho
+64n a_{\rm cell}\delta(1-q^2)\mathcal R .
}
\tag{14}
$$

证明(14)时，微包 self 的
$\int r_i^2J(xr_i^2)=m^2\xi_i/2+\Delta w_i/4$
必须保留。它与(13)中原 self 的 $-\Delta w_i/4$ 合并后，才准确得到 $\mathcal R$；不是把微包当成点质量再补一个估计。

原方向版和同源伴随版在 $\theta=\pi/2$ 的所有 quadratic 密度、local 四次密度和(14)相同。这只用于本矩的这个角度，绝不宣称两版的 pure $Q$ 相同。

## 5. 严格半平面来自有限 cell 恒等式

令

$$
c_q=\frac{32q+1}{64q+1}\in(0,1).
$$

式(11)给出以下**准确恒等式**：

$$
D_B(n^2-1)
=\frac{(4095-12\rho^2)A^2-12\nu(1-q^2)}{128A}
-\frac{D_B^2(n^2-1)}{128A}.
\tag{15}
$$

平方项非负。把(12)、(13)与(15)直接合并，得到

$$
\frac{S}{m^2\delta}+c_qU_\rho
\le n a_{\rm cell}
\left\{
A\left(4q-\frac{2731}{8}\right)
+64(1-q^2)\frac{B_{\rm loc}}{m^2}
\right\}.
\tag{16}
$$

右边还丢下了两个非正项：含 $\nu/A$ 的项和含 $D_B^2/A$ 的项。没有使用“$\rho=0$ 时 $B<64A$”这一错误方向；实际上原大 $A$ 的 $\rho=0$ 情形有 $B>64A$，但(15)统一覆盖两个排序。

结合(14)，

$$
\boxed{
\begin{aligned}
(1-c_q)S-c_q\frac Zk
\le \delta n a_{\rm cell}m^2
\left\{
A\left(4q-\frac{2731}{8}\right)
+64(1-q^2)\left[
\frac{B_{\rm loc}}{m^2}
-c_q\frac{\mathcal R}{km^2}
\right]
\right\}.
\end{aligned}}
\tag{17}
$$

这是原 $S,Z$ 的有限宽不等式，不是一个额外 LP 或渐近数值拟合。

## 6. 真实母根上的尺度，以及共同半平面

R270 的三母包与实际奇扰动幅 $hz$ 满足，在主 $\delta=0$ 母根上

$$
\gamma=1+O(h^2),\quad s=1+O(h^2),\quad z=O(1),\quad
N,U_3,V_2=O(h).
$$

左右镜像使总母包 even，但右子包本身不必 even。上式中的 $N$ 中心项也是 $O(h)$，因为 $N_0(v+hz e_v)=O(h)$；不能将该项错误地当成零或 $O(1)$。

已付的真实 $F_\kappa=0$ 给 $X_2-C\nu=O(h)$。式(2)及(10)遂给

$$
\frac{\mathcal R}{k}=O(h),\qquad
m\longrightarrow 3m_v,\qquad
\frac{\Delta}{4}\longrightarrow 2L_*m_v^2,\qquad
\frac{B_{\rm loc}}{m^2}\longrightarrow\frac{2L_*}{9}=\frac19 .
\tag{18}
$$

原 $L_*=1/2$。这些归一比值在小 $\kappa^2$ 邻域光滑；没有用实际 $\kappa=0$。

先取足够小但固定的正 $h$，可在各 $\delta=0$ 母根上取

$$
\left|\frac{B_{\rm loc}}{m^2}\right|\le1,\qquad
\left|\frac{\mathcal R}{km^2}\right|\le1.
\tag{19}
$$

原 $\alpha_0\in(1/3,1/2)$，所以 $q_0\in(9/64,1/4)$。原有限间距 $A\ge10$，于是(17)右方归一括号至多

$$
-\frac{2723}{8}A+128<0.
\tag{20}
$$

严格余量很明确；不需要拿小量数值误差与零比较。

所有这些排序、方向和最后位置的主 $\alpha$ 极限相同。原 leading 能量方程的唯一简单根来自

$$
256\alpha(1-\alpha)^5-(5-\alpha)=0;
$$

母形、最后中心、完整复制四次权只乘非零正因子，不改变这个根。令

$$
c_*=\frac{32q_0+1}{64q_0+1}.
$$

现在固定有限个所选 $A$、排序和最终中心，再取每个主宽度 $\delta>0$ 足够小。完整四变量 IFT 给出的实际参数、$S/\delta$ 和 $Z/(k\delta)$ 都连续；因此即使各 block 的实际 $q(\delta)$ 不完全相同，仍有同一个严格半平面

$$
\boxed{
(1-c_*)S_j-c_*\frac{Z_j}{k}<0
}
\tag{21}
$$

对每个实际有限宽 block 成立。这里是先固定 $h$、有限间距/中心，再缩小主 $\delta$。没有把只在 $\delta=0$ 的参数值当作已构造曲面的准确系数。

## 7. 完整副本和正幅混合不能解除余差

先看原八副本及十二副本。每个完整 base 的 inner $D_\theta$ 三矩已经为零，所以跨完整副本的二次 history 消失；但 base 内部的所有微包 history 一直保留。

对本稿的 $\theta=\pi/2$，$S$ 与 $Z$ 在共同平移下都保持：local 平移增量由已经支付的无中心四次和、第一中心和与母 $N_0=0$ 消失；primitive 增量是平移量乘 $\int g''{}^2J(f''{}^2-g''{}^2)=0$。后一个零正是 R273 的真实平方密度对称结论。$g$ 翻号不改变该角度的这两个量。故两层副本仅将 $(S,Z)$ 同乘一个正四次权和，保持(21)。

对最后互不交的有限个完整 block，原 full-circle cross 仍由 inner 三矩零准确消失。设最终正四次幅权为 $\lambda_j>0$，并且已经支付原 $A_{1,-3}$ 的第零外矩，因而

$$
\sum_j\lambda_jS_j=0.
$$

把(21)以这些正权相加，即得

$$
\boxed{
\sum_j\lambda_j\frac{Z_j}{k}>0.
}
\tag{22}
$$

所以最终 $A_{-1,-2}$ 第一外矩在 $\theta=\pi/2$ 严格非零，符号与 $k$ 相同；由(2)，也就是与 $-\kappa$ 相同。

R271 支付的是包含实际最后中心的 $\sum_j\lambda_j\delta_j\xi_jU_{\rho,j}$，不能把它改写成无 $\xi_j$ 的和。(22)没有否定 R271 的准确支付；它说明那一支付不解决本稿的原矩。

## 8. 后继需要改变什么

此严格障碍覆盖目前两排序、普通/伴随方向、小母宽同源分支和任意有限正幅混合。它同样覆盖 R271 的六个最终 block；增加同类 block、改最后正中心或再取更小正宽度都保留(21)，不能修复(22)。

它不排除一般合法圆，也没有排除三种以上真实方向斜率、不同的实平方质量分配、其他母形分支或改变原排序机制的构造。下一建设性问题必须改变能够打破共同半平面的真实数据，而不能把原已有门逐项成立当成 full ruling 候选已完成。

本稿新增的是一个准确的族内失败结论。R270、R271、R273 已付的等式保持为真；原“形式剩余条数”仍只是未付条件的记账，不是解空间维数。原 Gaussian 词独立性和三外矩分离意味着(22)是该族完整面积的真实阻断，而不只是某个选定有限截断的残差。
