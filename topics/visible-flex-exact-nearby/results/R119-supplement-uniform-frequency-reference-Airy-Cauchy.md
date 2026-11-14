# R119 续篇：实际双转向负分量的无频率损失 Airy Cauchy 与连续源

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对实际径向参考的完整内部负型分量，在原来的
真实密度 Airy 两态中、任意两个内部截面之间，可以去掉前篇的
$\langle m\rangle^{5/3}$ 损失。一个刻意宽松但有限的共同界为
$$
 \boxed{\quad
 \|U_{0,m}(t,s)\|_{\ell^1(\mathbb C^2)}
 <K_j:=2^{5000}(j+4)^5\delta_j^{-10},
 \qquad m\in4\mathbb Z,\quad t,s\in I_{j,k}.
 \quad}                                                     \tag{F.1}
$$
两个转向端、两个完整 Cauchy 分量、mean 状态和普通连续源都保留。
因此它给同一个 Wiener 或 Sobolev 空间中的完整径向 propagator，
没有再借一次角宽吸收输入频率。这项改善付出了更大的、明确的
$\delta^{-10}$ 条件数；它本身尚不支付现有新尾的无限相对反馈。

## 1. 同一个实际状态，及本证明允许的参数范围

令 $I=[t_-,t_+]$ 是已安装的一个完整内部负型分量，
$Q=-A_{\Gamma^0}\ge0$，$q=\sqrt Q$，$\mu=w/a_{phys}$，
$M=1+|m|$。仍使用
$$
 \varrho_j=32(j+4)/\delta_j,\qquad
 \omega_m=(Q+\varrho_j^2M^{-2/3})^{1/2},
$$
$$
 X_m=\sqrt\mu
   \operatorname{diag}(\sqrt{\omega_m},\omega_m^{-1/2})(z_m,v_m)^T,
 \qquad
 \partial_t\begin{pmatrix}z\\v\end{pmatrix}=
 \begin{pmatrix}0&1\\Q&0\end{pmatrix}\partial_\theta\begin{pmatrix}z\\v\end{pmatrix}
            +\operatorname{diag}(0,1+Q)\begin{pmatrix}z\\v\end{pmatrix}.
 \tag{F.2}
$$
对非零模，$z_m=im h_m$、$v_m=(h_m)_t$。
不把 $\omega$ 或 $\mu$ 冻结为常数。

当前 first-shear64、末因子 $c_j\in[16,64]$ 的新尾满足本篇全部
门。证明实际上只使用如下明确的较宽包络：
$$
 \delta/4<|I|<4\delta,\quad Q\text{ 单峰},\quad Q(t_\pm)=0,
 \quad Q_{max}<2^{12}(j+4)\delta^{-3/2},
$$
$$
 |Q_t|<2^{18}(j+4)\delta^{-3},\qquad
 |Q_{tt}|<2^{26}(j+4)\delta^{-9/2},\qquad
 \mu(t_-)/\mu(t_+)<2^{272}\delta^{-2}.
 \tag{F.3}
$$
二阶导是分片 $L^\infty$ 导数；$Q_t$ 在接缝连续，故没有遗漏
delta source。所有 log 跳幅在 $j/2$ 与 $3(j+4)$ 之间；参数
bump 的实半径至多 $2^{-16}$，支集与转向点邻域不交。

这些是可直接由实际 profile 核对的门，并不假定任何尚未构造的新
profile。当前对象有更强的 $\mu$ 比例 $2^8\delta^{-2}$。
保留 (F.3) 的宽裕常数是为了使今后另选有限首剪切常数时，所需
门仍为明确的几何条件，而不是隐含在一个未知常数内。

