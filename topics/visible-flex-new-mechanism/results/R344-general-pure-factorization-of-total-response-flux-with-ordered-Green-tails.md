# R344：有序 pure 交叉项恢复全部响应的真实总通量

日期：2026-11-15。**完整纸面证明；没有执行新的 profile 积分、原根恢复、符号消元、秩计算或科学运行。**

[R335](R335-complete-response-flux-identity-with-quadratic-tail-Green-correction.md) 证明，一般实紧输入的总通量不能只用无尾的 $16/5$ pure 收缩表示；真实二次左尾给出不可删的 Green 项。[R338](R338-weight-minus-six-pure-response-total-flux-and-exact-tail-coordinate.md) 已在完整权 $-6$ 上证明，这一修正通过已付的三维 pure 像因子化。

本稿将这个结论提升到**全部真实响应、全部权重**。关键不是假设其余权的 pure 秩，而是从原 universal pure 函数在两个真实有序不交输入上的 $2+2$ 系数恢复 Green 项。结果为
$$
\boxed{\Omega_u(\mathcal R\cap\ker\pi)=0
\quad\text{对每个实紧 }u.}
\tag{1}
$$
这里 $\mathcal R$ 是原完整响应空间，$\pi$ 是原正式相位 $-4$ pure 投影，$\Omega_u(V)=\int u'''V(u^2,0)$。没有把 $\mathcal R$ 换成交换子子空间，也没有假定全部第三空间在非仿射导子下闭合。

同时得到一个在原完整 $U$ 上可以直接定义、并杀掉整个 $\mathcal R$ 的有限线性读出。**尚未证明该读出在 $U$ 上非零，也尚未证明它在 $U_{-6}$ 上恒零。** R342 的首次观察仅在声明的有限多项式族上得到零，不支付这两个更强命题。

## 1. 原锚、正式 pure 与真实 Green 修正

全稿固定原共同右 collar $r_*$，
$$
J(F)(x)=\int_x^{r_*}F(t)\,dt,\qquad
u\in C_c^\infty((\ell,r_*)).
$$
允许中间输出有真实二次左尾。没有把任何 primitive 的左值另设为零。

沿 R335，令
$$
q_E(u)=\Phi_E(u,u),\qquad
C(A,B)(a;b,c)=\Phi_A(a,\Phi_B(b,c))-\Phi_B(a,\Phi_A(b,c)),
$$
$$
T_{AB}(u)=C(A,B)(u;u,u).
$$
完整响应的正式 pure 是
$$
\boxed{
\pi\mathcal B_E C(A,B)(u)
=\frac18\{DT_{AB}(u)[q_E(u)]-Dq_E(u)[T_{AB}(u)]\}.}
\tag{2}
$$
因为 $Dq_E(u)[w]=2\Phi_E(u,w)$，这与原 R247/R254 的 $1/8$ 规范完全一致；raw $V(0,u)$ 是它的十六倍。

真实三个矩是
$$
m(a,b)=\left(
\int a''b'',\
\int xa''b'',\
\int(x^2a''b''+2a'b')
\right).
\tag{3}
$$
特别记
$$
\mu(u)=m(u,u),\qquad \nu_E(u)=m(u,q_E(u)).
$$
设 $p_E(n)$ 为 $\Phi_E(a,b)$ 在 $m(a,b)=n$ 时的原二次左尾。原八坐标表为
$$
\begin{array}{c|c}
E&p_E(n)\\ \hline
L=p_0&(n_2-x^2n_0)/4\\
V_0=p_1&-x^2n_1/4\\
Q=p_2&-x^2n_2/4\\
P=r_0&n_0\\
R=r_1&xn_0\\
S=s_0&n_1\\
U_1=s_1&xn_1+n_2/2\\
T_1=t_1&xn_2
\end{array}
\tag{4}
$$
这里 $V_0,U_1,T_1$ 只是二次算子名称，不是完整成本空间或其元素。

对两个二次多项式，
$$
\mathcal G(p,q)=p''q-p'q'+pq''
=2p_2q_0-p_1q_1+2p_0q_2.
\tag{5}
$$
对原右零、左二次的两个输出 $a,b$，完整三次分部积分给
$$
\int a'''b+\int b'''a=-\mathcal G(a_{\rm left},b_{\rm left}).
\tag{6}
$$

为暂时将右侧包的矩与左输入分开，定义一个对 $n$ 线性的量
$$
\begin{aligned}
\mathfrak C_{E;A,B}(u;n)={}&
\mathcal G\{p_E(n),p_A(\nu_B)-p_B(\nu_A)\}\\
&-\mathcal G\{p_A(n),p_B(\nu_E)\}
+\mathcal G\{p_B(n),p_A(\nu_E)\}.
\end{aligned}
\tag{7}
$$
本式中的 $\nu$ 一直由同一个实际 $u$ 给出。令 $n=\mu(u)$ 才得到 R335 的真实修正
$\mathfrak C_{E;A,B}(u)$。R335 已证明
$$
\boxed{
5\Omega_u(\mathcal B_EC(A,B))
-16\int u'''\pi\mathcal B_EC(A,B)(u)
=4\mathfrak C_{E;A,B}(u;\mu(u)).}
\tag{8}
$$
第三对角核 $\chi\in\ker\Delta$ 的响应还满足
$$
\pi\mathcal B_E\chi=0,\qquad \Omega_u(\mathcal B_E\chi)=0.
\tag{9}
$$
原 [R254 完整分解](R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md) 给 $W=W_{71}+\operatorname{span}\{\chi_j\}$，故交换子响应及 (9) 覆盖整个 $\mathcal R$。

