# R271 附录：原总孔数缺陷与同一真实残量的统一一阶孔矩

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：以下原全算子的数算子交换子、同 forcing 拉通恒等式与真实孔矩已证明。**
对原最低 forcing $f_1=e_1$，本稿使用原完整 $J=1$ Gram 的最小者
$$
a_s=(I+T^*T/s)^{-1}f_1,
\qquad h_s=Ta_s,
\qquad s>0.
$$
这里的 $h_s$ 是原完整 $T$ 的真实残量，不是辅助层，也不是最高 carry 真 $F_0$ 的 $\xi_0$。
所有位都保留。所得总物理孔数一阶矩不依赖任何长前缀 $y$，
但目前只有一阶及其分数阶插值，不能把它们自动指数化成 $\mathscr X_\kappa$ 清除预算。

依赖的原模型身份见
[首位真实小图稿](R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md) §1、
[实际边界指数次数阈值稿](R239-appendix-actual-boundary-range-exponential-degree-threshold.md) §§1--2。
本稿的拉通和能量计算直接证明，不援引未知源正则性。

## 1. 原模型及真正总物理孔数

在 $\ell^2(\mathbb N_0)$ 的原整数基中，令
$$
\mathcal N e_n=\nu(n)e_n,
\qquad
\operatorname{Dom}\mathcal N
=\left\{v:\sum_{n\ge0}\nu(n)^2|v_n|^2<\infty\right\},
$$
其中 $\nu(n)$ 是二进制中 $1$ 的数目。
原物理真空为 $\Omega=e_0$。在有限子集表示中，$E_i$ 删除第 $i$ 个物理位，
所以
$$
[\mathcal N,E_i]=-E_i,\qquad
[\mathcal N,E_i^*]=E_i^*.
\tag{1.1}
$$
这不是旧头 Jordan 辅助分级，也不是 Fock 辅助高度。

原归一化幂和 Cayley 项满足
$$
\mathsf N_i=E_i+\eta_iE_i^*\mathsf N_{i+1},\qquad
\mathsf N_i^2=\eta_i\mathsf N_{i+1},\qquad
\|\mathsf N_i\|=1,
$$
$$
\eta_i=\frac{\alpha_{i+1}}{\alpha_i},\qquad
-\log\eta_i=1400\,16^i-630\,8^i+300\,2^i,
\qquad
0<\eta_i\le\eta:=\eta_0=e^{-1070}.
\tag{1.2}
$$
置 $a_i=(i+1)^{-2}$，$\sum_i a_i<2$，
$$
T_N=\sum_{i\ge0}a_i\mathsf N_i,
\qquad
T_Y=\sum_{i\ge0}a_i\mathsf Y_i,
\qquad
\mathsf Y_i=\mathsf N_i(I+\mathsf N_i)^{-1}.
\tag{1.3}
$$
两级数都是原算子范数收敛的级数。
两个原模型都有
$$
T\Omega=0,\qquad Tf_1=\Omega,\qquad
\mathcal Nf_1=f_1.
\tag{1.4}
$$

## 2. 全部真实 carry 的孔数缺陷

定义
$$
\mathcal B=T+[\mathcal N,T].
\tag{2.1}
$$
先在有限物理核心解释交换子；下面证明它有真实有界延拓，并且
$$
\boxed{
\|\mathcal B_N\|\le4\eta,\qquad
\|\mathcal B_Y\|\le64\eta.
}
\tag{2.2}
$$
所以两个模型均可统一使用 $\delta:=64e^{-1070}$。

