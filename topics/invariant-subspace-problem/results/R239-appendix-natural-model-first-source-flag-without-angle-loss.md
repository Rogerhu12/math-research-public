# R239 附录：天然四块模型首源旗的无角度支付与真实负图归约

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文证明一个比“原首头加天然零源旗”更大的闭源旗，在该旗上其余源头的完整右费用由四块延拓误差直接支付，不损失未知夹角。与真正左源流负图相交后，左费及完整左右核费均指数小于同源两费用；随后可作保持负图的真正两费用投影。本文没有将余图误作 primitive 支撑消失，也没有证明余源的温和两费用比较；普通 ISP 与 $N=M$ 仍为 OPEN。

依赖：[四块头比较](R239-appendix-four-block-head-comparison-and-quarter-depth-source-elimination.md)、[天然零源旗](R239-appendix-natural-four-block-free-flag-and-bare-chain-transport.md)、[首源头共同右度量及联合旗](R239-appendix-joint-deep-strip-flag-and-same-flat-middle-transfer.md)，以及 [R271 真负图与全部合法窗归约](R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)。新估计由 §3 的原完整右最小者投影证明，不由天然零源旗和首头对角之间的夹角推出。

## 1. 原坐标、模型源与唯一使用的小量

固定
$$
m\ge8,\quad d=2^m,\quad h=d/4,\quad n=m-2,
\quad4d\le q\le e^{d^3/4}.
$$
令 $A=A_m$、$D=D_m$，模型头为
$$
A_\square=I_4\otimes A_n+
(b_nE_0+b_{n+1}E_1)\otimes I_h.
$$
所有源和右链先保持原 $m$ 的物理分层、原尾 $D_m$ 及原宽度 $d$ 联合旗。

原强制 primitive 坐标为
$$
\mathscr U=
\bigoplus_{t=0}^{d-2}
\mathscr H_{\ge t+1}\otimes K_{q-t},
\qquad K_j=\ker D\cap\mathcal H_j,
$$
$$
\Gamma:\mathscr R_q\overset\sim\longrightarrow\mathscr U,
\qquad B_U=\Gamma^{-1},\qquad
\mu_A(r)^2=\langle\mathcal G\Gamma r,\Gamma r\rangle,
\quad\mathcal G\succeq I.
\tag{1.1}
$$
写 $a=(a_t)$，$a_t$ 位于孔层 $q-t$。顺次单步 MP primitive 延拓为
$$
\mathcal E_T^{\rm full}a
=\sum_{k\ge0}(-T)^kQ_ka,
\qquad C_T=P_{>q}\mathcal E_T^{\rm full},
$$
而源映射为
$$
\mathcal B_Ta
=T(P_q\mathcal E_T^{\rm full}a)
=\sum_{t=0}^{d-2}(-1)^tQ_tT^{t+1}a_t.
\tag{1.2}
$$
这里 $T=A$ 或 $A_\square$，并在 nilpotency 阶后自动截断。原映射满足 $\mathcal B_A|_{\mathscr U}=B_U$。链 $-C_Aa$ 是源 $B_Ua$ 的合法原完整右链。

四块延拓比较给
$$
\|C_A-C_\square\|\le\rho,
\qquad
\rho=216\eta_{m-3}(2048q^2)^3dh(h+1)^2e^{11d^4/40}
\le e^{-d^4/20}<1.
\tag{1.3}
$$
本稿只需 primitive 输入孔数 $\le q$ 的版本，不另扩大参数窗口。

原首源头投影记为
$$
P=\iota_0\iota_0^*,\qquad Q=I-P.
$$
其 primitive 像为
$$
\Delta=\Gamma(P\mathscr R_q)
=\bigoplus_{t=0}^{d-2}\mathbb Ce_{t+1}\otimes K_{q-t}.
\tag{1.4}
$$
头空间上的投影到 $e_0^\perp$ 另记为 $Q_{\rm head}$，以区别源 $Q$ 和顺次原像 $Q_t$。

## 2. 模型首源条件迫其规范右链完全落在物理首头

