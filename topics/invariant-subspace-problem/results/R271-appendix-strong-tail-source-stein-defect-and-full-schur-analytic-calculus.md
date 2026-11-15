# R271 附录：强位联块真实源的 Stein 缺陷与完整 Schur 解析演算

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。本文在强物理尾位并头后的同一个完整源上，证明
$$
\|C_{\mathrm s}^k\|_{L+B},\
\|C_{\mathrm s}^k\|_{L+G^{-1}}
\le \sqrt{k+1}\,\|D_>\|^k.
$$
这是真正先消左零源、保留完整／裸右链后的两种源度量；不使用头 Jordan 条件数，不删高返回，不要求源来自某个指定 primitive。由此在远尾小于原逆芽半径时，原逆芽的完整 Taylor 多项式可以在这两个真实源 Schur 度量中作统一有界演算。

这里被控制的是新联块算子 $C=A_m+D_<$ 在源上的作用，**不是**原 $A_m$、$B_m$ 或孔次数交换子。因此它不与旧全源孔导数反例冲突，也没有证明同源 $\mu^2\le\kappa\Xi^2$ 或 $N=M$。

依赖：

- [强尾并头的真实源、完整自然域、全部高返回及同一顶部预算](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)。
- [原真实逆芽的半径、全部 Taylor 系数及非线性小量](../notes/2026-11-14-true-head-inverse-germ-twelve-half-radius-and-weighted-coefficients-789f-next.md)。

## 1. 同一个固定源和四个真实度量

固定前一附录中的 $m,R,n$，记
$$
C=A_m+D_<,\qquad C^h=0,\qquad h=d+R,\qquad D=D_>,
\qquad \delta=\|D\|>0.
$$
所有源、左右链和伴随均保原物理内积。简写
$$
\mathscr R=\mathscr R_n^C,\quad
U=(E_n^C)^\dagger,\quad L=U^*U,\quad
G=F_nF_n^*,\quad
B=(F_n^b(F_n^b)^*)^{-1}.
\tag{1.1}
$$
因此
$$
\mu(r)^2=\langle Lr,r\rangle,\qquad
\alpha(r)^2=\langle Br,r\rangle,\qquad
\lambda(r)^2=\langle G^{-1}r,r\rangle.
\tag{1.2}
$$
$F_n$ 的域是完整有限右链，$F_n^b$ 的域是准确裸链；从完整链到裸链的满射包括前稿 (4.2) 的全部高返回修复。固定 $m,R,n$ 时这两个源映射及 $E_n^C$ 都是到闭空间 $\mathscr R$ 的有界满射，所以 (1.1) 中各逆都是该完整固定源上的有界严格正算子。

置
$$
S_b=L+B,\qquad S_f=L+G^{-1}.
\tag{1.3}
$$
它们分别是同源左最小费用加完整裸费用、同源左最小费用加完整普通费用。特别，$S_b$ 不把裸商核当成物理真核；$S_f$ 不把高返回费用置零。

头算子 $C$ 保持左空间及其零源核，并与源映射交换：
$$
E_n^C(Cv)=C E_n^Cv.
$$
所以 $C$ 保持 $\mathscr R$。以下
$$
C_{\mathrm s}=C|_{\mathscr R}
\tag{1.4}
$$
是这个准确源算子，没有再压到一个不保持的源子空间。它满足 $C_{\mathrm s}^h=0$。

对正度量 $S$，记 $\|r\|_S^2=\langle Sr,r\rangle$，
$\|T\|_S=\|S^{1/2}TS^{-1/2}\|$。全文不把 $S$ 与 $C_{\mathrm s}$ 交换。

## 2. 两个右域上的真实收缩

设 $c=(c_1,\ldots,c_h)$ 是完整右链。其准确内部方程和末端为
$$
Cc_j=-Dc_{j+1}\quad(1\le j<h),\qquad Cc_h=0.
$$
于是
$$
\sum_{j=1}^h\|Cc_j\|^2
=\sum_{j=1}^{h-1}\|Dc_{j+1}\|^2
\le\delta^2\sum_{j=1}^h\|c_j\|^2.
\tag{2.1}
$$
逐头作用 $c\mapsto Cc$ 仍保持完整右域的全部头旗、尾旗和内部方程，而且
$F_n(Cc)=C_{\mathrm s}F_nc$。把 (2.1) 用于同源完整最小链，得到
$$
\lambda(C_{\mathrm s}r)\le\delta\lambda(r),
\qquad
C_{\mathrm s}^*G^{-1}C_{\mathrm s}\le\delta^2G^{-1}.
\tag{2.2}
$$

