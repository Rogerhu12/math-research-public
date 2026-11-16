# R271 附录：真实强前缀与原大头的完整 Gram 比较及远尾方差同源极限

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 原强头
$$
C=A_m+D_{[m,m+R)}
$$
与同一物理坐标上的原真实大头 $A_{m+R}$ 的差，正是原全局 carry 误差的压缩。本稿把这一差直接放进完整正 Gram，得到对全部截断高度、乃至完整塔都统一的 inverse 比较。没有把 Gram 先压到 forcing 的原支持，没有交换压缩与 inverse，也不支付头 Jordan 相似条件数。

特别，$d=2^m$、$R=d$、$x=m+d$、$h=2d$ 时，可将此前一般强前缀定理的 $s_m\ge S_m$ 改为
$$
s_m\ge S_{x_m},\qquad s_m\longrightarrow0.
$$
这时 $S_x/S_m$ 可以趋零；不是仅向下移动固定几个位置的薄方差窗。原全部 $V_Q/K_Q/u_f$ 来源仍保持，条件是原物理 $Q\ge R+J$。原完整 $(C+D_x)$ 修复、受限返回和 same-$w$ 两费比较仍未由本稿闭合。

已付依据：

- [原联合 carry 与 $e^{26d^3}$ 母窗口](../notes/2026-11-14-joint-positive-carry-budget-and-twenty-six-window-actual-sources-789f-next.md)，尤其 §5(5.1)、(5.4)；
- [原放大方差、任意截断完整 inverse 与同源物理列](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)，尤其 §§1--5；
- [一次完整 MP 与同源残量](R271-appendix-damped-small-height-complete-once-mp-residual-and-moving-head-budget.md)，尤其 §§3--6；
- [二次顺次 MP 与真实 primitive 回馈](R271-appendix-coherent-second-sequential-mp-primitive-feedback-and-same-source-repair.md)。

## 1. 原 N/Y 坐标中的准确 carry 压缩

令 $T=T_N$ 或 $T_Y$，$M=\ker T$。原物理空间按二进制位分解。$\iota_p$ 将前 $p$ 位头嵌入原空间，并把以后全部位置于真空。其像为整数坐标
$$
\operatorname{span}\{e_0,\ldots,e_{2^p-1}\},
$$
是 $T$ 的不变子空间；真正的原头满足
$$
A_p=\iota_p^*T\iota_p.
\tag{1.1}
$$
这在 N 型保留全部加权后移幂，在 Y 型保留全部 Cayley 项的有限幂零代入，不换成普通 Boolean 头。

记
$$
b_i=(i+1)^{-2},\qquad
D_{\ge p}=\sum_{i\ge p}b_iE_i,\qquad
L_m=A_m+D_{\ge m}.
\tag{1.2}
$$
$E_i$ 是原第 $i$ 位 Boolean 删除，$\|E_i\|=1$。原幂与 Cayley 范数界给
$$
\|A_p\|\le6,\qquad
\sum_{i\ge m}b_i\le\frac1m.
\tag{1.3}
$$

设 $m\ge10$、$d=2^m$，取整数 $R\ge0$，置
$$
x=m+R,\qquad
C=A_m+D_{[m,x)},\qquad
h=d+R,\qquad C^h=0.
\tag{1.4}
$$
$C$ 作用于全部前 $x$ 位；旧头上的 $A_m$ 按恒等张量延拓，强位没有删任何状态。因此
$$
C=\iota_x^*L_m\iota_x,\qquad
C-A_x=\iota_x^*(L_m-T)\iota_x,\qquad
\|C\|\le7.
\tag{1.5}
$$
特别，Y 型的差也是 (1.5) 中完整的原差，不是分别删除 Cayley 高次项后的差。

令 $\eta_m=\|L_m-T\|$。所引 c26 稿的联合预算准确为
$$
\mathcal J_m(\mathcal R_m)
=\mathcal R_m
\sum_{\substack{j,k<d\\a\ge0}}
\frac{\mathcal R_m^{j+k+a}}{(j+1)!\,k!\,a!}
\|A_m^j(\operatorname{ad}_{D_m}^a(L_m-T))A_m^k\|
\le2e^{-(15/8)d^4},
$$
其中 $\mathcal R_m=e^{(417/8)d^3}\ge1$。保留其中的 $j=k=a=0$ 项，即得
$$
\boxed{
\eta_m\le2\mathcal R_m^{-1}e^{-(15/8)d^4}
\le e^{-d^4},\qquad m\ge10.
}
\tag{1.6}
$$
本稿只使用这个已经付清的无权后果；没有再把同一 carry 负指数用于另一项预算。

