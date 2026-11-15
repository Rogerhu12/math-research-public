# R303：完整 self 平移次数降至九、十维真实响应与同母全部中心的同时支付

日期：2026-11-15。**完整纸面证明；没有执行新的符号程序、profile 求积、秩计算、人工检查或科学运行。**

[R301](R301-five-dimensional-translated-full-self-control-and-compatibility.md) 已给同一母包完整 self 的五维平移响应。本稿使用已有七维 hook 串，把准确响应像扩为全部九次以下多项式；同时从 R56/R73 的完整二阶分子证明，任何真实零矩阵闭块的 canonical self 平移轮廓恰受这个次数上界约束。因此一个先固定的非零实紧母包，其**全部允许平移**的完整 self 可与 whole pure 和整个九维平台矩阵真实同时指定。

核心不是由最高 jet 主符号猜完整次数。第 2 节保留原二阶场、全部局部端势、真实左仿射尾和移动积分下限；唯一十次项由同一累计矩阵的端值准确消去。第 4 节再用完整有限射影流证明新响应的整个平台矩阵为零，未只检查它的最高 self 项。

本稿不支付所有不同母包的共同 self 函数，不把同一有限 $C^2$ 观测纤维当成母包不变，也不宣告完整 period/ruling 已解。

来源：[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R222](R222-simultaneous-real-pure-and-eight-flux-control.md)、[R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md)、[R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md)、[R266](R266-constant-platform-projective-model-for-full-third-kernel.md)、[R295](R295-final-grid-forces-zero-platform-matrix-and-exact-self-history-principal.md)、[R297](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md)、[R298](R298-zero-platform-matrix-with-nonzero-self-response-and-ten-observation-control.md)、R301。

## 1. 同一完整 self 观测

沿用真实成本空间 $U$、完整响应空间 $\mathcal R$、pure 投影 $\pi$，记
$$
\mathcal R_{\mathrm p0}=\mathcal R\cap\ker\pi.
$$
平台矩阵采用 R297 的全 $U$ 真实查询延拓
$$
\mathsf T:U\longrightarrow\operatorname{Mat}_3(\mathbb R).
$$
它由固定左、右三包的真实三矩和原有序交叉尾反解得到，不是在 pure 核外任取补空间。

对任意固定实紧 profile $u$，定义
$$
\mathfrak q_u(V)=\frac14[x^2]_{\rm left}V(u\odot u,0).
\tag{1}
$$
原共同右锚为 $r_*$；左端取真实二次尾的最高系数。在 R292/R295 的 actual whole-pure 零 hook 上，(1) 正是单包自历史 $q_B(u)$。

固定非零实光滑母包 $u$，其支撑含于 $[a,b]$，置
$$
u_c(x)=u(x-c).
\tag{2}
$$
允许的 $c$ 构成一个非空开区间，全部支撑与共同双 collar 留正距离。原右锚不随实际查询改变。平移后重标 $x=y+c$ 时，上锚是 $r_*-c$，仍在未平移母包的共同右零 collar；在这段零区间内移动锚不改变任何原尾。

本稿的最终多项式空间是允许 $c$ 开区间上的真实函数空间。比较系数只用原式在这一开区间的恒等，不需要实际采用无穷大平移或离开 $x+\omega>0$ 的物理允许区。

## 2. 从完整原二阶场证明 self 的平移次数上界

### 2.1 canonical self 的原源，不借 pure 消项删数据

在 R56 的完整第四成本中代入 $F=u^2,\phi=0$，所有含初阶 $Y_\phi$ 的项准确为零，留下
$$
V_B(u^2,0)=-\mathscr P_B H(Z_{u^2},Z_{u^2}).
\tag{3}
$$
这是原输入代入，不要求 $\phi=0$ 自身是一条非退化合法圆。它也不使用 $\pi V_B=0$ 来删去某个余项。whole-pure 身份只在把(1)重新识别为 R292 的 $Q_{ii}$ 时使用。

设实际块满足 $M_B=0$，其共同几何端口和 frame 真实闭合，二阶累计矩阵
$$
m(s)=\int_{s_0}^s M(\sigma)\,d\sigma
$$
保原初值
$$
m(s_0)=m(s_1)=0.
\tag{4}
$$
全部连接段和原端势包含在 $M(s)$ 中；不逐段重锚。按 R73，
$$
W_2=\Phi_{m(s)}(u,u).
\tag{5}
$$

