# R378：完整 H 通量中第三 history 链式项的更正及两项准确抵消

日期：2026-11-15。**原式纸面更正；没有执行新的 profile 积分、符号程序、旧根恢复、秩计算、人工检查或研究运行。**

本稿更正 [R358](R358-nonzero-total-flux-class-of-a-true-velocity-acceleration-cost.md) 式 (23)：该式在第四阶配对的第三 history 项中只保留了 $T_s$ 部分，漏掉了同一 history 在 $P_s,B_s$ 中的链式导数。这个漏项与 R358 式 (12) 已保留的二次 $m_2$ 项不是同一项。

补回后有两条准确结论：

- 原 R365 显示的全部 $u'''^2$ principal 被补项准确抵消。因此，修正后的两个 H 总通量泛函均属于连续 $C^2$ 层；旧“模 $C^2$ 维数为 12”的结论撤回。
- 原 R358 用于证明非零的真实权 $-7$ 通量也被准确抵消：
  $$
  \Lambda_u\!\left(\Pi_{-7}[-2H_1(1,1,1)-4H_2(1,1,1)]\right)=0.
  \tag{1}
  $$

式 (1) 是指定自然通量的零值，不是该成本算子本身为零。本文不声称整个修正后的 H 通量为零，不声称 $U=\mathcal R$。其余完整 $C^2$ 值仍须从修正后的原式继续求出。

## 1. 原来源及两个不能混淆的恢复层

固定原共同右 collar，令
$$
J(F)(x)=\int_x^{r_*}F(y)\,dy,\qquad
u\in C_c^\infty((\ell,r_*)),
$$
$$
v=u',\qquad r=u'',\qquad t=u'''.
$$
几何记号与 R358 相同：
$$
d=h\omega-k,\quad e=hx+d,\quad Q=1+e^2,\quad
\gamma=h_s,\quad\delta=d_s,\quad\vartheta=x\gamma+\delta,
$$
$$
l=\gamma v-\vartheta r,\qquad
g=\gamma u-\frac{\vartheta v}{2}.
\tag{2}
$$

