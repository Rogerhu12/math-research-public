# R271 附录：低早孔—增长远孔窗口上的模稳定范围右逆与规范形式读数

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** [原算子乘积窗口右逆](R271-appendix-true-global-anisotropic-low-head-growing-tail-adjoint-readout.md)已给真实 $T$ 的定量局部伴随读数，但其完整 MP 身份不能直接应用于尚未证明平方可和的形式原像。本文在同一乘积窗口上重新实施 [R239 高位实际幂平均](R239-high-bit-averaged-boundary-right-inverses-modulo-stable-range.md)，把该成本准确传到 $N^\perp$ 的规范形式原像。没有假定形式原像属于 Hilbert 空间，也没有将实际值域换成闭包。

## 1. 记号与主结论

固定原 $T=T_N$ 或 $T=T_Y$，保原全局 $B$，令
$$
M=\ker T,\qquad \mathcal N=\overline{BM},\qquad W=M\ominus\mathcal N.
\tag{1.1}
$$
本稿用 $\mathcal N$ 表示稳定范围，以免与远孔数 $N$ 混淆。原已付 $e_0\in\mathcal N$ 仍是以下有限旗论证的输入。

给定非负整数 $s,N$，置
$$
u=N+s+1025,\qquad x=48u,
$$
$$
\Pi=\Pi_{s,N}^{(x)}
=P_{\{\text{前 }x\text{ 位孔数}\le s\}}
 P_{\{\text{位 }i\ge x\text{ 孔数}\le N\}},
$$
$$
\Pi_+=\Pi_{s,N+1}^{(x)}.
\tag{1.2}
$$
沿用前稿常数
$$
S_x=\sum_{i\ge x}(i+1)^{-4},\qquad
\tau_x=\log(7\sqrt{2/S_x}),
$$
$$
\mathcal B_s(x)=(s+3)\sqrt{2/S_x}\,
e^{s\tau_x+\tau_x^{4/3}},\qquad
C^+_{s,N}=(1+C_3e^{-40u^4})\mathcal B_s(x).
\tag{1.3}
$$
这里 $C_3$ 是原模型一次固定的 $\mathscr X_3\to\mathcal H$ 真右逆范数。

**定理。** 对任意整数 $r\ge1$ 和任意要求的位起点，可构造有界映射
$$
\widetilde G:\Pi\mathcal H\longrightarrow\mathcal H
$$
使
$$
\boxed{
T\widetilde G=I_{\Pi\mathcal H},\qquad
\operatorname{Ran}\widetilde G\subseteq\operatorname{Ran}B^r,\qquad
\|\widetilde G\|\le2C^+_{s,N}.
}
\tag{1.4}
$$
对每个有限整数支撑 $v\in\Pi\mathcal H$，令 $Jv$ 为原规范有限三角解，即 $TJv=v$ 且 $(Jv)_0=0$。则
$$
\widetilde Gv-Jv\in\mathcal N.
\tag{1.5}
$$
于是对任意真实 $f\in\mathcal N^\perp$，其规范逐行形式解 $T^*h=f$ 满足
$$
\boxed{
\Pi h=\widetilde G^*f\in\Pi\mathcal H,\qquad
\|\Pi h\|\le2C^+_{s,N}\|f\|.
}
\tag{1.6}
$$
特别，(1.6) 适用于原未知 $w\in W$。对固定 $s$，右侧算子成本的对数为
$$
O_s\!\left(1+(\log(N+2))^{4/3}\right).
\tag{1.7}
$$
这仍只是 (1.2) 的实际位置—孔数窗口，而非全孔层或整个 $h$ 的无权平方和。

## 2. 加一远孔后的同一输入窗口

将前稿定理用于参数 $(s,N+1)$，其 $u$ 和 $x$ 正好是 (1.2)。因此存在同一个实际有界算子
$$
G_+:\mathcal H\longrightarrow\mathcal H,\qquad
TG_+=\Pi_+,\qquad \|G_+\|\le C^+_{s,N}.
\tag{2.1}
$$
$G_+$ 的输入已经乘 $\Pi_+$，完整跨头 carry 已由前稿一次精确修正支付。

取有限位集 $F\subseteq\{i\ge x\}$，其所有位还可高于任意指定起点，并令
$$
n=|F|=2(N+1),\qquad
Q_F=\sum_{j\in F}P_{j,0}.
\tag{2.2}
$$
对 $\Pi\mathcal H$，集合 $F$ 内的孔数至多 $N$，所以
$$
(n-N)I\le Q_F\le nI,\qquad
\|Q_F^{-1}|_{\Pi\mathcal H}\|\le(n-N)^{-1}.
\tag{2.3}
$$
$Q_F$ 及其此处的逆均保持两个截断。每个 $E_j^*$ 只在 $j\ge x$ 新建一孔，故
$$
E_j^*Q_F^{-1}\Pi\mathcal H\subseteq\Pi_+\mathcal H.
\tag{2.4}
$$
这一步保相同的 $x$，没有把早孔数 $s$ 偷换成总孔数 $s+N$。

定义
$$
\boxed{
\widetilde G
=\left.\sum_{j\in F}\mathsf N_jG_+E_j^*Q_F^{-1}
\right|_{\Pi\mathcal H}.
}
\tag{2.5}
$$
这里 $\mathsf N_j=B^{2^j}/d_j$ 是原真实归一化幂，不是纯 $E_j$。每个组合由 (2.1)–(2.4) 保证真实有定义。

## 3. 精确右逆、范数和实际右移值域

