# R150 补充：正 e 一般单位 k 图的原物理 f 整性与完整 singleton 零阶模型

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

## 1. 新结论与已经付清的范围

在当前剩余特征 $1009$ 的 W/b0 原图，设
$$
v(e)>0,\quad v(k)=0,\quad \zeta=\bar k\notin\{-2,-4,4\}.
\tag{1}
$$
[准确 q2 剩余式及正负四中心排除](R150-appendix-unit211-W-b0-positive-e-unit-k-exact-residual-quadratic-and-k-plus-minus-four-exclusion.md)
已付 $\lambda$ 是单位。置
$$
L=\frac{\zeta+2}{\zeta},\quad m_0=1-L,\quad
M_0=2L-1,\quad h_0=3-2L.
$$
于是
$$
L,\quad L-1,\quad M_0,\quad h_0
$$
都非零；这些是此前已完整排除的中心，不是本稿任取的一般开集。

**新结论：物理参数 $f$ 必整。** 随后同一物理 $t,V,W_1,x,y,A_1$、值参数 $\sigma$ 以及全部原 Gram 坐标也整。证明只用完整原 singleton $P$ 方程，未使用旧六射线投影的 gcd，也未倒 $P_{02}$ 的剩余、$D$、G36 首项或新的 $f$ 头。

## 2. 全部原恢复系数在此图整

原恒等式保持
$$
u=1+e,\ Q=ek,\ \delta=1-Q,\quad
J=2u(1-u)+\ell Q,\quad
T_0=2u-\ell Q-2u^2,
$$
$$
\Phi=T_0+4u-4+Q,\quad P_f=T_0(J-Q),\quad
G=\lambda P_{02}+eT_0,
$$
$$
P_c=QP_{02}(\ell+T)-GT_0,\qquad bc=M/(4\delta).
$$
同一点完整原恢复为
$$
t=-\frac{P_f f+P_c}{bcQ\Phi},\qquad
V=\frac{Jf-G+bcQt}{Q}=2uf+V_s,\qquad
W_1=T_0/2+2uf,
\tag{2}
$$
$$
V_s=-G/Q-P_c/(Q\Phi),\quad
x=\frac{(u-\ell Q)V-mW_1}{M},\quad
y=\frac{\ell W_1-uV}{M},\quad
A_1=2f-2V+2bc\,t.
\tag{3}
$$
这里 (2) 的第二个等号使用准确原身份
$J\Phi-P_f=2uQ\Phi$。其原完整来源也见
[同一 f 的完整 I11 源](../notes/2026-11-28-unit211-W-same-f-entire-pure-lambda-T-I11-original-return-8542.py)，
blob **c0b1f13b94335d0ad6287ea95ffdaffe38ff039f**；本稿只读取原定义，不执行旧呈示门。

在 (1) 中，以下提取 $e$ 幂后的式子准确正则：
$$
T_0=e\,t_0,\quad t_0=-(2u+k\ell),\qquad
\Phi=e^2\phi_2,\quad \phi_2=-\frac{2(k+4)}{uk+2},
$$
$$
P_{02}=e^2p_2,\quad
p_2=\frac{2u\{k^2+(5-2e)k+8\}}{uk+2},
$$
$$
J-Q=e^2j_2,\quad
j_2=-\frac{2k(2u-1)}{uk+2},
$$
$$
G=e^2g_2,\quad g_2=\lambda p_2+t_0,\qquad
P_c=e^3p_c,\quad
p_c=kp_2(\ell+T)-g_2t_0.
\tag{4}
$$
$bc,k,\phi_2,M$ 在本图均为单位，所以 (2)、(3) 是关于 f 的整仿射式。特别不要求 $\bar p_2\ne0$。原 b0 给
$T=u\ell(2\lambda-3)/(4u+2u/k-\ell)$，其分母剩余为 3，故 T 整。
由 $M\sigma^2=D=\ell A_2-T^2$ 且 M 单位，$\sigma$ 也整。因此完整物理
$$
h=1+T/\ell+m\sigma/\ell-\rho\sigma,\qquad
k_{\rm val}=1+T/\ell+m\sigma/\ell+\rho\sigma,\qquad
\rho^2=\delta
$$
均整。二次扩张中可以选择 $\bar\rho=1$；另一选择仅交换两 singleton，两个原方程本来都保留。

## 3. 原 Gram 的零阶 f 多项式模型