裸链 $b$ 的方程是
$$
Cb_j=-P_j^{\rm lo}Db_{j+1},\qquad Cb_h=0.
$$
$P_j^{\rm lo}$ 是尾物理正交投影，与头上的 $C$ 交换，故同样有
$$
\sum_j\|Cb_j\|^2\le\delta^2\sum_j\|b_j\|^2,
\qquad F_n^b(Cb)=C_{\mathrm s}F_n^bb.
$$
因此
$$
\alpha(C_{\mathrm s}r)\le\delta\alpha(r),
\qquad
C_{\mathrm s}^*BC_{\mathrm s}\le\delta^2B.
\tag{2.3}
$$
这是在完整右域和准确裸域内分别证明的收缩；没有由两个环境范数的夹逼交换某个压缩逆。

另外，两个源映射都取 $D$ 作用于第一段，所以
$$
\|F_n\|,\ \|F_n^b\|\le\delta.
$$
对任意同源候选链都有 $\|r\|\le\delta\|c\|$ 或 $\|r\|\le\delta\|b\|$。取真正最小者：
$$
\boxed{I_{\mathscr R}\le\delta^2B,\qquad
I_{\mathscr R}\le\delta^2G^{-1}.}
\tag{2.4}
$$
这里 $I_{\mathscr R}$ 使用源的原物理内积。

## 3. 左端精确缺陷与全部幂

令 $v=Ur$ 是左最小者，支撑在远孔 $0,\ldots,n$。把源 $r$ 注入第 $n$ 行，记这个等距注入为 $\iota_n$。左方程准确给
$$
Cv=-Dv+\iota_n r.
\tag{3.1}
$$
$Dv$ 支撑在 $0,\ldots,n-1$，故 (3.1) 的两项物理正交：
$$
\|Cv\|^2=\|Dv\|^2+\|r\|^2.
\tag{3.2}
$$
$Cv$ 是源 $C_{\mathrm s}r$ 的可行左向量。若 $P_{\mathscr K}$ 是同一左零源核 $\mathscr K_n^C$ 的物理正交投影，则真正最小者为
$$
UC_{\mathrm s}r=(I-P_{\mathscr K})CUr.
$$
所以还有精确正缺陷身份
$$
\boxed{
C_{\mathrm s}^*LC_{\mathrm s}
=I+U^*D^*DU
 -(P_{\mathscr K}CU)^*(P_{\mathscr K}CU).
}
\tag{3.3}
$$
特别
$$
C_{\mathrm s}^*LC_{\mathrm s}\le\delta^2L+I.
\tag{3.4}
$$
(3.3) 的最后一项完整保留；本文只在取上界时使用其正性。

合并 (2.3)、(2.4)、(3.4)，对 $k\ge0$ 归纳得到
$$
\boxed{
\begin{aligned}
\alpha(C_{\mathrm s}^kr)^2&\le\delta^{2k}\alpha(r)^2,\\
\mu(C_{\mathrm s}^kr)^2
&\le\delta^{2k}\bigl(\mu(r)^2+k\alpha(r)^2\bigr).
\end{aligned}}
\tag{3.5}
$$
第二式在 $k=0$ 是等式；由
$$
\mu(C_{\mathrm s}^{k+1}r)^2
\le\delta^2\mu(C_{\mathrm s}^kr)^2+\|C_{\mathrm s}^kr\|^2
\le\delta^2\mu(C_{\mathrm s}^kr)^2
   +\delta^2\alpha(C_{\mathrm s}^kr)^2
