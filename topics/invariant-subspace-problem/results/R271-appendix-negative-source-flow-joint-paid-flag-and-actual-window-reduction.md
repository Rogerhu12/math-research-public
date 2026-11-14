# R271 附录：真正负源图中的联合旗支付与全部合法窗口的同源归约

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2220。

状态：**已证明。** 一次真正向下左源流的像带有准确的首头负配对。本文将它与已经支付的深 jets / 单高块联合旗结合：在两者的交上，左费用不超过指数小的常数乘两费用；沿这个交作真正的两费用正交投影，同时保留源流像条件与两费用收缩。最后从同一个原顶部最小前驱出发，构造全部较低合法窗口的来源，支付真实缺陷向量的同一强极限及全部窗数。

所得余源同时满足负源图条件与联合旗的准确度量正交条件。它们不被宣称具有坐标支撑消失，也不被宣称仍共同组成一个逐孔源流。剩余的二次型比较仍未证明，本文不据此断言边界 $N=M$ 或普通 ISP 已解决。

依赖：[准确左源流像](R271-appendix-exact-left-source-flow-range-and-minimal-upward-extension.md)、[同源截断及完整未来窗预算](R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)、[深 jets 与单高块联合源旗](R239-appendix-joint-deep-strip-flag-and-same-flat-middle-transfer.md)及[实际源与合法窗口预算](R271-appendix-actual-source-two-form-ratios-and-legal-window-summation-threshold.md)。

## 1. 同一个原孔层的三个度量

固定原 $m\ge8$、$d=2^m$ 与合法孔层 $4d\le p\le e^{d^3/4}$。在原源空间
\[
\mathscr R_p=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,p}
\]
上省略下标 $p$，记
\[
L=J_{\rm left}^{-1},\qquad B=J_{\rm bare}^{-1},\qquad
G=J_{\rm right},\qquad \mathfrak M=B+LGL.
\tag{1.1}
\]
全部是原真正最小原像的度量，在每组固定参数下有界严格正。对应费用为
\[
\mu(r)^2=\langle Lr,r\rangle,\quad
\alpha(r)^2=\langle Br,r\rangle,\quad
\lambda(r)^2=\langle G^{-1}r,r\rangle,
\]
\[
\lambda_{\rm flat}(r)^2=\langle GLr,Lr\rangle,\qquad
\chi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2
=\langle\mathfrak Mr,r\rangle.
\tag{1.2}
\]
$\mathfrak M$ 是源上的正度量，不是原不变核空间 $M$。

令 $\iota_0:E_{d-1,p}\to\mathscr R_p$ 为首源头嵌入，
$P=\iota_0\iota_0^*$、$Q=I-P$。原首头分裂给
\[
[P,B]=[P,G]=0,\qquad B|_{P\mathscr R_p}=K,\qquad
G|_{P\mathscr R_p}=K^{-1},
\tag{1.3}
\]
其中
\[
K=\left((D:\mathcal H_{p+1}\to\mathcal H_p)^\dagger
\bigm|_{E_{d-1,p}}\right)^*
\left((D:\mathcal H_{p+1}\to\mathcal H_p)^\dagger
\bigm|_{E_{d-1,p}}\right).
\]
它是真正完整层 MP 逆所给的度量。

准确源流稿证明
\[
\boxed{\mathscr N=\operatorname{Ran}T_{p+1}
=\ker\bigl[\iota_0^*(L+B)\bigr].}
\tag{1.4}
\]
本稿只在这个已证明的实际像上使用首头负号，不将一般源免费放进 $\mathscr N$。

## 2. 负源图上的三费用完整式