## 2. 任意高度的完整 Gram 扰动引理

令 $A,B$ 为同一 Hilbert 空间上的有界算子，
$$
\|A\|,\|B\|\le M,\qquad \|A-B\|\le\eta.
$$
对 $s>0$、整数 $J\ge1$ 或 $J=\infty$，定义
$$
H_{A,J}(s)=\sum_{j=0}^J\frac{(A^*)^jA^j}{s^j j!}.
\tag{2.1}
$$
$J=\infty$ 的和在算子范数收敛，因为其范数被 $e^{M^2/s}$ 控制。每一个 $H_{A,J}(s)\succeq I$，故完整 inverse 有界且范数至多 $1$。

逐次 telescoping 给
$$
\|A^j-B^j\|\le j\eta M^{j-1}.
$$
把两边乘积的差分开，得到
$$
\|(A^*)^jA^j-(B^*)^jB^j\|
\le2j\eta M^{2j-1}.
$$
于是对全部 $J$，
$$
\boxed{
\begin{aligned}
\|H_{A,J}(s)-H_{B,J}(s)\|
&\le\frac{2\eta M}{s}
\sum_{k=0}^{J-1}\frac{(M^2/s)^k}{k!}\\
&\le\frac{2\eta M}{s}e^{M^2/s}.
\end{aligned}
}
\tag{2.2}
$$
$J=\infty$ 时第一行的和也取到无穷。有限 $J$ 时还可保
$$
\sum_{k<J}\frac{t^k}{k!}
\le \min\{e^t,\ J\max(1,t)^{J-1}\}.
\tag{2.3}
$$
这保留了在更远 $x$、较短 $J$ 时可用的另一个参数范围。

完整 resolvent identity 为
$$
H_{A,J}^{-1}-H_{B,J}^{-1}
=H_{A,J}^{-1}(H_{B,J}-H_{A,J})H_{B,J}^{-1}.
$$
因此
$$
\boxed{
\|H_{A,J}(s)^{-1}-H_{B,J}(s)^{-1}\|
\le\frac{2\eta M}{s}e^{M^2/s}.
}
\tag{2.4}
$$
这里没有 inverse 平方的 Loewner 推理，也没有先压 forcing 支持。两边都是同一完整空间上的 inverse。

## 3. 原强前缀在真正远尾方差上的统一比较

原连续尾方差满足
$$
S_x=\sum_{i\ge x}(i+1)^{-4},\qquad
\frac1{3(x+1)^3}\le S_x\le\frac1{3x^3}.
\tag{3.1}
$$
将 §2 用于 (1.5)，取 $M=7$。若 $s\ge S_x$，则对全部 $J$，
$$
\begin{aligned}
&\|H_{C,J}(s)-H_{A_x,J}(s)\|,\\
&\|H_{C,J}(s)^{-1}-H_{A_x,J}(s)^{-1}\|\\
&\qquad\le
42(x+1)^3
\exp\{-d^4+147(x+1)^3\}.
\end{aligned}
\tag{3.2}
$$
这里 $H_{C,J}$ 已保全部强位及所有中间源；$H_{A_x,J}$ 则保原真实 $x$ 位头的全部物理维数。

一个明确的全高度区间是
$$
\boxed{
m\ge10,\qquad m\le x,\qquad
x+1\le\frac{d^{4/3}}8,\qquad s\ge S_x.
}
\tag{3.3}
$$
在此范围，
$$
147(x+1)^3\le\frac{147}{512}d^4,
$$
而
$$
\log(42(x+1)^3)
\le\log(42d^4)\le\frac1{16}d^4
\qquad(d\ge1024).
$$
故 (3.2) 的对数至多 $-(333/512)d^4<-d^4/2$。准确有
$$
\boxed{
\sup_{1\le J\le\infty}
\|H_{C,J}(s)^{-1}-H_{A_x,J}(s)^{-1}\|
\le e^{-d^4/2}.
}
\tag{3.4}
$$
同一界亦适用于两个完整 Gram 的差。

特别取
$$
R=d,\qquad x=m+d,\qquad h=2d.
\tag{3.5}
$$
对 $m\ge10$，有 $8(m+d+1)\le d^{4/3}$，所以 (3.3) 成立。这没有改变原物理强位权或 far cut；$h=2d$、$x\asymp d$ 正是原可用的强前缀量级。

## 4. 全部强源 inverse 与相干代表的强极限