迭代 (1.2)，记 $p_{i,0}=1$、
$p_{i,\ell}=\prod_{j=i}^{i+\ell-1}\eta_j$，得到按算子范数收敛的准确展开
$$
\mathsf N_i
=\sum_{\ell=0}^\infty
p_{i,\ell}E_i^*E_{i+1}^*\cdots E_{i+\ell-1}^*E_{i+\ell}.
\tag{2.3}
$$
空创建积按恒等理解。
第 $\ell$ 项恰使原物理孔数改变 $\ell-1$，故
$$
\mathcal B_i:=\mathsf N_i+[\mathcal N,\mathsf N_i]
=\sum_{\ell\ge1}\ell p_{i,\ell}
E_i^*\cdots E_{i+\ell-1}^*E_{i+\ell},
$$
$$
\|\mathcal B_i\|
\le\eta_i\sum_{\ell\ge1}\ell\eta^{\ell-1}
=\frac{\eta_i}{(1-\eta)^2}<2\eta_i.
\tag{2.4}
$$
同时 $[\mathcal N,\mathsf N_i]=-\mathsf N_i+\mathcal B_i$ 的级数也按算子范数收敛。
对 (1.3) 求和即得 N 型的 (2.2)。

对 Y 型令 $R_i=(I+\mathsf N_i)^{-1}$，原界为 $\|R_i\|<3$。
逆的交换子恒等式及 $\mathsf Y_i=I-R_i$ 给
$$
[\mathcal N,\mathsf Y_i]
=R_i[\mathcal N,\mathsf N_i]R_i.
$$
所以准确有
$$
\mathsf Y_i+[\mathcal N,\mathsf Y_i]
=\mathsf N_i^2R_i^2+R_i\mathcal B_iR_i.
\tag{2.5}
$$
第一项不能省掉；它正是完整 Cayley 项的贡献。
由 (1.2)、(2.4)，
$$
\|\mathsf Y_i+[\mathcal N,\mathsf Y_i]\|
\le9\eta_i+18\eta_i=27\eta_i.
$$
故全部 $a_i$ 求和至多 $54\eta<64\eta$，证明 (2.2)。

## 3. 自然闭域与原 resolvent

式 (2.3)--(2.5) 也支付自然域，而非只给一个形式交换子。
有限物理向量是 $\mathcal N$ 的核心；有限位置/有限孔截断在其图范数中稠密。
先对有限和核 (1.1)，再用上述算子范数收敛与 $\mathcal N$ 闭性，得到
$$
T,T^*:\operatorname{Dom}\mathcal N\longrightarrow\operatorname{Dom}\mathcal N,
$$
$$
[\mathcal N,T]=-T+\mathcal B,
\qquad
[\mathcal N,T^*]=T^*-\mathcal B^*.
\tag{3.1}
$$
Y 型的 $R_i$ 同样保域：可先对 $e^{it\mathcal N}\mathsf N_i e^{-it\mathcal N}$
使用 (2.3) 的范数可微性，再对 $(I+\mathsf N_i)^{-1}$ 作逆差恒等式。
其交换子为 $-R_i[\mathcal N,\mathsf N_i]R_i$，给上述真实闭域身份。

置
$$
H=T^*T,\qquad R_s=(H+sI)^{-1},\qquad
Q_s=(TT^*+sI)^{-1}.
$$
由 (3.1)，
$$
[\mathcal N,H]=T^*\mathcal B-\mathcal B^*T
\tag{3.2}
$$
有界。
对 $e^{it\mathcal N}R_se^{-it\mathcal N}$ 使用逆差恒等式，
其范数导数由 (3.2) 给出。
对 $v\in\operatorname{Dom}\mathcal N$ 再取单位群差商，得到
$$
R_s\operatorname{Dom}\mathcal N\subset\operatorname{Dom}\mathcal N,
\qquad
[\mathcal N,R_s]=-R_s[\mathcal N,H]R_s.
\tag{3.3}
$$
因此以下所有 $\mathcal N a_s$、$\mathcal N h_s$ 都在真实 Hilbert 空间中。
这里不依赖先验的指数孔权正则性。

## 4. 原同一最低源的精确拉通身份

定义原 $J=1$ 完整 Gram 源及真实残量
$$
a_s=sR_sf_1=(I+T^*T/s)^{-1}f_1,
\qquad h_s=Ta_s.
\tag{4.1}
$$
它们满足
$$
\|a_s\|\le1,\qquad \|h_s\|\le\frac{\sqrt s}{2}.
\tag{4.2}
$$
后式是标量上界 $s\sqrt\lambda/(\lambda+s)\le\sqrt s/2$ 的谱计算。
又因 $T\Omega=0$ 且 $f_1\perp\Omega$，有 $a_s\perp\Omega$。

