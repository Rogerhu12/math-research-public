# R271 附录：同一物理尾的首核参数自由、已付一孔项与完整二孔正铅笔

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿保持原 $C$、物理尾 $D_x$、同一个首头 forcing、全部 $h$ 段以及原 matched / 帽来源。允许首核参数 $s$ 在物理方差 $S_x$ 之外变化，但不改变任何物理权值。代价是一个明确的一远孔项；在固定比例窗内，这个项由已付首核增益控制。真正二远孔费仍保完整跨旗正算子 $\Xi$，并写为一个原正铅笔的边界导数。本文没有用参数自由度证明该边界导数有界，也没有关闭 $N=M$。

内积对第一变量线性。所有正交、MP 和范数均为原 N/Y 的物理 $\ell^2(\mathbb N_0)$ 内积。

依据：

- [偶强段可达核与首头完整第二 Green](R271-appendix-even-strong-prefix-reachable-kernel-and-first-head-second-green-schur.md)；
- [真低链两孔范围与无罚来源](R271-appendix-true-low-chain-two-hole-range-and-unpenalized-return-source.md)，§§2–6；
- [匹配完整 Schur 的首远孔来源](R271-appendix-matched-full-resolvent-first-far-hole-and-native-mean-feedback.md)，§§1–4；
- [整个低旗返回源的跨头 Schur 能量](R271-appendix-complete-low-flag-return-source-and-cross-head-schur-energy-summability.md)，§§3–8；
- [跨头全高度 coherent Bessel](R271-appendix-cross-head-all-height-coherent-bessel-and-same-w-full-energy-summability.md)。

## 1. 不变的原模型与完整头算子

取原合法 $m$、偶数 $R$，记
$$
d=2^m,\qquad x=m+R,\qquad h=d+R,
$$
$$
C=A_m+D_{[m,x)},\qquad C^h=0,\qquad
D=D_x=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2},
$$
$$
S=\sum_{i\ge x}b_i^2,\qquad
\omega_1=D^*\Omega,\qquad
\omega_2=D^{*2}\Omega,\qquad
\sigma_2^2=\|\omega_2\|^2
=2\left(S^2-\sum_{i\ge x}b_i^4\right)>0.
\tag{1.1}
$$
强头有限维。原偶段可达性给
$$
K=\ker C\subset\operatorname{Ran}C,\qquad
Z=\ker C^*\perp K .
$$
定义
$$
P=P_K,\qquad G=(CC^*)^\dagger,\qquad
\Gamma=PG|_K>0,\qquad
\mathcal T=K^\perp\cap\operatorname{Ran}C,\qquad
M_{\mathcal T}=P_{\mathcal T}C^*C|_{\mathcal T}>0.
\tag{1.2}
$$
零维 $\mathcal T$ 按零二次型理解。$C$ 和 $D$ 作用于不同物理因子，并且
$\sum_{i\ge x}b_i<\infty$，故以下所有一、两远孔列都在原有界 $C+D$ 及其伴随的定义域。

原首头为 $f_1=e_1\otimes\Omega$，准确满足
$$
Ce_1=e_0,\qquad e_0\in K,\qquad \|e_0\|=\|e_1\|=1.
$$
本稿不把 $A_m$ 当作按物理孔数或整数标签单降一阶的算子。

对任意 $v\in K$，置
$$
r_v=(I-P)Gv,\qquad
q_v=(C^*)^\dagger r_v,\qquad
Jv=P_{\operatorname{Ran}C^2}q_v,\qquad
t_v=\frac{e_0-v}{S}-\Gamma v .
\tag{1.3}
$$
因为 $Gv\in\operatorname{Ran}C$ 且 $K\subset\operatorname{Ran}C$，
$$
r_v\in\mathcal T.
\tag{1.4}
$$
这里 $J:K\to\operatorname{Ran}C^2$ 是线性算子；$t_v$ 是一个明确的仿射来源。