按首头与其余头写 $L=(L_{ij})$，置
\[
N_0=K+L_{00},\qquad
S^-=L_{11}-L_{10}N_0^{-1}L_{01}.
\]
每个 $r\in\mathscr N$ 唯一写为
\[
r=\mathcal R^-x=(-N_0^{-1}L_{01}x,x),\qquad x=Qr.
\tag{2.1}
\]
记 $r_0=\iota_0^*r$、$\kappa=\langle Kr_0,r_0\rangle$，以及
$B_1=B|_{Q\mathscr R_p}$、$G_1=G|_{Q\mathscr R_p}$。则
\[
PLr=-\iota_0Kr_0,\qquad QLr=S^-x,
\]
\[
\boxed{\begin{aligned}
\mu(r)^2&=\langle S^-x,x\rangle-\kappa,\\
\alpha(r)^2&=\kappa+\langle B_1x,x\rangle,\\
\lambda_{\rm flat}(r)^2&=\kappa+\langle G_1S^-x,S^-x\rangle,\\
\chi(r)^2&=2\kappa+\langle B_1x,x\rangle
+\langle G_1S^-x,S^-x\rangle.
\end{aligned}}
\tag{2.2}
\]
第一式是完整左 Schur 身份；后两式使用 (1.3)，没有删去 $L$ 的任何交叉块。特别
\[
\boxed{\mu(r)^2+\kappa
=\operatorname{Re}\langle QLr,Qr\rangle.}
\tag{2.3}
\]
右侧在此真实负图上为正。以下利用的是这个准确等号。

## 3. 联合已付旗与负图的交具有指数小左费用

沿联合旗稿，令
\[
\Gamma:\mathscr R_p\overset{\sim}{\longrightarrow}\mathscr U_p,
\qquad B_U=\Gamma^{-1},\qquad
\mu(r)^2=\langle\mathcal G\Gamma r,\Gamma r\rangle,\quad
\mathcal G\succeq I.
\]
首源头的像为
\[
\Delta=\Gamma(P\mathscr R_p)
=\bigoplus_{t=0}^{d-2}\mathbb C e_{t+1}\otimes K_{p-t}.
\]
可取任意该稿允许的 $K_{\rm block}=2^r$，$4\le K_{\rm block}\le d/4$。令 $\mathscr Y$ 为去重后的浅单高块条带与正交于 $\Delta$ 的深 jets 之和，具体为
\[
\mathscr Y=\mathscr A_{\rm sh}\oplus\mathscr D_\perp,\qquad
\mathscr Y\perp\Delta,\qquad
\mathscr X=\Gamma^{-1}(\Delta\oplus\mathscr Y).
\tag{3.1}
\]
以下证明对任意闭 $\mathscr Y\perp\Delta$ 及已支付的 (3.2) 都成立，并不依赖其坐标形状。这里选用已知联合旗，以给出无需新增估计的具体版本。该稿已经用原完整右旗的真实列支付
\[
\boxed{\lambda(Qr)\le\delta\|P_{\mathscr Y}\Gamma r\|
\le\delta\mu(r)\quad(r\in\mathscr X),}
\tag{3.2}
\]
\[
\delta^2\le e^{-8d^4}+e^{-d^4/10},\qquad
\delta\le\sqrt2e^{-d^4/20}.
\tag{3.3}
\]
这里两组右链的像没有被假设正交；$\delta$ 已保留正确的 Cauchy 平方和。

设
\[
\mathscr Z=\mathscr N\cap\mathscr X.
\]
对 $r\in\mathscr Z$，记
\[
\lambda_{{\rm flat},1}(r)^2
=\langle G_1QLr,QLr\rangle.
\]
由 (2.3)、$Q$ 对 $G$ 的约化、完整逆度量的 Cauchy 不等式与 (3.2)，
\[
\begin{aligned}
\mu(r)^2+\kappa
&\le \|G_1^{-1/2}Qr\|\,
     \|G_1^{1/2}QLr\|\\
&=\lambda(Qr)\lambda_{{\rm flat},1}(r)\\
&\le\delta\|P_{\mathscr Y}\Gamma r\|
          \lambda_{{\rm flat},1}(r)\\
&\le\delta\mu(r)\lambda_{{\rm flat},1}(r).
\end{aligned}
\tag{3.4}
\]
若 $\mu(r)=0$，严格正性给 $r=0$；否则可除以 $\mu(r)$。得到
\[
\boxed{\mu(r)\le\delta\lambda_{{\rm flat},1}(r)
\le\delta\chi(r),\qquad r\in\mathscr Z.}
\tag{3.5}
\]
这是在真正源流像上的加强。联合旗稿对一般 $r\in\mathscr X$ 的常数为 $(2-\delta^2)^{-1}$；这里的平方费用常数变为 $\delta^2$，原因正是首头配对的负号。

## 4. 完整闭子空间及保负图的真正投影