由 $(H+s)a_s=sf_1$、$(\mathcal N-I)f_1=0$ 及 (3.2)--(3.3)，
$$
(H+s)(\mathcal N-I)a_s
=-(T^*\mathcal B-\mathcal B^*T)a_s.
$$
另一方面，(3.1) 给
$T(\mathcal N-I)a_s=\mathcal N h_s-\mathcal B a_s$。
因此
$$
\begin{aligned}
\mathcal N h_s
&=(I-TR_sT^*)\mathcal B a_s+TR_s\mathcal B^*h_s\\
&=sQ_s\mathcal B a_s+TR_s\mathcal B^*h_s.
\end{aligned}
$$
即
$$
\boxed{
\mathcal N h_s
=s(TT^*+s)^{-1}\mathcal B a_s
+T(T^*T+s)^{-1}\mathcal B^*h_s.
}
\tag{4.3}
$$
这是原同一个 forcing 的恒等式；没有把原最小者换成另一加权最小化。

同一计算实际上给一个原算子身份。令 $S_s=sT(T^*T+s)^{-1}$，则
$$
\boxed{
[\mathcal N,S_s]+S_s
=sQ_s\mathcal B\,sR_s+TR_s\mathcal B^*S_s,
\qquad
\|[\mathcal N,S_s]+S_s\|\le\frac54\|\mathcal B\|.
}
\tag{4.3a}
$$
左边先在 $\operatorname{Dom}\mathcal N$ 上定义，右边给它的有界延拓。
这不是逐 forcing 的常数；它说明原残量算子的物理降一级缺陷在整个 Hilbert 空间上一致受控。
(4.3) 是把 (4.3a) 作用于准确的 $\mathcal Nf_1=f_1$ 后得到的原源式。

由 $\|sQ_s\|\le1$、$\|TR_s\|\le1/(2\sqrt s)$ 和 (4.2)，得到
$$
\boxed{
\|\mathcal N h_s\|\le\frac54\|\mathcal B\|
\le\begin{cases}
5e^{-1070},&T=T_N,\\
80e^{-1070},&T=T_Y.
\end{cases}
}
\tag{4.4}
$$
这个总物理孔矩对全部 $s>0$ 一致，完全不含新增前缀长度 $y$。

## 5. 一个保正性的完整能量身份

将 $(H+s)a_s=sf_1$ 与 $(\mathcal N-I)a_s$ 配对并取实部，
右端因为 $(\mathcal N-I)f_1=0$ 精确为零。
再用 $T(\mathcal N-I)a_s=\mathcal N h_s-\mathcal B a_s$，得到
$$
\boxed{
s\langle(\mathcal N-I)a_s,a_s\rangle
+\langle\mathcal N h_s,h_s\rangle
=\operatorname{Re}\langle h_s,\mathcal B a_s\rangle.
}
\tag{5.1}
$$
$a_s\perp\Omega$，而非真空物理孔层均满足 $\mathcal N\ge1$，
所以左边两项都非负。
因而，若 $\delta_T$ 取 (2.2) 的对应常数，
$$
\boxed{
s\| (\mathcal N-I)^{1/2}a_s\|^2
+\|\mathcal N^{1/2}h_s\|^2
\le\frac{\delta_T}{2}\sqrt s.
}
\tag{5.2}
$$
其中 $(\mathcal N-I)^{1/2}$ 只在 $\Omega^\perp$ 上按正算子解释。
特别，
$$
\|\mathcal N^{1/2}h_s\|
\le\sqrt{\delta_T/2}\,s^{1/4},
\qquad
\| (\mathcal N-I)^{1/2}a_s\|
\le\sqrt{\delta_T/2}\,s^{-1/4}.
\tag{5.3}
$$
第二式不声称 $a_s$ 自身具有统一的孔矩。

