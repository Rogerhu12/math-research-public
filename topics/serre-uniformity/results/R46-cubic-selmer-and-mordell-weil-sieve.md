# R46：三次类域的 Selmer 嵌入、指标覆盖与精确 Mordell–Weil 筛

日期：2026-11-12；会话：serre-uniformity-astra-cont/2026-11-12。

**状态：已证明的全局筛。** 本文将 R37 的指定类群字符空间完整嵌入一个三同源 Selmer 群，包括素数 $3$ 和特殊的二进射线分支。R42 的候选三次域由此给出一组处处局部可解的光滑平面三次曲线。某个候选域是否通过有理点这一级筛，等价于其字符是否属于明确的 Mordell–Weil Kummer 像；没有通过的字符给出非零的 $\Sha$ 类。通过该筛仍不保证存在 R19 所需的原始整数指标点，本文也未证明该 Mordell–Weil 交空间对所有参数都为零。

本文只处理 R19 的固定 CM 参考三族；没有将这一 Selmer 嵌入自动推广到 R40 的可变四次参数。

## 1. 固定参数和两个 Mordell 曲线

固定带符号整数 $Z$，满足 $|Z|>1$、$(Z,6)=1$，并固定 R19 的 I、II、III 奇 $X$、III 偶 $X$ 中的一支。令 $c=1$ 对应 I、III，$c=8$ 对应 II，且
$$
d_0=\operatorname{sf}(Z),\qquad
Z=d_0z_0^2,\quad z_0>0,\qquad
F=\mathbb Q(\sqrt{\operatorname{sf}(cZ)}).
$$
保留 R37 对该分支的全部必要参数条件。尤其 $F$ 是真正的二次域；因为 $3\nmid cZ$，还必有 $F\ne\mathbb Q(\sqrt{-3})$。

固定
$$
e\in\{1,5\},\qquad a=cZ^e,
$$
对应素数指数 $p\equiv e\pmod6$。定义
$$
B_a:y^2=x^3+a,\qquad
D_a:V^2=U^3-27a.
\tag{46.1}
$$
使用 R37 的三同源
$$
\phi:B_a\longrightarrow D_a,\qquad
(x,y)\longmapsto
\left(
\frac{x^3+4a}{x^2},
\frac{y(x^3-8a)}{x^3}
\right).
\tag{46.2}
$$
其核为
$$
M_a=B_a[\phi]=\{O,(0,\sqrt a),(0,-\sqrt a)\}
\simeq\mathbb F_3(\chi_F).
\tag{46.3}
$$
对任何特征零域 $K\supseteq\mathbb Q$，记 Kummer 映射为
$$
\delta_K:D_a(K)/\phi B_a(K)\hookrightarrow H^1(K,M_a).
\tag{46.4}
$$

普通分支定义
$$
G_0=\operatorname{Cl}(F)/
\langle[\mathfrak q]:\mathfrak q\mid2Z\rangle,
\qquad
V_0=\operatorname{Hom}(G_0,\mathbb F_3).
\tag{46.5}
$$
射线分支即 III 偶 $X$，定义
$$
G=\operatorname{Cl}_{(2)}(F)/
\langle[\mathfrak q]:\mathfrak q\mid Z\rangle,
\qquad
V_2=\operatorname{Hom}(G,\mathbb F_3).
\tag{46.6}
$$
此时 $Z\equiv5\pmod8$，$F_2/\mathbb Q_2$ 为非分歧二次域。射线惯性在 $G/3G$ 中的像记为 $I_2$；R37 实际解要求相应字符在 $I_2$ 上非零。

以下用 $V$ 统一表示当前分支的 $V_0$ 或 $V_2$，用
$$
v=\dim_{\mathbb F_3}V
$$
表示其维数。它与整数 $e=p\bmod6$ 是不同的记号。

## 2. 主结论

**定理 R46。**

