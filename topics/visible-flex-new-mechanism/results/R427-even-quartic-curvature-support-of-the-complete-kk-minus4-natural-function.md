# R427：完整负四 kk 自然函数的偶四次曲率支撑与两个剩余读出

日期：2026-11-16。**完整原式纸面证明；没有执行新的 profile、积分、符号程序、秩、旧根研究、开发检查或科学运行。**

定义原完整正规系数
$$
V_{kk}(k)=[h^{-4}(\log h)^0]\widehat Q_{kk}(h,k,0).
$$
这里 $kk$ 是物理速度 $k_s^2$，真成本权为 $-4$；先作全部原历史导数和水平加速度分部积分，最后才限制 $\omega=0$。

本稿证明：存在三个实际原系数
$$
V_j=[h^{-4}k^j\omega^0(\log h)^0]\widehat Q_{kk},
\qquad j=0,2,4,
$$
使完整自然函数准确满足
$$
\boxed{
\Lambda_u(V_{kk}(k))
=\Lambda_u(V_0)+k^2\Lambda_u(V_2)+k^4\Lambda_u(V_4)
\quad\forall k,\quad u\in C_c^\infty(I).
}
\tag{1}
$$
所有奇次以及 $k$ 次数大于四的完整自然系数都为零。式(1)不声称原成本算子本身也只有这三项；其余项可能落在自然核中。

因此独立的 $k=0$ 锚付清后，只剩 $V_2,V_4$ 两个必要读出。本稿不计算它们的 $\Omega$，不由单锚猜乘 $(1+k^2)$，也不把两个标签数称为函数秩。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R367](R367-exact-N2-Green-contraction-and-nonzero-quartic-velocity-correction.md)独立的完整势/Green 身份、
[R418](R418-complete-kk-minus-six-natural-coefficient-and-common-query-cancellation.md)、
[R421](R421-all-curvature-kk-minus6-natural-identity-and-common-character-cancellation.md)及
[R423](R423-complete-static-potential-inputs-for-the-all-curvature-kk-minus4-coefficient.md)。
下面保 R423 新出现的四个势槽。

## 1. 固定右锚、完整正规式和水平导数

始终使用同一个真实右 collar，
$$
JF(x)=\int_x^{r_*}F(y)\,dy.
$$
outer profile 紧，二、三次恢复输出允许有其真实二次左尾，不将它们设为紧场。

沿 $h_s=h_{ss}=0$ 切片，令
$$
w=k_s,\qquad \beta=k_{ss},\qquad
Y=\partial_k+\frac1{2h}\partial_\omega.
\tag{2}
$$
原水平关系 $\omega_s=w/(2h)$ 保留。若完整密度为
$w^2\mathscr R+\beta\mathscr A$，则正规 $kk$ 是
$$
\mathscr R-Y\mathscr A.
\tag{3}
$$
真实端 germs 使 $w\mathscr A$ 的边势为零；这不删除其它 profile 尾或静态势。

原完整速度二次层仍为
$$
\widehat Q_2
=\operatorname{IBP}\left(
v_2-\mathcal B_{m_0}N_2-\mathcal B_{m_2}N_0
\right)-\Gamma(m_2).
\tag{4}
$$
采用原完整自然函数
$$
\Lambda_u(V)=\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
\tag{5}
$$
三个矩、正式 pure 和有序 $2+2$ 尾均取原规范。

R367 对任意八方向的完整 Green 身份，准确允许在(5)中将
$C_Aq_0$ 的 $-4\int a'a(u,q_0)$ 与
$-\mathcal B_{m_0}N_2$ 配对消去。它不消去静态 $b(u,q_2)$ 链、$-\Psi(u,n)$、$ZZ$ history 或 $-\mathcal B_{m_2}N_0$。

这是**自然层**的消项，不声称成对项的 raw self、pure 或尾各自零。若后继执行采用旧 paid pure 坐标，仍须装配原完整 raw self 后再校正，不能直接用下面已配对消项的 raw scalar 套旧 pure 行。

## 2. 保原全状态的两级支撑记号

暂不限制 $\omega$。令
$$
z=x+\omega,\qquad e=hz-k,\qquad Q=1+e^2,\qquad
S=1+k^2,\qquad K_0=kz^2-\frac{Sz}{h}.
$$
先将所有 $e$ 展成 $hz-k$。把 $z$、profile、原 $J$ 及其 $z$ 平移微分看成系数；它们不含新的 $h,k$ 幂。

