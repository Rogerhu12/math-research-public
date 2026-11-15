# R367：原 N2 势的完整 Green 收缩与不可删除的四次速度校正

> **2026-11-15 R378 更正。** 开头对旧H非零链的引用已撤回；本稿独立N2 Green/两真尾计算不由该漏项否定。详见[完整原式更正](R378-correction-of-the-third-history-term-in-the-complete-H-flux.md)。以下旧正文保留供追溯，不作为被撤回结论的当前证明。


日期：2026-11-15。**完整纸面推导；没有执行新的 profile 积分、原根恢复、消元、秩计算或研究运行。**

[R365](R365-complete-H-layer-affine-orbits-and-exact-total-flux-functionals.md)
已闭合实际 H 层的两个完整总通量泛函。
下一层必须回到 [R109](R109-local-density-of-the-complete-fourth-quotient.md)、
[R134](R134-acceleration-layer-from-complete-local-v4.md) 的原密度
$$
L_4=v_4-\mathcal B_{m_2}N_2.
$$
这里的 $N_2$ 是原第三密度的对称加速度势，不能因它不含加速度就将其四次速度响应删除。

本稿给出这份校正的完整外槽 Green 身份、正式 pure 与有序 $2+2$ 收缩，并在一个实际速度方向上得到
$$
\boxed{
\widehat\Lambda_u(\mathcal B_{m_2}N_2)
=-\frac1{80}\int e(1+e^2)^2r^3t^2
+\frac1{2400}\int e(9+e^2)r^5
+\frac1{240}\int er^3(M-\mu),}
\tag{1}
$$
其中 $h=1,\gamma=0,\delta=1$，
$e=x+d$、$r=u''$、$t=u'''$、
$M=J(er^2)$、$\mu=M(\ell)$。
后两项是准确的连续 $C^2$ 泛函，第一项给严格非零见证。

$\widehat\Lambda$ 表示对本稿明确检查过的 ambient 项，使用与原 $\Lambda$ 相同的 self、pure、有序尾配方。
本稿**不**宣称 $\mathcal B_{m_2}N_2$ 单独属于 $U$，
也不将 (1) 当成整个 $\widehat Q_4$ 的值。
它支付的是一个以前不能删除、现在已准确读出的真实校正。

## 1. 原对称加速度势及统一锚

固定原右 collar，记
$$
J(F)(x)=\int_x^{r_*}F(y)\,dy.
$$
所有输入先取实紧光滑；在需要原输出作为输入时，允许真实二次左尾，始终保持右零。

几何记号为
$$
d=h\omega-k,\quad e=hx+d,\quad Q=1+e^2,\quad
\gamma=h_s,\quad\delta=d_s,\quad
\vartheta=x\gamma+\delta,\quad c=\frac1{8h^3}.
\tag{2}
$$
对任意 profile $f$，定义
$$
l_f=\gamma f'-\vartheta f''.
$$
原第二局部第一分子 $a(f,g)$ 对称双线性，满足
$$
a(f,g)'=\frac{cQ}{2}\{f'''l_g+g'''l_f\},
\qquad a(f,g)(r_*)=0.
\tag{3}
$$
这就是 [R76(13)](R76-local-third-exact-loops-and-weight-three-control.md)
的真实分子及其极化。对角记 $a=a(u,u)$，则 $a'=cQu'''l_u$。