定义 primitive 闭旗
$$
\boxed{
\mathscr K_0=
\{a\in\mathscr U:Q_{\rm head}\mathcal B_\square a=0\},
\qquad
\mathscr X_0=B_U\mathscr K_0.
}
\tag{2.1}
$$
这是有界映射的核；$B_U$ 是固定参数下的有界同构，因此 $\mathscr X_0$ 为闭源子空间。

Taylor primitive 坐标的唯一性给
$$
a\in\mathscr K_0
\quad\Longleftrightarrow\quad
Q_{\rm head}A_\square^{t+1}a_t=0
\quad\text{对每个 }t.
\tag{2.2}
$$
确切地，$P_0D^jQ_ta_t$ 在 $j\ne t$ 时为零，在 $j=t$ 时为 $a_t$；因此不同 $t$ 的输出不能在 (1.2) 中隐藏相消。

若 (2.2) 成立，$A_\square^{t+1}a_t$ 只在物理头 $e_0$。模型严格降头，故
$A_\square^{t+2}a_t=0$。来自第 $t$ 个输入、越过旧 $q$ 的第一项是 $k=t+1$，其后全部为零。因此
$$
\boxed{
C_\square a
=e_0\otimes z(a)
\quad\text{只位于右首段 }q+1,
\qquad a\in\mathscr K_0.
}
\tag{2.3}
$$
相应尾向量属于 $\ker D^d$，并且 $D z(a)$ 属于原首源旗 $E_{d-1,q}$。这是一个实际原完整右链：原 $Ae_0=0$，所以高输出全部为零。其首源属于 $P\mathscr R_q$。

特别 $\Delta\subseteq\mathscr K_0$：对头 $e_{t+1}$，任何严格降头的第 $t+1$ 次幂都只能落在 $e_0$。天然模型零源旗在原强制坐标中的部分
$$
\mathscr Y=\mathscr F_\square\ominus\mathscr F_A
=\mathscr U\cap\ker\mathcal B_\square
$$
也包含在 $\mathscr K_0$。所以
$$
P\mathscr R_q\subseteq\mathscr X_0,
\qquad B_U\mathscr Y\subseteq\mathscr X_0.
\tag{2.4}
$$
这里未断言 $\mathscr Y\perp\Delta$，也不需要这个断言。

## 3. 原完整右投影直接消去模型首头链

令原完整右映射为 $F:\mathscr C\to\mathscr R_q$，其 Gram 为 $G=FF^*$。首头共同度量分裂已给
$$
[P,G]=0.
$$
故两个完整最小右像
$$
\mathscr U_P=F^\dagger(P\mathscr R_q),\qquad
\mathscr U_Q=F^\dagger(Q\mathscr R_q)
$$
是同一物理右带中的闭正交子空间；它们还与 $\ker F$ 正交。记 $\Pi_Q$ 为该物理右带中投到 $\mathscr U_Q$ 的正交投影。

任意合法完整右链 $c\in\mathscr C$ 满足
$$
\Pi_Qc=F^\dagger QFc.
\tag{3.1}
$$
这是先去除零源右核，再使用源度量 $G^{-1}$ 对首头的约化。特别 (2.3) 给
$$
\Pi_QC_\square a=0\quad(a\in\mathscr K_0),
$$
而原规范右链给
$$
\Pi_QC_Aa=-F^\dagger Q B_Ua.
$$
于是
$$
\boxed{
\begin{aligned}
\lambda_A(Qr)
&=\|F^\dagger Qr\|\\
&=\|\Pi_Q(C_A-C_\square)\Gamma r\|\\
&\le\rho\|\Gamma r\|\le\rho\mu_A(r),
\qquad r\in\mathscr X_0.
\end{aligned}}
\tag{3.2}
$$
这是本文的新支付。它用整个实际 $a=\Gamma r$，没有选分解 $a=\delta+y$ 后估计 $\|y\|/\|a\|$。即使天然零源旗与 $\Delta$ 的夹角退化，(3.2) 也原样成立。

