# R42：实际 Airy 传播的一整阶增益、有限 Dyson 余项及通量框架

2026-11-12，visible-exact-astra-f6a2。

**范围。** 在 R39 同一个真实 canonical simple-turn 组件上，可积的根部
奇性把传播增益提高到一整阶。有限次真实 Volterra 积分给任意预定有限阶
的强余项，含全部角频率、均值和普通源；有限近似的 Green 通量缺陷及
一个准确 $J$-酉修正也有明确界。系数可大，真实短 collar 支付其费用。

这不是 classical symbol expansion，不识别完整主返回、Maslov 相位或
R40 的实际低阶系数，也不解决全网反馈或非线性收敛。所用正则仍是
R39 的真实有限 Sobolev/jet 输入，未自动授予当前 C4 样条。

## 1. 同一个实际振幅系统与一整阶增益

沿用 [R39](R39-finite-component-airy-transfer-input.md) 的记号，
$q=2\pi/\ell$、$E_s=(H^s_\ell)^2$，$0\le\xi\le\delta\le h\le1$。
真实方程与完整框架为

\[
 U_{\xi\xi}-\xi U_{\phi\phi}+VU=f,\qquad
 (U,U_\xi)^t=F_*(\xi)z,\qquad z'=\mathcal K(\xi)z+\Gamma_f(\xi).
 \tag{1.1}
\]

$V$、$\mathcal K$、$\Gamma_f$ 就是 R39(5.4) 的完整对象。
选足够大的有限 Sobolev 档表，包含下面所有中间档和负阶对偶档。
记 R39 的同档常数为

\[
 K_s^{(0)}=100\pi\max(1,2^{1/3}q^{-2/3})M_{s+1/3}(V),
 \qquad \delta\max_sK_s^{(0)}\le1/10.
 \tag{1.2}
\]

则完整传播 $C(\xi,\eta)$ 在这些档上的正逆 norm 均不超过 $e^{1/10}$。
R39 的负实轴 Airy 界还给，对 $\xi>0$，

\[
 \|D_\pm(\xi)\|_{H^s\to H^{s+1/2}}
 \le10c\max(1,2^{1/4}q^{-1/2})\xi^{-1/4}.
 \tag{1.3}
\]

均值列由 $\xi\le1$ 同时控制。将此式用于 $\mathcal K$ 的两侧，
row/column 的两个 $\sqrt2$ 和 $\pi/(2c^2)$ 合为 $\pi/c^2$，得到

\[
 \boxed{\ \|\mathcal K(\xi):E_s\to E_{s+1}\|
       \le B_s\xi^{-1/2},\qquad
 B_s=100\pi\max(1,\sqrt2/q)M_{s+1/2}(V).\ }
 \tag{1.4}
\]

这个根部奇性可积。因此准确的 $C-I=\int\mathcal K C$ 给

\[
 \boxed{\ \|C(\xi,\eta)-I:E_s\to E_{s+1}\|
 \le2e^{1/10}B_s|\sqrt\xi-\sqrt\eta|.\ }
 \tag{1.5}
\]

反向传播也成立。先在 $\xi>0$ 的平滑数据上积分，再由 (1.4) 的
Bochner 可积主控延拓到根；没有假定 $\mathcal K(0)$ 的一阶增益 norm 有限。

## 2. 完整有限 Dyson 展开

先令 $\eta\le\xi$，置 $T_0=I$，

\[
 T_n(\xi,\eta)=
 \int_{\eta<t_1<\cdots<t_n<\xi}
       \mathcal K(t_n)\cdots\mathcal K(t_1)\,dt,\qquad
 P_N=\sum_{n=0}^NT_n.
 \tag{2.1}
\]

反向用有序反向积分。记

\[
 L=2|\sqrt\xi-\sqrt\eta|,\quad
 b_{s,n}=\prod_{r=0}^{n-1}B_{s+r},\quad b_{s,0}=1.
 \tag{2.2}
\]

**定理。** 每一项是真实全 Fourier 算子，且

\[
 \|T_n:E_s\to E_{s+n}\|\le L^n b_{s,n}/n!,
 \tag{2.3}
\]
\[
 \boxed{\ \|C-P_N:E_s\to E_{s+N+1}\|
 \le a_{s,N+1}:=e^{1/10}L^{N+1}b_{s,N+1}/(N+1)!.\ }
 \tag{2.4}
\]

**证明。** 最右 $\mathcal K(t_1)$ 用 $B_s$，后续依次用
$B_{s+1},\ldots,B_{s+n-1}$；标量有序积分准确为