$$
即完成归纳。用 (2.2) 和 (2.4) 的另一式，完全同样得到
$$
\boxed{
\begin{aligned}
\lambda(C_{\mathrm s}^kr)^2&\le\delta^{2k}\lambda(r)^2,\\
\mu(C_{\mathrm s}^kr)^2
&\le\delta^{2k}\bigl(\mu(r)^2+k\lambda(r)^2\bigr).
\end{aligned}}
\tag{3.6}
$$
因而两个完整源 Schur 度量都有
$$
\boxed{
\|C_{\mathrm s}^k\|_{S_b}\le\sqrt{k+1}\,\delta^k,\qquad
\|C_{\mathrm s}^k\|_{S_f}\le\sqrt{k+1}\,\delta^k.
}
\tag{3.7}
$$
常数不依赖 $h,n,R$、头 Jordan 相似或任一高出生逆的条件数。各固定源上的有界性和全部最小化已经包含在 §1；(3.7) 没有宣称全孔直和上的 $D^\dagger$ 有界。

## 4. 完整解析演算和预解式

若 $f(z)=\sum_{k\ge0}f_kz^k$ 在半径 $r_0>\delta$ 的闭圆盘邻域解析，因 $C_{\mathrm s}^h=0$，准确代入是
$$
f(C_{\mathrm s})=\sum_{k=0}^{h-1}f_kC_{\mathrm s}^k.
\tag{4.1}
$$
对 $S=S_b$ 或 $S_f$，(3.7) 给
$$
\|f(C_{\mathrm s})\|_S
\le\sum_{k=0}^{h-1}|f_k|\sqrt{k+1}\,\delta^k.
\tag{4.2}
$$
若 $\sup_{|z|=r_0}|f(z)|\le M$，Cauchy 系数界和 Cauchy–Schwarz 给
$$
\sum_{k\ge0}\sqrt{k+1}\,t^k
\le
\left(\sum_{k\ge0}(k+1)t^k\right)^{1/2}
\left(\sum_{k\ge0}t^k\right)^{1/2}
=(1-t)^{-3/2}.
$$
故
$$
\boxed{
\|f(C_{\mathrm s})\|_S
\le\frac{M}{(1-\delta/r_0)^{3/2}}.
}
\tag{4.3}
$$
例如，对任意复数 $z$ 满足 $|z|>\delta$，
$$
\boxed{
\|(zI-C_{\mathrm s})^{-1}\|_S
\le\frac1{|z|}
 \left(1-\frac{\delta}{|z|}\right)^{-3/2}.
}
\tag{4.4}
$$
(4.4) 在同一个物理源和完整源 Schur 度量中成立。它不是原环境 $\Gamma$ 的孔导数界，也不以源消元前的低零核作反例或作上界。

## 5. 原逆芽在新真实 Schur 度量中的小误差

现在取原 $N/Y$ 任一真实头，$m\ge10$，并记
$$
d_0=e^{-20},\qquad
\rho_m=e^{-25d^3/2},\qquad
r_m=\frac{\rho_m}{2d_0},\qquad
\varepsilon_m=e^{-d^3/4}.
$$
已付逆芽 $\psi_m$ 满足
$$
\psi_m(0)=0,\quad \psi_m'(0)=d_0,\qquad
|\psi_m(z)-d_0z|
\le2d_0^2\varepsilon_m|z|
\quad(|z|\le r_m).
\tag{5.1}
$$
置解析函数
$$
f_m(z)=\frac{\psi_m(z)}{z},\qquad f_m(0)=d_0.
$$
本文在新 $C_{\mathrm s}^h=0$ 上使用的是 $f_m$ 的 Taylor 多项式截到 $h-1$ 次；当 $h>d$ 时，不能误用旧头上仅截到 $d-1$ 次的多项式。

假设 $\delta<\rho_m$，并置
$$
t=\frac{\delta}{r_m}=\frac{2d_0\delta}{\rho_m}<2d_0<\frac14.
$$
因为 $f_m-d_0$ 的常数项为零，(5.1) 的 Cauchy 界和 (4.2) 给
$$
\|f_m(C_{\mathrm s})-d_0I\|_S
\le2d_0^2\varepsilon_m
 \left((1-t)^{-3/2}-1\right).