1. 类域论字符给出自然单射（选取核生成元后确定）
   $$
   V\hookrightarrow H^1(\mathbb Q,M_a),
   $$
   并且其像全部位于三同源 Selmer 群：
   $$
   \boxed{V\subseteq\operatorname{Sel}^{\phi}(B_a/\mathbb Q).}
   \tag{46.7}
   $$
   这里的 Selmer 群按全部完成域上的 Kummer 像定义。

2. 令
   $$
   U_e=\delta_{\mathbb Q}\bigl(D_a(\mathbb Q)/\phi B_a(\mathbb Q)\bigr),
   \qquad
   W_e=V\cap U_e,\qquad
   m_e=\dim_{\mathbb F_3}W_e.
   \tag{46.8}
   $$
   则有单射
   $$
   \boxed{
   V/W_e\hookrightarrow\Sha(B_a/\mathbb Q)[\phi].
   }
   \tag{46.9}
   $$
   因而，若 $R_e=\operatorname{rank}D_a(\mathbb Q)
   =\operatorname{rank}B_a(\mathbb Q)$，
   $$
   \boxed{
   m_e\le R_e,\qquad
   \dim_{\mathbb F_3}\Sha(B_a/\mathbb Q)[\phi]
   \ge v-m_e\ge v-R_e.
   }
   \tag{46.10}
   $$
   这不需要整个 $\Sha$ 有限的假设。

3. 每个非零候选字符 $\kappa\in V$（射线分支另要求 $\kappa(I_2)\ne0$）给出 R42 的一个三次域 $L$。令 $I_L$ 为任意整基 $(1,\omega,\eta)$ 对应的三次指标形式，且置
   $$
   J_e=\sqrt{\frac{|Z|^e}{|d_0|}}
   =|Z|^{(e-1)/2}z_0,\qquad
   \mu_e=
   \begin{cases}
   2J_e,&\text{I、II},\\
   J_e,&\text{III}.
   \end{cases}
   \tag{46.11}
   $$
   则
   $$
   D_L\mu_e^2=4a.
   \tag{46.12}
   $$
   光滑射影三次曲线
   $$
   C_{L,e}:\quad I_L(u,v)=\mu_e t^3
   \tag{46.13}
   $$
   在 $\mathbb R$ 及每个 $\mathbb Q_\ell$ 上都有点，并且
   $$
   \boxed{
   C_{L,e}(\mathbb Q)\ne\varnothing
   \iff \kappa\in W_e.
   }
   \tag{46.14}
   $$
   字符 $\kappa$ 和 $-\kappa$ 对应同一个三次域；(46.14) 无定向歧义，因为 Kummer 像对取负封闭。曲线的 Jacobian 为 $B_a$，其迹零元素构造给一个到 $D_a$ 的三次同源覆盖。

4. 普通分支中，能够通过这个有理点筛的候选三次域数恰为
   $$
   \boxed{N_e^{\rm MW}=(3^{m_e}-1)/2.}
   \tag{46.15}
   $$
   射线分支中，若每个 $W_e$ 中的字符都在 $I_2$ 上为零，则 $N_e^{\rm MW}=0$；否则
   $$
   \boxed{N_e^{\rm MW}=3^{m_e-1}.}
   \tag{46.16}
   $$
   实际 R19 解只能来自这些域。

特别地，如果 $R_e=0$，当前固定 $Z$、固定分支、$p\equiv e\pmod6$ 的 R19 解全被排除。但本文没有证明相关 Mordell 曲线总为秩零；“秩零时排除”不是变指数统一排除。

## 3. 类群字符如何进入三同源上同调

由 (46.3)，$G_F$ 在 $M_a$ 上作用平凡，而二次共轭作用为取负。因为 $2$ 在 $\mathbb F_3$ 中可逆，
$$
H^i(\operatorname{Gal}(F/\mathbb Q),M_a)=0
\quad(i>0).
$$
限制及 inflation–restriction 给同构
$$
H^1(\mathbb Q,M_a)
\simeq
\operatorname{Hom}_{\rm cont}(G_F,\mathbb F_3)^{-},
\tag{46.17}
$$
右边的上标表示二次共轭下反不变的字符。

