# R138 补篇：从真实根启动的局部 drift 与准确容量

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

本篇在[LC 平衡能量](R138-supplement-localized-eta-balanced-energy-and-root-capacity.md)
上给一个不同的、完整保留 Jacobian 的根接收器。它使用同一真实 Qrepair、
同一 moving 角和原 $d$，只改变辅助 drift flow 的初值位置。
全域 GB 体比较仍可使用原外端锚定的另一个辅助 flow；两者都是对同一原场的
合法不等式，没有把它们当成同一个坐标映射。

## 1. 真根锚定，不再变换根接收行

固定任意真正局部正区 $I_c=[r_*,r_c]$。令

$$
w(r,\phi)=\omega_{phys}(r,\Theta(r,\phi)),\qquad
D_rw=(\partial_r-d\partial_\phi)w.
\tag{RA.1}
$$

在完整圆周上解明确的辅助初值问题

$$
\psi_r(r,\xi)=-d(r,\psi(r,\xi)),\qquad
\psi(r_*,\xi)=\xi,
\quad z(r,\xi)=w(r,\psi(r,\xi)).
\tag{RA.2}
$$

原 piecewise radial、角上 $C^1$ 系数及完整 finite-energy 域足以按原唯一
Carathéodory flow 定义此映射；原相同周期和原对称性被保留。
没有使用 $r_*\!$ 的中点或 enclosure端点作为实际初值。

一阶变分式准确为

$$
J_r=-d_\phi(r,\psi)J,\qquad J(r_*,\xi)=1,
\quad J=\psi_\xi>0.
\tag{RA.3}
$$

因此任何完整 $D_c\ge\int_{r_*}^{r_c}\|d_\phi(r)\|_\infty dr$ 给

$$
\Gamma_c=e^{D_c},\qquad
\Gamma_c^{-1}\le J(r,\xi)\le\Gamma_c.
\tag{RA.4}
$$

根上 $z(r_*,\xi)=w(r_*,\xi)$ **准确相同**。若接收行 $P'$已在原 moving $\phi$
中构造，根配对就直接为 $\langle P',z(r_*)\rangle$，无需 density pullback，
也不再支付旧 LC.16 的另一个 $\sqrt\Gamma$。
这不是把未知实际 physical $\Theta$ 换成恒等；$\Theta$仍在(RA.1)和原接收器中。

## 2. 只付一次局部 Jacobian 的完整容量读出

取任意正径向权 $\alpha$。保持 LC 的

$$
p=\alpha/\eta,\quad q=\alpha\eta K,\quad \eta=-\gamma m>0,
$$
$$
C_{E,\alpha}\ge\sup_{I_c,\phi}\frac{\alpha(1+u^2+Kv^2)}{\sigma|v|},
\qquad
C_{H,\alpha}\ge\sup_{I_c,\phi}\frac{\alpha\gamma(u^2+Kv^2)}{|v|}.
\tag{RA.5}
$$

由 $z_r=(D_rw)\circ\psi$、$z_\xi=(w_\phi\circ\psi)J$，换元后的径向和
角向能量分别付 $J^{-1}$、$J$，所以

$$
\sqrt{\mathcal G_{p,q}[z]}
\le\sqrt{\Gamma_c}
\{\sqrt{C_{E,\alpha}}\sqrt E+
  \sqrt{C_{H,\alpha}}\|H\|_{L^2_rL^2_{\theta,av}(I_c)}\}.
\tag{RA.6}
$$

$E=\mathcal E/(2\pi)$；将局部物理能量增大为全域原 $E$ 是合法的。
完整 $H$ 局部范数也可直接用旧全域
$h_E\sqrt E+h_B\sqrt B$。没有删除局部或全域 $H$ mean。

以 LC.10–LC.15 的同一径向两权，在 $I_c$ 上取自由外值的准确容量范数
$\mathcal N_{p,q}$。对严格 mean-zero 的周期导数行 $P'$，

