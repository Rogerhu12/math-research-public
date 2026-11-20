# R138 补篇：截顶线性曲率的完整 H^(1/2) Grushin 常数

2026-11-20，visible-exact-astra-ac637-20261120 / joint_kernel。

**解析结论。** 在同一真实径向区间上，设

\[
\frac{14}{5}<L<\frac{29}{10},\qquad
\delta=\frac1{1840},\qquad
k_{\rm cap}(x)=\min\{46x,1/40\}.
\tag{GB.1}
\]

对所有环境向量场，保留环境零模，且不在根端施加边界条件，有

\[
\boxed{
\|z\|_{L^2_xH^{1/2}_\xi}
\le\frac52\left[\int_0^L\!\int_0^{2\pi}
 \bigl(|z_x|^2+k_{\rm cap}(x)|z_\xi|^2\bigr)\,d\xi\,dx\right]^{1/2}
 +\frac3{\sqrt2}\|z(L)\|_{L^2_\xi}.}
\tag{GB.2}
\]

圆周采用原完整 $2\pi$ 非归一化积分，Sobolev 权为
$\langle k\rangle^s=(1+k^2)^{s/2}$。证明不使用数值 ODE、Airy 函数、
模态截断或未知 BVP 的逆。下面的辅助 Neumann 条件仅用于构造一个
能量正交提升，绝不强加到未知方向上。

本篇只改善体 $H^{1/2}$ 费用。原
[V 补篇](R138-supplement-Volterra-Grushin-energy-and-root-defect-trace.md)
的体 $H^{2/3}$、根 $H^{1/3}$ 及缺陷根 $H^{-1/3}$ 费用保持原合同。

## 1. 外端零迹的全部频率

对任意复标量 $f\in H^1(0,L)$，记

\[
D=\int_0^L|f'|^2,\qquad M=\int_0^L|f|^2,\qquad
E_k[f]=D+k^2\int_0^L k_{\rm cap}|f|^2.
\tag{GB.3}
\]

先证：若 $f(L)=0$，则对每个整数 $k$，

\[
\boxed{\sqrt{1+k^2}\,M\le\frac{25}{4}E_k[f].}
\tag{GB.4}
\]

### 1.1 频率 |k|≤31，包括零模

由外端零迹，$|f(x)|^2\le(L-x)D\le LD$。常势 $1/40$ 与
$k_{\rm cap}$ 仅在 $[0,\delta]$ 不同，故

\[
E_k[f]\ge\left(1-\frac{29k^2}{736000}\right)D+
                 \frac{k^2}{40}M.
\tag{GB.5}
\]

系数在 $|k|\le31$ 严格为正。自由左端、右端零迹的 Poincaré 不等式为
$D\ge\pi^2M/(4L^2)$；可将 $f$ 偶反射到 $[-L,L]$ 后应用两端
Dirichlet 的 Fourier 正弦展开。用 $\pi^2>49/5$ 及 (GB.1)，令

\[
p=\frac{245}{841},\qquad \beta=\frac1{41}.
\]

由 $p<1$、$29/736000<1/1640=1/40-1/41$ 得

\[
E_k[f]\ge(p+\beta k^2)M.
\tag{GB.6}
\]

而

\[
\beta(p-\beta)=\frac{9204}{1413721}>\frac4{625},
\quad
p+\beta k^2
=\beta(1+k^2)+(p-\beta)
\ge2\sqrt{\beta(p-\beta)}\sqrt{1+k^2}
>\frac4{25}\sqrt{1+k^2}.
\tag{GB.7}
\]

这里的有理比较等价于 $5752500>5654884$，从而得到 (GB.4)。

### 1.2 频率 32≤|k|<16000

对 $0\le x\le\delta$、$\delta\le y\le2\delta$，

\[
|f(x)|^2\le2|f(y)|^2+
                    4\delta\int_0^{2\delta}|f'|^2.
\]

先对 $y$ 平均再对 $x$ 积分，得

\[
M\le3\int_\delta^L|f|^2+4\delta^2D
\le\max\{4\delta^2,120/k^2\}\,E_k[f].
\tag{GB.8}
\]

因 $\sqrt{1+k^2}\le|k|+1$，本频段乘上 Sobolev 权后的两个系数分别不超过

\[
\frac{64004}{3385600}<1,\qquad
\frac{120\cdot33}{32^2}<4<\frac{25}{4}.
\tag{GB.9}
\]

此段估计甚至不需 $f(L)=0$。

### 1.3 频率 |k|≥16000

置 $h=(46k^2)^{-1/3}$。由于 $46\cdot16000^2>1840^3$，有
$h\le\delta$，且 $2h<L$。在 $x\ge h$ 上，
$k^2k_{\rm cap}(x)\ge h^{-2}$。重复 (GB.8) 的短条带平均，

\[
M\le3\int_h^L|f|^2+4h^2D\le4h^2E_k[f].
\tag{GB.10}
\]

因此