R37 已直接证明，二次共轭在普通类群上取逆；在模 $(2)$ 射线类群上也取逆，因为
$$
\mathfrak a\,\overline{\mathfrak a}=(N\mathfrak a),
\qquad
N\mathfrak a\equiv1\pmod{2\mathcal O_F}
$$
对与 $(2)$ 互素的理想成立。因此 (46.5)、(46.6) 中的每个字符都是 (46.17) 的右边元素。Artin 互反和 (46.17) 给所需单射。

一个非零字符对应次数为 $3$ 的扩张 $H/F$；取负共轭保证 $H/\mathbb Q$ 的群为 $S_3$。三点仿射作用
$$
x\longmapsto\chi_F(\sigma)x+c(\sigma)
\quad(x\in\mathbb F_3)
\tag{46.18}
$$
将相应上同调类实现为一个三元素 étale 集合。它的三次代数就是 $H$ 的非 Galois 三次子域。更换核生成元会将字符乘以 $-1$，不改变这个三次域的同构类。

同样的论证可以在各完成域上使用。特别地，若字符在 $F$ 的所有相关局部 Galois 群上为零，其 $\mathbb Q_\ell$ 上的上同调类也为零：余下群至多为阶 $2$，其一阶上同调为零。

## 4. 一个未分歧 Kummer 引理

下面明确处理 Selmer 局部条件，不把“没有分歧”直接当作“来自局部点”。

**引理 46.1。** 设 $K$ 为非阿基米德局部域，剩余域 $k$ 有限；$\psi:B\to D$ 为椭圆曲线同源，其核 $M$ 在 $K$ 上未分歧。假定 $M$ 的闭包为 Néron 恒等分量 $\mathcal B^0$ 内的有限 étale 群概形 $\mathcal M$。则每个未分歧类
$$
\xi\in H^1_{\rm unr}(K,M)
$$
都属于 $D(K)/\psi B(K)$ 的 Kummer 像。

**证明。** 未分歧类由一个 $\mathcal M$-torsor 定义在整数环 $\mathcal O_K$ 上。将其沿
$\mathcal M\hookrightarrow\mathcal B^0$ 推出，得到一个 $\mathcal B^0$-torsor。它在有限 étale 平凡化后同构于光滑的 $\mathcal B^0$，故本身光滑。特殊纤维是连通光滑代数群 $\mathcal B_k^0$ 的 torsor；有限域上的 Lang 定理使它有 $k$ 点。光滑性和 Hensel 引理将该点提升为 $\mathcal O_K$ 点。

所以原来的类在 $H^1(K,B)$ 中为零。由
$$
0\longrightarrow M\longrightarrow B
\xrightarrow{\psi}D\longrightarrow0
$$
的上同调正合列，这恰说明 $\xi$ 来自 Kummer 像。证毕。

本题用到的连通特殊纤维只有好约化椭圆曲线和加性群。这里的 Lang 消失还可直接说明：加性群上的 Frobenius 减恒等映射是满射多项式；椭圆曲线上的 Frobenius 减恒等为非零同源，亦在代数闭包上满射。这使任意 Frobenius torsor cocycle 成为 coboundary。一般表述见 Milne, *Algebraic Groups* (2017), Theorems 17.96–17.98。

## 5. 全部局部条件的核对

### 5.1 q 整除 Z，及普通分支的素数 2

$V$ 的定义杀掉了每个位于 $Z$ 上方的素理想类，因此相应类域在那里完全分裂。由第 3 节末段，$\kappa|_{G_{\mathbb Q_q}}=0$，自然属于 Kummer 像。

普通分支也杀掉了 $2$ 上方的全部素理想；同样得到 $\kappa_2=0$。这里没有对 $B_a$ 的二进约化类型作额外推断。

### 5.2 其余好素数，除去 3

若 $\ell\nmid6Z$，则 $B_a$ 和 $D_a$ 好约化，$M_a$ 的有限 étale 闭包位于 Néron 恒等分量。R37 的类域在 $\ell$ 处未分歧，故 $\kappa_\ell$ 未分歧。引理 46.1 给出所需 Kummer 条件。