现在令 $m\to\infty$，取满足 (3.3) 的 $x_m=m+R_m$，以及
$$
s_m\ge S_{x_m},\qquad s_m\to0,\qquad
1\le J_m<h_m=2^m+R_m.
\tag{4.1}
$$
固定原有限物理 forcing $f$。充分大 $m$ 后 $f$ 位于前 $m$ 位，记其在前 $x_m$ 位加中间真空的同一向量为 $g_m$。取完整最小源
$$
a_m=H_{C_m,J_m}(s_m)^{-1}g_m,\qquad
q_m=\langle g_m,a_m\rangle.
\tag{4.2}
$$

所引放大方差定理在原真实头 $A_{x_m}$ 上适用，因为
$x_m\to\infty$、$s_m\ge S_{x_m}$、$s_m\to0$，并允许任意 $J_m\ge1$。故
$$
\iota_{x_m}H_{A_{x_m},J_m}(s_m)^{-1}g_m\to P_Mf.
$$
(3.4) 在同一完整头上的算子范数比较于是给
$$
\boxed{\iota_{x_m}a_m\longrightarrow P_Mf.}
\tag{4.3}
$$
这一步不使用 $s_m\ge S_m$。在 (3.5) 下，例如 $s_m=(1+o(1))S_{m+d}$，其与 $S_m$ 的比可以趋零。

因 $H_{C_m,J_m}\succeq I$，
$$
\epsilon_m
:=q_m-\|a_m\|^2
=\sum_{j=1}^{J_m}\frac{\|C_m^ja_m\|^2}{s_m^j j!}
\ge0.
\tag{4.4}
$$
由 (4.3) 和 $\langle f,P_Mf\rangle=\|P_Mf\|^2$，
$$
\boxed{\epsilon_m\to0.}
\tag{4.5}
$$
没有给 $\epsilon_m$ 添加未证明的移动参数速率。

在真正远尾 $D_{x_m}$ 上令
$$
\omega_{m,j}=(D_{x_m}^*)^j\Omega,\qquad
F_m=\sum_{j=0}^{J_m}
\frac{(-C_m)^ja_m\otimes\omega_{m,j}}{s_m^j j!}.
\tag{4.6}
$$
$\|\omega_{m,j}\|^2\le j!S_{x_m}^j$，不同 $j$ 处于正交远孔层，所以
$$
\|F_m-\iota_{x_m}a_m\|^2
\le\frac{S_{x_m}}{s_m}\epsilon_m\le\epsilon_m.
$$
因此
$$
\boxed{F_m\longrightarrow P_Mf}
\tag{4.7}
$$
在原物理 Hilbert 空间中强收敛。全部 $F_m$ 是有限远孔物理向量，所有有限层的删除、创建及所列头幂都在其自然定义域。

完整 $J=h_m-1$ 亦包含在 (4.1)--(4.7) 中；它不需要先用完整 inverse 推测 $a_m$ 的低强孔支持。

## 5. 同一个原 $V_Q/K_Q/u_f$，没有重选来源

沿原头 $m$ 的 total-tail cut 定义
$$
V_{m,Q}=\{v:\Pi_{\le Q}^{(m)}v=v,\
\Pi_{<Q}^{(m)}(A_m+D_m)v=0\},
$$
$$
K_{m,Q}=\ker(A_m+D_m)\cap\operatorname{Ran}\Pi_{\le Q}^{(m)}.
$$
因
$$
A_m+D_m=C_m+D_{x_m},
$$
这仍是原同一个算子，既没有把 $A_m$ 改成 $A_{x_m}$，也没有改变 far tail 权值。$A_{x_m}$ 只用于 §3 的完整 Gram 比较。

对每个 cut，只要求原准确的来源条件
$$
\boxed{Q_m\ge R_m+J_m.}
\tag{5.1}
$$
从原低行方程逐次将 $D_{x_m}$ 移至头侧，得到对 $0\le j\le J_m$
$$
P_{V_{m,Q_m}}(D_{x_m}^*)^j i_0
=(-1)^j(P_{V_{m,Q_m}}i_0)(C_m^*)^j.
$$
因为最多 $R_m$ 个强孔及 $j$ 个远孔，(5.1) 恰支付了这些行的原总孔 cut。对 $K_{m,Q_m}$ 相同身份成立。

