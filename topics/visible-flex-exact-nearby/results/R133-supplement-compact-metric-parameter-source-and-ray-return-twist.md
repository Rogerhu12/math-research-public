# R133：紧支度量参数的完整源与真实射线返回变分

**已证明（准确参数恒等式和可直接支付的横截判据）。**
本篇保留实际目标 $E_\nu=E e^{\nu w}$、完整 mean、近似中心的径向导数、
全部角频率和真实 PPoly 接缝。它不把有限差商当成真实分岔导数，
也没有宣称下面的横截判据已在最终中心上完成原生数值验证。

目标参数的控制函数是原来的
$w=4096t^6(1-t)^6$，$t=(r-1/20)/(13/100)$，
支于 $[1/20,9/50]$，外面准确为零。所有公式在实际 $K_\nu<0$、
$E_\nu-(a')^2>0$ 且中心 $v,m<0$ 的参数域上使用；第一转向点位于控制区间之外，
所以其位置对这个 $\nu$ 准确不变。

## 1. 原目标与全 mean 参数列

记 $\beta=a'/a$、$\gamma=\sqrt{E_\nu}/a$、$K=K_\nu$，
$\Delta=E_\nu-(a')^2$、$s=-a\sqrt{E_\nu/\Delta}$。完整真实内蕴曲率公式给

$$
 \partial_\nu\gamma=\frac w2\gamma,\qquad
 \partial_\nu K=-wK+T w',\qquad T=\frac{\beta}{2E_\nu},
$$
$$
 \partial_\nu s=\sigma_s w,\qquad
 \sigma_s=-\frac{s(a')^2}{2\Delta}\ge0.                    \tag{N.1}
$$

它们对原完整 primitive 目标成立，不是只对有限角平均成立。
例如
$K_\nu=e^{-\nu w}(K_0+\nu\beta w'/(2E))$ 直接给第二式。
第一式来自 $\gamma=\sqrt{E_\nu}/a$；第三式对
$\log(-s)=\log a+\frac12\log E_\nu-\frac12\log\Delta$ 微分。

对于未规范化状态 $Q=(u,v)$，令 $m=\langle v\rangle$、
$S=u^2+Kv^2$、$d=-\beta I S$。固定 $Q$ 的真实 moving 参数源为

$$
 \partial_\nu d=-\beta(\partial_\nu K) I(v^2),
$$
$$
 \begin{aligned}
 (\partial_\nu F)_1={}&(\partial_\nu d)u_\phi
 +\gamma m(\partial_\nu K+wK/2)v_\phi
 -\beta u(\partial_\nu K)v^2,\\
 (\partial_\nu F)_2={}&(\partial_\nu d)v_\phi
 -(w\gamma m/2)u_\phi
 -\beta(\partial_\nu K)v^3.
 \end{aligned}                                         \tag{N.2}
$$

它的真实第二平均准确是

$$
 \boxed{\langle(\partial_\nu F)_2\rangle
       =-\beta m(\partial_\nu K)\langle v^2\rangle.}
 \tag{N.3}
$$

证明中
$\langle I(v^2)v_\phi\rangle
=-\langle(v^2-\langle v^2\rangle)v\rangle$，
故漂移项和 $v^3$ 项留下 (N.3)，不是留下零。
$\gamma$ 参数项是角导，平均确为零。

若使用实际有限变量 $u=\alpha U,v=s+\alpha V$，固定 $U,V,\alpha$
时 $Q_\nu=(0,\sigma_s w)$，所以残差的参数列还包含

$$
 (\partial_\nu Q)_r-DF[\partial_\nu Q]-\partial_\nu F.
 \tag{N.4}
$$

不能只使用 (N.2)，也不能删除 (N.3)。全部 curvature 边界条件在
腰和 $R=25/8$ 的**显式** $\nu$ 列为零：那里 $w$ 及所需端 jet
准确为零，$s_\nu=0$，原真 regular $q_m(R)$ 也未变。
这句话不包括整体位置、独立 mean 高度或最终握持条件。

## 2. 固定完整有限中心的参数族与两条实际特征

先明确一个可计算的中心族：保持整个 $U,V,\alpha$ 和原 dyadic 径向
节点不动，只把实际 $s_\nu$、$K_\nu,\gamma_\nu$ 按 (N.1) 更新。
它是一个明确近似中心族，不是已得到的真实 BVP 解族。

令 $q=\sqrt{-K}$、$c=-\gamma m q>0$。moving 主部的两条特征速度为

$$
 F_\epsilon=\beta I(u^2+Kv^2)+\epsilon c,\qquad
 \epsilon\in\{+1,-1\}.
 \tag{N.5}
$$

其完整角导为
$(F_\epsilon)_\phi=\beta(S-\langle S\rangle)$，
与 $\epsilon$ 无关。沿上述中心族，

$$
 \boxed{\partial_\nu F_\epsilon=A_\epsilon w'+B_\epsilon w,}
 \tag{N.6}
$$
$$
 A_\epsilon=\beta T I(v^2)+
                       \epsilon\frac{\gamma mT}{2q},
 \qquad
 B_\epsilon=\beta K I(2\sigma_s v-v^2)
                       -\epsilon\gamma\sigma_s q.
 \tag{N.7}
$$

证明：$\partial_\nu v=\partial_\nu m=\sigma_s w$，
$\partial_\nu q=-(\partial_\nu K)/(2q)$。对 $c=-\gamma m q$ 微分时，
来自 $\partial_\nu\gamma$ 的 $w\gamma m q/2$ 与
$\partial_\nu K$ 中的 $-wK$ 准确相消，留下

$$
 \partial_\nu c=-\gamma\sigma_s q\,w+
                         \frac{\gamma mT}{2q}w'.
$$

再对 $\beta I(u^2+Kv^2)$ 微分，即得 (N.6)–(N.7)。
这些式子保留 $m$ 的变化；把它固定会遗漏最后一项。

## 3. 消去 $w'$，保留真正径向导数与所有跳

设 $\varphi_\epsilon(r;x)$ 解
$\varphi_r=F_\epsilon(r,\varphi)$、$\varphi(r_0)=x$。
径向分片是预先固定的；速度可有有限的真实 PPoly 跳，但整条特征和
参数变分连续。令

$$
 W_\epsilon(r,t;x)=
 \exp\left(\int_r^t(F_\epsilon)_\phi
                    (\rho,\varphi_\epsilon(\rho;x))\,d\rho\right)>0.
 \tag{N.8}
$$

完整参数变分公式为

$$
 \partial_\nu\varphi_\epsilon(t;x)=
 \int_{r_0}^t W_\epsilon(r,t;x)
       \partial_\nu F_\epsilon(r,\varphi_\epsilon(r;x))\,dr.
$$

以下取 $r_0\le1/20$、$t\ge9/50$，使积分覆盖整个控制支集；若积分在支集内部截断，则必须另保留两端的 $WA_\epsilon w$ 项。由于 $w$ 在两个控制端为零，在每个真实光滑片上分部积分得到

$$
 \boxed{
 \partial_\nu\varphi_\epsilon(t;x)=
 \int W_\epsilon\,w\,G_\epsilon\,dr
 -\sum_{r_i}W_\epsilon(r_i,t;x)w(r_i)
                         [A_\epsilon](r_i,\varphi_\epsilon(r_i;x)),}
 \tag{N.9}
$$
$$
 G_\epsilon=B_\epsilon-
       (\partial_r+F_\epsilon\partial_\phi)A_\epsilon
                         +(F_\epsilon)_\phi A_\epsilon.
 \tag{N.10}
$$

跳约定为右值减左值，所以 (N.9) 的接口符号是负。
目标自身真正连续的接缝不产生虚构跳；中心 PPoly 的准确 dyadic 跳
不能因为很小就删掉。$r_i$ 固定，因此没有额外移动节点项。

尤其 $\partial_rA_\epsilon$ 必须使用实际 PPoly 导数。明确可用

$$
 T'=\frac{\beta'}{2E_\nu}-T\frac{E_\nu'}{E_\nu},\quad
 \gamma'=\gamma\left(\frac{E_\nu'}{2E_\nu}-\beta\right),
 \quad q'=-K'/(2q),\quad
 m'=s'+\alpha V_0',\quad v_r=s'+\alpha V_r,
$$
$$
 \begin{aligned}
 \partial_r A_\epsilon={}&(\beta'T+\beta T')I(v^2)
                    +2\beta T I(vv_r)\\
 &+\frac{\epsilon}{2q}
  \left(\gamma'mT+\gamma m'T+\gamma mT'
                           -\gamma mT\,q'/q\right).
 \end{aligned}                                         \tag{N.11}
$$

$s'=\beta s(1-Ks^2)$ 是真实旋转背景恒等式；
$V_r,V_0'$ 则是原 PPoly 的准确导数，**不能**用近似中心的 PDE 右侧替换。
否则会暗中丢掉正在验证的真实残差。

对有限 $M$ 模 moving 中心，(N.7)、(N.11) 的角支持至多 $2M$，
(N.10) 至多 $4M$。所有分母在本控制区间仅依 $r$；
所以整个 $G_\epsilon$ 的连续角界可用完整有限卷积和闭角余项验证，
没有物理逆角商的无限尾问题。原 intrinsic 数据的无限 primitive 费用
仍属于其径向系数，必须完整保留。

## 4. 真返回横截的明确判据

由连续的角导上界可求
$0<W^-_\epsilon(r,t)\le W_\epsilon(r,t;x)\le W^+_\epsilon(r,t)$。
若 $G_\epsilon$ 在每个闭盒有真实下界 $g_\epsilon(r)$，
则 (N.9) 的统一下界可逐盒由

$$
 \int w\left[
 W_\epsilon^-\,\max(g_\epsilon,0)
 +W_\epsilon^+\,\min(g_\epsilon,0)\right]dr
 -\sum_i W_\epsilon^+(r_i,t)w(r_i)\|[A_\epsilon]_i\|_\infty
 \tag{N.12}
$$

给出；上界相应交换正负部分。这里 $w\ge0$，而不是假定
$G_\epsilon$ 每处都为正。必要时可沿真实特征细化包围；
仅取九个角点不能作为 (N.12) 的全圆门。

记两条向外完整流为 $\Phi_\pm$，真两程返回为

$$P=\Phi_-^{-1}\circ\Phi_+.$$

其准确参数导数为

$$
 \partial_\nu P(x)=
 \frac{\partial_\nu\Phi_+(x)-
                    \partial_\nu\Phi_-(P(x))}
      {\partial_x\Phi_-(P(x))}.                         \tag{N.13}
$$

因此若实际支付了
$\partial_\nu\Phi_+\ge p>0$、
$\partial_\nu\Phi_-\le-n<0$、
$\partial_x\Phi_-\le D$，便得到完整 lift 的
$\partial_\nu P\ge(p+n)/D>0$。没有把一个方向的流直接当成完整返回。

这仍不是任意参数区间上 rotation number 的严格下界：
一般圆微分同胚族可能有有理平台。若另外已经构造完整
$H_\nu\circ P_\nu=H_\nu+\omega_\nu$ 的可微共轭，则真实不变测度给

$$
 \partial_\nu\omega_\nu=
 \int H_\nu'(P_\nu(x))\,\partial_\nu P_\nu(x)\,d\mu_\nu(x).
 \tag{N.14}
$$

只有在该共轭和其参数意义已付的范围内，才能用 (N.13) 得 rotation
twist 和相应算术选择。本文没有预付这些门，也没有消去 Airy 的完整
反射、零阶项或真正正帽返回。

## 5. 真实解族偏离固定系数族的费用

若真实中心族对上述固定 $U,V$ 族另有状态导数
$h_{\rm add}=(\xi,\zeta)$，$z=\langle\zeta\rangle$，
在固定目标下速度的真实附加变分是

$$
 D_QF_\epsilon[h_{\rm add}]
 =2\beta I(u\xi+Kv\zeta)-\epsilon\gamma qz.
 \tag{N.15}
$$

令 $H=\operatorname{diag}(1,-K)$，$R=\sup_\phi\sqrt{u^2+(-K)v^2}$。因此它的完整上界为

$$
 \|D_QF_\epsilon[h_{\rm add}]\|_\infty
 \le\frac\pi4|\beta|R\|H^{1/2}h_{\rm add}\|_\infty
                            +\gamma q|z|.             \tag{N.16}
$$

四重周期完整 $H^1\to L^\infty$ 常数可取 $11/10$（包含 mean），
所以新四态强能量可直接支付第一项，mean 态支付第二项。
将 (N.16) 乘真正 $W_\epsilon^+$ 积分，便是从固定中心族的
(N.12) 转到实际解族所需的显式误差。这个误差若未支付，不能把
固定候选的参数导数称为真实分岔导数。

## 6. 旋转参考的独立核对与剩余实际门

在准确旋转参考 $u=0,v=m=s$，漂移为零。令 $c=-\gamma s q$，
直接用真实曲率公式消去 $E_\nu'$ 得

$$
 c^2=\frac{a''}{a}-\frac{\beta}{2}(\log\Delta)',\qquad
 \partial_\nu\int c\,dr
 =\int w\frac{E_\nu}{\Delta}
                  \left(\frac{\beta}{4c}\right)'dr.
 \tag{N.17}
$$

证明是
$\partial_\nu c^2=-(\beta/2)(wE_\nu/\Delta)'$，再对
$\int\partial_\nu c$ 分部积分；两个支集端项准确为零。
它独立核对 (N.6)–(N.10) 中的 $w'$ 符号和消去。
对于实际非轴对称中心，仍使用 (N.9) 的全部角项与全部跳，
不能沿用参考的符号判断。

后续实际工作需在同一
`ac1d5b98…` 中心上付 (N.10)–(N.12)、完整低 Schur/参数源、
真实解族的 (N.16) 和高频返回算术。本篇完成这些门的准确对象与
可计算公式，没有宣称它们已经数值闭合。