## 2. 多项式输入对真实右零输出的作用

令 $p=Ax^2+Bx+C$，$w$ 在共同右 collar 为零，左侧可以有二次尾。原 primitive 直接给
$$
J(p''w'')=-2Aw',\qquad
J(xp''w'')=-2A(xw'-w),
$$
$$
J(x^2p''w''+2p'w')=-2Ax^2w'-2Bw.
\tag{10}
$$
这些式子只用了 $w$ 的**右**零 jets；没有使用左紧性。

置
$$
D_-=\partial_x,\qquad D_0=x\partial_x-1,\qquad
D_+=x^2\partial_x-2x.
$$
将 (10) 代入原八个 $\Phi$，准确得到
$$
\Phi_E(p,w)=\mathscr L_E(p)w,
$$
以及
$$
\begin{array}{c|c}
E&\mathscr L_E(p)\\ \hline
P&-2A D_-\\
R&B D_-\\
S&-2A D_0\\
L&(C/2)D_--(A/2)D_+\\
V_0&(C/2)D_0\\
U_1&B D_0-A D_+\\
T_1&B D_+\\
Q&(C/2)D_+
\end{array}
\tag{11}
$$
这延续 [R259 第 5 节](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md) 的原式，并明确了本次所需的非紧左尾范围。

对固定 $X\in\operatorname{span}\{D_-,D_0,D_+\}$，按原同锚导子定义
$$
q_{X\cdot E}(u)=Xq_E(u)-Dq_E(u)[Xu].
\tag{12}
$$
[R247 第 6 节](R247-complete-response-Jacobi-presentation-and-pure-kernel-decomposition.md) 已证明原八维 $E_8$ 在这三个导子下闭合。因此 (12) 是原 $E_8$ 内的真实方向。这里只使用这个已付事实；不需要整个 $W$ 或 $\mathcal R$ 的 $\delta$ 闭合。

后文出现 $\mathscr L_A(p_E(n))\cdot B$ 时，先把 $n$ 固定为外部常数再使用 (12)。**不在 profile 变分中对 $n=\mu(u)$ 一并微分。** 最后才作该代入。

## 3. 原 pure 函数的有序 $2+2$ 系数

取两个实紧 profile $u,v$，满足
$$
\sup\operatorname{supp}u<\inf\operatorname{supp}v.
\tag{13}
$$
可各自有多个连通支撑。两者仍使用同一个原右锚。

对任意四次 pure 函数 $p$，定义普通多项式系数
$$
\Gamma_p^\to(u,v)=[a^2b^2]\,p(au+bv).
\tag{14}
$$
箭头表示 $u$ 在左、$v$ 在右，不是将两个方向无序平均。这个系数还可用有限原值写成
$$
\Gamma_p^\to(u,v)
=\frac12\{p(u+v)+p(u-v)-2p(u)-2p(v)\}.
\tag{15}
$$
它对原成本线性；不使用新的 profile 求积或机器插值证明。

原二次 integrand 局部，故
$$
\Phi_E(u,v)=0,\qquad q_E(au+bv)=a^2q_E(u)+b^2q_E(v).
\tag{16}
$$
右包的输出在整个左包及其左尾域上准确等于 $p_E(\mu(v))$；左包输出在右包及其右侧准确为零。令
$$
p_E=p_E(\mu(v)),\qquad
L_{AB}=\mathscr L_A(p_B)-\mathscr L_B(p_A).
$$
于是
$$
T_{AB}(au+bv)=a^3T_{AB}(u)+ab^2L_{AB}u+b^3T_{AB}(v).
\tag{17}
$$
没有 $a^2b$ 项。这里 $L_{AB}u$ 真紧，但 $T_{AB}(u)$ 一般保留左尾。

不能只对 (17) 沿非紧 $q_E$ 作一个未经证明的紧域变分。应回到原三个槽重展 (2)。其 $a^2b^2$ 项逐项为
$$
\begin{aligned}
[a^2b^2]DT_{AB}(au+bv)[q_E(au+bv)]
={}&\mathscr L_A(p_E)q_B(u)-\mathscr L_B(p_E)q_A(u)
+L_{AB}q_E(u)\\
&+Dq_A(u)[\mathscr L_B(p_E)u]
-Dq_B(u)[\mathscr L_A(p_E)u],
\end{aligned}
\tag{18}
$$
以及
$$
[a^2b^2]Dq_E(au+bv)[T_{AB}(au+bv)]
=Dq_E(u)[L_{AB}u].
\tag{19}
$$
例如 $\Phi_A(q_E(v),q_B(u))$ 正好是
$\mathscr L_A(p_E)q_B(u)$。$q_B(u)$ 虽可有左尾，但它在左包右侧为零，故整个原积分只见到右包输出的真实多项式尾；(10) 适用。没有将 $q_B(u)$ 假设为紧。

对任意固定 $n$ 定义原二次方向
$$
\boxed{
\begin{aligned}
\mathcal J_{E;A,B}(n)={}&
\mathscr L_A(p_E(n))\cdot B
-\mathscr L_B(p_E(n))\cdot A\\
&+\{\mathscr L_A(p_B(n))-\mathscr L_B(p_A(n))\}\cdot E.
\end{aligned}}
\tag{20}
$$
由 (12)、(18)、(19)，完整有序 pure 系数是
$$
\boxed{
8\Gamma_{\pi\mathcal B_EC(A,B)}^\to(u,v)
=q_{\mathcal J_{E;A,B}(\mu(v))}(u).}
\tag{21}
$$
这是原函数恒等，特别保留全部左尾，不是只比较局部主项。$1/8$ 来自正式 (2)，没有另行极化归一化。

## 4. 有序系数的收缩恰给真实 Green 项

记
$$
h_E(u)=\int u'''q_E(u).
$$
R335 的完整三阶伴随为
$$
D^3\Phi_E(a,w)
=D^2(g_E[a]D^2w)+D(h_E^{\rm op}[a]Dw)+c_E[a]w.
\tag{22}
$$
当 $a=u$ 紧时，三个系数都紧。因而即使另一个输出有真实左尾，原 Green 交换仍合法。

对紧方向 $w$，(22) 给
$$
\int u'''\Phi_E(u,w)=\int w'''q_E(u),
\qquad
\boxed{Dh_E(u)[w]=3\int w'''q_E(u).}
\tag{23}
$$
这里的因子 3 来自一个 outer 变分与两个原对称 inner 变分。

