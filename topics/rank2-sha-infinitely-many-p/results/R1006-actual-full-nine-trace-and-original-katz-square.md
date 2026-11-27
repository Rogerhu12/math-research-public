# R1006 — 实际 full9、全部54图及原负二 Katz 的精确平方公式

日期：2026-11-27。会话：`Astra-rank2-Sha-0b097461-20261127`。

**已证明；实际规范及原文已交叉核读。** 本篇把 R991/R995/R997 的实际
曲面和54条同源图接到 Hsieh 的一般 Waldspurger 公式；不调用其后加上
square-free 条件的定理。所得常数全部算出。原 Artin 投影、完整
corestriction、width3 的负二阶导数和 $p$ 的两个 Euler 因子均保留。

另须明确一个影响原目标的记号转换：R804 的 $\widehat\psi$ 是
$T_pE$ 的**算术**角色，而 R995/R998 部分式子的帽号采用第一上同调
的**对偶**角色。按 R804 的原算术约定，本篇检测的是 R995 的
$P_-$，外部椭圆曲线取 $e_E^-$。它准确给原 $V_j$；不能把
$e_E^+$ 的另一个混合因子直接叫作已经由 R994 消去的 $\beta_j$。
严格 Chow projectors 本身不变。第11节逐项给出转换。

本篇的结论是**新的明确循环之原最高 AJ 值与原 Katz 值的等价**，
不是原 Katz 值已在无穷多个 $p$ 非零，也不把这个新循环改名为
R854 的旧 canonical 循环。

## 1. 固定规范与结论

沿 R1002 取
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\operatorname{Im}\omega>0,\quad \delta=1+2\omega=i\sqrt3,
$$
$$
E=E_{27}:y^2+y=x^3,\qquad \omega_E=\frac{dx}{2y+1},
\qquad \psi=\psi_{27},\quad \beta_j=\psi\eta_j.
\tag{1}
$$
原 $j=4,10,16$、$H/K$、$[H:K]=18$、$\eta_j$ 完全不改。
令 $\Omega$ 为(1)的 raw CM period，按选定 CM 标号把复周期格写成
$\Omega\mathcal O_K$；选定9挠生成元及必要的单位标号时同时使用此
周期格。令 $\Omega_K=\Omega/(2\pi i)$，并固定 Igusa 平凡化
$$
\omega_E=\Omega_p\omega_{\rm Ig}.
\tag{2}
$$
所有 Katz 函数均采用 R1002 的同一周期和参数约定。

取包含原 $H$、全部306级点及图的有限 Galois 扩张 $L/K$。
第3、4节给出一个具体 CM 点和全部 $3\cdot18$ 条 degree34 同源
$\varphi_i:E\to S_{b_i}$ 及固定系数 $c_i$。循环为 R997 的修正图
$$
\Delta_{\varphi_i}
=\Gamma_{\varphi_i}-34(S_{b_i}\times O_E)-(O_{b_i}\times E).
$$
对每个好分裂 $p=\mathfrak p\bar{\mathfrak p}$，以同一个 CM
ordinary 方向作 R997(30)的实际算子
$$
Z_{j,p,L}^{[p]}
=\sum_i c_i\left(
\Delta_{\varphi_i}-\frac{A_p}{p^2}\Delta_{\varphi_{i,1}}
+\frac1{p^2}\Delta_{\varphi_{i,2}}\right),
\tag{3}
$$
其中 $\varphi_{i,k}=\varphi_{\mathfrak p^k}\varphi_i$，次数为
$34p^k$，$A_p$ 是 $f_{27}=\theta(\psi^2)$ 的原 Hecke 特征值。
CM 子群及这些商同源在 $L$ 上定义；并不需要为(3)任添一个
随 $p$ 改变的完整 $p$ 挠点域。

令 $\mathcal J_{j,p}$ 是先作
$$
e_{\eta_j}\operatorname{Cor}_{L/H},\qquad
e_{\eta_j}=\frac1{18}\sum_{\sigma\in\operatorname{Gal}(H/K)}
\eta_j(\sigma)^{-1}\sigma,
\tag{4}
$$
再按 R997 的完整有限和，以 $\Omega_S\otimes\omega_E$ 求得的
AJ 数值。这里 $\Omega_S=dt/v^2\wedge dx/(2y+x+t)$。
由于 $P_{\rm high}$ 自伴且该微分属于最高部分，在(3)前后加
R995 的完整最高 projector 都不改变此数值。

**定理。** 在以下实际级结构、Whittaker 和微分规范下，有
$$
\boxed{
\mathcal J_{j,p}^{2}
=\iota_p(-486\,\omega\,34^2)\,[L:H]^2\,\Omega_p^2\,
\mathscr K_{p,\mathfrak c}(\nu_j)
\mathscr K_{p,\mathfrak c}(\beta_j),
\qquad \mathfrak c=(34\delta^2).
}
\tag{5}
$$
其中 $\nu_j=\eta_j\psi_0^{-1}\bar\psi_0^2$ 正是原参数。
R1002 已证明第二个 Katz 因子对每个好分裂 $p$ 非零；所有其它
显示的因子也非零。因此
$$
\boxed{\mathcal J_{j,p}\ne0
\quad\Longleftrightarrow\quad
\mathscr K_{p,\mathfrak c}(\nu_j)\ne0.}
\tag{6}
$$
(5)是原完整 $H$ 上的 AJ 有限和规范。若改用原 $K$ 上下降表示的
指定 Artin de Rham 基，须乘第12节显示的非零 Artin 因子，不能
无声把它丢掉。

