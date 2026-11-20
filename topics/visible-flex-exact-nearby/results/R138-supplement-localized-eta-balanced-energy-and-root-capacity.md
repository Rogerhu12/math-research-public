# R138：真实 η 平衡能量与径向加权根容量

2026-11-20，visible-exact-astra-ac637-20261120 / joint_kernel。

本合同给 R138 同一真实 Qrepair 的局部接收器入口。它保留原物理角、
完整 mean、真实 drift 和全部环境频率，只改用原能量的一个准确平衡
恒等式。没有评估新数值常数，没有把已排除的全域 CE 接收器预算改称通过。

## 1. 两个梯度矩阵的准确抵消

使用 [V.9--11](R138-supplement-Volterra-Grushin-energy-and-root-defect-trace.md) 的同一对象，记

\[
 s=\Theta_\phi=v/m>0,\quad e=a\gamma,\quad
 \eta=-\gamma m>0,\quad
 \kappa=Kv^2,\quad
 \delta=b-uc,\quad Q=\delta^2+\kappa c^2,\quad
 M=1+u^2+\kappa,\quad \sigma=G\cdot n .
 \tag{LC.1}
\]

$\eta$ 只依赖径向变量；此处它是原 moving 输运速度 $-\gamma m$，不是固定的 intrinsic 参数 $\eta_0$，没有改变原背景或度量。令 $w=\omega\circ\Theta$，
$D_rw=(\partial_r-d\partial_\phi)w$，$H^\Theta=H\circ\Theta$。
原准确式为

\[
 D_rw+\gamma uH^\Theta
   =e\{-\delta X+(u\delta-\kappa c)Y\}\circ\Theta,
 \qquad
 w_\phi-sH^\Theta=s\,a(-cX+bY)\circ\Theta .
 \tag{LC.2}
\]

所有系数在需要时按同一 $\Theta$ 拉回。令
$\zeta=(\delta,\sqrt\kappa\,c)^T$。换回 $d\theta$ 并相对于原
能量密度 $ea\sigma|\zeta|^2$，两个平方分别对应矩阵

\[
 \frac{\gamma}{\sigma s}
 \begin{pmatrix}1+u^2&-u\sqrt\kappa\\-u\sqrt\kappa&\kappa\end{pmatrix},
 \quad
 \frac{s}{\gamma\sigma v^2}
 \begin{pmatrix}\kappa&u\sqrt\kappa\\u\sqrt\kappa&1+u^2\end{pmatrix}.
 \tag{LC.3}
\]

给前者权 $\eta^{-1}$、后者权 $\eta$ 后，两个前因子准确相等：

\[
 \frac{\gamma}{\eta\sigma s}
 =\frac{\eta s}{\gamma\sigma v^2}
 =\frac1{\sigma|v|}.
 \tag{LC.4}
\]

两矩阵之和恰为 $M I_2$。因而对任意正径向权 $\alpha(r)$，逐个
真实 $r$ 有准确恒等式

\[
 \begin{split}
 &\int\left\{\frac{\alpha}{\eta}
        |D_rw+\gamma uH^\Theta|^2
       +\alpha\eta K|w_\phi-sH^\Theta|^2\right\}\frac{d\phi}{2\pi}\\
 &\qquad=
 \int\frac{\alpha M}{\sigma|v|}
       ea\sigma Q\,\frac{d\theta}{2\pi}.
 \end{split}
 \tag{LC.5}
\]

此处不是分别用两次矩阵 trace 再相加；两个 off-diagonal 项真实抵消。
对 $K=0$ 的根端按连续极限解释，无须除以 $\kappa$。

两个 $H$ 修正的 Hilbert 直和范数也有准确平方：

\[
 \int\left\{\frac{\alpha\gamma^2u^2}{\eta}|H^\Theta|^2
                +\alpha\eta K s^2|H^\Theta|^2\right\}
        \frac{d\phi}{2\pi}
 =\int\frac{\alpha\gamma(u^2+\kappa)}{|v|}
             |H|^2\,\frac{d\theta}{2\pi}.
 \tag{LC.6}
\]

因此取

\[
 C_{E,\alpha}=\sup\frac{\alpha M}{\sigma|v|},\qquad
 C_{H,\alpha}=\sup\frac{\alpha\gamma(u^2+\kappa)}{|v|},
 \tag{LC.7}
\]

在两个梯度的同一 Hilbert 直和中用 Minkowski，得到

\[
 \left[\int\left\{\frac{\alpha}{\eta}|D_rw|^2
             +\alpha\eta K|w_\phi|^2\right\}dr\frac{d\phi}{2\pi}\right]^{1/2}
 \le\sqrt{C_{E,\alpha}}\sqrt E
       +\sqrt{C_{H,\alpha}}\|H\|_{L^2_rL^2_{\theta,\mathrm{av}}}.
 \tag{LC.8}
\]

