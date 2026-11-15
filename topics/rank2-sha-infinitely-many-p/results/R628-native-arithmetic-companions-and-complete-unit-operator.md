# R628 — 同一原算术行的伴随深域返回与完整 R/V 单位算子

日期：2026-11-15。**状态：已证明。**

本篇在 R626 的同一整联合上继续。原 $Y$ 单层核与整个
$Y/W$ 平面共同深核可以真正相消，得到保持原 $Y$ principal
测试的伴随深域返回；原 $W$ 则得到四层版本。这些是同一个
原 $q$ 下的 native 算术条件，不需把移动观察冒认成原观察。

进一步，整个 $R/V$ 平面的所有单位剩支可准确压到两个实际来源、
一个共同双单位域和一个收敛的 $2\times2$ 测试算子。
原四 sigma 因子还使其中一侧的前三个条件矩整条消失。
原两中央零的已付范围、四个不同的比值球和仍未关闭的测试都明确列出。

本篇不从有限状态闭包推断积分值非零。R594 的十一个自由系数
对这些完整平面行严格不可见；它们仍可改变不属于该平面的
$H/V$ 局部分配，不能改变本篇的完整单位剩项。

## 1. 同一个整来源与 R601 的真正联合核

沿用 R613、R617、R621、R626 的全部原规范、射线和坏集：
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1.
$$
保原六变量 $(C,Z,Q,r,c,d)$，
$$
\mu_0=\nu_{B_C}\otimes\nu^\flat,\qquad
\nu^\flat=\frac1{42}
(\nu_{f_1}\otimes\nu_\Sigma-\nu_{f_3}\otimes\nu_\Theta)
\otimes\nu_\sigma(r)\otimes\nu_\sigma(c)\otimes\nu_\sigma(d).
\tag{1}
$$
所有原伙伴均保留；$\mu_0$ 的第一 $Y/W$ 边际仍为 $S,6\delta T$。

记
$$
R=(1+3\omega)c+d,\quad K_0=c+(2+3\omega)d,\qquad
a=-3\omega/8,\quad a_W=a+2,
$$
$$
V=a_ZZ+a_QQ+2\delta r+b_KK_0,\qquad
Y=V+aR,\quad W=V+a_WR,
\tag{2}
$$
其中 $a_Z=(-2+\omega)/2,a_Q=(4+3\omega)/2,b_K=-(1+6\omega)/8$。
物理 Gram 为 $\operatorname{diag}(8,263/8)$。
$N(a)=9/64,N(a_W)=313/64$，两者均为当前单位。

本篇使用 R601 **整联合**式 (18)–(19)，而非只用 $S/T$ 边际：
该篇在 $f_1\otimes\Sigma$、$f_3\otimes\Theta$ 两完整五变量
来源上的 whole 核负交换，含真实 $Y$ 反射；取两支之差得
$$
\boxed{
\mu_0|_{\{Y\in p\}}
=\lambda(P_{Y,-\kappa})_*\mu_0,\qquad
\mu_0|_{\{W\in p^4\}}
=\lambda^4(P_{W,\kappa^4})_*\mu_0 .
}
\tag{3}
$$
原 $C$ 与 $Y,W$ 正交，所以 tensor 上 $\nu_{B_C}$ 原样保持。
(3) 包含其全部伙伴、原 half-period 中心和绝对符号。
它不要求第一 $Y$ 来源先作算术投影。

R626 已付同一 $\mu_0$ 的完整平面身份
$$
\boxed{
\mu_0|_{\{R,V\in p^n\}}
=\epsilon_p^n\lambda^{2n}
 (P_{\mathrm{pl},\kappa^n})_*\mu_0,\qquad\epsilon_p^2=1,
}
\tag{4}
$$
其中 $P_{\mathrm{pl},t}$ 在此二平面乘 $t$、在全部正交补为恒等。
$\epsilon_p$ 仍为原实际号，不猜它的值。

## 2. 两条完整伴随核由真限制域相消得到