R239 的原逐位递推
$$
\mathsf N_j=E_j+\eta_jE_j^*\mathsf N_{j+1}
$$
中，$\mathsf N_{j+1}$ 只作用于更高物理位，故与 $E_j^*$ 交换；再用 $(E_j^*)^2=0$，给出准确等式
$$
\mathsf N_jE_j^*=P_{j,0}.
\tag{3.1}
$$
又因 $T$ 与每个 $\mathsf N_j$ 交换，(2.4) 使
$$
\begin{aligned}
T\widetilde G
&=\sum_{j\in F}\mathsf N_jTG_+E_j^*Q_F^{-1}\\
&=\sum_{j\in F}\mathsf N_jE_j^*Q_F^{-1}\\
&=Q_FQ_F^{-1}=I_{\Pi\mathcal H}.
\end{aligned}
\tag{3.2}
$$
没有高位 carry 余项，亦不要求 $G_+$ 与 $\mathsf N_j$ 交换。

使用 $\|\mathsf N_j\|=\|E_j^*\|=1$，
$$
\|\widetilde G\|
\le\frac{n}{n-N}C^+_{s,N}
=\frac{2(N+1)}{N+2}C^+_{s,N}
<2C^+_{s,N}.
\tag{3.3}
$$
这没有依赖总孔 $s+N$ 的额外因子；平均集合只计远孔。

若每个 $j\in F$ 还满足 $2^j\ge r$，则
$$
\widetilde G
=B^r\left[
\sum_{j\in F}\frac{B^{2^j-r}}{d_j}\,
G_+E_j^*Q_F^{-1}
\right].
\tag{3.4}
$$
括号是有限个有界映射之和，所以 (3.4) 给真正的 $\operatorname{Ran}B^r$ 包含。括号范数无需统一控制；被估计的是完整 $\widetilde G$，其范数仍由 (3.3) 支付。

## 4. 有限旗及模稳定范围的准确运输

为自含，重述需要的实际有限旗论证。令
$$
\mathcal E_r=\ker B^r
=\operatorname{span}\{e_0,\ldots,e_{r-1}\}.
$$
原 $T_N,T_Y$ 的第一超对角都非零，且严格降低整数指标，因而
$$
T\mathcal E_{r+1}=\mathcal E_r.
\tag{4.1}
$$
若 $z\in M\cap\operatorname{Ran}B^r$，取 $y$ 使 $z=B^ry$。交换性给 $Ty\in\mathcal E_r$。由 (4.1) 取 $a\in\mathcal E_{r+1}$ 使 $Ta=Ty$，则
$$
z=B^r(y-a)+B^ra\in B^rM+\mathbb Ce_0\subseteq\mathcal N.
$$
故
$$
\boxed{M\cap\operatorname{Ran}B^r\subseteq\mathcal N.}
\tag{4.2}
$$

现在取有限整数支撑 $v\in\Pi\mathcal H$。其规范 $Jv$ 仍有限整数支撑，所有原 $B$ 权都严格为正，所以 $Jv\in\operatorname{Ran}B^r$。结合 (3.2)、(3.4)，
$$
\widetilde Gv-Jv\in M\cap\operatorname{Ran}B^r\subseteq\mathcal N.
$$
证明 (1.5)。这里不要求 $\operatorname{Ran}B^r$ 闭，也不从一般核包含推断稳定范围已经等于整个核。

## 5. 规范形式原像及合法的局部配对

取实际 $f\in\mathcal N^\perp$。因 $e_0\in\mathcal N$，$f_0=0$；原 R238 的有限三角递推给唯一逐行形式序列 $h$，满足 $T^*h=f$。

对有限整数支撑 $v\in\Pi\mathcal H$，所有规范三角配对都是有限和。按第一变量线性的内积约定，
$$
\langle h,v\rangle
=\langle f,Jv\rangle
=\langle f,\widetilde Gv\rangle.
\tag{5.1}
$$
第二个等号使用 (1.5) 和 $f\perp\mathcal N$。由 (3.3)，此泛函满足
$$
|\langle h,v\rangle|
\le2C^+_{s,N}\|f\|\,\|v\|.
\tag{5.2}
$$
有限整数支撑向量在 $\Pi\mathcal H$ 中稠密，故 Riesz 表示定理给 (1.6)。这个步骤只给实际窗口上的 Hilbert 读数；没有给未知形式 $h$ 擅取全空间伴随。

等价地，若将有限个总孔层上的原规范 $J_q$ 拼接为 $J$，则
$$
(\widetilde G-J)\Pi\mathcal H\subseteq\mathcal N,
$$
因为该窗口总孔数至多 $s+N$，各 $J_q$ 有界，且 $\mathcal N$ 闭。此表述与 (5.1)–(5.2) 相同，但其巨大环境 $\|J\|$ 没有进入新估计。

## 6. 与原未付返回的区别

本稿付清的是前稿尚未声称的一个新条件：对 $f\in\mathcal N^\perp$，即便规范 $h$ 尚未全局平方可和，(1.6) 仍由真实高位幂和有限旗成立。因此这里的形式读数不是把前稿 MP 自然域扩大后的假设。

它仍不意味着：

- 原 $w\in W$ 属于 $\operatorname{Ran}T^*$，或规范 $h$ 属于整个 $\mathcal H$；
- 原返回测试的 $P_{\widehat{\mathscr E}}$、全部零源 Schur 或普通右封口保持 (1.2)；
- 在缺乏统一尾速率时，可以让增长的 $\mathcal B_s(x)$ 任意乘上一个仅知趋零的物理尾；
- 可以将未证明收敛的 $\langle h,Tw\rangle$ 直接写成 $\|w\|^2$。

准确新增量是：原 $N^\perp$ 来源在低早孔—增长远孔窗口上的规范逆模 $\mathcal N$ 成本，由旧全层指数预算降到 (1.7)。后续能量或混合配对仍须保这个真实窗口与同一来源。
