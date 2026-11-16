# R271 附录：真低链的两孔范围约束、完整伴随消去与无罚来源费用

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿继续原首头的完整返回配对。由全左链的第零、第一行，证明其 coherent 一孔、两孔读数分别落在 $\operatorname{Ran}C$、$\operatorname{Ran}C^2$。这使前稿两孔代表中的 $\ker C^*$ 一孔项成为准确的低伴随零源；两孔头列也可投到 $\operatorname{Ran}C^2$。所得费用不大于原正饱和费用，并保同一 forcing、同一完整最小源和真正帽逆伴随。费用本身的原模型上界仍未证明。

内积对第一变量线性。所有头、尾、权和投影均为原 N/Y 的物理 $\ell^2(\mathbb N_0)$ 表示。

依据：

- [偶强段可达核与完整第二 Green](R271-appendix-even-strong-prefix-reachable-kernel-and-first-head-second-green-schur.md)；
- [一孔核消去、物理两孔正 Schur](R271-appendix-first-head-true-one-hole-kernel-elimination-and-two-hole-positive-schur.md)，§§1–6；
- [匹配完整 Schur 的首远孔读数](R271-appendix-matched-full-resolvent-first-far-hole-and-native-mean-feedback.md)，§§1–4；
- [强尾同一顶部源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)，§§2–4。

## 1. 原同源与完整有限头

取偶数 $R$，令
$$
d=2^m,\qquad x=m+R,\qquad h=d+R,\qquad
C=A_m+D_{[m,x)},\qquad C^h=0,
$$
$$
D=D_x=\sum_{i\ge x}b_iE_i,\quad b_i=(i+1)^{-2},\quad
S=\sum_{i\ge x}b_i^2.
$$
令
$$
K=\ker C,\quad Z=\ker C^*,\quad P=P_K,\quad
G=(CC^*)^\dagger,\quad \Gamma=PG|_K.
$$
已付偶段可达性给 $K\perp Z$、$K\subset\operatorname{Ran}C$。
全部头空间有限维，但维数及条件数未作统一估计。

记
$$
\omega_1=D^*\Omega,\qquad \omega_2=D^{*2}\Omega,\qquad
\sigma_2^2=\|\omega_2\|^2=2\left(S^2-\sum_{i\ge x}b_i^4\right)>0.
$$
原首头 $f_1=e_1\otimes\Omega$ 满足 $Ce_1=e_0$、$e_0\in K$。
以下始终使用前稿同一来源
$$
v=(I+S\Gamma)^{-1}e_0,\qquad
r=(I-P)Gv,\qquad
q=(C^*)^\dagger r,\qquad
A=(C^*)^\dagger|_Z.
\tag{1.1}
$$
因为 $r,Z\subseteq K^\perp=\operatorname{Ran}C^*$，有
$C^*q=r$、$C^*Az=z$。
MP 的值域给 $q,AZ\subseteq\operatorname{Ran}C$。

前稿的完整一孔残余代表为
$$
F^{(1)}=C^\dagger v\otimes\Omega+\Gamma v\otimes\omega_1,
\qquad
f_1-F^{(1)}=P_{\mathscr K_1^C}f_1,
\qquad
a_1:=\|F^{(1)}\|^2\le1.
\tag{1.2}
$$
其中 $\mathscr K_j^C=\ker(C+D)\cap\{N_>\le j\}$。
特别 (1.2) 保留了完整一孔 primitive 核，而非只留 coherent 一列。

## 2. 两个准确低伴随零源

对任意 $z\in Z$，
$$
\boxed{
z\otimes\omega_1=(C+D)^*(z\otimes\Omega),
}
\tag{2.1}
$$
以及
$$
\boxed{
Az\otimes\omega_2
=(C+D)^*(Az\otimes\omega_1-z\otimes\Omega).
}
\tag{2.2}
$$
逐项展开即证：$C^*z=0$、$C^*Az=z$，两个一孔项在 (2.2) 中准确抵消。
所有向量均在原 Hilbert 空间；$C$ 有界、$D$ 由 $\sum b_i<\infty$ 有界，
故没有额外未闭定义域。