置 $S=L+B$，定义 $S$ 度量中投向首源头的正交投影
\[
\Pi_P^S=\iota_0N_0^{-1}\iota_0^*S,\qquad
\mathcal E_N=I-\Pi_P^S.
\tag{4.1}
\]
由 $\iota_0^*S\iota_0=N_0$，直接有
\[
\mathcal E_N^2=\mathcal E_N,\qquad
\operatorname{Ran}\mathcal E_N=\mathscr N,\qquad
\ker\mathcal E_N=P\mathscr R_p,\qquad Q\mathcal E_N=Q.
\tag{4.2}
\]
因为 $P\mathscr R_p\subset\mathscr X$，$\mathcal E_N$ 将 $\mathscr X$ 映到 $\mathscr Z$。定义
\[
\mathcal R_N:\mathscr Y\longrightarrow\mathscr R_p,\qquad
\mathcal R_Ny=\mathcal E_N B_Uy.
\tag{4.3}
\]
这个映射是 $\mathscr Y$ 到 $\mathscr Z$ 的有界同构，逆准确为
\[
\boxed{y=P_{\mathscr Y}\Gamma r\quad(r\in\mathscr Z).}
\tag{4.4}
\]
证明：$\mathcal E_N$ 只加减首头，因此
$P_{\mathscr Y}\Gamma\mathcal R_Ny=y$。反之，给定 $r\in\mathscr Z$，其 $\Gamma$ 坐标只有 $\Delta$ 和 $\mathscr Y$ 部分，$r-B_Uy$ 属于首头；施加 $\mathcal E_N$ 即得 $r=\mathcal R_Ny$。故像闭，且没有把低锚置零。

令
\[
H_N=\mathcal R_N^*\mathfrak M\mathcal R_N.
\]
由 $\mathcal G\succeq I$、(4.4) 与 (3.5)，
\[
\|y\|\le\mu(\mathcal R_Ny)\le
\delta\chi(\mathcal R_Ny),
\]
从而
\[
\boxed{H_N\succeq\delta^{-2}I_{\mathscr Y}.}
\tag{4.5}
\]
因此其逆确实有界。对任意 $r\in\mathscr N$，取真正的 $\mathfrak M$ 正交投影
\[
s=P_{\mathscr Z}^{\mathfrak M}r
=\mathcal R_NH_N^{-1}\mathcal R_N^*\mathfrak Mr,
\qquad \widehat r=r-s.
\tag{4.6}
\]
则
\[
\boxed{\begin{gathered}
s,\widehat r\in\mathscr N,\qquad s\in\mathscr X,\\
\chi(r)^2=\chi(s)^2+\chi(\widehat r)^2,\\
\mu(s)\le\delta\chi(s)\le\delta\chi(r),\\
\|E_p^\dagger r-E_p^\dagger\widehat r\|
=\mu(s)\le\delta\chi(r).
\end{gathered}}
\tag{4.7}
\]
剩余空间准确为
\[
\boxed{\mathscr R_{\rm rem}
=\{r:\ \iota_0^*(L+B)r=0,\ 
\mathcal R_N^*\mathfrak Mr=0\}.}
\tag{4.8}
\]
所有交叉块都保留在 $\mathcal E_N,\mathcal R_N,H_N$ 与 $\mathfrak M$ 内。(4.8) 不等于物理 $Q$ 支撑，也不等于 $\Gamma r$ 在 $\mathscr Y$ 上为零，更不等于先前整个 $\mathscr X$ 的 $\mathfrak M$ 正交补。

若在 (4.8) 上另有 $\mu(u)^2\le C\chi(u)^2$，则由 (4.7)、三角不等式及二维 Cauchy，
\[
\mu(r)\le\delta\chi(s)+\sqrt C\,\chi(\widehat r)
\le\sqrt{\delta^2+C}\,\chi(r)
\quad(r\in\mathscr N).
\tag{4.9}
\]
这是准确的比较常数运输；尚未给出所需 $C$ 的上界。

## 5. 从一个真实顶部源进入负图：合法平移且保同一极限

先给不涉及原缺陷空间的一般事实。若 $5d\le q\le e^{d^3/4}$、
$v=E_q^\dagger r_q$，取 $p=q-d$，则 $p$ 合法、$p+d=q$。同源截断与源流像定理给
\[
r_p=Av_p,\qquad E_p^\dagger r_p=P_{\le p}^{(m)}v,\qquad
r_p\in\mathscr N_p.
\tag{5.1}
\]
完整未来窗的准确两投影预算给
\[
\boxed{\chi_p(r_p)^2\le
2\|P_{[p+1,q]}^{(m)}v\|^2.}
\tag{5.2}
\]
所以源进入负图是由同一个前驱的物理截断实现，未使用可能放大两费用的任意 $\mathcal E_N$ 投影。

