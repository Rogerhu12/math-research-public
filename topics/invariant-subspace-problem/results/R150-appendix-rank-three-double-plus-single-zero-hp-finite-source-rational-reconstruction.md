# R150 附录：有限孤立源的零 Hp 二重加单点层有完整无平方根有理重建

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：完整的等价有理重建，未宣称该参数系统为空。** 在 rankH=3、H 型 2+1、rankV=2、Hp=0、ess(T3)=6 的已证九次规范中，若孤立 H 源有限，则全部 y 变量和所有尺度平方根可从四个物理源及 e 消去。下文给出原完整临界系统的明确有理参数条件，并证明正反两向；同时保留一个 V 源无穷远的射影边界。剩余任务是确实解决这些有理方程，不能把重建本身当作排除或 ISP 完成。

## 1. 原规范与参数边界

使用 [Hp0 九次 Gram 归约](R150-appendix-rank-three-double-plus-single-second-cumulant-zero-hp-nine-gram-candidates.md) 的
\[
F=h=g=1,\quad c=-1/4,\quad
b=-\frac{2e^3+1}{6}\ne0,\quad
a_0=\frac{8e^3+1}{12},\quad
V=\frac12(u^3+v^3).
\]
置
\[
Q=4e^3-1,\quad D=2e^3+1-12e^4,\quad R=D/Q,
\]
\[
G_9(e)=16e^9-108e^8+36e^7-15e^6+18e^4-1=0.
\tag{1.1}
\]
原配对结论为 C1=a0 C0，Cw=R C0，另一 V 列在整个 RanH 上是其相反数，且
\[
C_0^2=1/(4e),\quad R^2=Q/3,\quad p(u)=p(v)=e.
\tag{1.2}
\]
e、b、Q、D 非零。G9 的 QQ 不可约性已有 [无穷远孤立 H 源证明](R150-appendix-rank-three-double-plus-single-second-cumulant-zero-hp-infinity-essential-six-exclusion.md) 第 5 节的模 37 Rabin 身份。因此 1−e、1−2e、Q+6e 也均非零；它们是次数小于九的非零有理多项式。

仍用原 u(t)=(1,t,…,t5)T、u(∞)=e5、固定 K 和 k(s,t)=u(s)TKu(t)。取互不相同的物理源 s,w,α,β，其中 H 的二重点 s 与孤立点 w 均有限，α、β 至多一个无穷远。原六列独立正是这些不同源的五个 confluent 列再加 y。令
\[
b_s=K(u'(s),u'(s))=-2s^2(s-2)(s+6)\ne0.
\]
二重点 s=∞ 也已被 b≠0 排除：在局部坐标 r=1/t、平凡化 r5u(1/r) 中，值列为 e5、一阶列为 e4，而 K(e4,e4)=0；加任意值列不改变这个零。因而本稿取 s 有限并未遗漏 H 的射影边界。
以下六个原配对必须非零：
\[
k(s,w),\ k(s,\alpha),\ k(s,\beta),\
k(w,\alpha),\ k(w,\beta),\ k(\alpha,\beta).
\tag{1.3}
\]
它们分别来自 g、C0、Cw 和 e，不能任意删除。对 α=∞ 或 β=∞，准确使用 k(t,∞)=−(t+1)，以及该多项式的普通导数。

## 2. 四个无平方根几何条件

