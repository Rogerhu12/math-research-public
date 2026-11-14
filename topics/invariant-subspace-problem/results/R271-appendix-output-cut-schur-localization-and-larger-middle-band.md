# R271 附录：物理输出切分的同源 Schur 估计与扩大顶带排除

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2116。

状态：**已证明。** 本文在原完整左最小前驱的正规方程中切分物理输出孔层，将长提升块直接配到同一个前驱的非 primitive 部分。这样无需支付整个顶带延拓算子的巨大范数。全部原合法窗口内，远低 primitive 部分可由去掉最后 $3d/8$ 层的中间带重建，误差至多 $e^{-d^4/20}$ 乘原非 primitive 范数；渐近可排除的顶带比例可取任意小于 $1-(128/770)^{1/3}$ 的数。

这是实际左最小者的必要重建条件，不是完整源 Schur 的支撑定理，也没有得到温和的三 Gram 上界。

## 1. 原完整左最小者与三个 primitive 带

固定原 $m\ge8$、$d=2^m$、$4d\le q\le e^{d^3/4}$。沿用[完整左 primitive 坐标](R271-appendix-full-left-primitive-coordinates-and-boundary-schur.md)及[全部源 jets](R271-appendix-source-primitive-jets-and-sequential-right-chain.md)中的
$$
\mathscr P_q=\mathbb C^d\otimes\bigoplus_{n=0}^{q}K_n,
\qquad K_n=\ker D_m\cap\mathcal H_n,
$$
$$
\mathcal E=I+\mathcal C_L,
\qquad
\mathcal C_L=P_{\le q}\sum_{t=1}^{d-1}(-A_m)^tQ_t,
\qquad \mathcal E^*\mathcal E=I+\mathcal C_L^*\mathcal C_L.
\tag{1.1}
$$
每个 $Q_tK_n$ 位于 $\mathcal H_{n+t}\ominus K_{n+t}$，所以 $\mathcal C_L\mathscr P_q$ 与整个 primitive 坐标空间正交。

给定任意原完整源 $r\in\mathscr R_q$，取它的真正最小左前驱
$$
v=E_q^\dagger r=\mathcal E p,
\qquad p=P_0v,\qquad
\nu=(I-P_0)v=\mathcal C_Lp,
\qquad \mu_q(r)=\|v\|,
\tag{1.2}
$$
其中 $P_0=P_{\ker D_m}$ 逐头作用。于是
$$
\|v\|^2=\|p\|^2+\|\nu\|^2.
\tag{1.3}
$$
取整数 $1\le r_*\le d-2$；这里 $r_*$ 是带宽，不是源 $r$。作原物理正交分解
$$
\begin{aligned}
\mathscr P_{\rm lo}&=\mathbb C^d\otimes\!\bigoplus_{n\le q-d+1}K_n,\\
\mathscr P_{\rm mid}&=\mathbb C^d\otimes\!\bigoplus_{q-d+2\le n\le q-r_*}K_n,\\
\mathscr P_{\rm top}&=\mathbb C^d\otimes\!\bigoplus_{q-r_*+1\le n\le q}K_n,
\end{aligned}
\qquad p=u+b_{\rm mid}+b_{\rm top}.
\tag{1.4}
$$
所有头方向均保留。尤其 $b_{\rm mid}$ 包括中间带内的自由头坐标，不仅是强制 jets。

由源 jets 稿的完整零源公式，$\mathscr P_{\rm lo}\subseteq\ker\mathcal B$。因此 (1.2) 的真实最小性允许沿整个 $\mathscr P_{\rm lo}$ 作任意变分，并给准确正规方程
$$
\boxed{u+C_0^*\nu=0,\qquad C_0=\mathcal C_L|_{\mathscr P_{\rm lo}}.}
\tag{1.5}
$$
这个等式在边界自由头已经一同最小化后仍成立；不要求它们为零。

## 2. 在物理输出端切开，不估计整个顶带列

令 $Q_-$、$Q_+$ 是 $\mathcal C_L$ 的非 primitive 输出空间上的物理孔层投影，分别保留
$$
n\le q-r_*+1,\qquad q-r_*+2\le n\le q.
\tag{2.1}
$$
它们互相正交且和为单位。记
$$
C_{0,-}=Q_-C_0,\qquad E_+=Q_+C_0,
\qquad C_{{\rm mid},-}=Q_-\mathcal C_L|_{\mathscr P_{\rm mid}}.
\tag{2.2}
$$
顶带输入孔数至少为 $q-r_*+1$，而 $\mathcal C_L$ 中每项至少升一孔，所以准确有
$$
\boxed{Q_-\mathcal C_L|_{\mathscr P_{\rm top}}=0.}
\tag{2.3}
$$
因此
$$
Q_-\nu=C_{0,-}u+C_{{\rm mid},-}b_{\rm mid}.
\tag{2.4}
$$
把 (2.4) 代入 (1.5)，得到保留同一实际 $\nu$ 的完整恒等式
$$
\boxed{
(I+C_{0,-}^*C_{0,-})u
=-C_{0,-}^*C_{{\rm mid},-}b_{\rm mid}-E_+^*Q_+\nu.
}
\tag{2.5}
$$
特别，没有把 $E_+^*Q_+\nu$ 展开成若干可能很大并互相抵消的顶带项。

