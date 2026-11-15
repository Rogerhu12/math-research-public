# R358：一个原速度—加速度成本的非零总通量商类

> **R382 后续核定（2026-11-15）。** [完整修正后原式](R382-universal-cancellation-of-the-corrected-H-total-flux-and-independent-Q4.md)现已证明所有实际状态的两个H自然总通量均为零。旧具体7/13自然通量控制在此通道没有H响应；仅保抽象条件命题，不能以本族读出满足其非零/满秩前提。此结论不说H算子为零或H属于R。


> **2026-11-15 R378 更正。** 原式(23)漏第三history在Ps/Bs的链项；指定真−7的自然通量准确为零，本文非零及由此给出的非成员证明撤回。详见[完整原式更正](R378-correction-of-the-third-history-term-in-the-complete-H-flux.md)。以下旧正文保留供追溯，不作为被撤回结论的当前证明。


日期：2026-11-15。**完整纸面证明；没有执行新的 profile 积分、原根恢复、符号消元、秩计算或科学运行。**

沿 [R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)，原完整成本空间 $U$ 上有自然读出
$$
\Lambda_u(V)=
\int u'''V(u^2,0)-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)),
\tag{1}
$$
并且 $\Lambda_u(\mathcal R)=0$。这里 $\pi$ 是原正式 pure 投影，$\mathscr G$ 是原 pure 的真实有序 $2+2$ 三矩尾映射，不是自由指定的补偿。

[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md) 已证明三个加速度平方正规族被 (1) 消去；[R356](R356-lowest-two-full-self-weights-and-universal-total-flux-cancellation.md) 支付了整个 $U$ 的最低两权。本稿继续原 $H_1,H_2$，得到一个非零类。

记 $S_*=(h,k,\omega)=(1,1,1)$，$H_1,H_2$ 采用 [R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R134](R134-acceleration-layer-from-complete-local-v4.md) 的原正规化。令
$$
V_*=-2H_1(S_*)-4H_2(S_*),\qquad
V_{*,-7}=\Pi_{-7}V_*.
\tag{2}
$$
$\Pi_{-7}$ 是成本的真整权投影。主结论为
$$
\boxed{
\Lambda_u(V_{*,-7})
=-\frac1{57600}\int (u'')^5
\quad\text{对每个实紧光滑 }u.}
\tag{3}
$$
因此
$$
\boxed{V_{*,-7}\in U\setminus\mathcal R,\qquad U/\mathcal R\ne0.}
\tag{4}
$$
这是实际成本**线性空间**中的非成员结论，不是一个单输入数值余差。它不授非负成本障碍，不声称某个固定候选的全部 period 不可解，也不声称 (2) 已由一条指定的实际路径实现。

## 1. 原控制、profile 与正规化

固定共同右 collar，使用
$$
J(F)(x)=\int_x^{r_*}F(y)\,dy,\qquad
u\in C_c^\infty((\ell,r_*)).
$$
全稿记
$$
v=u',\qquad r=u'',\qquad t=u'''.
$$
几何状态及速度写作
$$
d=h\omega-k,\quad e=hx+d,\quad Q=1+e^2,\qquad
\gamma=h_s,\quad \delta=d_s,\quad \vartheta=e_s=x\gamma+\delta.
\tag{5}
$$
原水平关系仍是 $\omega_s=k_s/(2h)$；因此
$$
k_s=2\omega\gamma-2\delta,\qquad
\omega_s=\frac{\omega\gamma-\delta}{h}.
\tag{6}
$$
$(\gamma,\delta)$ 只是同一真实控制分布的另两个速度坐标，未把 $\omega$ 固定或新增控制。

令
$$
l=\gamma v-\vartheta r,\qquad
g=\gamma u-\frac{\vartheta v}{2},\qquad
\eta=2h\vartheta-\gamma e,\qquad
c_1=\frac{2e\vartheta}{Q}-\frac{\gamma}{h}.
\tag{7}
$$
其中 $\eta$ 只是本文的线性速度缩写，不是 R56 的恢复量 $\eta_0$。有
$$
l'=-\vartheta t,\qquad g'=l/2.
$$

