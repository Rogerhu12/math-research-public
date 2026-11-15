# R794 — 原 E/J 深交域的完整三态返回、五维首矩与实际 W 环带

日期：2026-11-15。**状态：已证明。**

本篇保持 R734 的同一个最终测试 $q=q_N^*$，不重新适配任何一行。
从 R785 的完整三维偶深核与 R692 的整个 Y/Z 核，在真实限制域上约消，
得到 $E_{\mathcal V}$ 的完整偶深返回。它不是物理 E；二者仍差原 J 截距。

这一返回把 R791 已识别的整个五维 J 条件首矩准确带进
$\{E,J\in p^N\}$。系数为 $\lambda^N(119+144\kappa^N)/263$，
在原射线上为单位。旧帽与此交域的相交却必有 t 深 N，
故可在同一观察 $t/Y$、同一 q 下精确相减，给出帽外完整余域的非零首矩。
随后对原 Z 偶环带得到同一有限来源的全部首矩，以及真正 W 中央行的
非零首项和完整外部补偿。没有把这些受限行改认成一个新的原中央零。

## 1. 原来源、固定参数与三维几何

保 R785/R786/R791 的原普通射线、全部固定坏集和相对密度一子族：
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad N\in4\mathbf Z_{>0},\quad u=\kappa^N.
\tag{1}
$$
$p>163$，且当前好素数不等于263。实际 $\lambda,\kappa,u$ 都在
固定嵌入的 $K=\mathbf Q(\omega)$ 中；$\eta=\eta(p)$ 沿 N 变化保持固定。

沿原六输入和 R785 的行，记
$$
\begin{gathered}
a=1+3\omega,\quad h_0=17+3\omega,\quad
b_Y=(20+3\omega)/17,\\
P=b_YY+Z_0,\qquad W=P-at=b_YY+Z,\qquad Z=Z_0-at,\\
E=E_{\mathcal V}+e_JJ,\qquad
e_J=-1841/72,\\
E_{\mathcal V}=-\frac{17(25+48\omega)}{144}Z_0+h_0t .
\end{gathered}
\tag{2}
$$
原 $C,H_1,J$ 都正交于
$\mathcal V=\operatorname{span}(Y,Z_0,t)$。
整个实际 q 只依赖这三个伙伴，包括其全部六支、深/单位门、
最高三十次权、完整 C 深补项和所有 $\lambda,\kappa,u,\eta$ 系数。

原三态仍为 $e_0,e_1,e_2$，$h_W=e_1+e_2$。置
$$
c_B=1-\omega^2,\qquad B_0=(e_0-\omega h_W)/c_B,\qquad
\rho_\mu=q\mu .
\tag{3}
$$
本篇的完整来源恒等式适用于整个原三态空间。
首矩与非零结论使用 B0。原几何满足
$$
\mathcal T_*B_0=\omega^2B_0,\quad
Y\mathcal T=Y,\ P\mathcal T=P,\ J\mathcal T=J,\quad
t\mathcal T=\omega^2t,\quad q\circ\mathcal T=q .
\tag{4}
$$

R785 的准确范数为
$$
N(Y)=34,\qquad N(Z_0)=288/17,\qquad N(t)=2,\qquad
N(J)=72/7.
$$
用 $(25+48\omega)a=-7h_0$，(2) 又可写成
$$
\boxed{
E_{\mathcal V}=\frac{h_0}{144a}\Delta,\qquad
\Delta=119Z_0+144at,\qquad
N(E_{\mathcal V})=\frac{247\cdot263}{72}.}
\tag{5}
$$
确实 $N(h_0)=247=13\cdot19$；
Z0 项的范数为 $119\cdot247/72$，t 项为 $144\cdot247/72$。
此外
$$
E_{\mathcal V}\perp Y,\qquad E_{\mathcal V}\perp Z,
\qquad Z=W-b_YY.
\tag{6}
$$
所有换基分母及显示范数在当前 p 处均为单位。
因此 $(Y,Z,E_{\mathcal V})$ 是同一个 $\mathcal V$ 的真正正交整框架，
没有把物理 E 的 J 截距吸收进去。

## 2. 用整域推前约消支付 E_V 的整个偶核

