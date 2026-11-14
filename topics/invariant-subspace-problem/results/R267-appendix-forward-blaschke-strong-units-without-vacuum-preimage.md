# R267 第三附录：前向 Blaschke 块的收缩强单位与无真空原像

日期：2026-11-13（UTC）。作者：normal_states；Astra-ISP-1cf8c51d 复核。AI-assisted，GPT-6 Astra Pro。

**状态：完整证明的中间结果。** 本文构造原 Haar 模型中的非零交换子 $P$，以及同一组有界代数逆积 $W_n\in\mathcal A$，使 $PW_n$ 全为收缩且强趋 $I$，但 $1\notin\operatorname{Ran}P$。这说明 R244 的原始指定配对正则器范围严格大于其“真空有原像”的聚合逆图接口。本文没有为假想慢符号正常湮灭者证明指定配对条件，也没有给 $P=S R$ 或普通 ISP 的解。

## 1. 实际表示与局部比较

沿用原 Haar 空间 $H=L^2(\mathbb Z_2)$、真空 $1$、Walsh 基 $\chi_F$ 和
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},
\qquad
V_j=(I-N_j)(I+N_j)^{-1},
\qquad
V_j^0=I-2E_j.
$$
已证真实关系为
$$
V_F1=\chi_F,\qquad
\|V_j\|\le6,\qquad
\|V_j-V_j^0\|\le8\eta_j,
\qquad
\eta_j\le e^{-770\,16^j}.
\tag{1.1}
$$
$A$ 拟幂零，$1$ 对 $\mathcal A$ 循环；$A'$ 交换。对有限 Walsh 向量
$u=\sum_F\widehat u(F)\chi_F$，记
$$
X_u=\sum_F\widehat u(F)V_F\in\mathcal A.
$$
于是 $X_u1=u$。

设 $u$ 仅依赖 $q$ 个位组成的块 $F$，其最小位为 $m$。对应纯局部乘子为
$X_u^0=\sum_{J\subset F}\widehat u(J)V_J^0$。逐项望远镜及 Cauchy--Schwarz 给
$$
\begin{aligned}
\|X_u-X_u^0\|
&\le \sum_{J\subset F}|\widehat u(J)|
\,8q6^{q-1}e^{-770\,16^m}\\
&\le 8q6^{q-1}2^{q/2}\|u\|\,e^{-770\,16^m}.
\end{aligned}
\tag{1.2}
$$
以下只需 $\|u\|\le1$，统一采用更宽的误差预算
$$
\varepsilon(F)=32q9^q e^{-770\,16^m}.
\tag{1.3}
$$
这是真实算子范数差，不是把有限柱压缩当作乘法同态。

对依赖互不相交有限位块的 $u_1,\ldots,u_n$，准确有
$$
X_{u_1}\cdots X_{u_n}1=u_1\cdots u_n.
\tag{1.4}
$$
证明只需展开有限 Walsh 和：不同块的集合不相交，
$V_{J_1}\cdots V_{J_n}1=\chi_{J_1\cup\cdots\cup J_n}$。
本文只在真空列上使用 (1.4)，不声称整个实际乘子代数是普通点乘代数。

## 2. 纯前向 Blaschke 块的统一真空估计

在 $q$ 位纯空间上设
$$
D_q=\sum_{j=1}^qE_j,\qquad
T_q=\frac{2}{q+2}D_q,\qquad
\Omega=\Omega_+^{\otimes q}.
$$
$T_q^{q+1}=0$，且
$$
\|T_q\|\le\frac{q+1}{q+2}<1.
\tag{2.1}
$$
例如按孔数层分解，$D_q$ 在相邻层间的范数为
$\sqrt{(k+1)(q-k)}$；最大值至多 $(q+1)/2$。

给任意实数 $0<a<1$，定义
$$
R_{q,a}^0=(aI+T_q)(I+aT_q)^{-1},
\qquad
r_{q,a}=R_{q,a}^0\Omega.
\tag{2.2}
$$
准确缺陷恒等式为
$$
I-(R_{q,a}^0)^*R_{q,a}^0
=(1-a^2)(I+aT_q^*)^{-1}(I-T_q^*T_q)(I+aT_q)^{-1}\ge0.
\tag{2.3}
$$
故 $R_{q,a}^0$ 为收缩。