## 2. 真正的3处向量，及不能省略的投影

采用 Hsieh [H, §1.1] 的全局加性角色：
$\Psi_\infty(x)=e^{2\pi ix}$，所以
$$
\Psi_3(1/3)=\omega^{-1}.
\tag{7}
$$
这与 R991 第3节为局部 Gauss 和另选的
$\Psi_3(1/3)=\omega$ 相反。表示和 $\Lambda$ 不变；只须在本篇
Whittaker 模型中使用(7)，不能把两个加性角色混用。

记 R991 的 $I^+$、$\theta$、$D$、$h$ 为
$$
\theta\begin{pmatrix}a&b\\3c&d\end{pmatrix}=\omega^{b-c},
\quad D=\begin{pmatrix}0&-1\\3&0\end{pmatrix},
\quad h=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\tag{8}
$$
右 $\Lambda$ 型为 $(\theta,D\mapsto i)$。标准左有理群不变、
右平移的 adelization，使经典群角色与右 compact 角色互逆。
因此 $h_\Gamma(\tau)=f_{27}(\tau/3)$ 的经典
$h_\Gamma(\tau+1)=\omega h_\Gamma(\tau)$ 对应右 $\theta^{-1}$，
不能直接把它叫作 $\Lambda$ 型。

设 $W_3^0$ 为标准新向量，$W_3^0(1)=1$。
$\pi_3(\operatorname{diag}(3,1))W_3^0$ 在 identity 经典分量上的
形式为 $3^{-3/2}h_\Gamma$。但其全部 adelic 向量还含另一个
3型，故必须取真实有限投影
$$
w^-:=3^{3/2}e_{\theta^{-1}}
\pi_3(\operatorname{diag}(3,1))W_3^0,
\qquad
e_{\theta^{-1}}=\frac1{243}
\sum_{a\in I^+/(1+9M_2(\mathbf Z_3))}\theta(a)\pi_3(a).
\tag{9}
$$
该求和确合法：被投影向量固定 $1+9M_2(\mathbf Z_3)$，且商的
阶为 $3\cdot3\cdot9\cdot3=243$。

在 identity 经典分量上(9)仍精确为 $h_\Gamma$。证明是把
$I^+$ 的 determinant1 部分模足够高的 $3$ 次幂提升为
$\Gamma_1(3)\subset\mathrm{SL}_2(\mathbf Z)$，使用其经典角色
$\theta$；一般 $I^+$ 元素再乘一个 $1+3\mathbf Z_3$ 中的中心
平方根，该中心角色平凡。故平均的每项都给同一个 $h_\Gamma$。

R991 已辨认 $\pi_3=\mathrm{cInd}_{J}^{G}\Lambda$。
Frobenius reciprocity 和该紧诱导的不可约性表明其 $\Lambda$
线是一维；另一延拓给不等价表示。对 $h$ 共轭可知(9)属于唯一
$(\theta^{-1},D\mapsto-i)$ 线。因此
$$
w^+:=\pi_3(h)w^-
\quad\text{属于 }(\theta,D\mapsto i)\text{ 线}.
\tag{10}
$$
这些规范还能直接确定所需 Kirillov 函数：
$$
w^-(d(a))=3^{3/2}{\bf1}_{1/3+\mathbf Z_3}(a),\qquad
w^+(d(a))=3^{3/2}{\bf1}_{-1/3+\mathbf Z_3}(a).
\tag{11}
$$
确实右 $n(1)$ 的特征 $\omega^{-1}$ 和(7)强迫第一个支撑；
$\operatorname{diag}(1+3\mathbf Z_3,1)$ 不变性使其在该支撑上常数。
identity 分量的 $h_\Gamma=q^{1/3}+\cdots$ 与标准
$W_\infty(d(a))=a^{3/2}e^{-2\pi a}{\bf1}_{a>0}$ 强迫常数
$3^{3/2}$。第二式由 $h$ 得到。

## 3. 合成 $P h$、原 $K$ 分量及真实无穷 CM 点

Hsieh 的标准 torus 嵌入和 normalizer 为
$$
\iota(\omega)=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},\quad
J=\begin{pmatrix}-1&-1\\0&1\end{pmatrix},\quad
P=\begin{pmatrix}1&-1\\1&1\end{pmatrix}.
$$
于是 $P^{-1}\iota(\delta)P=D$。
标准 torus 下使用的3处向量是
$$
W_3=\pi_3(P)w^+=\pi_3(P h)w^-.
\tag{12}
$$
所以相对于 R997 的固定 $h_\Gamma$，真实 finite 点是
$$
g=P h=\begin{pmatrix}-1&-1\\-1&1\end{pmatrix},
\qquad \det g=-2\equiv1\pmod3.
\tag{13}
$$
只用 $P$ 的非平方分量而漏掉 $h$，会重复错翻一次 CM 方向。