这里 $E=\mathcal E/(2\pi)$。无额外因子 $\sqrt2$，完整 $H$ 零模保留。
例如在原每个径向 cell 上取严格已知
$c_i\ge\sup M/(\sigma|v|)$，定义 $\alpha=1/c_i$，即可令
$C_{E,\alpha}\le1$。相应根容量也随 $\alpha$ 改变；不能只缩小 (LC.7)
而仍沿用另一个权的旧容量。整体重标 $\alpha\mapsto t\alpha$ 使
容量乘 $1/t$、两能量系数乘 $t$，最终接收费用不变。

## 2. 原 drift 之后仍是径向两权

令 $\psi_r=-d(r,\psi)$、$\psi(R,\xi)=\xi$，
$z(r,\xi)=w(r,\psi(r,\xi))$，$J=\psi_\xi$。
原已付范围 $\Gamma^{-1}\le J\le\Gamma$ 给

\[
 \mathfrak p=\alpha/\eta,\qquad
 \mathfrak q=\alpha\eta K,\qquad
 \mathcal G_{\mathfrak p,\mathfrak q}[z]
 =\int\{\mathfrak p|z_r|^2+\mathfrak q|z_\xi|^2\}
                  dr\frac{d\xi}{2\pi},
\]
\[
 \sqrt{\mathcal G_{\mathfrak p,\mathfrak q}[z]}
 \le\sqrt\Gamma\{
     \sqrt{C_{E,\alpha}}\sqrt E
       +\sqrt{C_{H,\alpha}}\|H\|_{L^2_rL^2_{\theta,\mathrm{av}}}\}.
 \tag{LC.9}
\]

换元时两个能量分别乘 $J^{-1}$ 和 $J$，所以只用一次 $\Gamma$。
若另有完整径向上界 $g(r)\ge\max(J,J^{-1})$，也可以将
两权同时改为 $\mathfrak p/g,\mathfrak q/g$，使 (LC.9) 右侧不再有
全域 $\sqrt\Gamma$。这是不同容量的准确比较，须重新使用该权的容量，
不能免费把已成全域常数换成未付的局部 $g$。

## 3. 自由外值的准确标量容量

在 $x=r-r_*\in[0,L]$，先取任意有界正权
$0<p_-\le\mathfrak p\le p_+$ 和非负 $\mathfrak q$，后者在正测度集合
上严格为正。对每个环境整数频率 $k\ne0$，定义