完整外槽并不是从对角值任意猜出的极化：原 R56 的
$
P_{H(Y_f,K_A)}
=\frac{(Qf''-hef')A+J(Qf'''A)}{4h}
$
对独立的 $f,A$ 成立。
将它代入真实恢复，R76(14) 的第三加速度系数对完整外槽就是
$$
2c\{Ql_f\,a(g,g)_{\rm acc}
-\vartheta J(Qf'''a(g,g)_{\rm acc})\}.
$$
按 [R77](R77-weight-three-local-operator-actual-finite-controllability.md)
对速度一次、加速度一次式取对称势，准确得到原 $N_2=P_{\rm acc}$：
$$
\boxed{
N(f;g,g):=N_2(f;g,g)
=c\{Ql_f\,a(g,g)-\vartheta J(Qf'''a(g,g))\}.}
\tag{4}
$$
内两槽作对称极化。
取势的因子 $1/2$ 来自速度一次式的 Euler 收缩，不是新增的三阶选择。
从 $(h,k)$ 换到 $(h,d)$ 时，同一个速度二次势只是作坐标代入；
状态依赖的加速度变换另影响第三速度项，不改变 (4)。

对紧 $u$，$a_L=a(u,u)(\ell)$ 是原真实三矩的线性函数：
$$
\boxed{
a_L=
\frac{
\gamma\{(1+d^2)\mu_0-h^2\mu_2\}
-2h\delta(d\mu_0+h\mu_1)}
{16h^3},}
\tag{5}
$$
$$
\mu_0=\int(u'')^2,\quad
\mu_1=\int x(u'')^2,\quad
\mu_2=\int\{x^2(u'')^2+2(u')^2\}.
$$
式 (5) 不把左值设为零。

## 2. 原外槽三阶算子确实自伴

固定紧 $u$，置
$$
F=Qa,\qquad T=N(u;u,u).
$$
对任意右零 $f$，同锚积分分部给
$$
N(f;u,u)=c\{\gamma Ff'+\vartheta J(F'f'')\}.
\tag{6}
$$
右端 $f''a$ 的边项由右 collar 支付；不需要 $f$ 左紧。

对 (6) 求三阶导，得到完整原式
$$
\boxed{
D^3N(\,\cdot\,;u,u)
=c\left\{
D^2\bigl((\gamma F-\vartheta F')D^2\bigr)
+D\bigl(\gamma F''D\bigr)
\right\}.}
\tag{7}
$$
例如四、三、二、一阶导数系数依次为
$$
\gamma F-\vartheta F',\quad
-2\vartheta F'',\quad
-\vartheta F''',\quad
\gamma F'''.
$$
这正是 (7) 的展开，没有遗漏原 primitive。

式 (7) 形式自伴。
实际交换积分时仍必须使用完整 Green 端项：
本稿涉及的交换至少有一个紧参数 $u$，
所以四阶 Green 项在两端为零。
随后若在两个有尾输出之间移动三阶导数，则保留
$$
\mathcal G(p,q)=p''q-p'q'+pq'',
\qquad
\int f'''g+\int g'''f=-\mathcal G(f_{\rm left},g_{\rm left}).
\tag{8}
$$
若 $p,q$ 为二次多项式，这个值与左 collar 中的评价点无关。

## 3. 对角总通量与非紧变分的额外边界

记 $j=J(Qu'''a)$。紧 $u$ 满足 $l_u'=-\vartheta u'''$，故
$$
\int Qu'''l_u a
=\frac1c\int a'a=-\frac{a_L^2}{2c},
$$
$$
\int\vartheta u'''j=-\int Qu'''l_u a.
$$
于是
$$
\boxed{\int u'''N(u;u,u)=-a_L^2.}
\tag{9}
$$
这不是零，而是一个准确的真实左尾平方。

但是，**不能直接沿有二次左尾的方向微分 (9)**。
对一般右零、左二次的 $w$，相同推导完整保留
$[l_wj_w]_\ell^{r_*}$，给
$$
\boxed{
\int w'''N(w;w,w)
=-a_L(w)^2-c\,l_{w,L}j_{w,L}.}
\tag{10}
$$
这一额外项正是后面的必要 Green 修正。

现令 $E\in E_8$ 为原八算子的任意固定方向，
$$
q=\Phi_E(u,u),\qquad p=q_{\rm left},\qquad
\alpha=a(u,q)_L,\qquad
S=-\int qT'''.
\tag{11}
$$
紧 $u$ 的 $T$ 具有真实线性左尾
$$
T_{\rm left}=-c\vartheta j_L.
$$
若 $p=p_2x^2+p_1x+p_0$，则
$$
\ell_p=\gamma p'-\vartheta p''
=\gamma p_1-2\delta p_2
$$
为常数，且
$$
\boxed{\mathcal G(p,T_{\rm left})=c\,\ell_pj_L.}
\tag{12}
$$
将 (10) 在 $w=u+\epsilon q$ 处准确微分，
$$
D\!\left(\int w'''N(w;w,w)\right)_{w=u}[q]
=-4a_L\alpha-\mathcal G(p,T_{\rm left}).
\tag{13}
$$
(13) 的最后一项不能通过“outer 紧”省掉；变分后的 outer 不再紧。

## 4. 完整响应的 self 和正式 pure

对任意内对称三线性算子 $\tau$，原响应的代数式为
$$
\mathcal B_E(\tau)(F,\phi)
=2\tau(\Phi_ED;D)
-4\tau(\phi;\phi,\Phi_ED)
+4\Phi_E(\phi,\tau(\phi;D)),
\quad D=F-\phi^2.
$$
因此对本稿的 $N$ 仍准确有
$$
\mathcal B_E(N)(u^2,0)=2N(q;u,u),
$$
$$
\pi\mathcal B_E(N)(u)
=\frac18\{DT(u)[q]-2\Phi_E(u,T)\}.
\tag{14}
$$
这里只采用原正式 $\pi$ 规范，不假设 $N\in W$。

利用 (7) 的真实自伴性，
$$
\Omega_u(\mathcal B_E N)=2S.
\tag{15}
$$
由 (8)，
$$
\int q'''T=S-\mathcal G(p,T_{\rm left}),
$$
而原八算子的三阶伴随又给
$$
\int u'''\Phi_E(u,T)=-S+\mathcal G(p,T_{\rm left}).
$$
将这些式子与 (13) 代入 (14)，得到
$$
\boxed{
8\int u'''\pi\mathcal B_E(N)(u)
=S-4a_L\alpha-2\mathcal G(p,T_{\rm left}).}
\tag{16}
$$
其中系数 $-2$ 同时使用 (10) 的非紧变分尾和原三阶 Green 项。
把 (9) 无条件微分会误成 $-1$。

## 5. 原有序 2+2 系数与完整三矩输运

取真正紧的 $v$，其支撑完全在 $u$ 右侧，记 $n=\mu(v)$。
右包在左域的第二局部分子准确为 $a(n)$，按 (5) 线性解释；
其原八算子输出的左尾记为 $p_E(n)$。
二者都是真正同锚尾，不是自由参数。

定义一阶算子
$$
X=c\{(\gamma Q-2he\vartheta)D+2h^2\vartheta\}.
\tag{17}
$$
若 $\zeta=\gamma Q-2he\vartheta$，则
$\zeta'=-2h^2\vartheta$，所以
$X=c(\zeta D-\zeta')$ 属于原三个 projective 导子的线性跨度。

真实支撑直接给
$$
N(u;v,v)=a(n)Xu,\qquad N(v;u,u)=0.
\tag{18}
$$
对左域的真实二次尾 $p=p_E(n)$，
$$
N(p;u,u)=c\ell_pQa,
$$
$$
2N(u;u,p)=c^2\ell_p
\{Ql_uF_u+\vartheta F_u^2/2\},
\qquad
F_u=Qu''-2heu'+2h^2u.
\tag{19}
$$
这里 $F_u'=Qu'''$，所以
$J(Qu'''F_u)=-F_u^2/2$；
其边界来自紧 $F_u$，没有要求 $a$ 左紧。

用原三个槽展开 (14) 的 $[\xi^2\eta^2]$
系数，不能只在紧输入展开式上作非紧变分。
记该正式 pure 系数为 $\Gamma^\to_E(u;n)$，则
$$
\boxed{
8\Gamma^\to_E(u;n)
=a(n)\,q_{X\cdot E}(u)
+c\ell_pQa
+c^2\ell_p\{Ql_uF_u+\vartheta F_u^2/2\}.}
\tag{20}
$$
其中
$q_{X\cdot E}=Xq_E-Dq_E[Xu]$ 是原 $E_8$ 内的真实导子作用，
由 [R344](R344-general-pure-factorization-of-total-response-flux-with-ordered-Green-tails.md) 的原三槽与右尾公式解释。
式 (20) 对 $n$ 线性，已经证明本项的有序三矩因子化。

为收缩它，(5) 的双线性极化给
$$
2\alpha=\int(Xu)'''q.
\tag{21}
$$
原八算子的紧参数变分恒等式则给
$$
\int u'''q_{X\cdot E}(u)=-3\int(Xu)'''q=-6\alpha.
$$
另一方面，利用 $a'=cQu'''l_u$、
$l_u'=-\vartheta u'''$ 及紧 $F_u,l_u$，
$$
\int u'''\{cQa+c^2Ql_uF_u+c^2\vartheta F_u^2/2\}
=-c\,j_L.
$$
故
$$
\boxed{
8\int u'''\Gamma^\to_E(u;n)
=-6a(n)\alpha-\mathcal G(p_E(n),T_{\rm left}).}
\tag{22}
$$
三右包的真实矩基可按原 R352 作有限线性读出，
所以最后可代入 $n=\mu(u)$。
这不要求存在一个位于 $u$ 右侧、却与 $u$ 有相同实二阶重心的单个包。

## 6. 完整的自然读出扩展

对本项定义
$$
\widehat\Lambda_u(\mathcal B_E N)=
\Omega_u(\mathcal B_E N)
-\frac{16}{5}\int u'''\pi\mathcal B_E N(u)
-\frac{32}{15}\int u'''\Gamma^\to_E(u;\mu(u)).
\tag{23}
$$
(20) 已付其真实尾因子化，故 (23) 没有新增任意选择。
若一个项已在原 $U$ 中，此配方就是原 $\Lambda$；
本稿不因写了 (23) 就宣称该单项属于 $U$。

合并 (15)、(16)、(22)，得到主 Green 身份：
$$
\boxed{
\widehat\Lambda_u(\mathcal B_E N)
=\frac85\left\{
S+2a_L\alpha+\frac23\mathcal G(p_E(\mu(u)),T_{\rm left})
\right\}.}
\tag{24}
$$
它保留原外槽、正式 pure 的 $1/8$、
有序而非平均的 $2+2$ 系数，以及全部真实左尾。

(24) 不是全部响应的零式。
原 $\mathcal R$ 中第三输入属于已付的 $W$；
本稿的 $N_2$ 是原局部势，不能未经证明替换成 $W$ 元素。

## 7. 一个实际速度方向的完整值

现在固定 $h=1$、$\gamma=0$、$\delta=1$，
所以真实 $k_s=-2$。
$k$ 可为任一实际状态值，$e=x+d$、$Q=1+e^2$。
令
$$
r=u'',\quad t=u''',\quad M=J(er^2),\quad\mu=M_L.
$$
原 R73 的点态速度二次密度与原 R76 分子准确为
$$
q=m_2(u,u)=-\frac M4,\qquad
a=B=-\frac{Qr^2+2M}{16}.
\tag{25}
$$
由 (4)，
$$
T=-\frac{QrB+J(QtB)}8,\qquad
T'=-\frac{erB}{4}+\frac{Q^2r^2t}{64}.
\tag{26}
$$
$q$ 左尾为常数、$T$ 左尾为常数，故本方向
$\mathcal G(q_{\rm left},T_{\rm left})=0$，
这是实际次数判断，不是删掉一般式 (24) 的 Green 项。

同时
$$
a_L=-\frac\mu8,\qquad
\alpha=a(u,q)_L=\frac1{96}\int er^3.
\tag{27}
$$
第二式由
$q''=(r^2+2ert)/4$
及原混合矩得到；一次紧 $r^3$ 分部积分支付其符号。

在 (11) 中移两次导数，真实边项全零，得到
$$
\begin{aligned}
S=-\int q''T'
={}&-\frac1{128}\int eQ^2r^3t^2\\
&+\frac1{16}\int er^3B
+\frac18\int e^2r^2tB
-\frac1{256}\int Q^2r^4t.
\end{aligned}
\tag{28}
$$
将 (25) 代入后三项，准确分部积分给
$$
\boxed{
S=-\frac1{128}\int eQ^2r^3t^2
+\frac1{3840}\int e(9+e^2)r^5
+\frac1{384}\int er^3M.}
\tag{29}
$$
例如两个含 $t$ 的局部项合为
$-\int Q(1+3e^2)r^4t/256$，
而 primitive 项使用 $M'=-er^2$；
其边项都带紧 $r^3$ 或 $r^5$。
这完整保留了左值 $\mu$，并没有把 $M$ 当成紧 primitive。

把 (27)、(29) 放入 (24)，便得到开头 (1)。
因此这份四次速度校正的真实尾恰以
$M-\mu=-\int_\ell^x er^2$
出现，不能用 $M$ 或零尾替代。

## 8. C² 余项与严格非零

(1) 的后两项只使用 $r=u''$ 和一个同锚二次 primitive，
所以在固定紧窗口上是连续的 $C^2$ 五次泛函。

选实际窗口使 $e>0$，取紧光滑 $u_0$，
在某个小开区间上 $r_0=u_0''<0$。
取非零紧光滑 $\chi$ 支撑在此区间，纸面定义
$$
u_N=u_0+N^{-5/2}\chi(x)\cos(N(x-x_0)).
$$
每个有限 $N$ 都是真正紧光滑输入，$u_N\to u_0$ 于 $C^2$，而
$$
u_N'''=N^{1/2}\chi(x)\sin(N(x-x_0))+O(1).
$$
普通分部积分消去双频振荡后，
$$
\boxed{
\lim_{N\to\infty}
\frac{\widehat\Lambda_{u_N}(\mathcal B_{m_2}N_2)}N
=-\frac1{160}\int eQ^2r_0^3\chi^2>0.}
\tag{30}
$$
因此 (1) 不恒为零。
这只是有限 $N$ 存在的纸面证明，没有运行这个输入族。

## 9. 对真正 Q4 剩余项的意义

本稿支付了原 $\mathcal B_{m_2}N_2$ 的一个完整、非零读出，
所以不能把 H 层的计算直接复制成完整四次速度成本。

尤其，在累计 second/third 值最后设零时，
真实第三场的导数仍含其对累计 second 的导数乘 $m_2$。
这类项在 H 提取中纯为速度四次，故不改变 R358/R362/R365；
在当前 Q4 中却必须保留。
同样，R129 的 $D_0P_{3v}$、所有原边势及 $N_2$ 响应都要按原式合成。

本稿没有给出完整 $\widehat Q_4$ 的新 U 非成员结论。
单独的 ambient 校正可有在完整 $U$ 中相消的真权分量；
因此它不与 [R356](R356-lowest-two-full-self-weights-and-universal-total-flux-cancellation.md)
的完整最低权消去冲突。
真正的下一式仍是
$$
\widehat Q_4=Q_4^v-D_0P_{3v}-\mathcal B_{m_2}N_2,
$$
而不是 (1) 的单项。

原 $N_0$ 与完整 $\widehat Q_2$ 也没有在本稿被设为零。
所有结论保持原右锚、真实左尾和同一 canonical 二阶选择；
没有增加真实控制预算或预授全 period、whole ruling 或最终嵌入。