定义
$$
\boxed{
E_Y=R-c_YY,\quad c_Y=\frac{3+3\omega}{34},\qquad
E_W=R-c_WW,\quad c_W=\frac{19+3\omega}{72}.
}
\tag{5}
$$
这里 $E_Y,E_W$ 不是原 carry 的 $E,F$。
准确有
$$
E_Y\perp Y,\quad N(E_Y)=263/34,\qquad
E_W\perp W,\quad N(E_W)=263/72.
\tag{6}
$$
两个框架 $(Y,E_Y)$、$(W,E_W)$ 相对 $(R,V)$ 的行列式均为 $-1$。
故各自的共同深域都等于 (4) 的真实共同深域，不仅格体积相同。

由于 $P_{Y,-\kappa}$ 固定整个 $E_Y$ 及其余伙伴，(3) 真正给
$$
\mu_0|_{\{Y,E_Y\in p\}}
=\lambda(P_{Y,-\kappa})_*
       (\mu_0|_{\{E_Y\in p\}}).
\tag{7}
$$
左端又由 (4) 等于
$\epsilon_p\lambda^2(P_{\mathrm{pl},\kappa})_*\mu_0$。
映射 $P_{Y,-\kappa}$ 在其整像上可逆；推前对有界测度单射。
只在该像上应用逆并取消外部 $\lambda$，准确得到
$$
\boxed{
\mu_0|_{\{E_Y\in p\}}
=\epsilon_p\lambda(P_{E_Y,\kappa}R_Y)_*\mu_0,
\qquad R_Y=P_{Y,-1}.
}
\tag{8}
$$
物理恒等式是
$P_{Y,-\kappa}^{-1}P_{\mathrm{pl},\kappa}
=P_{E_Y,\kappa}R_Y$。反射没有省掉。

同理，在 $W,E_W$ 都四深的整域中，(3) 和 (4) 的 $n=4$
相消，因 $\epsilon_p^4=1$，得到
$$
\boxed{
\mu_0|_{\{E_W\in p^4\}}
=\lambda^4(P_{E_W,\kappa^4})_*\mu_0 .
}
\tag{9}
$$
这里没有给 $E_W$ 的单层核猜 scalar。
(8)–(9) 是原完整六变量测度身份；不需要另给这两个有理轴
寻找 theta 锚，也没有删除其余四伙伴。

反射 $R_Y$ 保 $E_Y$，与其缩放交换。因此所有 $n,m\ge0$ 均有
$$
\begin{aligned}
\mu_0|_{\{E_Y\in p^n\}}
 &=(\epsilon_p\lambda)^n
   (P_{E_Y,\kappa^n}R_Y^n)_*\mu_0,\\
\mu_0|_{\{E_W\in p^{4m}\}}
 &=\lambda^{4m}(P_{E_W,\kappa^{4m}})_*\mu_0 .
\end{aligned}
\tag{10}
$$
相应共同 $Y/E_Y$ 深度矩形也完全保持：
$$
\mu_0|_{\{Y\in p^r,E_Y\in p^s\}}
=\epsilon_p^s\lambda^{r+s}
 (P_{Y,(-1)^{r+s}\kappa^r}P_{E_Y,\kappa^s})_*\mu_0 .
\tag{11}
$$

## 3. 原 q 与未移动中央的真正传播

固定任意 carry 深度 $N_0\ge1$，使用 R594 的同一个正支
$q=q_{+,N_0}$，包括它全部 $\lambda,\kappa$ 系数及
$D/\kappa^{N_0}$。
原 $C,F,G$ 都与 $Y/W$ 平面正交，所以
$q$ 被 (3)、(8)、(9) 的全部物理映射逐点保持。
原完整 $\pi_4$ 中性身份仍是
$$
(\pi_4)_*(q\mu_0)=\beta^{N_0}(\pi_4)_*\mu_0 .
\tag{12}
$$