为逐项确定级点，使用 [H, §§4.1、4.4] 的 **row/adjugate**
约定：标准行基在复环面上为 $(\omega,1)$，右 $g$ 的级结构作用
为行向量乘 $g'=\det(g)g^{-1}$。取 $u_9$ 为
$E[9]$ 的 $\mathcal O_K/(9)$ 生成元，(13)给实际基
$$
\boxed{((1+\omega)u_9,(\omega-1)u_9).}
\tag{14}
$$
因为 $g'=\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)$。
其 Weil pairing 指数乘 $-2$，故仍在原 $K$ 分量。
矩阵 $\delta$ 在该基中为 $-D$，与 $w^-$ 的全3型一致。
在2、17处取标准 CM 基，再用 CRT 得完整306级结构。

(14)的第二个3挠点为 $(\omega-1)u_3=-\delta u_3$，是
$\ker[\delta]$ 的非零点。故其 $X_1(3)$ 点是 $t=\infty$，
不是 $t=1/24$ 的另一类非 CM 稳定3子群。
在 R991 的三重覆盖 $v^3=t(1-27t)$ 上，它提升到唯一的无穷点。

这也可由真实好模型直接核验。置
$$
z=v/t,\quad r=1/t,\quad z^3=r^2-27r,\quad
x=z^{-2}X,\quad y=z^{-3}Y.
$$
则通用曲面变为
$$
Y^2+zXY+(r-27)Y=X^3.
\tag{15}
$$
无穷纤维 $r=z=0$ 的方程是 $Y^2-27Y=X^3$；
$X=9x_E,Y=-27y_E$ 准确给(1)。此时
$$
\omega_{\rm new}=\frac{dX}{2Y+zX+r-27},\qquad
\omega_{\rm new}|_E=-\frac13\omega_E,
\quad \omega_{\rm old}=z\omega_{\rm new}.
\tag{16}
$$
并且
$$
\Omega_S=-\frac{dr}{z}\wedge\omega_{\rm new},\qquad
r=-z^3/27+O(z^6).
\tag{17}
$$
所以 $\Omega_S$ 在该纤维恰有一阶零；不会把一个在此为零的
weight3 值冒称非零。后文使用的是完整带权商算子及其 raised/负二
值，均在这个好模型上评价或延拓。所有目标同源的微分仍按
$\varphi^*\omega_{\varphi}=\omega_E$ 固定。

## 4. 全部54商图与有限向量的精确对应

对 $q=2,17$，在标准 CM 基上取 $C_{q,0}=\langle u_q\rangle$。
以 $t$ 遍历
$C_{q+1}=\mathbf F_{q^2}^{\times}/\mathbf F_q^{\times}$，定义
$$
C_{q,t}=\bar t C_{q,0},\qquad
c_{q,t}=\chi_{j,q}(t)^{-1},\qquad
\chi_j=\eta_j(\psi N_K^{-1/2})^{-1}.
\tag{18}
$$
这里的共轭是必须的：row/adjugate 约定下右 $\iota(t)$ 对实际
级点的 CM 乘数是 $\bar t$，不是 $t$。因此(18)准确实现 R991
的 $t e_x=e_{tx}$ 与原系数，而没有把系数偷偷取逆。

令 $g_q=d(q^{-1})=\operatorname{diag}(q^{-1},1)$，$W_q^0(1)=1$。
其 adjugate 把格 $(\tau,1)$ 变成 $(\tau,1/q)$，故确为实际商
$E\to E/C_{q,0}$，并保拉回微分等于原微分。
Hsieh(5.1)中的 $|\det g_q|_q^{3/2}$ 给几何 weight3 向量
$$
W_q=q^{3/2}\sum_{t\in C_{q+1}}
\chi_{j,q}(t)^{-1}\pi_q(\iota(t)g_q)W_q^0.
\tag{19}
$$
没有除以 $q+1$。该向量非零：邻点置换模的常数部分被
$A_q=0$ 消去，而其 Steinberg 部分不可约，所有非平凡 torus
角色各出现一次；(18)选中的两个角色都非平凡。

取全部
$$
\varphi_{t,s}:E\longrightarrow E/(C_{2,t}+C_{17,s}),\qquad
c_{t,s}=c_{2,t}c_{17,s}.
\tag{20}
$$
原9级沿这些 degree34 同源运输，再忘至 $\Gamma$，得到(3)的
所有实际目标纤维及图。它们一般不在源的无穷纤维；不删重复
共轭，也不把54项换成球向量。

若 $R_{q,k}$ 表示这一个完整带权商算子在几何 weight $k$ 形式
上的作用，令
$$
V_j=R_{2,3}R_{17,3}h_\Gamma.
\tag{21}
$$
Gauss–Manin/Kodaira–Spencer 对 degree $q$ 同源的自然性，或逐个
Tate 商的 $q$-展开，给
$$
R_{q,k+2}\theta=q\,\theta R_{q,k}.
$$
故 $w=3+2m$ 时
$$
T_m:=R_{2,w}R_{17,w}\theta^m h_\Gamma
=34^m\theta^m V_j.
\tag{22}
$$
例如商 $C=\langle1/q\rangle$ 的几何值为 $q^k f(q\tau)$；
对它求 $\theta$，即直接核得上述因子 $q$。
后文的 $34^{-2}$ 来自(22)，不能把固定 weight3 有限向量当成
weight $-1$ 的商算子而省去它。