置
$$
Z=I-T_q,\qquad
c=\frac{1-a}{1+a},\qquad
d=\frac{a}{1+a}<\frac12.
$$
纯 Walsh 列直接给
$$
Z\Omega=\frac{2\Omega+\sum_{j=1}^q\chi_j}{q+2},
\qquad
Z^*\Omega=\frac{2\Omega-\sum_{j=1}^q\chi_j}{q+2},
$$
所以
$$
\|Z\Omega\|=\|Z^*\Omega\|=\frac{\sqrt{q+4}}{q+2},
\qquad
\langle Z\Omega,\Omega\rangle=\frac2{q+2}.
\tag{2.4}
$$

第一种恒等式
$$
R_{q,a}^0-I=-(1-a)(I+aT_q)^{-1}Z
$$
以及
$\|(1-a)(I+aT_q)^{-1}\|\le(1-a)/(1-a\|T_q\|)\le1$
给出全参数统一界
$$
\boxed{
\|r_{q,a}-\Omega\|
\le\frac{\sqrt{q+4}}{q+2}<q^{-1/2}.
}
\tag{2.5}
$$

为了控制无限乘积的均值，使用二阶展开
$$
R_{q,a}^0-I
=-cZ(I-dZ)^{-1}
=-cZ-cdZ^2(I-dZ)^{-1}.
\tag{2.6}
$$
因为 $\|Z\|\le2$，
$$
\|(I-dZ)^{-1}\|\le\frac1{1-2d}=\frac1c.
$$
$Z$ 与其预解式交换，故
$$
\begin{aligned}
|\langle r_{q,a}-\Omega,\Omega\rangle|
&\le \frac{2c}{q+2}
+cd\|(I-dZ)^{-1}\|\|Z\Omega\|\|Z^*\Omega\|\\
&\le \frac2{q+2}+\frac12\frac{q+4}{(q+2)^2}
<\frac3q.
\end{aligned}
\tag{2.7}
$$
$r_{q,a}$ 是实向量，故均值 $\mu_{q,a}$ 为实数。对 $q\ge8$，
$$
1-\frac3q\le\mu_{q,a}\le1,\qquad
0\le1-\|r_{q,a}\|^2\le\frac6q.
\tag{2.8}
$$
右侧范数亏损由
$\|r_{q,a}\|^2\ge\mu_{q,a}^2\ge1-6/q$ 得到。
(2.5)--(2.8) 对整个区间 $0<a<1$ 统一，参数趋零不会破坏这些前向估计。

## 3. 同一纯块的逆真空可以任意大

$R_{q,a}^0$ 可逆。其逆为
$$
U_{q,a}^0=(I+aT_q)(aI+T_q)^{-1}
=aI+(1-a^2)(aI+T_q)^{-1}.
\tag{3.1}
$$
因 $T_q^{q+1}=0$，
$$
a^{q+1}U_{q,a}^0\Omega
=a^{q+2}\Omega
+(1-a^2)\sum_{k=0}^q(-1)^ka^{q-k}T_q^k\Omega
\longrightarrow(-1)^qT_q^q\Omega
\quad(a\downarrow0).
\tag{3.2}
$$
而
$$
T_q^q\Omega
=\left(\frac2{q+2}\right)^q q!\,2^{-q/2}e_1^{\otimes q}\ne0.
$$
因此对每个固定 $q$，
$$
\boxed{\|U_{q,a}^0\Omega\|\longrightarrow\infty\quad(a\downarrow0).}
\tag{3.3}
$$
这只使用一个有限块的准确 Laurent 展开，不通过全空间谱半径推断向量增长。

## 4. 递归选择参数与真实提升

取
$$
q_\nu=2^{\nu+6},\qquad \nu=1,2,\ldots,
\qquad
\sum_{\nu\ge1}\frac1{q_\nu}=\frac1{64}.
\tag{4.1}
$$
由 (3.3)，可为每个 $\nu$ 选
$$
0<a_\nu<2^{-\nu},\qquad
\|U_{q_\nu,a_\nu}^0\Omega\|\ge3\nu.
\tag{4.2}
$$
记
$$
M_\nu=\|U_{q_\nu,a_\nu}^0\|<\infty.
$$
再递归选互不交且依次后移的实际位块
$F_\nu=[m_\nu,m_\nu+q_\nu)$，使
$$
\varepsilon_\nu
:=32q_\nu9^{q_\nu}e^{-770\,16^{m_\nu}}
\le
\min\left\{
2^{-\nu}q_\nu^{-2},\,\frac1{4M_\nu}
\right\}.
\tag{4.3}
$$
每次只有有限个条件，故可以选到有限整数 $m_\nu$。
纯块参数先选，位位置随后根据其完整逆范数选择；没有忽略逆条件数。