$R_Y$ 把 $Y$ 变成 $-Y$，但
$\langle-Y\rangle=\langle Y\rangle$；$E_Y$ 缩放保持 $Y$。
因此对整个 Mellin 参数 $u$，(10) 给
$$
\boxed{
\begin{aligned}
\int_{\substack{E_Y\in p^n\\Y\ {\rm unit}}}
q\langle Y\rangle^{d_pu}\,d\mu_0
 &=(\epsilon_p\lambda)^n\beta^{N_0}J_S(u),\\
\int_{\substack{E_W\in p^{4m}\\W\ {\rm unit}}}
q\langle W\rangle^{d_pu}\,d\mu_0
 &=6\delta\lambda^{4m}\beta^{N_0}J_T(u).
\end{aligned}}
\tag{13}
$$
这是原未移动 $Y/W$ 观察，没有另换归一测试。
相邻深度相减还给完整 $E_Y$ 环带、
以及 $4m\le v_p(E_W)<4m+4$ 的完整四层块；系数分别为
$(\epsilon_p\lambda)^n(1-\epsilon_p\lambda)$ 和
$\lambda^{4m}(1-\lambda^4)$。
因此原两个中央零确实进入所有这些整域。

(13) 不声称固定某个伙伴值后的条件中央也为零；
其余伙伴完整积分仍是原算术行的一部分。

## 4. R/V 两个实际来源的共同双单位域

令 $\mu_1=K_R\mu_0$，并记
$$
\boldsymbol{\mathfrak m}=
\begin{pmatrix}(\pi_{RV})_*\mu_0\\(\pi_{RV})_*\mu_1\end{pmatrix},
\qquad
\mathsf X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\boldsymbol\nu=\mathbf1_{\{R,V\ {\rm unit}\}}\boldsymbol{\mathfrak m}.
$$
R626 的完整两态给
$$
\boldsymbol{\mathfrak m}|_{R\in p}
=\lambda(P_{R,\kappa})_*\mathsf X\boldsymbol{\mathfrak m},
\qquad
\boldsymbol{\mathfrak m}|_{V\in p}
=\epsilon_p\lambda(P_{V,\kappa})_*\mathsf X\boldsymbol{\mathfrak m}.
\tag{14}
$$
下面的式子先在这个准确两变量推前中写出；
有额外隐藏 cut 时，必须回到 R626 的完整转置，不能套边际式。

为核定真正的零行，整个二变量生成函数是
$$
\mathfrak F_i(l,v)=-\frac1{84}\mathcal C_{29}(v)F_i(l,b_Kv),
\quad
\mathcal C_{29}(v)=
\sigma(\delta v)\sigma(2\delta v)\sigma(\gamma v)\sigma(\bar\gamma v),
\tag{15}
$$
其中 $\gamma=3+\omega,\alpha=1+3\omega$，且 R541 已付
$$
F_0(l,m)=\sigma(\alpha l+m)\sigma(l-\bar\alpha m),\qquad
F_1(l,m)=-\sigma(\gamma l+m)\sigma(l-\bar\gamma m).
$$
原纯 $C$ 投影保持 $R,V$，故 (15) 对本篇的 $\mu_0,\mu_1$
就是原六 sigma 的真实推前，没有把 $\nu^\flat$ 换成别的来源。

$\mathcal C_{29}(0)=0$ 且从 $v^4$ 起，所以：

1. 两个完整 $R$ 边际都恒等于零，因而其任意完整 $R$ 测试为零。
2. 对 $k=0,1,2,3$，两个完整条件矩
   $\int V^k\varphi(R)\,d\mathfrak m_i$ 对任意连续 $\varphi$ 都为零。

第二点是 (15) 的整生成函数的前三次导数为零，
不是从总质量为零猜出来的。可合法取
$\varphi=\mathbf1_{R\ {\rm unit}}R^{-k}\langle R\rangle^{d_pu}$。

由 (14) 和这些真零行，准确得
$$
\boxed{
\boldsymbol\nu(1)=0,\quad
\boldsymbol\nu(\langle R\rangle^{d_pu})=0,\quad
\boldsymbol\nu((V/R)^k\langle R\rangle^{d_pu})=0
\quad(k=1,2,3).
}
\tag{16}
$$
这里没有去掉任何单位限制。
特别 $V$ 深、$R$ 单位条带的常数 log 项整条为零，
而它的前三次非恒定项也整条为零。