## 5. 算术 Artin、$\epsilon(u)$ 和整个权分支的实际 trace

一律令 $\operatorname{rec}_{\rm ar}$ 把素理想 uniformizer 送到
算术 Frobenius。原有限角色满足
$$
\eta_j(\operatorname{rec}_{\rm ar}(u))
=\eta_{j,f}(u)
=\epsilon_2(u_2)^{-1}\vartheta_{l_j}(u_{17})
\quad(u\in\widehat{\mathcal O}_K^{\times}).
\tag{23}
$$
这与主理想公式
$\eta_j((a))=\epsilon_2(a)\vartheta_{l_j}(a)^{-1}$ 互逆，正是
R806(8)–(9)的原约定。

定义 $\epsilon(u)\in\mu_6$ 为 $u_3\bmod3$ 的唯一单位提升。
于是
$$
\psi_f(u)=\epsilon(u),\qquad
\psi((a))=\epsilon(a)^{-1}a.
\tag{24}
$$
有限 idèle 单位分量是 $\epsilon$，不是理想公式中的
$\epsilon^{-1}$。CM 主定理在实际 $E$ 的所有 Tate 模上给
$$
\rho_E(\operatorname{rec}_{\rm ar}(u))
=\epsilon(u)u^{-1}\in\widehat{\mathcal O}_K^{\times}.
\tag{25}
$$
也可直接由 $\ell$-adic avatar
$\rho_{E,\ell}(\operatorname{rec}_{\rm ar}(a))
=\iota_\ell(\psi_f(a))a_\ell^{-1}$ 核定；在好素理想处它给
算术 Frobenius 值 $\psi(\mathfrak q)$，在主全局单位上给1。

使用 R1002 的经典族
$$
m\ge0,\quad m\equiv-2\pmod6,\quad w=3+2m,
\quad \xi_{m,j}=\eta_j^{-1}(\psi N_K^{-1/2})^{-w}.
\tag{26}
$$
向量的右有限特征为 $\xi_{m,j}^{-1}$。在2、3、17处它准确等于
固定的 $\chi_j$，包括 $D/\delta$ 的值 $i$；因为
$w\equiv-1\pmod{12}$，不仅是模3单位指数相同。

由 row/adjugate，(25)对几何级结构的作用对应右
$$
a=\overline{\rho_E(\operatorname{rec}_{\rm ar}(u))}
=\epsilon(u)^{-1}\bar u^{-1}.
$$
所有有限单位的右特征于是给
$$
\begin{aligned}
\xi_{m,j,f}^{-1}(a)
&=\xi_{m,j,f}^{-1}(\epsilon(u)^{-1})
\xi_{m,j,f}^{-1}(\bar u^{-1})\\
&=\epsilon(u)^{-w}\,
\eta_j(u)\epsilon(u)^w
=\boxed{\eta_j(u)}.
\end{aligned}
\tag{27}
$$
这里用了全局主单位关系
$\xi_{m,j,f}^{-1}(\epsilon)=\epsilon^w$，及
$\xi_{m,j,f}^{-1}(N u)=\chi_K(Nu)=1$。
这支付整个权分支的平凡化，不是只在 $m=-2$ 猜一个符号。

由于 $h_K=1$，$\operatorname{Gal}(L/K)$ 中每个元素都可以由
有限单位表示。(27)准确适用于(20)的带权几何和：Galois 作用
在级点、子群、商曲线和同源上，$c_i$ 始终是固定系数。
这不是把 $c_i$ 再作复共轭。$p$-depletion 的三个商也与这些
Galois 作用交换，所以同一等式仍成立。

因此原完整有限和中
$$
\operatorname{Cor}_{L/H}\text{ 给 }[L:H],\qquad
\frac1{18}\sum_\sigma\eta_j(\sigma)^{-1}\eta_j(\sigma)=1.
\tag{28}
$$
所有实际重数均保留，(28)不产生额外18，也不把相反的 $\eta$
投影偷换进来。

## 6. 两个不分歧 inert 位的完整局部常数