\tag{5.2}
$$
为核最后的级数上界，令
$a_k=(3/2)_k/k!$。$a_0=1$ 且
$$
\left(\frac{a_{k+1}}{a_k}\right)^2
=\left(\frac{k+3/2}{k+1}\right)^2
\ge\frac{k+2}{k+1},
$$
故 $a_k\ge\sqrt{k+1}$，对 $k\ge1$ 求和即得 (5.2)。

又当 $0\le t\le1/4$ 时
$$
(1-t)^{-3/2}-1\le4t.
$$
定义
$$
H_C=d_0^{-1}f_m(C_{\mathrm s}),\qquad
\eta_m^{C}=16d_0^2\varepsilon_m\frac{\delta}{\rho_m}.
\tag{5.3}
$$
两个完整源度量同时满足
$$
\boxed{
\|H_C-I\|_{S_b}\le\eta_m^{C},\qquad
\|H_C-I\|_{S_f}\le\eta_m^{C}.
}
\tag{5.4}
$$
特别 $0<\eta_m^C<1/2$，而且
$$
\boxed{
(1-\eta_m^C)^2S
\le H_C^*SH_C
\le(1+\eta_m^C)^2S,\qquad
\|H_C^{-1}\|_S\le(1-\eta_m^C)^{-1}
}
\tag{5.5}
$$
对 $S_b,S_f$ 各自成立。所有乘积次序都是实际同源同余，没有把 $H_C$ 与 $S$ 当作交换。

前稿取 $R=\lceil c_0\rho_m^{-1}\rceil$、$c_0>1$ 时，
$\delta<\rho_m/c_0$，因此
$$
\eta_m^C\le\frac{16d_0^2}{c_0}e^{-d^3/4}.
\tag{5.6}
$$
这确实把原解析小量送进新联块的真实完整 Schur 度量；无需乘 $h$ 或头环境范数。

## 6. 真实负图的伴随作用及未付范围

令
$$
X_0=\mathscr R\cap(\ker C\otimes\mathcal H_n^>),\qquad
\mathscr N=\{r:\langle S_b r,z\rangle=0\ \text{对全部 }z\in X_0\}.
\tag{6.1}
$$
这是前稿同一实际源所在的准确负图。$C_{\mathrm s}z=0$，故
$H_Cz=z$ 对全部 $z\in X_0$ 成立。定义 $S_b$ 伴随
$$
H_C^{\dagger_b}=S_b^{-1}H_C^*S_b.
$$
那么
$$
\boxed{
H_C^{\dagger_b}\mathscr N\subseteq\mathscr N,\qquad
\|H_C^{\dagger_b}-I\|_{S_b}\le\eta_m^C.
}
\tag{6.2}
$$
第一式直接由
$\langle S_bH_C^{\dagger_b}r,z\rangle
=\langle S_br,H_Cz\rangle$
得到；第二式是 (5.4) 的同一 Hilbert 度量伴随。这里不把普通物理伴随冒充 $S_b$ 伴随，也不声称 $H_C$ 本身保 $\mathscr N$。

本文已付的量包括两个右收缩、左最小化的精确正缺陷、全部源的幂界、真实两种 Schur 度量上的解析与逆解析预算，以及 (6.2) 的准确负图作用。

仍未付的核心是
$$
\mu(r_n^C)^2
\le\kappa_m\bigl(\alpha(r_n^C)^2+
\langle GLr_n^C,Lr_n^C\rangle\bigr)
\tag{6.3}
$$
在同一个原 $w,u_Q$ 产生的源族上的所需量级。尤其：

- $C_{\mathrm s}=A_m+D_<$ 与原 $A_m$ 不同；从 (5.4) 不能删掉强位 $D_<$ 的非约化返回。
- $S_b$ 与 $S_f$ 分别受同一个 $H_C$ 控制，不等于二者已经相互可比；$G^{-1}-B$ 的高返回仍保留。
- (6.2) 的源范数近恒等不自动支付新的 flat 费，不能把它当成已有三费滤波或直接完成 (6.3)。
- 原并头窗口的量级仍是 $\kappa_mh/Q=O(1)$，不是旧 $d/Q$。本稿没有把一个解析半径直接改称该 $\kappa_m$。

这条结果把“远尾范数小”升级成了完整源 Schur 内的可证演算；下一步仍需处理左／右的同源比较及强块高返回。