第一项未消失的条件来源也可以精确显示：
$-\mathcal C_{29}(v)/84=v^4/2+O(v^{10})$，故
$$
\int V^4\varphi(R)\,d\mathfrak m_i
=12\Omega^4\int\varphi\,d\nu_{\phi_i},
\quad
\phi_0=\sigma(\alpha z)\sigma(z),\quad
\phi_1=-\sigma(\gamma z)\sigma(z).
\tag{17}
$$
在原 $\mathcal S_8$ 中，
$$
\phi_0=\sigma^8((1+3\omega)x^3+4b),\qquad
\phi_1=\sigma^8(-(3+\omega)x^3-4\omega b),
$$
$$
\frac{\phi_0+\phi_1}{2}
=(\omega-1)\sigma^8(x^3-2b),\qquad
\frac{\phi_0-\phi_1}{2}
=-2\omega^2\sigma^8(x^3+b).
\tag{18}
$$
这些是 (14) 同一两个来源的条件矩，不给其负四矩新增算术身份。

## 5. 所有单位剩支的完整两来源算子

在共同双单位域置 $z=R/V$。对单位常数 $t$，定义
$$
g_t(z)=\mathbf1_{\{1+tz\ {\rm unit}\}},
\qquad
\boldsymbol J_t(u)=
\int_{\{V+tR\ {\rm unit}\}}
 \langle V+tR\rangle^{d_pu}\,d\boldsymbol{\mathfrak m}.
$$
$t=a,a_W$ 时第一分量分别为 $J_S(u),6\delta J_T(u)$；
第二分量仍为实际第二态的未知算术行。

定义固定大小的矩阵
$$
\mathsf L_k=\lambda\mathsf X(I-\lambda\kappa^k\mathsf X)^{-1},
\qquad
\mathsf H_k=\epsilon_p\lambda\mathsf X
 (I-\epsilon_p\lambda\kappa^k\mathsf X)^{-1}\quad(k\ge1),
$$
$$
\mathsf L_0=\lambda\mathsf X(I-\lambda\mathsf X)^{-1}.
\tag{19}
$$
$k\ge1$ 的分母都是 $1+p\mathcal O$；
$k=0$ 的 $1-\lambda^2$ 已由原 R410 支付为单位。

把整个单位域严格分成
$\{R,V\ {\rm unit}\}$、
$\{R\in p,V\ {\rm unit}\}$、
$\{V\in p,R\ {\rm unit}\}$；
$R,V$ 同时深时 $V+tR$ 不可能为单位。
对第二、第三支分别用 (14)，再按同轴深／单位分解正矩，
得到整个 Mellin 身份
$$
\boxed{
\begin{aligned}
\boldsymbol J_t(u)
={}&\boldsymbol\nu\!\left(
 g_t(z)\langle V\rangle^{d_pu}
             \langle1+tz\rangle^{d_pu}\right)
+\mathsf L_0\boldsymbol\nu(\langle V\rangle^{d_pu})\\
&+\sum_{k\ge1}\binom{d_pu}{k}\kappa^k
 \left[
 t^k\mathsf L_k
  \boldsymbol\nu(\langle V\rangle^{d_pu}z^k)
 +\langle t\rangle^{d_pu}t^{-k}\mathsf H_k
  \boldsymbol\nu(\langle R\rangle^{d_pu}z^{-k})
 \right].
\end{aligned}}
\tag{20}
$$
第一行中的 $g_t$ 保原失败单位支；
不能先把 $\log(1+tz)$ 延到它的非单位处。
最后一项在 $k=1,2,3$ 准确为零，由 (16) 而来。

例如正比矩的真实方程是
$$
\int_{V\ {\rm unit}}(R/V)^k\langle V\rangle^{d_pu}
       \,d\boldsymbol{\mathfrak m}
=(I-\lambda\kappa^k\mathsf X)^{-1}
 \boldsymbol\nu(\langle V\rangle^{d_pu}z^k).
$$
负比矩同理使用第二个逆。
常数 $V$ 行使用 $(I-\lambda\mathsf X)^{-1}$；
常数 $R$ 行则因完整 $R$ 边际零而整条消失。
这些步骤支付 (20) 的全部常数与 log 质量。