以下双线性式及 Haar 测度全按 [H, §§1.1、2.2]：
$$
b_q(W_1,W_2)=\int_{\mathbf Q_q^\times}
W_1(d(a))W_2(d(-a))\chi_{K,q}(a)^{-1}\,d^\times a.
\tag{29}
$$
在 $q=2,17$，Satake 参数为 $1,-1$，故
$$
W_q^0(d(q^n))=
\begin{cases}q^{-n/2},&n\ge0\text{ 为偶数},\\0,&\text{其它},\end{cases}
\quad b_q(W_q^0,W_q^0)=\zeta_q(2)=:b_0.
\tag{30}
$$
令 $u_t=\pi_q(\iota(t)g_q)W_q^0$。由
$b(\pi(g)v,\pi(g)w)=\chi_K(\det g)b(v,w)$，有
$b(u_t,u_t)=-b_0$。又因球 Hecke 特征值为0，
$\sum_tu_t=0$。$\mathrm{GL}_2(\mathbf F_q)$ 在有序异点对上传递，
故所有异点双线性值相同，再对该和配对给
$$
b(u_t,u_s)=b_0/q\quad(t\ne s).
\tag{31}
$$
标准 $J$ 固定参考子群，因为 $g_q^{-1}Jg_q$ 为整可逆矩阵；
并且 $J\iota(t)=\iota(\bar t)J$，所以 $Ju_t=u_{\bar t}$。
令 $v=\sum_t\chi_q(t)^{-1}u_t$。非平凡角色和为0，因而
$$
b(v,Jv)=-b_0(q+1)-\frac{b_0}{q}(q+1)
=-\frac{\zeta_q(2)(q+1)^2}{q}.
\tag{32}
$$
(19)是 $W_q=q^{3/2}v$，而
$$
\operatorname{vol}(K_q^\times/\mathbf Q_q^\times)=1,\qquad
\frac{L(1,\chi_{K,q})}{\zeta_q(1)}=\frac{q-1}{q+1}.
$$
完整局部 toric 积分遂为
$$
\boxed{\mathcal P_q(W_q,W_q,\xi_{m,j,q})=-q^4
\qquad(q=2,17).}
\tag{33}
$$
这个计算保留所有邻点及其系数；没有把“某个 toric 向量非零”
当成实际54图的数值计算。

## 7. Wild3 的相位与完整局部常数

令 $\iota_-(t)=g^{-1}\iota(t)g$，于是 $\iota_-(\delta)=-D$。
直接矩阵乘法给
$$
g^{-1}Jg
=\frac12\begin{pmatrix}-1&-1\\-3&1\end{pmatrix}
=\iota_-(-\omega)h.
\tag{34}
$$
又 $\chi_{K,3}(\det g)=\chi_{K,3}(-2)=1$。
$w^-$ 在 $\iota_-$ 下的特征为 $\chi_{j,3}$，$hw^-$ 的特征为
其共轭，所以(34)引入的相位是
$$
\chi_{j,3}(-\omega^2)=(-\omega^2)^{-1}=-\omega.
\tag{35}
$$
不能把 normalizer 换成裸 $h$ 而删去此相位。

在(11)的支撑上 $\chi_{K,3}(a)=1$，乘法测度为 $1/2$。
因此
$$
b_3(w^-,w^+)=27/2,\qquad
b_3(W_3,JW_3)=-27\omega/2.
\tag{36}
$$
[H, §3.6.3] 的精确测度为
$\operatorname{vol}(K_3^\times/\mathbf Q_3^\times)=2/\sqrt3$；
$L(1,\chi_{K,3})=1$，$\zeta_3(1)=3/2$。故
$$
\boxed{\mathcal P_3(W_3,W_3,\xi_{m,j,3})=-6\sqrt3\,\omega.}
\tag{37}
$$
由(33)、(37)，全部固定有限常数为
$$
\boxed{\mathcal P_2\mathcal P_3\mathcal P_{17}
=-6\sqrt3\,\omega\,34^4.}
\tag{38}
$$
它对三个 $j$ 相同且严格非零。

## 8. 一般 Waldspurger、类数1及全局常数

这里只调用 [H, Proposition2.1] 的一般公式：
$$
P_\xi(\phi)^2
=\Lambda(1/2,\pi_K\otimes\xi)
\prod_{v\in\mathcal S}
\frac{\mathcal P_v(W_v,W_v,\xi_v)}
{L(1/2,\pi_{K,v}\otimes\xi_v)}.
\tag{39}
$$
它允许当前3处 supercuspidal，也允许 CM 的分解 base change。
不借用 [H, §3.5] 之后的 square-free 全局假设。
在2、17处两个 CM 因子都保留原非平凡有限角色；3处的单位指数
分别为 $2m+1\equiv3$、$2m+5\equiv1\pmod6$，也均非平凡。
所以这三个坏位的两个完整局部 $L$ 因子均为1，(38)不另漏
分母中的局部因子；其它未列有限位使用原归一球向量。

所有有限单位上，实际向量均为 $\xi_f^{-1}$ 特征。
普通 $p$ 处取 R1002 的 $p$-depleted Kirillov 函数
${\bf1}_{\mathbf Z_p^\times}$，只需其对 split 单位的这一性质。
无穷处明确取
$$
W_{\infty,m}=\pi_\infty(\varsigma_\infty)
\widetilde V_+^m W_{\infty,3}^{0},\qquad
\varsigma_\infty=
\begin{pmatrix}\sqrt3/2&-1/2\\0&1\end{pmatrix},
\qquad \varsigma_\infty i=\omega,
$$
其中 $W_{\infty,3}^{0}(d(a))=a^{3/2}e^{-2\pi a}{\bf1}_{a>0}$。
令 $\phi$ 为这些局部向量的全局纯张量 realization。
因而 $\phi(1)$ 是原 raised 形式在 $\tau=\omega$ 及已指定有限
级结构的值，包含 $(\operatorname{Im}\omega)^{w/2}$ 的 adelic
因子；不是在 $i$ 点对未平移的 raised 向量求值。
这个平移后的 raised 权 $w$ 与 $\xi_\infty$ 完全抵消。
因为 $h_K=1$，torus 商每个元素可由无穷分量与有限单位表示，
故被积函数在整个 torus 商上恒等于基点值。于是
$$
P_\xi(\phi)=\operatorname{vol}(T,dt)\,\phi(1),\qquad
\operatorname{vol}(T,dt)
=\frac2\pi L(1,\chi_K)=\frac2{3\sqrt3}.
\tag{40}
$$
此处不用另一个只在 cyclic-Heegner 条件下给出的 CM 求和定理。