\[
\sqrt{1+k^2}\frac M{E_k[f]}
\le4\,46^{-2/3}\sqrt{1+k^2}|k|^{-4/3}
\le4\,46^{-2/3}\sqrt2\,|k|^{-1/3}<2<\frac{25}{4}.
\tag{GB.11}
\]

最后仅使用 $46^{2/3}>4$、$\sqrt2<2$。三段覆盖全部整数频率，证明 (GB.4)。
没有按输入方向删去任何环境低频。

## 2. 精确能量提升的完整边界常数

对每个 $k\ne0$，令 $u_k$ 为一维辅助边值问题

\[
-u_k''+k^2k_{\rm cap}u_k=0,\qquad u_k'(0)=0,
\qquad u_k(L)=1.
\tag{GB.12}
\]

令 $u_0=1$。该弱解由零外迹空间上的严格凸能量最小化唯一给出；
非负势的最大值原理给 $0<u_k\le1$。对任意 $f$ 写
$g=f-u_kf(L)$。则 $g(L)=0$，并且分部积分准确给

\[
E_k[f]=E_k[g]+|f(L)|^2E_k[u_k].
\tag{GB.13}
\]

交叉项为零的原因是 $g(L)=0$、$u_k'(0)=0$ 及 (GB.12)，而非 $f'(0)=0$。

现证全部 $k$ 的提升平方常数为

\[
\boxed{\sqrt{1+k^2}\int_0^L u_k^2\le\frac92.}
\tag{GB.14}
\]

零模时左侧是 $L<29/10$。$|k|=1$ 时由 $u_k\le1$ 得
$\sqrt2L<(29/10)\sqrt2<9/2$。

对于 $|k|\ge2$，把势降低为
$k_{\rm step}=0$ 于 $[0,\delta]$，$k_{\rm step}=1/40$ 于
$[\delta,L]$。同一混合边界的最大值原理给 $0<u_k\le v_k$，其中

\[
t=\frac{|k|}{\sqrt{40}},\quad d=L-\delta,\qquad
v_k(x)=
\begin{cases}
\operatorname{sech}(td),&0\le x\le\delta,\\
\cosh(t(x-\delta))/\cosh(td),&\delta\le x\le L.
\end{cases}
\tag{GB.15}
\]

比较方向可直接核对：
$(-\partial_x^2+k^2k_{\rm cap})(v_k-u_k)
=k^2(k_{\rm cap}-k_{\rm step})v_k\ge0$，且差有零外端值及零根端导数。

准确积分为

\[
\int_0^L v_k^2
=\frac{L+\delta}{2}\operatorname{sech}^2(td)
                  +\frac{\tanh(td)}{2t}.
\tag{GB.16}
\]

令 $x=td$、$q=(L+\delta)/(L-\delta)$。由 $L>14/5>201\delta$，
$1<q<101/100$。函数

\[
F(x)=x\operatorname{sech}^2x+\tanh x
\]

满足 $F'(x)=2\operatorname{sech}^2x(1-x\tanh x)$。其唯一最大点
$x_c$ 满足 $x_c\tanh x_c=1$，且 $F(x_c)=x_c<5/4$：
因为 $e^{5/2}>1+5/2+25/8+125/48=443/48>9$，所以
$(5/4)\tanh(5/4)>1$。于是

\[
\begin{split}
\sqrt{1+k^2}\int_0^L u_k^2
&\le\frac{\sqrt{1+k^2}}{2t}
       \{qx\operatorname{sech}^2x+\tanh x\}\\
&<\frac{5\sqrt2}{2}\frac{101}{100}\frac54
=\frac{2525\sqrt2}{800}<\frac92.
\end{split}
\tag{GB.17}
\]

首因子使用 $|k|\ge2$；最后的平方有理比较为
$12751250<12960000$。故 (GB.14) 对所有频率成立。

## 3. 求和、环境均值与闭合

对完整环境 Fourier 系数逐项使用分解 (GB.13)，并将其记为
$z=g+u[z(L)]$。Parseval、(GB.4)、(GB.13) 给

\[
\|g\|_{L^2H^{1/2}}\le\frac52\mathfrak G_{\rm cap}[z]^{1/2}.
\]

(GB.14) 给

\[
\|u[z(L)]\|_{L^2H^{1/2}}\le\frac3{\sqrt2}\|z(L)\|_2.
\]

在同一 Hilbert 范数中使用三角不等式即证 (GB.2)。环境向量的每一分量
都采用相同标量势，故无需另付维数因子；$k=0$ 由 $u_0=1$ 及第 1.1 节
完整控制。两侧以有限能量范数闭合，可由光滑方向延拓到相同有限能量类。
原弱齐次核能量资格仍按照 V 第 9 节进入，不能从本篇单独授予。

## 4. 同一个 Qrepair 的实际消费

沿用 [V](R138-supplement-Volterra-Grushin-energy-and-root-defect-trace.md)
的 $\mathcal E,\mathcal B,H,C_E,C_H,A_\Theta,\Gamma,h_E,h_B$。
[更紧外端与曲率补篇](R138-supplement-sharper-outer-lift-and-capped-curvature-energy.md)
已从相同已成输入证明