记
$$
\gamma=h_s,\quad d=h\omega-k,\quad e=hx+d,\quad
Q=1+e^2,\quad z=x+\omega.
$$
R295 的完整二阶恢复为
$$
V_Z=(A_Z,zP+B,eA_Z-hW_2),\qquad
A_Z=(W_2)_x/2+\eta_0/h,
\tag{6}
$$
$$
P=\frac{J_e}{8h}+\frac e8(u')^2,\qquad
B=\frac{|V_Y|^2}{2h},
\tag{7}
$$
$$
\eta_0=
-\frac{e_sQ}{16h^2}(u'')^2
+\frac{\gamma Q}{8h^2}u'u''
-\frac{\gamma e}{8h}(u')^2
-\frac1{16}\partial_s(J_e/h).
\tag{8}
$$
式(8)保完整 $s$ 微分，不先把几何冻结。

### 2.2 同锚平移的全部高次来源

在 $x=y+c$ 下记
$$
r=u''(y),\qquad r'=u'''(y),\qquad
J_0(y)=\int_y^{r_*-c}r(\eta)^2d\eta,
$$
以及原 $J_1,J_2^*$。共同右零 collar 使
$$
J_0[u_c](y+c)=J_0[u](y),
$$
$$
J_1[u_c](y+c)=cJ_0[u](y)+J_1[u](y),
$$
$$
J_2^*[u_c](y+c)=c^2J_0[u](y)+2cJ_1[u](y)+J_2^*[u](y).
\tag{9}
$$
这里 $J_2^*=\int(x^2(u'')^2+2(u')^2)$，其 $2(u')^2$ 未删。

R255 的八个完整二次算子中，只有 $\Phi_{p_2}$ 能在(5)产生平移四次项。其完整式含
$$
\Phi_{p_2}(u,u)
=-xu^2+x^2uu'-\frac{x^3}{2}(u')^2-\frac{x^2}{4}J_2^*(u,u).
$$
由(9)，准确得到
$$
\deg_c W_2\le4,\qquad
[c^4]W_2(s,y+c)=-\frac{m_{p_2}(s)}4J_0(y).
\tag{10}
$$

式(7)、(8)分别给
$$
\deg_c P\le2,\quad \deg_c B\le2,\quad
\deg_c\eta_0\le3.
\tag{11}
$$
最后一项 $\partial_s(J_e/h)$ 至多二次；$e_sQ$ 是唯一可能的三次因子。于是(6)、(10)给
$$
[c^4]A_Z=\frac{m_{p_2}}8r^2.
\tag{12}
$$
$V_Z$ 的三个分量次数分别至多为 $4,3,5$，而五次项唯一来自 $eA_Z$：
$$
[c^5]V_Z=
\left(0,0,\frac{h\,m_{p_2}}8r^2\right).
$$
对真实 profile 坐标求导，$D_x=D_y$，所以完整身份为
$$
\boxed{
[c^5]V_{Z,x}
=\left(0,0,\frac{h\,m_{p_2}}4r r'\right).
}
\tag{13}
$$
没有把(13)当作全部场；它只是完整有限多项式的准确最高系数。所有低次字段、原尾及局部 chain 项仍在(6)–(11)中。

### 2.3 固定左 collar 与移动包之间的尾必须保留

令固定左 collar 点为 $\ell$，令 $U_c(s),V_c(s)$ 为平移单包在其左外区间的真实仿射分子
$$
V_Z=xU_c+V_c.
$$
由 R292 的三矩恢复，$U_c,V_c$ 均对
$$
\mu(u_c)=\bigl(\mu_0,\mu_1+c\mu_0,
\mu_2+2c\mu_1+c^2\mu_0\bigr)
\tag{14}
$$
线性。因此它们及 $\nabla_sU_c$ 的平移次数都至多为二。

特别不能把 $V_{Z,x}$ 当成紧函数。对完整原积分
$$
E_Z(s,c)=\int_\ell^{r_*}|V_{Z,x}(s,x;u_c)|^2dx
$$
有准确分裂
$$
\boxed{
E_Z(s,c)
=(a+c-\ell)|U_c(s)|^2
+\int_a^b|V_{Z,x}(s,y+c;u_c)|^2dy.
}
\tag{15}
$$
右侧包外场为真零，左侧为真常导数 $U_c$。第一项次数至多为五；这正是移动积分下限产生的真实尾，不得丢掉。第二项由(13)次数至多为十，且
$$
\boxed{
[c^{10}]E_Z(s,c)
=\frac{h^2m_{p_2}^2}{16}
\int_a^b r^2(r')^2dy.
}
\tag{16}
$$

### 2.4 完整十次项是一个已付真实端项

R295(20)–(21)的完整左尾恒等为
$$
[x^2]\mathscr P H(Z,Z)
=\int_B\left\{
\frac{k}{2h}E_Z
+k\left[(\ell-\omega)\frac{|U_c|^2}{2h}
+\frac{U_c\cdot V_c}{h}\right]
+\frac{|\nabla_sU_c|^2}{2h^2}
\right\}ds.
\tag{17}
$$
除 $E_Z$ 外，显示的每项次数至多为四；(15)的额外左尾至多为五。所以(3)、(16)、(17)给完整 self 的十次系数
$$
[c^{10}]\mathfrak q_{u_c}(V_B)
=-\frac1{128}
\left(\int_Bkh\,m_{p_2}^2ds\right)
\int r^2(r')^2dy.
\tag{18}
$$

R73(9)是逐点原身份
$$
(m_{p_2})_s=-kh/2.
$$
故由(4)
$$
\int_Bkh\,m_{p_2}^2ds
=-\frac23[m_{p_2}^3]_{s_0}^{s_1}=0.
\tag{19}
$$
这是完整三次 history 端项消零，未假定 $k$ 或 $m_{p_2}$ 逐点为零。

由此得到
$$
\boxed{
c\longmapsto\mathfrak q_{u_c}(V_B)
\ \in\operatorname{Pol}_{\le9}
\quad\text{对每个真实 }M_B=0\text{ 闭块。}}
\tag{20}
$$
R130 的 $U$ 由这些真实零低阶成本张成；(1)线性，故(20)延至全部 $V\in U$。第三 hook 背景也可直接用同一原式证明(20)，或由其真实倒行双字归属 $U$ 后继承。

这个结论覆盖完整 $C^2$ 余项和所有累计尾，不是由 R295 主符号次数推断。只知道主项的 $c^{10}$ 为零不足以得到(20)；本节使用的是完整(6)、(15)、(17)。

## 3. 七维 hook 串及完整 self 公式

沿用 R255 的
$$
P=\Phi_{r_0},\qquad E_+=\Phi_{p_2},
\qquad \mathfrak H_j=\delta^j\mathfrak H\quad(0\le j\le6),
$$
以及
$$
N=\mathscr L_{\partial_x},\quad
H=\mathscr L_{x\partial_x-1},\quad
\delta=\mathscr L_{x^2\partial_x-2x}.
$$
$\mathfrak H$ 的 H 权为 $-3$，所以准确未除阶乘规范给
$$
N\mathfrak H_j=-j(7-j)\mathfrak H_{j-1}
\quad(1\le j\le6),\qquad N\mathfrak H_0=0.
\tag{21}
$$
二次块有
$$
N^4E_+=-6P,\qquad N^5E_+=0.
\tag{22}
$$
N 对完整响应两槽满足 Leibniz 规则。

R258 给
$$
K_f^\tau=-J^3\mathscr A_f^\tau,\qquad
\mathscr A_f^\tau=D^2(aD^2)+D(bD)+c,\qquad
(\mathscr A_f^\tau)^*=\mathscr A_f^\tau .
$$
因此对任意这些 $\tau\in Z$，完整 self 是
$$
\boxed{
\mathfrak q_u(\mathcal B_E\tau)
=-\frac14\int c_{\tau,u}\,\Phi_E(u,u).
}
\tag{23}
$$
原二次输出可以有真实左多项式尾；右三常数由原 K 支付。

对根 $\mathfrak H_0$，
$$
\mathscr A_f^{\mathfrak H_0}
=D^2\{(6f'f'''-2(f'')^2)D^2\}
-D\{6(f''f''')'D\}.
\tag{24}
$$
故 $c_{\mathfrak H_0}=0$，即
$$
\mathfrak q_u(\mathcal B_E\mathfrak H_0)=0
\quad\text{对全部 }E,u.
\tag{25}
$$

由 R258 的完整系数递推，首条导链满足
$$
c_{\mathfrak H_1,u}=-6D^3((u'')^2)
=-1024\,c_{\chi_{30},u}.
\tag{26}
$$
这是 c 的完整身份，不把两个完整第三算子认成同一个。由 R298，
$$
\boxed{
\mathfrak q_u(\mathcal B_P\mathfrak H_1)
=-6\,\mathcal I(u),\qquad
\mathcal I(u):=\int(u'')^2(u''')^2>0.
}
\tag{27}
$$
非零实紧母包保证严格性。若该积分为零，则在 $u''\ne0$ 的每个连通区间上 $u'''=0$；连续到紧支端点只能得到 $u''=0$，继而 $u=0$，矛盾。

## 4. 新最高响应的整九矩准确为零

定义
$$
\boxed{\mathcal K_{\rm top}=\mathcal B_{E_+}(\mathfrak H_6).}
\tag{28}
$$
因 $\Delta\mathfrak H_6=0$，它是实际 pure-zero 响应。还必须证明它在整个平台矩阵核内；不能从某个 self 主项推断这一点。

### 4.1 一个完整有限流矩身份

记射影小参数为 t，取其足够小，使相关紧支和共同 collars 保持合法。R266 的有限流为
$$
\rho_tu(y)=(1+ty)^2u\!\left(\frac y{1+ty}\right),
$$
$$
\mathscr A_u^{e^{t\delta}\mathfrak H}
=e^{-tZ^*}\mathscr A_{\rho_tu}^{\mathfrak H}e^{-tZ},
\quad Z=x^2D-2x,\quad Z^*=-x^2D-4x.
\tag{29}
$$
这里只消费已付完整局部源共轭，原 K 的右常数不作重选。

置 $A=1+ty$、$h_t=\rho_tu$。因为
$$
\rho_t1=A^2,\qquad \rho_t(x^2)=y^2,
$$
(29)和真实变量代换给
$$
\int x^2c_{e^{t\delta}\mathfrak H,u}(x)dx
=\int y^2\mathscr A_{h_t}^{\mathfrak H}(A^2)\,dy.
\tag{30}
$$
这里所有算子系数由紧 $h_t$ 给出，故可对多项式 $1,x^2$ 作真实分部积分；没有给非紧 profile 偷设零端迹。

写
$$
a_{h_t}=6h_t'h_t'''-2(h_t'')^2,\qquad
V_{h_t}=6(h_t''h_t''')'=3D^2((h_t'')^2).
$$
由(24)
$$
\int a_{h_t}=-8\int(h_t'')^2.
$$
而(30)的双线性形式准确为
$$
4t^2\int a_{h_t}
+4t\int y(1+ty)V_{h_t}
=-32t^2E_t+24t^2E_t=-8t^2E_t,
\tag{31}
$$
其中 $E_t=\int(h_t'')^2$。

该能量也可完整积出，而不是近似。设 $B=1-tx$，则
$$
h_t''=B^2u''+2tBu'+2t^2u,\qquad dy=B^{-2}dx.
$$
平方后对紧 $u$ 分部积分：含 $u^2/B^2$ 与 $uu'/B$ 的两项准确相消，其余给
$$
\boxed{
E_t=\int\{(1-tx)^2(u'')^2+2t^2(u')^2\}
=\mu_0(u)-2t\mu_1(u)+t^2\mu_2(u).
}
\tag{32}
$$
这是同一真实三矩，特别保 $\mu_2$ 中的 $2(u')^2$。

综上，
$$
\boxed{
\int x^2c_{e^{t\delta}\mathfrak H,u}
=-8t^2\{\mu_0-2t\mu_1+t^2\mu_2\}.
}
\tag{33}
$$
右端最高为四次。按
$e^{t\delta}\mathfrak H=\sum t^j\mathfrak H_j/j!$ 比较系数，准确得到
$$
\int x^2c_{\mathfrak H_5,u}=
\int x^2c_{\mathfrak H_6,u}=0
\quad\text{对全部真实紧 }u.
\tag{34}
$$

### 4.2 从真实右包尾到整个矩阵核

若 $u$ 全在紧包 $v$ 左方，完整二次 $E_+$ 在 u 支撑处为
$$
\Phi_{E_+}(v,v)(x)=-\frac{\mu_2(v)}4x^2.
\tag{35}
$$
没有遗漏常数或一次项：它们在这个特定原八矩方向确为零。

R297/R298 的完整有序查询公式为
$$
\mathfrak t_{u,v}(\mathcal B_E\tau)
=-\frac14\int c_{\tau,u}(x)\,
\Phi_E(v,v)(x)\,dx.
\tag{36}
$$
将(34)、(35)代入，所有这种原查询为零。由 R297 的三矩开集或固定三左三右基，
$$
\boxed{\pi\mathcal K_{\rm top}=0,\qquad
\mathsf T(\mathcal K_{\rm top})=0.}
\tag{37}
$$
这是真完整九矩零，而不是一条矩值或只对三矩为零的单包成立。

### 4.3 N 保留这一共同核

对完整成本的平移作用，所有输入与输出同时按原同锚重标。左二次多项式的最高系数在坐标平移下不变；共同右锚的变动留在零 collar。因此
$$
\frac{d}{dc}\mathfrak t_{u_c,v_c}(V)
=\mathfrak t_{u_c,v_c}(NV).
\tag{38}
$$
若 $\mathsf T(V)=0$，左端对全部互相分离的真实 u、v 恒为零。再用同一三矩基，得 $\mathsf T(NV)=0$。pure 投影也与真平移交换。于是
$$
\boxed{
N^j\mathcal K_{\rm top}\in
\mathcal R_{\mathrm p0}\cap\ker\mathsf T
\quad\text{对所有 }j\ge0.
}
\tag{39}
$$
没有把固定圆 period 商当作 sl2 模；(38)只陈述本稿明确定义的 universal 原查询。

## 5. 十维完整 self 平移同构

### 5.1 唯一非零最低 self 系数

用(21)、(22)逐槽展开 $N^9\mathcal K_{\rm top}$。可能的两种分配是二次方向用三次/四次 N、第三方向用六次/五次 N。第一种落在 $\mathfrak H_0$，其完整 self 由(25)为零。第二种用
$$
N^4E_+=-6P,\qquad
N^5\mathfrak H_6=-86400\,\mathfrak H_1.
$$
故
$$
\mathfrak q_u(N^9\mathcal K_{\rm top})
=\binom94(-6)(-86400)
\,\mathfrak q_u(\mathcal B_P\mathfrak H_1)
=-391910400\,\mathcal I(u).
\tag{40}
$$
这里 $391910400=1080\cdot9!$。

$N^{10}\mathcal K_{\rm top}$ 只剩
$$
N^{10}\mathcal K_{\rm top}
=-653184000\,\mathcal B_P\mathfrak H_0.
\tag{41}
$$
它的完整 self 为零，且 $N^{11}\mathcal K_{\rm top}=0$。不把(41)的真实响应本身宣成零。

由同锚原平移，
$$
\mathfrak q_{u_c}(V)=\mathfrak q_u(e^{cN}V).
\tag{42}
$$
因此(40)准确给
$$
[c^9]\mathfrak q_{u_c}(\mathcal K_{\rm top})
=-1080\,\mathcal I(u)\ne0.
\tag{43}
$$
这是完整 self 的系数，不是最高 jet 近似。

### 5.2 明确十条列及所有低阶项

定义
$$
G_l=-\frac{N^{9-l}\mathcal K_{\rm top}}{1080\cdot9!},
\qquad 0\le l\le9,
\tag{44}
$$
并记 $d_l(u)=\mathfrak q_u(G_l)$。由(39)、(40)，
$$
\pi G_l=0,\quad \mathsf T(G_l)=0,\quad
d_0(u)=\mathcal I(u)>0.
\tag{45}
$$
对 $l\ge1$ 有 $NG_l=G_{l-1}$；$NG_0$ 未必是零响应，但由(41)它的全部完整 self 为零。故(42)准确给
$$
\boxed{
\mathfrak q_{u_c}(G_l)
=\sum_{r=0}^l\frac{c^r}{r!}d_{l-r}(u).
}
\tag{46}
$$
每一项均来自完整原算子，不需新增求积。式(46)的最高项是
$\mathcal I(u)c^l/l!$，于是
$$
\boxed{
\mathcal Q_u:
\operatorname{span}(G_0,\ldots,G_9)
\longrightarrow\operatorname{Pol}_{\le9},\quad
V\mapsto[c\mapsto\mathfrak q_{u_c}(V)]
\quad\text{是同构。}}
\tag{47}
$$

这里十条成本本身也真实独立：一个零成本关系经(47)必使全部系数为零。但没有宣称整个 self 空间只有十维；(47)先固定了母包 u。

结合第 2 节，
$$
\boxed{
\mathcal Q_u(U)=
\mathcal Q_u(\mathcal R_{\mathrm p0}\cap\ker\mathsf T)
=\operatorname{Pol}_{\le9}.
}
\tag{48}
$$
这次是完整次数上界与明确真实响应下界夹逼，不只是十个点值的偶然独立。

## 6. 九矩加全部平移轮廓的真实联合控制

任选十个互异允许中心 $c_0,\ldots,c_9$。由(46)，self 评价矩阵
$$
S_{jl}=\mathfrak q_{u_{c_j}}(G_l)
$$
的准确行列式为
$$
\boxed{
\det S=
\frac{\mathcal I(u)^{10}}{\prod_{l=0}^9l!}
\prod_{0\le i<j\le9}(c_j-c_i)\ne0.
}
\tag{49}
$$
若 queries 带非零幅度，行列式再乘所有幅度的四次方。查询本身不必组成圆；若用于实际编码微包，仍按原圆要求使其支撑合法且不交。

R297 的九条 $R_{ab}$ 给 $\mathsf T(R_{ab})=e_{ab}$。用(47)的准确逆，减去一个 G 组合，即可消掉每条 $R_{ab}$ 的**整个**固定母包 self 多项式，不仅十个值。因此
$$
\boxed{
(\mathsf T,\mathcal Q_u)(\mathcal R_{\mathrm p0})
=\operatorname{Mat}_3(\mathbb R)\oplus
\operatorname{Pol}_{\le9}.
}
\tag{50}
$$
这是十九个真正独立的有限原查询；不是形式生成数。

将 R222 的一般有限观测定理应用于
$$
F=(\mathsf T,
\mathfrak q_{u_{c_0}},\ldots,\mathfrak q_{u_{c_9}}),
$$
便可对任意 $p\in\pi U$、矩阵 A 和任意 $Q\in\operatorname{Pol}_{\le9}$，得到有限真实同端口、frame 恒等的块 D，满足
$$
\boxed{
M_D=\mathbf T_D=0,\quad
\pi V_D=p,\quad
\mathsf T(V_D)=A,\quad
\mathfrak q_{u_c}(V_D)=Q(c)
\ \text{对全部允许 }c.
}
\tag{51}
$$
$\mathbf T_D$ 是完整第三算子，区别于平台矩阵。最后一个全区间恒等由完整(20)和十个准确值推出；没有将十个近似样本外推成函数身份。

R222 的实际复制、桥、whole-pure 截面及最后有界 $C^1$ 误差全部保留。纯校正会改变 self，但其改变仍在同一个九次多项式空间中，已经由这十九个联合观测同时支付。没有先求一个符号负成本再假定其实际实现。

加入先选真实 hook 背景并按原 Klein 四块规范给四分之一校正，得到实际闭 hook X：
$$
\boxed{
M_X=0,\quad
\mathbf T_X=\kappa\mathfrak H,\quad
\pi V_X=0,\quad
\mathsf T(V_X)=A,\quad
q_X(u_c)=Q(c)
\quad\text{对全部允许 }c.
}
\tag{52}
$$
尤其可取 $A=0,Q=0$。于是该固定母包任意有限数量、任意允许不同中心、任意非零实幅度的所有完整 $q_i$ 同时为零；包数可以远大于十。

共同 I 的选择仍先于最后计数：先选 fixed full-pure 库、九矩及本稿十方向的原生成族、背景和桥，再选 I 和母包；最后选真实参数盒与有限重复。大系数用有限复制实现，不需要扩大既有 scalar 包络。

本稿不单凭(50)宣告保预先冻结的度量、总长或 Gaussian germ。若另调用 R302 已付的完整 prototype 结构和最终增强 IFT，可以对明确已经包括的有限观测作相应 germ/Morse 安装；不能据此顺带固定一个未纳入控制的整个无限 shape 族。

## 7. 同母全中心与换母问题的准确边界

### 7.1 已经取消了 R301 的多中心插值余门

对同一固定 u，第 2 节证明整个真实 self 轮廓都在 $\operatorname{Pol}_{\le9}$。第 5 节又给完整响应同构。因此不再留下“第十一个中心也许多一个新 self 条件”的问题：任意多个中心的值都受同一个次数上界约束。

这是对固定母形的完整结论，不只是“至多十个数可控”。也没有借用当前模板某几个位置的特殊关系。

### 7.2 不能因此同时清所有不同母包

换成 $\widetilde u$ 后，(46)的十个 $d_l$、三角逆、原控制基准和最终几何参数一般都改变。虽然 $\mathcal I(\widetilde u)>0$ 使同一十条原生成方向仍给该母包的同构，但它们不必用**同一组**控制系数同时消掉两种母包。

因此不能将(48)改写成
$$
\{u\mapsto\mathfrak q_u(V):V\in U\}
=
\{u\mapsto\mathfrak q_u(V):V\in
\mathcal R_{\mathrm p0}\cap\ker\mathsf T\}.
$$
这个真正的全 Q 函数像结论尚未证明。

同 $\mathcal F^\star$ 或同 $\mathcal F^+$ 的高频母包仍可能有不同
$\int(u'')^2(u''')^2$ 和不同完整 $d_l$。R295/R298 的正则阶边界保留；不能把完整 self 悄悄加进一个仅 $C^2$ 的观测系统。

### 7.3 一个已有来源支持的有限参数接口

R301§8的参数化论证可原样用本稿十列替换五列：对一个已经明确给定的紧、有限维、非零母包族，若 profiles/中心/幅度关于参数为 $C^1$ 的 $C^3$ 值映射，并有固定支撑包络和中心间距，则 $\mathcal I$ 在紧集上有正下界，(49)及其逆有统一 $C^1$ 界。

原生成库不变；先把母包参数与全部目标纳入联合 compact 盒，再选统一有限复制数，最后对完整十九个观测及 whole pure 作同一次实际校正。这给一个随母包参数重新选择几何的 $C^1$ 截面。

它不是一个冻结几何对整个 shape 族的共同解；也不授无限高频全族的统一 $C^3$ 界或预算。若实际构造的 profile 由后来选择的几何反过来决定，还必须支付这个相互依赖的联合选择次序，不能把两次分别存在直接拼接。

## 8. 已付与未付

本稿的新增完整结论是：

- 全 canonical self 平移次数至多九，完整十次项由真实 $M=0$ 消去，原左尾和移动积分下限保留；
- 一个明确响应 $\mathcal B_{p_2}(\mathfrak H_6)$ 的整个平台矩阵为零，其完整 self 具有严格非零九次项；
- 十条明确 N 导链对每个固定非零母包给全部 $\operatorname{Pol}_{\le9}$，完整上下界一致；
- whole pure、九矩和同一母包的全部允许中心 self 可真实同时支付；
- 换母、有限参数族、固定几何与全 Q 函数像之间的边界明确保留。

当前巨量编码圆若所有微包确为该同一母包的幅度和平移，此结论支付它们全部二次 self 数值；若最终同纤维构造使用不同母包或不同宽度，则必须按第 7 节另付联合兼容，不能直接套同母结论。

内部 Laurent、端通量、平台仿射部分、全角其余 mixed 函数和同一个二阶 gauge 的 ruling 仍分别需要原完整条件。本稿没有重新执行旧 pure、八 χ、Gaussian 能量或 canonical 第四 forcing，也没有以十九维联调替代主课题完成。

作者责任：所有新系数和消项来自上述有限手写微分、同锚积分、真实端值与已发表有限控制定理；没有新增科学执行或未披露的符号计算。