### 5.3 素数 3：同源次数等于剩余特征，仍须证明

因为 $3\nmid a$，
$$
\Delta(B_a)=-432a^2,\qquad
\Delta(D_a)=-432\cdot729a^2,
$$
所以显示短模型的判别式赋值分别为 $3$ 和 $9$。两者都小于 $12$，因此都是 $\mathbb Z_3$ 上的极小模型。

令
$$
\omega_B=\frac{dx}{2y},\qquad
\omega_D=\frac{dU}{2V}.
$$
由 (46.2)，
$$
dU=(1-8a/x^3)\,dx,\qquad
V=y(1-8a/x^3),
$$
因此
$$
\boxed{\phi^*\omega_D=\omega_B.}
\tag{46.19}
$$
这是极小不变微分的等式，而不只是非极小模型之间的形式计算。所以扩张到 Néron 模型后，恒等分量间的同态在恒等元处微分为单位，并由平移在整个恒等分量上 étale。

还需检查核的整闭包。$a$ 为 $3$ 进单位，故 $\sqrt a$ 至多需要非分歧二次扩张；核的三个点
$$
O,\quad(0,\sqrt a),\quad(0,-\sqrt a)
$$
在特殊纤维上互不相同，后两个点的 $y$ 坐标都是单位。模 $3$ 的 Weierstrass 方程只有 $y=0$ 的点可能奇异，故这两个核点均为光滑点。特殊纤维为尖点三次曲线，其光滑部分连通，因而这些点位于 Néron 恒等分量。

这构造了 $\mathcal B^0$ 中一个秩为 $3$ 的有限 étale 核闭包；它与 (46.19) 所给的 étale 同源核一致。并未假定一个未经验证的商整模型。

还可以直接核对特殊纤维同源，避免依赖隐含的类型分类。记 $\bar a\in\mathbb F_3^\times$，在源光滑加性群上用坐标
$$
s=(x+\bar a)/y
$$
并令 $O\mapsto0$，在目标上用 $u=U/V$、$O\mapsto0$。由
$y^2=(x+\bar a)^3$ 及 (46.2) 的模 $3$ 约化，得到
$$
u=s-\bar a\,s^3.
$$
其导数为 $1$、次数为 $3$，是加性群之间有限 étale 的三次同源。这一核对只依赖 $a\bmod3$；$a\equiv\pm1\pmod9$ 不产生额外例外。

另一方面，R37 的普通和射线类域在 $3$ 处都未分歧，$F/\mathbb Q$ 在 $3$ 处亦未分歧。因此 $\kappa_3$ 为未分歧核类。现在可合法应用引理 46.1，得到
$$
\kappa_3\in\delta_{\mathbb Q_3}(D_a(\mathbb Q_3)).
\tag{46.20}
$$

### 5.4 射线分支的素数 2：整个一阶上同调都是 Kummer 像

此分支只有族 III 偶 $X$，故 $c=1$，而
$$
a=Z^e\equiv5\pmod8.
$$
所以 $M_a$ 为未分歧的一维 $\mathbb F_3$ 模，Frobenius 作用为 $-1$。

直接计算
$$
\boxed{\dim_{\mathbb F_3}H^1(\mathbb Q_2,M_a)=1.}
\tag{46.21}
$$
说明如下。野惯性为 pro-$2$，在 $M_a$ 上作用平凡，且到 $\mathbb F_3$ 的连续同态为零，所以可以通过温和商计算。取温和惯性生成元 $\tau$ 和 Frobenius $\sigma$，满足
$$
\sigma\tau\sigma^{-1}=\tau^2.
$$
一个 cocycle 在 $\sigma$ 上的值可唯一加 coboundary 消去，因为
$\sigma-1=-2$ 在 $\mathbb F_3$ 上可逆。在 $\tau$ 上的值可任取 $b\in\mathbb F_3$；上面关系给出的条件为
$$
-b=2b,
$$
自动成立。因此剩下恰一个自由参数，得到 (46.21)。