\[
\begin{split}
K&\ge k_{\rm cap},\qquad \|\omega_R\|_2\le\frac85\sqrt{\mathcal B},\\
\mathfrak G_{\rm cap}[v_*]^{1/2}
&\le\sqrt\Gamma\{
       \sqrt{C_E}\sqrt{\mathcal E}+\sqrt{C_H}\|H\|_2\},\\
\|H\|_2&\le h_E\sqrt{\mathcal E}+h_B\sqrt{\mathcal B}.
\end{split}
\tag{GB.18}
\]

其中 $v_*=(\omega\circ\Theta)\circ\psi$、$\psi(R)=\mathrm{id}$。
两次 $H^{1/2}$ composition 范数至多 $\sqrt{A_\Theta\Gamma}$，
$\|v_*(R)\|_2\le\sqrt{A_\Theta}\|\omega_R\|_2$。将 (GB.2) 代入，得到

\[
\boxed{\|\omega\|_{L^2_rH^{1/2}_\theta}
\le w_E^{1/2}\sqrt{\mathcal E}+w_B^{1/2}\sqrt{\mathcal B},}
\tag{GB.19}
\]

\[
\begin{split}
w_E^{1/2}
&=\frac52\Gamma\sqrt{A_\Theta}
                 (\sqrt{C_E}+\sqrt{C_H}h_E),\\
w_B^{1/2}
&=\frac52\Gamma\sqrt{A_\Theta C_H}\,h_B
                 +\frac{24}{5\sqrt2}A_\Theta\sqrt\Gamma.
\end{split}
\tag{GB.20}
\]

上标 $1/2$ 是 Sobolev 阶数标签，绝不表示对 $w_E,w_B$ 取平方根。
已成 X/Y 的完整保存球可直接支付 (GB.20)，无需重做径向传播、Jacobi
方向、曲率或 frame 目标。新体误差系数准确为

\[
\begin{split}
a_{EE}&=E_0(w_E^{1/2})^2+E_1w_E^{1/2}h_E,\\
a_{EB}&=2E_0w_E^{1/2}w_B^{1/2}
                +E_1(w_E^{1/2}h_B+w_B^{1/2}h_E),\\
a_{BB}&=E_0(w_B^{1/2})^2+E_1w_B^{1/2}h_B.
\end{split}
\tag{GB.21}
\]

这些为五个新的标量预算；旧 X/Y 的原五个量、原失败门及全对象保持原样。
尤其根缺陷仍使用旧 Y 的 $r=(r_E,r_B)$，因为旧 $H^{2/3}$ 体估计不能由
(GB.19) 代替。本篇没有授予全参数 inverse，也未把同实际 $\eta$ 的
WVC hybrid 当作真实 $DF(Qrepair)$。

## 5. 若新体门通过，可另给根费用预算下界

设新完整保存球的向上端点已证明

\[
a_{EE}<2,\quad a_{BB}<1,\quad
a_{EB}^2<4(2-a_{EE})(1-a_{BB}).
\tag{GB.22}
\]

令 $a_{EE},a_{EB},a_{BB}$ 在本节取这些非负向上端点，旧 $r_E,r_B$
亦取其完整保存球的非负向上端点，并定义

\[
M=\begin{pmatrix}
2-a_{EE}&-a_{EB}/2\\
-a_{EB}/2&1-a_{BB}
\end{pmatrix},\qquad
C_{\rm allow}=\frac{\det M}{2r^T\operatorname{adj}(M)r}.
\tag{GB.23}
\]

(GB.22) 给 $M>0$。若 $r\ne0$，则分母严格正，且
$C_{\rm allow}=1/(2r^TM^{-1}r)$。由 $M$ 内积的 Cauchy–Schwarz，

\[
rr^T\le(r^TM^{-1}r)M,
\qquad
M-C_*rr^T\ge\frac12M>0
\quad\hbox{当 }0\le C_*\le C_{\rm allow}.
\tag{GB.24}
\]

因此若后续同对象完整根型真正支付 $C_*\le C_{\rm allow}$，
V.25 的两能量吸收门有严格余量。本篇没有给出该 $C_*$。
$C_{\rm allow}$ 必须以有向**下界**保存并从保存后的完整十进制球重新读取
其下端点；只用 quotient 的 upper 或 midpoint 无效。若体门不通过，
不计算或发布这一条件目标；若 $r=0$，另按根费用不影响门的精确情形处理，
不能作零分母除法。

整个新消费者只读取完整 X/Y actual 与 execution，并检验身份、成功状态、
旧完整计数和保存球；不调用旧 producer、不恢复旧科学数组、不重算任何旧
成功目标。五个新上界和可选一个下界仍须在公共 Actions 有向计算后才有
数值资格。当前本篇只登记解析定理及其准确消费接口。
