# R988 — level12 模 K3 的实际 Chow 双逆与原 λ 的新 CM 图循环输入

**状态：已证明。** 本文给出一个新的、固定于系数素数之前的循环来源。
实际的 level12 椭圆模曲面与 $E_0^2$ 之间存在定义于 $K$ 的
双向 Chow 对应；它们在超越动机上严格互逆，而不只在上同调上互逆。
张量第三个 $E_0$ 后，最高三次投影、原三个十八阶有限角色及
各个素数的 Abel–Jacobi 图全部相容。

这里没有把 R854 的旧 weight4 辅助模形式上的规范循环运输过来，
没有把新循环叫作 R831 的原端点循环，也没有证明新循环的 AJ 非零。
新来源的价值是：模曲面、CM 纤维和图循环都真实存在，
从该来源到 $E_0^3$ 的 Chow 运输与逆已经付清，
故可以直接研究这一新的具体循环，不必再假设一般 CM Chow 比较。

**后续 R990：本篇(35)–(38)新定义的 CM17 图族，在取到原 H 的 trace 后已证明为有理 Chow 零。上面的 Chow 双逆和所有 AJ 交换图保持有效；该特定新族不再作为非零候选。实际循环、局部 Artin 元及全2处 Hom 的证明见 [R990](R990-level-twelve-cm-graph-trace-vanishing-at-two.md)。**

会话：Astra-rank2-Sha-0b097461-20261127。

## 1. 实际模曲面、正确的 SL₂ 提升及全部 Néron–Severi 指数

沿 R806 固定
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,
\quad E_0:y^2=x^3+1,\quad \delta=1+2\omega.
$$
定义
$$
\Gamma=\Gamma_0(12)\cap\Gamma_1(3)
       =\Gamma_0(12)\cap\Gamma_1(6)\subset\mathrm{SL}_2(\mathbf Z).
\tag{1}
$$
第二个等号因为 $12\mid c$、$ad-bc=1$ 迫 $a,d$ 为奇数，
而 $a,d\equiv1\pmod3$ 随即给 $a,d\equiv1\pmod6$。
这里不用含 $-I$ 的整个 $\Gamma_0(12)$ 作通用椭圆族。

令 $S/\mathbf Q$ 为此通用族的光滑极小紧化。
Livné–Yui [LY, Proposition4、Table2 的第7项、§4] 和
Top–Yui [TY, §2.3.2] 给出其实际模型；可分别使用
$$
y^2+(t^2+1)xy-t^2(t^2-1)y=x^3-t^2(t^2-1)x^2
\tag{2}
$$
或下列双有理模型：
$$
(x+y)(x+1)(y+1)+(1-s^2)xy=0.
\tag{3}
$$
(2) 的 $t$ 与 (3) 的 $s$ 是各自的参数，不在此未经换元相认。
族从 $X_1(6)$ 拉回，保留指定的六阶截面。
六个奇异纤维的完整类型是
$$
I_{12},\ I_4,\ I_3,\ I_3,\ I_1,\ I_1.
\tag{4}
$$
其 Euler 数为24，基曲线是 $\mathbf P^1$，因而 $S$ 是 K3 曲面。
平凡格由零截面、纤维及不交零截面的纤维分量生成；其秩为
$$
2+(12-1)+(4-1)+2(3-1)=20.
$$
K3 的 Picard 数至多20，故
$$
\rho(S_{\overline K})=20,\qquad
\operatorname{rank}\mathrm{MW}(S_{\overline K}/\mathbf P^1)=0.
\tag{5}
$$