由于
$$
-27a\equiv1\pmod8,
$$
存在 $v_0\in\mathbb Z_2^\times$ 满足 $v_0^2=-27a$。取
$$
P_0=(0,v_0)\in D_a(\mathbb Q_2).
$$
R37 的三同源逆像三次式在此为
$$
T^3-\frac{2v_0}{27}.
\tag{46.22}
$$
其常数项赋值恰为 $1$，故为 $2$-Eisenstein，多项式没有 $\mathbb Q_2$ 根。因此
$\delta_{\mathbb Q_2}(P_0)\ne0$。结合 (46.21)，得到
$$
\boxed{
\delta_{\mathbb Q_2}(D_a(\mathbb Q_2))
=
H^1(\mathbb Q_2,M_a).
}
\tag{46.23}
$$
所以射线空间的全部类，无论其在惯性上为零还是非零，都满足此处 Selmer 条件。

### 5.5 无穷位

实 Galois 群阶为 $2$，而 $M_a$ 的阶为 $3$，故
$H^1(\mathbb R,M_a)=0$。全部无限位条件也满足。

第 5.1–5.5 节完成 (46.7) 的证明。

## 6. Mordell–Weil 与 Sha 的精确分界

按定义，
$$
\operatorname{Sel}^{\phi}(B_a/\mathbb Q)
=
\{\xi\in H^1(\mathbb Q,M_a):
\xi_v\in\operatorname{im}\delta_{\mathbb Q_v}
\text{ 对所有 }v\}.
$$
三同源的全局和局部上同调正合列给
$$
0\longrightarrow
D_a(\mathbb Q)/\phi B_a(\mathbb Q)
\longrightarrow
\operatorname{Sel}^{\phi}(B_a/\mathbb Q)
\longrightarrow
\Sha(B_a/\mathbb Q)[\phi]
\longrightarrow0.
\tag{46.24}
$$
这里右端表示 $\phi:\Sha(B_a)\to\Sha(D_a)$ 的核。这个正合列只使用局部处处平凡的定义，不使用 BSD 或 $\Sha$ 整体有限性；可参照 Milne, *Arithmetic Duality Theorems*, I §6 的同一上同调图表论证。

将 $V$ 限制到 (46.24)，其核恰为 $V\cap U_e=W_e$，故得到 (46.9)。

为说明 (46.10) 中没有隐藏的有理 $3$ 挠点修正，直接使用 $3$ 除法多项式。对 $B_a$，
$$
\psi_3(x)=3x(x^3+4a).
$$
若有非零有理 $3$ 挠点，则或者 $x=0$ 而 $a$ 为平方，或者 $x^3=-4a$ 而
$y^2=-3a$ 为平方。前者给 $F=\mathbb Q$，后者给 $F=\mathbb Q(\sqrt{-3})$，均已排除。对 $D_a$ 同理：$x=0$ 要求 $-3a$ 为平方；另一分支给 $y^2=81a$，要求 $a$ 为平方。故
$$
B_a(\mathbb Q)[3]=D_a(\mathbb Q)[3]=0.
\tag{46.25}
$$

同源在阶与 $3$ 互素的有限挠群上为同构；在自由部分上，两组同秩格之间的映射余商被 $3$ 消去，因为对偶同源与 $\phi$ 的复合为 $[3]$。于是
$$
\dim_{\mathbb F_3}
D_a(\mathbb Q)/\phi B_a(\mathbb Q)\le R_e.
$$
因此 $m_e\le R_e$，并由 (46.9) 得到余下维数不等式。

若 $v>R_e$，这确实证明存在非零的 $\phi$-Sha 类。但它不是矛盾；它说明一些类域候选被全局有理点条件阻挡，不能由“类群不为零”反推实际点。

## 7. 指标三次覆盖的显式构造

### 7.1 三同源逆像的三次代数