[H, Proposition3.3] 对 $k=3$ 给
$$
\mathcal P_\infty
=\frac{8\,m!(m+2)!}{(4\pi)^{2m+4}}.
\tag{41}
$$
R1002(18)的两 Katz 因子相乘含
$(2\pi/\sqrt3)^{2m+2}m!(m+2)!$。
取 $\operatorname{Im}\omega=\sqrt3/2$，adelic 值转到原代数微分
值的因子为 $(2\pi i/\Omega)^w(\sqrt3/2)^{-w/2}$。
因此其平方与(41)及 Katz 阶乘/周期相除，精确剩下
$$
\frac{8}{(4\pi)^{w+1}}
\frac{(2\pi i)^{2w}(\sqrt3/2)^{-w}}
{(2\pi/\sqrt3)^{w-1}}
=-\frac4{\sqrt3}.
\tag{42}
$$
$w$ 恒奇；所有随 $m$ 变化的 $\pi$ 和阶乘已消去。
再除以(40)的体积平方，得到 $-9\sqrt3$。
与(38)相乘，完整固定代数常数为
$$
\boxed{C=162\,\omega\,34^4.}
\tag{43}
$$

## 9. 先消去 $p$ 的 Euler 因子，再在 Igusa 塔上延拓

R1002 的两个**完整**经典角色是
$$
\nu_1(m)=\eta_j\psi^{m+1}\bar\psi^{-m},\qquad
\nu_2(m)=\eta_j\psi^{m+3}\bar\psi^{-m-2}.
\tag{44}
$$
其所有有限型已经在那里核定；在 $m=-2$ 精确成为
$\nu_j$ 与 $\beta_j$。

在分裂 $p$ 选第一对角坐标为 $\bar{\mathfrak p}$。这一选择也
与实际 Igusa 级结构相符，而非只是一种局部 $L$ 因子排序：令
$\theta_1=\omega_{\bar{\mathfrak p}}$、
$\theta_2=\omega_{\mathfrak p}$，取
$$
s_p=\frac1{\theta_1-\theta_2}
\begin{pmatrix}\theta_1&\theta_2\\1&1\end{pmatrix}
\in\mathrm{GL}_2(\mathbf Z_p).
$$
它把 $\iota$ 对角化为 $(\bar{\mathfrak p},\mathfrak p)$。
按同一 row/adjugate，第二级点的行向量为
$e_2s_p'=(-1,\theta_1)/(\theta_1-\theta_2)$，经
$p_\omega(a,b)=a\omega+b$ 在这两个分量上恰为 $(0,1)$。
所以它正是 formal $\mathfrak p$ 线的 Igusa 标号，倍率为1；
$\det s_p$ 是 $p$-单位。由此
$\pi_p(s_p)W_p^{[p]}$ 与 R997 的 canonical-subgroup depletion
在同一个 Igusa 点相符，使用的就是(2)，没有另插一个随权变化的
未定 $p$-单位因子。

[H, Lemma3.4、Proposition3.5] 对
$W_p^{[p]}(d(a))={\bf1}_{\mathbf Z_p^\times}(a)$ 的 zeta 积分为1，
其相对完整局部 $L$ 因子的比值准确是
$$
e_{1,p}(m)^2e_{2,p}(m)^2,\qquad
e_{i,p}(m)=1-\nu_i(m)(\bar{\mathfrak p})^{-1}.
\tag{45}
$$
R1002(19)–(20)已逐个核到(45)，其中每个 Katz 角色的两个普通
Euler 因子相等。把(45)与两 Katz 插值公式相除时，它们在每个
经典权先精确抵消。不得把未抵消的 $p^m$ 分别延拓成 $p^{-2}$。

将(39)–(45)全部用**Igusa** 微分表示，得到
$$
\boxed{
\bigl(\theta^m V_j^{[p]}(x_0,\omega_{\rm Ig})\bigr)^2
=\iota_p(C)\,
\mathscr K_{p,\mathfrak c}(\nu_1(m))
\mathscr K_{p,\mathfrak c}(\nu_2(m)).}
\tag{46}
$$
这里 $x_0$ 是第3节的真实 CM 点。经典 Maass–Shimura 值与
$p$-adic $\theta$ 值在 CM 点相容，只用 BDP 的 Lemmas1.5/1.7、
Proposition1.12 的 CM 分裂与微分比较；这些局部比较可拉到完整
级结构，不需要该文全球 Theorem5.13 的 cyclic-ideal 假设。

