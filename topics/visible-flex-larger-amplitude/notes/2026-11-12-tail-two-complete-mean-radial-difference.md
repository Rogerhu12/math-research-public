# 两个完整 mean 根的径向导数差与连续二阶高度预算

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）
日期：2026-11-12

**状态：完整条件证明；没有新增数值执行或外侧存在性结论。**
本工具接
[两个完整 mean 根的有理差界](2026-11-12-tail-two-complete-mean-roots-rational-difference.md)
及 [carrier 几何接口](2026-11-12-tail-carrier-mean-and-geometric-interface.md)。
它只消费相同真实背景上的两组实际候选高度和各自完整 mean 根；
不改变候选，不补造 PDE 解，不要求中间插值状态也满足 mean 方程。
这里的差界是实全角界；任何复角条带或空间曲面误差仍须另外支付。

## 1. 准确状态、根和径向正则性

沿一个真实物理径向区间，设 $r>0$、$w(r)>0$，$w$ 为 $C^1$。
两组非均值高度 $h_i^\perp(r,\theta)$ 至少关于 $r$ 为 $C^2$，
关于 $\theta$ 足够光滑以交换本节出现的导数。当前有限 Fourier 候选满足
后一要求。置

$$
 z=w^2,\quad E=1+z,\quad
 P_i=\frac{\partial_\theta h_i^\perp}{rw},\quad
 T_i=\partial_\theta P_i,\quad
 \overline K_i=\frac{\partial_r h_i^\perp}{w},\quad
 K_i=c_i+\overline K_i,\quad Y_i=1+K_i.
 \tag{MR.1}
$$

这里完整高度的径向导数为 $h_{i,r}=w(1+K_i)$，完整 mean 只加一次。
定义

$$
 A=1-zP^2,\qquad D=E-zY^2-EzP^2,\qquad L=Y+ET,
$$

$$
 \Gamma=\frac{1+zYT/A}{\sqrt D},\qquad
 \mathcal M=\frac{\langle\Gamma\rangle-1}{z}.
 \tag{MR.2}
$$

根 $c_i(r)$ 是 $\mathcal M(c_i,\overline K_i,P_i,T_i)=0$ 的完整真实角平均根。
假设整区间两端状态都有
$A_i\ge a_*>0,D_i\ge d_*>0,L_i\ge l_*>0$。
已付的 R64 端符号与严格单调性确定该允许分支；本工具不使用近似根值替代它。
由于 $\mathcal M_c=\langle LD^{-3/2}\rangle>0$，
隐函数定理给 $c_i\in C^1$。论证在每个原光滑片内成立，
兼容端点则取同一实际单侧极限。

令 $\delta X=X_B-X_A$。此前完整状态线段的公式给
$A_t,D_t,L_t$ 的同一严格正下界。
不要求该线段上的中间状态为 mean 根。

## 2. 去掉假性的 $1/z$ 分母

记

$$
 d=Y^2-1+EP^2=2K+K^2+EP^2,\qquad
 e=d+zP^2,\qquad q=\sqrt D.
$$

由于 $D=1-zd$，有逐点准确恒等式

$$
 G:=\frac{\Gamma-1}{z}
  =\frac{YT}{Aq}+\frac{d}{q(1+q)},\qquad
 \mathcal M=\langle G\rangle .
 \tag{MR.3}
$$

这使用 $1-q=zd/(1+q)$，没有将两个近一数作数值相减。
关于 $(K,P,T)$ 的偏导仍是

$$
 B_K=\frac{L}{D^{3/2}},\qquad
 B_T=\frac{Y}{A\sqrt D},\qquad
 B_P=\frac{EP(1+zYT/A)}{D^{3/2}}
       +\frac{2zPYT}{A^2\sqrt D}.
 \tag{MR.4}
$$

关于 $z$ 的偏导保持 $K,P,T$ 不变。此时
$A_z=-P^2,d_z=P^2,D_z=-e,q_z=-e/(2q)$，故

$$
 G_z=
 \frac{YT\,P^2}{A^2q}
 +\frac{YT\,e}{2Aq^3}
 +\frac{P^2}{q(1+q)}
 +\frac{de(1+2q)}{2q^3(1+q)^2}.
 \tag{MR.5}
$$

该式没有 $1/z$ 或 $1/w$ 的额外奇性。
它是完整 integrand 的偏导，不是先平均后将非零项删掉所得的近似式。

## 3. 完整径向隐微分

令 $\alpha=1/r+w_r/w$。从 (MR.1) 的实际高度导数直接得到

$$
 P_r=\frac{\overline K_\theta}{r}-\alpha P,\qquad
 T_r=\frac{\overline K_{\theta\theta}}{r}-\alpha T,\qquad z_r=2ww_r.
 \tag{MR.6}
$$

因为 $\overline K_r$ 和 $T_r$ 角均值均为零，
对完整根方程求径向导数后可准确写成