级数对 $u\in\mathbb Z_p$ 一致收敛。
求中央导数时
$\left.\partial_u\binom{d_pu}{k}\right|_0
=d_p(-1)^{k+1}/k$；
高阶尾的赋值至少为 $k-v_p(k)$。
当前 $p\ge71$，故截到 $k=3$ 的中央尾属于 $p^4\mathcal O^2$。
没有把大次数分母当单位。

## 6. 两个比值测度及四个不同的真实球

令
$$
\boldsymbol\eta=z_*\boldsymbol\nu,\qquad
\boldsymbol\zeta=z_*(d_p\log\langle V\rangle\,\boldsymbol\nu).
\tag{21}
$$
它们分别是整的两分量有界测度与取值于 $p\mathcal O^2$ 的
两分量有界测度，不是两个待猜常数。
(16) 给
$$
\boldsymbol\eta(1)=0,\qquad
\boldsymbol\zeta(1)=-d_p\boldsymbol\eta(\log\langle z\rangle).
\tag{22}
$$

原 $Y/W$ 失败单位球的中心分别为
$$
y=-1/a=8\omega^2/3,\qquad
w=-1/a_W=-8/(16-3\omega).
$$
新伴随球的中心则为
$$
e=\frac{24(1+\omega)}{263},\qquad
f=\frac{8(19+3\omega)}{263}.
\tag{23}
$$
它们全为单位。四个中心两两之差也全为当前单位：
其范数依次为
$$
\begin{array}{c|c}
y-w&2^{14}/(3^2\cdot313)\\
e-y&2^{14}17^2/(3^2\cdot263^2)\\
f-w&2^{18}3^4/(313\cdot263^2)\\
e-f&2^{14}/263^2\\
e-w&2^{14}349/(313\cdot263^2)\\
f-y&2^{14}349/(3^2\cdot263^2).
\end{array}
\tag{24}
$$
$263$ 已由旧射线排除；$313,349$ 均不在 $p\equiv7\bmod64$；
其余小素数也已排除。因此这是真正四个不同的模 $p$ 球。

记 $\mathbb B(t,n)=\{z-t\in p^n\}$。
在 $\{E_Y\in p^n,Y\ {\rm unit}\}$、$n\ge1$ 上，
$R,V$ 自动都是单位，且
$$
E_Y=V\frac{263}{272}(z-e).
$$
同理，在 $\{E_W\in p^{4m},W\ {\rm unit}\}$、$m\ge1$ 上，
$R,V$ 自动为单位，且
$E_W=V(263/576)(z-f)$。
因此 (13) 在同一个双单位测度上准确成为
$$
\boxed{
\begin{aligned}
\zeta_0(\mathbb B(e,n))
+d_p\eta_0\!\left(
 \mathbf1_{\mathbb B(e,n)}\log\langle1+az\rangle\right)
 &=(\epsilon_p\lambda)^nJ'_S,\\
\zeta_0(\mathbb B(f,4m))
+d_p\eta_0\!\left(
 \mathbf1_{\mathbb B(f,4m)}\log\langle1+a_Wz\rangle\right)
 &=6\delta\lambda^{4m}J'_T .
\end{aligned}}
\tag{25}
$$
同 $q$ 版本在两边整体乘 $\beta^{N_0}$。
这里的两个球上对数自变量均为单位，由 (24) 保证。
这给原中央零的真正局部传播；但不是传播到另两个不同的失败球
$\mathbb B(y,1),\mathbb B(w,1)$。

为完整写出尚余方程，置
$$
k_t(z)=g_t(z)\log\langle1+tz\rangle,
$$
并将 (20) 求导后相减。公共的 $\mathsf L_0\boldsymbol\zeta(1)$
整条相消，得到
$$
\boxed{
\begin{aligned}
\boldsymbol{\mathcal T}
={}&\boldsymbol\zeta(\mathbb B(w,1))
  -\boldsymbol\zeta(\mathbb B(y,1))
  +d_p\boldsymbol\eta(k_a-k_{a_W})\\
&+d_p\sum_{k\ge1}\frac{(-1)^{k+1}\kappa^k}{k}
 \left[
 (a^k-a_W^k)\mathsf L_k\boldsymbol\eta(z^k)
 +(a^{-k}-a_W^{-k})\mathsf H_k\boldsymbol\eta(z^{-k})
 \right].
\end{aligned}}
\tag{26}
$$
第一分量正是 $\mathcal T=J'_S-6\delta J'_T$。
第二分量没有预设零。
(26) 是完整、收敛、仅两来源的原单位剩支算子，
没有另留一个未显示的深域。
但其测试空间仍是有界函数空间，不能把“两个来源”
误称为只剩两个未知数。