对三个一阶场 $X=D_-,D_0,D_+$，逐次分部积分给
$$
\int u'''Xq+\int(Xu)'''q=0
\tag{24}
$$
对任意原右零 $q$ 成立。端项均被紧 $u$ 的 jets 消掉。由 (12)、(23)，
$$
h_{X\cdot E}(u)=-3\int(Xu)'''q_E(u).
\tag{25}
$$

现在固定一个二次多项式 $p$。令 $a=\Phi_A(u,q_B(u))$；其真实左尾是 $p_A(\nu_B)$。用 (22) 的紧系数自伴性，先得
$$
\int\{\mathscr L_A(p)u\}'''q_B
=\int p\,D^3\Phi_A(u,q_B)=\int p\,a'''.
$$
最后一步必须保留原左端：
$$
\boxed{
\int\{\mathscr L_A(p)u\}'''q_B
=-\mathcal G\{p,p_A(\nu_B)\}.}
\tag{26}
$$
因为 $p'''=0$，右端 $a$ 全零，而左端恰为 (5)。这一步没有将有尾的三阶配对冒作反对称。

结合 (25)，得到
$$
h_{\mathscr L_A(p)\cdot B}(u)
=3\mathcal G\{p,p_A(\nu_B)\}.
\tag{27}
$$
将 (20) 的四项逐项代入 (27)，正好给
$$
\boxed{
h_{\mathcal J_{E;A,B}(n)}(u)
=3\mathfrak C_{E;A,B}(u;n).}
\tag{28}
$$
因此 (21) 的实际收缩是
$$
\boxed{
\int u'''\Gamma_{\pi\mathcal B_EC(A,B)}^\to(u,v)
=\frac38\,\mathfrak C_{E;A,B}(u;\mu(v)).}
\tag{29}
$$