对随 $m\to\infty$、$v_m\to w$ 的这种族，$p_m\ge4d_m$，原有限孔基完备性使
$P_{>p_m}^{(m)}w\to0$。于是
\[
E_{p_m}^\dagger r_{p_m}\to w,\qquad
\chi_{p_m}(r_{p_m})\to0.
\tag{5.3}
\]
再用 (4.6) 得 $\widehat r_{p_m}\in\mathscr R_{{\rm rem},p_m}$，并仍保 (5.3)。这一结论不要求先把未付的两费用归约运输过任意源投影。

## 6. 实际非零缺陷的全部窗口可同时支付

回到两个原边界之一，记 $M=\ker T$、$N=\overline{BM}$、
$W=M\ominus N$。假设 $0\ne w\in W$。这里的 $N$ 是原闭包空间，与本稿逐孔 $\mathscr N_p$ 不同。

对每个 $m$ 取
\[
Q_m=\left\lfloor e^{d^3/4}\right\rfloor,\qquad
I_m^-=\{4d,4d+1,\ldots,Q_m-d\},\qquad
|I_m^-|=Q_m-5d+1.
\tag{6.1}
\]
它不是在固定 $m$ 中令孔层趋于无穷；每个端点都在原合法有限窗口内。

原低投影与左零源核预算给一个真正顶部最小者 $u_m=E_{Q_m}^\dagger r_{Q_m}$，满足
\[
\boxed{\|u_m-P_{\le Q_m}^{(m)}w\|
\le\eta_m\|w\|,\qquad
\eta_m=e^{-74d^4}+e^{-75d^4}.}
\tag{6.2}
\]
具体地，先取 $v_m=P_{V_{m,Q_m}}w$，再取其同源真正左最小者；前一步误差至多 $e^{-74d^4}\|w\|$，第二步至多 $e^{-75d^4}\|w\|$。这些正是实际源预算稿 §3 的原估计。

令
\[
\tau_m=\|1_{\{\mathcal N_{\rm tot}>4d\}}w\|,\qquad
t_m=\tau_m/\|w\|\longrightarrow0,
\tag{6.3}
\]
其中 $\mathcal N_{\rm tot}$ 为原全部物理位孔数。尾孔数不超过总孔数，所以每个 $p\ge4d$ 都有
$\|P_{>p}^{(m)}w\|\le\tau_m$。

对同一个 $u_m$ 和每个 $p\in I_m^-$，定义
\[
r_p=A(u_m)_p,\qquad v_p=P_{\le p}^{(m)}u_m.
\]
由准确同源定理，
\[
v_p=E_p^\dagger r_p,\qquad r_p\in\mathscr N_p.
\tag{6.4}
\]
同时
\[
\mu_p(r_p)\ge
\left(\sqrt{1-t_m^2}-\eta_m\right)\|w\|.
\tag{6.5}
\]
全部未来窗来自这个同一个 $u_m$。每一孔层出现至多 $d$ 次，因此
\[
\boxed{\begin{aligned}
\sum_{p\in I_m^-}\chi_p(r_p)^2
&\le2d\,\|P_{[4d+1,Q_m]}^{(m)}u_m\|^2\\
&\le2d(\tau_m+\eta_m\|w\|)^2.
\end{aligned}}
\tag{6.6}
\]
还逐窗有 $\chi_p(r_p)\le\sqrt2(\tau_m+\eta_m\|w\|)$。因 (6.2) 已是一个顶部误差，(6.6) 对它只付真实窗口重叠数 $d$，没有额外遗漏指数多窗的 carry 项。