原两个中央零准确给 (20) 两个第一分量的导数条件、
以及 (25)。它们尚未使 (26) 中两个失败球的
$\zeta$ 行或完整 $\eta$ 核自动消失。
四球在 (24) 中严格分离，因而没有可免费互换的切集。

## 7. 与原简单极点和负五行的实际首三项

定义同一来源的完整矩
$$
\boldsymbol P_k=
\int_{V\ {\rm unit}}R^kV^{-k}\,d\boldsymbol{\mathfrak m},
\qquad
\boldsymbol Q_k=
\int_{R\ {\rm unit}}V^kR^{-k}\,d\boldsymbol{\mathfrak m}.
$$
(16) 说明 $\boldsymbol Q_1=\boldsymbol Q_2=\boldsymbol Q_3=0$。
令
$$
\boldsymbol{\mathcal N}
=\boldsymbol\nu\!\left(
d_p\{g_a\log\langle V(1+az)\rangle
     -g_{a_W}\log\langle V(1+a_Wz)\rangle\}\right).
\tag{27}
$$
它是原两个各自单位指示在共同 $R/V$ 双单位域上的完整 native
差，不把失败支删去。

R617 的 $P_1$ 是 $\boldsymbol P_1$ 的第一分量。
整个 odd $\mathcal S_8$ 的 $K_R=-1$ 给
$\boldsymbol P_1=(P_1,-P_1)^t$，同样
$\boldsymbol P_3=(P_3,-P_3)^t$。
第二矩由 R626 的两个整来源给
$$
\boldsymbol P_2=
\begin{pmatrix}
2(\omega-1)P_D-4\omega^2P_\Theta\\
2(\omega-1)P_D+4\omega^2P_\Theta
\end{pmatrix},
\quad
P_D=\int_{V\ {\rm unit}}V^{-2}\,d\xi_D,\quad
P_\Theta=\int_{V\ {\rm unit}}V^{-2}\,d\xi_\Theta .
\tag{28}
$$
这是原同一第二矩的完整分解，不赋两个分量共同 scalar。

第三矩也没有引入模糊的新来源：
在 entire $\mathcal S_8\otimes\mathcal S_8$ 中，
$\partial_l^3F_0(0,m)=-144\omega b\,y_\wp(m)\sigma(m)^8$。
其型五奇线唯一，系数由原
$\sigma(z)=z+bz^7/210+\cdots$ 的完整 $l^3m^5$ 项确定。
所以原 $\nu_3$ 准确为
$$
\frac{24\omega b\Omega^3}{7}\,
\nu_{B_C}\otimes
(\nu_{f_1}\otimes\nu_\Sigma-\nu_{f_3}\otimes\nu_\Theta)
\otimes\nu_\sigma(r)\otimes\nu_{-y_\wp\sigma^8}(K_0),
\tag{29}
$$
且 $P_3=\int_{V\ {\rm unit}}V^{-3}\,d\nu_3$。

写
$$
c_2=2-3\omega/4,\qquad c_3=(-229+171\omega)/96,\qquad
P_2^*=2(\omega-1)P_D+4\omega^2P_\Theta .
$$
从 (20) 的两个真条带直接得到第一分量的实际展开
$$
\boxed{
\mathcal T
=\mathcal N_0+2d_p\lambda\kappa P_1
+d_p\lambda c_2\kappa^2P_2^*
-d_p\lambda c_3\kappa^3P_3+p^4\mathcal O .
}
\tag{30}
$$
$V$ 深支的完整第一非零可能项是 (17) 的第四条件矩；
它已被保在 $p^4$ 尾内，不被假定为零。