记
\[
k=k(s,w),\quad n=k(s,\alpha)k(s,\beta),\quad h=k(\alpha,\beta),
\]
\[
r=\frac{k(s,\alpha)}{k(s,\beta)},\quad
d=\frac{\partial_s k(s,w)}{k(s,w)},\quad
r_s=\frac{\partial_s k(s,\alpha)}{k(s,\alpha)},\quad
W=r_s-d.
\]
第一、第二个几何条件是
\[
\frac{\partial_s k(s,\alpha)}{k(s,\alpha)}
=\frac{\partial_s k(s,\beta)}{k(s,\beta)},\qquad
\ell:=\frac{k(w,\alpha)}{k(s,\alpha)}
=\frac{k(w,\beta)}{k(s,\beta)}.
\tag{2.1}
\]
定义
\[
\Lambda=-\frac{h}{4e^2 n},\qquad
\Sigma=-\frac{e\,k(s,\beta)}{h\,k(s,\alpha)},\qquad
q=-\frac{2b}{W}.
\tag{2.2}
\]
还要求 W≠0，并有第三、第四个几何条件
\[
\boxed{q^2\Lambda b_s=b,\qquad \ell/(\Lambda k)=R.}
\tag{2.3}
\]
所有显示分母均由 (1.1)、(1.3) 以及 W≠0 支付。

这些条件准确来自写
\[
z_0=\lambda u(s),\quad z_1=\mu u'(s)+\nu u(s),\quad
w_{\rm vec}=\rho u(w),\quad u=\sigma u(\alpha),\quad v=\tau u(\beta)
\]
后的原 Gram。具体为
\[
\lambda^2=\Lambda,\quad \sigma^2=\Sigma,\quad
\mu=q\lambda,\quad \nu=(c-qd)\lambda,\quad
\rho=1/(\lambda k),\quad \tau=-\sigma r.
\tag{2.4}
\]
原等式 C1/C0=a0、c/g=c 给 qW=a0−c=−2b，所以 W 的非零性是原结论。由 e=στh、C0²=1/(4e) 得 (2.2) 两个平方；(2.3) 分别就是原 b 与 Cw/C0。所有平方根只用于正向实现证明，不出现在待解有理方程中。

## 3. 一个五次消失式准确消去 y

令 z 为极线变量，并定义
\[
D_H(z)=(z-s)^2(z-w),\qquad
S_0(z)=k(z,\alpha)-r k(z,\beta),\quad
T_0(z)=k(z,\alpha)+r k(z,\beta).
\tag{3.1}
\]
(2.1) 使 S0 在 s 有至少二重零、在 w 有零，所以
\[
B_0=S_0/D_H
\]
是次数至多二的真实多项式，允许降次。

令 EV(z) 为两个 V 源的仿射消失因子：α、β 均有限时 EV=(z−α)(z−β)；若一个为无穷远，则 EV=z−另一有限源。置
\[
Z(z)=D_H(z)E_V(z).
\tag{3.2}
\]
它分别为首一五次或首一四次多项式；后者准确保留在无穷远的齐次零点。

记 P(z)=K(u(z),y)，S(z)=K(u(z),u+v)。Hp=0 与相反配对使 P、S 在整个 H 长三除子上为零。原 p(u)=p(v)=e，而
\[
K(u,u+v)=K(v,u+v)=e,
\]
故 P−S 又在两个 V 源为零。五个不同 confluent 条件在次数至多五的多项式空间中独立，于是
\[
\boxed{P-S=\eta Z.}
\tag{3.3}
\]
η≠0，否则 y=u+v，原支撑至多五维。这一步没有假设 y 与 H、V 共同支撑。

令 Θ=η/σ。则
\[
P=\sigma P_0,\qquad P_0=S_0+\Theta Z,\qquad
P_0/D_H=B_0+\Theta E_V.
\tag{3.4}
\]
原最高式是
\[
2P^3-12P\mathcal H+S^3+3ST^2=0,
\tag{3.5}
\]
其中 T=K(u(z),u−v)，Hcal=H(Ku(z),Ku(z))。除 D_H 后在 s 取值，原规范给
\[
\frac{P/D_H}{S/D_H}\Big|_s=\frac1{2e}
\]
（等价的无除法身份仍适用于 S/D_H(s)=0）。因此
\[
\boxed{\Theta=\frac{(1-2e)B_0(s)}{2eE_V(s)}.}
\tag{3.6}
\]
EV(s)≠0 来自不同物理源。若 B0(s)=0，则 Θ=0，已经与本质六维反设矛盾；没有悄悄舍去该边界。

