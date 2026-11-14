# R271 附录：真实好顶部的加权总度量与增长失真的相容源删除

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2220；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 从同一个实际顶部向量中选出一处两费用小的真实切口，再在一个加权总度量中作一次顶部投影，可以同时保留整条相容源流、全部已选切口的两费用预算和固定实际缺陷来源。允许顶部回缩常数满足 $C_m^2=O(e^{d^3/4}/d)$，不再只允许一致有界常数。

结合原低三维块联合回缩及线性失真优化，得到一个明确的实际应用：同一原配对前缀内，任意位置至多约 $m\sqrt{Q_m/d}/128$ 个完整三维块以及全部指定远尾出生，可以一同作为可付删除空间。没有把这些模式当成全部原源，也不把投影余条件写成坐标消失。实际余比较、无权 $N=M$ 与普通 ISP 仍为 OPEN。

依赖：[同源截断与未来带](R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)、[真实源流像](R271-appendix-exact-left-source-flow-range-and-minimal-upward-extension.md)、[不交窗顶部投影](R271-appendix-disjoint-window-top-projection-and-coherent-source-flow-removal.md)、[低三维块全模式联合回缩](R271-appendix-low-triplet-count-joint-retraction-and-original-high-energy-bound.md)、[前缀分割的线性失真](R271-appendix-linear-triplet-count-distortion-by-prefix-splitting.md)。

## 1. 保同一个实际顶部和一列不交未来带

固定原 $m,d=2^m,A=A_m,D=D_m$，并令
\[
Q=Q_m=\lfloor e^{d^3/4}\rfloor,\qquad b_0=Q-d.
\]
原 $0\ne w\in W=M\ominus N$ 的顶部构造给
\[
u_Q=E_Q^\dagger r_Q,\qquad
\|u_Q-P_{\le Q}^{(m)}w\|\le\eta_m\|w\|,
\quad \eta_m=e^{-74d^4}+e^{-75d^4}.
\]
记
\[
\tau_m=\|1_{\{\mathcal N_{\rm tot}>4d\}}w\|,\qquad
t_m=\tau_m/\|w\|\longrightarrow0,\qquad
\varepsilon_m=\tau_m+\eta_m\|w\|.
\tag{1.1}
\]
不假设这个尾有任何额外速率。

取
\[
a=b_0-d\left\lfloor\frac{b_0-4d}{d}\right\rfloor,\qquad
I=\{a,a+d,\ldots,b_0\},
\]
故 $4d\le a<5d$。对每个 $p\le Q$，仍定义真正来源
\[
r_p=A(u_Q)_p,\qquad E_p^\dagger r_p=P_{\le p}u_Q.
\]
保持原三个 Gram 和两已付费用
\[
L_p=J_{{\rm left},p}^{-1},\quad
B_p=J_{{\rm bare},p}^{-1},\quad
G_p=J_{{\rm right},p},\quad
\mathfrak M_p=B_p+L_pG_pL_p,
\]
\[
\Xi_p(r)^2=\alpha_p(r)^2+\lambda_{{\rm flat},p}(r)^2
=\langle\mathfrak M_pr,r\rangle .
\]
各未来带 $[p+1,p+d]$、$p\in I$ 彼此不交，故
\[
\boxed{\sum_{p\in I}\Xi_p(r_p)^2
\le2\|P_{[a+1,Q]}u_Q\|^2
\le2\varepsilon_m^2.}
\tag{1.2}
\]

只在顶部一半中选终端：
\[
J=I\cap[\lceil Q/2\rceil,Q-d],\qquad K=|J|.
\tag{1.3}
\]
对充分大的 $m$，
\[
K\ge Q/(4d),\qquad K\sim Q/(2d).
\tag{1.4}
\]
从 (1.2) 的有限平均可选一处真正切口 $b\in J$，使
\[
\boxed{\Xi_b(r_b)^2\le2\varepsilon_m^2/K.}
\tag{1.5}
\]
这个 $b$ 可依赖同一个 $w$。它在任何投影前选出；没有先改源再把新来源的切口冒作旧来源。