\[
 \int_{\eta<t_1<\cdots<t_n<\xi}\prod_i t_i^{-1/2}\,dt
 =\frac1{n!}\left(\int_\eta^\xi t^{-1/2}dt\right)^n=L^n/n!.
 \tag{2.5}
\]

每一步都在整个 $E_s$ 上估计，不由单列 norm 免费推断全算子界。
迭代真实 Volterra 方程 $n=N+1$ 次，余项是

\[
 R_n:=C-P_N=
 \int_{\eta<t_1<\cdots<t_n<\xi}
 \mathcal K(t_n)\cdots\mathcal K(t_1)C(t_1,\eta)\,dt.
 \tag{2.6}
\]

最右的 $C$ 只在初始 $E_s$ 使用 $e^{1/10}$，之后用 $n$ 个一阶
增益界，即得 (2.4)。反向同理。高阶 $B_{s+r}$ 只进入有限乘积。证毕。

若 $B_*\ge\max_{0\le r<n}B_{s+r}$，可选共同门

\[
 2B_*\sqrt\delta\le\varepsilon_*,\qquad
 a_{s,n}\le e^{1/10}\varepsilon_*^n/n!.
 \tag{2.7}
\]

给定实际有限表，取 $\delta\le\varepsilon_*^2/(4B_*^2)$，再与
(1.2) 和 R39 的实际坐标 collar 门同时取小。严格 cut 的
$\delta^{-1/4}$ 等 trace 费用仍须计入，不能称缩短 collar 没有代价。

## 3. 普通源、双 Cauchy 迹和通量缺陷

用同一个 $P_N$ 定义

\[
 z_N(\xi)=P_N(\xi,0)z_0+
       \int_0^\xi P_N(\xi,t)\Gamma_f(t)\,dt.
 \tag{3.1}
\]

R39 给 $G_\ell=\pi C_D/(\sqrt2c^2)$ 及
$\|\Gamma_f(t)\|_{E_s}\le G_\ell\|f(t)\|_{H^{s-1/3}}$。
令 $a^*_{s,n}$ 为 (2.4) 用 $L=2\sqrt\delta$ 的值，则

\[
 \boxed{\ \|z-z_N\|_{C([0,\delta];E_{s+n})}
 \le a^*_{s,n}\bigl(\|z_0\|_{E_s}
             +G_\ell\|f\|_{L^1_\xi H^{s-1/3}}\bigr),\quad n=N+1.\ }
 \tag{3.2}
\]

所有 mean、cross sign 和源项都保留。物理源仍通过 R39 的 Jacobian、
height 和 divergence 附加零阶项；任意弱源不自动满足这个强 source 门。
在严格 cut 乘 $F_*(\delta)$，得到
$H^{s+n+1/2}\oplus H^{s+n-1/2}$ 中误差至多 $B_\delta$ 乘 (3.2)
右端；根 pair 输入再付 $I_0$。第二槽始终是完整 momentum。

对实 $V$，准确有 $C^*JC=J$，$J=\operatorname{diag}(I,-I)$。
若 (2.4) 同时在 $s$ 及 $-s-n$ 有界，真实对偶给

\[
 \|R_n^*:E_s\to E_{s+n}\|\le a_{-s-n,n}.
 \tag{3.3}
\]

由 $C^*=JC^{-1}J$，相应档上 $C^*$ 的 norm 也至多 $e^{1/10}$。
准确恒等式

\[
 P_N^*JP_N-J=-C^*JR_n-R_n^*JC+R_n^*JR_n
 \tag{3.4}
\]

从而给

\[
 \|P_N^*JP_N-J:E_s\to E_{s+n}\|
 \le e^{1/10}(a_{s,n}+a_{-s-n,n})+a_{s,n}a_{-s-n,n}.
 \tag{3.5}
\]

这里负阶输入是实付条件；只有正阶单列误差不够建立共同 Green 形式。

## 4. 有明确门的准确 $J$-酉修正

在预选有限档表及所需对偶档上，假设 (2.7) 已使 $a_{s,n}\le a$，
并满足

\[
 e^{1/10}a<1,\qquad r:=2e^{1/10}a+a^2\le1/2.
 \tag{4.1}
\]

欲控制 $E_s\to E_{s+n}$，同时付 $s,s+n,-s-n,-s-2n$ 对应的
有限展开费用。令

\[
 E=JP_N^*JP_N-I,\qquad
 W=(I+E)^{-1/2}=\sum_{k\ge0}{-1/2\choose k}E^k,\qquad Q_N=P_NW.
 \tag{4.2}
\]