## 2. 任意首核参数的准确等价来源

首先
$$
k(v)=
(e_1-C^\dagger v)\otimes\Omega
-\frac{e_0-v}{S}\otimes\omega_1
\tag{2.1}
$$
是一个真实核向量：
$$
(C+D)k(v)=0.
$$
确实，$CC^\dagger v=v$、$C(e_0-v)=0$、$D\omega_1=S\Omega$，
所以两个真空项相消，一孔项为零。这个核向量的远孔数至多一，
并没有使用最小范数或 bosonic 替代。

因此 $f_1$ 减去真核后有代表
$$
F_1(v)=C^\dagger v\otimes\Omega
       +\frac{e_0-v}{S}\otimes\omega_1.
\tag{2.2}
$$
以下再作准确低伴随消元。由既有物理正交分解
$$
\ker C^{*2}=Z\oplus^\perp (C^*)^\dagger Z,\qquad
\operatorname{Ran}C
=(C^*)^\dagger Z\oplus^\perp\operatorname{Ran}C^2,
$$
存在唯一 $z_v\in Z$ 使
$$
q_v-Jv=(C^*)^\dagger z_v,\qquad
C^*Jv=r_v-z_v.
\tag{2.3}
$$
逐项展开得到完整恒等式
$$
\boxed{
F_1(v)-F(v)=(C+D)^*\Psi(v),
}
\tag{2.4}
$$
其中
$$
\boxed{
F(v)=t_v\otimes\omega_1+Jv\otimes\omega_2,\qquad
\Psi(v)=(Gv-z_v)\otimes\Omega-Jv\otimes\omega_1 .
}
\tag{2.5}
$$
证明中，右端真空项为 $C^*Gv=C^\dagger v$；
一孔项为
$$
Gv-z_v-C^*Jv=Gv-r_v=\Gamma v;
$$
两孔项为 $-Jv\otimes\omega_2$。
而 (2.2) 中的一孔系数减去 $t_v$ 恰为 $\Gamma v$。
于是
$$
\boxed{f_1-F(v)=k(v)+(C+D)^*\Psi(v).}
\tag{2.6}
$$

这同时保留真实核来源和低伴随来源，不能把两者任意互换。
不同远孔层正交，所以
$$
\boxed{
\|F(v)\|^2=S\|t_v\|^2+\sigma_2^2\|Jv\|^2 .
}
\tag{2.7}
$$

## 3. 原 PV / PK、全左列与全部 h 段不变

先固定原合法母窗口 $Q\ge R+2$。
(2.1) 的总原尾孔数至多 $R+1\le Q$，因此 $k(v)\in K_Q$。
(2.5) 的 $\Psi(v)$ 总原尾孔数至多 $R+1<Q$。
原低 forcing 身份准确给
$$
P_{V_Q}(C+D)^*\Psi(v)=0,\qquad
P_{K_Q}(C+D)^*\Psi(v)=0.
$$
故
$$
\boxed{
(P_{V_Q}-P_{K_Q})f_1=(P_{V_Q}-P_{K_Q})F(v)
\quad\text{对所有 }v\in K.
}
\tag{3.1}
$$
没有把 $P_V$ 或 $P_K$ 移过 $C^*$。

取任一原合法 cut
$$
n\ge2,\qquad n+h+R<Q.
\tag{3.2}
$$
记完整左最小列为 $U_n$，完整右/裸最小列为 $J_{f,n},J_{b,n}$，
$$
L_n=U_n^*U_n,\quad H_n=J_{f,n}^*J_{f,n},\quad
B_n=J_{b,n}^*J_{b,n},
$$
$$
s_{f,n}[F]=(L_n+H_n)^{-1}U_n^*F.
$$
$k(v)$ 的远孔数至多一，故是原左零源；$\Psi(v)$ 的远孔数至多一，
在 $n\ge2$ 时落在真正低伴随零源域。于是
$$
\boxed{
U_n^*f_1=U_n^*F(v),\qquad
s_{f,n}[f_1]=s_{f,n}[F(v)].
}
\tag{3.3}
$$
这保留原全部 $h$ 段，不是以一、两段右链替换完整右链。