## 2. 在这个好顶部使用正确的加权总度量

令 $I_b=I\cap[a,b]$。对任意顶部源 $r\in\mathscr R_b$，置
\[
\Pi_{p,b}r=A P_pE_b^\dagger r.
\]
准确有
\[
E_p^\dagger\Pi_{p,b}r=P_{\le p}E_b^\dagger r,\qquad
\Pi_{b,b}=I.
\tag{2.1}
\]
原 $r_b\in\mathscr N_b$，其中
$\mathscr N_b=\ker[\iota_0^*(L_b+B_b)]$，因为 $b<Q$。

与未加权总度量不同，这次定义
\[
\boxed{
\mathfrak H_b^{\rm good}
=\mathfrak M_b+
K^{-1}\sum_{p\in I_b}\Pi_{p,b}^*\mathfrak M_p\Pi_{p,b}.
}
\tag{2.2}
\]
这是原源空间上的真正有界严格正度量，且
$\mathfrak H_b^{\rm good}\succeq\mathfrak M_b$。两个 $p=b$ 项分别具有系数 $1$ 和 $K^{-1}$，不将其中一个省掉。记其范数为 $\Psi_b$。

由 (1.2)、(1.5)，同一个原顶部满足
\[
\boxed{\Psi_b(r_b)^2\le4\varepsilon_m^2/K.}
\tag{2.3}
\]
顶部权重一保证可以使用顶部廉价估计；其余切口权重 $K^{-1}$ 保证不因累加这些费用毁掉好顶部的小量。

## 3. 顶部廉价类可以具有增长常数

设 $\mathscr E_b\subseteq\mathscr R_b$ 是一个已证明闭的原源空间，并有同源估计
\[
\boxed{\lambda_b(s)\le C_b\alpha_b(s)
\quad(s\in\mathscr E_b),\qquad C_b\ge1.}
\tag{3.1}
\]
它是原完整右费与原裸费，包含所有原自由度与交叉 Gram。

取
\[
Z_b=\mathscr E_b\cap\mathscr N_b,\qquad
s_b=P_{Z_b}^{\mathfrak H_b^{\rm good}}r_b,\qquad
\widehat r_b=r_b-s_b.
\tag{3.2}
\]
若还有已经由同一个顶部满足的闭约束，可以在 $Z_b$ 中继续取其交；不能凭逐窗不相容的旧余源构造这种约束。

投影保持顶部负图，且
\[
\Psi_b(r_b)^2=\Psi_b(s_b)^2+\Psi_b(\widehat r_b)^2.
\tag{3.3}
\]
对所有 $p\le b$ 定义
\[
s_p=\Pi_{p,b}s_b,\qquad
\widehat r_p=\Pi_{p,b}\widehat r_b.
\tag{3.4}
\]
它们是同一个新顶部最小者的所有真正截断，故
\[
T_{p+1}\widehat r_{p+1}=\widehat r_p,\qquad
E_p^\dagger\widehat r_p=P_{\le p}E_b^\dagger\widehat r_b.
\tag{3.5}
\]

(3.3) 与 (2.2) 给两项分别有用的真实残源预算：
\[
\boxed{\Xi_b(\widehat r_b)^2\le4\varepsilon_m^2/K,}
\]
\[
\boxed{\sum_{p\in I_b}\Xi_p(\widehat r_p)^2
\le4\varepsilon_m^2.}
\tag{3.6}
\]
未加权总和允许从原来的上界 $2\varepsilon_m^2$ 变成 $4\varepsilon_m^2$；没有声称它逐项或总体严格收缩。真正收缩的是 (3.3) 中显示的加权度量。

准确余条件为
\[
\boxed{\widehat r_b\in\mathscr N_b,\qquad
\iota_{Z_b}^*\mathfrak H_b^{\rm good}\widehat r_b=0.}
\tag{3.7}
\]
它不是每个切口的独立 $\mathfrak M_p$ 正交条件，也不是所选模式的坐标为零。