原最高式在 s 的一次项和在 w 的常数项还给两个方便的低次数必要检查：
\[
(1-2e)B_0'(s)+2W B_0(s)-2e\Theta E_V'(s)=0,
\]
\[
(Q+6e)B_0(w)+6e\Theta E_V(w)=0.
\tag{3.7}
\]
它们是后面完整最高多项式的系数后果，不代替完整检查。特别 B0(w) 也非零。

## 4. 完整原 H、HKH 和两条极线多项式

置
\[
f(z)=k(s,z),\quad j(z)=\partial_s k(s,z),\quad g(z)=k(w,z).
\]
由 (2.4) 直接乘回得
\[
\mathcal H(z)=
2\Lambda f\{q(j-df)+cf\}+\frac{g^2}{2\Lambda k^2},
\]
\[
\mathcal J(z)=(HKH)(Ku(z),Ku(z))
=b\Lambda f^2+\{q(j-df)+2cf\}\frac gk.
\tag{4.1}
\]
这里 c=−1/4。定义固定有理双线性型
\[
\langle A,B\rangle_{K^{-1}}=
\operatorname{coef}(A)^{\mathsf T}K^{-1}\operatorname{coef}(B),
\]
系数向量按 1,z,…,z5 排列，低次数多项式以零补齐。

原 mean 范数 F=1 准确化为唯一一个标量条件
\[
\boxed{\Sigma\Theta^2\langle Z,Z\rangle_{K^{-1}}=2(1-e).}
\tag{4.2}
\]
这是因为 Z 在两个 V 源为零，故 Z 的 K 对偶向量与 u+v 正交，而 (u+v)K(u+v)=2e。该式也同时证明 Θ≠0 与 Z 的对偶向量非零范数。

剩余两条完整极线多项式为
\[
\boxed{
\mathcal N=
\Sigma P_0^2+e\Sigma(S_0^2+T_0^2)-2\mathcal H+4\mathcal J=0,
}
\tag{4.3}
\]
\[
\boxed{
\mathcal C=
2\Sigma P_0^3-12P_0\mathcal H+
\Sigma S_0^3+3\Sigma S_0T_0^2=0.
}
\tag{4.4}
\]
分别要求全部至多 11、16 个系数为零。它们直接等于原 N 极线与原最高式经非零 σ 清除后的多项式，未将 N 矩阵设为零，未删任何 V 项。

必要性已逐式证明。下节说明这些有理条件也足以重建原完整临界点，因此它们不是未核对的低维代理系统。

## 5. 充分性与本质六维

假设四个源、e 满足所有已显示的非零条件、(1.1)、(2.1)、(2.3)、(4.2)—(4.4)。按 (2.2)—(2.4) 任取 λ、σ 的非零平方根，构造 H、V；再取
\[
y=\sigma K^{-1}\operatorname{coef}(P_0).
\]
直接乘回给 g=1、c=−1/4、b≠0，两个 V 列在整个 H 三空间的配对相反，且 e=uKv。C0²=1/(4e)，C1=a0 C0、Cw=R C0 也准确成立。由 R²=Q/3，
\[
H(Ku,Ku)=H(Kv,Kv)
=2a_0C_0^2+\frac12R^2C_0^2=e^2/2.
\tag{5.1}
\]
P0 在 H 除子为零，故 Hp=0。(3.4) 在 V 源给 p(u)=p(v)=e；(4.2) 给 yKy=2，即 F=1。

原完整 mean 向量为
\[
\Gamma=(F^2-2p^{\mathsf T}Hp+2\operatorname{tr}((HK)^2))y
-4FHp+8HKHp+4V(p,p,\cdot)-8V:(KHK).
\]
在当前规范，pTHp=0、tr((HK)²)=2hgc=−1/2，故 Gaussian 部分为零；(5.1) 使两个 V 系数也逐个为零。所以 Γ=0。其余梯度正是 (4.3)、(4.4)，因而全部原梯度均为零。