令同一个实际 $w\in W$ 给
$$
u=(P_{V_Q}-P_{K_Q})w,\qquad r_n=Cu_n,
$$
$$
\mathcal P_n=(L_n+H_n)^{-1}(H_n-B_n),\qquad
\widetilde v_n=U_n\mathcal P_nr_n .
$$
$\mathcal P_n$ 仍仅在父稿的 $L_n+B_n$ 度量中使用其自伴正收缩性质。
同一个完整 matched 量满足
$$
\begin{aligned}
\mathfrak M_n
&=\langle(H_n-B_n)r_n,s_{f,n}[f_1]\rangle\\
&=\langle\widetilde v_n,F(v)\rangle\\
&=\sqrt S\,\langle\beta_{x,1}\widetilde v_n,t_v\rangle
+\sigma_2\,\langle\beta_{x,2}\widetilde v_n,Jv\rangle .
\end{aligned}
\tag{3.4}
$$
$\beta_{x,j}$ 是原归一 coherent 第 $j$ 远孔读行。
它们作用于整个实际左列；没有假定该列本身是 coherent 塔。

若采用父稿已付 Riordan 参数，并进一步取
$n+2h+R<Q$，则 (3.3) 还准确保持
$$
z_n=(J_{f,n}-J_{b,n})s_{f,n}[f_1],\qquad
\widehat z_n
=P_{\widehat{\mathscr E}_n}K_{n,\mathrm{amb}}^{-*}z_n.
\tag{3.5}
$$
这里保留真正帽外投影及逆伴随，不以环境交换代替它们。

## 4. 在不改物理尾的条件下改变 s

对 $s>0$ 定义
$$
v_s=(I+s\Gamma)^{-1}e_0,\qquad
F_s=F(v_s).
$$
由 $e_0-v_s=s\Gamma v_s$，
$$
\boxed{
t_{v_s}=(s/S-1)\Gamma v_s,\qquad
F_s=(s/S-1)\Gamma v_s\otimes\omega_1
       +Jv_s\otimes\omega_2.
}
\tag{4.1}
$$
特别 $s=S$ 恰恢复已付的纯两孔无罚代表。
$s$ 只是 (2.1) 中真核选择的参数；物理 $b_i,D,S,C$ 全部不变，
也没有增添辅助 mode。

固定 $\lambda>1$，对所有 $s\in[S,\lambda S]$，
$\Gamma$ 的自身正谱演算给
$$
\boxed{
S\|t_{v_s}\|^2
\le(\lambda-1)^2S\|\Gamma(I+S\Gamma)^{-1}e_0\|^2 .
}
\tag{4.2}
$$
这里只使用 $\Gamma$ 与自己的 resolvent 对易；
未要求它与 $G$、$J$ 或下一节的 $\Xi$ 对易。

在已付原 $\tau_{14}$ 跨头序列上，整个低旗增益定理给
$$
\sum_m S_m\|\Gamma_m(I+S_m\Gamma_m)^{-1}e_0\|^2<2.
\tag{4.3}
$
这里先由 $\Gamma$ 的自身谱演算得
$S\|\Gamma v_S\|^2\le q_1-q_0\le q_\ell-q_0$，
其中 $q_j$ 是原首头对相应完整物理核的投影平方范数；
再用已付的 $\sum_m(q_{\ell,m}-q_{0,m})<2$。
因此，任意先于所有 cut 选定的 $s_m\in[S_m,\lambda S_m]$ 都满足
$$
\boxed{\sum_m S_m\|t_{v_{s_m}}\|^2<2(\lambda-1)^2.}
\tag{4.4}
$$
跨头完整 coherent Bessel 的一孔子行另有
$\sum_m\|\beta_{x_m,1}w\|^2\le2\|w\|^2$。
故在同一个固定 $w$ 上，
$$
\boxed{
\sum_m
\left|\sqrt{S_m}\langle\beta_{x_m,1}w,t_{v_{s_m}}\rangle\right|
\le2(\lambda-1)\|w\|.
}
\tag{4.5}
$$
这支付的是新的 primitive 一孔项；没有给二孔项加上同样结论。
若使用变化的 $\lambda_m$，准确条件是
$\sum_m(\lambda_m-1)^2S_m\|\Gamma_mv_{S_m}\|^2<\infty$，
不能将任意增长 $\lambda_m$ 视作已付。

