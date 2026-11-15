# R370：完整 δ⁴ 正规成本的精确 C² 总通量

日期：2026-11-15。**原式纸面证明；没有执行新的 profile 积分、符号程序、原根恢复、秩计算、人工检查或研究运行。**

[R367](R367-exact-N2-Green-contraction-and-nonzero-quartic-velocity-correction.md)
支付了原 $\mathcal B_{m_2}N_2$ 的完整读出，但该单项不是整个四次速度成本。
本稿将它与真正的 $C_A m_2$、第三 history、第二 history 和原速度势归一化一起收齐。

在实际状态
$$
h=1,\qquad d=\omega-k,\qquad e=x+d,\qquad Q=1+e^2
$$
上，取原水平控制的 $\gamma=h_s=0$ 方向，记 $w=d_s$。
于是 $k_s=-2w$、$\omega_s=-w$。
令 $\mathcal Q_\delta(S)$ 为完整正规密度 $\widehat Q_4$ 中的 $w^4$ 系数。
若原 $(h_s,k_s)$ 规范写
$\widehat Q_4=\sum_{i+j=4}Q_{ij}h_s^i k_s^j$，则
$$
\mathcal Q_\delta(1,k,k+d)=16Q_{04}(1,k,k+d).
\tag{1}
$$
这是原 [R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、
[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、
[R134](R134-acceleration-layer-from-complete-local-v4.md) 的完整正规系数，
不是另选的局部单项。

主结论是
$$
\boxed{
\Lambda_u\bigl(\mathcal Q_\delta(1,k,k+d)\bigr)
=\frac1{80}\int (x+d)(u'')^5
\qquad(u\in C_c^\infty(I)).
}
\tag{2}
$$
它与独立的 $k$ 无关，适用于每个共同物理窗口合法的实际状态。
右边是准确的连续 $C^2$ 五次泛函，而非仅 principal 或小尺度首项。
因此本稿给出一个确实非零的完整 Q4 读出。
不由此宣称所有 Q4、Q2 或整个实际成本半群已经控制。

## 1. 规范、真尾与归一化次序

始终固定原右 collar $r_*$：
$$
Jf(x)=\int_x^{r_*}f(y)\,dy,\qquad
v=u',\quad r=u'',\quad t=u'''.
$$
未注明的积分均在同一窗口上。
记
$$
P=J(r^2),\quad M=J(er^2),\quad
\mu_0=P(\ell),\quad \mu=M(\ell).
\tag{3}
$$
$P,M$ 的左值保留；没有假定它们紧支撑。
状态微分 $\partial_d$ 作用于 $e,Q$ 及原函数内的同一系数，保持 $u$ 和右锚不变。
下文也用下标 $e$ 表示这个状态微分。

采用 [R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)
的真实读出
$$
\Lambda_u(V)=\int tV(u^2,0)
-\frac{16}{5}\int t\,\pi V(u)
-\frac{32}{15}\int t\,\mathscr G_{V,u}(\mu(u)).
\tag{4}
$$
这里最后一项是原 pure 的有序 $2+2$ 真实三矩尾，不是自由补偿。
原响应空间 $\mathcal R$ 被 (4) 消去。
在中间 ambient 项上，只有明确保留了该同锚尾映射后，才使用同一配方。

令 $\beta=w_s$。
原三阶几何 jets 先通过真实 $s$ 分部积分消去。
随后一个 scalar 收缩若成为
$$
a(d)\beta^2+\sigma(d)w^2\beta+\rho(d)w^4,
$$
则其速度三次势为 $\sigma w^3/3$，完整四次余项是
$$
\rho-\frac13\partial_d\sigma.
\tag{5}
$$
状态方向在本方向实际为 $\partial_d-2\partial_k$；
下面所有导数权四的显示系数都不依赖独立 $k$，所以准确缩为 $\partial_d$。
两端常值 germs 支付所有显示的正导数权边势。
不把速度固定后求到的 $\rho$ 单独当成正规 Q4。

## 2. 原第二场与局部第三量

由 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、
[R76](R76-local-third-exact-loops-and-weight-three-control.md)，原第二密度和局部第一分子在此方向为
$$
m_2(u,u)=w^2q,\qquad a=wB,
\qquad
q=-\frac M4,\quad B=-\frac{Qr^2+2M}{16}.
\tag{6}
$$
其所需导数为
$$
B'=-\frac{Qrt}{8},\qquad
B_e=-\frac{er^2+P}{8},\qquad
q'=\frac{er^2}{4},\qquad q_e=-\frac P4.
\tag{7}
$$
定义
$$
D=B_e+\frac{q'}2=-\frac P8,\qquad
E=eD+B-q.
\tag{8}
$$
第二 history 的值最后为零，其导数仍是 $w^2q$。
所以原第二场协变导数的高权平面准确为
$$
(\nabla_sV_Z)_{\rm plane}^{[2]}
=(\beta B+w^2D,\ e\beta B+w^2E).
\tag{9}
$$

令 $j_B=J(QtB)$、$j_{B_e}=J(QtB_e)$。
[R358](R358-nonzero-total-flux-class-of-a-true-velocity-acceleration-cost.md)
从原 R56 完整恢复得到的第三局部第一分子为
$$
c=\beta C_b+w^2 C_v,\qquad
C_b=-\frac{j_B}{8},\quad
C_v=-\frac{j_{B_e}}8-\frac{Q^2r^2t}{64}.
\tag{10}
$$
特别 $j_{B_e}$ 不等于 $(j_B)_e$；后者还含 $J(2etB)$。

原第三密度的权三部分准确是
$$
n^{[3]}=2w\beta T+w^3n_0,
\tag{11}
$$
其中
$$
T=N_2(u;u,u)=-\frac{QrB+j_B}{8},
\tag{12}
$$
$$
\boxed{
n_0=\frac{eQr^3+J(r^3)-3J(erP)}{48}.}
\tag{13}
$$
为核对 (13)，先从原 $\ell-\Psi$ 保留未化简式
$$
n_0=-\frac{QrB_e+j_{B_e}}4
-\frac{erB+J(etB)}2
+\frac{vq}{4}+\frac{J(Qrq''+2vq')}{8}.
\tag{14}
$$
前两项来自 $H(Y,K)$ 的真实导数；
后两项是原 $-\Psi(u,m_2)$，不能删去。
代 (6)(7)，只在紧 $r,v$ 上分部积分，就得到 (13)。

另外，
$$
T=\frac{Q^2r^3+J(eQr^3)-6J(erM)}{192},
\qquad
T'=-\frac{erB}{4}+\frac{Q^2r^2t}{64},
\tag{15}
$$
$$
n_0'=\frac{e(e r^3+Qr^2t+rP)}{16}.
\tag{16}
$$
这些均保留同一原积分常数。

## 3. 两条不能删的第三 history 导数

按 [R109](R109-local-density-of-the-complete-fourth-quotient.md)，
先求完整物理导数，代入 history 方程，最后才令累计第二、第三值为零。

第一，第三场对累计 second 的线性依赖，求导后给
$-K(u,m_2)$。
原局部动态项的导数已经包含在 (10) 的 $c_s$ 内；
不能因此再删掉这个静态 $K$ 的链式项。
令 $\mathfrak b=B(u,q)$ 为 (6) 的真实对称极化，原 R56 配对给它的总通量贡献
$$
\Delta_C=\frac12\int Qrt\,\mathfrak b .
\tag{17}
$$

第二，第三 history 的导数给 $-Y_n$。
它同时进入 $T_s$ 和 $P_s$，二者必须一起恢复。
在此方向，完整贡献为
$$
-\Psi(u,n)=w\left\{\frac{vn}{4}
+\frac{J(Qrn''+2vn')}{8}\right\}.
\tag{18}
$$
特别不能只取 $T_s$ 内的
$-wv(en'/2-n)/4$，而漏掉 $+wP_{u,n}$。

定义一个保真线性收缩
$$
\mathscr P(f)=\int t\left\{\frac{vf}{4}
+\frac{J(Qrf''+2vf')}{8}\right\}.
$$
紧 outer $r$ 及 $v$ 直接给
$$
\boxed{\mathscr P(f)=\frac18\int r^2(Qf''-2f).}
\tag{19}
$$
证明只用 $\int tJF=\int rF$ 和
$\int tvf=-\int r^2f-\int rvf'$。
$f$ 可有真实左尾，未令它左紧。

剩余 $c$ 项在原 R56 中为
$$
-\frac w4\{Qr c_s+J(Qt c_s)\}
-\frac{w^2}{2}\{er c+J(et c)\}.
$$
对紧 outer 收缩，再沿 $s$ 作一次真实分部积分，准确等于
$$
-4\beta\int B'c
\tag{20}
$$
模掉显示的端势。
这里 $a_s'=\beta B'+w^2B_e'$，而 $B_e'=-ert/4$；
两份纯速度项准确相消。
这一步消去了三阶几何 jets，没有同时删掉 (17)(18)。

## 4. 四个原配对的完整系数表

用 $Z,Y,Zt,Yt$ 分别标记
$ZZ,YC,ZZ_{\rm tail},YC_{\rm tail}$。
每个 scalar 收缩在上述原分部积分后写为
$a_\bullet\beta^2+\sigma_\bullet w^2\beta+\rho_\bullet w^4$。

原 $ZZ$ 的 normal 原函数及必要 history 导数是
$$
P_B=-\frac{eB^2}{2}+\frac12J(Q(B')^2),
$$
$$
P_{Bq}=\frac14J\{(eB'+B)q'-(QB'+eB)q''\}.
\tag{21}
$$
真实 $P_{ZZ,s}$ 含 $-2w^3P_{Bq}$，不是只对 $w^2P_B$ 求状态导数。
于是
$$
\begin{aligned}
a_Z&=\frac12\int tQB^2,\\
\sigma_Z&=\int t\{B(D+eE)-2P_B\},\\
\rho_Z&=\int t\{(D^2+E^2)/2-(P_B)_e+2P_{Bq}\}.
\end{aligned}
\tag{22}
$$
由 (17)–(20)，完整 $YC$ 给
$$
\begin{aligned}
a_Y&=-4\int B'C_b,\\
\sigma_Y&=-4\int B'C_v+2\mathscr P(T),\\
\rho_Y&=\Delta_C+\mathscr P(n_0).
\end{aligned}
\tag{23}
$$

现取真正位于 $u$ 右侧的辅助包。其三矩最终按 R352 的实际线性读出匹配为 $\mu(u)$。
记其在左域的真实局部分子系数为
$$
\eta=-\mu/8,\qquad \zeta=-\mu_0/8,\qquad
\eta_e=\zeta,\quad\zeta_e=0.
\tag{24}
$$
匹配以前，(24) 对右包矩线性解释。
这不要求一个右包与 $u$ 同时具有相同重心。

设
$$
E_t=e\zeta-\eta,\quad
P_{tB}=-eB\eta/2,\quad
P_{qt}=\eta(e q'-2q)/4.
$$
右包 $q_{\rm tail}=2\eta$ 在 $x$ 上为常数。
因此第二对原配对给
$$
\begin{aligned}
a_{Zt}&=\frac12\int tQB\eta,\\
\sigma_{Zt}&=\int t\{(B\zeta+D\eta+eBE_t+eE\eta)/2-2P_{tB}\},\\
\rho_{Zt}&=\int t\{(D\zeta+EE_t)/2-(P_{tB})_e+P_{qt}\}.
\end{aligned}
\tag{25}
$$
$P_{qt}$ 是左包 history 的实际导数。
右包 $q_{\rm tail}$ 的 $x$ 导数为零，所以另一份 $P$ 交叉项准确为零。

令
$$
F=Qr-2ev+2u,\quad V=u-ev,
$$
$$
C_{bt}=\eta F/8,\quad C_{vt}=\zeta F/8,\quad
T_t=\eta V/4,\quad n_{0t}=\zeta V/2.
\tag{26}
$$
右包的整个第三尾恢复于是给
$$
\begin{aligned}
a_{Yt}&=-4\int B'C_{bt},\\
\sigma_{Yt}&=-4\int B'C_{vt}+2\mathscr P(T_t),\\
\rho_{Yt}&=\mathscr P(n_{0t}).
\end{aligned}
\tag{27}
$$
此处没有 $\Delta_{Ct}$：
$B(u,q_{\rm tail})=0$ 是本方向真实常数尾的极化结果，
不是把一般传入 second 删除。

## 5. 原 Λ 因子与 N2 整项抵消

原 self、raw pure 和有序 $2+2$ 系数给
$$
\frac54\Lambda
=\Omega(YC)-\Omega(ZZ)
+\frac13\Omega(ZZ_{\rm tail})
+\frac23\Omega(YC_{\rm tail}).
\tag{28}
$$
其来源及 $1/3,2/3$ 固定于 R352/R358，不能重新平均顺序。

系数表首先给独立的加速度检查：
$$
a_Y-a_Z=-B_L(j_B)_L/2,\qquad
a_{Zt}=a_{Yt}=B_L(j_B)_L/2.
$$
因此 (28) 的 $\beta^2$ 系数逐状态为零，
准确回到 [R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md)，
并未将某份单尾平方设为零。

再记原 R367 的
$$
S=-\int qT''',\qquad \alpha=B(u,q)_L.
$$
$q$ 与 $T$ 在左侧都为常数，所以该方向的三阶 Green 配对为零。
对原 $N_2$ 完整外槽变分，得到
$$
\Delta_C=2S+4B_L\alpha.
$$
而 R367 的完整 self、pure、真实有序尾已经给
$$
\widehat\Lambda(\mathcal B_{m_2}N_2)
=\frac85(S+2B_L\alpha)=\frac45\Delta_C.
\tag{29}
$$
这里也可直接用
$\int tN(u;u,q)=-\Delta_C/2$
和原非紧变分式核对；没有把 $q$ 当成紧 profile。

故 (23) 中的 $\Delta_C$ 被正规化中真正减去的
$\mathcal B_{m_2}N_2$ **整项**消去。
并非只消去它的 $r^3t^2$ 主部。
定义
$$
\begin{aligned}
S_{\rm self}&=\mathscr P(n_0)-\rho_Z
-\frac13\partial_e(\sigma_Y-\sigma_Z),\\
T_Z&=\rho_{Zt}-\frac13\partial_e\sigma_{Zt},\\
T_Y&=\rho_{Yt}-\frac13\partial_e\sigma_{Yt}.
\end{aligned}
\tag{30}
$$
在 $\sigma_Y$ 中仍使用 (23) 的全部表达式。
那么完整正规成本的读出准确为
$$
\boxed{\Lambda(\mathcal Q_\delta)
=\frac45\{S_{\rm self}+T_Z/3+2T_Y/3\}.}
\tag{31}
$$

## 6. Self 的完整分部积分

给出足够逐行核对的中间式。
令
$$
K=\int Q^3r^3t^2,\qquad H=\int eQ^2r^3t^2,\qquad
I=\int B'j_{B_e}.
$$
由 (15)(16)(19)，准确有
$$
\begin{aligned}
\mathscr P(T)
={}&-\frac K{256}
+\frac1{3840}\int Q(6+5e^2)r^5
+\frac1{384}\int Mr^3-\frac14\int r^2T,\\
\mathscr P(n_0)
={}&-\frac H{64}
+\frac1{960}\int e(7+4e^2)r^5
+\frac1{192}\int Pr^3-\frac14\int r^2n_0.
\end{aligned}
\tag{32}
$$
一次真实左尾分部积分还给
$$
\begin{aligned}
I={}&-B_L(j_{B_e})_L
+\frac1{960}\int Qr^5+\frac1{192}\int eQPr^3\\
&+\frac1{96}\int Mr^3-\frac1{32}\int eMPr,
\end{aligned}
\tag{33}
$$
$$
(j_{B_e})_L=-\frac1{12}\int r^3+\frac14\int ePr,
\qquad
\partial_e(j_{B_e})_L=\frac14\int Pr.
\tag{34}
$$
例如 (33) 中的第一项来自 $[Bj_{B_e}]_\ell^{r_*}$，不可省略。

由 (22) 独立收集 $ZZ$ 得
$$
\begin{aligned}
-\rho_Z+\frac13\partial_e\sigma_Z
={}&-\frac H{64}
+\frac1{2880}\int e(41+3e^2)r^5\\
&+\frac1{192}\int(e^2-1)Pr^3
+\frac1{192}\int eP^2r-\frac1{96}\int PMr.
\end{aligned}
\tag{35}
$$
其中 $2P_{Bq}$ 贡献了
$-\int eQ^2r^3t^2/32$；
原 $J(Q(B')^2)$ 的状态微分贡献相反的 $1/64$ 部分。
这说明先删 history 再求导会改变 (35)。

代 (32)–(35) 入 (30)，所有 $H$ 准确相消。
剩下的一次导数用紧 $r^3,r^5$ 分部积分。
原 primitive 的最后合并使用
$$
\int r^2JF+\int PF=\mu_0\int F,
\tag{36}
$$
而不是错误的“$P$ 紧”身份。
又
$$
\int Pr=\int vr^2,\qquad
\int r(M-eP)=\int ur^2,
\tag{37}
$$
第二式来自 $(M-eP)'=-P$、$(M-eP)''=r^2$ 和紧 $u$。

最后准确得到
$$
\boxed{
S_{\rm self}
=\frac1{64}\int er^5
+\frac{\mu_0}{384}\int(e^2-1)r^3
-\frac{\mu_0}{192}\int ur^2
-\frac{\mu}{192}\int vr^2.}
\tag{38}
$$
(38) 是完整等式；未留下未控制的 $C^2$ 余项或高阶 primitive。

## 7. 两份真实尾各自相同

先从 (25) 得到
$$
\begin{aligned}
T_Z={}&\frac{\zeta}{48}\int(e^2-1)r^3
+\frac{\zeta}{24}\int r(eP-M)
-\frac{\eta}{24}\int Pr.
\end{aligned}
$$
使用 (37)，即
$$
\boxed{
T_Z=\frac{\zeta}{48}\int(e^2-1)r^3
-\frac{\zeta}{24}\int ur^2
-\frac{\eta}{24}\int vr^2.}
\tag{39}
$$

再核 $YC$ 尾，不从 (39) 猜测。
由 $V=u-ev$、$V'=-er$，
$$
\mathscr P(V)=-\frac1{12}\int r^3-\frac14\int r^2V,
$$
$$
\int B'F=\frac1{24}\int eQr^3+\frac14\int eVr^2.
\tag{40}
$$
把 (40)、$\eta_e=\zeta$ 代入 (27)，得到
$$
\boxed{T_Y=T_Z.}
\tag{41}
$$
因此右包的实际状态导数也保留在相消中，不能只匹配其一个瞬时值。

最后按原三矩线性读出代入 (24)，式 (39) 恰为
$$
T_Z=T_Y
=-\frac{\mu_0}{384}\int(e^2-1)r^3
+\frac{\mu_0}{192}\int ur^2
+\frac{\mu}{192}\int vr^2.
\tag{42}
$$
这是 (38) 除局部项以外的准确负值。
由 (31) 得
$$
\Lambda(\mathcal Q_\delta)
=\frac45\left\{\frac1{64}\int er^5\right\}
=\frac1{80}\int er^5,
$$
证明 (2)。

## 8. 真 U 成员、非零与最低两权边界

(1) 是 R130/R134 已付的完整正规状态系数，
所以
$$
\mathcal Q_\delta(1,k,k+d)\in U.
$$
(2) 不把 R367 的单 ambient 响应提升成 U 元素；
正是把该响应与原 $v_4$ 全部合成后，才使用这条成员结论。

非零不需新的数值或高频试验。
取实偶非负紧 bump $\eta\ne0$，三个平移支撑互不交，
$$
r(x)=-\eta(x-x_0)
+\frac12\eta(x-x_0-b)+\frac12\eta(x-x_0+b).
$$
它的零、一阶矩均为零，所以 $u=J^2r$ 是真正紧光滑 profile。
准确有
$$
\int r^5=-\frac{15}{16}\int\eta^5,\qquad
\int(x+d)r^5=-\frac{15(x_0+d)}{16}\int\eta^5.
$$
选 $x_0+d\ne0$，并在选择实际 $k,\omega$ 时保共同窗口的 $x+\omega$ 间隙，
即得
$$
\Lambda_u(\mathcal Q_\delta)
=-\frac{3(x_0+d)}{256}\int\eta^5\ne0.
\tag{43}
$$
由 $\Lambda(\mathcal R)=0$，该完整成本不在原响应空间内。

在 $d=0$，原正伸缩下 (2) 恰按 $\epsilon^{-8}$ 缩放，
所以 [R203](R203-general-pure-lowest-two-weights-vanish.md)、
[R356](R356-lowest-two-full-self-weights-and-universal-total-flux-cancellation.md)
的 faithful 有限整权分解给
$$
\boxed{
\Lambda_u\!\left(\Pi_{-6}\mathcal Q_\delta(1,k,k)\right)
=\frac1{80}\int x(u'')^5.}
\tag{44}
$$
这是成本真权 $-6$，因为自然读出另带伸缩权 $-2$。
它不与整个 $U$ 的真权 $-9,-8$ 消去冲突。
$d\int r^5$ 对应真权 $-7$；不存在从单 ambient 高阶项越过完整抵消的推断。

## 9. 已付 pure 校正给一个准确的 C² 总通量类

无需重算旧表。
[R207](R207-complete-weight-minus6-pure-image-equals-three-dimensional-response.md)
已付 $\pi U_{-6}=\pi\mathcal R_{-6}$。
因此可在原响应内选 $R_\pi$，准确消去
$\Pi_{-6}\mathcal Q_\delta$ 的完整 pure，令
$$
W_{-6}=\Pi_{-6}\mathcal Q_\delta-R_\pi
\in U_{-6}\cap\ker\pi.
$$
pure 算子真正为零时，其每个真实有序 $2+2$ 系数也为零；
故原 (4) 对该同一元素就是 $\Omega$，从而
$$
\boxed{\Omega_u(W_{-6})=\frac1{80}\int x(u'')^5.}
\tag{45}
$$
这是已知实际 pure 响应校正后的精确泛函身份。
没有重新求旧 rank，也没有把左二次尾 self $Q$ 与完整 scalar self $\Sigma$ 混同。
本稿未宣称这一元素的 whole self 为零。

## 10. 完成范围

本稿完成一个整个正规 Q4 状态方向，包括：

- 原 $C_A m_2$、$-Y_n$ 与两种 $P_s$ history；
- R129 的真实速度三次势及其状态导数；
- R367 的完整非紧 Green 校正；
- 两份有序三矩尾的实际状态输运；
- 全部 $C^3$ 平方与 $C^2$ primitive 的准确抵消。

最后的非零式是 (2)，而不是 R367 的单项。
它不判定其余四个 Q4 方向、完整 Q2 或静态族，
不把线性空间成员当成实际成本半群的双向可达。
R363/R366 的真实有限读出控制仍按各自已证的路径范围使用；
本稿不新增一个未经证明的全 joint 或 full period 截面。