定义 $\mathcal C_{m,\epsilon}$ 为有限 Laurent 多项式之类：
$$
F=\sum_{j\in\mathbb Z,\ \ell\ge0}
h^jk^\ell F_{j\ell},
\qquad
j+\ell\le m,\qquad
j+\ell\equiv\epsilon\pmod2 .
\tag{6}
$$
这是完整原式的次数上界和奇偶约束，不是原成本真权的重新定义，也不假各项达到上界。

乘积使两个 $m$ 相加、两个 $\epsilon$ 模二相加；$x$ 微分、同锚 $J$、profile 积分和极化都保持该类。乘 $h^a$ 或 $k^a$ 同时把 $m,\epsilon$ 平移 $a$。

尤其在一般状态先作用(2)时，
$$
\boxed{Y\mathcal C_{m,\epsilon}
\subset\mathcal C_{m-1,\epsilon+1}.}
\tag{7}
$$
$\partial_k$ 使 $k$ 幂减一；另一项只微分 $z$ 及同锚系数，再乘 $1/(2h)$。两者都使 $j+\ell$ 减一。这个证明在限制 $\omega=0$ 前成立，不能从一个已经置零的局部分量推断其 $Y$ 导数也为零。

对完整标量，也可使用 R421 的准确等价式
$$
[h^{-4}]Y\mathscr A\big|_{\omega=0}
=\partial_k\mathscr A_{-4}
+\frac12\partial_{\rm c}\mathscr A_{-3},
\tag{8}
$$
其中 $\partial_{\rm c}$ 输运整个 profile、primitive 与真实左矩。后面两项都保留。

## 3. 原二次与静态第三场的支撑

记
$$
p=u',\quad r=u'',\quad t=u''',\quad
P=J(r^2),\quad M_z=J(zr^2),
$$
$$
L_z=p-zr,\quad G_z=u-zp/2,\quad
H_z=z^2r-2zp+2u.
$$
本稿 $H_z$ 是局部 jet，不是正规 H 层。原 $k_s$ 方向第二局部分子为 $(wA,b,ewA)$，其中
$$
A=\frac{Sr^2}{32h^3}
-\frac{k(zr^2+P)}{16h^2}
+\frac{z^2r^2+2M_z}{32h}.
\tag{9}
$$
静态 $b,q_0$ 在 $\omega=0$ 的完整式为
$$
b=\frac{SR}{8h}+kb_0+hb_1,
$$
$$
q_0=-\frac{S^2R}{8h^2}+\frac{kSE}{h}
+k^2V-\frac{ST}{8}-\frac{kh}{2}\mathbf Y(u,u),
\tag{10}
$$
沿 R417 的原 $R,T,E,V,b_0,b_1$ 定义。一般状态把相应完整算子的坐标写成 $z$，同样具有(10)的支撑，真实右锚不变。也可直接用原完整
$
q_0=(kz-S/h)b+G_z^2/2
$
核对这一一般状态界；不是仅从 $\omega=0$ 的瞬时值猜其水平导数。

原物理 $kk$ 矩阵及静态二阶投影为
$$
q_2=m_{2,kk}(u,u)
=\frac{kP}{16h^3}-\frac{M_z}{16h^2},
\qquad
A_u=K_0r-K_0'p+2ku=\frac{SL_z}{h}+kH_z.
\tag{11}
$$
由(9)—(11)直接有：

| 原量 | 所属类 |
|---|---|
| $e,\ K_0,\ A_u,\ b$ | $\mathcal C_{1,1}$ |
| $Q,\ q_0$ | $\mathcal C_{2,0}$ |
| $A$ | $\mathcal C_{-1,1}$ |
| $q_2$ | $\mathcal C_{-2,0}$ |
| $YA,\ Yb$ | $\mathcal C_{-2,0},\ \mathcal C_{0,0}$ |

表(12)。例如 $q_0$ 的 $h^{-2}S^2,h^{-1}kS,k^2,S,hk$ 各有 $j+\ell\le2$ 且总偶；并未把 $S$ 当成独立变量。