具体地，$|S''|<6$、$|S'''|\le60$。参数 bump
$B(z)=64z^3(1-z)^3$ 满足 $|B'''|<2^{15}$，
$\psi(x)=B(8(x-1/4))$ 满足 $|\psi'''|<2^{24}$。
乘 $|\gamma|\le2^{-16}$ 及真实 $\sqrt{12}/\eta$ 的幂即得 (F.3)。
相邻较外胞元的较大 $\delta$ 只改善这些界。

## 2. 每个真实转向根的准确四次形状

转向点位于未被参数 bump 改动的上升 log-quintic 内。写
$$
 Q(s)=7-30B s^2(1-s)^2,\quad B=\sqrt{12}\,\Delta/\eta,
 \quad z=s_0(1-s_0)=\sqrt{7/(30B)}.
 \tag{F.4}
$$
当前全部层有 $0<z<2^{-20}$。令 $a=|Q_t(t_e)|$，并以向负区的
方向 $\varsigma=+1$（左根）或 $-1$（右根）定义
$$
 x=\varsigma a(t-t_e),\qquad
 d=\frac{z}{196(1-4z)}<2^{-10}.
$$
直接使用 $s-s_0=\varsigma\sqrt{12}x/(a\eta)$，得到准确多项式
$$
 \boxed{\quad
 Q(x)=x+(14d-1/28)x^2-dx^3-7d^2x^4.
 \quad}                                                     \tag{F.5}
$$
根到最近 quintic 接缝的 $x$ 距离至少 $14\sqrt{1-4z}>13$，
所以后文的完整 $|x|\le1$ 复盘位于同一个真实解析 germ，未穿过
只 $C^2$ 的径向接缝。两个根的同一公式来自各自的向内方向；没有把右根的 conormal
方向同左根混用。准确斜率公式是
$$
 a^2=10080\sqrt{12}\,\Delta\eta^{-3}(1-4z),
 \qquad
 \delta^{-9/4}<a<2^{16}\sqrt{j+4}\,\delta^{-9/4}.
 \tag{F.6}
$$
这里若根在相邻较外胞元，使用其真实 $\delta_e\le2\delta_j$；
斜率公式的固定前因子仍给显示的严格下界。

令 $Q(x)=x B_0(x)$，在完整复盘 $|x|\le1$ 上有
$|B_0-1|<1/16$。取在0处为1的解析平方根，并定义
$$
 J(x)=\frac32\int_0^1s^{1/2}\sqrt{B_0(sx)}ds,
 \quad R(x)=J(x)^{2/3},\quad \xi=xR(x),\quad g=\xi_x.
 \tag{F.7}
$$
这就是准确的 $\xi=(\frac32\int_0^x\sqrt{Q})^{2/3}$，包括根点。
完整复盘上 $|J-1|<1/16$、$|R-1|<1/16$。
Cauchy 在 $|x|\le1/2$ 给
$$
 |g-1|<1/8,\qquad |g_x|<1/2,\qquad |g_{xx}|<3.
 \tag{F.8}
$$
由于 $g$ 与1的距离小于1，直线积分证明 $\xi$ 在此盘单射。
边界上 $|\xi|>15/32$，所以其解析逆覆盖 $|\xi|\le1/4$。
本篇实际根 collar 取 $0\le\xi\le1/64$；其外端满足
$$
 Q\ge \frac{15}{17\cdot64}>1/128.
 \tag{F.9}
$$
单峰性因此使两根 collar 之外的整个中间严格段都满足 $Q>1/128$。

## 3. 真根上的完整 Liouville potential

先取 $y=\sqrt\mu\,h$。因为 $(\log\mu)_t=-1-Q$，原完整方程
准确成为
$$
 y_{tt}+\left[m^2Q+\frac{Q_t}{2}-\frac{(1+Q)^2}{4}\right]y=0.
 \tag{F.10}
$$
这里密度的两个导数均保留。转入 (F.5) 的 $x$，再令
$v=\sqrt g\,y$，得到
$$
 v_{\xi\xi}+[\kappa^2\xi+V(\xi)]v=0,\qquad \kappa=|m|/a,
$$
$$
 V=\frac{\varsigma Q_x/(2a)-(1+Q)^2/(4a^2)}{g^2}
           +\frac{3g_x^2}{4g^4}-\frac{g_{xx}}{2g^3}.
 \tag{F.11}
$$
由 (F.8)、$a>1$、$|Q|<1$、$|Q_x|<2$，完整复域
$|\xi|\le1/4$ 上有 $|V|<16$。
这是实际 full potential 的界，不是只从有限 root jets 外推。
右根的 $\varsigma$ 只改变已保留的一阶密度项的号。

## 4. 一个带两行的全频 Airy 估计

以下给出所用常数的自足推导。令 $F(x)$ 是
$u_{xx}+xu=0$ 的实基本矩阵，$F(0)=I$，$x\ge0$。
在 $[0,1]$ 上它及其逆的 Euclidean norm 小于2。
对 $x\ge1$，令
$$
 Z=\operatorname{diag}(x^{1/4},x^{-1/4})(u,u_x)^T,
 \qquad S=\begin{pmatrix}1&e(x)\\e(x)&1\end{pmatrix},
 \quad e(x)=1/(4x^{3/2}).
$$
准确有 $Z_x=(x^{1/2}J+(4x)^{-1}\operatorname{diag}(1,-1))Z$，
$J=(0,1;-1,0)$。因此
$$
 \frac d{dx}(Z^*SZ)=Z^*S_xZ,\qquad
 \int_1^\infty\frac{|e'|}{1-e}dx=\log(4/3).
 \tag{F.12}
$$
这同时控制高度和导数；不是从一个 height Green 升级成两行。
由 $\det F=1$，得到整个 $x\ge0$ 上
$$
 \|\operatorname{diag}((1+x)^{1/4},(1+x)^{-1/4})F(x)\|_2,
 \|[\operatorname{diag}((1+x)^{1/4},(1+x)^{-1/4})F(x)]^{-1}\|_2<6.
 \tag{F.13}
$$

对 $\kappa\ge1$，参考 $v_{\xi\xi}+(\kappa^2\xi+1)v=0$
经 $x=\kappa^{2/3}\xi+\kappa^{-4/3}$ 化为上述准确 Airy 方程。
取两行权
$$
 s_\kappa=(\kappa^2\xi+\kappa^{4/3}+1)^{1/2},\qquad
 Z_\kappa=\operatorname{diag}(\sqrt{s_\kappa},s_\kappa^{-1/2})(v,v_\xi)^T.
$$
其任意双向 propagator norm 小于36，更可用64。
真实 (F.11) 的差 $W=V-1$ 满足 $|W|<17$，在这一两行系统中
只有下左项 $-W/s_\kappa$，其 norm 至多 $17\kappa^{-2/3}$。
准确 interaction picture 的完整 Duhamel generator 故满足
$$
 \int_0^{1/64}\|B_{int}(\xi)\|d\xi
 <64^2\frac{17}{64}\kappa^{-2/3}\le1088.
$$
普通有限维 Gronwall 在同一个两行空间给
$$
 \boxed{\quad\|U_{root}(\xi,\eta)\|_2
                  <64e^{1088}<2^{2182}.\quad}
 \tag{F.14}
$$
没有因迭代次数重复支出任何角宽；此处所有矩阵都对每个真实频率
明确给出。大常数是固定的，与 $\delta,j,m$ 无关。

## 5. 严格负段的完整 wave potential 和频率分界

在 $Q>1/128$ 的中间段令 $ds=qdt$、$u=\sqrt q\,y$。
准确得到
$$
 u_{ss}+(m^2+V_w)u=0,
$$
$$
 V_w=\frac{Q_t}{2Q}-\frac{(1+Q)^2}{4Q}
              +\frac{5Q_t^2}{16Q^3}-\frac{Q_{tt}}{4Q^2}.
 \tag{F.15}
$$
这包括原密度的 potential，不能只保留 principal $m^2$。
(F.3)、$|I|<4\delta$ 和真实下界 $Q>1/128$ 逐项给
$$
 \int|V_w|ds
 \le\int_I\left[
 \frac{|Q_t|}{2\sqrt Q}+
 \frac{(1+Q)^2}{4\sqrt Q}+
 \frac{5Q_t^2}{16Q^{5/2}}+
 \frac{|Q_{tt}|}{4Q^{3/2}}\right]dt
 <2^{60}(j+4)^2\delta^{-5}.
 \tag{F.16}
$$
分片的 $Q_{tt}$ 在积分中保留，连续 $Q_t$ 保证没有隐藏端点项。

取准确频率分界
$$
 m_*=2^{64}(j+4)^2\delta^{-5}.
 \tag{F.17}
$$
若 $|m|\ge m_*$，wave 两态 $(mu,u_s)$ 的主部是 skew 矩阵，
其差项 norm 是 $|V_w|/|m|$。故 (F.16) 给双向 wave norm
$<e^{1/16}<2$。而 (F.6) 给 $\kappa=|m|/a>2^{12}$，
所以两侧实际根均合法使用 (F.14)。

## 6. 两端 raw 高度/flux 框架逐项付费

严格段中的两个变换并不只作用于高度。它们准确给
$$
 u=\sqrt q\sqrt\mu\,h,\qquad
 u_s=\frac{\sqrt\mu}{\sqrt q}
 \left[h_t+\left(\frac{(\log\mu)_t}{2}
                       +\frac{q_t}{2q}\right)h\right].
 \tag{F.18}
$$
在 $|m|\ge m_*$，(F.3)、$Q>1/128$ 给全部 shear 的无量纲
norm 小于1。又
$\varrho^2M^{-2/3}<2^{-32}$，所以 $\omega/q<2$。
严格 wave 两态与原 $X$ 的双向变换 norm 可安全取8。

根处令 $\omega_{nat}=g(\xi+\kappa^{-2/3})^{1/2}$。完整关系为
$$
 \varsigma a\,\frac{v_\xi}{\sqrt{\omega_\kappa}}
 =\frac{y_t}{\sqrt{\omega_{nat}}}
   +\frac{\varsigma a g_x}{2g\sqrt{\omega_{nat}}}y,
 \qquad \omega_\kappa=(\xi+\kappa^{-2/3})^{1/2}.
 \tag{F.19}
$$
原第二行则是
$(y_t-(\log\mu)_t y/2)/\sqrt\omega$。这把右根方向、密度 shear
和 $g_x$ 全部保留。由 $\kappa>2^{12}$、(F.8)，上述 shear norm
小于2；shifted Airy 的额外 $+1$ 也只需一个小于2的因子。

由 (F.6)，原平衡权与自然根权的比例在整个根 collar 上满足
$$
 1/2<\omega/\omega_{nat}
 <2^6(j+4)\delta^{-1/4}=:R_j.
 \tag{F.20}
$$
因此每次 root 两行变换及其逆可取 $16\sqrt{R_j}$。
在两个 collar 外端，$\xi=1/64$ 且 $\kappa>2^{12}$，自然根权
与实际严格 $q$ 权的比例小于2；没有再支付一个发散端点比。

任意两点之间最多穿过两根 collar 和一个严格段。即使对每个
collar 都重复采用安全的两个端点框架费，(F.14)、(F.18)--(F.20)
也给
$$
 \|U_{0,m}(t,s)\|_2
 <2^{4400}(j+4)^2\delta^{-1/2},\qquad |m|\ge m_*.
 \tag{F.21}
$$
这保留完整端口条件数；没有把单端 norm 当作双向 propagator。

## 7. 低频全部保留，最后消除频率损失

对于 $|m|<m_*$，重用前篇真正的辅助速度能量证明，而不是丢掉
这些模。将其密度比 $2^8\delta^{-2}$ 放宽到 (F.3)，同一完整
推导给
$$
 \|U_{0,m}(t,s)\|_1
 <2^{160}(j+4)\delta^{-1}M^{5/3}.
 \tag{F.22}
$$
其中辅助单峰因子只用
$|I|q_{max}<2^8\sqrt{j+4}\delta^{1/4}<1$，该式在129起的所有
层成立。$M<2m_*$，故准确得到
$$
 \|U_{0,m}(t,s)\|_1
 <2^{272}(j+4)^5\delta^{-28/3}
 <2^{272}(j+4)^5\delta^{-10}.
 \tag{F.23}
$$
结合 (F.21) 以及 Euclidean 到两分量和 norm 的费用即为 (F.1)。
这是真正的全频分界证明；没有用有限模式扫描覆盖未知高频。

特别 $m=0$ 的完整参考两态直接是
$$
 U_{0,0}(t,s)=\operatorname{diag}\left(
 \sqrt{\frac{\mu(t)\omega_0(t)}{\mu(s)\omega_0(s)}},
 \sqrt{\frac{\mu(s)\omega_0(s)}{\mu(t)\omega_0(t)}}\right).
 \tag{F.24}
$$
它包含原梯度框架在真实角 pullback 后可能出现的常数槽；不能
未经 weighted mean 条件就删掉第一行。真正 raw 高度的 mean
仍另外使用 $p_{h,0}$ 的 source 原函数和一个独立高度常数。

## 8. 同空间完整 propagator、源和权限

由于参考是径向的，(F.1) 直接给每个实 $s$、每个角宽 $r\ge0$
上的同空间界：
$$
 \|U_0(t,s_0)\|_{H^s\to H^s},\qquad
 \|U_0(t,s_0)\|_{\mathcal A_r^2\to\mathcal A_r^2}<K_j.
 \tag{F.25}
$$
对完整两行连续源 $G$，真实 Duhamel 公式及其强次序为
$$
 X(t)=U_0(t,s_0)X(s_0)+\int_{s_0}^tU_0(t,\tau)G(\tau)d\tau,
$$
$$
 \sum_m e^{r|m|}\sup_{t\in I}|X_m(t)|_1
 \le K_j\left[\|X(s_0)\|_{\mathcal A_r^2}
              +\sum_m e^{r|m|}\int_I|G_m(t)|_1dt\right].
 \tag{F.26}
$$
没有交换 $\sup$ 与 Fourier 和。L2 径向源另付真实
$\sqrt{|I|}<2\sqrt\delta$。例如原 raw 高度普通源准确进入
$G_1=0$、$G_2=\sqrt\mu\,aw e/\sqrt{\omega_m}$；实际射线共轭的
两个 correlated source 行则仍按原完整 source 合同输入，不能只
保留其差行。mean 的通量原函数及物理端点项亦不改变。

所有有限转向端的原两迹可准确恢复为
$$
 h_m=\frac{X_{m,1}}{im\sqrt\mu\sqrt{\omega_m}},\qquad
 p_{h,m}=\sqrt\mu\sqrt{\omega_m}\,X_{m,2},\quad m\ne0.
 \tag{F.27}
$$
这是 raw flux；grounded/normal 输出还须使用此前已付的真实
水平变化与 shear。式 (F.27) 没有删除任一端口分量。

(F.25) 允许在**已经证明同空间有界**的完整扰动 $B$ 上使用真正的
interaction picture；其充分费用是 $K_j^2\int_I\|B\|$。
本篇没有把原有宽差扰动自动升格为同宽算子，也没有支付所有
正型两端 DN 的全网络接合。尤其 $(F.1)$ 的 $\delta^{-10}$
与现新尾状态幂并不自动可和，需要下一项实际构造/条件数预算。

这里参数范围内的 propagator norm 一致，不表示对 $\Gamma$
微分仍无频率损失：真实主相位改变会产生 $m$ 因子。全部参数、
两射线 return 和最终固定度量选择仍须按实际 KAM/共轭合同处理。

[准确根多项式、Liouville 与两行预算程序](../scripts/fourfold_uniform_reference_Airy_Cauchy_20261113.py)
和 [完整报告](../notes/2026-11-13-R119-uniform-reference-Airy-Cauchy-budget.json)
核全部归一、potential、根/严格拼接、频率分界和明确常数。