对行 L 使用原实际映射
$$
P_{L,z}=I+(z-1)\bar L^{\,t}L/N(L).
$$
令 $r\ge0$ 为偶数，$v=\kappa^r$。
R692 给原三态的完整 Y、Z 两层核，R785 给整个 $\mathcal V$：
$$
\begin{aligned}
\rho_\mu|_{\{Y,Z\in p^r\}}
 &=\lambda^{2r}(P_{Y,v}P_{Z,v})_*\rho_\mu,\\
\rho_\mu|_{\{\mathcal V\in p^r\}}
 &=\lambda^{3r}(M_{\mathcal V,v})_*\rho_\mu .
\end{aligned}
\tag{7}
$$
第一式保原一层的物理 $R_Y$ 与交换态；它们只因 r 偶而准确平方消去。
不是从边际 S/T 推出联合 scalar。

由 (6)，$P_{Y,v}P_{Z,v}$ 固定 $E_{\mathcal V}$。
在(7)第一式再限制 $E_{\mathcal V}\in p^r$，得到
$$
\rho_\mu|_{\{\mathcal V\in p^r\}}
=\lambda^{2r}(P_{Y,v}P_{Z,v})_*
           \bigl(\rho_\mu|_{E_{\mathcal V}\in p^r}\bigr).
$$
而
$M_{\mathcal V,v}=P_{Y,v}P_{Z,v}P_{E_{\mathcal V},v}$。
与(7)第二式比较，在完整整像上的推前单射下约去
$\lambda^{2r}(P_{Y,v}P_{Z,v})_*$，严格得到
$$
\boxed{
\rho_\mu|_{E_{\mathcal V}\in p^r}
=\lambda^r(P_{E_{\mathcal V},\kappa^r})_*\rho_\mu,
\qquad r\in2\mathbf Z_{\ge0}.}
\tag{8}
$$
所以(8)保全部三个状态、全部原伙伴、同一个 q。
这里没有宣称任意受限测度的深限制算子可逆，也不需另猜一个
高次数 whole scalar。约消发生在(7)已经支付的同一个完整来源上。

同理，$(Y,Z,E_{\mathcal V})$ 的任意偶深矩形都是原来源上的真实返回，
总系数为三个深度对应的 $\lambda$ 幂之积。
任何额外门都必须按这三个实际正交缩放转置。

## 3. 完整物理矩阵、E 截距与所有附门

从(5)直接算实际 $P_{E_{\mathcal V},v}$：
$$
\boxed{
\begin{aligned}
Y'&=Y,\quad W'=W,\quad Z'=Z,\quad J'=J,\\
t'&=\frac{(119+144v)t+119(v-1)Z_0/a}{263}
    =\frac{-119Z+v\Delta}{263a},\\
Z_0'&=\frac{(144+119v)Z_0+144a(v-1)t}{263}
     =\frac{144Z+v\Delta}{263},\\
P'&=b_YY+Z_0',\qquad
E'=vE_{\mathcal V}+e_JJ .
\end{aligned}}
\tag{9}
$$
C、H1、q 亦逐点固定。矩阵确实保持 $Z_0'-at'=Z$，
将 $\Delta$ 乘 v；在 $(Z_0,t)$ 上的行列式为 v。

特别，在 $J\in p^N$ 上，
$$
\boxed{
E\in p^N\Longleftrightarrow E_{\mathcal V}\in p^N.}
\tag{10}
$$
故对任意完整连续测试 f，(8)给
$$
\boxed{
\int_{\{J,E\in p^N\}}f\,d\rho_\mu
=\lambda^N\int_{J\in p^N}
                 f\circ P_{E_{\mathcal V},u}\,d\rho_\mu.}
\tag{11}
$$
若 f 只依 Y、W、J，则它在(11)中完全不变。
更一般，若 $J\in p^j$、$E\in p^r$、$j\ge r$ 且 r 偶，
相同证明给 $\lambda^r$ 及(9)中的 $v=\kappa^r$；
q 的固定测试深度仍是 N，没有静默更换 q。