(29) 的两个范围都不能省略：右包矩是实际 $\mu(v)$；右包必须位于整个 $u$ 的右侧。没有把任意抽象三向量直接宣称为某个实紧 profile 的矩。

## 5. 三条真实右包恢复左包的三个矩

给定非零实紧 $u$，其支撑与右锚之间有一个非空开区间。在其中选择三个互不交、同形、同宽的非零实偶 bump 平移
$$
v_j(x)=\eta(x-c_j),\qquad c_1<c_2<c_3,
$$
使它们均在整个 $u$ 的右侧。无需将其作为新的几何或合法圆输入；这里是在原 universal pure 函数上定义有限观测。

令
$$
a_\eta=\int(\eta'')^2>0,\qquad
b_\eta=\int\{t^2(\eta'')^2+2(\eta')^2\}.
$$
偶性给
$$
\mu(v_j)=(a_\eta,a_\eta c_j,a_\eta c_j^2+b_\eta).
\tag{30}
$$
所以真实矩矩阵
$$
M=[\,\mu(v_1)\ \mu(v_2)\ \mu(v_3)\,]
$$
满足
$$
\det M=a_\eta^3(c_2-c_1)(c_3-c_1)(c_3-c_2)\ne0.
\tag{31}
$$
这只是三个明确平移矩的 Vandermonde 恒等，不是新数值秩。

定义真实系数
$$
(c^{\,u}_1,c^{\,u}_2,c^{\,u}_3)^t=M^{-1}\mu(u).
\tag{32}
$$
这些系数可以有符号；它们是**线性读出的系数**，不要求实际负幅微包或有符号几何成本的实现。

对固定 $u$，(7) 对 $n$ 线性。故 (29) 与 (32) 给
$$
\boxed{
\mathfrak C_{E;A,B}(u;\mu(u))
=\frac83\sum_{j=1}^3 c^{\,u}_j
\int u'''\Gamma_{\pi\mathcal B_EC(A,B)}^\to(u,v_j).}
\tag{33}
$$
$u=0$ 时全式为零，可单独取零读出，无需求逆任何依赖 $u$ 的矩阵。

## 6. 全部真实响应的 pure 因子化

将 (33) 代入 (8)，得到
$$
\boxed{
\begin{aligned}
\Omega_u(V)={}&
\frac{16}{5}\int u'''\pi V(u)\\
&+\frac{32}{15}\sum_{j=1}^3c^{\,u}_j
\int u'''\Gamma_{\pi V}^\to(u,v_j),
\qquad V\in\mathcal R.
\end{aligned}}
\tag{34}
$$
对交换子响应，这是上文逐槽证明的结果；对全部 $\chi$ 响应，$\pi=0$ 和 $\Omega=0$ 由 (9) 同时成立。R254 的真实分解遂支付整个 $\mathcal R$，不需要猜测其完整 pure 核。

若 $\pi V=0$ 作为原 universal pure 函数，则它在 $u$、$v_j$、$u\pm v_j$ 上都为零，故 (34) 给 (1)。特别
$$
\boxed{\Omega_u(\mathcal R\cap\ker(\pi,\mathcal Q))=0.}
\tag{35}
$$
这是 (1) 的子空间后果；$\mathcal Q$ 是原 universal self 坐标。没有声称 $\mathcal Q=0$ 单独足够。

(34) 对每个实紧 $u$ 成立，不要求 $\mu(u)=0$。它也没有撤回 R335 的反例：所增加的是可由 **pure 的有序交叉值** 读取的尾修正，而不是把原 Green 项消掉。

### 6.1. 原反例校准

对 $V_*= \mathcal B_LC(P,R)$，R335 已得
$$
\mathfrak C_{L;P,R}(u;n)=\frac16n_0M_3,\qquad
M_3=\int(u'')^3.
$$
故 (29) 给
$$
\int u'''\Gamma_{\pi V_*}^\to(u,v)
=\frac1{16}\mu_0(v)M_3.
$$
(32) 再给
$$
\frac{32}{15}\sum_jc^{\,u}_j
\int u'''\Gamma_{\pi V_*}^\to(u,v_j)
=\frac{2}{15}\mu_0(u)M_3.
\tag{36}
$$
正好恢复 R335 的非零原尾。这里不能将 $V_*$ 误标为 pure-zero。

## 7. 在原 U 上定义的全响应 annihilator

对任意原完整成本 $V\in U$，使用同一个已选择的 $u,v_1,v_2,v_3$ 与 (32)，定义
$$
\boxed{
\begin{aligned}
\Lambda_{u,\mathbf v}(V)={}&\Omega_u(V)
-\frac{16}{5}\int u'''\pi V(u)\\
&-\frac{32}{15}\sum_{j=1}^3c^{\,u}_j
\int u'''\Gamma_{\pi V}^\to(u,v_j).
\end{aligned}}
\tag{37}
$$
这是一个真正线性泛函，且
$$
\boxed{\Lambda_{u,\mathbf v}|_{\mathcal R}=0.}
\tag{38}
$$
没有预先要求 $\pi V\in\pi\mathcal R$，所以也没有把某个未知奇权的 pure 像或完整 $U$ 的 pure 像偷换成响应像。

固定 $u,\mathbf v$ 后，(15) 表明 (37) 只用有限个原 pure 输出函数及一个真实 self 输出函数。其积分是原数学泛函的定义，不是本稿执行的新 evaluator 或科学计算。

在 $\mathcal R$ 上，任意符合条件的三个辅助包都给同一个 (34)。但对一般 $V\in U$，本文不证明 (37) 与辅助包选择无关，也不证明它非零。

在已付的权 $-6$ 上，[R207](R207-complete-weight-minus6-pure-image-equals-three-dimensional-response.md) 给
$\pi U_{-6}=\pi\mathcal R_{-6}$。因此对任意 $V\in U_{-6}$，可用一个响应代表其 pure，(33) 的读出正是 R338 的
$$
\frac{\mu_0M_3}{6}\ell_{\rm tail}(\pi V).
$$
从而
$$
\boxed{\Lambda_{u,\mathbf v}(V)=\mathcal A_u(V)\quad(V\in U_{-6}),}
\tag{39}
$$
这里 $\mathcal A_u$ 是 R338(21)。在这一已付空间内辅助包选择无关。若 $\pi V=0$，则任何权上都直接有
$$
\Lambda_{u,\mathbf v}(V)=\Omega_u(V).
\tag{40}
$$

## 8. 相邻权 $-5$ 的完整 Green 余项

本节只从原尾表 (4) 手展相邻权，展示 (34) 怎样清掉此前不能由偶权 pure 表推断的余项；没有求新的 pure 秩。

记
$$
r=u'',\quad v=u',\quad
M_3=\int r^3,\quad N_3=\int vr^2,\quad X_3=\int xr^3,
$$
$$
A=\mu_0N_3,\qquad B=\mu_0X_3,\qquad C=\mu_1M_3.
$$
原二导和普通分部积分给
$$
\begin{aligned}
(\nu_P)_0&=0,&(\nu_P)_1&=2M_3/3,&
(\nu_P)_2&=4X_3/3-2N_3,\\
(\nu_R)_0&=(\nu_S)_0=-M_3/3,&
(\nu_R)_1&=X_3/3-N_3,&(\nu_S)_1&=X_3/3,\\
(\nu_L)_0&=-N_3/2,&
(\nu_{U_1})_0&=N_3-X_3.
\end{aligned}
\tag{41}
$$
例如 $q_L''=(u-xv)r'-(xr^2+Jr^2)/2$，其中
$\int rJ(r^2)=\int vr^2$，故原非紧 $J$ 项确实参与 $(\nu_L)_0$。

下表列出全部 28 个交换子生成标签。括号方向严格按显示顺序，不是旧文件原列号；表内值为 $\mathfrak C_{E;A_0,B_0}(u;\mu(u))$。

| 外 $E$ | 第三交换子 $C(A_0,B_0)$ | 完整 Green 项 |
|---|---|---|
| $P$ | $C(P,Q)$ | $4B/3-2A$ |
| $P$ | $C(R,V_0)$ | $B/6-A/2$ |
| $R$ | $C(P,V_0)$ | $B/6-A/2+C/6$ |
| $V_0$ | $C(P,R)$ | $C/6$ |
| $P$ | $C(S,V_0)$ | $B/6$ |
| $S$ | $C(P,V_0)$ | $B/6+C/2$ |
| $V_0$ | $C(P,S)$ | $C/2$ |
| $P$ | $C(R,T_1)$ | $4B/3-2A$ |
| $R$ | $C(P,T_1)$ | $4B/3-2A$ |
| $T_1$ | $C(P,R)$ | $0$ |
| $P$ | $C(S,T_1)$ | $0$ |
| $S$ | $C(P,T_1)$ | $0$ |
| $T_1$ | $C(P,S)$ | $0$ |
| $L$ | $C(P,L)$ | $B/6$ |
| $U_1$ | $C(P,U_1)$ | $2C/3$ |
| $P$ | $C(L,U_1)$ | $5B/6-A$ |
| $L$ | $C(P,U_1)$ | $5B/6-A$ |
| $U_1$ | $C(P,L)$ | $0$ |
| $R$ | $C(R,L)$ | $A/2$ |
| $S$ | $C(S,L)$ | $-B/6-C/3$ |
| $R$ | $C(S,L)$ | $A/2-B/6-C/6$ |
| $S$ | $C(R,L)$ | $-C/6$ |
| $L$ | $C(R,S)$ | $B/6-A/2$ |
| $R$ | $C(R,U_1)$ | $5B/3-3A+C/3$ |
| $S$ | $C(S,U_1)$ | $0$ |
| $R$ | $C(S,U_1)$ | $B/3$ |
| $S$ | $C(R,U_1)$ | $B/3+C/3$ |
| $U_1$ | $C(R,S)$ | $C/3$ |

穷尽性只用已发表真权：
$E_8$ 为 $(-1,0,1,-3,-2,-2,-1,0)$；
三算子权和 $-5$ 的四种组合是
$(-3,-3,1),(-3,-2,0),(-3,-1,-1),(-2,-2,-1)$，分别给 $1,12,5,10$ 个上述标签。

另八条生成方向是外 $L,U_1$ 配 $\chi_{30}$，外 $R,S$ 配 $\chi_{32},\chi_{34}$，外 $P$ 配 $\chi_{37},\chi_{100}$；它们的 $\pi,\Omega$ 均零。使用 R254 的原完整提升把相应 $\tau_j$ 换成 $\chi_j$，只是一项已付线性换基。

因此这 28+8 条覆盖权 $-5$ 的全部原响应。**36 是生成标签数，不是本稿声称的真实秩。** 对其中任意实际 pure-zero 组合，(33) 强迫上表的 $A,B,C$ 聚合值为零，继而由 (8) 得 $\Omega=0$。这不需要一张尚未发布的 $\pi\mathcal R_{-5}$ 坐标表，也不从权 $-6$ 或 $-4$ 的已付维数外推奇权维数。

## 9. R342 的结果与尚未消失的 U 问题

首次新观察 [run **43745111286**](https://github.com/Rogerhu12/math-research-public/actions/runs/43745111286)、job **132906586198**、source
**f9f4030bfea092d5dfd82cf1989a0e13e73c1cdb** 已完成。其固定原 $U_{-6}$ pure-zero 目标是
$$
A_*=N^7G+\frac{315}{32}R_0+\frac{315}{16}R_2-\frac{315}{32}R_3.
$$
[原观察入口](../scripts/literature_weight_minus6_total_flux_observer.py) 只读取已存完整 mixed 根，实际新观察在声明的
$$
u_\lambda(x)=
t^8(1-t)^8\{1+\lambda(2t+3t^2+5t^3)\},\qquad
t=x-2,\quad 2\le x\le3
$$
及外部零延拓上，得到 $\Omega_{u_\lambda}(A_*)$ 的全部 $\lambda$ 系数为空表，即该族多项式恒零。输出状态为
$ \texttt{declared\_family\_zero\_universal\_functional\_unresolved}$，
报告 SHA-256 为
$\texttt{fafb8df1127d9a675db9fe265cb3aa972f8212410ac5ad3eabd404384b33a36f}$。
这是原已完成运行的结果引用，本稿没有重跑。

该输入的零延拓为有限阶平端 $C^7$，不是直接称为 $C^\infty$。实际没有非零 witness，故也没有可由光滑逼近推出的非零原紧函数结论。

本稿的新定理只证明 $\Omega$ 对所有权的 **response pure 核** 为零，以及可用 (37) 在全部 $U$ 上定义真正的 response annihilator。它既不证明 $A_*\in\mathcal R$，也不证明 $\Lambda(A_*)$ 在所有紧输入上恒零。一个特定族上的零不能补上这一步。

## 10. 对实际 period 控制的准确影响

全权结论 (1) 说明：一旦保持整个 universal pure，响应不能独立改变这个总通量读出。这超出了 R338 的单权结论，也超出了某个 $\mathcal K$ 导子串的零身份。

另一方面，只有证明某个原 $U$ 成本在 (37) 下非零，才会得到真实的新响应商障碍。若该读出在相关 $U$ 上恒零，它就只是原几何成本自身满足的兼容身份。本文不把这两个方向之一当作既成事实。

[R340 的两个内部退化通量](R340-local-whole-pure-self-kernel-and-two-actual-degenerate-flux-controls.md) 仍可由具体 whole pure/self 核方向改变；它们与这里的**整个包总通量**是不同读出。本稿没有用两个点代表全部 period，也没有把辅助 pure 观测转化成新的几何控制权限。

下一最小问题是从原完整 $U_{-6}$ 成本的真实 mixed 输出证明或否定 $\Lambda(A_*)\equiv0$，而不是再求旧 pure/self/rank，或仅换一个数值输入族。全空间 $U/\mathcal R$ 的其他读出、平台及退化点兼容、同一二阶 gauge 的全 period 和主课题的固定度量有限嵌入族，均未由 (34) 或 (38) 自动完成。
