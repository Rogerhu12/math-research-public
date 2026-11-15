# R340：whole pure/self 核中的两条局部响应与两个真实退化通量的联合控制

日期：2026-11-15。**完整纸面证明；没有执行新符号程序、数值求积、人工检查或科学运行。**

[R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md) 已支付完整 universal pure 与完整 universal self 的真实同时控制，但不能把该结论与 R330 的两个内部通量满射直接相加。[R336](R336-self-cost-of-the-flux-successor-prevents-naive-joint-control.md) 已指出，原第二列 $\delta\mathcal K$ 带有严格正 self 成本。

本稿给出一个新的、完全局部的两列替代。两列都属于完整响应空间中的
$$
\mathcal R\cap\ker E,\qquad E=(\pi,\mathcal Q),
$$
而在 R324/R330 的同一真实解析微包圆上，它们的两个退化通量形成一个严格非零的二阶行列式。因此可以用**同一个真实几何控制系统**同时取得 whole-pure 零、whole-self 零和这两条原 period 必要条件。

主证明从原三槽交换子与完整响应直接出发。此前讨论中“$NG_0=0$”只是未发表的推测，而且不成立；第 8 节给出准确修正。本稿没有把该推测作为分包或尾消去的前提。

来源：[R247](R247-complete-response-Jacobi-presentation-and-pure-kernel-decomposition.md)、[R303](R303-complete-self-degree-nine-and-all-translation-control.md)、[R326](R326-one-global-second-gauge-pays-the-complete-rational-port-and-preserves-joint-cost.md)、[R330](R330-two-actual-packet-degenerate-fluxes-and-twenty-observation-control.md)、R333、R336，以及 [R302](R302-regular-chi-prototypes-shared-reversal-and-enhanced-Morse-control.md) 的真实共享原型、增强目标与 Morse 接口。R303 的具体 $G_0$ 仅用于第 8 节对照；主定理不依赖其导链。

## 1. 原算子、完整成本和两个新方向

全篇保持同一个右锚 $r_*$，使用
$$
J(F)(x)=\int_x^{r_*}F(y)\,dy,\qquad J'=-F,
$$
$$
P(a,b)=J(a''b''),\qquad
R(a,b)=a'b'+xJ(a''b''),\qquad
S(a,b)=J(xa''b'').
\tag{1}
$$
这些分别是原 $r_0,r_1,s_0$ 方向。所有输入都具有原共同零 collar；原二次输出仍允许真正的左多项式尾。

三槽交换子定义为
$$
[A,B](a;b,c)
=\Phi_A\{a,\Phi_B(b,c)\}
-\Phi_B\{a,\Phi_A(b,c)\}.
$$
置
$$
\tau_S=[P,S].
$$
直接用 $(S(b,c))''=-b''c''-x(b''c'')'$ 和
$(P(b,c))''=-(b''c'')'$，原两条嵌套积分准确相消，给
$$
\boxed{\tau_S(a;b,c)=-J(a''b''c'').}
\tag{2}
$$
它对全部三槽对称。这是完整同锚身份，不仅是其 diagonal 或三阶主项。

对 $D=F-\phi\odot\phi$，原完整响应为
$$
\mathcal B_E(\tau)(F,\phi)
=2\tau(\Phi_ED;D)
-4\tau(\phi;\phi,\Phi_ED)
+4\Phi_E\{\phi,\tau(\phi;D)\}.
\tag{3}
$$
记原射影代数导子
$$
\mathscr D=x^2\partial_x-2x,\qquad
\delta A=\mathscr D_{\rm out}A
-\sum_{\rm input\ slots}A(\ldots,\mathscr D\,\cdot,\ldots).
\tag{4}
$$
定义
$$
\boxed{
\widetilde{\mathcal K}=\frac13\mathcal B_P(\tau_S),
\qquad
\widetilde{\mathcal H}=\delta\widetilde{\mathcal K}.
}
\tag{5}
$$
$\delta$ 是对原算子的有限代数作用，不是声称已经对真实几何作了一次非仿射坐标改变。