对右零但可有左尾的 $q$，原
$$
c_q(q)=\frac{Qr q'}{16h^2}
+\frac{(hp-er)q}{8h}
+\frac{J(Qr q''+2h^2p q')}{16h^2}.
$$
完整第三局部第一分子为
$$
c=c_0+\beta C_b+w^2C_v,
$$
$$
c_0=-\frac{G_zb'}{4h}+\frac{L_zb}{8h}+c_q(q_0),
\qquad
C_b=-\frac{J(QtA)}{8h^2},
$$
$$
C_v=-\frac{QrA'}{16h^3}
-\frac{YJ(QtA)}{8h^2}+c_q(q_2).
\tag{13}
$$
这是 R418 的全部原 $P_s$、$\eta$ 恢复，含 $-P(Y,Y_q)$，不只保最高 jet。逐项用(7)(12)得
$$
\boxed{
c_0\in\mathcal C_{2,0},\qquad
C_b\in\mathcal C_{-1,1},\qquad
C_v\in\mathcal C_{-2,0}.
}
\tag{14}
$$

## 4. 完整线性第三密度 n1，而非只用已列的最低三幂

原 $n_1=[w]n$ 的较高 $h$ 幂也会进入本次 $h^{-4}$，不能仅引用 R421 的 $h^{-5},h^{-4},h^{-3}$ 表。

先对独立 outer $f$ 与 inner $g^2$ 写完整式。将 $A,b,q_0$ 取为由 $g$ 生成的原二次函数，令
$$
G_f=f-zf'/2,
$$
$$
P_{f,A}=
\frac{(Qf''-hef')A+J(Qf'''A)}{4h},
\qquad
B_{f,A}=
\frac{(hef-Qf'/2)A}{2h}.
$$
原 R56/R73 直接给
$$
\boxed{
\begin{aligned}
n_1(f;g^2)={}&
\frac{G_f}{2h}\{Yb+(k+e)A\}
-\frac{f'b}{8h^2}\\
&+K_0P_{f,A}+\frac{K_0}{z}B_{f,A}
-\frac{f'q_0}{8h}
-\frac{J_e(f,q_0)}{16h^3}.
\end{aligned}}
\tag{15}
$$
最后两项就是完整 $-\Psi_{w=1}(f,q_0)$，不能删去。

为核原来源，$\nabla_sY_f$ 的 normal 分子是 $hG_f$，第三分子的线性速度项为 $wf'/4$。对
$K_g=(wA,b,ewA)$，其 normal 速度项为
$w\{Yb+(k+e)A\}$，第三静态项为 $-b$。故原 $T_s/(2h^2)$ 恰给(15)第一行。原 $K_0P+(K_0/z)B$ 给第二行前两项。$\gamma=0$ 时，$-\lambda P_s$ 只从这份配对产生 $w\beta,w^3$，不进入线性 $w$ 槽；$\gamma B_s$ 为零。最后按 R73 的
$\Psi_w=f'q_0/(8h)+J_e(f,q_0)/(16h^3)$ 扣除，得到(15)。

这里 $K_0/z=kz-S/h$，所以未留下一个额外有理 $k$ 系数。所有 $J$ 与原左值保真；(15)适用于本次响应所需的非紧 outer。

用(12)逐项检查：
$P_{f,A}\in\mathcal C_{0,0}$，
$B_{f,A}\in\mathcal C_{0,0}$；
$K_0$ 与 $K_0/z$ 都在 $\mathcal C_{1,1}$。
第一行至多 $\mathcal C_{-1,1}$，最后两项至多 $\mathcal C_{1,1}$。
因此
$$
\boxed{n_1\in\mathcal C_{1,1}.}
\tag{16}
$$
它完整包括本次需要的 $h^{-1},h^{-2},h^{-3}$，不是对未知高幂作外推。

可用已付最低幂作一个独立原式对照。对角 $f=g=u$ 时，(15)的 $h^{-5}$ 是
$$
-\frac{S^3}{128}\{2xr^3/3-pr^2\}
+\frac{S^3}{128}J(2rL_x\,t).
$$
原同锚 IBP 给
$$
J(2rL_x\,t)=-pr^2+\frac23xr^3-\frac13J(r^3).
$$
于是准确回到
$$
[h^{-5}]n_1=-S^3J(r^3)/384,
\tag{17}
$$
其中 $L_x=p-xr$；这与 R421 的真实最低槽一致。其左常数未设零。

## 5. 全部 YC/ZZ 标量及水平正规导数的支撑

配对消去第1节明确的 $C_A/N_2$ 后，R418 原四个标量为
$$
\mathscr A_Y=\int\left\{
\frac{QA_u t C_b}{2h}-4A'c_0\right\},
$$
$$
\mathscr R_Y=
\int\frac{QA_u t C_v}{2h}
-\int\frac{tG_z}{2h}b(u,q_2)+\mathscr D(n_1),
$$
$$
\mathscr D(f)=\int\frac{r^2f}{8h}
-\int\frac{Qr^2f''}{16h^3}.
\tag{18}
$$
$\mathscr D$ 是完整 $-\int t\Psi_w(u,f)$。它的降阶只用紧 outer 的两 collar；允许 $f$ 有真实左尾。

原 $ZZ$ 为
$$
\mathscr A_Z=
\int\left\{
\frac{tA}{h^2}
\left(\frac Q2q_0'-(k+e)b-ehq_0\right)
-\frac{r(b')^2}{4h^3}
\right\},
\tag{19}
$$
$$
\begin{aligned}
\mathscr R_Z=\int\bigg\{&
\frac t{h^2}(D_0D_2+E_0E_2+M_1^2/2)\\
&+\frac{A_u}{2h}\{Q(A')^2+2heAA'+h^2A^2\}\\
&+\frac{(ke-1)tQA^2}{2h^2}
-\frac t{h^2}P_{A,q_0}
\bigg\},
\end{aligned}
\tag{20}
$$
其中
$$
D_0=q_0'/2-kb,\quad E_0=eq_0'/2-b-hq_0,
$$
$$
D_2=YA+q_2'/2,\quad E_2=eD_2-A/2-hq_2,
\quad M_1=Yb+(k+e)A,
$$
$$
P_{A,q_0}=
\{(Qq_0''-heq_0')A+J(Qq_0'''A)\}/(4h).
\tag{21}
$$
最后一项保原两份 history 交叉，不省略其外 $1/2$ 或左尾。

由前节得完整表：

| 原量 | 所属类 |
|---|---|
| $D_0,E_0$ | $\mathcal C_{2,0},\ \mathcal C_{3,1}$ |
| $D_2,E_2,M_1$ | $\mathcal C_{-2,0},\ \mathcal C_{-1,1},\ \mathcal C_{0,0}$ |
| $P_{A,q_0}$ | $\mathcal C_{2,0}$ |
| $\mathscr A_Y,\mathscr A_Z$ | $\mathcal C_{1,1}$ |
| $\mathscr R_Y,\mathscr R_Z$ | $\mathcal C_{0,0}$ |
| $Y\mathscr A_Y,Y\mathscr A_Z$ | $\mathcal C_{0,0}$ |

表(22)。例如：

- $\mathscr R_Y$ 的第一项由 $(QA_u/h)\in\mathcal C_{2,0}$ 和 $C_v\in\mathcal C_{-2,0}$ 得总类 $\mathcal C_{0,0}$。
- $b(u,q_2)/h$ 至多 $\mathcal C_{-2,0}$；$\mathscr D(n_1)$ 的两项均至多 $\mathcal C_{0,0}$。
- $\mathscr R_Z$ 中 $E_0E_2/h^2$、metric 三项、$(ke-1)QA^2/h^2$ 和 $P_{A,q_0}/h^2$ 都在 $\mathcal C_{0,0}$；其余项有更低上界。
- 加速度标量先属于 $\mathcal C_{1,1}$，必须再用(7)，而非先把一般 $Y$ 删掉。按(8)，其 $h^{-4}$ 直接 $k$ 导数和 $h^{-3}$ 中心导数都只给偶次、最高 $k^4$。

因此原正规差
$$
(\mathscr R_Y-Y\mathscr A_Y)
-(\mathscr R_Z-Y\mathscr A_Z)
\in\mathcal C_{0,0}.
\tag{23}
$$
提取 $h^{-4}$ 时，(6)强制
$$
\ell\le4,\qquad \ell\equiv0\pmod2.
\tag{24}
$$
这是从完整原密度得到的偶四次支撑，不使用有限曲率采样或旧 pure 列的次数。

## 6. 原 N0 四势、Gamma 及两份真尾

R423 的完整独立 outer 公式已付
$$
[N_0]_{h^{-2}}=S(\tau_0+k^2\tau_1),\qquad
[N_0]_{h^{-1}}=k(\tau_2+k^2\tau_{2b}).
$$
由原
$$
m_{2,kk}=\frac{k\mathbf P}{16h^3}-\frac{\mathbf S}{16h^2},
$$
本次势准确为
$$
\boxed{
-[h^{-4}]\mathcal B_{m_{2,kk}}N_0
=\frac S{16}\mathcal B_{\mathbf S}(\tau_0+k^2\tau_1)
-\frac{k^2}{16}\mathcal B_{\mathbf P}(\tau_2+k^2\tau_{2b}).
}
\tag{25}
$$
四个 $\tau$ 都是与 $h,k$ 无关的完整三槽算子，其 true outer、原左尾和参考规范保持 R417/R423。式(25)显然也只有 $k^0,k^2,k^4$，但第二组没有显式 $S$ 因子，不能把它删掉后宣布整式可除以 $S$。

$\Gamma(m_{2,kk})$ 只有 $h^{-3},h^{-2}$ 原 scalar 支撑，故 $h^{-4}$ 系数为零。$N_0$ 的固定参考常数及 $F_*(k,\omega)$ 不含负 $h$ 幂，乘本 $m_2$ 也不能进入该目标；这不是假定它们一般为零。

还须核(23)是否已涵盖(5)的 pure 和两份有序补偿。上面的原式保持 outer 与 inner 的真实线性/双线性配对；(15)(25)更是完整独立 outer 身份。换入任意不交实紧包的幅度多项式并取原有序系数，不增加任何 $h,k$ 幂。R352 的右包三矩因子化由三个固定真实矩基完成，只是与 $h,k$ 无关的线性操作，随后代入 $\mu(u)$ 也如此。

因此两份有序尾和原 pure 都保(24)。第1节已配对消掉的 $C_A/N_2$ 是完整自然恒等；其 raw 各项不需要被分别宣布为零。综合(23)—(25)及原 $4/5,1/3,2/3$ 比例，得到整个(5)的偶四次结构(1)。

## 7. S 因子的精确待付条件

为避免预授一个尚未求值的关系，记
$$
\mathcal A=\Lambda_\cdot(V_0),\qquad
\mathcal B=\Lambda_\cdot(V_2),\qquad
\mathcal C=\Lambda_\cdot(V_4).
$$
定义实际同权类
$$
\Delta=V_2-V_0-V_4.
\tag{26}
$$
式(1)可以无条件改写为
$$
\boxed{
\Lambda_\cdot(V_{kk}(k))
=(1+k^2)\{\mathcal A+k^2\mathcal C\}
+k^2\Lambda_\cdot(\Delta).
}
\tag{27}
$$
这是恒等式，不是对 $S$ 的猜测。由于(1)最高次数为四，
$$
\boxed{
\text{整个自然多项式有因子 }1+k^2
\iff \Lambda_\cdot(\Delta)=0 .
}
\tag{28}
$$
(28)只作实系数多项式的整除判断，不以复曲率作为真实几何状态。

完整全曲率低权或势的既有结论没有单独支付(28)。特别，R421 负六层的 $S^2$ 因子与 R425 hh 层的 $S^2$ 因子不能搬到这里。即使最后(28)成立，也仍须求 $\mathcal C$ 的完整自然值。

等价地，在自然函数层可用
$$
\Lambda_\cdot(\Delta)
=\Lambda_\cdot\{V_{kk}(1)-2V_0-2V_4\}.
\tag{29}
$$
这里 $V_{kk}(1)$ 是一个真实状态值的 $h^{-4}$ 系数；(29)不声称两个原成本本身相等。

## 8. 后继最小目标和 PSD 的准确范围

在独立的 $k=0$ 完整锚 $\mathcal A$ 已知后，有两种等价的最小继续方式：

- 求完整 $\Lambda(V_2),\Lambda(V_4)$；
- 求完整 $\Lambda(\Delta),\Lambda(V_4)$，同时明确回答(28)。

这只是三个多项式系数中两个尚未由已有完整身份确定的目标，不宣称它们作为 universal 函数或共同查询列必线性独立。任何新消费都须保(4)(25)的完整 self/pure/ordered 规范；旧 pure 坐标不是新自然值。

[R425](R425-complete-hh-minus4-natural-identity-and-PSD-cross-cancellation.md) 使同一共同商的负四正字符只有 kk 可能保留。若其 $k=0$ 锚也由独立证明在该共同商中消去，则对这个正字符
$$
d_\lambda(k)=k^2b+k^4c .
$$
逐所有实际 $k$ 的非负性准确等价于
$$
b\ge0,\qquad c\ge0.
\tag{30}
$$
只有再付(28)在此字符上的零值，才可令 $b=c$；本稿没有这样做。对原 universal $\mathcal A$ 的非零函数，也不能仅凭其标签就推 $d_\lambda(0)\ne0$。

本稿独立完成的是完整自然函数的偶性、次数上界和准确整除判据。它保留两项尚未付的完整读出，不计算新 $\Omega$，不把 formal 原因子或 signed 类当作一条实际无基准路径，也不宣布共同低自然商、period 或最终 joint 已经解决。