为不漏掉平凡格的有限指数，直接算几何挠截面。
在通用族的挠局部系统 $(\mathbf Q/\mathbf Z)^2$ 上，
几何挠截面恰为 $\Gamma$ 不变量。
群中的三个实际矩阵
$$
\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
\begin{pmatrix}1&0\\12&1\end{pmatrix},\quad
\begin{pmatrix}7&4\\12&7\end{pmatrix}
\tag{6}
$$
依次迫不变量为 $(a,0)$、$12a=0$、$6a=0$。
反过来，由(1)可见每个 $(a,0)$、$6a=0$ 都被整个 $\Gamma$ 固定。
故几何挠截面群准确为 $\mathbf Z/6\mathbf Z$。
Shioda–Tate 的平凡格商为 Mordell–Weil 群，因此
$$
[\mathrm{NS}(S_{\overline K}):\mathrm{Triv}(S)]=6.
\tag{7}
$$
平凡格的判别式是
$$
-12\cdot4\cdot3\cdot3=-432,
$$
于是
$$
\operatorname{disc}\mathrm{NS}(S_{\overline K})=-12,
\qquad \det T(S)=12.
\tag{8}
$$
特别是其 CM 域准确为 $\mathbf Q(\sqrt{-3})=K$。
下文只需(8)的平方类；并未把平凡格误称为整个整 NS 格。

## 2. 超越二次表示是原 ψ₀²，不遗漏有限坏位

由 [LY, §2、§4]，$H^2_{\rm tr}(S)$ 的模形式是
$$
f_{12}(z)=\eta(2z)^3\eta(6z)^3
\in S_3(\Gamma_0(12),\chi_{-3}).
\tag{9}
$$
[LY, Proposition10(1),(3)，第7项] 识别其 Hecke 角色：
它是在 $K$ 上 infinity type 为 $(-2,0)$、导子恰为 $(2)$
的唯一角色。这里使用该命题的角色识别，
不使用预印本中 Fourier 系数显示式的排字约定。

原 $\psi_0$ 的导子为 $(2\delta)$。
其二处的三次单位角色平方后仍非平凡，三处的二次单位角色平方后平凡，
所以 $\psi_0^2$ 的导子恰为 $(2)$。
它的 infinity type 与(9)相同。
类数为1及全局单位的相容性给该角色的唯一性，故
$$
f_{12}=\theta_{\psi_0^2}.
\tag{10}
$$
这是包含坏处有限角色的等式，而非只认无穷型或 CM 域。
也可对照 Li–Long–Tu [LLT, Theorem1.2] 的同一 theta 形式识别。
该文的 Fermat 曲线 $u^3+v^3=1/4$ 经
$X=3/(u+v)$、$Y=9(u-v)/(u+v)$ 成为 $Y^2=X^3-27$；
它由原 $E_0$ 的标准三同源
$$
(x,y)\longmapsto
\left(\frac{x^3+4}{x^2},\frac{y(x^3-8)}{x^3}\right)
\tag{11}
$$
得到，故这里没有换一条具有未付有限扭曲的 CM 角色。

因此，在与 R806 相同的 CM 嵌入下，对每个系数素数 $\ell$，
$$
H^2_{\rm tr}(S_{\overline K},\mathbf Q_\ell)
\otimes K_\ell
\simeq \psi_{0,\ell}^{2}\oplus\bar\psi_{0,\ell}^{2}.
\tag{12}
$$
这也是 $E_0^2$ 的最高二次分量。
两角色在任何有限扩域后仍不同：它们的比值有非零的两嵌入
Hodge–Tate 权差，因而不可能成为有限阶角色。
本处只有纯表示的识别；下三节另外构造实际 Chow 双逆。

## 3. 真实二重覆盖、两条同源与有限域上的 Chow 双逆

先把所有对应放在有限 Galois 扩张 $L/K$ 上。
由 Shioda–Inose [SI, pp.119–136]，(8)给实际图
$$
S\dashrightarrow Y=\operatorname{Km}(E_1\times E_2)
\dashleftarrow E_1\times E_2,
\tag{13}
$$
两条有理映射的次数均为2；左图是 Nikulin 商，右图是 $[-1]$ 商。
$E_1,E_2$ 是 CM 域同为 $K$ 的两条椭圆曲线。
它们各自的整 CM order 可以不同，不能由(8)直接声称二者都等于 $E_0$。
但其复格均为 $K$ 中的格，适当相乘后互相包含，故分别存在同源
$$
u_i:E_0\longrightarrow E_i\quad(i=1,2),
\qquad d_i=\deg u_i>0.
\tag{14}
$$
将 $L$ 扩大一次即可同时定义(13)、(14)、各解消、所需 NS 除子及 CM 作用。
Shioda–Inose 的格构造给的是代数曲面和代数映射。
若使用其复同构，固定图的 Hilbert 多项式后，Isom 概形中的复点可在
$\overline{\mathbf Q}$ 上取得，故仍只需有限扩域。