对有限点 $P=(U,V)\in D_a(K)$，令
$$
f_P(T)=T^3-\frac U3T-\frac{2V}{27}.
\tag{46.26}
$$
直接计算得
$$
\operatorname{disc}(f_P)
=\frac4{27}(U^3-V^2)=4a.
\tag{46.27}
$$
R37 已证明：若 $Q=(x,y)$ 满足 $\phi(Q)=P$，则
$$
t=\frac{2y}{3x}
$$
满足 $f_P(t)=0$；反过来，从一个根 $t$ 可恢复
$$
x=3t^2-U/3,\qquad y=3tx/2.
$$
因为 $a\ne0$，恢复过程中的 $x$ 不会为零。由此，$\phi^{-1}(P)$ 的三元素 Galois 集合与 $f_P$ 的根集相同。

因此 $f_P$ 的三次 étale 代数，正是 Kummer 类 $\delta_K(P)$ 的三点仿射作用 (46.18) 对应的代数。这将三同源下降和具体三次域接在一起，而不只使用“有根当且仅当在像中”。

### 7.2 从指标覆盖的点到 Mordell 点

设 $L$ 为一个候选三次域，$I_L$ 和 $\mu_e$ 如主定理。由 R42 的判别式及指标表，有 (46.12)。

曲线 $C_{L,e}$ 光滑：若某个射影奇点满足 $t\ne0$，则对 $t$ 的偏导
$-3\mu_e t^2$ 非零；若 $t=0$，则将使二元三次式 $I_L$ 有重根，与 $D_L\ne0$ 矛盾。故它是光滑射影 genus $1$ 曲线。

对一个 $K$ 点 $(u:v:t)$ 且 $t\ne0$，在三次 étale 代数
$L_K=L\otimes_{\mathbb Q}K$ 中定义
$$
\xi=u\omega+v\eta
-\frac{\operatorname{Tr}_{L_K/K}(u\omega+v\eta)}3,
\qquad
\theta=\xi/t.
\tag{46.28}
$$
平移不改变指标形式和判别式，所以
$$
\operatorname{Tr}(\theta)=0,\qquad
\operatorname{disc}(\theta)
=D_L\frac{I_L(u,v)^2}{t^6}
=D_L\mu_e^2=4a.
\tag{46.29}
$$
因此 $\theta$ 生成整个 étale 代数，其特征多项式可唯一写为
$$
T^3-x_\theta T-2w_\theta.
$$
由判别式公式，
$$
x_\theta^3-27w_\theta^2=a.
$$
于是
$$
P_\theta=(3x_\theta,27w_\theta)\in D_a(K).
\tag{46.30}
$$
式 (46.26) 恰为 $\theta$ 的多项式，故其三次代数为 $L_K$。这说明
$\delta_K(P_\theta)=\kappa_K$ 或 $-\kappa_K$，定向取决于整基和核生成元的选择。

迹和范数还给出显式覆盖映射：
$$
U=\frac{3\,\operatorname{Tr}(\xi^2)}{2t^2},
\qquad
V=\frac{27\,N(\xi)}{2t^3}.
\tag{46.31}
$$
它是非恒定的，故从稠密开集唯一延拓为光滑射影曲线间的态射。

### 7.3 反向：Kummer 像给指标覆盖的有理点

若 $\kappa_K$ 非零且位于局部或全局 Kummer 像，取
$P\in D_a(K)$ 使 $\delta_K(P)=\pm\kappa_K$。此时三点仿射作用无不动点，因此 $f_P$ 不可约，三次代数是域 $L_K$。将其根写为
$$
\theta=b+u\omega+v\eta,\qquad b,u,v\in K.
$$
由 (46.27) 及整基判别式公式，
$$
I_L(u,v)^2=\frac{4a}{D_L}=\mu_e^2.
$$
若值为 $+\mu_e$，得到 $(u:v:1)\in C_{L,e}(K)$；若为 $-\mu_e$，将 $u,v$ 同时取负即可。这一取负相应于 $P\mapsto-P$，Kummer 像保持不变。