最后，u(s)、u′(s)、u(w)、u(α)、u(β) 是五个独立 confluent 列。Z 的 K 对偶向量正交于其整个五空间；由 (4.2) 和 e≠1，该向量范数非零，所以不在该五空间内。由 η=σΘ≠0，y 又在该五空间之外。这给完整六列基。相应三次张量在此基中含独立的 y³、非退化三维 H 的 yH 项和两个 V 立方项；比较一次收缩的 y²、yH 及两个平方系数，任何消去方向必须为零，故 ess(T3)=6。

这证明显示有理系统与所声明的原规范层完全等价；所有平方根选择只是原可逆尺度实现，不产生被遗漏的复相位分支。

## 6. 可提前使用的原 N 导数门

完整 N 的 w 一次系数另给一个很小的必要方程。设
\[
N_t=k(t,\alpha)k(t,\beta),\quad
r_w=\frac12\partial_w\log N_w,\quad
d_w=\partial_w\log k(s,w).
\]
这里所有 log 只表示非零有理函数的 f′/f。则
\[
\boxed{
QW(r_w-d_w)-2(2e^3+1)\partial_s\partial_w\log k(s,w)=0.
}
\tag{6.1}
\]
证明：取 w1=ρu′(w)，Xj=K(zj,w1)。原 N(w,w1)=0 精确为
\[
eC_w\,K(u-v,w_1)=X_1+a_0X_0.
\]
由 (2.4)，
\[
X_1+a_0X_0
=q\,\partial_s\partial_w\log k+(Q/6)d_w.
\]
又因两 V 配对在 w 相反，
K(u−v,w1)/K(u−v,wvec)=r_w，且 Cw²=Q/(12e)。
代入 qW=−2b=(2e³+1)/3 即得 (6.1)。它保留了完整 2e(u²+v²) 项。

同样，N 在 H 长三除子上的前六个 Hermite 系数可先检查为
\[
\mathcal H(z)-2\mathcal J(z)
+\frac{2e^2}{h}k(z,\alpha)k(z,\beta)
\equiv0\pmod{D_H(z)^2}.
\tag{6.2}
\]
因为 P、S 均被 D_H 整除，而
T²=S²−4UV、UV=(e/h)k(z,α)k(z,β)。
它只含原物理源和 e，尚未引入或求解任何额外 y 系数；(4.3) 的剩余系数仍须检查。

## 7. 两个 V 源均有限时的对称整数输入

本节只改写前述等价重建，便于生成可核对的原理想。令 x=α+β、z=αβ，Δ=x²−4z≠0。用 r 表示极线变量。定义
\[
k(s,a)\equiv A_s+B_s a\pmod{a^2-xa+z},
\quad A_r=A_s|_{s\mapsto r},\quad B_r=B_s|_{s\mapsto r},
\]
\[
N_s=A_s^2+xA_sB_s+zB_s^2,\quad
N_r=A_r^2+xA_rB_r+zB_r^2,\quad
S_*(r)=A_sB_r-B_sA_r.
\]
直接展开两列行列式得
\[
k(s,\beta)k(r,\alpha)-k(s,\alpha)k(r,\beta)
=(\alpha-\beta)S_*(r).
\]
因此实际 $S=\kappa S_*$，其中 $\kappa=\sigma(\alpha-\beta)/k(s,\beta)$；本节使用 $\Theta_*=\eta/\kappa=k(s,\beta)\Theta/(\alpha-\beta)$，准确保留第3节的原尺度。其无平方根尺度为
\[
\Xi=\kappa^2=\frac{e}{q_{\rm pair}N_s},
\quad
q_{\rm pair}=x^3-5x^2+x^2z-6xz+32z-5z^2,
\]
因为 k(α,β)=−Δqpair。相应
\[
\Lambda=\frac{\Delta q_{\rm pair}}{4e^2N_s}.
\tag{7.1}
\]