也允许在每个同一模型内先选一个概率测度 $\nu_m$，
支撑于 $[S_m,\lambda S_m]$，再令
$$
\bar v=\int v_s\,d\nu(s),\qquad
\bar F=F(\bar v)=\int F_s\,d\nu(s).
\tag{4.6}
$$
由于 $t_v$ 仿射且测度总质量为一，(2.6)、(3.1)–(3.5) 对 $\bar F$
原样成立。Jensen 不等式给
$$
S\|t_{\bar v}\|^2\le\int S\|t_{v_s}\|^2\,d\nu(s),\qquad
\sigma_2^2\|J\bar v\|^2
\le\int\sigma_2^2\|Jv_s\|^2\,d\nu(s).
\tag{4.7}
$$
选参或平均都须先于全部 $Q/cut$ 配对，不改变同一个实际 $r_n$。

## 5. 二孔部分的完整正算子

定义
$$
E=(I-P)G|_K:K\longrightarrow\mathcal T,\qquad
\boxed{\Xi=J^*J=E^*M_{\mathcal T}^{-1}E\succeq0.}
\tag{5.1}
$$
验证第二式时，令 $q_\flat=Jv$、$p_\flat=C^\dagger q_\flat$。
因 $q_\flat\in\operatorname{Ran}C^2$ 且 $K\subset\operatorname{Ran}C$，
$p_\flat\in\mathcal T$，$Cp_\flat=q_\flat$。
由 (2.3) 与 $Z\perp\mathcal T$，
$$
M_{\mathcal T}p_\flat=Ev.
$$
所以
$$
\|Jv\|^2
=\langle M_{\mathcal T}p_\flat,p_\flat\rangle
=\langle Ev,M_{\mathcal T}^{-1}Ev\rangle.
$$
这保留了原 $\operatorname{Ran}C$ 约束后的完整头逆。

还有一个等价的完整旗表达。置
$$
\mathcal H_{\rm src}=C^*E
=-P_{(\ker C^2)^\perp}C^*\Gamma:K\to(\ker C^2)^\perp.
$$
则
$$
J=(C^{*2})^\dagger\mathcal H_{\rm src},\qquad
\boxed{
\Xi=\mathcal H_{\rm src}^*
       (C^{*2}C^2)^\dagger
       \mathcal H_{\rm src}.
}
\tag{5.2}
$$
原 ad 恒等式还给
$\operatorname{Ran}\mathcal H_{\rm src}
\subset\ker C^{2d-1}\ominus\ker C^2$。
(5.2) 的 inverse 仍在完整强头中取；它没有被换成该低旗的压缩逆。

准确二孔费为
$$
\boxed{
\gamma(s)^2
=\sigma_2^2
\langle (I+s\Gamma)^{-1}e_0,\,
        \Xi(I+s\Gamma)^{-1}e_0\rangle .
}
\tag{5.3}
$$
若用 $ds/(s\log\lambda)$ 平均，则 (4.7) 给
$$
\sigma_2^2\|J\bar v\|^2
\le\frac{\sigma_2^2}{\log\lambda}
\left\langle e_0,\,
\left[\int_S^{\lambda S}
 (I+s\Gamma)^{-1}\Xi(I+s\Gamma)^{-1}\frac{ds}{s}\right]e_0