若 $\kappa_K=0$，其三次 étale 代数有一个 $K$ 因子，形如 $K\times K'$ 或 $K^3$。取一个非平凡幂等元，它不在标量 $K$ 中但满足二次多项式，故其 $(u,v)$ 坐标满足
$$
I_L(u,v)=0,\qquad (u,v)\ne(0,0).
$$
于是 $(u:v:0)$ 是 $C_{L,e}$ 的 $K$ 点。

反过来，若覆盖有一个 $t=0$ 的 $K$ 点，其指标形式存在 $K$ 射影零点，所以三次代数不是域，仿射三点作用有不动点，故 $\kappa_K=0$。综合得到对每个特征零域的判据
$$
C_{L,e}(K)\ne\varnothing
\iff
\kappa_K\in\delta_K(D_a(K)).
\tag{46.32}
$$
符号 $\pm$ 不影响右边。

取全部完成域，并应用第 5 节，即得处处局部可解；取 $K=\mathbb Q$，即得 (46.14)。在 $\mathbb Q$ 上 $I_L$ 不可约，所以没有 $t=0$ 的有理点。

### 7.4 Jacobian 和覆盖的次数

标准二元三次式构造给出：若 $z^3=f(u,v)$、$\operatorname{disc}(f)=D$，则其 Jacobian 为
$$
y^2=4x^3+D.
$$
这个公式可在 Alpöge–Bhargava–Shnidman, *Math. Ann.* **391** (2025), §1.1 中核对。

在 (46.13) 中令 $z=\mu_e t$，得到
$$
z^3=\mu_e^2 I_L(u,v),
$$
右边三次式的判别式为 $\mu_e^8D_L$。所以 Jacobian 是
$$
y^2=4x^3+\mu_e^8D_L.
$$
令 $x=\mu_e^2 X$、$y=2\mu_e^3Y$，并使用 (46.12)，便得到
$$
Y^2=X^3+\frac{\mu_e^2D_L}4=X^3+a.
$$
因此 Jacobian 确实是 $B_a$，不是 $D_a$。

对一个几何一般的 $P\in D_a$，(46.31) 的逆像由多项式 $f_P$ 的三个根分配给 $L$ 的三个几何嵌入而给出。六个分配中，指标形式的指定符号保留恰三个偶定向分配。因此映射次数为 $3$。这个有向三点作用正是 (46.3) 的核作用，且由第 7.1 节的逆像公式，它在选取一个几何基点后识别为 $\phi:B_a\to D_a$。故 $C_{L,e}\to D_a$ 是该三同源的覆盖，相关 torsor 类为 $\kappa$ 在 $H^1(\mathbb Q,B_a)$ 中的像（定向改变至多取负）。

## 8. 通过全局筛的候选域计数与 Hasse 障碍

普通分支的非零字符按 $\{\kappa,-\kappa\}$ 配对，且同一对给同一三次域。由 (46.14)，通过有理点筛的字符恰为 $W_e\setminus\{0\}$，因此数量为
$$
N_e^{\rm MW}=\frac{3^{m_e}-1}{2}.
$$

射线分支只计数在 $I_2$ 上非零的字符。若限制映射
$$
W_e\longrightarrow\operatorname{Hom}(I_2,\mathbb F_3)
$$
为零，则没有这样的域。若非零，它是到一维空间的满射，具有
$2\cdot3^{m_e-1}$ 个在惯性上非零的字符；除以取负配对，得到 (46.16)。

因此，R42 候选数目 $N_Z$ 中，恰有
$$
\boxed{N_Z-N_e^{\rm MW}}
\tag{46.33}
$$
个三次域对应的 $C_{L,e}$ 处处局部可解而无有理点。这里按候选域标号计数，没有声称不同域的覆盖必定两两非同构。

普通分支可将该数写成
$$
\frac{3^v-3^{m_e}}2.
$$
若 $v>R_e$，它至少为
$$
\frac{3^v-3^{R_e}}2>0.
$$
射线分支若 $I_2$ 可见，则总候选数为 $3^{v-1}$，再减去 (46.16) 的数目或零。所有这些 Hasse 障碍都是实际的全局 $\Sha[\phi]$ 障碍，不是尚未排查的局部条件。