定义
$$
G_-=I+C_{0,-}^*C_{0,-}\succeq I,
\qquad
\mathcal T_{m,q,r_*}=-G_-^{-1}C_{0,-}^*C_{{\rm mid},-}.
\tag{2.6}
$$
$\mathcal T_{m,q,r_*}$ 是原 $\mathscr P_{\rm mid}\to\mathscr P_{\rm lo}$ 上的有界算子。它也有直接最小化含义：$\mathcal T_{m,q,r_*}b$ 是
$$
\min_{a\in\mathscr P_{\rm lo}}
\left(\|a\|^2+\|C_{0,-}a+C_{{\rm mid},-}b\|^2\right)
\tag{2.7}
$$
的唯一最小者。这里仅给 (2.6) 的解释；不把 (2.7) 的截断最小者当作原完整左前驱。

式 (2.5) 现在给
$$
\boxed{
u-\mathcal T_{m,q,r_*}b_{\rm mid}
=-G_-^{-1}E_+^*Q_+\nu.
}
\tag{2.8}
$$
故有更强的正能量估计
$$
\boxed{
\begin{aligned}
\|G_-^{1/2}(u-\mathcal T_{m,q,r_*}b_{\rm mid})\|
&\le\|E_+\|\,\|Q_+\nu\|,\\
\|u-\mathcal T_{m,q,r_*}b_{\rm mid}\|
&\le\|E_+\|\,\|\nu\|.
\end{aligned}}
\tag{2.9}
$$
证明只用 $\|G_-^{-1/2}\|\le1$。第一行还等于误差在 primitive 远低部分与其低输出延拓上的完整直和范数。

### 2.1 保留同一源的完整合法前驱替换

还可在原物理左空间中实施这一替换。令
$$
\delta u=u-\mathcal T_{m,q,r_*}b_{\rm mid},\qquad
v_{\rm cut}=\mathcal E(\mathcal T_{m,q,r_*}b_{\rm mid}+b_{\rm mid}+b_{\rm top}).
$$
因为 $\delta u\in\mathscr P_{\rm lo}\subseteq\ker\mathcal B$，$\mathcal E\delta u$ 是原左空间中的真实零源向量。因此 $v_{\rm cut}=v-\mathcal E\delta u$ 仍然具有同一个原源 $r$，且保留了两个边界带的全部坐标。

取任意 $\varepsilon\ge\|E_+\|$。物理输出的正交分解与 (2.9) 给
$$
\begin{aligned}
\|\mathcal E\delta u\|^2
&=\|G_-^{1/2}\delta u\|^2+\|E_+\delta u\|^2\\
&\le\varepsilon^2(1+\varepsilon^2)\|Q_+\nu\|^2.
\end{aligned}
$$
故
$$
\boxed{\|v_{\rm cut}-v\|
\le\varepsilon\sqrt{1+\varepsilon^2}\,\|\nu\|.}
\tag{2.10}
$$
原 $v$ 是完整最小前驱，故与零源向量 $\mathcal E\delta u$ 正交；相应费用准确为
$$
\boxed{\|v_{\rm cut}\|^2
=\|v\|^2+\|\mathcal E\delta u\|^2.}
\tag{2.11}
$$
因此这里的低部重建不仅是坐标近似，还给同一原源的完整合法前驱及明确的非负费用增量。它仍然不把截断 Gram $G_-$ 当成原完整左 Gram。

## 3. 原长提升块的指数界

远低输入孔数至多为 $q-d+1$，$E_+$ 的输出孔数至少为 $q-r_*+2$。因此每个有效提升阶均满足
$$
t\ge d-r_*+1.
\tag{3.1}
$$
沿[原头四次幂预算](R271-appendix-primitive-bandwidth-and-far-schur-localization.md) §4，取
$$
\gamma=770/256,\qquad
\Theta=\log(12\mathcal L)<d^3/2+11,
\quad
\mathcal L=512\sqrt{q+2d-1}(m+q+2d-1)^{3/2}.
$$
每一固定阶的全部输入孔直和满足
$$
\|(-A_m)^tQ_t\|\le
w_t:=\exp[t\Theta-\gamma(t-m)_+^4].
\tag{3.2}
$$
所以
$$
\boxed{\|E_+\|\le\sum_{t=d-r_*+1}^{d-1}w_t.}
\tag{3.3}
$$
没有输入孔数 $q$ 的额外因子；固定阶的不同输入孔层输出正交。

