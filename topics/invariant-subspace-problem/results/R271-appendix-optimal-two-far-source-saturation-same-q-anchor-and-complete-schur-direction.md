# R271 附录：同 Q 投影锚、原两远孔最优饱和费与完整 Schur 比较方向

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：下述结论已证明。** 本文在已经构造的同一物理来源族中，允许整个首核参数，而不只选取一个标量 resolvent 参数。准确极小化给出一个完整正算子的有界谱函数。更关键的是：原同 $Q$ 投影直接保留单位首头的非零锚，因此该极小代表的范数不必再乘原未来平均误差。即使只用保守上界 $\kappa_{\rm opt}\le S^{-1/2}$，原 carry 仍使其物理锚误差跨头可和。

所得必要条件只要求最优费用倒数的和有限；若以后证明 $\kappa_{\rm opt,m}^2\le c_m$ 且 $\sum_m c_m^{-1}=\infty$，即可消去相应首头锚，不需要证明费用本身可和。本文尚未给出这个实际费用上界。最后完整核查与已付低旗 Schur 增益的比较方向：现有直接比较提供最优费用的下界，不能反向用它支付最优费用。原高旗 inverse 和帽外投影继续保留，未证明 $N=M$。

内积对第一变量线性。

依据：

- [同物理尾的首核参数自由度与完整二孔正铅笔](R271-appendix-physical-tail-kernel-parameter-freedom-and-complete-two-hole-positive-pencil.md)，§§1–3、5、7；
- [原两孔范围与无罚返回来源](R271-appendix-true-low-chain-two-hole-range-and-unpenalized-return-source.md)；
- [跨头全高度 coherent Bessel 与同 W 完整逆能量](R271-appendix-cross-head-all-height-coherent-bessel-and-same-w-full-energy-summability.md)，§§1–4；
- [完整低旗返回来源与跨头 Schur 增益](R271-appendix-complete-low-flag-return-source-and-cross-head-schur-energy-summability.md)，§§3–4、8；
- [原强尾同一顶部流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)，§2。

## 1. 同一原模型、有限强头和真实低来源

固定原 N/Y 模型及一个 $m\ge10$，记
$$
d=2^m,\quad R\ \text{为偶数},\quad x=m+R,\quad h=d+R,
$$
$$
C=A_m+D_{[m,x)},\qquad C^h=0,\qquad
D=D_x=\sum_{i\ge x}b_iE_i,\quad b_i=(i+1)^{-2}.
$$
$C$ 作用于整个有限强头空间；不将其限制到测试的低孔或低整数头。
$D$ 作用于原无限远尾，与全部强头算子交换。令
$$
S=\sum_{i\ge x}b_i^2,\qquad
\omega_j=(D^*)^j\Omega,\qquad
\sigma_2^2=\|\omega_2\|^2=2\left(S^2-\sum_{i\ge x}b_i^4\right)>0.
\tag{1.1}
$$
远尾所有列均在原 Hilbert 空间中；$D$ 及 $C+D$ 有界。

沿用
$$
K=\ker C\subset\operatorname{Ran}C,\quad Z=\ker C^*\perp K,\quad
P=P_K,\quad G=(CC^*)^\dagger,\quad \Gamma=PG|_K>0,
$$
$$
\mathcal T=K^\perp\cap\operatorname{Ran}C,\qquad
M_{\mathcal T}=P_{\mathcal T}C^*C|_{\mathcal T}>0.
\tag{1.2}
$$
这里所有强头 inverse 都在相应完整有限维空间上。原单位头满足
$Ce_1=e_0$、$e_0\in K$、$\|e_0\|=\|e_1\|=1$；写
$f_1=e_1\otimes\Omega$。

对 $v\in K$ 定义
$$
r_v=(I-P)Gv,\qquad
q_v=(C^*)^\dagger r_v,\qquad
Jv=P_{\operatorname{Ran}C^2}q_v,
$$
$$
t_v=\frac{e_0-v}{S}-\Gamma v,\qquad
F(v)=t_v\otimes\omega_1+Jv\otimes\omega_2.
\tag{1.3}
$$
$J:K\to\operatorname{Ran}C^2$ 为同一完整来源算子。父稿证明
$$
\Xi=J^*J=E^*M_{\mathcal T}^{-1}E,\qquad
E=(I-P)G|_K.
\tag{1.4}
$$
不删去 $\mathcal T$ 的高旗 nuisance。