以下先在整恢复系数上取剩余，仍把 f 当独立变量，尚不假设 f 整。令
$$
\mu=2\bar\lambda-3,\quad T_{\rm res}=L\mu/3,\quad
v_0=\overline{V_s},\qquad F=f+v_0,\qquad A=m_0+v_0.
$$
由 (2)—(4)，
$$
\bar t=\frac{4F}{M_0},\quad
\bar V=2f+v_0,\quad \bar W_1=2f,
$$
$$
\bar x=\frac{2Lf+v_0}{M_0},\quad
\bar y=\frac{-2m_0f-v_0}{M_0},\quad \bar A_1=0.
\tag{5}
$$
这些式子表示原多项式各 f 系数的剩余，故用来研究 f 极点并不循环论证。

若需要显式参数，令 $J_p=4L^2-3L+1$，则
$$
v_0=\frac{\bar\lambda J_p(8L-3)/3-LM_0^2}{M_0(L-1)}.
\tag{6}
$$
不倒 (6) 的分子。

取 $\bar\rho=1$，原权和完整四行 Gram 为
$$
a=m_0,\quad b=1/2,\quad c=M_0/2,
$$
$$
v_0^{\rm row}=(0,0,2,0),\quad
v_1^{\rm row}=(0,0,-2A,0),
$$
$$
v_B=(2,-2A,0,t_0^{\rm val}),\qquad
v_C=(0,0,t_0^{\rm val},0),\quad
t_0^{\rm val}=4F/M_0.
\tag{7}
$$
始终用真实 dual 乘法
$(xy)_1=x_0y_1+x_1y_0$，而
$$
\tau(z)=m_0z_0+z_1+\tfrac12z_2+\tfrac{M_0}{2}z_3.
$$
由 (7)，
$$
\tau(v_B)=2f,\quad
\tau(v_B^2)=-4m_0-8v_0+\frac{8F^2}{M_0},
$$
$$
\tau(v_B^3)=-16m_0-24v_0+\frac{32F^3}{M_0^2}.
$$
因此完整中心三次式准确为
$$
\begin{aligned}
P_B^{(0)}
={}&-16m_0-24v_0+\frac{32F^3}{M_0^2}\\
&+24fm_0+48fv_0-\frac{48fF^2}{M_0}+16f^3.
\end{aligned}
\tag{8}
$$

## 4. 物理 f 的全部极点被原 P 方程排除

(8) 的 f 三次系数为
$$
\frac{32}{M_0^2}-\frac{48}{M_0}+16
=\frac{16(M_0-1)(M_0-2)}{M_0^2}\ne0,
\tag{9}
$$
因为 $M_0-1=2(L-1)$、$M_0-2=2L-3=-h_0$ 都已证明非零。
原 $P_2(v_B)$ 对 f 的次数至多三，所有其余系数由 §2 为整。

若 $v(f)<0$，(9) 保证原 $P_2(v_B)$ 的三次项是唯一最低阶，且其阶是 $3v(f)<0$。另一方面，完整物理右侧
$$
P_{02}h^3
$$
有正阶，或者为零，因为 $P_{02}=e^2p_2$、$p_2,h$ 整。这与原
$P_2(v_B)-P_{02}h^3=0$ 矛盾。因此 $v(f)\ge0$。再由 (2)、(3) 得全部原 Gram 坐标整。

这个证明涵盖 $P_{02}$ 首项消失、$D$ 剩余为零和 G36 首项消失的情况，不先把已付的全域分母当成赋值单位。

## 5. 为新完整 N/P 首阶输入保留的准确零阶关系

由 (7)，
$$
d=DK(\mathbf1)=(1,-A,2f,t_0^{\rm val}/2),\qquad F_2=\tau(d)=2f.
$$
对 $v_B$ 有 $DK(v_B)=(0,0,\tau(v_B^2),0)$，所以
$\tau(v_BDK(v_B))=0$。代完整原 N4 公式直接得
$$
N_4(v_B)^{(0)}=P_B^{(0)}.
\tag{10}
$$
同时
$$
P_2(v_C)^{(0)}=0,\qquad N_4(v_C)^{(0)}=0.
\tag{11}
$$
(10)、(11) 是关于独立 f 的完整零阶恒等式，不使用原 q2、R6、N5 的必要 gcd。既然 §4 已付全部坐标整，可以对新的完整原误差进一步取正阶原关系，例如
$e^{-1}(N_B-P_B)$、$e^{-1}P_C$、$e^{-1}N_C$ 的正则剩余；它们的实际首阶系数尚未在本稿执行或预报。

本稿已完成的是原 f 整性及 (5)—(11) 的同点原模型。一般 k 剩余点、正 e 的 k 负二分支、内部权图及有限 DVR 边界仍开放；普通 ISP 尚未完成。