纯有限代数的 $\Omega$ 循环，维数与局部空间同为 $2^{q_\nu}$，故 $u\mapsto X_u^0$ 是准确逆识别；特别 $X_{r_{q_\nu,a_\nu}}^0=R_{q_\nu,a_\nu}^0$。

将 $r_{q_\nu,a_\nu}$ 放到 $F_\nu$，仍记 $r_\nu$，定义
$$
L_\nu=X_{r_\nu},\qquad
R_\nu=\frac{L_\nu}{1+\varepsilon_\nu},
\qquad
\widetilde r_\nu=R_\nu1=\frac{r_\nu}{1+\varepsilon_\nu}.
\tag{4.4}
$$
由 (1.2)--(1.3)，
$$
\|L_\nu-R_{q_\nu,a_\nu}^0\|\le\varepsilon_\nu.
\tag{4.5}
$$
因此 $\|R_\nu\|\le1$。

同时 $R_\nu$ 在 $\mathcal A$ 中可逆。说明如下：$L_\nu$ 是 $A$ 的有限有理函数，所有分母由 $I+N_j$ 构成。将 $A$ 代入零时，所有 $V_j$ 取值 $1$，所以该有理函数的常数值等于纯块代数中 $R_{q_\nu,a_\nu}^0$ 的常数值 $a_\nu\ne0$。$A$ 拟幂零，故 $L_\nu-a_\nu I$ 拟幂零，范数收敛的逆级数给 $L_\nu^{-1}\in\mathcal A$。这也可由相应有理函数在零附近的解析逆得到。

为了保留逆真空的大范数，(4.3)--(4.5) 的 Neumann 估计给
$$
\|L_\nu^{-1}\|
\le\frac{M_\nu}{1-\varepsilon_\nu M_\nu}
$$
及
$$
\|L_\nu^{-1}1-U_{q_\nu,a_\nu}^0\Omega\|
\le
\frac{\varepsilon_\nu M_\nu}{1-\varepsilon_\nu M_\nu}
\|U_{q_\nu,a_\nu}^0\Omega\|
\le\frac13\|U_{q_\nu,a_\nu}^0\Omega\|.
$$
故
$$
\boxed{
\|R_\nu^{-1}1\|
=(1+\varepsilon_\nu)\|L_\nu^{-1}1\|
\ge\frac23\|U_{q_\nu,a_\nu}^0\Omega\|
\ge2\nu.
}
\tag{4.6}
$$
所有 pure/actual 比较均发生在原 Haar 空间中的有界算子上。

## 5. 前向乘积的非零强极限

记
$$
\mu_\nu=\langle\widetilde r_\nu,1\rangle,
\qquad
\alpha_\nu=\|\widetilde r_\nu\|^2.
$$
由 (2.8)、(4.3)，
$$
1-\frac4{q_\nu}\le\mu_\nu\le1,
\qquad
1-\frac8{q_\nu}\le\alpha_\nu\le1.
\tag{5.1}
$$
这些均值均严格正。因各块互不相交，有限普通函数乘积
$$
h_n=\prod_{\nu=1}^n\widetilde r_\nu
$$
满足
$$
\|h_n\|^2=\prod_{\nu=1}^n\alpha_\nu,
\qquad
\langle h_n,1\rangle=\prod_{\nu=1}^n\mu_\nu.
\tag{5.2}
$$
对 $m>n$，准确有
$$
\|h_m-h_n\|^2
=\left(\prod_{\nu\le n}\alpha_\nu\right)
\left(
\prod_{n<\nu\le m}\alpha_\nu+1
-2\prod_{n<\nu\le m}\mu_\nu
\right).
\tag{5.3}
$$
两个亏损级数可和，故尾部两个乘积都一致趋于 $1$。
于是 $h_n\to h$ 于 $H$，并有
$$
\|h\|^2=\prod_{\nu\ge1}\alpha_\nu
\ge1-\sum_{\nu\ge1}\frac8{q_\nu}\ge\frac78,
\qquad
\langle h,1\rangle\ge\frac{15}{16}.
\tag{5.4}
$$

定义实际有限乘积
$$
P_n=\prod_{\nu=1}^nR_\nu.
$$
每个 $P_n$ 是 $\mathcal A$ 中的收缩，而且 (1.4) 给 $P_n1=h_n$。
对任意多项式 $p$，
$$
P_np(A)1=p(A)h_n\longrightarrow p(A)h.
$$
由 $1$ 循环及统一收缩界，$P_n$ 在全 $H$ 上强收敛到收缩 $P\in A'$。
又 $P1=h\ne0$，故 $P\ne0$。