为使来源检查自含，令
$$
z_v=C^*(q_v-Jv)\in Z,
$$
$$
k(v)=(e_1-C^\dagger v)\otimes\Omega
-\frac{e_0-v}{S}\otimes\omega_1,\qquad
\Psi(v)=(Gv-z_v)\otimes\Omega-Jv\otimes\omega_1.
$$
原准确恒等式是
$$
\boxed{
k(v)\in\ker(C+D),\qquad
f_1-F(v)=k(v)+(C+D)^*\Psi(v).
}
\tag{1.5}
$$
例如 $C(e_1-C^\dagger v)=e_0-v$，而
$D\omega_1=S\Omega$，故第一个式子直接成立。
第二个式子逐远孔 $0,1,2$ 比较；其中
$C^*Jv=r_v-z_v$ 及 $CC^*Gv=v$ 保留原 MP 规范。

$k(v)$ 和 $\Psi(v)$ 的远孔至多一，原 $m$ 后总孔至多 $R+1$；
$F(v)$ 的远孔至多二，原总孔至多 $R+2$。因此在
$$
Q\ge R+2
\tag{1.6}
$$
下，$k(v)\in K_Q$，且原低行定义准确给
$P_{V_Q}(C+D)^*\Psi(v)=P_{K_Q}(C+D)^*\Psi(v)=0$。
所以
$$
\boxed{
P_{\mathscr U_Q}F(v)=P_{\mathscr U_Q}f_1,\qquad
P_{\mathscr U_Q}:=P_{V_Q}-P_{K_Q}.
}
\tag{1.7}
$$
这里使用完整 $V_Q/K_Q$，而非某个仅非零源图。

## 2. 在整个 K 上的唯一最优两行代表

由两个远孔层正交，
$$
\|F(v)\|^2
=\frac1S\|e_0-(I+S\Gamma)v\|^2
+\sigma_2^2\langle v,\Xi v\rangle .
\tag{2.1}
$$
置
$$
A=I+S\Gamma,\qquad T=A^{-1}\Xi A^{-1}\succeq0,\qquad
b=S\sigma_2^2.
\tag{2.2}
$$
本节的 $A$ 仅为严格正源矩阵，不与原头 $A_m$ 混同。
令 $u=Av$，则 (2.1) 准确变成
$$
S^{-1}\|e_0-u\|^2+\sigma_2^2\langle u,T u\rangle .
$$
第一项严格凸，故全部 $K$ 上唯一极小者为
$$
\boxed{
u_{\rm opt}=(I+bT)^{-1}e_0,\qquad
v_{\rm opt}=A^{-1}(I+bT)^{-1}e_0.
}
\tag{2.3}
$$
不需要 $T$ 可逆。记 $F_{\rm opt}=F(v_{\rm opt})$、
$\kappa_{\rm opt}=\|F_{\rm opt}\|$，代入正规方程得
$$
\boxed{
\begin{aligned}
\kappa_{\rm opt}^2
&=\sigma_2^2\langle e_0,T(I+bT)^{-1}e_0\rangle\\
&=\frac1S\left[1-\langle e_0,(I+bT)^{-1}e_0\rangle\right].
\end{aligned}}
\tag{2.4}
$$
因此
$$
\boxed{
0\le\kappa_{\rm opt}^2\le S^{-1},\qquad
\kappa_{\rm opt}^2
\le\sigma_2^2\|J(I+S\Gamma)^{-1}e_0\|^2.
}
\tag{2.5}
$$
后一式只需把 $v=(I+S\Gamma)^{-1}e_0$ 作为候选，此时首远孔项为零。
所以优化不会超过原无罚纯二孔费；它允许重新保留一个共同的首远孔项来降低总费用。

(2.4) 是有界谱函数的真实有限饱和值，不是先前正铅笔的 $t=0$ 导数。
但 $S^{-1}$ 仍可能很大，不能把 (2.5) 本身当作原问题所需的一致费用界。

## 3. 同 Q 投影直接保非零锚，不乘未来平均损失

固定原同一个 $w\in W$，并在原合法母窗中取
$$
u=P_{\mathscr U_Q}w,\qquad
\|u-P_{\{\mathcal N_m\le Q\}}w\|
\le2\eta_m\|w\|,\qquad
\eta_m=e^{-6d^4}.
\tag{3.1}
$$
$\mathcal N_m$ 是原 $m$ 后总物理孔数，(3.1) 是对整个允许 $Q$ 窗的一致界。
由 (1.7)，
$$
\langle u,F(v)-f_1\rangle=0.
$$
再由 (1.6) 的准确支撑，
$$
\langle w,F(v)-f_1\rangle
=\langle P_{\{\mathcal N_m\le Q\}}w-u,F(v)-f_1\rangle.
$$
$f_1$ 在远真空，而 $F(v)$ 只在远孔一、二，故
$\|F(v)-f_1\|^2=1+\|F(v)\|^2$。得到
$$
\boxed{
|\langle w,F(v)\rangle-\langle w,f_1\rangle|
\le2\eta_m\|w\|\sqrt{1+\|F(v)\|^2}.
}
\tag{3.2}
$$
这一步既没有重新选择 $w$，也没有对 cut 另取来源。
它不需要先把 $u_{\le n}$ 换成其 matched 来源。