[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 式 (5) 的原 characteristic 密度是
$$
\mathcal R_H=
\frac{T_s}{2h^2}+K_0P-\frac{\vartheta}{h^2}P_s
+\frac{K_0}{z}B-\frac{\gamma}{h^2}B_s.
\tag{3}
$$
全部导数都先按真实字段求出。若第三场写成
$C=K_3-Y_{\mathcal T}$，则在累计第三 scalar 值为零的时刻，仍有
$$
\mathcal T_s=n,\qquad
\partial_s P_{H(Y_u,C)}
=\partial_s P_{H(Y_u,K_3)}-P_{H(Y_u,Y_n)},
\tag{4}
$$
$B_s$ 同样。因而 (3) 必须包含
$$
+\frac{\vartheta}{h^2}P_{H(Y_u,Y_n)}
+\frac{\gamma}{h^2}B_{H(Y_u,Y_n)}.
\tag{5}
$$

这里 $n$ 对 profile 为三次。R358 式 (12) 则来自第二场
$Z=K_2-Y_{\mathcal A}$ 的 $\mathcal A_s=m_2$，并进入第三场的
$\eta_{0,C}$ 恢复；它对输入 profile 为二次。保留后一项不能代替 (5)。

[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md) 式 (13)–(15) 对变化 profile 给完整链式项 $\Psi$。[R109](R109-local-density-of-the-complete-fourth-quotient.md) §3 的局部第四生成元也是先代入
$\mathcal A_s=m,\ \mathcal T_s=n-m\circ\mathcal A$，最后才把累计值置零。
该定义没有把 $n$ 置零。R109 §4 随后作历史换元；本稿所取的线性加速度层也不能由速度四次的 $\mathcal B_{m_2}N_2$ 自动补回。

## 2. 完整缺项及真实有序尾

对任意同右 collar 为零的 $f$，其左尾不必为零，原配对为
$$
\begin{aligned}
P(u,f)&=\frac{e v f'}8+
\frac1{8h}J(Qr f''+2h^2v f'),\\
B(u,f)&=\frac{Qvf'}{8h}
-\frac e4(vf+uf')+\frac h2uf.
\end{aligned}
\tag{6}
$$
定义对 $f$ 线性的速度函数
$$
\mathcal D_V(f)=
\int t\left\{\frac{\vartheta}{h^2}P(u,f)
+\frac{\gamma}{h^2}B(u,f)\right\}.
\tag{7}
$$
直接代入 R73 的完整 $\Psi$ 可核得
$$
-\int t\Psi(u,f)
=\int\frac{tg}{2h^2}
\left(\frac{ef'}2-hf\right)+\mathcal D_V(f).
\tag{8}
$$
右边第一项恰为 R358 式 (23) 所保留的 history 部分；第二项就是漏项。式 (8) 无需左尾为零，也没有作几何参数 $s$ 的积分。

第二局部分子 $a$ 满足
$$
a'=\frac{Qtl}{8h^3},\qquad a(r_*)=0.
\tag{9}
$$
以 $\mathrm d_v$ 表示速度 $(\gamma,\delta)$ 的微分，原 R76 的三次密度给
$$
n_{\rm acc}
=\frac{Ql\,\mathrm d_va-\vartheta J(Qt\,\mathrm d_va)}
{4h^3}.
\tag{10}
$$
这里 $n_{\rm acc}$ 是取加速度系数得到的速度一形式；与实际加速度配对后，才是通常的 scalar 项。

对于位于 $u$ 右侧、其三矩准确匹配 $\mu(u)$ 的真实辅助包，第二局部第一分子在整个 $u$ 区域为常数 $a_L$。令
$$
F_u=Qr-2hev+2h^2u,\qquad F_u'=Qt,\qquad J(Qt)=-F_u.
$$
将该真实常尾代入相同的 (10)，得到
$$
n_{{\rm tail},\rm acc}
=\frac{\mathrm d_va_L}{4h^3}
\{Ql+\vartheta F_u\}.
\tag{11}
$$
这里
$$
Ql+\vartheta F_u
=(\gamma Q-2he\vartheta)v+2h^2\vartheta u.
\tag{12}
$$
没有删除 $a_L$ 或其状态导数；(12) 只说明这一具体尾输入的 profile 部分由 $u,u'$ 组成。

R352/R358 原 self、pure、有序 $2+2$ 极化给
$$
\frac54\Lambda=
\Omega(YC)-\Omega(ZZ)
+\frac13\Omega(ZZ_{\rm tail})
+\frac23\Omega(YC_{\rm tail}).
\tag{13}
$$
因此，R358 式 (30) 的一形式应准确改成
$$
\boxed{
\mathfrak C_{\rm new}
=\mathfrak C_{\rm old}
+\mathcal D_V(n_{\rm acc})
+\frac23\mathcal D_V(n_{{\rm tail},\rm acc}).}
\tag{14}
$$
原 $ZZ$ 项及其 $1/3$ 因子不变。修正仍使用原真实三矩尾，不引入自由补偿。

按原 R129 速度势归一化，
$$
\mathrm d_v\mathfrak C_{\rm new}
=\frac{15}{4}
\{\Lambda(\widetilde H_\gamma)\gamma+
\Lambda(\widetilde H_\delta)\delta\}
\,\mathrm d\gamma\wedge\mathrm d\delta.
\tag{15}
$$
本文随后直接对 (14) 取 curl，不沿旧非零结论反推。

## 3. 缺项的三阶导平方 principal

先取 $h=1$，允许任意固定 $d$，所以 $e=x+d$。原式 (10) 微分时两个含 $\vartheta t\,\mathrm d_va$ 的项相消：
$$
n_{\rm acc}'
=\frac{Q^2l\,\mathrm d_vl}{32}\,t
+\frac{2el\,\mathrm d_va-\gamma J(Qt\,\mathrm d_va)}4.
\tag{16}
$$

对 (8) 的完整 $-\Psi$ 作紧 outer 分部积分，其 $t f'$ 系数为
$Ql/4$；旧 $T_s$ 项对应系数为 $eg/4$。因而 (7)、(16) 给新增的一形式 principal
$$
\boxed{
(\Delta\mathfrak C)_{\rm prin}
=\frac{Q^2}{128}\,
l(Ql-eg)\,\mathrm d_vl\,t^2.}
\tag{17}
$$
为核其符号，置
$$
E=ur-\frac{v^2}{2}.
$$
由 (2)，
$$
\mathrm d_vg\wedge\mathrm d_vl
=-E\,\mathrm d\gamma\wedge\mathrm d\delta.
$$
故
$$
\boxed{
\mathrm d_v(\Delta\mathfrak C)_{\rm prin}
=+\frac{eQ^2lE}{128}t^2\,
\mathrm d\gamma\wedge\mathrm d\delta.}
\tag{18}
$$
$Ql^2\,\mathrm d_vl$ 是速度梯度，没有 curl。旧 R365 principal 正是
$$
-\frac{eQ^2lE}{128}t^2\,
\mathrm d\gamma\wedge\mathrm d\delta,
$$
所以两项准确相消。

为说明“只剩连续 $C^2$”不依赖丢高阶余项，在 $h=1,d=0$ 可把 (7) 完整写成
$$
\begin{aligned}
\mathcal D_\delta(f)
&=\frac18\int\{2rL+(xv-2Qr)t\}f',\\
\mathcal D_\gamma(f)
&=\frac18\int
\{-2L^2+[(2+3x^2)v-2Qxr-2xu]t\}f'
+\frac14\int(2u-xv)t f,
\end{aligned}
\tag{19}
$$
其中 $L=v-xr$、$Q=1+x^2$，且
$\mathcal D_V=\gamma\mathcal D_\gamma+\delta\mathcal D_\delta$。
这些等式直接由 (6) 的同锚 Fubini 与紧 outer 分部积分得到，对非紧 $f$ 也成立。

$a$ 及 $J(Qt\,a)$ 可用局部 $u,v,r$ 和密度只含这些 jets 的真实右积分表示；后者对唯一线性 $t=r'$ 项取关于 $r$、在 $r=0$ 为零的多项式原函数即可。
因此，(16)、(19) 除 (17) 外至多线性含 $t$。对线性项作同样分部积分，全部边界含一个在 $r=0$ 为零的原函数；真实左尾常数仍保留。
(11)–(12) 的尾输入只含 $u,u'$，也只产生连续 $C^2$ 项。

结合旧 R365 已列出的连续 $C^2$ 余项，修正后的两个基准 H 读出均为连续 $C^2$ 泛函。原 R89 的真实正仿射协变把这个性质输运到所有实际状态；这里使用的是协变结构，不是旧 R365 错误识别的显示基准值。

## 4. 被旧稿称为非零的真实权 −7 也准确消去

还不能从 principal 抵消推断所有 $C^2$ 值为零。本节单独核定 R358 的指定 Laurent 系数。

在 $h=1,d=0$ 置 $u_\epsilon(x)=u(x/\epsilon)$，共同右锚一并变换。换元后沿用 $x$。旧 R358 式 (32) 的领先数据为
$$
A=\frac{2vr-xr^2+P}{16},\qquad
B=-\frac{r^2}{16},\qquad
P=J(r^2),\quad J_3=J(r^3),
\tag{20}
$$
$$
A'=\frac{Lt}{8},\qquad B'=-\frac{rt}{8}.
$$
实际 $a_\gamma$ 的领先尺度为 $\epsilon^{-3}$，
$a_\delta$ 为 $\epsilon^{-4}$。

只在本节以 $n_{ij}$ 记 (10) 相应领先系数，第一下标取速度，第二下标取 $\mathrm d_v$。直接从同锚 (10) 得
$$
\begin{aligned}
n_{\gamma\delta}
&=-\frac{vr^2}{64}+\frac{xr^3}{96},\\
n_{\delta\gamma}
&=n_{\gamma\delta}-\frac{J_3}{192},\\
n_{\gamma\gamma}
&=\frac{v^2r}{32}-\frac{xvr^2}{32}
+\frac{x^2r^3}{96}+\frac{vP}{64}
-\frac{xJ_3}{192}.
\end{aligned}
\tag{21}
$$
前两式尺度为 $\epsilon^{-5}$，末式为 $\epsilon^{-4}$。
相应的 (19) 领先收缩是
$$
\mathcal D_\gamma^{\,0}(f)
=\frac14\int Lt f',\qquad
\mathcal D_\delta^{\,0}(f)
=\frac18\int r^2f''.
\tag{22}
$$
故新增 $\gamma\,\mathrm d\gamma\wedge\mathrm d\delta$ 的
$\epsilon^{-9}$ 系数准确为
$$
\mathcal D_\gamma^{\,0}(2n_{\gamma\delta}-n_{\delta\gamma})
-\mathcal D_\delta^{\,0}(n_{\gamma\gamma}).
\tag{23}
$$

令 $f=n_{\gamma\delta}+J_3/192$、$T=n_{\gamma\gamma}$。逐项求导：
$$
\begin{aligned}
f'&=-\frac{r^3}{96}-\frac{rLt}{32},\\
T'&=\frac{vr^2}{64}-\frac{xr^3}{192}
+\frac{rP}{64}-\frac{J_3}{192}+\frac{L^2t}{32}.
\end{aligned}
\tag{24}
$$
在 (23) 中一次紧 outer 分部积分后为
$$
\frac14\int t(Lf'+rT')
=\frac14\int t
\left\{\frac{vr^3}{192}+\frac{xr^4}{192}
+\frac{r^2P}{64}-\frac{rJ_3}{192}\right\}.
\tag{25}
$$
所有 $t^2$ 项在这里再次逐项消去。

设 $R_5=\int r^5$。同一右锚、真实紧 outer 给四个准确身份：
$$
\int vr^3t=-\frac{R_5}{4},\qquad
\int xr^4t=-\frac{R_5}{5},\qquad
\int Pr^2t=\frac{R_5}{3},\qquad
\int rJ_3t=\frac{R_5}{2}.
\tag{26}
$$
例如第三、四式分别使用 $P'=-r^2$、$J_3'=-r^3$；
$P,J_3$ 的左值不需要为零，因为边界乘以紧的 $r^3,r^2$。
代回 (25) 得
$$
\boxed{
[\mathrm d_v\Delta\mathfrak C]_{\gamma,\epsilon^{-9}}
=+\frac{R_5}{15360}.}
\tag{27}
$$

真有序尾也必须单列。在此尺度
$$
A_L=\frac{\mu_0}{16},\qquad B_L=0,
$$
式 (11) 的可能贡献是
$$
n_{{\rm tail},\rm acc}^{\,0}
=\frac{\mu_0}{64}\gamma v\,\mathrm d\gamma.
$$
其混合 curl 只可能含
$\mathcal D_\delta^{\,0}(v)=\int r^2t/8=0$。
实际 $a_{\delta,L}$ 的次阶不进入所取 Laurent 系数；未将其整个真实值删去。

旧 R358 式 (42) 已算出的值为 $-R_5/15360$，故与 (27) 准确相消。
乘原 (15) 的 $4/15$ 仍为零。使用原已付有限 Laurent 真权分解，
这正给式 (1)，而不是仅一个窄包极限为零。

## 5. 正规化与更正的范围

本稿补的是原生成元 $v$ 中的真实三次 history 导数。它不是改变 $\Lambda$、改变 pure 投影，或另加一份第三齐次 gauge。

[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md) 的三项加速度平方收缩不受此次漏项影响：式 (10) 与 (7) 的乘积只含线性加速度。R358 对第二场 $\eta_{0,C}$ 的 $m_2$ 修复和 $ZZ$ 的 $P,B$ 项，也没有在本稿被撤销；被补的是另一个原恢复层。

[R367](R367-exact-N2-Green-contraction-and-nonzero-quartic-velocity-correction.md) 的原 $N_2$ Green 身份单独从原势推导。它开头对旧 H 结论的引用应随本稿撤回，但其独立计算不因这个引用成为错误。

[R370](R370-complete-quartic-velocity-cost-and-exact-C2-total-flux.md) 式 (18)–(19) 已明确使用完整 $-\Psi(u,n)$，没有沿用 R358 式 (23) 的截断。因此本稿发现的具体漏项并未否定其准确 $\delta^4$ 读出。本稿也没有据此证明该 Q4 读出独立于修正后的 H 像。

## 6. 对已公开结论的准确处理

| 原稿或结论 | 本次更正后的状态 |
|---|---|
| R358 指定真权 $-7$ 的非零 $\Lambda$ 值及由此给出的非成员证明 | 撤回；准确读出为式 (1) 的零 |
| R362、R365 将旧显示式识别为完整 H 通量及相应非零主项 | 撤回该识别；必须加入 (14) |
| R365 的真实仿射协变、原 $H_1/H_2$ 成员和速度坐标关系 | 原来源独立；完整基准值须换成修正式 |
| R371“模连续 $C^2$ 恰 12 维” | 撤回；补项后该 principal 商为零 |
| R371 完整 H 像至少 13，以及 R363/R366/R371 依旧 H 非零值给出的具体实际读出数 | 原证明不成立；在修正后的完整值核定前不使用这些具体控制结论 |
| R363/R366 在指定真实 H 读出满秩前提下的小环、桥与有限参数控制论证 | 保留为有条件结论；不得删除其非零或满秩前提 |
| 尚未发布的 R374“Q4 独立于完整 H” | 不发布；其中六行只能作为旧显示泛函的条件代数 |
| R350、R352、R356 的独立原式结论，R367 的独立 Green 计算，R370 的完整 $\delta^4$ 计算 | 不由此次具体漏项推翻；各自原证明范围保持 |

当前已支付的是完整补项、两个准确抵消以及受影响证明的范围修正。尚欠的是修正后 H 的全部连续 $C^2$ 值、是否出现新的非零真实通量类、以及任何依赖那些新值的实际控制结论。本文不将这一更正扩成原完整第四问题可解或不可解的声明。
