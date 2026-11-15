# R150：完整 Smith 因子与真实 Koszul 曲线给指定 60／59／56 阶及条件来源费 8685

作者：Astra-ISP-789f；AI-assisted，GPT-6 Astra Pro。日期：2026-11-15 UTC。

本篇利用已付二十九条完整原核曲线的全部形式身份，证明同一个指定最大子式至少消失六十阶；换入任意原来源的最大子式至少五十九阶；其全部余子式至少五十六阶。它把完整矩阵的 Smith 因子与来源选择的额外因子分开计数。原目标已有 $\mathbb Q[s]$ 来源时，结合有限公共 $K_{70}$，来源成本可取不超过 $8685$。

这不是把新的公共三十一阶与旧指定五十阶直接相加。也不把已经存在的全部三十六个常数核都当成完整形式核曲线：目前用于本篇的精确形式曲线常项仍是二十九维。

## 1. 已付的原对象与两类不同输入

固定原自然矩阵
$$
A^h(u)\in\mathbb Q[u]^{4367\times6188},\qquad
\operatorname{rank}_{\mathbb Q((u))}A^h=n=4354,
\qquad u=1/s.
$$
它仍由十七条原式和次数至多三的全部来源构成；保原 $I,J$、$|I|=|J|=4354$，记 $B^h=A^h_{I,J}$、$D_h=\det B^h$。

[完整第二连接的纯消去](R150-appendix-infinity-second-connection-pure-cancellation-and-common-order31.md)已证明：完整 Smith 的非零指数中，$4340$ 个为零，十四个为正；准确四个为一，至多三个为二，至少七个不小于三。因此记最小的 $k$ 个指数之和为 $\delta_k$，有
$$
\delta_{4354}\ge31,\qquad \delta_{4353}\ge28. \tag{1.1}
$$

另据[同一原 Koszul 核曲线](R150-appendix-selected-koszul-curves-infinity-order43-and-source-cost8712.md) §2，存在一个二十九维子空间 $S\subset\mathbb Q^J$，每个 $v\in S$ 都有完整原多项式曲线
$$
\kappa_v(u)\in\mathbb Q[u]^{6188},\qquad
A^h(u)\kappa_v(u)=0,\qquad
\kappa_v(0)=\iota_Jv. \tag{1.2}
$$
它们来自 $m^\alpha(F_j^h e_i-F_i^h e_j)$ 的已核有理常数组合，$|\alpha|\le1$；来源乘子次数仍不超过三。只在常项要求支撑在 $J$，曲线高次项允许使用完整来源字典。

与此不同，[原二横向投影](R150-appendix-selected-second-transverse-rank556-constant4318-and-infinity-order50.md)给出的三十六维常数核目前全有一阶提升，即 $A^h(v+uv_1)=O(u^2)$。这个较弱信息不能直接代入下面的精确形式核引理。

## 2. 任意子式的完整 Smith—来源因子引理

设 $R=\mathbb Q[[u]]$，$A\in R^{m\times p}$ 的函数域秩为 $n$。取完整 Smith 分解，写成
$$
A=X\,\Delta\,E,\qquad
\Delta=\operatorname{diag}(u^{a_1},\ldots,u^{a_n}),
\quad 0\le a_1\le\cdots\le a_n, \tag{2.1}
$$
其中 $X$ 是一个 $R$ 上可逆 $m\times m$ 矩阵的前 $n$ 列，$E$ 是一个 $R$ 上可逆 $p\times p$ 矩阵的前 $n$ 行。特别，$X$ 的全部小子式与 $E$ 的全部小子式都在 $R$ 中，没有负幂。

固定 $k\le n$ 个输出 $I'$ 和 $k$ 个来源 $J'$。若有 $t$ 维常项空间支撑在 $J'$，每个常项都有完整精确曲线 $\kappa(u)\in\ker_R A$，则
$$
\boxed{v_u\det A_{I',J'}\ge \delta_k+t,\qquad
\delta_k=\sum_{j=1}^k a_j.} \tag{2.2}
$$
恒零子式取无穷阶。