现在取明确带宽
$$
r_*=3d/8.
$$
则 (3.3) 只含 $t\ge5d/8+1$。[深源 Schur 稿](R271-appendix-deep-source-jet-schur-elimination-with-original-flat-cost.md) §2 对完全相同的和已经证明
$$
\boxed{\|E_+\|\le\varepsilon_d=e^{-d^4/20}\qquad(m\ge8).}
\tag{3.4}
$$
为保留常数来源：$m/d\le1/32$，且在 $t\ge5d/8$ 上
$\gamma(t-m)^4-(d^3/2+11)t$ 递增；最左端给
$$
\log w_t\le
-\frac{8230545}{134217728}d^4+\frac{55}{8}d
<-\frac3{50}d^4+\frac{55}{8}d.
$$
再用 $\log d+(55/8)d\le d^4/100$ 即得 (3.4)。

将 (3.4) 代入 (2.9)，对每个原完整源得到
$$
\boxed{
\|G_-^{1/2}(u-\mathcal T_{m,q,3d/8}b_{\rm mid})\|
\le e^{-d^4/20}\|(I-P_0)E_q^\dagger r\|.
}
\tag{3.5}
$$
这里实际中间带缩为
$$
\boxed{q-d+2\le n\le q-3d/8.}
\tag{3.6}
$$

## 4. 任意小于 0.450155… 的顶带比例

置
$$
\theta_*=(128/770)^{1/3},\qquad \rho_*=1-\theta_*.
$$
固定 $0<\rho<\rho_*$，取 $r_*=\lfloor\rho d\rfloor$，并记 $\theta=1-\rho>\theta_*$。对任意
$$
0<c<\gamma\theta^4-\theta/2
\tag{4.1}
$$
及充分大的 $m$，原全部合法 $q$ 上都有
$$
\boxed{\|E_+\|\le e^{-cd^4}.}
\tag{4.2}
$$
这是因为 (3.1) 给 $t/d\ge\theta$，$m/d\to0$，且 $\Theta/d^3\le1/2+o(1)$；函数 $\gamma s^4-s/2$ 在 $s\ge\theta>\theta_*$ 上严格递增而正。有限个至多 $d$ 项的求和因子被 (4.1) 的严格余量吸收。

因此 (2.8)–(2.9) 对整个最后 $\lfloor\rho d\rfloor$ 个 primitive 孔层给同源排除。极限常数约为 $\rho_*=0.450155\ldots$。这比直接估计 $C_0^*C_{\rm top}$ 时所付的两列范数乘积更强：本稿仅估计长提升列 $E_+$，另一端始终是原真实非 primitive 向量 $\nu$。

## 5. 非零实际缺陷必须由较窄中间带重建

取原 $w\in W$，并采用[首源头与中间带稿](R239-appendix-first-source-head-metric-splitting-and-middle-band-schur-amplification.md) §5 的同一个实际源序列 $r_m$、真正左最小者 $v_m=E_{q_m}^\dagger r_m$。既有结论是
$$
v_m\to w,\qquad P_0^{(m)}v_m\to w,
\qquad \nu_m=(I-P_0^{(m)})v_m\to0.
\tag{5.1}
$$
边界 primitive 带位于至少一孔的远尾子空间，故同一实际孔带估计给
$$
b_{{\rm mid},m}\to0,\qquad b_{{\rm top},m}\to0,
\qquad u_m\to w.
\tag{5.2}
$$
由 (3.5)，准确得到
$$
\boxed{
\mathcal T_{m,q_m,3d/8}b_{{\rm mid},m}\longrightarrow w,
\qquad b_{{\rm mid},m}\longrightarrow0.
}
\tag{5.3}
$$
若 $w\ne0$，则 $b_{{\rm mid},m}$ 最终非零，且
$$
\boxed{
\frac{\|\mathcal T_{m,q_m,3d/8}b_{{\rm mid},m}\|}
{\|b_{{\rm mid},m}\|}\longrightarrow\infty.
}
\tag{5.4}
$$
同样可将 $3/8$ 换成任何固定 $\rho<\rho_*$，并使用 (4.2)。

(5.3) 没有另换源，亦没有声称强制源坐标只支持在 (3.6) 内。它读取的是同一个完整左最小者的实际 primitive 中间带，保留其中全部自由头及它们与强制坐标的耦合。$\mathcal T_{m,q,r_*}$ 的实际中间方向仍可能放大；本文未给其温和统一上界，也不能将这里的低输出 Gram $G_-$ 换回完整远低 Gram 后宣称相同结论。完整源三 Gram 比较、无权 $N=M$ 和普通 ISP 均继续开放。