以下记 $t_2(V)$ 为曲面的超越 Chow 动机，系数取 $\mathbf Q$。
可用一个度1零循环及 NS 交矩阵的逆构造其 projector；
对 $S$，(5)的20条平凡格除子已张满 $\mathrm{NS}_{\mathbf Q}$，
因此无需假设平凡格整饱和。
解消新增的例外除子属于 Tate 动机，不进入 $t_2$。

记(13)两映射为 $q_S:S\dashrightarrow Y$、
$q_A:A=E_1\times E_2\dashrightarrow Y$。
其图在解消上定义 $q_*,q^*$；以下等式均已夹上 $t_2$ projector。
对次数2商，图复合给
$$
q_{S,*}q_S^*=2,\qquad q_S^*q_{S,*}=1+\iota,
\tag{15}
$$
其中 $\iota$ 是 Nikulin involution。
这里不能只用 $\iota$ 在 $H^2_{\rm tr}$ 上平凡。
本 $S$ 的 $\rho=20$，Pedrini [Pe, Theorem2 及其证明、Theorem3]
给出 $\iota=1$ 在 $t_2(S)$ 上成立，并给出 $h(S)$ 的 Kimura 有限维性。
该证明利用奇异 K3 的 Shioda–Inose 格和 symplectic involution
对零循环的作用，结论是在 Chow 范畴。
故(15)的第二式也准确为2。

类似地，$[-1]$ 在阿贝尔曲面的 $h^2$，从而在 $t_2(A)$ 上恒等，
故
$$
q_{A,*}q_A^*=q_A^*q_{A,*}=2
\tag{16}
$$
在对应的两个超越动机上成立；这亦是 [KMP, Remark7.6.13] 的 Kummer 对应。
于是
$$
C=\tfrac12q_A^*q_{S,*}:t_2(S)\longrightarrow t_2(A),
\quad D=\tfrac12q_S^*q_{A,*}:t_2(A)\longrightarrow t_2(S)
\tag{17}
$$
严格满足 $DC=1$、$CD=1$。

置 $u=u_1\times u_2$、$d=d_1d_2$。
椭圆曲线 $h^1$ 上的同源及对偶同源给实际 Chow 逆，
张量后得到
$$
u^*:t_2(A)\xrightarrow{\sim}t_2(E_0^2),
\qquad (u^*)^{-1}=d^{-1}u_*.
\tag{18}
$$
这里的 $d^{-1}$ 保留，不把(14)未计算的次数说成1。
合成(17),(18)得固定的
$$
U_L=\tfrac12u^*q_A^*q_{S,*},\qquad
V_L=\tfrac1{2d}q_S^*q_{A,*}u_*.
\tag{19}
$$
它们在 $L$ 上是严格 Chow 双逆。

有关从复数域回到 $L$ 的等式也无需假设新的注入猜想。
任何所用的有理等价只含有限个子簇与有理函数，先 spread 到一个有限型
$\overline{\mathbf Q}$ 代数，再在非空开集取闭点即可下降到
$\overline{\mathbf Q}$；随后所有有限数据定义于某有限扩域。
对有限扩域，Chow 的 restriction/corestriction 复合为扩域次数，
在 $\mathbf Q$ 系数下 restriction 是单射。
故上述已定义于 $L$ 的 projector 与图等式确在 $L$ 的 Chow 群内成立。

## 4. 降到 K；一个明确三项式修正给 Chow 逆

令 $M=t_2(S)$、$N=t_2(E_0^2)$。
这两个动机可取定义于 $K$ 的 self-dual projector。
对 $S$，NS projector 的交矩阵表达式在更换 NS 基时不变。
又 $\mathrm{Pic}^0(S)=0$，因此 NS 基的 Galois 变换关系已是
有理等价关系；取 trace 后其下降仍为同一个幂等 projector。