## 4. 全部左像、完整顶部右费及真实反馈均已支付

原正逆 Cauchy 及 (3.1) 给
\[
\mu_b(s)^2\le
\lambda_b(s)\lambda_{{\rm flat},b}(s)
\le\frac{C_b}{2}\Xi_b(s)^2
\quad(s\in Z_b).
\]
结合 (2.3)、(3.3)，得到
\[
\boxed{\mu_b(s_b)\le
\sqrt{\frac{2C_b}{K}}\,\varepsilon_m,}
\]
\[
\boxed{\lambda_b(s_b)\le
\frac{2C_b}{\sqrt K}\,\varepsilon_m.}
\tag{4.1}
\]
所以整个相容族的原物理左改变量满足
\[
\boxed{\sup_{p\le b}
\|E_p^\dagger r_p-E_p^\dagger\widehat r_p\|
\le\sqrt{\frac{2C_b}{K}}\,\varepsilon_m,}
\tag{4.2}
\]
而顶部真正完整最小费满足
\[
\boxed{|\lambda_b(r_b)-\lambda_b(\widehat r_b)|
\le\frac{2C_b}{\sqrt K}\,\varepsilon_m.}
\tag{4.3}
\]
这里没有免费控制每个较低切口各自的完整右费。

记 $R_p=(D:\mathcal H_{p+1}\to\mathcal H_p)^\dagger$。
同一改变量 $z=E_b^\dagger s_b$ 的唯一源流纤维为
\[
z_{p+1}=-R_ps_p+g_{p+1},
\]
其中 $g_{p+1}$ 是原流与残流真实非首头 primitive 增量的差。其两个尾分量正交。于是
\[
\boxed{\sum_{p=a}^{b-1}
\bigl(\|R_ps_p\|^2+\|g_{p+1}\|^2\bigr)
=\|P_{[a+1,b]}z\|^2
\le\frac{2C_b}{K}\varepsilon_m^2.}
\tag{4.4}
\]
全部单步 MP 反馈与 primitive 变化一次支付，没有用步数乘最大误差。

因此只需沿所选头子序列有
\[
\boxed{C_b^2\le C_0K}
\tag{4.5}
\]
且 $C_0$ 固定，(4.1)–(4.4) 就全部趋零。具体地，
\[
\mu_b(s_b)\le
\sqrt2 C_0^{1/4}K^{-1/4}\varepsilon_m,\qquad
\lambda_b(s_b)\le2\sqrt{C_0}\,\varepsilon_m.
\]
这不需要给 $\tau_m$ 添加速率。由原截断近似，
\[
\boxed{\sup_{a\le p\le b}
\|E_p^\dagger\widehat r_p-w\|
\le
\left(1+\sqrt{\frac{2C_b}{K}}\right)\varepsilon_m
\longrightarrow0.}
\tag{4.6}
\]
新的顶部仍有 (3.6) 的特别小的真实 flat/裸费用，可以继续进行已经证明的一次顶部运输。别的余图若未被实际保持，不能随同免费运输。

## 5. 明确原低三维块应用：约 m sqrt(Q/d) 个任意位置模式

使用前缀分割稿的同一个闭源空间、同一个原配对和同一个回缩。该稿证明，在 $m\ge47$、短塔参数 $\theta\le1/8$ 时，
\[
\boxed{C\le32(1+R/m)}
\tag{5.1}
\]
控制至多 $R$ 个完整三维 $Q$ 块的全部位置模式及其所选远尾出生。它不含模式数因子。

对充分大的 $m$，令
\[
X_m=\sqrt{Q_m/d},\qquad
\boxed{R_m=\left\lfloor\frac{mX_m}{128}\right\rfloor,\quad
s=R_m-1,\quad T=2R_m-1.}
\tag{5.2}
\]
对每个候选终端 $q\in J$，取原配对数
\[
N_{\rm pair}=q-s=q-R_m+1,\qquad
J_{\rm tail}=m+2N_{\rm pair}.
\]
所有权和原头仍是原始的 $A_m,D_m$；仅在这些真实对上构造已经证明的回缩。