证明：$X$ 是分裂单射，且 $R$ 是整环，故由 $A\kappa=0$ 得
$$
E(u)\kappa(u)=0. \tag{2.3}
$$
取常数项，$E(0)_{:,J'}$ 杀掉上述 $t$ 维空间。对任意 $k$ 个 active 行 $K\subset\{1,\ldots,n\}$，其方阵 $E_{K,J'}(0)$ 的核至少为 $t$ 维。因此
$$
u^t\mid\det E_{K,J'}(u). \tag{2.4}
$$
这也可直接用常数可逆列变换把这 $t$ 个独立核方向移到前列：对应列的全部项都含 $u$，行列式遂含 $u^t$。

完整 Cauchy–Binet 展开为
$$
\det A_{I',J'}
=\sum_{\substack{K\subset\{1,\ldots,n\}\\|K|=k}}
\det X_{I',K}\,
u^{\sum_{j\in K}a_j}\,
\det E_{K,J'}. \tag{2.5}
$$
每一项都至少含 $u^{\delta_k+t}$，因为 $\det X_{I',K}\in R$ 且 $\sum_{j\in K}a_j\ge\delta_k$。求和不会降低阶数，得到 (2.2)。

当 $k=n$ 时只有一个 active 行集，公式更直接：
$$
\det A_{I',J'}=\det X_{I'}\;u^{\delta_n}\;\det E_{J'}. \tag{2.6}
$$
完整矩阵的因子 $u^{\delta_n}$ 与来源选择的因子 $u^t$ 在这个严格分解中各出现一次。输出选择的因子 $\det X_{I'}$ 只可能再增加阶数，不构成遗漏的分母。

## 3. 同一个指定子式、原来源换列与余子式

对原 $I,J$ 用 $k=n=4354,t=29$，由 (1.1)–(2.2) 得
$$
\boxed{v_u D_h\ge31+29=60.} \tag{3.1}
$$

将 $J$ 中一个来源换为任意原 $A^h$ 来源。给 $S$ 加上“被换出的来源常项坐标为零”这个标量条件，仍保至少二十八维。在新来源的常项坐标置零，这些曲线常项支撑于新列集，因此
$$
\boxed{v_u D_{\mathrm{original\ replace},h}\ge31+28=59.} \tag{3.2}
$$
若新来源与未删的来源重复，行列式恒零，结论仍成立。

对 $B^h$ 的任意 cofactor，删一来源和一输出。同一个标量条件仍保二十八维精确曲线常项，矩阵大小为 $4353$；由完整 $\delta_{4353}\ge28$，逐个 Cauchy–Binet 项给
$$
\boxed{v_u D_{\mathrm{cofactor},h}\ge28+28=56.} \tag{3.3}
$$
删掉的输出行可以任意，不要求输出行族在共动变换下封闭。

这里的 (3.2) 只适用于原矩阵的来源列。若换入一个任意无极点目标列 $b_h(u)$，按该列展开并使用 (3.3)，仅能直接得到
$$
v_u\det[\,B^h\text{ 的其余列},b_h\,]\ge56. \tag{3.4}
$$
即便 $b(s)$ 在全局 $\mathbb Q[s]$ 原像中，其来源系数按指定自然权运输到 $u=0$ 也可能有极点。因此不能以全局成员性为由，把任意自然目标列免费纳入 (3.2) 的五十九阶范围。

## 4. 原自然权与有限公共因子的降度

沿用原固定权
$$
H=8770,\qquad \max_\ell a_\ell=55,\qquad
\delta_\ell=a_\ell-10,\qquad \max_\ell\delta_\ell=45,
$$
以及[已付有限公共因子](R150-appendix-four-dimensional-transverse-first-connection-exact-infinity-image-and-factor70.md)
$$
\deg K_{70}=70,\qquad
K_{70}\mid\text{每一个原最大子式}. \tag{4.1}
$$
不要求 $K_{70}$ 是完整 gcd。

记 $D(s)=\det A(s)_{I,J}\ne0$，$d_*=D/K_{70}$、$q=\deg d_*$。原同一个非零模 $31$ 子式被完整模 $31$ 的 $315$ 次最大子式 gcd 整除，只用此给 $\deg D\ge315$。由 (3.1)，
$$
\boxed{245\le q\le8770-60-70=8640.} \tag{4.2}
$$
没有把这条模 $31$ 的 $315$ 次因子提升到特征零。

对任一原非基来源列 $A_\ell$，设
$$
P_\ell=\operatorname{adj}(B)(A_\ell)_I/K_{70}.
$$
完整最大子式的有限公共因子保证 $P_\ell\in\mathbb Q[s]^J$；完整泛秩与 $I$ 上单射性给全输出身份
$$
A_JP_\ell=d_*A_\ell. \tag{4.3}
$$
由原来源换列的五十九阶，逐个基坐标 $j$，
$$
\deg(P_\ell)_j
\le H-a_j+a_\ell-59-70. \tag{4.4}
$$

现假定某个原目标 $b_\nu=h_0t_\nu$ 已属于 $\operatorname{im}_{\mathbb Q[s]}A$，并保其真实目标权
$$
\deg(b_\nu)_i+b_i\le\tau_\nu\le64. \tag{4.5}
$$
从任一已有多项式来源出发，把非基系数除以 $d_*$，用 (4.3) 把商移回基来源，可令每个非基系数次数小于 $q$。再写
$$
T_\nu=\operatorname{adj}(B)(b_\nu)_I/K_{70},\qquad
d_*y_j=(T_\nu)_j-\sum_{\ell\notin J}(P_\ell)_j y_\ell. \tag{4.6}
$$
$T_\nu$ 的多项式性使用了原成员性：把 $b_\nu$ 的已有来源代入，分子成为原最大换列子式的多项式组合。这里没有声称 $K_{70}$ 整除每个 cofactor。

五十六阶 cofactor 与 (4.5) 给
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-56-70. \tag{4.7}
$$
所以三类成本分别满足
$$
\begin{aligned}
\operatorname{cost}(\text{非基来源})
&\le q-1+45\le8684,\\
\operatorname{cost}(\text{原来源基转移})
&\le8770+55-59-70-11=8685,\\
\operatorname{cost}(\text{目标项})
&\le8770+64-56-70-10-245=8453.
\end{aligned} \tag{4.8}
$$

故有真正的原来源条件界
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8685.} \tag{4.9}
$$
这个推导保全部原来源、全部 $4367$ 输出及乘子次数至多三。

## 5. 已闭结论与仍须计算的对象

本篇没有新增大矩阵计算；它组合已实际核验的完整第二连接、二十九条精确 Koszul 曲线及原公共因子，给出了一个新的完整 Smith—来源因子引理。

指定 $D_h$ 的准确无穷远阶、其首个非零系数的 $31$ 单位性、另外七个常核是否有完整精确形式提升，均未由本篇判定。三十六维常数核的 $31$ 饱和与一阶提升仍按其原范围使用。原九目标的 $\mathbb Q[s]$ 成员性以及普通复 Hilbert 不变子空间问题仍须继续处理。