目标 $N$ 还可用原 CM 自同构明确写出。
设 $\pi_1=\Delta_{E_0}-[0]\times E_0-E_0\times[0]$，
$R_2=[\omega]\times[\omega]$，则
$$
P_2=(\pi_1\otimes\pi_1)\frac{2-R_2-R_2^2}{3}
\tag{20}
$$
是 $N$ 的 projector。
在 $h^1\otimes h^1$ 中，它保留 $(2,0),(0,2)$，
杀掉两个 $(1,1)$ CM 除子方向。
后者由实际对角及 CM 图给出，故这是 Chow projector。
更精确地，交矩阵构成的两个 Lefschetz projector 包含在 $R_2$ 不变量中；
二者的余 projector 同调为零。它是阿贝尔有限维动机的直和因子，
Kimura nilpotence 应用于其幂等恒等映射迫它为零。
所以这里的 $P_2$ 确可作为 $t_2(E_0^2)$ 的 refined Chow projector，
并非只在 realization 中作此命名。

固定一个好辅助 $\ell$ 来检查图的 Galois 下降。
由(12)，$U_{L,\ell}$ 只能将 $\psi_0^2$ 线送到同名线、
将 $\bar\psi_0^2$ 线送到同名线：不同角色在 $G_L$ 上亦不同。
所以 $U_{L,\ell}$ 不仅与 $G_L$，也与整个 $G_K$ 交换。
$V_{L,\ell}$ 同理。
这一点用的是(10)的完整角色识别，不能仅用两边同为 CM。

置 $n=[L:K]$，在 $K$ 上定义归一化图的 trace
$$
A=n^{-1}\operatorname{Cor}_{L/K}U_L:M\longrightarrow N,
\quad B=n^{-1}\operatorname{Cor}_{L/K}V_L:N\longrightarrow M.
\tag{21}
$$
在任何 Weil 上同调中，$A,B$ 互逆。
此时尚不能直接写 $BA=AB=1$ 在 Chow 中；以下付这个差别。

**引理。** 若 Chow 动机 $Q$ 是 Kimura 有限维，
其 realization 集中在一个偶数次数且总维数为2，则每个同调平凡的
$e\in\operatorname{End}(Q)$ 满足 $e^2=0$。

**证明。** $\bigwedge^3Q$ 是有限维动机的直和因子，realization 为零。
Kimura 的 nilpotence theorem [Ki, Proposition7.5；亦见§7.3]
应用于其恒等映射，给 $\bigwedge^3Q=0$。
因此 $Q^{\otimes3}$ 上的三阶反对称器为零。
将它与 $1\otimes e\otimes e$ 复合，再对后两因子取范畴迹，
六个置换逐项给
$$
0=(\operatorname{tr}e)^2\,1-\operatorname{tr}(e^2)\,1
  -2\operatorname{tr}(e)\,e+2e^2.
\tag{22}
$$
Chow 范畴的这些迹属于 $\mathbf Q$，其 realization 就是通常的迹。
同调平凡给 $\operatorname{tr}e=\operatorname{tr}(e^2)=0$，
所以(22)给 $e^2=0$。证毕。

引理适用于 $M,N$：前者由 [Pe, Theorem2]，后者为阿贝尔型动机。
相应有限维性及 $\bigwedge^3=0$ 也按§3的有限等价/trace 论证下降到 $K$。
故
$$
(1_M-BA)^2=0,\qquad (1_N-AB)^2=0.
\tag{23}
$$
定义真正的 Chow 逆为这个明确的有限组合：
$$
\boxed{A^{-1}=2B-BAB.}
\tag{24}
$$
直接算
$$
(2B-BAB)A=2BA-(BA)^2=1_M,
$$
$$
A(2B-BAB)=2AB-(AB)^2=1_N.
\tag{25}
$$
于是
$$
\boxed{t_2(S)_K\simeq t_2(E_0^2)_K\quad\text{在有理 Chow 范畴中}.}
\tag{26}
$$
本证明没有把一般 pure CM realization 的忠实性升级为 mixed/Chow 忠实性。
使用的是实际有限图，且其同调误差由已知有限维性和(22)给显式修正。
所有分母来自固定的 $2,3,d,n$、NS 交矩阵等有限数据；
清除它们只给一个固定整数 $D$，并不声称 $D$ 的素因子已全部算出。
在有理 Chow 和有理 AJ 中(26)对所有 $\ell$ 有效；
若要求整格同构，须保留 $\ell\mid D$ 的有限例外。