现在对所有 $m$ 使用原 $\tau_{14}$ 的偶数强前缀和
$$
e^{(25/2)d_m^3}\le x_m\le e^{13d_m^3},\qquad
h_m\le2x_m,\qquad Q_m=d_m^2h_m.
\tag{3.3}
$$
父稿已经核过 $4d_m\le Q_m<e^{14d_m^3}<
e^{(1601/64)d_m^3}$，所以 (3.1) 的母窗及 (1.6) 同时成立。
原积分下界给
$$
S_{x_m}\ge\frac1{3(x_m+1)^3}.
$$
结合 (2.5)，对 $m\ge10$，
$$
\begin{aligned}
2\eta_m\sqrt{1+\kappa_{\rm opt,m}^2}
&\le4e^{-6d_m^4}(x_m+1)^{3/2}\\
&\le8\sqrt2\,
 \exp\left[-6d_m^4+\frac{39}{2}d_m^3\right]\\
&\le e^{-5d_m^4}.
\end{aligned}
\tag{3.4}
$$
最后一步只需
$d_m^4-(39/2)d_m^3\ge\log(8\sqrt2)$，$d_m\ge1024$ 严格满足。
所以
$$
\boxed{
|\langle w,F_{\rm opt,m}\rangle-\langle w,f_1\rangle|
\le e^{-5d_m^4}\|w\|.
}
\tag{3.5}
$$
右侧及其平方均跨 $m$ 可和。这里支付了优化代表的 $S^{-1/2}$ 上界与原 carry 的准确组合，而不是仅作尺度判断。

## 4. 真正两行 Bessel 必要条件与足够的倒数门槛

在第 $m$ 个强头中，把远真空输出识别为强头空间，定义原行
$$
\beta_{m,j}=\frac{D_{x_m}^jP_{\{N_{\ge x_m}=j\}}}{\sigma_{m,j}},
\qquad j=1,2,\qquad \sigma_{m,1}=\sqrt{S_m}.
$$
原跨头全高度定理特别给
$$
\sum_{m\ge m_0}
\left(\|\beta_{m,1}w\|^2+\|\beta_{m,2}w\|^2\right)
\le2\|w\|^2.
\tag{4.1}
$$
这是整行 Hilbert 范数预算，原各强头来源都保留。

写
$$
\mathbf c_m=\big(\sqrt{S_m}\,t_{v_{\rm opt,m}},
             \ \sigma_{m,2}J_mv_{\rm opt,m}\big),
\qquad \|\mathbf c_m\|=\kappa_{\rm opt,m}.
$$
于是
$$
\langle w,F_{\rm opt,m}\rangle
=\langle(\beta_{m,1}w,\beta_{m,2}w),\mathbf c_m\rangle.
$$
对所有 $\kappa_{\rm opt,m}>0$，
$$
\boxed{
\sum_m
\frac{|\langle w,F_{\rm opt,m}\rangle|^2}
     {\kappa_{\rm opt,m}^2}
\le2\|w\|^2.
}
\tag{4.2}
$$

设 $\alpha=\langle w,f_1\rangle\ne0$。
由 (3.5)，存在 $m_1$ 使以后所有物理配对绝对值至少 $|\alpha|/2$。
因此以后 $\kappa_{\rm opt,m}>0$，且
$$
\boxed{
\sum_{m\ge m_1}\kappa_{\rm opt,m}^{-2}
\le\frac{8\|w\|^2}{|\alpha|^2}<\infty.
}
\tag{4.3}
$$
若某个更后面的 $\kappa_{\rm opt,m}=0$，(3.5) 本身已与此锚冲突。

令
$$
\zeta_m=
1-\langle e_0,(I+S_m\sigma_{m,2}^2T_m)^{-1}e_0\rangle\in[0,1].
$$
(4.3) 的准确谱读数是
$$
\boxed{\sum_{m\ge m_1}\frac{S_m}{\zeta_m}<\infty.}
\tag{4.4}
$$
$\zeta_m=0$ 按前一段单独处理，不能除零。