还存在原物理正交分解
$$
\boxed{
\ker(C^{*2})=Z\oplus^\perp AZ,\qquad
\operatorname{Ran}C=AZ\oplus^\perp\operatorname{Ran}C^2.
}
\tag{2.3}
$$
证明第一式：若 $y\in\ker C^{*2}$，则 $C^*y\in Z$。
因 $Z\subseteq\operatorname{Ran}C^*$，
$y-A(C^*y)\in Z$；又 $AZ\subseteq\operatorname{Ran}C=Z^\perp$，
所以这是完整正交分解。
对第一式取正交补，再使用 $\operatorname{Ran}C=Z^\perp$，得到第二式。
这里用到了真实偶段可达性；没有把一个非单位相似当作物理正交投影。

令
$$
P_{\flat}=P_{\operatorname{Ran}C^2},\qquad
q_{\flat}=P_{\flat}q,\qquad
z_0=C^*(q-q_{\flat})\in Z.
\tag{2.4}
$$
于是 $q-q_{\flat}=Az_0$、$C^*q_{\flat}=r-z_0$。
前稿的一孔代表可直接改为纯两孔代表
$$
F^{(\flat)}=q_{\flat}\otimes\omega_2,
\qquad
\gamma_{\flat}^2=\|F^{(\flat)}\|^2
=\sigma_2^2\|q_{\flat}\|^2,
\tag{2.5}
$$
因为
$$
\boxed{
F^{(1)}-F^{(\flat)}
=(C+D)^*\big[(Gv-z_0)\otimes\Omega-q_{\flat}\otimes\omega_1\big].
}
\tag{2.6}
$$
真空项是 $C^*Gv=C^\dagger v$；
一孔项是 $Gv-z_0-C^*q_{\flat}=\Gamma v$，
所以 (2.6) 完整成立。

由于 (2.5) 只有远两孔，$F^{(1)}\perp F^{(\flat)}$。
对原正饱和参数 $\lambda=\sigma_2^2/S$，
$q^\sharp=(I+\lambda AA^*)^{-1}q$，前稿费用为
$$
\gamma_2^2=\sigma_2^2\langle q,(I+\lambda AA^*)^{-1}q\rangle .
$$
(2.3) 给 $P_{\flat}q^\sharp=q_{\flat}$，从而
$$
\boxed{\gamma_{\flat}^2\le\gamma_2^2.}
\tag{2.7}
$$
这个改进来自 (2.1)–(2.2) 的准确零源，未用大系数项的小范数估计。

## 3. 全左链的范围约束与不变的完整源

固定一个原实际母窗口 $Q\ge R+2$。
(2.6) 括号内的原总尾孔数至多 $R+1<Q$，
所以原 $P_{V_Q}(C+D)^*$ 低 forcing 身份准确杀掉它；
$P_{K_Q}$ 对整个伴随像为零。
同时 (1.2) 的真核差属于 $K_Q$。
因此
$$
\boxed{
(P_{V_Q}-P_{K_Q})f_1
=(P_{V_Q}-P_{K_Q})F^{(1)}
=(P_{V_Q}-P_{K_Q})F^{(\flat)}.
}
\tag{3.1}
$$
没有要求 $P_V$、$P_K$ 或 MP 与 $C^*$ 交换。

取父稿任一合法 cut $n\ge2$、$n+h+R<Q$。
对全左域 $V_n^C$ 中任意向量 $y=(y_0,\ldots,y_n)$，
原两条低行是
$$
Cy_0+Dy_1=0,\qquad Cy_1+Dy_2=0 .
$$
$C$ 与 $D$ 作用不同物理因子，故
$$
Dy_1=-Cy_0,\qquad D^2y_2=C^2y_0.
$$
归一为完整 coherent 读行即
$$
\boxed{
\beta_{x,1}y=-Cy_0/\sqrt S\in\operatorname{Ran}C,\qquad
\beta_{x,2}y=C^2y_0/\sigma_2\in\operatorname{Ran}C^2.
}
\tag{3.2}
$$
这对整个 $V_n^C$ 成立，不只对选定的 coherent 候选。
特别 $P_Z\beta_{x,1}y=0$。
两条行的运算都是原有界 $D$ 在指定物理层上的作用。