(3.5) 与同档嵌入给 $\|E\|\le r$，故级数在所有声明的同档 norm 中
绝对收敛。$P_N=C(I-C^{-1}R_n)$ 由 (4.1) 可逆，$W$ 也可逆。
又 $E^*J=JE$，实系数幂级数给 $W^*J=JW$；$W$ 与 $I+E$ 交换。
因此

\[
 \boxed{\ Q_N^*JQ_N=J,\qquad Q_N^{-1}=JQ_N^*J.\ }
 \tag{4.3}
\]

这是准确、满射的 $J$-酉框架。它不是原 PDE 的准确传播，真实差仍须保留。
若实际只算 (4.2) 的有限段，其尾还须用几何级数支付。

在 $E_s\to E_{s+n}$ 的 $E^k$ 中，用一个因子取得增益，其余在输出档
使用 $r$。因为 $r\le1/2$，

\[
 \|W-I\|_{s\to s+n}
 \le\|E\|_{s\to s+n}
 \sum_{k\ge1}\left|{-1/2\choose k}\right|r^{k-1}
 \le2\|E\|_{s\to s+n}.
 \tag{4.4}
\]

由 $Q_N-C=-R_n+P_N(W-I)$，在上述表上

\[
 \boxed{\ \|Q_N-C:E_s\to E_{s+n}\|
          \le a+2(e^{1/10}+a)r.\ }
 \tag{4.5}
\]

所有量来自同一个实际 $\mathcal K$ 和有限系数表，没有背景幅度小性假设。

## 5. 一次、二次参数差量的有限表版本

先把实际族放在同一个固定 Hilbert 标尺。假设完整 $\mathcal K_p$ 已
验证两次可微，且整个参数区间内、全部所用中间档上

\[
 \|\partial_p^j\mathcal K_p(\xi):E_s\to E_{s+1-j}\|
       \le B_*\xi^{-1/2},\qquad j=0,1,2.
 \tag{5.1}
\]

允许每次参数导损一阶。R39 的同档传播门也须在同一参数区间一致成立。
置 $\alpha_*=2B_*\sqrt\delta$。准确 Duhamel 微分给

\[
 \|\partial_p C:E_s\to E_s\|\le e^{1/10}\alpha_*,
 \qquad
 \|\partial_p^2 C:E_s\to E_{s-1}\|
       \le e^{1/10}(\alpha_*+\alpha_*^2).
 \tag{5.2}
\]

一次导含一个 $\partial_p\mathcal K$；二次导含一个
$\partial_p^2\mathcal K$ 及两个有序的一次导因子。所有传播因子的区间
长度相加等于原长度，共同指数仍为 $e^{1/10}$。双一次导的项本来不损阶，
嵌入 $E_s\hookrightarrow E_{s-1}$ 即可。

对 (2.6) 的 $n=N+1$ 因子余项逐项微分，得到

\[
 \|\partial_p^jR_n:E_s\to E_{s+n-j}\|
 \le e^{1/10}\frac{\alpha_*^n}{n!}P_j(n,\alpha_*),
 \tag{5.3}
\]
\[
 P_0=1,\qquad P_1=n+\alpha_*,
 \qquad P_2=(n+\alpha_*)^2+\alpha_*.
 \tag{5.4}
\]

证明是有限乘积法则：一次导有 $n$ 个打在 $\mathcal K$ 的项和一个
打在末端 $C$ 的项；二次导的 $n$ 个二阶因子与 $n(n-1)$ 个双一次
因子给 $n^2$，再加 $2n\alpha_*$ 和 (5.2) 的
$\alpha_*+\alpha_*^2$。有序积分仍由 (2.5) 控制；所用所有输入档按
实际导数损失放进有限表。没有无限阶微分或未计的未来阶数。

若实际圆长、root coordinate、source height 或 frame 随 $p$ 变，
必须先验证它们对 (5.1) 的真实贡献，不能只对 $V$ 求导后称作几何导数。
源的参数版对 (3.1) 同样微分，并另付准确 $\Gamma_f$ 的 jet；本节
没有免费给出那个输入。

## 6. 后续边界

现在已提供可计算的全频有限 root 传播近似、任意预定有限强余项、
ordinary source 与真通量修正。还须对同一对象完成正侧有限 Ai
试解与完整 DN 的比较、所有端口的共同 Gram、严格负区实际相位与
低阶符号，以及全网络的有限低块和高频反馈。

R40 假设的是已验证的完整标量符号；并非任意有三阶平滑误差的近似
都自动具有该符号。本文 Airy 积分仍须继续分析才能识别那些实际系数。
固定握持帽和精确非线性迭代也仍须实付。