因为 $Q_m$ 指数大于任意 $d$ 的固定幂，充分大 $m$ 时
\[
R_m\ge d,\qquad R_m\le q/2,\qquad R_m\le N_{\rm pair}.
\tag{5.3}
\]
原短塔参数为
\[
H=T+d+1=2R_m+d,\qquad
P=s+R_m+d=2R_m+d-1.
\]
由 $J_{\rm tail}+1\ge q\ge Q_m/2$，
\[
\begin{aligned}
\theta
&=\frac{12HP}{J_{\rm tail}+1}
\le\frac{108R_m^2}{q}
\le\frac{216R_m^2}{Q_m}\\
&\le\boxed{\frac{27m^2}{2048d}\longrightarrow0.}
\end{aligned}
\tag{5.4}
\]
所以最终 $\theta\le1/8$，满足 (5.1) 的完整条件。

每个具有 $r\le R_m$ 个三维块的模式保留完整远尾出生
\[
\begin{cases}
0\le b_{\rm far}\le R_m-1,&r=0,\\
0\le b_{\rm far}\le R_m-r,&1\le r\le R_m.
\end{cases}
\tag{5.5}
\]
其源 active 次数 $t=s+r-b_{\rm far}$ 满足
\[
\max(0,2r-1)\le t\le2R_m-1=T.
\]
因此每个模式的高出生域都确实为零，原同源 $\lambda\le C\alpha$ 保持；没有删掉这项下界。

由 (5.1)、(5.2)，当 $X_m\ge128$ 时，
\[
C\le32(1+R_m/m)\le32+X_m/4\le X_m/2.
\]
于是
\[
\boxed{C^2\le Q_m/(4d)\le K.}
\tag{5.6}
\]
这对全部候选终端统一成立，所以选出 (1.5) 的真实好终端后仍可使用。取 $C_0=1$，(4.1)–(4.6) 立即支付相容实际删除，特别
\[
|\lambda_b(r_b)-\lambda_b(\widehat r_b)|\le2\varepsilon_m,\qquad
\sum_{p=a}^{b-1}
(\|R_ps_p\|^2+\|g_{p+1}\|^2)
\le2K^{-1/2}\varepsilon_m^2.
\tag{5.7}
\]
整个原模式联合数从一致常数实例的 $O(m)$ 扩大为
$R_m\sim m\sqrt{Q_m/d}/128$。它仍远小于 $N_{\rm pair}\asymp Q_m$；超过 $R_m$ 的模式以及不同配对划分的联合没有被支付。

## 6. 剩余比较门槛与准确限制

由于 $b\ge Q/2$，$|I_b|\asymp Q/d$。令
\[
\vartheta_m=
\sqrt{1-t_m^2}-\eta_m
-\sqrt{2C_b/K}\,(t_m+\eta_m)\longrightarrow1.
\]
所有 $p\in I_b$ 满足
$\mu_p(\widehat r_p)\ge\vartheta_m\|w\|$。
对同一个相容残源族定义
\[
\mathcal C_{m,p}^{\rm rem}(w)
=\frac{\mu_p(\widehat r_p)^2}{\Xi_p(\widehat r_p)^2}.
\]
由 (3.6)，
\[
\boxed{\sum_{p\in I_b}
\frac1{\mathcal C_{m,p}^{\rm rem}(w)}
\le\frac{4(t_m+\eta_m)^2}{\vartheta_m^2}
\longrightarrow0.}
\tag{6.1}
\]
因此，在保留 (3.7) 与同一实际来源的这个余族上，
$\sup_{p\in I_b}\mathcal C_{m,p}^{\rm rem}=O(Q/d)$
仍足以排除非零 $w$。本文没有证明这个剩余比较。

新增的支付是：真实好终端的选择、加权总度量的全部费用、增长回缩常数下的整流及完整顶部费运输，以及一个大幅扩展而仍具体的原模式删除空间。它不把原来源改成模型来源，不将总正交条件替成每窗正交，也不声称所有原高返回已经受控。