\right\rangle.
\tag{5.4}
$$
积分是有限维正算子的 Bochner 积分。
非交换的 $\Xi$ 留在两个 resolvent 中间。

## 6. 原正铅笔的边界导数

在 $\operatorname{Ran}C=K\oplus^\perp\mathcal T$ 上令
$$
M=CC^*|_{\operatorname{Ran}C}>0,\qquad
N=P_{\mathcal T}M_{\mathcal T}^{-1}P_{\mathcal T}\succeq0.
$$
对 $s,t\ge0$ 定义
$$
\mathcal Q(s,t)=
\langle e_0,(M+sP+tN)^{-1}e_0\rangle .
\tag{6.1}
$$
完整 Woodbury 恒等式给
$$
(M+sP)^{-1}e_0=G(I+s\Gamma)^{-1}e_0=Gv_s.
\tag{6.2}
$$
因此
$$
\mathcal Q(s,0)=\langle e_0,\Gamma(I+s\Gamma)^{-1}e_0\rangle,
$$
以及
$$
\boxed{
-\partial_t\mathcal Q(s,0)
=\langle Ev_s,M_{\mathcal T}^{-1}Ev_s\rangle
=\gamma(s)^2/\sigma_2^2 .
}
\tag{6.3}
$$
所有 inverse 在这里都作用于有限维严格正空间，故微分合法。
(6.3) 将二孔费识别为同一个原两参数正铅笔的边界导数；
它不是首逆标量 $\mathcal Q(s,0)$ 的 $s$ 导数。
对 $t>0$ 的有限增量也不能未经额外估计替代 $t=0$ 导数。

## 7. 同 w 的平均、非零锚和帽误差

令 $F$ 是上面先选好的 $F_s$ 或 $\bar F$，
$\kappa=\|F\|$。对原同一 cut 集 $\mathcal I$，
设 $N_{\rm cut}=|\mathcal I|$、$n_0=\min\mathcal I\ge2$、
$b_w=\|P_{\{N_> >n_0\}}u\|$。
原完整未来预算与实际 carry 给
$$
e_m=2\eta_m\|w\|+\sqrt{h/N_{\rm cut}}\,b_w,\qquad
\Phi=\frac1{N_{\rm cut}}\sum_{n\in\mathcal I}\mathfrak M_n,
$$
$$
\boxed{
|\Phi-\langle w,F\rangle|\le\kappa e_m,\qquad
|\Phi-\langle w,f_1\rangle|\le e_m.
}
\tag{7.1}
$$
第一式保全部 $h$ 段及其重复计数；第二式保原单位首头锚。
物理配对准确分为
$$
\langle w,F\rangle
=\sqrt S\langle\beta_{x,1}w,t_v\rangle
+\sigma_2\langle\beta_{x,2}w,Jv\rangle .
\tag{7.2}
$$
在 (4.4) 的跨头条件下，第一项已由 (4.5) 绝对可和。
二孔项仍需 (5.3) 或 (5.4) 的实际费用控制。

当采用真正帽门 $n+2h+R<Q$ 和父稿参数时，
因 (3.3) 保持同一个 $s_{f,n}$，
完整核增量可以同时以 $f_1$ 和 $F$ 估计：
$$
\sum_n\lambda_n(s_{f,n})^2\le h\min(1,\kappa^2).
$$
原帽均值附加误差仍不超过
$$
\mathcal C_0^2\frac{h}{N_{\rm cut}}\,
b_w\,\min(1,\kappa).
\tag{7.3}
$$
这里始终保留 (3.5) 的外投影。
不能将未压缩相似伴随或某一远孔范数代替这个真实帽量。

本稿新增的是同一原物理源的可选首核参数及完整二孔正铅笔。
已付 primitive 一孔项不等于已付 $\Xi$；低旗标的源支撑也不等于完整 inverse 的解支撑。
原二孔/高旗费用与 $N=M$ 继续未闭。