## 4. 这个旗比 Δ加天然零源旗恰多最后两个模型首头 jets

因为 $A_\square^{h+2}=0$，其首源头的 Taylor 深度最多为 $h$。对 $0\le t\le h-2$，原对角向量 $e_{t+1}$ 位于第一低块，且
$$
A_\square^{t+1}e_{t+1}=A_n^{t+1}e_{t+1}\ne0
\quad\text{在头 }e_0.
\tag{4.1}
$$
所以这些层的模型首源已由 $\Delta$ 在模 $\mathscr Y$ 下覆盖。

记
$$
\omega=A_n^{h-1}e_{h-1}\ne0,
\qquad\omega\in\mathbb Ce_0,
\quad b=b_n,\quad c=b_{n+1}.
$$
原物理四块中有准确幂恒等式
$$
\boxed{
A_\square^h e_{2h-1}=h b\,\omega,
\qquad
A_\square^{h+1}e_{d-1}=h(h+1)bc\,\omega.
}
\tag{4.2}
$$
第一式只有一次高位删除和 $h-1$ 次低头项存活；第二式只有两次高位删除和 $h-1$ 次低头项存活，且 $(bE_0+cE_1)^2e_3=2bc e_0$。因此它们分别补上 $t=h-1,h$ 的最后两层模型首源 jets，且原强制旗要求的头下界均满足。

对 $t\ge h-1$，原对角头 $e_{t+1}$ 已被 $A_\square^{t+1}$ 杀掉：写头指标 $t+1=kh+\ell$，则该基向量在模型中的最大非零幂阶不超过 $\ell+\operatorname{popcount}(k)<kh+\ell$。故这些对角本已在 $\mathscr Y$ 中。

因此有准确的代数和（并未声明各项正交）
$$
\boxed{
\mathscr K_0=
\mathscr Y+\Delta
+\bigl(\mathbb Ce_{2h-1}\otimes K_{q-h+1}\bigr)
+\bigl(\mathbb Ce_{d-1}\otimes K_{q-h}\bigr).
}
\tag{4.3}
$$
证明覆盖时，对每个 $t$，(2.2) 的像是至多一维头 $e_0$；(4.1) 或 (4.2) 提供非零原像，扣去该原像后恰落在 $\ker A_\square^{t+1}$，即 $\mathscr Y$。对 $t\ge h+1$，模型幂已为零，整个该层均在 $\mathscr Y$ 中。

所有这些和在固定参数下闭：每层只有有限维头子空间，再与同一个 primitive 尾空间张量，最后只有有限个 $t$。未由有限维闭性声称统一夹角界。

## 5. 整个旗上的一般两费用比较

原三个度量为
$$
L=J_{\rm left}^{-1},\quad B=J_{\rm bare}^{-1},
\quad G=J_{\rm right},\quad\mathfrak M=B+LGL,
$$
$$
\mu^2=\langle Lr,r\rangle,\quad
\alpha^2=\langle Br,r\rangle,\quad
\lambda_{\rm flat}^2=\langle GLr,Lr\rangle,
\quad\chi^2=\alpha^2+\lambda_{\rm flat}^2.
$$
首头分裂给 $B_P=K,G_P=K^{-1}$，二者均约化 $P$。定义
$$
\alpha_0^2=\langle K\iota_0^*r,\iota_0^*r\rangle,
\qquad \ell_j=\|G^{1/2}P_jLr\|,
\quad P_0=P,\ P_1=Q.
$$
对 $r\in\mathscr X_0$，(3.2) 与两个度量 Cauchy 给
$$
\mu^2\le\alpha_0\ell_0+\rho\mu\ell_1,
\qquad\chi^2\ge\alpha_0^2+\ell_0^2+\ell_1^2.
$$
归一化 $\mu=1$，先用 $\alpha_0^2+\ell_0^2\ge2\alpha_0\ell_0$，再最小化
$u^2+2\max(1-\rho u,0)$；因 $\rho<1$，最小值为 $2-\rho^2$。因此
$$
\boxed{\mu(r)^2\le\frac1{2-\rho^2}\chi(r)^2,
\qquad r\in\mathscr X_0.}
\tag{5.1}
$$
这只在已明确的旗上成立，不是整个原源空间的统一结论。