$$
 \mathcal A_i\,c_{i,r}+\mathcal F_i=0,\qquad
 \mathcal A_i=\langle B_{K,i}\rangle,
$$

$$
 \mathcal F_i=
 \left\langle
 (B_{K,i}-1)\overline K_{i,r}
 +B_{P,i}P_{i,r}
 +(B_{T,i}-1)T_{i,r}
 +(G_z)_i z_r
 \right\rangle .
 \tag{MR.7}
$$

没有使用真实 Darboux 方程来替换候选的二阶导数。
式 (MR.6) 是兼容高度自身导数的恒等式；
$\overline K_r$ 必须来自实际候选，不能另取 PDE 给出的值。

相减给出

$$
 \mathcal A_B\,\delta c_r
 =-\delta\mathcal F-\delta\mathcal A\,c_{A,r}.
 \tag{MR.8}
$$

交换 $A,B$ 也成立。因此可以在最后一项使用两侧已付
$|c_{i,r}|$ 上界的较小者，但不能直接假设 $\delta c_r=0$。

## 4. 全为有理运算的系数差

下面所有数都是同一整叶上的非负上界。取

$$
 z\le z_*,\quad E_*=1+z_*,\quad
 |K_i|\le k,\quad |P_i|\le p,\quad |T_i|\le t,\quad
 d_0=\min(1,d_*).
$$

由已付完整根差及非均值场差，取

$$
 |\delta K|\le e_K:=|\delta c|_{\rm ub}
          +\|\delta\overline K\|_\infty,\qquad
 |\delta P|\le e_P,\qquad |\delta T|\le e_T.
 \tag{MR.9}
$$

置以下幅度与差：

$$
\begin{aligned}
 Y_*&=1+k,& \Delta Y&=e_K,\\
 U_*&=Y_*t,& \Delta U&=t e_K+Y_*e_T,\\
 d_*^{\,a}&=2k+k^2+E_*p^2,&
 \Delta d&=2Y_*e_K+2E_*p e_P,\\
 e_*^{\,a}&=d_*^{\,a}+z_*p^2,&
 \Delta e&=\Delta d+2z_*p e_P,\\
 \Delta A&=2z_*p e_P,&
 \Delta D&=z_*\Delta d,\\
 L_*&=Y_*+E_*t,&
 \Delta L&=e_K+E_*e_T.
\end{aligned}
\tag{MR.10}
$$

$d_*^{\,a},e_*^{\,a}$ 是 $|d|,|e|$ 的幅度上界，与正域下界 $d_*$
不同。上述差由同一 $z$ 下准确相减而来；
没有把共同真实 $w$ 当成两次独立扰动。

使用成对记号 $(M,\Delta)$ 表示两侧绝对值均不超过 $M$、
同一函数的差不超过 $\Delta$。可取

$$
\begin{array}{c|c|c}
\text{因子}&M&\Delta\\ \hline
A^{-1}&a_*^{-1}&\Delta A/a_*^2\\
A^{-2}&a_*^{-2}&2\Delta A/a_*^3\\
F_1=D^{-1/2}&d_0^{-1}&\Delta D/(2d_0^2)\\
F_3=D^{-3/2}&d_0^{-2}&3\Delta D/(2d_0^3)\\
J=(1+\sqrt D)^{-1}&j=(1+d_0)^{-1}&j^2\Delta D/(2d_0)\\
B=2J-J^2&2j-j^2&j^2\Delta D/d_0
\end{array}
\tag{MR.11}
$$

证明只需正函数的均值定理及 $0<d_0\le1$。
特别地 $\sqrt D\ge\sqrt{d_0}\ge d_0$，
$|(\sqrt D)_B-(\sqrt D)_A|\le\Delta D/(2d_0)$。
$J\in(0,j]$，故 $|B|\le2j-j^2$、$|\delta B|\le2|\delta J|$。
所有根式的上下界最终均以安全整数幂替代。

对任意有限因子组，定义正的乘积差算子

$$
 \mathfrak D((M_1,\Delta_1),\ldots,(M_n,\Delta_n))
 =\sum_{i=1}^n\Delta_i\prod_{j\ne i}M_j .
 \tag{MR.12}
$$

逐项望远镜展开证明它包围乘积差，允许各实际因子有符号，
也不要求它们独立。

取 $P_*=(p,e_P)$、$P^2_*=(p^2,2pe_P)$，
$Y_*=(Y_*,e_K)$、$U_*=(U_*,\Delta U)$，
$d_*^{a}=(d_*^{a},\Delta d)$、$e_*^{a}=(e_*^{a},\Delta e)$。
另外

$$
 N_*=\left(1+\frac{z_*U_*}{a_*},
 z_*\left(\frac{\Delta U}{a_*}+\frac{U_*\Delta A}{a_*^2}\right)\right)
 \tag{MR.13}
$$

包围 $N=1+zYT/A$ 的幅度和差。
在不致混淆时，以下公式内的符号表示其对应成对数据：