特别，若在无限子列 $\mathcal J$ 上能够证明一个实际上界
$$
\kappa_{\rm opt,m}^2\le c_m,\qquad
\sum_{m\in\mathcal J}c_m^{-1}=\infty,
\tag{4.5}
$$
则相应 $\alpha$ 必须为零。这里 $c_m$ 是标量费用上界；例如对全部充分大的 $m$ 有 $c_m=O(m\log(m+1))$ 已足够；在任意稀疏子列上仍须实际核对倒数和发散。
本稿没有证明原模型满足 (4.5)，也没有用 $\sum_m\kappa_{\rm opt,m}^2<\infty$
这个不必要的更强要求。

## 5. 全部 h 段、matched 平均及真正帽的同一来源

对原 $n\ge2$ 且 $n+h+R<Q$，沿用同一个最小左列 $U_n$、
完整右费 $H_n$、裸右费 $B_n$ 和
$$
s_{f,n}[F]=(L_n+H_n)^{-1}U_n^*F.
$$
(1.5) 的真核项及低伴随项都被 $U_n^*$ 杀掉，所以
$$
U_n^*F(v)=U_n^*f_1,\qquad
s_{f,n}[F(v)]=s_{f,n}[f_1].
\tag{5.1}
$$
这里使用全部 $h$ 段及全部高低零源，不把 $h$ 换成二。

原同 $w$ 的左最小代表记为 $u_{\le n}=U_nr_n$，
matched 向量记为
$$
\mathcal P_n=(L_n+H_n)^{-1}(H_n-B_n),\qquad
\widetilde v_n=U_n\mathcal P_nr_n .
$$
于是原主交叉项准确为
$$
\mathfrak M_n
=\langle(H_n-B_n)r_n,s_{f,n}[f_1]\rangle
=\langle\widetilde v_n,f_1\rangle
=\langle\widetilde v_n,F(v)\rangle.
$$
父稿给
$$
\|\widetilde v_n-u_{\le n}\|\le\|Y_n\|,
\qquad Y_n=(u_{n+1},\ldots,u_{n+h}).
$$
二者之差仍在 $\operatorname{Ran}U_n$，故可同时以 $F(v)$ 和 $f_1$ 配对。
由于 $n\ge2$ 包含 $F(v)$ 的全部远孔支撑，
$$
\boxed{
\begin{aligned}
|\mathfrak M_n-\langle w,F(v)\rangle|
&\le\min(1,\|F(v)\|)\|Y_n\|
       +2\eta_m\|w\|\,\|F(v)\|,\\
|\mathfrak M_n-\langle w,f_1\rangle|
&\le\min(1,\|F(v)\|)\|Y_n\|
       +2\eta_m\|w\|.
\end{aligned}}
\tag{5.2}
$$
因此对同一 cut 集 $\mathcal I$、$N_{\rm cut}=|\mathcal I|$，
全部未来层至多重复 $h$ 次，(5.2) 的 $\|Y_n\|$ 均值可换成
$\sqrt{h/N_{\rm cut}}\,b_w$。
(3.2) 则完全不含这个未来平均项。

若再使用原真帽门 $n+2h+R<Q$，仍准确保持
$$
\widehat z_n
=P_{\widehat{\mathscr E}_n}K_{n,\mathrm{amb}}^{-*}
       \mathcal R_n s_{f,n}[f_1]
=P_{\widehat{\mathscr E}_n}K_{n,\mathrm{amb}}^{-*}
       \mathcal R_n s_{f,n}[F(v)].
$$
未交换或删除外投影。原混合预算仍为
$$
\mathcal C_0^2\frac{h}{N_{\rm cut}}\,b_w\min(1,\|F(v)\|).
\tag{5.3}
$$
(3.3) 可继续取
$Q_m/2\le n\le Q_m-R_m-2h_m-1$；
其 $h_m/N_{\rm cut}\le3/d_m^2$，原全部域和两端 partial 都保持。

## 6. 完整 Ropt 逆，以及与低旗已付费的准确方向

本节不把 (2.4) 的谱函数当作已付低旗增益。
令
$$
\mathcal F_2=\ker C^2,\qquad \mathcal U=\mathcal F_2^\perp,\qquad
M_2=(C^2|_{\mathcal U})^*(C^2|_{\mathcal U})>0,
$$
$$
D_0=-P_{\mathcal U}C^*\Gamma A^{-1}:K\to\mathcal U.
$$
父稿的完整来源式给
$$
T=D_0^*M_2^{-1}D_0.
$$
完整 Woodbury 恒等式于是得到
$$
\boxed{
\kappa_{\rm opt}^2
=\left\langle D_0e_0,
 \left(\sigma_2^{-2}M_2+S D_0D_0^*\right)^{-1}
 D_0e_0\right\rangle.
}
\tag{6.1}
$$
若 $\mathcal U=\{0\}$，该二次型按零处理。
否则括号在整个 $\mathcal U$ 严格正；其 inverse 并未压到 $D_0e_0$ 所在的低旗。

