# R362：完整 H2 的真实 C² 余项与权负六纯核总通量非零

日期：2026-11-15。**完整纸面证明；没有执行新的 profile 求积、参数族运行、原根编译、消元、秩计算或人工检查。**

[R358](R358-nonzero-total-flux-class-of-a-true-velocity-acceleration-cost.md) 已从原 R56 恢复得到完整速度一形式，并在一个实际 $H_1,H_2$ 组合的真权 $-7$ 上证明总通量商读出非零。本稿继续同一个原式，支付一个更直接的未付门：**原 $U_{-6}$ 的 pure 核中，真实总通量并不恒为零。**

取原实际状态
$$
S_*=(h,k,\omega)=(1,1,1),\qquad
W_6=\Pi_{-6}H_2(S_*).
\tag{1}
$$
这里 $H_2$ 是 [R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、
[R134](R134-acceleration-layer-from-complete-local-v4.md) 的真实正规系数，
$\Pi_{-6}$ 是真成本整权投影。

本稿给出一个明确、连续的 $C^2$ 泛函 $\mathfrak R_6$，使
$$
\boxed{
\Lambda_u(W_6)=
\frac1{1920}\int x\,u''
\left(u\,u''-\frac{(u')^2}{2}\right)(u''')^2
+\mathfrak R_6(u).}
\tag{2}
$$
$\Lambda$ 是 [R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md) 的自然总通量读出，消去整个原真实响应空间 $\mathcal R$。
式 (2) 的余项不是“较低阶”的口头占位：第 3–5 节给出其完整同锚原表达式及连续 $C^2$ 证明。

由 (2) 可在真正紧光滑 profiles 上证明 $\Lambda(W_6)\not\equiv0$。
再用 [R207](R207-complete-weight-minus6-pure-image-equals-three-dimensional-response.md) 已付的
$\pi U_{-6}=\pi\mathcal R_{-6}$，得到一个准确确定的
$$
\boxed{W_6^0\in U_{-6}\cap\ker\pi,\qquad
\Omega_u(W_6^0)\not\equiv0.}
\tag{3}
$$
这关闭了 [R338](R338-weight-minus-six-pure-response-total-flux-and-exact-tail-coordinate.md)
留下的真实 $U_{-6}$ 总通量问题。
它不把 R342 的单个声明输入族零值提升为一般身份，
也没有为得到 (3) 重新消费任何旧机器根。

## 1. 同一原锚与实际 H 规范

全稿固定 $u\in C_c^\infty((\ell,r_*))$，记
$$
v=u',\qquad r=u'',\qquad t=u''',\qquad
J(F)(x)=\int_x^{r_*}F(y)\,dy.
$$
所有 profile 运算采用这个真实右锚。
在 $S_*$，$d=h\omega-k=0$、$e=x$、$Q=1+x^2$。

仍用 R358 的真实速度坐标
$$
\gamma=h_s,\qquad\delta=d_s,\qquad
k_s=2\omega\gamma-2\delta.
$$
其速度面积变换为
$$
\gamma(k_s)_s-k_s\gamma_s
=-2(\gamma\delta_s-\delta\gamma_s)
+\text{速度三次式}.
$$
所以，在 [R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md)
已付的 $\Lambda(\bar A)=0$ 后，
$$
\boxed{
\Lambda(\mathcal H_\gamma)
=-2\Lambda(H_1+2\omega H_2),\qquad
\Lambda(\mathcal H_\delta)=4\Lambda(H_2).}
\tag{4}
$$
第二式的因子是 $+4$；不能只将 $k_s$ 的 $\delta$ 系数 $-2$ 代入而忘记面积本身的另一个 $-2$。

R358 的完整一形式 $\mathfrak C$ 使用 $5\Lambda/4$ 的规范，故
$$
[\delta]\,
\frac{\mathrm d_v\mathfrak C}
{\mathrm d\gamma\wedge\mathrm d\delta}
=15\,\Lambda_u(H_2(S_*)).
\tag{5}
$$
这里 $[\delta]$ 指取速度一次式中的 $\delta$ 系数，不是 profile 导子。

## 2. 原第二局部场的两个完整系数

记原三条同锚 primitive 为
$$
J_0=J(r^2),\qquad J_1=J(xr^2),\qquad
J_2=J(x^2r^2+2v^2).
$$
由 [R76(13)](R76-local-third-exact-loops-and-weight-three-control.md)，
第二局部第一分子 $a=\gamma A+\delta B$ 的两个准确系数是
$$
\boxed{
A=\frac{2Qvr-2xv^2-xQr^2+J_0-J_2}{16},\qquad
B=-\frac{Qr^2+2J_1}{16}.}
\tag{6}
$$
直接求导得
$$
A'=\frac{Qt(v-xr)}8,\qquad B'=-\frac{Qtr}{8}.
\tag{7}
$$
真实左值一般不为零：
$$
A_L=\frac{\mu_0-\mu_2}{16},\qquad
B_L=-\frac{\mu_1}{8},
$$
$$
\mu_0=\int r^2,\quad
\mu_1=\int xr^2,\quad
\mu_2=\int(x^2r^2+2v^2).
\tag{8}
$$
再令
$$
j_A=J(QtA),\qquad j_B=J(QtB),\qquad
F=Qr-2xv+2u.
\tag{9}
$$
因此 $F'=Qt$、$J(Qt)=-F$。
下文不会用“outer 紧”替换 $A_L,B_L$ 或这两个 $j$ 的真实左尾。

## 3. 完整速度外微分的两次准确抵消

R358 已将原 $YC$、$ZZ$ 及两个有序尾一起写成
$$
\mathfrak C=\mathfrak C_0+\mathfrak T_0-\Theta+\Theta_{\rm tail}/3.
\tag{10}
$$
本稿仅在 $S_*$ 对这个已付完整式作代数整理，不重新选择 canonical 场。

先记 $a=\gamma A+\delta B$。
$\mathfrak C_0$ 的第一项是
$$
-\int t\,a(\gamma-x\delta)\,\mathrm d_va.
$$
$-\Theta$ 的真实 $P,B$ 项则给
$$
-\frac12\int t\{a^2+xJ(Qa'^2)\}\,\mathrm d\gamma
+\frac12\int t\{xa^2-J(Qa'^2)\}\,\mathrm d\delta.
$$
两者相加后，其 $\delta$ 外微分系数准确为
$$
\int t\{-J(QA'B')+xJ(QB'^2)\}.
$$
真实 Fubini 给
$$
-\int rQA'B'+\int(xr-v)QB'^2=0
\tag{11}
$$
，因为 (7) 两项逐点相消。
$\gamma$ 系数也同样相消。这不要求 $A,B$ 左紧：
Fubini 的两个 antiderivative 是真正紧的 $r$ 和 $xr-v$。

原
$Ql a'\mathrm d_va'/2$
在此状态已是速度三次梯度，外微分为零。
这是先作准确外微分再消去，不是按 high-jet 大小舍弃。

尾部也有一份必须连同原 $1/3$ 因子处理的准确势。
令 $\alpha=\gamma-x\delta$。R358 的前两个 tail 项与 $\Theta_{\rm tail}/3$ 合为
$$
\frac16\,\mathrm d_v\left\{
a_L\int t\alpha a
\right\}.
\tag{12}
$$
故它们的外微分为零。
$A_L$、$B_L$ 在 (12) 中完整保留；没有单独宣布某个有序尾为零。

## 4. 完整 H2 身份及显式真实余项

把其余各项收齐，定义
$$
\begin{aligned}
\mathscr L(u)=\frac1{16}\int t\bigg\{&
\left((3x^2-1)r-\frac72xv+2u\right)j_B\\
&+(2v-4xr)j_A\\
&+(2ur+v^2-2xvr)B+2vrA
\bigg\},
\end{aligned}
\tag{13}
$$
以及
$$
\begin{aligned}
K_{\gamma\delta}(u)=\frac1{24}\int t\bigg\{&
F\left((1-3x^2)r+\frac72xv-2u\right)\\
&+2ur+v^2-2xvr
\bigg\},
\end{aligned}
$$
$$
K_{\delta\delta}(u)
=\frac1{24}\int t\{(v-2xr)F-vr\}.
\tag{14}
$$
最后的真实尾贡献恰为
$$
\mathscr T(u)=B_LK_{\gamma\delta}(u)-2A_LK_{\delta\delta}(u).
\tag{15}
$$
例如将 R358 剩余 tail 写成 $\mathrm d_va_L\,K(\gamma,\delta)$，
其中 $K=K_{\gamma\gamma}\gamma^2+
K_{\gamma\delta}\gamma\delta+K_{\delta\delta}\delta^2$，
其 $\delta$ 外微分系数就是 (15)。
这说明两个左值的系数与因子 $2$ 来自真实外微分，而非补设。

唯一没有进入 (13)–(15) 的项，是原
$$
\frac{x}{2}\,g\,a'\,\mathrm d_va',
\qquad
g=\gamma(u-xv/2)-\delta v/2.
$$
它的 $\delta$ 外微分系数准确为
$$
\frac{xQ^2}{128}\,
r\left(ur-\frac{v^2}{2}\right)t^2.
\tag{16}
$$
确切地，
$$
\mathrm d_vg\wedge\mathrm d_va'
=\frac{Qt}{8}\left(-ur+\frac{v^2}{2}\right)
\mathrm d\gamma\wedge\mathrm d\delta,
$$
再乘 $xB'/2$ 就得到 (16)。

结合 (5)，完整身份为
$$
\boxed{
\Lambda_u(H_2(S_*))
=\frac1{1920}\int x(1+x^2)^2
r\left(ur-\frac{v^2}{2}\right)t^2
+\frac1{15}\{\mathscr L(u)+\mathscr T(u)\}.}
\tag{17}
$$
这是全部同锚 $H_2$ 收缩，不是只报告 principal。
(13)–(15) 定义的余项保留了原单词、同锚积分和全部左值。

## 5. 为什么显示余项真正连续于 C²

需要证明的是完整 $\mathscr L+\mathscr T$ 的正则性，
不能仅凭 (13) 含一个 $u'''$ 就称其“低阶”。

先给所用的准确原函数消元规则。
若 $a=a(x,u,v)$ 为多项式，$m\ge0$，而 $G$ 是由连续 $C^2$ 密度的同锚 primitives 形成的乘积，则
$$
\begin{aligned}
J(a r^m tG)
={}&-\frac{a r^{m+1}G}{m+1}\\
&-\frac1{m+1}J\{r^{m+1}(a'G+aG')\}.
\end{aligned}
\tag{18}
$$
$a'$ 中只出现 $r$，而这些 $G'$ 仍只依赖 $C^2$ 数据。
右边界的 $r^{m+1}$ 为零；没有使用左端 $G=0$。
同样，
$$
\int a r^m tG
=-\frac1{m+1}\int r^{m+1}(a'G+aG')
\tag{19}
$$
的两个边项由紧 $r$ 支付。

为避免对嵌套 primitive 的正则性作隐含假设，
(18) 对 (9) 直接给出如下两个完整式：
$$
\boxed{
j_B=\frac{Q^2r^3}{48}+\frac{QrJ_1}{8}
+\frac14J(xrJ_1)-\frac1{24}J(xQr^3),}
\tag{20}
$$
$$
\boxed{
\begin{aligned}
j_A=\frac1{16}\bigg\{&
-Q^2vr^2+2xQv^2r+\frac{xQ^2r^3}{3}
-Qr(J_0-J_2)\\
&+J\left(
4x^2v^2r+\frac{Q(1-x^2)}{3}r^3
-2xr(J_0-J_2)\right)
\bigg\}. 
\end{aligned}}
\tag{21}
$$
每个 integrand 只使用 $u,u',u''$ 和同样低阶的原函数。
这些原函数的真实左值仍可非零。

将 (6)、(20)、(21) 放入 (13) 后，
所有剩余 $t$ 都是一次的，并乘一个关于 $r$ 的有限多项式；
其系数只用 $x,u,v$ 及上述 primitives。
逐项用 (19) 即得只依赖 $C^2$ 数据的准确表达式。
(14) 的两个积分没有嵌套困难，直接同法消去 $t$。
最后，(8) 的三个矩也是连续 $C^2$ 泛函。

因此在每个固定紧支撑窗口、固定空 collar 上，
$$
\boxed{\mathscr L+\mathscr T
\text{ 是一个连续的 }C^2\text{ 五次多项式泛函。}}
\tag{22}
$$
这里的多项式允许有限个真正 Volterra 节点。
没有把含 $t^2$ 的 (16) 纳入余项，也没有假设任何单包三矩为零。

## 6. 真权负六的完整分解

对 $u_\epsilon(x)=u(x/\epsilon)$，
R105/R352 的真伸缩给
$$
\Lambda_{u_\epsilon}(H_2(S_*))
=\sum_\sigma \epsilon^{\sigma-2}
\Lambda_u(\Pi_\sigma H_2(S_*)).
\tag{23}
$$
原式全为有限 Laurent 式。特别，连续 $C^2$ 余项的每个 Laurent 系数仍连续于 $C^2$：
可以用有限个固定正伸缩值的可逆 Vandermonde 线性组合提取系数。
这只是有限 Laurent 身份，不执行新的函数秩或评价计算。

定义准确余项
$$
\mathfrak R_6(u)
=\frac1{15}[\epsilon^{-8}]
\{\mathscr L(u_\epsilon)+\mathscr T(u_\epsilon)\}.
\tag{24}
$$
这个定义与 (6)、(8)、(13)–(15)、(20)、(21) 一起完全指定了其原函数值。
它不把一个未读余式声明为零。

(17) 第一项中
$$
x(1+x^2)^2=x+2x^3+x^5.
$$
由于 $r(ur-v^2/2)t^2\,dx$ 缩放为 $\epsilon^{-9}$，
只有第一个 $x$ 项进入 $\epsilon^{-8}$。
故 (23) 的该系数正是 (2)，且 $\mathfrak R_6$ 连续于 $C^2$。
成本权是 $-6$，总通量缩放权是 $-8$；两者没有混用。

## 7. 真正光滑 profiles 上的严格非零

取一个固定真正光滑紧 profile $u_0$，
在某个 $x_0>0$ 有严格正局部最大值，
$$
u_0(x_0)>0,\qquad u_0'(x_0)=0,\qquad u_0''(x_0)<0.
$$
因此
$$
a_0(x)=x\,u_0''(x)
\left(u_0(x)u_0''(x)-\frac{u_0'(x)^2}{2}\right)
$$
在 $x_0$ 为正，且在某个小开区间保持正。
取非零 $\chi\in C_c^\infty$ 支撑于该区间，定义纸面 profile 族
$$
u_N(x)=u_0(x)+N^{-5/2}\chi(x)\cos(N(x-x_0)).
\tag{25}
$$
本稿不运行该族，也不寻找数值阈值。对每个有限 $N$，
它都是同一紧窗口中的真正 $C^\infty$ profile。

直接微分给 $u_N\to u_0$ 于 $C^2$，而
$$
u_N'''=N^{1/2}\chi(x)\sin(N(x-x_0))+O(1)
$$
一致成立。因此 (22)、(24) 给
$\mathfrak R_6(u_N)=O(1)$。
对显式正项，普通分部积分消去 $\cos(2N(x-x_0))$ 后得到
$$
\boxed{
\lim_{N\to\infty}\frac{\Lambda_{u_N}(W_6)}{N}
=\frac1{3840}\int a_0(x)\chi(x)^2\,dx>0.}
\tag{26}
$$
系数的 $C^2$ 小变化在除以 $N$ 后趋零；原 $u_0'''$ 的交叉项也趋零。
不存在需要另行控制的隐藏 $C^3$ 余项。

于是对所有充分大的、但仍有限的 $N$，$\Lambda_{u_N}(W_6)>0$。
这证明
$$
W_6\in U_{-6}\setminus\mathcal R_{-6}.
\tag{27}
$$
这只是严格存在证明，没有执行新研究计算。
共同物理区间可在所有所需有限几何选定后固定；
$u_0,\chi$ 及所有 $u_N$ 均支撑于其同一个正子区间。
原右锚不随 $N$ 改动。

## 8. 原 pure 核中的真实总通量

R207 的完整原式结论是
$$
\pi U_{-6}=\pi\mathcal R_{-6}
=\operatorname{span}(\rho_0,\rho_2,\rho_3),
\qquad \rho_j=\pi R_j.
$$
其中 $R_0,R_2,R_3$ 是 R144/R338 的固定真实响应列。
没有把它们与其他论文的列号混用，也不重新核算旧秩。

令唯一实数 $a,b,c$ 满足
$$
\pi W_6=a\rho_0+b\rho_2+c\rho_3,
$$
并准确定义
$$
R_\pi=aR_0+bR_2+cR_3,\qquad
W_6^0=W_6-R_\pi.
\tag{28}
$$
这三个数是一个已付三维真实函数空间中的唯一坐标；
本稿不编造其机器数值，也不依赖取得数值才能使用 (28)。

由 R130/R134、真权不变性及 $\mathcal R\subset U$，
$$
W_6^0\in U_{-6}\cap\ker\pi.
$$
R352 的自然有序尾读出只依赖 $\pi V$，所以
$$
\boxed{
\Omega_u(W_6^0)=\Lambda_u(W_6^0)
=\Lambda_u(W_6).}
\tag{29}
$$
第一等式使用真正的 $\pi W_6^0=0$；第二等式使用
$\Lambda(\mathcal R)=0$。
于是 (26) 正是一条 pure-zero 原成本的非零真实总通量。

更具体地，R338 的限定 annihilator
$$
\mathcal A_u(V)=\Omega_u(V)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{2}{15}\mu_0\!\left(\int r^3\right)
\ell_{\rm tail}(\pi V)
$$
在整个 $U_{-6}$ 上与 R352 的 $\Lambda$ 相同：
对给定的 $\pi V$ 取 R207 的响应代表，
二者的 pure-dependent 修正都由该同一响应的原 Green 式决定。
因此本稿也得到
$$
\mathcal A_u(W_6)=\Omega_u(W_6^0)\not\equiv0.
\tag{30}
$$
这不是由 R338 的响应表外推 U，而是由 (17)–(26) 新支付了真实 U 的原值。

## 9. 同一个完整式的范围及剩余问题

(17) 还准确显示真权 $-4,-2$ 的相应分解：
它们的 $C^3$ 平方项分别为
$$
\frac1{960}\int x^3r(ur-v^2/2)t^2,\qquad
\frac1{1920}\int x^5r(ur-v^2/2)t^2,
$$
其余项同样连续于 $C^2$。
同一正窗口的 (25) 证明这两个状态值的 $\Lambda$ 也不恒零，
故它们亦不在相应响应子空间。
这里没有为这两个权重新消费 pure 或 self 表；
本稿的显式 pure-kernel 改正 (28) 只使用已经全文列明的权 $-6$ 三基。

新结果不授 whole-self 零，不授全部 mixed period 或全部 ruling。
$\mathcal R$ 不能消去的新商类属于真实成本**线性空间**；
一条指定实际路径的可达性、成本半群的正性或双号、
保持原 $M/T$ 和端口的联合实现都需另证。
尤其不能把 (26) 的 profile 高频族解释成一条已经实现的几何控制路径。

本稿保留全部原左尾与同一个二阶 canonical 选择。
它支付的是原 U 的具体总通量新值，
不是重新评价 R342 的声明族，也不是把一条缺失日志换成新的无穷试验。