$$
\begin{aligned}
 \Delta B_K&=\mathfrak D(L,F_3),\\
 \Delta B_T&=\mathfrak D(Y,A^{-1},F_1),\\
 \Delta B_P&=E_*\mathfrak D(P,N,F_3)
          +2z_*\mathfrak D(P,U,A^{-2},F_1),\\
 \Delta G_z&=\mathfrak D(U,P^2,A^{-2},F_1)
       +\tfrac12\mathfrak D(U,e,A^{-1},F_3)\\
 &\quad+\mathfrak D(P^2,F_1,J)
       +\tfrac12\mathfrak D(d,e,F_3,B).
\end{aligned}
\tag{MR.14}
$$

最后一式使用准确恒等式
$(1+2q)/(1+q)^2=2J-J^2$，因此没有省去 (MR.5) 的第四项。

## 5. 显式 $c_r$ 差界

从前一证明的 (M.12) 取已付
$|B_K-1|\le C_K,|B_P|\le C_P,|B_T-1|\le C_T$。
设

$$
\begin{aligned}
 \|\overline K_{i,r}\|_\infty&\le R_K,&
 \|\delta\overline K_r\|_\infty&\le e_{Kr},\\
 \|P_{i,r}\|_\infty&\le R_P,&
 \|\delta P_r\|_\infty&\le e_{Pr},\\
 \|T_{i,r}\|_\infty&\le R_T,&
 \|\delta T_r\|_\infty&\le e_{Tr},\\
 |z_r|&\le Z_r.
\end{aligned}
$$

这些量从已有 $\overline K,\overline K_r,H$ 的完整 Fourier 系数及
(MR.6) 计算。例如
$R_P\le\|\overline K_\theta\|_\infty/r_{\min}+\alpha_{\max}p$，
$e_{Tr}\le\|\delta\overline K_{\theta\theta}\|_\infty/r_{\min}
+\alpha_{\max}e_T$，其中
$\alpha_{\max}=1/r_{\min}+\|w_r/w\|_\infty$；
$Z_r\le2w_{\max}|w_r|_{\max}$。
全部 $m,m^2$ 乘子均实际计入，不能由有限角采样代替。

令

$$
\begin{aligned}
 E_F={}&\Delta B_K R_K+C_K e_{Kr}
       +\Delta B_P R_P+C_P e_{Pr}\\
      &+\Delta B_T R_T+C_T e_{Tr}+Z_r\Delta G_z,\\
 C'_0={}&\min(C'_{A},C'_{B}),
\end{aligned}
$$

其中 $C'_i$ 是原完整候选已付的 $|c_{i,r}|$ 上界。
由 (MR.8) 与 $\mathcal A_i\ge l_*/E_*^2$ 得

$$
 \boxed{
 |\delta c_r|
 \le \frac{E_*^2}{l_*}\bigl(E_F+\Delta B_K C'_0\bigr).
 }
 \tag{MR.15}
$$

可再与 $C'_A+C'_B$ 取较小者，因为它们控制的是同一实际根导数差。
两侧的 $c_r$ 原始实际证明仍需保留，不能用该比较公式代替其存在性。

## 6. 完整高度二阶差和端点兼容

用同一真实 $w,w_r$，准确地

$$
\begin{aligned}
 \delta h_r&=w(\delta c+\delta\overline K),\\
 \delta h_{rr}&=w_r(\delta c+\delta\overline K)
                 +w(\delta c_r+\delta\overline K_r),\\
 \delta h_{r\theta}&=w\,\delta\overline K_\theta .
\end{aligned}
\tag{MR.16}
$$

因此 (MR.15) 直接替换原先粗的 $C'_A+C'_B$ 项，得到连续真实
$h_{rr}$ 的比较；其余非均值 $h,h_\theta,h_{\theta\theta}$ 直接消费
全部实际 Fourier 系数。完整 mean 高度只按

$$
 \delta h_0(r)-\delta h_0(r_L)=\int_{r_L}^r w(s)\delta c(s)\,ds
 \tag{MR.17}
$$

累积，并复用已付正质量 $I_{00}+I_{01}=\int w\,dr$。
不得在内部节点重置常数或省去最终延续到后续未改片的同一高度偏移。

若两候选的非均值物理两 jet 在一个共端点准确相同，
同一完整 mean 分支的唯一性先给 $\delta c=0$；
(MR.6)--(MR.8) 再给 $\delta c_r=0$。
选择一个共同 mean 高度常数后，完整物理两 jet 因而兼容。
该端点结论来自实际高度与根唯一性，不依赖任何有限差分样本。

本工具支付的是候选间实高度 $C^2$ 差。
要将它变成真实曲面的曲率、reach、held 位移或全时几何结论，
仍须支付真实外解误差、水平展开及全域嵌入接口；
不能仅由候选 Darboux 残差有限或正域门通过就宣称存在该空间曲面。