取 $p\ge2d-2$、$p\le h-1$，并写
$$
\mathcal U_p=\mathcal F_{p+1}\ominus\mathcal F_2,\quad
J_0=C|_{\mathcal F_2},\quad T_0=C|_{\mathcal U_p}.
$$
所引低旗稿已经证明 $D_0K\subseteq\mathcal F_{2d-1}\ominus\mathcal F_2$；
因此 $D_0e_0\in\mathcal U_p$。
完整 bosonic 低块 Schur 为
$$
S_{b,p}=
\sum_{j=2}^{p}\frac{(C^j|_{\mathcal U_p})^*(C^j|_{\mathcal U_p})}
                       {j!S^j}
+I_{\mathcal U_p}+T_0^*(SI+J_0J_0^*)^{-1}T_0 .
\tag{6.2}
$$
设
$$
\theta=\frac{\sum b_i^4}{S^2}<1,\qquad
\mathcal R_{\rm opt,p}
=P_{\mathcal U_p}
 (\sigma_2^{-2}M_2+SD_0D_0^*)|_{\mathcal U_p}.
$$
在 $K$ 上，$J_0J_0^*=\Gamma^{-1}$；
在 $K^\perp$ 上 $J_0J_0^*=0$。
因此
$$
S\Gamma^2(I+S\Gamma)^{-2}
\preceq\Gamma(I+S\Gamma)^{-1}
=(SI+J_0J_0^*)^{-1}|_K.
$$
这准确给出
$$
SD_0D_0^*|_{\mathcal U_p}
\preceq T_0^*(SI+J_0J_0^*)^{-1}T_0.
$$
又 $\sigma_2^2=2S^2(1-\theta)$，故
$$
\boxed{
(1-\theta)\mathcal R_{\rm opt,p}\preceq S_{b,p}.
}
\tag{6.3}
$$
正逆序和完整压缩逆比较的方向是
$$
\boxed{
\begin{aligned}
q_{b,p}(f_1)-q_1(f_1)
&=\langle D_0e_0,S_{b,p}^{-1}D_0e_0\rangle\\
&\le\frac1{1-\theta}
 \langle D_0e_0,\mathcal R_{\rm opt,p}^{-1}D_0e_0\rangle\\
&\le\frac{\kappa_{\rm opt}^2}{1-\theta}.
\end{aligned}}
\tag{6.4}
$$
最后一步使用全逆在低子空间上的短缩不小于压缩后取逆。
真实 physical 低旗 Schur 不小于 bosonic Schur，
故真实 $q_p-q_1$ 还不大于 (6.4) 第一行。

所以已付的跨头低旗增益，并不通过 (6.3) 提供
$\kappa_{\rm opt}$ 的所需上界。这一方向和 (6.1) 的完整高旗 inverse
是后续估计必须保留的两个具体对象。

## 7. 当前准确结论

新可用对象是同一原来源上的最优两远孔代表、严格可和的同 $Q$ 锚误差、
实际两行 Bessel 的倒数必要条件，以及保全部 $h$ 段和真帽的来源运输。
后继只需找到足以触发 (4.5) 的原模型费用上界，或直接控制相同配对；
无需先证明费用平方本身可和。

本文没有把 $S^{-1}$ 叫作绝对常数，没有反向使用 (6.4)，
也没有以优化或锚恒等式代替原普通返回、完整高旗 Schur 或 $N=M$。

## 根独立复核记录

/root（OpenAI ChatGPT / GPT-6 Astra Pro，2026-11-16）逐节完整审查：原零/一/二远孔恒等式、严格凸正规方程与$T$可有核的情形均保留；同$Q$锚只用完整真实投影和支撑，$S^{-1/2}$与原carry的数值界已核。跨头预算作用于同一$w$的两行，故非零锚准确迫使费用倒数和有限，而不是费用本身可和。

完整压缩逆比较是 $P_{\mathcal U_p}\mathcal R_{\rm opt}^{-1}|_{\mathcal U_p}\succeq\mathcal R_{\rm opt,p}^{-1}$；与正文$(1-\theta)\mathcal R_{\rm opt,p}\preceq S_{b,p}$合并，只能给已付增益不超过最优费用的倍数。全文没有反用该方向。normal_annihilator 亦已独立全文复核通过。根将倒数和例子的范围明确为全部充分大的$m$，不对任意稀疏子列作无根据的发散断言。实际原费用上界仍须继续。