现在每个窗口选 $K_{\rm block}=d/4$ 的同一类联合旗，取 (4.6) 的
\[
\widehat r_p=r_p-P_{\mathscr Z_p}^{\mathfrak M_p}r_p
\in\mathscr R_{{\rm rem},p}.
\]
(4.7) 逐项保持两费用不增，所以
\[
\boxed{\sum_{p\in I_m^-}\chi_p(\widehat r_p)^2
\le2d(\tau_m+\eta_m\|w\|)^2.}
\tag{6.7}
\]
取 (3.3) 中对全部这些窗口有效的 $\delta_m$。由 (6.5) 与逐窗改变量，
\[
\boxed{\mu_p(\widehat r_p)\ge\vartheta_m\|w\|,\quad
\vartheta_m=\sqrt{1-t_m^2}-\eta_m
-\sqrt2\delta_m(t_m+\eta_m)\longrightarrow1.}
\tag{6.8}
\]
更强地，真正左最小前驱的同一极限是对窗口一致的：
\[
\boxed{\sup_{p\in I_m^-}
\|E_p^\dagger\widehat r_p-w\|
\le(1+\sqrt2\delta_m)(\tau_m+\eta_m\|w\|)
\longrightarrow0.}
\tag{6.9}
\]
这里先得到同源族 $r_p$，然后逐窗投影。没有声称投影后的 $\widehat r_p$ 之间仍满足 $T_{p+1}\widehat r_{p+1}=\widehat r_p$；(6.7) 只需逐窗度量收缩，(6.8)–(6.9) 只需已经付清的左改变量。

## 7. 剩余比较只需在同时两种图条件的实际族上支付

充分大 $m$ 时 $\vartheta_m>0$，故每个 $\widehat r_p$ 非零且
$\chi_p(\widehat r_p)>0$。定义真实余源比例
\[
C_{m,p}^{\rm rem}(w)
=\frac{\mu_p(\widehat r_p)^2}{\chi_p(\widehat r_p)^2}>0.
\tag{7.1}
\]
由 (6.7)–(6.8)，准确有
\[
\boxed{\frac1d\sum_{p\in I_m^-}
\frac1{C_{m,p}^{\rm rem}(w)}
\le \frac{2(t_m+\eta_m)^2}{\vartheta_m^2}
\longrightarrow0.}
\tag{7.2}
\]
因此若仅在这个实际余源族上证明上界
$C_{m,p}^{\rm rem}(w)\le C_{m,p}(w)$，并在一条趋于无穷的头子序列上有
\[
\limsup\frac1d\sum_{p\in I_m^-}\frac1{C_{m,p}(w)}>0,
\tag{7.3}
\]
就排除了该非零 $w$。窗口子集版本同样成立。

特别，因为 $|I_m^-|\sim e^{d^3/4}$，只需沿同一头子序列付
\[
\boxed{\sup_{p\in I_m^-}C_{m,p}^{\rm rem}(w)
=O\!\left(\frac{e^{d^3/4}}d\right)}
\tag{7.4}
\]
即可矛盾。这个常数目标与先前合法窗口预算同阶，但现在比较对象已严格缩到 (4.8) 的同时两种图条件及 (6.4)–(6.9) 支付的同一物理缺陷来源。

若 (7.3) 对每个假定非零 $w\in W$ 都能支付，则 $W=0$、$N=M$。本文尚未证明 (7.3) 或 (7.4)。自由中段 Schur 回馈、多高位原头耦合、完整高修复和全部实际源交叉块仍是剩余量；(4.8) 不许可把这些项当坐标零。普通可分无穷维复 Hilbert ISP 的完成标准保持不变。


## 8. 完整右费和保持原 primitive 增量的一层运输

以下仍保 §§1–4 的同一个原负图与已付旗，记 $\beta=\delta^2$。本节不给上层新的平坦费用或再次负图条件；它支付完整右最小费，以及同一条源流连接的一层真实左运输。

### 8.1 完整右费与总左右费的准确上界

对 $r\in\mathscr Z$，令 $\ell=\lambda_{{\rm flat},1}(r)$。原 (3.4) 是
\[
\mu(r)^2+\kappa\le\delta\mu(r)\ell.
\tag{8.1}
\]
配方直接给
\[
0\le\kappa\le\delta\mu(r)\ell-\mu(r)^2
\le\frac{\beta}{4}\ell^2,\qquad
\mu(r)^2\le\beta\ell^2.
\tag{8.2}
\]
由共同首头分裂及已付旗条件，
\[
\lambda(r)^2=\kappa+\lambda(Qr)^2,\qquad
\lambda(Qr)^2\le\beta\mu(r)^2.
\]
所以
\[
\boxed{\lambda(r)^2
\le\left(\frac{\beta}{4}+\beta^2\right)\ell^2
\le\left(\frac{\beta}{4}+\beta^2\right)\chi(r)^2.}
\tag{8.3}
\]
对总左右费用，直接使用 (8.1) 比分别相加更强：
\[
\begin{aligned}
\mu(r)^2+\lambda(r)^2
&=\mu(r)^2+\kappa+\lambda(Qr)^2\\
&\le\delta\mu(r)\ell+\beta\mu(r)^2\\
&\le\beta(1+\beta)\ell^2.
\end{aligned}
\]
因此
\[
\boxed{\mu(r)^2+\lambda(r)^2
\le c_\beta\chi(r)^2,\qquad c_\beta=\beta(1+\beta).}
\tag{8.4}
\]