把 (4.6) 的完整 $H_{C_m,J_m}(s_m)a_m=g_m$ 代入，准确有
$$
\boxed{
P_{V_{m,Q_m}}F_m=P_{V_{m,Q_m}}f,\qquad
P_{K_{m,Q_m}}F_m=P_{K_{m,Q_m}}f.
}
\tag{5.2}
$$
从而
$$
u_{m,Q_m,f}
=(P_{V_{m,Q_m}}-P_{K_{m,Q_m}})f
=(P_{V_{m,Q_m}}-P_{K_{m,Q_m}})F_m.
\tag{5.3}
$$
全部内层顶部及左右两端 partial 仍取自这个同一实际 $u$。本稿没有由 (5.1) 自动取消各内部窗口的原限制。

逐参数令
$$
\Delta_{m,Q,f}^2=\|f\|^2-\|u_{m,Q,f}\|^2.
$$
正交孔层以及 (5.2) 给
$$
\|u_{m,Q,f}\|^2\le\|F_m\|^2\le q_m.
$$
又对 $0\le X\le I$ 有 $X-X^2\le I-X$。因此
$$
\boxed{
0\le\epsilon_m\le\|f\|^2-q_m\le\Delta_{m,Q,f}^2.
}
\tag{5.4}
$$
(4.5) 与 (5.4) 都保留完整中间源 inverse，而非压到 forcing 原有坐标后的逆。

## 6. 原 $R=d$ 窗口内的一次／二次完整 MP 应用

取 (3.5)，因此 $C_m^{2d}=0$、$\|C_m\|\le7$。令
$$
\tau_x=\left(\frac{\log(x+1)}x\right)^{1/3},\qquad
s_m=(1+\tau_x)S_x,\qquad
J_m=\left\lceil\frac{8\log(x+1)}{\tau_x}\right\rceil.
\tag{6.1}
$$
充分大 $m$ 时 $1\le J_m<2d$ 且 $R_m+J_m<4d$。所以可继续选择原 c26 合法的任何
$$
4d\le Q_m\le e^{26d^3}.
\tag{6.2}
$$
新 (4.7) 给 $F_m\to P_Mf$，同时旧一次完整 MP 定理直接用于同一个 $C_m,D_x,a_m,F_m$，得到
$$
\boxed{
\|D_x^\dagger(C_m+D_x)F_m\|^2
\le C_{\rm abs}\tau_x^2\,\epsilon_m
\le C_{\rm abs}\tau_x^2\,\Delta_{m,Q,f}^2.
}
\tag{6.3}
$$
这里因 $\|C_m\|\le7$ 已把旧固定多项式因子吸收入绝对常数。最高截断 top 包含在所引原精确预算中，不被写成零。

同理，取旧二次稿的
$$
\widehat\tau_x=\left(\frac{\log^3(x+1)}x\right)^{1/5},
\qquad
\widehat J_m=\left\lceil\frac{16\log(x+1)}{\widehat\tau_x}\right\rceil,
\qquad s_m=(1+\widehat\tau_x)S_x,
$$
也满足 (4.1)、(5.1)、(6.2)。该相同来源的第一、第二完整顺次 MP 修正仍满足旧平方预算，且现在其原物理 forcing 同时满足新强极限 (4.7)。

(6.3) 的 $D_x^\dagger$ 是完整原算子的 Moore--Penrose inverse；全孔直和可无界，但本稿各输入只占有限个确定层。原连续尾每个固定层已有完整有界右逆，所引一次、二次稿已逐列保其自然域。这里没有将 primitive Gram inverse 代替完整 $D_x^\dagger$。

## 7. 尚未由本比较消去的门

本稿新增的是原强前缀的**真实远尾方差**下的完整 inverse 与 same-$u$ 收敛，尤其覆盖 $R=d$、$h=2d$，并允许所有 $J$ 的统一比较。此前一般强前缀仅由 $s\ge S_m$ 保证的下界，现已在 (3.3) 的明确原 carry 范围内延到 $s\ge S_x$。

它不把任何 $F_m$ 自动改成 $\ker(C_m+D_x)$ 向量。一次修复
$$
F_m-D_x^\dagger(C_m+D_x)F_m
$$
仍留下 $-C_mD_x^\dagger(C_m+D_x)F_m$；二次修复仍有其准确后继项。全部深核旗、帽返回、完整普通右旗和真实中间 Schur 继续保留。

同样，$F_m$ 的零远孔源 $a_m$ 可以占据所有强位；(4.3) 未给它一个可免费用于 MP 或 carry 的孔支持或强收敛速率。原 $K_{m,Q}$ 到全局 $N$ 的母提升仍只在原合法 $Q$ 上使用，(3.4) 不扩大该窗口。本文没有证明 $N=M$。