## 5. 张量第三因子后，原最高三次及三 finite η 原样通过

令
$$
\mathcal A=A\otimes\pi_1,
\qquad \mathcal A^{-1}=(2B-BAB)\otimes\pi_1.
\tag{27}
$$
它们是 $M\otimes h^1(E_0)$ 与 $N\otimes h^1(E_0)$ 的严格 Chow 双逆，
由 codimension3 的外积图表示。
在 $E_0^3$ 上取原最高三次 projector
$$
\Pi_3=\pi_1^{\otimes3}\frac{1+R_3+R_3^2}{3},
\qquad R_3=[\omega]\times[\omega]\times[\omega].
\tag{28}
$$
它恰保留 $(3,0),(0,3)$，且其像包含于 $N\otimes h^1(E_0)$。
故在 $S\times E_0$ 上
$$
\Pi_S=\mathcal A^{-1}\Pi_3\mathcal A
\tag{29}
$$
是一个真正的 Chow projector；其幂等性由(25)逐项给出。
不需要假定 $S$ 上存在未构造的阶3几何自同构。

若需原单条 CM 角色而不是两条共轭之和，令
$$
e_+=\pi_1\frac{[\omega]-\omega^2}{\omega-\omega^2},
\quad e_- =\pi_1-e_+,
\quad \Pi_3^+=e_+^{\otimes3}.
\tag{30}
$$
系数扩到 $K$ 后，这些都是定义于 $K$ 的实际对应。
固定与 R806 相同的 CM 嵌入，$\Pi_3^+$ 实现 $\psi_0^3$；
其源 projector 为 $\Pi_S^+=\mathcal A^{-1}\Pi_3^+\mathcal A$。

保持 R806 的固定扩张 $H/K$、$[H:K]=18$ 及三个角色
$\eta_j$，$j=4,10,16$。在 $E=K(\zeta_{18})$ 系数下定义
$$
e_{\eta_j}=\frac1{18}\sum_{\sigma\in\operatorname{Gal}(H/K)}
                      \eta_j(\sigma)^{-1}\sigma.
\tag{31}
$$
本处 $e_{\eta_j}$ 选择满足 $\sigma z=\eta_j(\sigma)z$ 的循环。
由 restriction/Shapiro，AJ 的此 eigenspace 对应
$$
H^1\left(K,
  \psi_{0,\ell}^{3}\eta_j^{-1}(2)\right),
\tag{32}
$$
即 R814 的原 $\lambda_j=\eta_j^{-1}\psi_0^3$、再作原 AJ 的 Tate twist。
这样解释了有限角色的逆号，不能把循环 eigenspace 与系数扭曲的号直接相认。

因为(27)定义于 $K$，它与(31)在 Chow 群中严格交换。
所以三角色的全部局部数据继续是 R806 的原数据：
$$
\mathfrak f_{\eta_j}=(34),\quad e_2(H/K)=3,\quad e_{17}(H/K)=18,
\quad e_3(H/K)=1,\quad\eta_j(\delta)=-1,
\tag{33}
$$
以及
$$
\mathfrak f_{\lambda_j}=(34\delta),\quad
\eta_j^3=\psi_{17}/\psi_0,\quad \eta_j^9=\kappa_{17}.
\tag{34}
$$
这里的新 level12 仅属于辅助模曲面；它没有删除原 $2,3,17$ 的角色，
也没有把原 level10404 的三次表示改成 level12 的二次表示。