固定 $p$ 后取
$$
m_n=-2+6(p-1)p^n\longrightarrow-2.
\tag{47}
$$
在 $p$-depleted $q$-展开中只有 $p\nmid n$，且原宽度为3，
故 $(n/3)^{m_n}$ 一致趋于 $(n/3)^{-2}$。
BDP Proposition5.10 证明中使用的整 $q$-expansion principle，
逐项给相同的 Igusa 评值连续性；若有固定分母，先乘一次固定
分母再用该论证。Katz 函数在同一角色分支上连续。
$\psi/\bar\psi$ 在素于 $p$ 的理想上取 $K$ 中的 $p$-单位，
在当前分裂嵌入下其剩余阶整除 $p-1$；有限3型由因子6固定。

因此可以对(46)直接取极限：
$$
\bigl(\theta^{-2}V_j^{[p]}(x_0,\omega_{\rm Ig})\bigr)^2
=\iota_p(C)\,
\mathscr K_{p,\mathfrak c}(\nu_j)
\mathscr K_{p,\mathfrak c}(\beta_j).
\tag{48}
$$
从未单独假定 $\Omega_p^{3+2m_n}$ 连续；它的剩余 Teichmüller
部分不必属于 $\mathbf F_p^\times$。周期已在(46)中全部消去。
只在端点用 weight $-1$ 和(2)，得到
$$
Q_{j,p}:=\theta^{-2}V_j^{[p]}(x_0,\omega_E)
=\Omega_p\theta^{-2}V_j^{[p]}(x_0,\omega_{\rm Ig}).
\tag{49}
$$

## 10. 原 degree34、完整 trace 与(5)的证明

(22)在同一 $p$-depleted 连续族的端点给
$$
R_{2,-1}R_{17,-1}\theta^{-2}h_\Gamma^{[p]}
=34^{-2}\theta^{-2}V_j^{[p]}.
\tag{50}
$$
这里只有有理 $p$-单位34的幂，其沿(47)的连续性没有额外
系数域的剩余阶问题。

R997 已在原曲面上证明 $f_{\Omega_S}=-\delta h_\Gamma$，及每条
实际同源的
$\operatorname{AJ}(\Delta_{\varphi}^{[p]})(\Omega_S\omega_E)
=d_\varphi\theta^{-2}f_{\Omega_S}^{[p]}(x_\varphi)$。
因此完整54项、尚未 trace 的数值为
$$
-34\delta\,R_{2,-1}R_{17,-1}
\theta^{-2}h_\Gamma^{[p]}(x_0,\omega_E)
=-\frac\delta{34}Q_{j,p}.
\tag{51}
$$
此式同时保留了原 $d_\varphi/c_\varphi$：在每个商上使用的微分
恰为 $\omega_{t_b}/c_\varphi$，其拉回是 $\omega_E$。
R997 的 $p^{-2}$ 图系数也已完整保留在(3)，没有用函数的
$A_p/p$ 代替它。

由(27)–(28)，原 $e_\eta\operatorname{Cor}_{L/H}$ 把(51)乘以
$[L:H]$。将(48)、(49)代入，且
$$
\left(-\frac\delta{34}\right)^2C
=\frac{-3}{34^2}\,162\omega34^4
=-486\omega34^2,
$$
即得(5)。$\square$

## 11. 原算术表示是 $P_-$，不是漏掉 dual 的 $P_+$

为消除帽号歧义，令 $\chi_E$ 表示 $T_pE$ 上 $[\delta]=\delta$
一线的算术角色，$\varepsilon$ 为 cyclotomic 角色。于是
$$
\chi_E\bar\chi_E=\varepsilon,\qquad
\chi_E(\operatorname{Frob}^{\rm ar}_{\mathfrak q})
=\psi(\mathfrak q)
\quad(\mathfrak q\nmid3p).
\tag{52}
$$
第一上同调是 Tate 模的对偶。其 $[\delta]^*=\delta$ 线因此为
$\chi_E^{-1}$，另一线为 $\bar\chi_E^{-1}$；不能省略这个逆。
R991 的完整 CM 纯实现比较、并以 holomorphic 线的 Hodge–Tate
型定位，给 $t_2(S)$ 的两线 $\chi_E^{-2},\bar\chi_E^{-2}$。
因此 R995 的 cohomological projectors 满足
$$
\begin{array}{c|c|c}
\text{projector}&H^3\text{ 的算术角色}&H^3(2)\otimes\eta_j^{-1}\\\hline
P_+&\chi_E^{-3}&\eta_j^{-1}\bar\chi_E^3\varepsilon^{-1}\\
P_-&\bar\chi_E^{-3}&\eta_j^{-1}\chi_E^3\varepsilon^{-1}.
\end{array}
\tag{53}
$$
R804(6)、(12)的原角色正是
$$
\boxed{V_j=\eta_j^{-1}\chi_E^2\bar\chi_E^{-1}
=\eta_j^{-1}\chi_E^3\varepsilon^{-1},}
\tag{54}
$$
因为 $\psi_{27}^3=\psi_0^3$，这包括所有有限扭曲。
所以(53)的第二行才是本篇原目标。