保留原全部 $h$ 段最小列
$$
r_n=Cu_n,\quad L_n=U_n^*U_n,\quad
H_n=J_{f,n}^*J_{f,n},\quad B_n=J_{b,n}^*J_{b,n},
$$
$$
s_{f,n}[F]=(L_n+H_n)^{-1}U_n^*F,\qquad
\mathcal P_n=(L_n+H_n)^{-1}(H_n-B_n).
$$
由 (1.2)、(2.6) 以及 $U_n$ 与完整左零源的正交性，
$$
U_n^*f_1=U_n^*F^{(1)}=U_n^*F^{(\flat)}.
\tag{3.3}
$$
因此同一 $s_{f,n}$ 本身不变。
令 $\widetilde v_n=U_n\mathcal P_nr_n$；
$\mathcal P_n$ 仍只在原 $L_n+B_n$ 度量中是已付自伴正收缩。
(3.2) 适用于 $\widetilde v_n$，给
$$
\boxed{
\mathfrak M_n
:=\langle(H_n-B_n)r_n,s_{f,n}[f_1]\rangle
=\sigma_2\langle\beta_{x,2}\widetilde v_n,q_{\flat}\rangle .
}
\tag{3.4}
$$
原 $Z$ 一孔项在这个完整匹配式里准确为零。

由于 (3.1)、$F^{(1)}\perp F^{(\flat)}$，
相同实际投影另有
$$
\|(P_{V_Q}-P_{K_Q})f_1\|^2
\le\frac{a_1\gamma_{\flat}^2}{a_1+\gamma_{\flat}^2}.
\tag{3.5}
$$
若 $\gamma_{\flat}=0$，(3.1) 直接给零投影。
(3.5) 仍不是 $\gamma_{\flat}$ 的上界。

## 4. 这个费用保留的真正头 Schur

(2.3) 给以下全部等价的原度量表达：
$$
q_{\flat}=(C^{*2})^\dagger C^*r,\qquad
\frac{\gamma_{\flat}^2}{\sigma_2^2}
=\min_{\zeta\in Z}\|q+A\zeta\|^2 .
\tag{4.1}
$$
第一个式子由 $C^{*2}q=C^*r$ 与最小值域
$(\ker C^{*2})^\perp=\operatorname{Ran}C^2$ 得到；
第二个式子是 (2.3) 中的正交距离。

更具体地，令
$$
\mathcal T=K^\perp\cap\operatorname{Ran}C,\qquad
M_{\mathcal T}=P_{\mathcal T}C^*C|_{\mathcal T}.
$$
$M_{\mathcal T}$ 在这个有限维空间上严格正。
若 $p_{\flat}=C^\dagger q_{\flat}$，
则 $p_{\flat}\in\mathcal T$：
因 $q_{\flat}\in\operatorname{Ran}C^2$，
可写 $q_{\flat}=Cz$、$z\in\operatorname{Ran}C$；
又 $K\subset\operatorname{Ran}C$，
所以去掉 $P_Kz$ 后仍在 $\operatorname{Ran}C$。
由 $C^*q_{\flat}=r-z_0$、$z_0\in Z\perp\mathcal T$，
$$
M_{\mathcal T}p_{\flat}=P_{\mathcal T}r.
$$
于是
$$
\boxed{
\frac{\gamma_{\flat}^2}{\sigma_2^2}
=\langle P_{\mathcal T}r,M_{\mathcal T}^{-1}P_{\mathcal T}r\rangle .
}
\tag{4.2}
$$
这正是保 $\operatorname{Ran}C$ 约束后的完整头 Schur。
若 $\mathcal T=\{0\}$，按零二次型理解。

也有准确饱和极限
$$
\frac{\gamma_{\flat}^2}{\sigma_2^2}
=\lim_{\rho\to\infty}
\langle q,(I+\rho AA^*)^{-1}q\rangle .
\tag{4.3}
$$
这些表达说明哪些来源确实退出了配对，仍未估计 (4.2)
在原 $m,R$ 及同一 $r=(I-P)Gv$ 上的费用。
尤其未将 $G$ 换成其 primitive 压缩 $\Gamma$。

## 5. 同一个 $w$、全 cut 与纯两孔 Bessel