## 6. 全部前缀、分数阶孔矩和实际尾界

对任何真实位集 $I$，其物理数算子 $N_I$ 与 $\mathcal N$ 对角，且
$0\le N_I\le\mathcal N$。
因此 (4.4)、(5.2) 对任何有限旧强前缀 $I=[m,y)$ 的残量也成立，常数不依赖 $y$。
特别可取上一个相对全 $T$ 定理中的 $y\asymp e^{12d^3}$。

对 $0\le\theta\le1$，正算子谱测度的 Hölder 不等式给
$$
\boxed{
\|\mathcal N^\theta h_s\|
\le\left(\frac{\sqrt s}{2}\right)^{1-\theta}
\left(\frac54\delta_T\right)^\theta.
}
\tag{6.1}
$$
故每个严格低于一阶的真实孔矩都以明确速率趋零。
$\theta=1/2$ 可使用 (5.3) 的更锐常数。
对任意整数 $q\ge1$，还可同时取
$$
\boxed{
\|\mathbf1_{\{\mathcal N\ge q\}}h_s\|
\le\min\left\{
\frac{\sqrt s}{2},\
\frac{5\delta_T}{4q},\
\sqrt{\frac{\delta_T}{2q}}\,s^{1/4}
\right\}.
}
\tag{6.2}
$$
这是实际总孔数尾，不是暗对计数、primitive 出生或辅助高度的替代尾。

端点一阶还有无速率的真实收敛。两个原 $T$ 的第一超对角全部非零，
且严格降低整数指标；在每个有限前缀上逐个反解可知，所有有限物理向量都属于 $\operatorname{Ran}T$。
因此 $\overline{\operatorname{Ran}T}=\mathcal H$、$\ker T^*=0$，从而
$$
sQ_s\xrightarrow{\mathrm{strong}}0.
$$
同时 $a_s\to P_Mf_1$，而谱测度上的有界收敛给
$$
\frac{h_s}{\sqrt s}\longrightarrow0.
$$
后式的平方乘子为 $s\lambda/(\lambda+s)^2\le1/4$，在每个 $\lambda\ge0$ 都趋零。
现在在 (4.3) 中，第一项因 $\mathcal B a_s$ 强收敛与 $sQ_s$ 一致有界而趋零；
第二项至多为 $\delta_T\|h_s\|/(2\sqrt s)$，也趋零。
所以准确有
$$
\boxed{\|h_s\|+\|\mathcal N h_s\|\longrightarrow0\qquad(s\downarrow0).}
\tag{6.3}
$$
这是同一个真实残量在原总孔数图范数中的收敛，不仅是每个固定孔层的收敛。
本段没有给一阶端点的速率，也没有从中推出指数孔权收敛。

## 7. 同源范围与仍需补齐的清除

对每个原 $w\in M=\ker T$，
$$
\langle w,a_s\rangle=\langle w,f_1\rangle.
\tag{7.1}
$$
因此以上估计始终针对一个保该配对的实际正则化源。
若通过有限强头原物理列接回同一个 $V_Q/K_Q/u$，
继续使用已付相对全算子比较和原逐列身份；
它们各自的母支持条件、全部 partial 及真实 MP 域不由 (4.3) 删除。

本稿可以替代对 $h_s$ 的旧强前缀一阶孔矩所作的粗 $y$ 估计，
但 (6.1)--(6.2) 不能控制
$\sum_qe^{\kappa q}\|P_qh_s\|$。
尤其，有限个多项式孔矩不产生 $\kappa>2+2\log2$ 的实际右逆输入范数。
将 (4.4) 自动升级成 $\gamma<1/16$ 的指数孔权，或据此声称清除费用只依赖旧 $d$，都不成立。

下一步的具体对象已变成同一个 $h_s$ 的更高物理孔矩或完整指数矩，
其实际源满足 (4.3) 和正身份 (5.1)。
本稿未完成普通 ISP，也未支付最高 carry 真 $F_0$ 在 $S_x$ 的绝对残余。