在基域与系数域采用同一 $\delta$ 嵌入时，
$\Omega_S\omega_E\in P_+$。由 $P_-^{\rm t}=P_+$，
$$
\mathcal J_{j,p}
=\operatorname{AJ}_p\!\left(
P_-e_{\eta_j}\operatorname{Cor}_{L/H}Z_{j,p,L}^{[p]}
\right)(\Omega_S\omega_E).
\tag{55}
$$
它直接检测(54)。不需要为了把错误的 $P_+$ 标签保住而再把
$\eta$、素位和 full9 分量翻转。若选择另一基域嵌入，仍须按
R811/R997 同时运输 CM 线、原有限角色与素位；本篇没有在
$\mathbf C_p$ 内施加一个虚构的复共轭。

同样修正 R998 第4节的单线使用方向。原来源应取 $e_E^-$；
其另一混合线准确为
$$
\chi_E^{-2}\bar\chi_E^{-1}\varepsilon^2\eta_j^{-1}
=\boxed{\bar\chi_E\eta_j^{-1}}.
\tag{56}
$$
这是 $\beta_j^c$ 的 Tate 中央实现。R998 第1–3节已经用 R994
与 Kato 支付它的完整 Bloch–Kato Selmer 消失。若用该文的
cohomological avatar，(56)写作
$\widehat\beta_j(1)$，因为
$\widehat\beta_j=\chi_E^{-1}\eta_j^{-1}$；两个约定不能混排。

相反，$e_E^+$ 的混合线在**固定算术** $e_{\eta_j}$ 后是
$\chi_E\eta_j^{-1}$，不是(56)，不能仅援引已经证明的
$L(\psi\eta_j,1)\ne0$ 宣布它消失。
R998 的两个完整 $\beta_j$ Selmer 消失定理本体不变；其用于原
有限角色来源的第4节标签须按(52)–(56)更正。

因此对属于原完整 $f$ 条件的新 $e_E^-$ 来源，实际最高投影
$P_-$ 与混合零的论证现在完全一致。任意 $H^1$ 类并不因此
自动满足 $f$ 条件；(55)的非零检测本身也未依赖这个额外断言。

## 12. 原 Artin de Rham 基、范围与后继门槛

(5)/(55)首先是原 $H$ 上完整有限和。将它下降为(54)时，若
原指定 Artin 基写为
$$
a_{j,p}e_{\eta_j^{-1}}\in D_{\rm dR}(\eta_j^{-1}),
\qquad g(a_{j,p})=\eta_j(g)a_{j,p},
$$
则对偶测试基是 $a_{j,p}^{-1}e_{\eta_j}$，相应下降数值为
$$
\mathcal J_{j,p}^{\rm orig}=a_{j,p}^{-1}\mathcal J_{j,p}.
\tag{57}
$$
在 R804 的原 ray 上，其指定共同基为
$a_{j,p}=\sqrt{17}$，所以原 Artin 对偶规范的平方在(5)右侧再
乘 $1/17$。这是明确的非零固定因子；不把 complete finite trace
与一个忽略 Artin 基的局部标量混为同一规范。
本篇 CM 周期使用(1)；与 $E_0$ 微分比较时，R991(37)给最高
三次微分的准确倍率2，不能再任添或删去这个已付的扭曲尺度。

本篇确实完成：真实 full9 级点及其所属分量、真实光滑基点、
全部54图、所有局部常数、完整 $\eta$ trace 与 corestriction、
经典全局公式到负二值的连续延拓、以及原算术 $V_j$ 的正确
单线定位。没有把复高度或复 Rankin 导数非零当作 étale AJ
跨 $p$ 保真性。

仍须继续证明原 $\mathscr K_p(\nu_j)$ 对所需无穷多个不同 $p$
非零，或者寻找能支付同一原目标的新非零输入。(6)将此门槛
放在了一个已经实际构造并完全归一化的新最高图循环上，
没有把该门槛删除。

## 原始来源

- M.-L. Hsieh, *Special values of anticyclotomic Rankin–Selberg
  L-functions*, Documenta Mathematica **19** (2014), 709–767。
  本篇用 §§1.1、2.1–2.3 的一般 Proposition2.1；
  §§3.6–3.7 的 Proposition3.3、Lemma3.4、Proposition3.5；
  §§4.1、4.4–4.5 的 row/adjugate 模问题与几何微分规范；
  §5.1 的 raised operator 比较及印刷页751的 Haar 体积。
  [原文](https://content.ems.press/assets/public/full-texts/serials/dm/19/8965392/online/10.4171-dm-462.pdf)。
- M. Bertolini, H. Darmon, K. Prasanna, *Generalized Heegner cycles
  and p-adic Rankin L-series*, Duke Math. J. **162** (2013),
  1033–1148；Lemmas1.5/1.7、Proposition1.12、Proposition5.10 的
  $q$-expansion 连续性证明。局部 AJ 公式按 R997 已核范围使用，
  不援用不满足假设的全球 Theorem5.13。
  [作者原文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/51.BDP1/paper.pdf)。
- F. Castella, *Katz p-adic L-functions and arithmetic applications*，
  §2.1.2、Theorem2.2.1，原始周期及 Katz 插值依 R1002。
  [作者全文](https://web.math.ucsb.edu/~castella/Katz.pdf)。
- R804、R806、R811、R991、R994、R995、R997、R998、R1002：
  原角色、严格对应、实际局部 AJ 及已经付清的输入。

本篇没有新增数学程序运行，也没有重跑原唯一 Artinian 作业。