## 6. 一个真实有限 CM 图循环族与全 AJ 交换

下面给可直接继续研究的新对象，而不只留下抽象动机名称。
固定一个几何循环子群 $C_{17}\subset E_0[17]$，令
$$
\varphi:E_0\longrightarrow E'=E_0/C_{17}.
\tag{35}
$$
固定兼容的 $P_6\in E_0[6]$ 和循环 $C_{12}\subset E_0[12]$，
其中 $P_6$ 生成 $C_{12}$ 的六阶子群。
因为 $(17,12)=1$，其像给 $E'$ 的同样 level 结构。
它对应 $X_\Gamma$ 的一个非 cusp CM 点 $t_\varphi$，
实际纤维 $S_{t_\varphi}$ 与带此 level 结构的 $E'$ 同构。
取一次有限 Galois 扩张 $M_0/K$，包含 $H$ 并定义所有这些数据。
于是有真实曲线
$$
G_\varphi=\{(\varphi(Q),Q):Q\in E_0\}
       \subset S_{t_\varphi}\times E_0\subset S\times E_0.
\tag{36}
$$
$S\times E_0$ 是三维，故(36)是 codimension2 循环。
先施加 $\pi^S_{\rm tr}\otimes\pi_1$；该 projector 的 realization
只在总次数3，因此杀掉循环的次数4 cycle class。
所以
$$
\Delta_\varphi=
(\pi^S_{\rm tr}\otimes\pi_1)_*[G_\varphi]
\in\mathrm{CH}^2((S\times E_0)_{M_0})_{\rm hom,\mathbf Q}.
\tag{37}
$$
定义固定的新来源
$$
Z^S_j=e_{\eta_j}\,\operatorname{Cor}_{M_0/H}
                     (\Pi_S^+\Delta_\varphi),
\qquad Z^E_j=\mathcal A_*Z^S_j.
\tag{38}
$$
所有选择先于 $\ell$ 固定；(38)允许某个角色投影或 trace 为零。
本文不以存在图循环代替其非零性。
也可把(35)的全部18个循环子群及兼容 level 选择保成一个固定有限族，
逐个使用(38)，不改变下面的结论。

严格 Chow 双逆给
$$
Z^S_j=\mathcal A^{-1}_*Z^E_j.
\tag{39}
$$
对每个 $\ell$，所有箭头由实际代数对应给出，因而有完整交换图
$$
\begin{array}{ccc}
\mathrm{CH}^2((S\times E_0)_H)_{\rm hom,E}^{\Pi_S^+,\eta_j}
 &\xrightarrow{\ \mathcal A_*\ }&
\mathrm{CH}^2((E_0^3)_H)_{\rm hom,E}^{\Pi_3^+,\eta_j}\\
\operatorname{AJ}_\ell\downarrow&&\downarrow\operatorname{AJ}_\ell\\
H^1(H,\Pi_S^+H^3_{\rm et}((S\times E_0)_{\overline K},E_\ell)(2))^{\eta_j}
 &\xrightarrow{\ \mathcal A_\ell\ }&
H^1(H,\Pi_3^+H^3_{\rm et}((E_0^3)_{\overline K},E_\ell)(2))^{\eta_j}.
\end{array}
\tag{40}
$$
两条横箭头都有(27)给出的实际逆；trace、finite projector、
restriction 及(32)的下降与此图相容。
因此对同一 $j$、同一 $\ell$，
$$
\operatorname{AJ}_\ell(Z^S_j)\ne0
\quad\Longleftrightarrow\quad
\operatorname{AJ}_\ell(Z^E_j)\ne0.
\tag{41}
$$
在普通好素数处，$D_{\rm dR}$、$D_{\rm cris}$、ordinary CM 直线及
Bloch–Kato 局部条件也由同一表示同构运输。
若要求指定微分下的数值对数或整 Euler 因子，还须计算(27)的固定标量；
本文没有把它省成1。

## 7. 付清的门与下一实际非零门