## 9. 与真正 Fermat 整数点的距离

对 R19 实际解，写 $p=6k+e$。R37 已构造
$$
P=\left(\frac{3X}{Z^{2k}},\frac{27W}{Z^{3k}}\right)
\in D_a(\mathbb Q),
$$
其 Kummer 类非零，且三次域就是 $T^3-XT-2W$ 所定义的域。因此该类必须在 $W_e$ 中；射线分支还须在 $I_2$ 上非零。这证明本筛对实际解的必要性。

在 R42 的指标坐标中，实际解提供更强的条件：
$$
I_L(u,v)=\pm\mu_e|Z|^{3k},
\qquad u,v\in\mathbb Z,\quad (u,v)=1.
\tag{46.34}
$$
所以 (46.13) 中还需要一个可取为
$$
t=\pm|Z|^k
$$
的整数坐标，并满足迹给出的整平移、对应 $X,W$ 的全部互素性和二进条件。

普通有理点只能给出若干分母的 $(u:v:t)$；清分母一般不会使 $t$ 成为指定的 $Z$ 幂，也不会保留所需原始性。故下列三个层次必须分清：

- 类域字符属于 $V$：本文证明这已保证相应三次覆盖处处局部可解。
- 类域字符属于 $W_e$：等价于该覆盖存在有理点，排除了相应非零 $\Sha$ 障碍。
- 存在 (46.34) 及 R19 的全部整数条件：这才给实际的固定 CM 同余曲线。

最后一层仍有真正的全局分母问题。

R42 的解数界也可按 $p\bmod6$ 改进：对每个 $e$，将其中的候选域数 $N_Z$ 替换为 $N_e^{\rm MW}$，再对 $e=1,5$ 求和。例如 I、II 中
$$
\#\{(p,X,W)\}
\le
2(15\,000\,000)^{\omega(|Z|)+2}
\bigl(N_1^{\rm MW}+N_5^{\rm MW}\bigr).
\tag{46.35}
$$
III 的指数可减一。也可取此界与 R42 原界的较小者。

这里并未发现新的“固定 $Z$ 后最大 $p$ 有效”机制：R13 早已给
$$
p\mid\gcd_{q\mid Z}\bigl(q-\chi_{-4}(q)\bigr),
$$
所以固定 $Z$ 的素数候选本来就有限。本结果增加的是精确的全局有理点障碍与候选类域筛，不应把固定参数有限性重复算成统一性突破。

## 10. 文献定位与结论边界

1. R37、R42：指定类群商、全部分裂和分歧性质、三同源逆像三次式、最大整环判别式与指标形式。
2. J. S. Milne, *Algebraic Groups* (2017), Theorems 17.96–17.98：[作者公开版本](https://www.jmilne.org/math/Books/iAG2017.pdf)。第 4 节给出本题所需 Lang–Hensel 论证。
3. J. S. Milne, *Arithmetic Duality Theorems*, 2nd ed. (2006), I §6，特别是 Selmer 和 Tate–Shafarevich 群的正合列图表：[作者公开版本](https://www.jmilne.org/math/Books/ADTnot.pdf)。本文对三同源版本直接从上同调列推导。
4. L. Alpöge, M. Bhargava, A. Shnidman, *A positive proportion of cubic fields are not monogenic yet have no local obstruction to being so*, Math. Ann. **391** (2025), 5535–5551，§1.1：[正式发表原文](https://doi.org/10.1007/s00208-024-03054-w)。本文只使用并核对二元三次覆盖的 Jacobian 公式；没有将该文的正比例结论套用到本题的指定分母素数支持。

目前仍缺少对所有允许 $Z$ 证明 $W_e=0$ 或其射线惯性限制为零的方法；即便某些 $W_e$ 非零，也还须研究其中有理点的完整分母支持。本文没有给出 Mordell–Weil 秩的统一上界，没有假定 $\Sha$ 总为零，也没有将有理覆盖点等同于 Fermat 整数解。