## 6. 同一组有限逆积给收缩强单位

置
$$
W_n=P_n^{-1}=\prod_{\nu=1}^nR_\nu^{-1}\in\mathcal A.
\tag{6.1}
$$
这里不声称 $\|W_n\|$ 一致有界；每个 $W_n$ 是有界算子。

对固定 $n$ 和 $m>n$，全部因子在 $\mathcal A$ 中交换，所以
$$
P_mW_n=\prod_{\nu=n+1}^mR_\nu
$$
是收缩。取强极限得
$$
K_n:=PW_n\in A',\qquad \|K_n\|\le1.
\tag{6.2}
$$
由 (1.4)，$K_n1$ 是尾部普通函数乘积的 $L^2$ 极限。其与 $1$ 的距离平方为
$$
\prod_{\nu>n}\alpha_\nu+1-2\prod_{\nu>n}\mu_\nu
\longrightarrow0.
$$
再次使用 $1$ 循环及 $\|K_n\|\le1$，得到
$$
\boxed{PW_n\longrightarrow I\quad\hbox{强收敛，且 }\|PW_n\|\le1.}
\tag{6.3}
$$

这还给出完整有限放大旗子商结论。给任意有限 $d$ 及闭
$A^{(d)}$ 不变子空间 $N\subset M$，所有 $R_\nu,W_n,P$ 都保持 $N,M$。
诱导算子 $P_{M/N}$ 满足相同收缩强单位关系，因而是单射且像稠密：
若 $P_{M/N}x=0$，则每个 $K_{n,M/N}x=0$，强极限给 $x=0$；
而 $K_{n,M/N}(M/N)$ 包含于 $P_{M/N}$ 的像并强趋全空间。

特别，(6.3) 对任何正常泛函都可以在有界乘积 $PW_n$ 上取极限。这一锚不要求 $1\in\operatorname{Ran}P$。

## 7. 真空没有原像

先不对实际逆积作任何张量分离。由于 $P_{n-1}$ 为收缩，
$$
P_{n-1}W_n=R_n^{-1}
$$
准确成立，于是 (4.6) 给
$$
\boxed{
\|W_n1\|\ge\|P_{n-1}W_n1\|
=\|R_n^{-1}1\|\ge2n.
}
\tag{7.1}
$$

若存在 $g\in H$ 满足 $Pg=1$，则利用交换性与 (6.3)，
$$
W_n1=W_nPg=PW_ng=K_ng\longrightarrow g,
$$
与 (7.1) 矛盾。因此
$$
\boxed{1\notin\operatorname{Ran}P.}
\tag{7.2}
$$
另一方面，第 6 节已经严格给出 $P$ 单射、像稠密及其每个有限放大不变子商上的同样性质；(7.2) 不涉及闭包。

## 8. 与已有指定正常矩接口的准确关系

R267 本体及其前两个附录从收敛的**逆**真空乘积构造 $g$，得到 $Pg=1$ 和 $P^{-1}=X_g$。本文使用收敛的**前向**真空乘积来构造 $P$，并由 (7.1) 排除这样的 $g$。两条构造都具有 (6.3) 中的同组收缩强单位。

因此，R244 原始条件
$$
Pf_i\in\operatorname{Dom}X_{Cf_i},
\qquad
\phi(PF)=B(Fh_P,1)
$$
仍然可以对本类 $P$ 提出；原始指定配对结论并不要求 $1\in\operatorname{Ran}P$。但 R244 聚合逆图附录以 $g=P^{-1}1$ 为核心的三向等价不能直接应用于本文例子。

目前未证明：给定满足 $\phi(S\mathcal A)=0$ 的非零正正常见证，能够选择本文的参数和块，使其逐列配对条件、或相应固定真空表示成立。收缩强单位本身只支付非零锚与有限旗子商的单射/稠密，并不支付指定无界乘子域。也没有证明本 $P$ 属于 $S A'$ 或 $S B(H)$。

## 已证依赖

- R267：实际局部 $V_j$ 结构、真空列与无交块乘积方法。
- R267 第二附录：纯 Blaschke 缺陷恒等式；本稿第 2 节已重新给出所需式子。
- R88：$1$ 循环、实际有限 Walsh 乘子与交换子闭性。
- R244 及其聚合逆图附录：只用于第 8 节的接口定位；第 1--7 节的构造和证明独立于指定正常见证。