(26)和(40)给的是可作用于混合循环的真实代数双逆。
这是对新 $S\times E_0$ 来源的完成结论，
不需要 Beilinson、一般 Bloch–Kato 注入或 mixed CM realization 的猜想。

但是它不蕴含“任一 $\ell$ 非零则其余 $\ell$ 非零”。
即使源与目标 Chow 动机同构，AJ 的 kernel 仍可能依赖 $\ell$；
这里没有对这个 kernel 作无依据的断言。
下一具体门是(38)的角色 trace、局部 test vector、实际 AJ 值及跨素数非零。
标准 Heegner 假设不能不加检查地使用：$2$ 在 $K$ 惰性，
不存在 $\mathcal O_K$-稳定的循环四阶子群，故 level12 CM 点并非
通常 cyclic12 ideal 数据。
不过(35)–(37)的通用族点与图本身没有这个限制。
BDP [BDP, §5.2、Proposition5.2.1] 在另一 CM 域给过用非标准
level CM 点直接算 AJ 的做法；是否得到本(38)的非零须另作实际推导。

本篇没有动当前唯一原几何 v8 的任何生产源、参数或数学门，
没有发新计算作业，也没有把其尚未完成的四交/厚 Norm/shadow 记为通过。

## 8. 依赖与出处

- [LY] Ron Livné, Noriko Yui, *The modularity of certain non-rigid Calabi–Yau threefolds*,
  Journal of Mathematics of Kyoto University 45 (2005), 645–665；
  [arXiv:math/0304497v2](https://arxiv.org/abs/math/0304497v2)。
  本文引用预印本 Proposition4、Table2 第7项、§4、Proposition10(1),(3)；
  期刊采用分节编号。
- [TY] Jaap Top, Noriko Yui, *Explicit equations of some elliptic modular surfaces*,
  Rocky Mountain Journal of Mathematics 37 (2007), 663–687，§2.3.2；
  [作者全文](https://www.math.rug.nl/~top/top-yu.pdf)。
- [SI] Tetsuji Shioda, Hiroshi Inose, *On singular K3 surfaces*,
  in *Complex Analysis and Algebraic Geometry* (1977), 119–136；
  [出版记录](https://doi.org/10.1017/CBO9780511569197.010)。
- [Pe] Claudio Pedrini, *On the finite dimensionality of a K3 surface*,
  Manuscripta Mathematica 138 (2012), 59–72，Theorems2,3 及 Theorem2 的证明；
  [作者预印本](https://arxiv.org/abs/1106.1115)。
- [Ki] Shun-Ichi Kimura, *Chow groups are finite dimensional, in some sense*,
  Mathematische Annalen 331 (2005), 173–201，§7、Proposition7.5；
  [DOI](https://doi.org/10.1007/s00208-004-0577-3)。
- [KMP] Bruno Kahn, Jacob Murre, Claudio Pedrini,
  *On the transcendental part of the motive of a surface*,
  in *Algebraic Cycles and Motives*, Vol.2, LMS Lecture Note Series344 (2007), 143–202，
  refined surface projector、birational invariance 与 Remark7.6.13 的 Kummer 对应；
  [作者全文](https://webusers.imj-prg.fr/~bruno.kahn/preprints/surfaces4.pdf)。
- [LLT] Wen-Ching Winnie Li, Ling Long, Fang-Ting Tu,
  *Computing special L-values of certain modular forms with complex multiplication*,
  SIGMA14 (2018),090，Theorem1.2；[全文](https://emis.de/ft/24022)。
- [BDP] Massimo Bertolini, Henri Darmon, Kartik Prasanna,
  *p-adic L-functions and the coniveau filtration on Chow groups*,
  with an appendix by Brian Conrad, J. reine angew. Math.731 (2017)，§5.2；
  [作者全文](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP5-hl.pdf)。
- 原有限角色、全部 $2,3,17$ 局部数据与 Tate/互反约定见 R806、R811、R814；
  原 $E_0^3$ 最高 projector 与实际 shadow 图见 R859。

本文是代数构造与证明；未把任何本地计算或未执行 helper 当作数学回执。