## 6. 真实负源图上的指数小加强

R271 的准确原源流像为
$$
\mathscr N=\operatorname{Ran}T_{q+1}
=\ker[\iota_0^*(L+B)].
\tag{6.1}
$$
令 $r\in\mathscr N$，$r_0=\iota_0^*r$，$\kappa=\langle Kr_0,r_0\rangle$。准确负配对是
$$
PLr=-\iota_0Kr_0,
\qquad
\mu(r)^2+\kappa=\operatorname{Re}\langle QLr,Qr\rangle.
\tag{6.2}
$$
置 $\mathscr Z_0=\mathscr N\cap\mathscr X_0$。对 $r\in\mathscr Z_0$，(3.2) 给
$$
\boxed{\mu(r)^2+\kappa\le\rho\mu(r)\ell_1.}
\tag{6.3}
$$
故
$$
\boxed{\mu(r)\le\rho\ell_1\le\rho\chi(r).}
\tag{6.4}
$$
同一个不等式还给
$$
0\le\kappa\le\frac{\rho^2}{4}\ell_1^2,
\qquad
\lambda(Qr)^2\le\rho^2\mu(r)^2.
$$
由于完整右费亦由首头约化，$\lambda(r)^2=\kappa+\lambda(Qr)^2$，从而
$$
\boxed{
\begin{aligned}
\lambda(r)^2&\le(\rho^2/4+\rho^4)\chi(r)^2,\\
\mu(r)^2+\lambda(r)^2&\le\rho^2(1+\rho^2)\chi(r)^2,
\qquad r\in\mathscr Z_0.
\end{aligned}}
\tag{6.5}
$$
后一个常数直接由 (6.3) 加上 $\lambda(Qr)^2$ 得到；没有使用错误的 $\alpha\ge\lambda$ 方向。

## 7. 保负图的真正两费用投影：无需天然 Y 的夹角

因 $\Delta\subseteq\mathscr K_0$，可以在 primitive 原内积中定义
$$
\mathscr W_0=\mathscr K_0\cap\Delta^\perp,
\qquad \mathscr K_0=\Delta\oplus\mathscr W_0.
\tag{7.1}
$$
这只是在已经证明闭且包含 $\Delta$ 的 $\mathscr K_0$ 内取正交补；(3.2) 已独立付清，故没有借此偷付天然 $\mathscr Y$ 的角度。

置
$$
N_0=\iota_0^*(L+B)\iota_0=K+L_{00},
\qquad
\mathcal E_N=I-\iota_0N_0^{-1}\iota_0^*(L+B).
$$
它的像是 $\mathscr N$，核是首源头，而且只加减首源头。因此它将 $\mathscr X_0$ 映到 $\mathscr Z_0$。定义
$$
\mathcal R_0=\mathcal E_N B_U|_{\mathscr W_0}.
\tag{7.2}
$$
这是 $\mathscr W_0$ 到 $\mathscr Z_0$ 的有界同构，其逆是
$$
w=P_{\mathscr W_0}\Gamma r\quad(r\in\mathscr Z_0).
\tag{7.3}
$$
由 (1.1)、(6.4) 及 (7.3)，
$$
\|w\|\le\mu(\mathcal R_0w)\le\rho\chi(\mathcal R_0w).
$$
所以
$$
H_0=\mathcal R_0^*\mathfrak M\mathcal R_0
\succeq\rho^{-2}I.
\tag{7.4}
$$
对于任意真正负图源 $r\in\mathscr N$，取
$$
s=\mathcal R_0H_0^{-1}\mathcal R_0^*\mathfrak Mr,
\qquad \widehat r=r-s.
\tag{7.5}
$$
则
$$
\boxed{
\begin{gathered}
s,\widehat r\in\mathscr N,\qquad s\in\mathscr X_0,\\
\chi(r)^2=\chi(s)^2+\chi(\widehat r)^2,\\
\|E_q^\dagger r-E_q^\dagger\widehat r\|
=\mu(s)\le\rho\chi(r).
\end{gathered}}
\tag{7.6}
$$
精确余图为
$$
\boxed{
\iota_0^*(L+B)\widehat r=0,
\qquad\mathcal R_0^*\mathfrak M\widehat r=0.
}
\tag{7.7}
$$
它不等于 $P_{\mathscr K_0}\Gamma\widehat r=0$，也不等于模型首源或天然零源 primitive 坐标消失。所有左交叉与低锚仍在 $\mathcal E_N,\mathcal R_0,H_0$ 和 $\mathfrak M$ 内。