保持同一个实际 $w\in W$，
$u=(P_{V_Q}-P_{K_Q})w$，以及父稿的
$$
\|u-P_{\mathcal N\le Q}w\|\le2\eta_m\|w\|,\qquad
\|\widetilde v_n-u_{\le n}\|\le\|Y_n\|,
\quad Y_n=(u_{n+1},\ldots,u_{n+h}).
$$
因为 $F^{(\flat)}$ 的原总尾孔数至多 $R+2$，
$$
|\mathfrak M_n-\langle w,F^{(\flat)}\rangle|
\le\gamma_{\flat}\big(\|Y_n\|+2\eta_m\|w\|\big),
$$
$$
|\mathfrak M_n-\langle w,f_1\rangle|
\le\|Y_n\|+2\eta_m\|w\|.
\tag{5.1}
$$
第二式保留原单位首头的非零锚。

在同一 cut 集 $\mathcal I$ 上平均，记 $N=|\mathcal I|$，
$n_0=\min\mathcal I\ge2$、$b_w=\|P_{\{N_> >n_0\}}u\|$，
$$
e=2\eta_m\|w\|+\sqrt{h/N}\,b_w,\qquad
\Phi=N^{-1}\sum_{n\in\mathcal I}\mathfrak M_n.
$$
全部未来层至多重复 $h$ 次，因此
$$
|\Phi-\sigma_2\langle\beta_{x,2}w,q_{\flat}\rangle|
\le\gamma_{\flat}e,\qquad
|\Phi-\langle w,f_1\rangle|\le e.
\tag{5.2}
$$
原参数与 $q_{\flat}$ 先选定，再对所有 cut 使用同一来源。

若 $x_{\ell+1}\ge a(x_\ell+1)$、$a>1$，
前稿的完整两孔 Bessel 常数为
$$
B_2(a)=1+\frac{2\sqrt2\,a^{-3}}{1-a^{-3}}.
$$
在 $\sum_\ell e_\ell^2<\infty$ 时，只有两孔行就给
$$
\boxed{
\left(\sum_{\ell:\gamma_{\flat,\ell}>0}
\frac{|\Phi_\ell|^2}{\gamma_{\flat,\ell}^2}\right)^{1/2}
\le\sqrt{B_2(a)}\,\|w\|
 +\left(\sum_\ell e_\ell^2\right)^{1/2}.
}
\tag{5.3}
$$
故非零首头锚仍要求
$\sum_\ell\gamma_{\flat,\ell}^{-2}<\infty$。
(5.3) 比保留 $Z$ 一孔行的必要费用式更窄，
并未证明原模型违反这个要求。

## 6. 真帽逆伴随仍保持原来源

本节仅在父稿已付 Riordan 正反预算的参数上，
并取更严格的 $n+2h+R<Q$。
记 $\mathcal R_n=J_{f,n}-J_{b,n}$，则 (3.3) 给
$$
z_n=\mathcal R_ns_{f,n}[f_1]
=\mathcal R_ns_{f,n}[F^{(\flat)}],\qquad
\widehat z_n=P_{\widehat{\mathscr E}_n}K_{n,\mathrm{amb}}^{-*}z_n .
$$
没有移动或删掉这个外投影。
原混合恒等式仍准确为
$$
\langle\widehat{\mathcal R}_n(g_{\rm R}(C_s)r_n),\widehat z_n\rangle
-\mathfrak M_n
=\langle K_{n,\mathrm{amb}}J_{b,n}r_n,\widehat z_n\rangle .
$$
完整核增量可分别用 $f_1$ 与同一个 $F^{(\flat)}$：
$$
\sum_n\lambda_n(s_{f,n}[f_1])^2\le h\min(1,\gamma_{\flat}^2),
\qquad
\sum_n\alpha_n(r_n)^2\le hb_w^2.
$$
因此帽均值误差不超过
$$
\mathcal C_0^2\frac hN\,b_w\min(1,\gamma_{\flat}).
\tag{6.1}
$$
归一后的整行 (5.3) 只需把 $e_\ell$ 增加
$\mathcal C_0^2(h_\ell/N_\ell)b_{w,\ell}$，并明确要求这个总误差平方可和。
全部 $h$ 段、完整左右零源与两端 partial 均继续保留。

当前剩余目标是 (4.2) 对原 $C_m,r_m$ 的真实费用控制。
本稿没有以纯两孔代表、相同帽源或 Bessel 必要条件代替这一目标，
也没有证明 $N=M$。