记 k=k(s,w)，ks=∂s k，
\[
J_0=A_s\partial_sB_s-B_s\partial_sA_s,\quad
E_s=s^2-sx+z,\quad E_w=w^2-wx+z,
\]
\[
W_0=k\partial_sN_s-2N_s\partial_s k,
\]
\[
L_2=2A_sA_w+(A_sB_w+B_sA_w)x+2zB_sB_w.
\]
J0 被 Es 整除；这也直接由原 Wronskian 的 (s−α)(s−β) 因子看出。定义
\[
C_3(s,w,x,z)=
\frac{S_*(w)-(w-s)J_0}{(w-s)^2}.
\]
分子是准确整除。S* 除以 DH(r)=(r−s)²(r−w) 的首一多项式商记 B*(r)；在 J0/Es=C3=0 下余数为零。设
\[
Z(r)=D_H(r)(r^2-xr+z),\quad
Z_n=3200\langle Z,Z\rangle_{K^{-1}},\quad
P_*(r)=S_*(r)+\Theta_* Z(r).
\]
固定 K 的 3200K^-1 是整数矩阵，故 Zn 是真实整数多项式。

引入五个辅助变量 h,l,v,q,t，准确代表 1/k、Λ、Ξ、μ/λ、Θ。以下十二个多项式均来自前文原系统：
\[
\begin{gathered}
J_0/E_s=0,\quad C_3=0,\\
v q_{\rm pair}N_s-e=0,\qquad
4e^2N_sl-\Delta q_{\rm pair}=0,\qquad lq^2b_s-b=0,\qquad hk-1=0,\\
qW_0+4bN_sk=0,\qquad
L_2-2Rl kN_s=0,\\
2eE_st-(1-2e)B_*(s)=0,\\
(Q+6e)B_*(w)+6etE_w=0,\\
q\{(1-2e)B_*'(s)-2et(2s-x)\}-4bB_*(s)=0,\\
vt^2Z_n-6400(1-e)=0.
\end{gathered}
\tag{7.2}
\]
这是未经任意饱和的原尺度系统：第一条尺度式强制 qpair、Ns、v 非零；喷射范数式强制 l、q、bs 非零；随后 λ 尺度式又强制 Δ 非零；hk=1 强制 k 及 w−s 非零。Ns 含 Es²，故 J0/Es 的整除没有删除尚可能分支。C3 与完整单点比例式又迫两个 w–V 配对非零。其余出现的 e、Q、b 都是前述九次域中的已证单位。

要继续检查全部原梯度，设
\[
f=k(s,r),\quad j=\partial_s k(s,r),\quad g=k(w,r),
\quad U=q(j-hk_sf),
\]
\[
\mathcal H=2lf(U+cf)+\frac{q^2b_s}{2b}h^2g^2,\qquad
\mathcal J=blf^2+(U+2cf)hg,
\]
\[
\Omega=\frac{v q_{\rm pair}q^2b_s}{4e^2b}.
\]
由 (7.2)，1/l=q²bs/b、Ω=e/(Δqpair)，故完整原极线准确为
\[
\mathcal N=v(P_*^2+2eS_*^2)+4e\Omega N_r-2\mathcal H+4\mathcal J,
\]
\[
\mathcal C=v(P_*^3+2S_*^3)-6P_*\mathcal H+6\Omega S_*N_r.
\tag{7.3}
\]
这里 $\mathcal C$ 是原最高式除以非零 $2\kappa$ 后的表达式。要求其全部至多 11、16 个系数为零，与第 4 节一致。这里用 UV=−ΩNr，保留原全部 V 项。源码中的有限域计算只用作这个原理想的方向探针；未得到真实 QQ[e]/G9 单位身份之前，不能把模点或模 Gröbner 基推成复数排空。

原对称输入的[自含生成源](../notes/2026-11-26-h21-all-finite-original-modular-structure-347c.py)已经固定于提交816ddd187cbedbcd7af373ebc0ec9db50f3b3145。它的有限域输出只用于推进原方程；本稿等价重建由上述原式的正反向证明给出，不以尚未结束的计算作为证明依据。