原失败观察为
$$
U=u_JJ+u_ZZ_0,\qquad
u_J=\frac{7(4+9\omega)}{72},\quad
u_Z=-\frac{68+33\omega}{144}.
$$
它在(11)的右边准确为
$$
\boxed{
U'=u_JJ+\frac{u_Z}{263}(144Z+u\Delta).}
\tag{12}
$$
所以附 $U\notin p^{N+300}$ 时，必须使用(12)的整个不等式。
附 t-unit、P-unit 或原 cd 门，也分别使用(9)；
t-unit不能在这里免费替换成一个标量 depletion。
在 $u\in p^N$ 的范围，$Z_0'\in p^N$ 与 $t'\in p^N$
各自都准确等价于 $Z\in p^N$，但深达 $N+300$ 的失败门
仍含(12)的 $u\Delta$，不能删除。

## 4. 同一 (Y,W) 全来源的四个 E/J 格

令 $\pi=(Y,W)$，并对每个原态记
$$
\mathscr B_{\rm all}=\pi_*\rho_\mu,\quad
\mathscr B_J=\pi_*(1_{J\in p^N}\rho_\mu),\quad
\mathscr B_E=\pi_*(1_{E\in p^N}\rho_\mu).
$$
这些都是整个两输出测度；没有把 $\mathscr B_E$ 认作其两个边际的张量积。
(11)给完整分割
$$
\boxed{
\begin{array}{c|cc}
 &E\in p^N&E\notin p^N\\ \hline
J\in p^N&
\lambda^N\mathscr B_J&(1-\lambda^N)\mathscr B_J\\
J\notin p^N&
\mathscr B_E-\lambda^N\mathscr B_J&
\mathscr B_{\rm all}-\mathscr B_E-(1-\lambda^N)\mathscr B_J .
\end{array}}
\tag{13}
$$
该表允许任意相同的 Y/W 混合观察和 unit 条件，不只常数测试。
若另附依赖 P 或 t 的门，须返回(11)，不能继续用(13)省去其转置。

原 R702/R734 的 E 深三态边际仍准确为
$$
\begin{aligned}
Y_*(1_{E\in p^N}q(e_0,e_1,e_2))
&=\lambda^{2N}(S,\ \omega^2S/2+[1/2]_*U_{136},\
                        \omega^2S/2-[1/2]_*U_{136}),\\
W_*(1_{E\in p^N}q(e_0,e_1,e_2))
&=\lambda^{2N}6\delta(T,T,-T).
\end{aligned}
\tag{14}
$$
原整 q 总边际和 R791 的 J 来源也全部保持。
但(14)并未给 $\mathscr B_J$ 的 W 中央一个额外的零；
(13)明确留下另一行的完整差。

## 5. B0 的整个五维首矩进入真实 E 深门

对任何 T-不变的 J 条件及任意完整 Y 测试，由(4)有
$$
Y_*(1_{J\in p^N}qB_0)=0,\qquad
Y_*(Z_0\,1_{J\in p^N}qB_0)=0.
\tag{15}
$$
定义 R791 的整个首矩来源与其负一行
$$
\mathcal L_N^J=\Omega^{-1}Y_*(t\,1_{J\in p^N}qB_0),\qquad
M_J=\int_{\substack{J\in p^N\\Y\ {\rm unit}}}\frac tYq\,dB_0 .
\tag{16}
$$
$\mathcal L_N^J$ 是原裸 $\mathcal S_{34}$ type5 的完整五维来源，
包含 R791 的两个实际算术幅度与未丢的 primitive 三维块。

令
$$
A(v)=\frac{119+144v}{263}.
$$
将(9)代入(11)，再用(15)，得到来源级而非仅负矩的身份
$$
\boxed{
\Omega^{-1}Y_*(t\,1_{J,E\in p^N}qB_0)
=\lambda^N A(u)\mathcal L_N^J .}
\tag{17}
$$
同理，因为 Z 在(9)不动且 $Z=Z_0-at$，
$$
\boxed{
\Omega^{-1}Y_*(Z\,1_{J,E\in p^N}qB_0)
=-a\lambda^N\mathcal L_N^J,\qquad
Y_*(1_{J,E\in p^N}qB_0)=0.}
\tag{18}
$$
(17)、(18)保任意完整 Y 测试。它们没有使用原 cd-Z 首矩的另一条零，
也没有把 cd 返回权替换成原 q。

$119=7\cdot17$，故 $A(u)\in\mathcal O^\times$。
R791 给同一实际射线子族上所有 N 的 $M_J\ne0$，
以及其完整两算术幅度为单位。因此
$$
\boxed{
\int_{\substack{J,E\in p^N\\Y\ {\rm unit}}}\frac tYq\,dB_0
=\lambda^N A(u)M_J\ne0.}
\tag{19}
$$
这条已识别负一行现在处于原物理 E 深门内部。
它不是原中央 $J'_S$，也不是未切 J 的 E 深首矩。

## 6. 旧帽的准确交集及帽外首矩非零

保持 R773/R783 的原帽与失败深度：
$$
\mathcal H_N=\{Y\ {\rm unit},\ J,Z_0\in p^N,\
                       U\notin p^{N+300}\}.
\tag{20}
$$
在该帽上，(2)中除 $h_0t$ 外的两项都深 N，
所以实际集合恒等式为
$$
\boxed{
\mathcal H_N\cap\{E\in p^N\}
=\mathcal H_N\cap\{t\in p^N\}.}
\tag{21}
$$
这也保 R780 更正后的事实：帽上 t-unit 的 W 近消支在 E-unit，
不能从第三 E 深行相减。

令
$$
M_H=\int_{\mathcal H_N}\frac tYq\,dB_0 .
$$
原 t 单轴对 B0 的完整核心为 $\beta$，而 q 和(20)的全部门独立于 t。
故在同一观察下，
$$
\boxed{
\int_{\mathcal H_N\cap\{E\in p^N\}}\frac tYq\,dB_0
=\beta^N u\,M_H.}
\tag{22}
$$
这里保了原 U 失败，没有以它的总质量代替。

定义完整余域
$$
\mathcal C_N=
\{Y\ {\rm unit},\ J,E\in p^N\}\setminus\mathcal H_N .
$$
它准确由以下两个不交部分组成：
$$
\begin{aligned}
\mathcal C_N^{<}
 &=\{Y\ {\rm unit},\ J,E\in p^N,\ Z_0\notin p^N\},\\
\mathcal C_N^{U}
 &=\{Y\ {\rm unit},\ J,E,Z_0\in p^N,\ U\in p^{N+300}\}.
\end{aligned}
\tag{23}
$$
第一部分中 $Z_0\notin p^N$ 等价于 $t\notin p^N$；
第二部分必有 t 深 N。没有额外加 L-unit、P-unit 或任意 CD 条件。
由(19)、(22)，
$$
\boxed{
\int_{\mathcal C_N}\frac tYq\,dB_0
=\lambda^N A(u)M_J-\beta^Nu M_H .}
\tag{24}
$$

这里不仅有一个渐近比较。按 R791 和 R773 的原规范，写
$$
M_J=\lambda^N\beta^N\mathfrak I_J(u),\qquad
M_H=\lambda^{2N}\beta^N\mathfrak I_H(u).
$$
R773 的帽首矩原写在 $e_0$ 上；因(20)是 $\mathcal T$-不变域，
该篇(A15)准确说明其 t 首矩与 B0 上相同，没有更换来源。
两个 $\mathfrak I$ 都由同一原 type5 五维来源、同一 $\Omega$ 读取；
两条算术幅度均为单位，primitive 块完整保留。
将(24)除以 $\lambda^{2N}\beta^N$，得到
$$
\boxed{
A(u)\mathfrak I_J(u)-\beta^Nu\mathfrak I_H(u).}
\tag{25}
$$
在每条算术线上的第一个系数为单位，第二个属于 $p^N\mathcal O$，
所以其差仍为单位。全部系数属于实际代数域，两个点的共同周期已清楚。
用 R735/R761 的有限 point-factor 分离，严格得到
$$
\boxed{\int_{\mathcal C_N}tY^{-1}q\,dB_0\ne0
\quad\text{对同一好素数子族的全部 }N\in4\mathbf Z_{>0}.}
\tag{26}
$$
(26)没有分别给(23)两个部分非零，也没有将完整余域删除。

固定实际 p 和 $\eta(p)$，令 R791 的
$v_p^+=v_p(\mathfrak I_J(0))<\infty$。
R773/R791 两个来源都在固定有限 carrier 中按真实代数系数趋向各自
$u=0$ 极限；$\beta^Nu$ 以赋值 N 趋零。因此对充分大的原 N，
$$
v_p\!\left(\int_{\mathcal C_N}tY^{-1}q\,dB_0\right)=v_p^+.
\tag{27}
$$
这没有将点惯性投影施加到一个无限 P 分母或无限对数级数。

## 7. 原 Z 偶环带上的全部首矩

记 $\mathcal J\mathcal E_N=\{J,E\in p^N\}$。
Z 的完整偶深核固定 Y、J、E、q，并在原三态上保持同一状态。
因此，对任意偶 $j\ge0$，
$$
\rho_{B_0}|_{\mathcal J\mathcal E_N,\ Z\in p^j}
=\lambda^j(P_{Z,\kappa^j})_*
       (\rho_{B_0}|_{\mathcal J\mathcal E_N}).
\tag{28}
$$
在 $\mathcal V$ 中有
$$
t=-\frac{119}{263a}Z+\frac{144}{263h_0}E_{\mathcal V}.
$$
第二项被 Z 缩放固定。结合(17)、(18)及
$Y_*(E_{\mathcal V}1_{\mathcal J\mathcal E_N}qB_0)
=h_0\lambda^N u\,\Omega\mathcal L_N^J$，得到
$$
\boxed{
\begin{aligned}
\Omega^{-1}Y_*(t\,1_{\mathcal J\mathcal E_N,Z\in p^j}qB_0)
 &=\frac{\lambda^{N+j}}{263}
       (119\kappa^j+144u)\mathcal L_N^J,\\
\Omega^{-1}Y_*(Z\,1_{\mathcal J\mathcal E_N,Z\in p^j}qB_0)
 &=-a\lambda^{N+j}\kappa^j\mathcal L_N^J .
\end{aligned}}
\tag{29}
$$
这是全部五坐标及任意 Y 测试的真实公式，不只一个抽样正矩。

若 $0\le j\le N$，在 $\mathcal J\mathcal E_N$ 上
$$
Z\in p^j\Longleftrightarrow t\in p^j
                    \Longleftrightarrow Z_0\in p^j .
\tag{30}
$$
证明是 $\Delta\in p^N$ 及(9)的可逆两线性式。
所以(29)在这个范围也给原 t 深条带，没有改变物理门。

取真实两层环带
$$
\mathcal A_{N,j}=\{J,E\in p^N,\ v_p(Z)\in\{j,j+1\}\},
\quad j\ge0\text{ 偶}.
$$
相减(29)给
$$
\boxed{
\begin{aligned}
\Omega^{-1}Y_*(t\,1_{\mathcal A_{N,j}}qB_0)
={}&\frac{\lambda^{N+j}}{263}
 \bigl[119\kappa^j(1-\lambda^2\kappa^2)
       +144u(1-\lambda^2)\bigr]\mathcal L_N^J,\\
\Omega^{-1}Y_*(Z\,1_{\mathcal A_{N,j}}qB_0)
={}&-a\lambda^{N+j}\kappa^j(1-\lambda^2\kappa^2)
                                               \mathcal L_N^J .
\end{aligned}}
\tag{31}
$$
第二行的负一矩对每个 j 非零。
第一行在偶 $j\le N-2$ 时括号赋值恰 j；
在 $j\ge N+2$ 时赋值恰 N，使用原 $1-\lambda^2$ 单位。
$j=N$ 的完整括号保留，不猜它的赋值。
对 $2\le j\le N-2$，(30)还给实际 t/Z0 的同一两层环带；
在 Y-unit 上，P、W 及原 $V_Y=36Y-(17-3\omega)W$ 全为单位。

## 8. 同一实际 W 中央行与完整外部

置
$$
f_w(x)=1_{x\ {\rm unit}}\langle x\rangle^{d_pw},\qquad d_p=p-1,
$$
$$
G_N(z,w)=\int_{\mathcal J\mathcal E_N}
                       f_w(b_YY+zZ)\,q\,dB_0 .
$$
$z\in p\mathcal O$ 时 unit 条件准确为 Y-unit。
由(18)，其整条 Y 来源为零，故
$G_N(0,w)=0$、$G_N(z,0)=0$。
完整对数导数为
$$
\partial_wG_N(z,0)
=d_p\sum_{r\ge1}\frac{(-1)^{r+1}z^r}{r b_Y^r}
 \int_{\substack{\mathcal J\mathcal E_N\\Y\ {\rm unit}}}
                   Z^rY^{-r}q\,dB_0 .
\tag{32}
$$
只用(18)读取第一项，全部其它负矩和 log 分母保在(32)：
$$
\boxed{
\partial_wG_N(\kappa^j,0)
=-\frac{d_pa}{b_Y}\lambda^N\kappa^jM_J+p^{2j}\mathcal O,
\qquad j\ge2\text{ 偶}.}
\tag{33}
$$
原 q 整有界，且对 $r\ge2$ 有
$rj-v_p(r)\ge2j$，所以显示尾界包括整个无穷级数。
这里不对(32)施加 point-only 投影。

原 W 未归一观察在真实
$\{J,E\in p^N,\ Z\in p^j\}$ 上的 Mellin 行，恰为
$$
\boxed{
\mathscr I_{N,j}(w)
=\int_{\mathcal J\mathcal E_N,Z\in p^j}f_w(W)\,q\,dB_0
=\lambda^jG_N(\kappa^j,w).}
\tag{34}
$$
对两层 Z 环带则是
$\lambda^j[G_N(\kappa^j,w)-\lambda^2G_N(\kappa^{j+2},w)]$。
其首项由(31)第二行准确给出。
当 $j>v_p(M_J)$ 时，(34)及该环带行的中央导数都非零，
赋值恰为 $j+v_p(M_J)$。
固定 p 后，对足够大的 N，赋值为 $j+v_p^+$。

现在在**原同一个物理 E 深门**中取完整补域
$$
\mathscr X_{N,j}(w)
=\int_{\{E\in p^N\}\setminus
               \{J\in p^N,\ Z\in p^j\}}f_w(W)\,q\,dB_0 .
$$
R702/R734 的整个 W 来源给
$$
\boxed{
\mathscr X_{N,j}(w)+\mathscr I_{N,j}(w)
=\frac{\lambda^{2N}6\delta}{c_B}J_T(w).}
\tag{35}
$$
这个补域包含全部 J 浅和 J 深/Z 浅部分；
原 W unit 仍在 f 中，不被换成一个不同的单位观察。

因此若原 $J_T'(0)=0$，所付结论准确是
$$
\boxed{
\mathscr X_{N,j}'(0)=-\mathscr I_{N,j}'(0),\qquad
v_p(\mathscr X_{N,j}'(0))=j+v_p(M_J)
}
\tag{36}
$$
于上述非零范围，而不是令(34)为零。
原第三 E 深行、R780/R784 的 E 浅 CM 行及所有不同逆观察继续保留。
(35)也没有把两个独立的 R791 第一负矩升级成全对数级数独立。

## 9. 本篇的有限接口与范围

本篇完成三项相连的原来源结论：

1. (8)是整个原三态、同 q 的 E_V 偶核；(9)–(13)给物理 E 截距、
   全 Y/W 两输出及所有附门的准确转置。
2. (17)–(26)将已识别的 J 首矩送进真正 E 深门，并在同一原帽/U
   分割下证明完整帽外首矩非零；没有借裸负矩跳过条件来源。
3. (29)–(36)给原 Z/t 环带的有限五维首矩、实际 W 中央首项及全部补偿。

所有计算是已付完整来源恒等式之间的代数推导，没有新增数值采样、
输出证书、射线或未执行的 public-run 声明。
本篇依赖的实际非零幅度和整逆，正是 R773/R791 已发表的公开运行；
无需再次运行这些 producer。

最小仍未消掉的原中央补项明确为(35)的 $\mathscr X_{N,j}$，
以及在附原帽/U、CD 或 CM 词观察后由(9)、(12)逐项产生的对应补项。
既有 $J'_S=J'_T=J'_U=0$ 没有单独赋这些项零。
主目标仍须从同域词或另一条已识别全来源取得独立约束。

## 依赖

- [R692](R692-original-four-axis-three-state-and-arithmetic-unit-cuts.md)：原 Y/Z/W/V 的完整三态及物理反射。
- [R702](R702-forty-five-neutral-tests-and-complete-three-state-arithmetic-gate.md)：同 E 深门的全三态算术来源。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：本文未改的最终 q 和全部代数系数。
- [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)、[R761](R761-primitive-type-five-ninth-order-characters-and-point-fields.md)：完整负一 point-factor 与不同有限角色的分离。
- [R773](R773-native-common-hat-domain-and-five-conditional-moment-return.md)：原帽、U 失败、完整五条件矩及实际非零幅度。
- [R780](R780-original-third-central-b-state-and-true-w-deep-return.md)：修正后的物理 E 深浅范围。
- [R785](R785-original-three-state-even-frames-and-exact-e-gate.md)：原三维偶核及 E 的固定 J 截距。
- [R786](R786-original-j-depth-three-output-and-native-e-exteriors.md)：同 q 的完整 J 来源。
- [R791](R791-original-j-depth-negative-moments-and-two-e-sectors.md)：真实 J 负一行、两幅度单位及固定 carrier 的赋值。