这两列都有既有真实原型。具体地，令 $U_1=\Phi_{s_1}$。原 E8 作用给
$$
\delta P=-2(R+S),\qquad \delta S=-2U_1,
$$
所以
$$
\delta\tau_S=-2[R,S]-2[P,U_1],
$$
$$
\boxed{
\widetilde{\mathcal H}
=-\frac23\left\{
\mathcal B_R(\tau_S)+\mathcal B_S(\tau_S)
+\mathcal B_P([R,S])+\mathcal B_P([P,U_1])
\right\}.}
\tag{6}
$$
例如 $\delta S=-2U_1$ 可直接由
$U_1(a,b)=xa'b'+xJ(xa''b'')+\frac12J(x^2a''b''+2a'b')$
分部积分核得。因此 (5)–(6) 只使用已有二次方向与真实交换子第三原型；没有添加一个尚未实现的模板。

## 2. 原完整响应化为一个单层积分

现取 $F=f\odot f$，并记
$$
r=\phi'',\qquad
d=(f'')^2-(\phi'')^2,\qquad A=PD=J(d).
\tag{7}
$$
这里 $d$ 是对称输入的 $[2,2]$ 槽值，不是普通函数 $f^2-\phi^2$ 的某个四阶导数。

由 $A''=-d'$ 和 (2)，(3) 的三项分别为
$$
2\tau_S(A;D)=2J(dd')=-d^2,
$$
$$
-4\tau_S(\phi;\phi,A)=-4J(r^2d'),
$$
$$
4P\{\phi,\tau_S(\phi;D)\}
=4J(rr'd+r^2d').
$$
全部边项使用右 collar 中 $d=r=0$。三项合并得到
$$
\boxed{
\mathcal B_P\tau_S(f^2,\phi)
=-d^2+2J\{(r^2)'d\}.}
\tag{8}
$$
没有删除 $A$ 的左常数，没有把某个单包的三矩设零，也没有留下未经记录的双层 history。

## 3. 不交真实微包上的准确局部化

取任意有限个值支撑严格不交的实紧 profiles $u_i$：
$$
f=\sum_i a_i u_i,\qquad
\phi=\sum_i c_i u_i,\qquad
d_i=a_i^2-c_i^2,\qquad r_i=u_i''.
\tag{9}
$$
各支撑之间留正间隙。于第 $i$ 包，
$r^2=c_i^2r_i^2$、$d=d_i r_i^2$，且
$$
J\{(r_i^2)'r_i^2\}=-\frac12r_i^4.
$$
这个等式对整个区间成立：被积密度是 $(r_i^4)'/2$，在完整单包上的积分严格为零。故该包在自身左方也不留下常数，其他包更不会带来额外交叉尾。

将它代入 (8)，得到
$$
\boxed{
\widetilde{\mathcal K}(f^2,\phi)
=-\frac13\sum_i a_i^2(a_i^2-c_i^2)r_i^4.}
\tag{10}
$$
这是完整原输出，而不是只在包内成立或只在某个 moment 商内成立。

导子 (4) 不扩大任何输入支撑，且
$$
(\mathscr D u)''=x^2u'''+2xu''-2u'.
$$
因此可对 (10) 沿真实四个输入槽同时求导。输出导子与输入导子之差为
$$
\boxed{
\widetilde{\mathcal H}(f^2,\phi)
=\frac13\sum_i a_i^2(a_i^2-c_i^2)
\{10x r_i^4-8u_i'r_i^3\}.}
\tag{11}
$$
在所有相邻间隙及左右外 collar，(10) 和 (11) 都准确为零，且全部 jets 平坦。这里不再需要用一个平台校正来遮蔽其他包的二次尾。

## 4. 两列属于完整 universal pure/self 核

完整 self 的规范是
$$
\mathcal Q(V):u\longmapsto
\frac14[x^2]_{\rm left}V(u^2,0).
\tag{12}
$$
这一节对任意实紧 $u$ 成立，不要求它自身三矩为零，也不先限定同母平移族。

在 (8) 置 $f=0,\phi=u$，有 $d=-r^2$，因而
$$
-d^2+2J\{(r^2)'d\}
=-r^4-2J\{(r^2)'r^2\}=0.
$$
所以 $\pi\widetilde{\mathcal K}=0$。pure 投影与原导子交换；也可直接对上述恒零 pure 函数求导。因此
$$
\pi\widetilde{\mathcal H}=0.
$$

另一方面，令 $f=u,\phi=0$，(10)–(11) 给
$$
\widetilde{\mathcal K}(u^2,0)=-\frac13(u'')^4,
$$
$$
\widetilde{\mathcal H}(u^2,0)
=\frac13\{10x(u'')^4-8u'(u'')^3\}.
\tag{13}
$$
它们都是原区间内的紧输出，左二次系数准确为零。于是
$$
\boxed{
\widetilde{\mathcal K},\widetilde{\mathcal H}
\in\mathcal R\cap\ker\pi\cap\ker\mathcal Q
=\mathcal R\cap\ker E.}
\tag{14}
$$
这比保持原十个低权 self 坐标严格更强。由 R314 的忠实全 self 呈示，还可推出这两列的整个有序矩阵 $\mathsf T$ 为零；本证明没有反过来以 $\mathsf T=0$ 代替整个 self 为零。

注意 (13) 的输出函数一般不为零。因此 (14) 不意味着两列是零成本，也不意味着其完整 period 对任意查询都零。

## 5. 固定同一真实圆与两个内部退化点

现在固定 R324 的最终有限频率、解析紧微包圆，原局部有理芽参数也已经固定。R330 已说明，在一个最终完整 block、一个固定十二副本内部，可选择八完整副本中的两个对应微包，写成
$$
f=\rho_j a\,u(x-t_j),\qquad
g=\rho_j b\,u(x-t_j),
\qquad j=0,1,
\tag{15}
$$
其中
$$
\rho_0\rho_1\ne0,\quad t_0\ne t_1,\quad
a\ne0,\quad a^2-b^2\ne0.
\tag{16}
$$
$u$ 是已经完成所有有限频率与有限纠正后的实际 profile，不换成未扰动母包。原等平方背景的两类幅度确给最后两个不等式。

令
$$
v=u',\quad r=u'',\quad s_3=u''',\quad
A_u=6v s_3-2r^2.
$$
R330 的直接存在证明给一个真实点 $x_*$：
$$
A_u(x_*)=0,\qquad v(x_*),r(x_*)>0.
\tag{17}
$$
简要地，实际 $u=\psi P$ 的 prefactor 为正，左平端邻域有 $u',u''>0$。在 $u'>0$ 的首段令 $z=(u')^{2/3}$，则
$z''=A_u/(9(u')^{4/3})$。$z'$ 从左平端的零值上升，随后在第一个 $u'=0$ 点之前为负，故它在严格内部有一个正最大点；该点满足 (17)。不要求这是简单零点，也不执行数值找根。

写 $\ell$ 为该基本包左端，
$$
\ell_j=\ell+t_j,\qquad x_j=x_*+t_j.
$$
这两个点是当前实际 $A_f$ 的零点，且以后几何联调中保持 profiles 和这些查询点固定。

原修正部分通量为
$$
\boxed{
\begin{aligned}
\mathcal F_j(V)
={}&\int_{\ell_j}^{x_j} f'\,
\partial_x^2 V(f^2,g)\,dx\\
&-\{f(x_j)-f(\ell_j)\}
\partial_x^2V(f^2,g)(\ell_j).
\end{aligned}}
\tag{18}
$$
该延拓在全部 $U$ 上使用原完整函数。当 $\pi V=0$ 时，它正是实际 $V_d$ 分支的相应必要门。

由 R181 的原完整方程，
$$
f'L_f(w)''
=\partial_x\{A_f(f'w''-f''w')\}.
\tag{19}
$$
左平端和右端 $A_f(x_j)=0$ 同时支付边项，且
$L_f(w)''(\ell_j)=0$。所以
$$
\boxed{\mathcal F_j(L_f(w))=0}
\tag{20}
$$
对任意允许的全区间光滑 $w$ 成立。没有要求该 $w$ 在所选微包外为零。

## 6. 两个局部响应的通量和准确行列式

先在基本包上令 $f=a u,g=b u$。由 (10)–(11)，其左平台修正为零。左平端的全部边项也为零。

普通分部积分给
$$
\int_\ell^{x_*}v(r^4)''
=\left[4vr^3s_3-\frac45r^5\right]_{x_*}.
$$
在 (17) 使用 $v s_3=r^2/3$，得到
$$
\boxed{
C_*:=\mathcal F_*(\widetilde{\mathcal K})
=-\frac8{45}a^3(a^2-b^2)r(x_*)^5\ne0.}
\tag{21}
$$

对 $B=10xr^4-8vr^3$，保全部上端 jets 的准确恒等为
$$
\int_\ell^{x_*}v B''
=\left[
8vr^4+40xvr^3s_3-24v^2r^2s_3-8xr^5
\right]_{x_*}.
\tag{22}
$$
例如从 $vB'-rB+\int s_3B$ 推得此式时，
$\int s_3B=2xr^5-2vr^4$；没有残留未计算积分。在 (17)，(22) 化为 $16x_*r(x_*)^5/3$。因此
$$
\boxed{
\mathcal F_*(\widetilde{\mathcal H})
=\frac{16}{9}a^3(a^2-b^2)x_*r(x_*)^5
=-10x_*C_*.}
\tag{23}
$$

在实际第 $j$ 个对应包，四次输出和读出的一个 $f'$ 共给第五次幅度，且 (11) 中的 $x$ 是真实全局坐标。因此
$$
\boxed{
\mathcal F_j(\widetilde{\mathcal K})=\rho_j^5C_*,
\qquad
\mathcal F_j(\widetilde{\mathcal H})=-10x_j\rho_j^5C_*.
}
\tag{24}
$$
其他包在这里没有残留尾，所以不需要给 (24) 添加一个未知“跨包常数”。

由 (16)、(21)，
$$
\boxed{
\det
\begin{pmatrix}
\mathcal F_0(\widetilde{\mathcal K})&
\mathcal F_0(\widetilde{\mathcal H})\\
\mathcal F_1(\widetilde{\mathcal K})&
\mathcal F_1(\widetilde{\mathcal H})
\end{pmatrix}
=-10\rho_0^5\rho_1^5 C_*^2(x_1-x_0)\ne0.}
\tag{25}
$$
从而得到同一个核中的准确满射
$$
\boxed{
(\mathcal F_0,\mathcal F_1)
(\mathcal R\cap\ker E)=\mathbb R^2.}
\tag{26}
$$
不把两个行数当成秩；真实常数、实际间距和完整尾都已进入 (25)。

## 7. 为什么这次能与 whole E 控制真正相接

记
$$
\mathscr P=E(U),\qquad \mathscr L=E(\mathcal R),
\qquad \mathscr C=\mathscr P/\mathscr L,
\qquad
\widehat E=(E,\mathcal F_0,\mathcal F_1).
$$
由 (26)，线性像准确满足
$$
\boxed{
\widehat E(U)=\mathscr P\times\mathbb R^2,\qquad
\widehat E(\mathcal R)=\mathscr L\times\mathbb R^2.
}
\tag{27}
$$
因此增广响应商与原 $\mathscr C$ 自然同构。这里没有声称
$E(U)=E(\mathcal R)$ 在全权成立；R333 的实际输入只是其权零等号和已满联合闭锥。

固定点通量不是仿射不变的 universal 观测，故不能未经证明把 R333 的缩放直接改成作用于 $\ker\widehat E$。正确构造仍在**原 E 商**上进行：

1. 沿 R333 §5.1–5.2，用原 $\mathscr C$ 的非零权缩放、有限真实复制和全部端口桥，取得紧商目标集的真实有限 $C^1$ 截面。其两个通量成本作为真实函数记录，绝不置零。
2. 在 $\mathcal R$ 中选若干列使其 E 像构成 $\mathscr L$ 的基，再加 (5) 两列。由 (25)、(27)，这些列在 $\widehat E(\mathcal R)$ 中构成一个完整基；原 E 列的未知通量成本是矩阵左下块，保留不删。
3. 如 R333 §5.3，先用原商截面消掉各第三 prototype 的 E 商基准。它们的完整第三量保留，新增所有成本都记入新的基准。真实 R101 字给
   $$
   \widehat E_0(t)+n
   \left\{2\sum_j\widehat E(\widehat V_j)
   +\sum_jt_j\widehat E(K_j)\right\}.
   \tag{28}
   $$
   括号内的原 E 商为零；所加两个通量没有引入新的商。
4. 再用一个已固定的原 E 商截面支付 (28) 的目标商差。其整对 E 和两个通量都保留。选择增广响应基坐标后，剩余完整方程仍是
   $$
   F(p,t)+n(A+t)=p_{\rm resp}.
   \tag{29}
   $$
   $F$ 在固定紧参数盒中为 $C^1$，并在选最后整数 $n$ 前已经固定。原 R212/R333 的有限大 $n$ 收缩给准确解与 $C^1$ 目标依赖。

(18) 的额外光滑性可直接由 R56 的实际有限恢复求导后积分获得：profiles、$x_j$ 和积分端点都固定。它是有限维 $U$ 上的真实线性函数，也可用有限原函数评价表达。对自由几何变量的导数仍是 R302 所用的光滑积分密度；profile 坐标中的固定点不产生几何参数中的 Dirac 约束。

因此对真实 $M=\mathbf T=0$ 成本半群 $\mathcal S$，得到
$$
\boxed{
\widehat E(\mathcal S)=E(U)\times\mathbb R^2,
}
\tag{30}
$$
并具有紧目标集上的真实有限 $C^1$ 截面。目标的 E 部分仍须属于 $E(U)$，不是不加相容限制的 $\pi U\times\mathcal Q(U)$。

这一推导不是先独立实现 E，再免费加一个 signed 通量响应。所有 prototype、商修正、真实桥和复制基准都保留在同一个 (28)–(29) 中。

## 8. 与旧 K、G0 的准确关系及 NG0 更正

本节只作原来源核对，不参与 (8)–(30) 的证明。沿用
$$
\mathfrak H=[P,S]-3[P,R],\qquad
\mathcal K=\mathcal B_P([P,R]).
$$
于是
$$
\widetilde{\mathcal K}
=\mathcal K+\frac13\mathcal B_P\mathfrak H.
\tag{31}
$$

R303 定义
$$
\mathcal K_{\rm top}
=\mathcal B_{p_2}(\delta^6\mathfrak H),\qquad
G_0=-\frac{N^9\mathcal K_{\rm top}}{1080\cdot9!}.
$$
其原未除阶乘链给
$$
N^3p_2=-3(R+S),\quad N^4p_2=-6P,\quad N^5p_2=0,
$$
$$
N^6\delta^6\mathfrak H=518400\mathfrak H,\qquad
N^5\delta^6\mathfrak H=-86400\delta\mathfrak H.
$$
Leibniz 只有 $(3,6)$、$(4,5)$ 两项，故
$$
N^9\mathcal K_{\rm top}
=-130636800\,\mathcal B_{R+S}\mathfrak H
+65318400\,\mathcal B_P(\delta\mathfrak H).
$$
因为 $1080\cdot9!=391910400$，准确有
$$
\boxed{
G_0=\frac13\mathcal B_{R+S}\mathfrak H
-\frac16\mathcal B_P(\delta\mathfrak H)
=-\frac16\delta(\mathcal B_P\mathfrak H).
}
\tag{32}
$$
结合 (31)，
$$
\boxed{\delta\mathcal K-2G_0=\widetilde{\mathcal H}.}
\tag{33}
$$
这证明此前提出的修正候选确实等于本稿直接原式给出的局部列。

但是 $G_0$ 的完整 self 平移为常数不意味着它作为完整响应被 N 杀掉。原
$N(\mathcal B_P\mathfrak H)=0$、$H(\mathcal B_P\mathfrak H)=-5\mathcal B_P\mathfrak H$ 和 $[N,\delta]=2H$ 给
$$
\boxed{NG_0=\frac53\mathcal B_P\mathfrak H,}
\tag{34}
$$
并非零身份。确实，R303 原式给 $\mathcal Q(\mathcal B_P\delta\mathfrak H)=-6\mathcal I$，而 $\mathcal Q(\mathcal B_{R+S}\mathfrak H)=0$；故 $\delta(\mathcal B_P\mathfrak H)$ 的 self 非零，$\mathcal B_P\mathfrak H$ 本身也不是零响应。R303 原文已经明确保留完整响应与其 self 的这一差别。本文纠正的是此前讨论中的未证推测，没有修改 R303 的已发表结论。

R336 的准确 $\mathcal Q(\delta\mathcal K)=2\mathcal I$ 与
R303 的 $\mathcal Q(G_0)=\mathcal I$ 也与 (33) 的 whole-self 零一致。不过该对照不能替代第 2–4 节的完整函数与真实尾证明。

## 9. 在同一个实际闭几何上付全部 self 和两条通量

原实际选择必须按以下顺序解释。

先将 R333 的有限库、原 E 商截面、(6) 的有限交换子原型、闭 hook 背景和所需 scalar/frame 桥一同选定。按 R312 的真实安装接口，固定指定有理核心的参数
$$
h=h_e(1+\varepsilon\sigma^2),\qquad
k=\kappa,\qquad \omega=\omega_e,
\quad h_e>0,\ \varepsilon>0,\ \kappa\ne0.
$$
然后取 R324 最终 profiles，固定 (15)–(18) 的两包、退化点和查询。后续不为控制成本重新改 $\varepsilon,\kappa$ 或替换母形。

对这些固定查询，按第 7 节建立真实有限增强截面，全部基准与参数盒进入同一构造。R302 的共享原型与真倒行保证每次扰动后的完整低阶传递仍正确；即使内部第三原型变化，也不把一个旧第三量强行标为当次第三量。指定有理核心保持，核心外的自由几何变化及增强 IFT 共同支付全部目标，并可在同一精确约束族中取得 Morse 性。

Klein 闭合使用修改后 prototype 的真实位移；若背景为 $V_{\rm base}$，完整目标是
$$
\widehat E(V_{\rm base})+4\widehat E(V_B).
$$
取后一项为前者的负值，严格得到一个新实际闭 hook：
$$
\boxed{
\pi V_X=0,\qquad
\mathcal Q(V_X)=0,\qquad
\mathcal F_0(V_X)=\mathcal F_1(V_X)=0.
}
\tag{35}
$$
原 $M=0$、非零第三 hook 结构和共同端口均保留。背景的实际 hook 强度以该几何的 $\tau\ne0$ 为准；这里不需要把某条旧几何的数值 $\tau$ 当作额外不变量。

这是一项新全局几何选择，通常改变度量、全局传入历史、长度及位移。它不是在原冻结几何或原固定 $g$ 上免费叠加响应。最终几何选定以后，才固定它自己的度量、同一个圆和同一个规范问题。

R324 已付的该有理核心条件只依固定局部芽和固定 profiles。对本次真实传入矩阵 $m_*$，重取 R326 同一个
$$
w_c=-\Phi_{m_*}(f^2-\phi_\theta^2).
$$
其合法三矩及六交叉矩仍由原完整复制结构支付。对于 $V_d$，
$$
V_d^c=V_d-2\tau L_f\{\Phi_{m_*}(f^2-g^2)\}.
$$
由 (20)，
$$
\boxed{\mathcal F_j(V_d^c)=\mathcal F_j(V_d)=0,\qquad j=0,1.}
\tag{36}
$$
所以本稿确实支付同一 joint 系统中两条真实必要条件，而没有为它们另选一个不相容的二阶 $w$。

## 10. 已经多付的条件与准确剩余范围

(35) 的 whole-self 零与 whole-pure 零，通过 R314/R292 准确给
$$
\mathsf T(V_X)=0,\qquad q_X(u_i)=0
\quad\text{对当前全部实际微包 }u_i.
\tag{37}
$$
因而 R330 当时仍留下的各包二次平台条件，不再只靠十个低权坐标，而是由同一几何的完整 universal self 支付。这个推论不将原仿射尾和全区间积分常数一并设零。

本稿新付的内部条件仍只有 (36) 的两个实际点；不以两点代表全部 period。尚未支付：

- 其他 $A_f$ 零点、$V_e^c$ 及各包总通量的全部必要条件；
- 真实仿射平台、零间隙与右锚常数的共同匹配；
- 内部退化点的光滑除法、临界点跨接和其余真实端分支；
- 两个完整目标是否实际属于 $L_f$ 的像；
- 周期特解存在后，R327 的十三行是否有同一光滑相位解与正确种子；
- 指定有理核心以外的全部 ruling、高阶收敛及有限等距族。

本稿的严格推进是 (14)、(25)、(30) 和 (35) 的同一条链：原完整响应给两列局部 whole-E 核方向，真实同形副本给两个非零通量，原 E 商与新增响应核一起作有限实际控制，最后在同一新几何、同一圆和同一个规范下保留其真实含义。