这里没有使用 $\alpha(Qr)\ge\lambda(Qr)$。原裸链只解低输出方程，可能还有待修复的高返回；完整右链的低投影才给裸可行者，所以实际方向是 $\alpha\le\lambda$。本节所需信息只有 (8.1)、完整首头分裂及 (3.2)，不把这两个可行集错误地反向包含。

### 8.2 准确紧支撑零源向量

将真正完整右最小链 $F_p^\dagger r$ 嵌入原物理带 $[p+1,p+d]$，定义
\[
k_p(r)=E_p^\dagger r-F_p^\dagger r.
\]
同源两条链的唯一源互相抵消，故
\[
(A_m+D_m)k_p(r)=0,\qquad
\operatorname{supp}_{\rm holes}k_p(r)\subseteq[0,p+d].
\]
左右物理支撑正交，所以由 (8.4)，
\[
\boxed{\|k_p(r)\|^2
=\mu(r)^2+\lambda(r)^2
\le c_\beta\chi(r)^2\quad(r\in\mathscr Z).}
\tag{8.5}
\]
这是原有限头加正规尾模型的准确零源向量；未把它不经 carry 处理就当作实际边界 $T_N/T_Y$ 的零源向量。

### 8.3 保同一个原 primitive 增量的真实一层运输

令
\[
\mathcal D_{p+1}=D|_{\mathscr X_{p+1}},\qquad
\mathcal U_p=-A_m\mathcal D_{p+1}^\dagger.
\]
源流像稿给每条实际纤维
\[
t_{\rm up}=\mathcal U_pr+A_mg,\qquad
g\in\bigoplus_{i=1}^{d-1}e_iK_{p+1}^{\rm prim},
\]
及真正最小前驱的准确拼合
\[
E_{p+1}^\dagger t_{\rm up}
=E_p^\dagger r\ \oplus\
(-\mathcal D_{p+1}^\dagger r+g).
\tag{8.6}
\]
对任意源 $s$，完整右链的首段必须经 $D$ 映到 $s$，因此完整 MP 的最小性给
\[
\|\mathcal D_{p+1}^\dagger s\|
\le\|F_p^\dagger s\|=\lambda(s).
\tag{8.7}
\]
全部受限旗已经由源流像稿证明保持；没有替换为顺次幂逆。

现在对一个真实 $r\in\mathscr N_p$ 作 (4.6)：
$r=s+\widehat r$，$s\in\mathscr Z_p$。从某个给定的上层源
$t_{\rm up}=\mathcal U_pr+A_mg$ 出发，保持其同一个 $g$，定义
\[
\widehat t_{\rm up}=\mathcal U_p\widehat r+A_mg.
\]
它仍是正确原纤维中的真实上层源，并有
\[
T_{p+1}\widehat t_{\rm up}=\widehat r.
\]
相减 (8.6)，用 (8.7)、(8.4) 及 $\chi(s)\le\chi(r)$，得到
\[
\boxed{\begin{aligned}
\|E_{p+1}^\dagger t_{\rm up}
 -E_{p+1}^\dagger\widehat t_{\rm up}\|^2
&=\mu_p(s)^2+\|\mathcal D_{p+1}^\dagger s\|^2\\
&\le\mu_p(s)^2+\lambda_p(s)^2\\
&\le c_\beta\chi_p(s)^2
\le c_\beta\chi_p(r)^2.
\end{aligned}}
\tag{8.8}
\]
因此联合旗删除不仅保留本层负图和两费用，还能沿同一个实际 primitive 增量向上运输一层，左向量改变量的常数仍指数小。

$\widehat t_{\rm up}$ 不被宣称属于下一负图 $\mathscr N_{p+1}$；它自己的 $\chi_{p+1}$ 也未由 (8.8) 控制。故 (8.8) 不能无条件迭代为整条已归约源流。原剩余比较、自由中段和高修复仍未闭合。