\[
 \begin{split}
 s_k&=\inf_{f\in H^1(0,L),\,f(0)=1}
       \int_0^L\{\mathfrak p|f'|^2+k^2\mathfrak q|f|^2\}\,dx>0,\\
 c_k&=1/s_k .
 \end{split}
 \tag{LC.10}
\]

外值完全自由，故对原任意实际方向

\[
 |f(0)|^2\le c_k
       \int_0^L\{\mathfrak p|f'|^2+k^2\mathfrak q|f|^2\}\,dx.
 \tag{LC.11}
\]

极小器满足 $-(\mathfrak p f')'+k^2\mathfrak q f=0$ 和自然
$\mathfrak p(L)f'(L)=0$。后一个条件只属于比较极小器，没有施加给
原方向。原接口处仍仅要求实际 $H^1$ 函数连续；极小器的连续 flux
是变分方程的结果，不是新的原 transmission。

若用逐 cell 常数下界
$\underline{\mathfrak p}\le\mathfrak p$、
$\underline{\mathfrak q}\le\mathfrak q$，则比较能量较小、$s_k$ 较小、
$c_k$ 较大，所以给原 (LC.11) 的合法容量上界。
所有 cell 必须覆盖真实 $[r_*,R]$，包括原根 germ、真实端点与每个原接口。

### 完整有限分段的精确反向递推

在一个常系数 cell，记其真实长度为 $h>0$、
$p=\underline{\mathfrak p}>0$、$q=\underline{\mathfrak q}\ge0$。
令 $s_+$ 为右侧余区的 Dirichlet-to-Neumann 系数；从外端开始
$s_R=0$。若 $q>0$，设

\[
 Z=|k|\sqrt{pq},\qquad t=\tanh(|k|\sqrt{q/p}\,h).
\]
\[
 \boxed{\quad
 s_- = Z\,\frac{s_++Zt}{Z+s_+t}.
 \quad}
 \tag{LC.12}
\]

若 $q=0$，准确的连续极限为

\[
 \boxed{\quad s_-=\frac{s_+}{1+h s_+/p}.\quad}
 \tag{LC.13}
\]

将全部 cell 按真实顺序反向消费后，
$s_{\rm root}$ 就是比较势的 (LC.10)。证明可由
$(f,pf')$ 的准确常系数传递矩阵，或固定左右端值后最小化
cell 能量加 $s_+|f(h)|^2$ 得到。

所有量均非负；递推对 $s_+$ 严格单调。可是 (LC.12) 对 $h$ 的
单调方向取决于 $s_+\lessgtr Z$，故不能一律用真实长度的 lower。
长度有区间时必须完整有向包住此有理双曲表达式，或先证明其单调方向
再取正确端点；(LC.13) 则随 $h$ 增大而减小。
输入 true-length、$p,q$ 的球不能换成 midpoint。

环境 $k=0$ 时 $s_0=0$，自由外值下不能控制根常量。它仅满足

\[
 |f(0)-f(L)|^2
 \le\left(\int_0^L\mathfrak p^{-1}dx\right)
                         \int_0^L\mathfrak p|f'|^2dx .
 \tag{LC.14}
\]

下面只因接收行具有零平均而不消费这个零模；不据角 composition
默认原方向仍有普通零平均。

## 4. 完整加权 Gram 的密度拉回

对任意环境向量 mean-zero 接收行 $a(\phi)$，定义准确根对偶范数

\[
 \mathcal N_{\mathfrak p,\mathfrak q}(a)^2
   =\sum_{k\in\mathbb Z\setminus\{0\}}c_k|\widehat a_k|^2 .
 \tag{LC.15}
\]

它正是 $z\mapsto\langle a,z(0)\rangle$ 对 (LC.9) 能量的平方对偶范数。
由 Fourier 正交、(LC.10) 的各频极小器及 Cauchy--Schwarz 可证；
一般有限能量情形用有限 Fourier 和的闭包。环境三分量全部包含。
有限接收器有各频矩阵 $A_k$ 时，对应完整 Gram 为
$\sum_{k\ne0}c_kA_kA_k^*$，保留不同接收行间的有符号相关性。

**密度转授引理。** 设 $\chi$ 为定向全圈角微分同胚，
$g^{-1}\le\chi'\le g$。定义
$T_\chi a=(a\circ\chi)\chi'$。则

\[
 \langle T_\chi a\rangle=\langle a\rangle=0,\qquad
 \mathcal N_{\mathfrak p,\mathfrak q}(T_\chi a)
 \le\sqrt g\,\mathcal N_{\mathfrak p,\mathfrak q}(a).
 \tag{LC.16}
\]

证明不要求把 $c_k$ 先压成三个 Sobolev 项。对任意测试函数
$v(x,\xi)$，将同一个根角 $\chi$ 固定地延拓到整个径向区间，令
$u(x,\phi)=v(x,\chi^{-1}(\phi))$。准确换元给

\[
 \langle T_\chi a,v(0)\rangle=\langle a,u(0)\rangle,\qquad
 \mathcal G_{\mathfrak p,\mathfrak q}[u]
 \le g\,\mathcal G_{\mathfrak p,\mathfrak q}[v].
 \tag{LC.17}
\]

第二式中径向和角向能量分别乘 $\chi'$ 和 $1/\chi'$；因为权只依赖
径向，二者皆由 $g$ 控制。取对偶 supremum 即得 (LC.16)。
该证明使用的径向固定延拓只是比较测试函数，不替换实际 $\psi(r)$。

取 $\chi=\psi(r_*,\cdot)$ 后，由完整密度配对、(LC.9)、旧 V.8 得

\[
 \begin{split}
 |\langle a,w(r_*)\rangle|
 \le \Gamma\,\mathcal N_{\mathfrak p,\mathfrak q}(a)
 \{(\sqrt{C_{E,\alpha}}+\sqrt{C_{H,\alpha}}h_E)\sqrt E
                    +\sqrt{C_{H,\alpha}}h_B\sqrt B\}.
 \end{split}
 \tag{LC.18}
\]

这保留了真正的加权容量，而未重复产生旧全域 CE 因子。
若密度端及径向能量用了更细的、已经支付的不同 Jacobian 上界，
则分别取对应平方根；不能把某一个上界免费用在另一步。

## 5. 与原 finite 接收器的最小接口

原 [relative R.5--6](R138-supplement-original-high-compression-and-relative-root-receivers.md) 的 $P_c$ 给

\[
 c\cdot Wz=-\rho^{-1}
       \{\langle P_c',w(r_*)\rangle+\langle P_c,\mathsf H\rangle\}.
 \tag{LC.19}
\]

$P_c'$ 因全圈周期导数而严格 mean-zero，所以可用 (LC.18)；$P_c$ 自身
的 mean 仍在第二项保留。一个新的完整消费者只需将旧 R.12 的三项
容量替换成 $\|c\mapsto P_c'\|_{\mathcal N_{\mathfrak p,\mathfrak q}}$，
并使用同一 $\alpha$ 的 (LC.7)。原 $P_c$ 的非齐次 $H^{1/3}$ source
费用、实际 mean 分母、整个 $Q_H$ 逆尾及旧 $r_E,r_B,A_\Theta$ 继续保留。

此处没有授予这些新容量/接收器已经足够小，也没有重新计算旧 X/Y/GB、
原 high 41 球或两模三个矩阵项。数值实现若采用有限 Fourier Gram，
仍须完整包住全部尾；若只计算有限 $c_k$，也必须证明未计算频率的容量
上界。所有新严格门只可消费完整保存并读回的有向球，不能把一个有限
矩阵或局部测试函数冒作完整根读出。