后面的上标 $[j]$ 指几何导数权，不指 profile 真权。先完成全部真实导数，再将累计第二、第三 scalar 的值置零；它们的导数仍代入原递推。[R109](R109-local-density-of-the-complete-fourth-quotient.md) 规定的正是这个次序。R134 已证明：这足以决定 $H_1,H_2$；被减去的 $\mathcal B_{m_2}N_2$ 只是速度四次项，不能改变这两个系数。

## 2. 第二局部场及不能删除的 history 导数

令 $a=\eta_{0,Z}/h$ 为第二局部场的第一分子。原 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md) 给
$$
\boxed{a'=\frac{Qt\,l}{8h^3},\qquad a(r_*)=0.}
\tag{8}
$$
$a$ 对 $(\gamma,\delta)$ 线性。

原第二 scalar 密度的速度二次部分为
$$
\boxed{
m_2=\frac{2\vartheta a}{h}+\frac{Ql^2}{8h^4},
\qquad
m_2'=\frac{2\gamma a}{h}+\frac{e l^2}{4h^3}.}
\tag{9}
$$
第一式可直接由 R73(5)–(6) 的速度二次系数与 R350(7) 的 $a$ 代入得到；局部 $r^2$、$vr$ 项相消，剩余正是 R73 的 $v^2,J_0,J_1,J_2^*$ 四项。第二式由 (8)、$l'=-\vartheta t$ 微分，两个 $\vartheta Qtl$ 项准确相消。

若累计第二 scalar 值为零，其真实 $s$ 导数仍为 $m_2$。于是第二分子的高导数权平面部分为
$$
(\nabla_sV_Z)^{[2]}_{\rm plane}
=\left(
a_s+\frac{m_2'}2,\
e\left(a_s+\frac{m_2'}2\right)+\vartheta a-hm_2
\right).
\tag{10}
$$
这里 $a_s$ 是完整状态导数，包含加速度及速度平方；不能只取其中一个部分。

## 3. 第三局部场：完整 history 项使原式简化

记 $c=\eta_{0,C}^{[2]}/h$ 为第三局部场第一分子的导数权二部分，令
$$
f_1=he v-Qr,\qquad G=he u-\frac{Qv}{2},
\qquad j=J(Qt\,a).
$$
原分子内积给
$$
P_C=\frac{-f_1a+j}{4h},\qquad
B_C=\frac{Ga}{2h}.
\tag{11}
$$
对第一式求真实 $s$ 导数时，必须保留
$$
\boxed{
(P_C)_s=(P_{C,\mathrm{local}})_s
-P_{H(Y_u,Y_{m_2})}
\quad\text{在导数权二层。}}
\tag{12}
$$
这是第二场 $Z=K_2-Y_A$ 的真实 $A_s=m_2$，而非新增 forcing。其完整原量为
$$
P_{H(Y_u,Y_{m_2})}
=\frac{e v m_2'}8
+\frac1{8h}J(Qr m_2''+2h^2v m_2').
\tag{13}
$$

为使符号可直接回原式检查，R56 的另一所需配对是
$$
T_{sx}^{[2]}
=\frac{g(ea'+ha)}2
+\frac{f_1(a_s+m_2'/2)}4
+\frac{(hv-er)(\vartheta a-hm_2)}4.
\tag{14}
$$
将 (11)–(14) 代入 R56 的
$$
c=-\frac{T_{sx}^{[2]}}{2h^2}
+\frac{\vartheta P_C'}{2h^2}
+\frac{\gamma B_C'}{2h^2}
-\frac{(P_C)_s}{2h},
$$
同锚分部积分后得到
$$
c=-\frac{j_s}{8h^2}+\frac{\gamma j}{8h^3}
-\frac{Ql a'}{8h^3}
+\frac1{16h^2}J\!\left[t(2he\,m_2-Qm_2')\right].
\tag{15}
$$
每次原函数积分只使用右零 jets。没有令 $m_2$ 的左尾为零。

由 (9)，
$$
2he\,m_2-Qm_2'=2(Q_s-Q\gamma/h)a.
$$
又 $j_s=J(Q_s t a)+J(Qt a_s)$，所以 (15) 准确化成
$$
\boxed{
c=-\frac{J(Qt a_s)}{8h^2}
-\frac{Ql a'}{8h^3}.}
\tag{16}
$$
漏掉 (12) 会错误留下其他局部项；本稿只使用完整式 (16)。它的加速度部分与 R350 已付的原系数相同。

第三 scalar 密度 $n^{[3]}$ 的加速度部分由原 [R76](R76-local-third-exact-loops-and-weight-three-control.md) 的 $\Sigma$ 给
$$
\boxed{
n_{\rm acc}
=\frac{Ql\,a_{\rm acc}-\vartheta J(Qt a_{\rm acc})}{4h^3}.}
\tag{17}
$$
其中 $a_{\rm acc}$ 表示 $a_s$ 对加速度的线性部分。R73 的 $-\Psi(u,m_2)$ 只有速度三次，不增加 (17)。

## 4. 原 self、pure 与有序尾的系数

记 $\mathcal K(A,B)$ 为原 characteristic 配对 $\mathcal R_{H(A,B)}$ 的真实 $s$ 积分。完整 self 与 raw pure 分别是
$$
\Sigma=-\mathcal K(Z,Z),\qquad
P_{\rm raw}=16\pi V=-\mathcal K(Z,Z)-4\mathcal K(Y,C).
\tag{18}
$$
对一个真实位于 $u$ 右侧的辅助包，第二场在整个 $u$ 左域只留下其原三矩尾。该尾的局部第一分子是常数
$$
a_L=-\frac{p_s}{2h},
$$
其中 $p$ 是原第二 normal 的真实三矩值。匹配辅助三矩为 $\mu(u)$ 后，$a_L$ 恰为当前 $a$ 的真实左值，所有状态导数也同步匹配。

原有序 raw pure 的 $2+2$ 系数是
$$
\Gamma_{\rm raw}
=-2\mathcal K(Z,Z_{\rm tail})
-4\mathcal K(Y,C_{\rm tail}).
\tag{19}
$$
这正是 R352 的原支撑展开，因子没有重新极化。因此 (1) 等价于
$$
\boxed{
\frac54\Lambda=
\Omega(\mathcal K(Y,C))-\Omega(\mathcal K(Z,Z))
+\frac13\Omega(\mathcal K(Z,Z_{\rm tail}))
+\frac23\Omega(\mathcal K(Y,C_{\rm tail})).
}
\tag{20}
$$
本节及下节可以先在原有限局部环境中，用同一组三个实际右包作线性读出；取出 $H_1,H_2\in U$ 后，R352 保证它就是 (1)，与辅助方案无关。

## 5. 线性加速度项：ZZ 的 P、B 项也必须保留

用 $\mathrm d_v$ 表示只对速度 $(\gamma,\delta)$ 的微分。$\mathrm d_va$ 与实际加速度配对，表示 $a_s$ 的线性加速度部分；状态微分的其余部分是速度平方。

先对原 $s$ 导数作完整分部积分，路径端点为常值 germs，所以显式速度边势为零。记
$$
\alpha=Q\gamma/h-e\vartheta,\qquad \lambda=\vartheta/h^2.
$$
由 R56 与 (10)，模掉纯速度四次项，
$$
\begin{aligned}
\Omega(\mathcal R_{H(Z,Z)}^{[4]})\equiv
\int t\bigg\{&
\frac{Q a_s^2+2aa_s\alpha}{2h^2}\\
&+\lambda_s P_2+
(\gamma/h^2)_s B_2\bigg\},
\end{aligned}
\tag{21}
$$
其中
$$
\boxed{
P_2=-\frac{ea^2}{2}+\frac{J(Qa'^2)}{2h},
\qquad B_2=\frac{Qa^2}{2h}.}
\tag{22}
$$
最后两项只取其含加速度部分。它们来自原
$-\lambda P_s-\gamma B_s/h^2$，不能因为加速度平方部分不使用它们就删除。

式 (21) 的第一个分式可直接核对：原平面平方展开中 $a_s$ 的线性系数是
$Qm_2'/2+e\vartheta a-ehm_2=\alpha a$，这里准确使用 (9)。
式 (22) 则由
$Q a'^2+2heaa'+h^2a^2=Qa'^2+(hea^2)'$
及同一右零端得到；不要求 $a$ 左紧。

对 $Y$–$C$ 项，保留第三 history 的真实导数，原式给
$$
\begin{aligned}
\Omega(\mathcal R_{H(Y,C)}^{[4]})
={}&-4\int(a_s'-c_1a')c\\
&+\int\frac{t g}{2h^2}
\left(\frac{e n'}2-hn\right).
\end{aligned}
\tag{23}
$$
第一行的局部项与 primitive 项各给
$Q(\lambda_s r-\lambda_s'v)c/(4h)$；
两项相加才得到显示的因子 $4$。
具体用
$$
a_s'-c_1a'
=-\frac{Qt}{8h}(\lambda_s r-\lambda_s'v).
$$
紧 outer 的分部积分与真实 Fubini 均保留非紧 inner 左尾。

代入 (16)、(17)。加速度平方 bulk 与 (21) 相消，剩余 $x$ 边项
$-a_{s,L}J(Qt a_s)_L/(2h^2)$
再与 (20) 两个有序尾的对应项相消。若暂将 (22) 的两个项另列，在线性加速度层得到
$$
\begin{aligned}
\mathfrak C_0
=\int\bigg\{&
-\frac{t a\alpha}{h^2}\,\mathrm d_va
-\frac{c_1a'}{2h^2}\,\mathrm d_vj
+\frac{Ql a'}{2h^3}\,\mathrm d_va'\\
&+\frac{eg a'}{2h^2}\,\mathrm d_va'
-\frac{g a'}{hQ}\,\mathrm d_va
+\frac{gt\eta}{16h^5}\,\mathrm d_vj
\bigg\},\qquad j=J(Qt a).
\end{aligned}
\tag{24}
$$
其真实尾项是
$$
\begin{aligned}
\mathfrak T_0
={}&\frac{a_L}{6h^2}\int t\alpha\,\mathrm d_va
+\frac{\mathrm d_va_L}{6h^2}\int t\alpha a\\
&+\mathrm d_va_L\left\{
\frac1{3h^2}\int F c_1a'
-\frac2{3h}\int\frac{ga'}Q
-\frac1{24h^5}\int gt\eta F
\right\},
\end{aligned}
\tag{25}
$$
其中
$$
F=Qr-2he v+2h^2u,\qquad F'=Qt,\qquad J(Qt)=-F.
\tag{26}
$$

为准确核对尾系数，两个原 tail 配对在含加速度层为
$$
\begin{aligned}
\Omega(\mathcal R_{H(Z,Z_{\rm tail})})
\equiv\int t\bigg\{&
\frac{Qa_sa_{s,L}+\alpha(a_sa_L+a_{s,L}a)}{2h^2}\\
&+\lambda_sP_{2,\rm tail}
+(\gamma/h^2)_sB_{2,\rm tail}\bigg\},
\end{aligned}
$$
$$
\begin{aligned}
\Omega(\mathcal R_{H(Y,C_{\rm tail})})
\equiv{}&\frac{a_{s,L}}{2h^2}J(Qt a_s)_L\\
&+a_{s,L}\left\{
\frac1{2h^2}\int F c_1a'
-\frac1h\int\frac{ga'}Q
-\frac1{16h^5}\int gt\eta F
\right\},
\end{aligned}
\tag{27}
$$
而
$$
P_{2,\rm tail}=-\frac{eaa_L}{2},
\qquad B_{2,\rm tail}=\frac{Qaa_L}{2h}.
\tag{28}
$$
例如 $Z$–$Z_{\rm tail}$ 的右 primitive 直接为
$a_LJ((ea)')/2=-eaa_L/2$。
右包的真实 $a_L$ 与导数始终保留，没有把它置零。

定义
$$
\Theta=\int t\left\{
\frac{P_2}{h^2}\,\mathrm d_v\vartheta+
\frac{B_2}{h^2}\,\mathrm d_v\gamma\right\},
$$
$$
\Theta_{\rm tail}=\int t\left\{
\frac{P_{2,\rm tail}}{h^2}\,\mathrm d_v\vartheta+
\frac{B_{2,\rm tail}}{h^2}\,\mathrm d_v\gamma\right\}.
\tag{29}
$$
因此，(20) 的**完整**线性加速度一形式为
$$
\boxed{
\mathfrak C=\mathfrak C_0+\mathfrak T_0-\Theta+\frac13\Theta_{\rm tail}.}
\tag{30}
$$
(25)、(27)、(30) 精确保留原来的 $1/3,2/3$ 有序因子。

在 $(h,d)$ 正规化中，把剩余速度面积写成
$$
(\mathcal H_\gamma\gamma+\mathcal H_\delta\delta)
(\gamma\delta_s-\delta\gamma_s).
$$
取速度外微分可消去准确的速度三次势。按 R129 的因子 $3$ 与 (20) 的规范，
$$
\boxed{
\mathrm d_v\mathfrak C
=\frac{15}{4}
\{\Lambda_u(\mathcal H_\gamma)\gamma+
\Lambda_u(\mathcal H_\delta)\delta\}
\,\mathrm d\gamma\wedge\mathrm d\delta.}
\tag{31}
$$
这里的方向是 $\partial_\gamma C_\delta-\partial_\delta C_\gamma$。
此式只是从同一原局部成本取系数；不是另加一套 normal gauge。

## 6. 从完整原式取一个准确 Laurent 系数

固定 $h=1,d=0$，置 $u_\epsilon(x)=u(x/\epsilon)$，同锚右 collar 一并缩放；把换元后的变量仍记为 $x$。原 R76(13) 给
$$
a_h(u_\epsilon)(\epsilon x)
=\epsilon^{-3}A(u)(x)+O(\epsilon^{-1}),
\qquad
a_d(u_\epsilon)(\epsilon x)
=\epsilon^{-4}B(u)(x)+O(\epsilon^{-2}),
$$
$$
\boxed{
A=\frac{2vr-xr^2+J(r^2)}{16},
\qquad B=-\frac{r^2}{16}.}
\tag{32}
$$
这些是原式的有限 Laurent 展开，不是数值近似或新 profile 试验。真实微分为
$$
A'=\frac{(v-xr)t}{8},\qquad B'=-\frac{rt}{8}.
\tag{33}
$$

取 (31) 中 $\gamma\,\mathrm d\gamma\wedge\mathrm d\delta$ 的
$\epsilon^{-9}$ 系数。先看 (24)。只有以下两项有贡献：
$$
-\gamma\int t\,a\,\mathrm d_va
+\frac{\gamma}{2}\int a'\,\mathrm d_vj,
\qquad j=J(ta),\quad a=\gamma A+\delta B.
\tag{34}
$$
截断依据逐项明确：在缩放后的基点，
$$
Q=1+\epsilon^2x^2,\qquad
c_1=-\gamma+2\epsilon x\delta+O(\epsilon^2\gamma),
\qquad \alpha=\gamma-\epsilon x\delta,
$$
$$
g_\gamma=O(1),\quad g_\delta=O(\epsilon^{-1}),
\qquad\eta_\gamma=O(\epsilon),\quad\eta_\delta=2.
$$
所以 (24) 所有含 $g$ 的项在所取外微分系数中至少是
$\epsilon^{-7}$，前两项未列出的坐标修正也至少是这个阶。
另一个看似更高的项在取任何极限之前已是准确速度梯度：
$$
\frac{Ql a'}{2h^3}\,\mathrm d_va'
=\mathrm d_v\left(\frac{Qq^2l^3}{6h^3}\right),
\qquad q=\frac{Qt}{8h^3},\quad a'=ql.
\tag{35}
$$

(34) 的所取外微分系数为
$$
-\int tAB+\int A'J(tB)-\frac12\int B'J(tA).
\tag{36}
$$
$B_L=0$，且 $J(tB)_L=-\int r^2r'/16=0$，所以真实同锚分部积分给
$$
\int A'J(tB)=\int B'J(tA)=\int tAB.
\tag{37}
$$
这里没有假设 $A_L=0$。故 (36) 为 $-\frac12\int tAB$。

还必须加入 (29) 的 $-\Theta$。其同阶所取外微分系数准确为
$$
\int t\{AB-J(A'^2)+xJ(A'B')\}.
\tag{38}
$$
由 (33) 及真正紧的 outer $r,xr-v$，
$$
\int tJ(A'^2)=\int rA'^2
=\frac1{64}\int r(v-xr)^2t^2,
$$
$$
\int xtJ(A'B')=\int(xr-v)A'B'
=\frac1{64}\int r(v-xr)^2t^2.
\tag{39}
$$
这两个 primitive 项准确相消。因此 (38) 为 $+\int tAB$。
这一步说明：漏掉 $ZZ$ 的原 $P,B$ 项会把最终符号算反。

(25) 和 $\Theta_{\rm tail}/3$ 在这个系数上均为零。完整依据是
$$
A_L=\frac{\mu_0}{16},\quad B_L=0,\quad
\int tA=\frac1{48}\int r^3,\quad
\int tB=0,\quad \int rB'=0.
\tag{40}
$$
例如 (25) 第一、二项的可能 $\epsilon^{-9}$ 混合项含
$A_L\int tB$；第三项的可能同阶项含 $A_L\int rB'$。
其它含 $g$ 的尾项至少是 $\epsilon^{-7}$。
(29) 的 tail 中同阶可能项也含 $A_L\int tB$；
其余最高项只有 $\gamma^2\mathrm d\gamma$，外微分为零。
实际 $a_{d,L}$ 的次项为 $\epsilon^{-2}$，只进入更低阶，
没有因 $B_L=0$ 就删除整个真实 $a_L$。

最后，保留全部边项的三次分部积分给
$$
\begin{aligned}
\int tAB
&=-\frac1{256}
\int tr^2\{2vr-xr^2+J(r^2)\}\\
&=-\frac1{256}
\left(-\frac12+\frac15+\frac13\right)\int r^5
=-\frac1{7680}\int r^5.
\end{aligned}
\tag{41}
$$
三分数分别来自 $r^4,r^5,r^3$ 的真实导数；
各边界乘积都有一个紧的 outer 因子。

合并 (36)–(41)，完整 (30) 的系数是
$$
\boxed{\frac12\int tAB=-\frac1{15360}\int r^5.}
\tag{42}
$$
由 (31)，
$$
\Lambda_{u_\epsilon}(\mathcal H_\gamma)
=-\frac{\epsilon^{-9}}{57600}\int (u'')^5
+O(\epsilon^{-8}).
\tag{43}
$$
这里只写了一个较弱余阶界；显示的 Laurent 系数是准确的。

## 7. 回到原 H1/H2 与真成本权

由 (6)，
$$
\gamma(k_s)_s-k_s\gamma_s
=-2(\gamma\delta_s-\delta\gamma_s)
+\text{纯速度三次式}.
\tag{44}
$$
因此，在施加 $\Lambda$ 后，
$$
\boxed{
\Lambda(\mathcal H_\gamma)
=-2\Lambda(H_1+2\omega H_2).}
\tag{45}
$$
加速度坐标的变化还会从加速度平方项产生线性加速度项。
R350 已证明三个原 $\bar A$ 系数在**每个实际状态**都被 $\Lambda$ 消去；
它们的状态导数亦被消去，所以这些附加项不改变 (45)。
(44) 的速度三次项只改变速度四次成本，不改变所取的两个 $H$。

[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md) 与 R134
已付每个实际状态的 $H_1,H_2\in U$，不是把一个形式局部系数直接宣布为可控成本。
故 (2) 是实际 $U$ 元素，真 affine 不变性又使其整权投影属于 $U$。

[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)
的同锚伸缩恒等式给
$$
\Lambda_{u_\epsilon}(V)
=\epsilon^{-2}\Lambda_u(D_\epsilon V)
=\sum_\sigma\epsilon^{\sigma-2}
\Lambda_u(\Pi_\sigma V),\qquad V\in U.
\tag{46}
$$
pure 与有序尾读出也满足相同身份：把实际右辅助包和 $u$ 一起伸缩，
原三矩匹配系数不变。整个 primitive 常数随同一右 collar 变换，没有重置。

这里使用的是已付真 affine 算子作用与
[R203](R203-general-pure-lowest-two-weights-vanish.md) 的有限多项式、faithful 原式延拓，
不要求将一条冻结的全局几何或一组旧实际 profiles 机械缩放后仍当作同一输入。
原式系数身份一旦成立，就在原共同物理区间的全部紧 profiles 上成立。

在 $S_*=(1,1,1)$，(43)–(46) 将 $\epsilon^{-9}$ 系数准确识别为成本权 $-7$，
证明 (3)。这不是从一个窄包的首项推断整个函数；它是有限 Laurent 式对每个
紧光滑 profile 的系数身份。

## 8. 真正光滑紧支撑的非零见证

取非零、非负、偶的 $\eta\in C_c^\infty$，选固定 $a_0$ 使下列三个支撑不交：
$$
r(x)=\eta(x)-\frac12\eta(x-a_0)-\frac12\eta(x+a_0).
\tag{47}
$$
准确有 $\int r=\int xr=0$。以同一右锚置 $u=J^2r$；
这两个矩使 $u,u'$ 在左空 collar 也为零。因此 $u$ 是真正的偶
$C_c^\infty$ profile，且 $u''=r$。

不交支撑给
$$
\int r^5
=\left(1-\frac2{32}\right)\int\eta^5
=\frac{15}{16}\int\eta^5>0.
\tag{48}
$$
故 (3) 在此 profile 上严格负。可以先作固定的正缩放与平移，
把全部支撑放入原共同活动区间内部；(48) 仍非零。
在基点的局部坐标选择中，也可以把支撑取在 $1+x>0$ 的小区间。
不需要任何数值求积。

$\Lambda_u$ 消去整个 $\mathcal R$，而 (48) 使其在 $V_{*,-7}$ 上非零，
所以 $V_{*,-7}\notin\mathcal R$。其实际 $U$ 成员资格来自 R130，
不是依赖这个 profile 见证而补设。

## 9. 新结论的准确范围

本稿支付了超出 R350 三个零加速度平方族、R356 两个零最低权的新总通量商坐标。
原响应空间不能线性张成全部 canonical 第四成本：
$$
U/\mathcal R\ne0.
$$
这不授非负成本障碍：实际有限路径成本构成的半群与其线性空间不同。
也没有证明 $V_{*,-7}$ 为 pure-zero、whole-self-zero，
或它是一条已指定实际几何路径的成本。

证明始终保留 (12) 的真实第二 history 导数、(21) 的完整 $P,B$ 项、
(27) 的同一有序尾、原正规化和真成本权。
同一二阶选择下的全部 period、所有平台及内部退化点通量、
整个 ruling、正则几何实现、高阶条件及最终等距嵌入仍是各自的义务。
本稿没有为取得 (3) 执行新运行、重新评价旧根或增加参数族试验。