$$
|\langle P',w(r_*)\rangle|
\le\sqrt{\Gamma_c}\,\mathcal N_{p,q}(P')
\{(\sqrt{C_{E,\alpha}}+\sqrt{C_{H,\alpha}}h_E)\sqrt E
 +\sqrt{C_{H,\alpha}}h_B\sqrt B\}.
\tag{RA.7}
$$

不要求 $r_c$ 是原外端，亦不要求未知解在 $r_c$ 满足任何边界条件。
free-outer极小器的自然 Neumann 条件仍只属于比较问题。
环境零模仅因 $P'$是周期导数而不被这一个 functional读取，
没有被从原 $w$或 $H$ 方程删除。

## 3. 原 finite 接收器、Theta 与完整 source

沿用[relative R.5–R.6](R138-supplement-original-high-compression-and-relative-root-receivers.md)
的准确式

$$
c\cdot Wz_L=-\rho^{-1}
 \{\langle P_c',w(r_*)\rangle+\langle P_c,\mathsf H\rangle\},
\qquad \rho=a/m.
\tag{RA.8}
$$

这里 $P_c'$是同一 moving 角的 periodic derivative，$P_c$本身的mean保留。
设 $N_W\ge\sup_{|c|=1}\mathcal N_{p,q}(P_c')$，
$P_{W,1/3}\ge\sup_{|c|=1}\|P_c\|_{H^{1/3}}$。
原真实密度 $\mathsf H=\Theta_\phi(H\circ\Theta)$仍付
$\|\mathsf H\|_{H^{-1/3}}\le\sqrt{A_\Theta}\|H\|_{H^{-1/3}}$。
故完整读出系数可取

$$
\boxed{\begin{split}
\alpha_E^{root}(W)
&=|\rho|^{-1}\{\sqrt{\Gamma_c}N_W
       (\sqrt{C_{E,\alpha}}+\sqrt{C_{H,\alpha}}h_E)
       +P_{W,1/3}\sqrt{A_\Theta}\,r_E\},\\
\alpha_B^{root}(W)
&=|\rho|^{-1}\{\sqrt{\Gamma_c}N_W
       \sqrt{C_{H,\alpha}}h_B
       +P_{W,1/3}\sqrt{A_\Theta}\,r_B\}.
\end{split}}
\tag{RA.9}
$$

原 $r_E,r_B$仍是 Y 已付的真正 root $H^{-1/3}$ source界。
原独立mean的 $D$、原 $Q_H$ Neumann逆及完整尾没有改变或免除。
非归一化能量与 $(2\pi)$ 根型之间的因子，按原 relative/RT 约定同乘消去。

即使全域体比较使用原外锚定 flow，也可与(RA.9)同时用于同一原未知方向。
它们分别估计 body norm 和 root functional，未把两个 flow 的中间函数相互等同。
这使体谱改进与本局部根接收器在数学上可以独立组合。

## 4. 原 d 的完整闭行费用与可直接复用的全域界

原 moving drift 准确为

$$
d=-\beta I_\phi S,\qquad
S=u^2+Kv^2,\qquad d_\phi=-\beta\Pi_0S,
\tag{RA.10}
$$

$I_\phi$和 $\Pi_0$保留原有序 primitive/去均值定义；mean $m$仍在 $v$ 中。
此处是实际 moving $\phi$导数，原 `drift_phi_A0`已经包含物理频率 $4j$，
不再额外乘4，亦不先转成physical角导数。

body每个原闭行已经保存 `bounds.drift_phi_A0`，记其上端 $d_i$；
$U_i,V_i$为原完整 Wiener $A_0$界，$\beta_i,K_i$为原intrinsic绝对上界。
这里原修补证书给的是完整 pair 界
$\|e_u\|_{A_0}+\|e_v\|_{A_0}\le\varepsilon$；因此两分量平方和至多为
$\varepsilon^2$，不是把两个独立 $\varepsilon$ 界相加。
直接复用 X 已证的完整 repair费

$$
\Delta S_i\le\max(1,K_i)\{2(U_i+V_i)\varepsilon+\varepsilon^2\},
\quad
\widehat d_i=d_i+2\beta_i\Delta S_i,
\qquad\varepsilon=4\cdot10^{-18}.
\tag{RA.11}
$$

root germ的原Wiener strip包围支配真圆周 $A_0$，所以其原未修补输入可取

$$
d_g\le |\beta|_g(U_g^2+|K|_gV_g^2),
\tag{RA.12}
$$

再付同(RA.11)。这里利用 $\Pi_0$的 Wiener norm不增性质，不把仅点态 $C^0$
source当成可用 $1/4$ primitive的包围。所有费用与旧 X 的背景定义完全一致。

原 X 已完成整个 $[r_*,R]$ 的非负积分 $D_0$及 $\Gamma=e^{D_0}$。
因此对任一子段，已经合法有

$$
\Gamma_c\le\Gamma_{old}.
\tag{RA.13}
$$

仅此已允许在新的根锚定接收器中用 $\sqrt{\Gamma_{old}}$；
不能把(RA.13)误写成 $\Gamma_c=1$。
进一步证明短段费用接近1，需要一个新的完整局部积分，不能由原global scalar反推。

## 5. 固定根层 1/100 的最小新 scalar 目标

可以固定 $r_c=r_*+1/100$，只新计算

$$
D_{loc}\ge\int_{r_*}^{r_*+1/100}\|d_\phi\|_\infty dr,
\qquad \Gamma_{loc}=e^{D_{loc}}.
\tag{RA.14}
$$

真正积分以整根区间保守扩至 $[r_{lo},r_{hi}+1/100]$；
首片用whole germ，其后保留所有原positive行、candidate/intrinsic接口。
本integrand是正闭行标量，故无需任何新ODE或新的Fourier系数。
以原整行(RA.11)上端乘精确相交长度相加即可；不用因子分片来虚构更紧旧 norm。

最小输入为原positive4+germ1，读取两完整native；另读整个旧X actual+execution，
保持same Qrepair/参数、原mean/interface/physical规范。只用原完整已付背景包围，
不读取候选5shards，不调用RS的T积分或任何旧X/Y/GB/geometry目标。
最终只需保存新的 $D_{loc}$ upper和新 $\Gamma_{loc}$ upper；
前者完整保存读回后才能取exp，后者也完整保存读回后进入(RA.9)。

若要同时消费一个新的体谱预算，两个对象须各自完整，不能把一个局部prefix当作
全域谱成功。任意期望的“接近1”门必须在新合同预先写明，并用完整保存球判断；
本纯证明没有为 $\Gamma_{loc}$赋予尚未得到的数值。
原96×96根负部、完整high返回/尾、准确容量Gram及全局非线性仍由其自己的合同处理。