如在 (7.7) 上另付 $\mu(u)^2\le C\chi(u)^2$，则由 (7.6) 与二维 Cauchy 得
$$
\mu(r)^2\le(\rho^2+C)\chi(r)^2\quad(r\in\mathscr N).
\tag{7.8}
$$
本文没有提供这个余图 $C$。

## 8. 完整核及同一个 primitive 增量的一层运输

对投影分量 $s\in\mathscr Z_0$，准确原有限模型零源核
$$
k_q(s)=E_q^\dagger s-F^\dagger s
$$
支持于 $\le q+d$，并由左右物理支撑正交及 (6.5) 满足
$$
\boxed{\|k_q(s)\|^2\le\rho^2(1+\rho^2)\chi(s)^2.}
\tag{8.1}
$$
这仍是原 $A_m+D_m$ 核，不未经 carry 比较就称为实际边界算子核。

若 $q,q+1$ 均合法，记
$$
\mathscr X_{q+1}=\bigoplus_{i=0}^{d-1}e_i
(\ker D^{d-i}\cap\mathcal H_{q+1}),
\qquad\mathcal D_{q+1}=D|_{\mathscr X_{q+1}}.
$$
对同一个原源流纤维，R271 的准确拼合写为
$$
t_{\rm up}=-A_m\mathcal D_{q+1}^{\dagger}r+A_mg,
\qquad
E_{q+1}^{\dagger}t_{\rm up}
=E_q^\dagger r\oplus(-\mathcal D_{q+1}^{\dagger}r+g),
$$
其中 $g\in\bigoplus_{i=1}^{d-1}e_iK_{q+1}$ 是该纤维已经给定的实际 primitive 增量。以 (7.5) 的 $\widehat r$ 替换 $r$，但保持同一个 $g$，得到 $\widehat t_{\rm up}$，并且
$$
\boxed{
\|E_{q+1}^{\dagger}t_{\rm up}
-E_{q+1}^{\dagger}\widehat t_{\rm up}\|^2
\le\rho^2(1+\rho^2)\chi(r)^2.
}
\tag{8.2}
$$
这里只用 $\|\mathcal D_{q+1}^{\dagger}s\|\le\lambda(s)$ 和 (6.5)。没有声称新的上层源满足下一负图或其两费用自动收缩，因此不能无条件迭代 (8.2)。

## 9. 实际窗口族和剩余范围

R271 的同一个顶部最小者在每个完整未来窗的真实截断都落在 $\mathscr N_q$，并有同向量累计两费用预算。对该族逐窗使用 (7.5)，两费用不增、左改变量至多 $\rho_q\chi_q$。由于 (1.3) 对全部原合法 $q$ 统一有 $\rho_q\le e^{-d^4/20}$，R271 的实际窗数及同一强极限预算可原样用于新的余图 (7.7)。不需要把各窗投影后的源重新声明为同一条源流。

新的闭合部分是：天然模型零源旗、原首头对角以及模型最后两个首头 jets 可以一起支付，且无需任何未经证明的夹角下界。支付来自原完整最小右投影对模型首头链的精确消去。新的余问题仍是 (7.7) 中实际来源的温和两费用比较，而不是某个声称已经消失的 primitive 支撑。