R621 的原有限身份
$P_1=(-36b_K)\Omega^5I_1+\mathcal B_1$ 于是给
$$
\boxed{
\mathcal T
=\mathcal N_0+
2d_p\lambda\kappa
 \{(-36b_K)\Omega^5I_1+\mathcal B_1\}
+p^2\mathcal O .
}
\tag{31}
$$
这直接连接同一个完整 native 单位剩项、原负五行及全部
$H/V$ 边界；不是另造一个单位见证。
原两中央零时，(30)–(31) 的左端为零，
右端显示的补偿全部仍存在。
特别不从 $-36b_K$ 为单位推 $I_1$ 或 $\mathcal N_0$ 非零。

## 8. 十一个自由 q 方向在这些完整行上严格不可见

(12) 对任何满足 R594 全部九行和原 $B_C$ 归一的二十列系数
都成立。它也准确传给实际第二态：
$$
\boxed{(\pi_4)_*(q\mu_1)=\beta^{N_0}(\pi_4)_*\mu_1.}
\tag{32}
$$
证明不需要猜新来源的 theta 系数。
先在 (12) 两边限制 $R\in p$；因 $R=(W-Y)/2$，
此限制属于真正 $\pi_4$ 条件。
再用 $\mu_0|_{R\in p}=\lambda(P_{R,\kappa})_*\mu_1$。
$q\circ P_{R,\kappa}=q$，且 $P_{R,\kappa}$ 在 $\pi_4$
中诱导一个在其整像上可逆的映射。
取消 $\lambda$ 和这个单射推前，便是 (32)。

因此对任意完整连续 $f(R,V)$，包括所有紧开单位指示、(20)–(31)
的收敛核以及 (25) 的球，
$$
\boxed{
\int q f(R,V)\,d\mu_i
=\beta^{N_0}\int f(R,V)\,d\mu_i,\qquad i=0,1.
}
\tag{33}
$$
这覆盖整个原平面上的全部域，而不只一个总质量。
两个可行系数之间的十一个中性方向对这些行都严格给零。

这不意味着这些方向在任意隐藏 cut 上也无作用。
R626 的 $H/V$ word 交域含非 $\pi_4$ 条件，
其原 $q\circ\mathsf A\mathsf B$、
$q\circ\mathsf B\mathsf A$ 和两条不同 native 测试仍必须保留。
尤其 (31) 中可对整个平面式抽出 $\beta^{N_0}$，
却不能把它擅自分配成每个原 $q$ 加权的
$H$ 深、$V$ 深或有理余项；后者仍按 R626 的完整转置处理。

已付的新算术传播是 (13)、(25)；已付的完整单位剩支是
(20)、(26)、(30)。
尚需的是原两个失败球和其余单位比值上的实际测试关系，
或带原隐藏条件的 word 补偿能否合法给该关系。
既有三中央条件、质量单位或状态数有限均不自动完成这一步。

## 精确文件与依赖

- [精确脚本](../scripts/check-r628-native-companions-and-complete-unit-operator.js)
- [精确证书](../scripts/check-r628-native-companions-and-complete-unit-operator.json)
- [R601：原 Q 两张量与全五变量 Y/W 核](R601-original-q-tensors-complete-y-w-cores-and-fifteen-source-spectrum.md)
- [R626：完整 R/V 两态、H/V word 与全部边界](R626-original-v-core-and-finite-native-boundary.md)
- [R594：同一整九行补偿及十一中性方向](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)
- [R541：原第二态的实际双 sigma 身份](R541-original-degree8-second-state-and-exact-sigma-transport.md)
- [R617：原第一矩与简单极点](R617-original-norm8-annulus-and-negative-five-pole.md)
- [R621：原负五有限补偿](R621-original-six-degree-finite-pole-compensation.md)

证书以 BigInt 的 $\mathbb Q(\omega)$ 算术核定原平面、
两伴随及整个物理矩阵的符号 $\kappa$ 身份、
四中心全部差范数和实际条件矩常数。
完整 restriction/pushforward 相消、Mellin 一致收敛和
所有剩支量词由正文证明。
