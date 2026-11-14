# R40：完整 Selmer 的反圆分主项、剩余 Sha 块与二阶非零判据

**可信度：已证明。** 日期：2026-11-12。

固定
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad
P=(-1,4),\quad Q=(9,24),
$$
并固定 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$。
写 $p=\mathfrak p\bar{\mathfrak p}$，
$\pi=\psi(\mathfrak p)$、$\bar\pi=\psi(\bar{\mathfrak p})$，
$\iota=\iota_{\mathfrak p}(i)\in\mathbb Z_p$，所以 $\iota^2=-1$。
本文的 $\psi$ 是固定曲线的 Hecke 字符。

R4 给出 $\operatorname{rank}E(\mathbb Q)=2$；
R37 已证明
$$
j_p=h^-([i]P,Q)\ne0.
\tag{1}
$$
本文把 (1) 放进 Perrin–Riou **不预设 Sha 有限**的原始完整
Selmer 主项定理，而不只使用其 Mordell–Weil 特例。

## 1. 结论与实际 Katz 分支

令 $K_\infty/K$ 是唯一的 $\mathbb Z_p^2$-扩张，
$D_\infty/K$ 为其中的反圆分 $\mathbb Z_p$-扩张。
设 $\mathcal O$ 为 $\mathbb Q_p$ 最大非分歧扩张的整数环的完备化。
使用 Agboola–Howard 2006，§2.1 的 Katz 测度 $\mu_{\mathfrak p}$，
并用其中的扭转约定
$$
\operatorname{Tw}_\chi(g)=\chi(g)g.
$$
定义已移动到 Selmer 中心的测度
$$
\mathcal L_{E,\mathfrak p}
=\operatorname{pr}_{K_\infty}
\operatorname{Tw}_{\psi_{\mathfrak p}}(\mu_{\mathfrak p}),
\qquad
F^-_p=\operatorname{pr}_{D_\infty}\mathcal L_{E,\mathfrak p}.
\tag{2}
$$
这里 $\psi_{\mathfrak p}$ 是作用在 $T_\pi E$ 上的完整 Galois 字符；
先扭转再投影，已把有限字符分量一并选定。
在 Agboola–Howard 原文中主要写的是共轭素位 $\mathfrak p^*$；
将全文两素位互换即为 (2)。

令 $\kappa=\langle\psi_{\mathfrak p}\rangle$、
$\kappa^*=\langle\psi_{\bar{\mathfrak p}}\rangle$，
它们是 $\operatorname{Gal}(K_\infty/K)$ 上的两个主单位字符。
反圆分字符 $\rho^- =\kappa/\kappa^*$ 给出
$\operatorname{Gal}(D_\infty/K)\simeq1+p\mathbb Z_p$。
选择 $\gamma^-$ 使 $\rho^-(\gamma^-)=u=1+p$，写
$$
T=\gamma^--1,\qquad
F^-_p(T)\in\mathcal O[[T]],\qquad
a^-_{2,p}=[T^2]F^-_p(T).
\tag{3}
$$

**定理 A。** 令
$$
r_p=\operatorname{corank}_{\mathbb Z_p}
\Sha(E/\mathbb Q)[p^\infty]
=\operatorname{rank}_{\mathbb Z_p}N_p,
\tag{4}
$$
其中 $N_p$ 是 R35 的实际中心类群核。则：

1. $F^-_p\ne0$，且
   $$\operatorname{ord}_{T=0}F^-_p\ge2+r_p.$$
2. 在完整 Selmer 空间上有一个自然的 $r_p$ 维剩余交替配对
   $C_p$，详见 §4，满足
   $$
   \operatorname{ord}_{T=0}F^-_p=2+r_p
   \quad\Longleftrightarrow\quad \det C_p\ne0.
   \tag{5}
   $$
   当 $r_p=0$ 时，空矩阵的行列式约定为 $1$。
3. 因而有无条件等价
   $$
   \boxed{\quad
   \Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
   \quad\Longleftrightarrow\quad a^-_{2,p}\ne0.
   \quad}
   \tag{6}
   $$

(6) 没有附加 cyclotomic 调节子非零的假设。
它仍未证明 $a^-_{2,p}$ 对无穷多个 $p$ 非零。

**定理 B（临界值的有限证书）。** 对 $n\ge0$，设
$$
m_{p,n}=(p-1)p^n,\qquad
t_{p,n}=u^{m_{p,n}}-1,\qquad
V_{p,n}=F^-_p(t_{p,n}).
\tag{7}
$$
则
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\quad\Longleftrightarrow\quad
\exists n\ge0:\ v_p(V_{p,n})<3(n+1).
\quad}
\tag{8}
$$
这些 $V_{p,n}$ 是实际 Katz 插值值；其对应的复临界值为
$$
L(\psi^{2m_{p,n}+1},m_{p,n}+1),
\tag{9}
$$
带 §7 明确指定的 Katz 周期与 Euler 正规化。
不把 (9) 的普通复非零性替代 (8) 的赋值条件。

## 2. 完整 Selmer 的维数：pi 初级与全 p 初级不能混用

记 $\check S_\pi(K)$ 为 $\pi^n$-Selmer 群对乘 $\pi$ 的逆极限。
Kummer 正合列给出
$$
0\longrightarrow E(K)\otimes_{\mathcal O_K}\mathcal O_{K,\mathfrak p}
\longrightarrow\check S_\pi(K)
\longrightarrow T_\pi\Sha(E/K)\longrightarrow0.
\tag{10}
$$
本文所有维数均在张量 $\mathbb Q_p$ 后读取。
设
$$
S=\check S_\pi(K)\otimes\mathbb Q_p,\quad
S^*=\check S_{\bar\pi}(K)\otimes\mathbb Q_p,\quad
W=E(K)\otimes_{\mathcal O_K,\iota_{\mathfrak p}}\mathbb Q_p.
$$
于是
$$
0\longrightarrow W\longrightarrow S\longrightarrow
V_\pi\Sha(E/K)\longrightarrow0.
\tag{11}
$$

为核对这里的 $r$，令
$S_{\mathbb Q}=\check{\operatorname{Sel}}_p(E/\mathbb Q)\otimes\mathbb Q_p$。
限制与核心限制（$p\ne2$）及 $[i]$ 给出
$$
\check{\operatorname{Sel}}_p(E/K)\otimes\mathbb Q_p
=S_{\mathbb Q}\oplus[i]S_{\mathbb Q}.
\tag{12}
$$
也可从 $E^{(-1)}\simeq E$ 的二次扭曲分解得到 (12)。
复共轭在右边两项分别为 $+1,-1$。
投影
$$
e_\pi=\tfrac12(1+\iota^{-1}[i]),\qquad
e_{\bar\pi}=\tfrac12(1-\iota^{-1}[i])
\tag{13}
$$
分别将 $S_{\mathbb Q}$ 同构到 $S,S^*$。
例如 $e_\pi$ 在 $S_{\mathbb Q}$ 上的核为零：若
$[i]x=-\iota x$，施复共轭再比较即得 $2\iota x=0$。
由 (12)，它也满射。此论证与 Kummer 子空间相容，故
$$
V_\pi\Sha(E/K)\simeq V_p\Sha(E/\mathbb Q),
\qquad
\dim S=\dim S^*=2+r_p.
\tag{14}
$$
特别地，$\operatorname{corank}\Sha(E/K)[p^\infty]=2r_p$；
Perrin–Riou 主项里使用的是**单个** $\pi$ 初级的 $r_p$，不是 $2r_p$。

R35 §5 的正合列
$$
0\longrightarrow F_p^{\rm MW}
\longrightarrow\operatorname{Hom}(N_p,\mathbb Q_p/\mathbb Z_p)
\longrightarrow\Sha(E/\mathbb Q)[p^\infty]\longrightarrow0
\tag{15}
$$
中 $F_p^{\rm MW}$ 有限。
取 Tate 模后有理化，(15) 识别
$V_p\Sha(E/\mathbb Q)$ 与 $(N_p\otimes\mathbb Q_p)^\vee$，
所以 (4) 成立。R34 还给出 $r_p\in\{0,2,4,\ldots\}$。
有限余生成 $\mathbb Z_p$-模的余秩为零当且仅当它有限，
故不需要另假设全 Sha 有有限素数支撑。

## 3. Perrin–Riou 原定理的条件、中心与完整矩阵

这里使用已经出版的
Perrin–Riou，*Arithmétique des courbes elliptiques et théorie d'Iwasawa*，
Mémoires SMF 17 (1984)，V.8、V.17，及 V §4 的高度比较。
原文印刷页 96 明确要求沿 $F_\infty/F$ 各有限层的
$\mathfrak p$-adic 与 $\bar{\mathfrak p}$-adic Leopoldt 条件；
同页说明 $F(E_p)/K$ 为阿贝尔时满足。
这是 II §2.2、印刷页 44 定义的局部单位对角像秩条件，
不是在任意数域上无条件使用通常 Leopoldt 猜想。

本题取 $F=K$。曲线有全部 $\mathcal O_K$ 乘法，$p>3$、好普通约化；
CM 理论使全部扭点域及相关各有限层对 $K$ 阿贝尔，
因此上述两条件成立。
原文 II §1 先分开有限 tame 部分和 pro-$p$ 的
$\mathbb Z_p^2$-塔，故这里没有偷偷把基域改成 $K(E[p])$、
也没有改变 (14) 的维数。

设 $H_p$ 为原文 $Y(K_\infty)$ 的特征级数；$Y$ 是 ordinary
$\pi^\infty$-Selmer 的 Pontryagin 对偶。
完整高度是在 $S\times S^*$ 上定义的。
V §4、Theorem 12、Corollary 13 证明其对称性及与解析高度的比较；
V §5、印刷页 118–119 经 (13) 识别两边，给出一个
$(2+r_p)\times(2+r_p)$ 矩阵 $\mathcal M_p$，使高度 pencil 为
$$
s\mathcal M_p+s^*\mathcal M_p^t.
\tag{16}
$$
V.17 的有理化形式是：存在非零标量 $c_p$，使
$$
H_p(\kappa^s\kappa^{*s^*})
\equiv c_p\det(s\mathcal M_p+s^*\mathcal M_p^t)
\pmod{(s,s^*)^{3+r_p}}.
\tag{17}
$$
低于 $2+r_p$ 的次数全部为零。
$c_p$ 保留原公式 (19) 的 Euler、有限 Sha/Div 和格指数因子；
这些都是非零数。原公式在整格基下另保留一个 $\mathbb Z_p^\times$
因子。本文为便于采用 $P,Q$ 与有理补空间作基，允许 $c_p$ 吸收基变换的
非零行列式，**不宣称这种 $c_p$ 一定为单位**。
非退化性或 Sha 有限均不是 (17) 的前提。

更强的 V.8 对每个 $\mathbb Z_p$ 方向断言：零阶至少为 $2+r_p$，
恰等于该数当且仅当该方向的**完整**高度非退化。
原证明也处理特征分支恒零的情形；不能为了应用定理预先假设它非零。

### 3.1 与旧单塔中心 $T=p$ 的准确区别

设两个生成元满足
$$
(\kappa(\gamma_1),\kappa^*(\gamma_1))=(u,1),\qquad
(\kappa(\gamma_2),\kappa^*(\gamma_2))=(1,u).
$$
在**未扭转**的 tame $\psi_{\mathfrak p}$ 分量，
Selmer 中心对应字符 $\psi_{\mathfrak p}$，即原坐标 $(p,0)$。
扭转后的 (17) 在 $(s,s^*)=(0,0)$ 展开；换回未扭转坐标为
$$
(T_1,T_2)=(u^{1+s}-1,u^{s^*}-1).
\tag{18}
$$
反圆分方向是 $s^*=-s$，不是固定第二变量为零。
在已扭转的 Iwasawa 坐标 $X,Y$ 中，其限制为
$$
(X,Y)=\bigl(T,(1+T)^{-1}-1\bigr),\qquad T=u^s-1.
\tag{19}
$$
所以这里的二阶项不能直接替换为 R20–R36 的单 $\pi$ 塔的 $G_p(p)$。
由于一阶及常数项已为零，换元恰给
$$
[s^2]F^-_p(u^s-1)=\log_p(u)^2a^-_{2,p}.
\tag{20}
$$
若采用相反的对偶或 Artin 约定，还会有
$T\mapsto(1+T)^{-1}-1$；它的导数为 $-1$，故不改变二阶非零判据。

## 4. 已知 Mordell–Weil 块和实际剩余交替块

将 $S,S^*$ 通过 (13) 识别到同一个 $S_{\mathbb Q}$。
在其已知 Mordell–Weil 子空间 $W_{\mathbb Q}=\langle P,Q\rangle_{\mathbb Q_p}$
上，记 R39 的 cyclotomic 高度矩阵为 $H$，并令
$$
J=\begin{pmatrix}0&j_p\\-j_p&0\end{pmatrix}.
$$
直接将 (13) 代入双线性高度，利用
$h_{\mathfrak p}([i]U,[i]V)=h_{\mathfrak p}(U,V)$，得到
$$
\mathcal M_p|_{W_{\mathbb Q}}
=M_0=\frac14(H+\iota^{-1}J).
\tag{21}
$$
例如混合条目为
$\tfrac12(h_{\mathfrak p}(P,Q)+\iota^{-1}h_{\mathfrak p}([i]P,Q))$
，而 $H_{PQ}=2h_{\mathfrak p}(P,Q)$、
$j_p=2h_{\mathfrak p}([i]P,Q)$。
这也核对了 $M_0=M_p/2$，其中 $M_p$ 是 R39 的线性 period 矩阵。
全局共同负号的高度约定不影响以下行列式。

定义完整交替形式
$$
B^-_p=\mathcal M_p-\mathcal M_p^t.
$$
由 (21)，
$$
B^-_p|_{W_{\mathbb Q}}=\frac1{2\iota}J,
\qquad
\det(B^-_p|_{W_{\mathbb Q}})=-\frac{j_p^2}{4}\ne0.
\tag{22}
$$
这里是识别后的二维 CM 交叉矩阵；不要把它与
$E(K)\otimes_{\mathbb Z}\mathbb Q_p$ 上四维对称的 $h^-$ 矩阵混为同一矩阵。

令
$$
U_p=W_{\mathbb Q}^{\perp_{B^-_p}}
=\{x\in S_{\mathbb Q}:B^-_p(x,w)=0\ (w\in W_{\mathbb Q})\}.
\tag{23}
$$
虽然完整 $B^-_p$ 尚不一定非退化，(22) 已足够给出
$$
S_{\mathbb Q}=W_{\mathbb Q}\oplus U_p.
\tag{24}
$$
证明是：对任意 $x$，(22) 唯一确定 $w_x\in W_{\mathbb Q}$ 满足
$B^-_p(w_x,w)=B^-_p(x,w)$，于是 $x-w_x\in U_p$；
两子空间的交为零。该投影只使用实际高度，没有任取一个不相关的补空间。

将 (24) 与 (11)、(14) 合成，商映射限制给出
$$
U_p\xrightarrow{\sim}V_\pi\Sha(E/K)
\simeq V_p\Sha(E/\mathbb Q)
\simeq(N_p\otimes\mathbb Q_p)^\vee.
\tag{25}
$$
因此 $\dim U_p=r_p$。
把 $B^-_p|_{U_p}$ 的矩阵记为 $C_p$；它是实际完整 Selmer 高度在
Sha 商上的、由 (23) 唯一选择的剩余形式，而不是抽象猜测的额外块。
交替性使两个交叉块同时为零，故
$$
\det B^-_p=-\frac{j_p^2}{4}\det C_p.
\tag{26}
$$
变更 $U_p$ 的基只将右边乘一个非零平方，不改变非退化性。

在 (17) 中令 $s^*=-s$，得到
$$
[s^{2+r_p}]H_p((\kappa/\kappa^*)^s)
=-c_p\frac{j_p^2}{4}\det C_p.
\tag{27}
$$
更低次数均为零。
V.8 或 (27) 立即给出 (5) 的 characteristic 版本。
若 $r_p=0$，(22) 强迫恰为二阶；反过来，二阶主项非零由
$\operatorname{ord}\ge2+r_p$ 强迫 $r_p=0$。

## 5. 从 characteristic 到实际 Katz：已出版的完整接口

采用 Agboola–Howard，*Anticyclotomic Iwasawa theory of CM elliptic curves*，
AIF 56 (2006)，1001–1048 的规范。以下输入均不假设基层 Sha 有限。

- Theorem 2.2.1（Yager）把半局部单位模映到由
  $\sigma_{\mathfrak a}-N\mathfrak a$ 生成的理想，并把椭圆单位映到
  $(\sigma_{\mathfrak a}-N\mathfrak a)\mu_{\mathfrak p}$。
- Proposition 2.3.1、Proposition 2.3.4 给出扭转后的 Coleman 比较，
  同时保留 ordinary 局部条件和有限域下降的条件。
- Lemma 2.4.5、Corollary 2.4.6 核对类域论模与真正 Selmer 对偶的扭转。
  Theorem 2.4.7 是 Rubin 主猜想的 twisted 特征理想等式。
- 在根数 $+1$ 的情况下，Corollary 2.4.14 和
  Theorem 2.4.17(1)(b),(c) 直接给出 $D_\infty$ 上的 torsion 性及
  Katz 测度与 ordinary Selmer 特征理想的相等。

整系数比较所需条件 $p\nmid[K(\mathfrak f):K]$ 在这里全部成立。
因为 $\mathfrak f=(34(1+i))$ 等于一个单位乘
$(1+i)^3\cdot17$，类数为一的 ray class 公式给
$$
[K(\mathfrak f):K]
=\frac{N\mathfrak f}{4}
\left(1-\frac12\right)\left(1-\frac1{17}\right)^2
=256.
\tag{28}
$$
四个根单位仅 $1$ 模 $\mathfrak f$ 为 $1$，所以分母确为 $4$。
非异常性已在 R7、R24 证明。原曲线根数为 $+1$，证明见
`notes/2026-11-12-cm-local-inputs.md`。

也可以在双变量层直接检查 Coleman 像的额外理想为整个环：
固定辅助理想 $(7)$ 满足 $\psi((7))=-7$，扭转后的辅助因子在中心为
$-7-49=-56$，对全部目标 $p$ 为单位。因此其在
$\mathcal O[[X,Y]]$ 中为单位。
Theorem 2.4.7 与 Proposition 2.3.4 因而给出
$$
(\mathcal L_{E,\mathfrak p})
=\operatorname{char}_{\mathcal O[[\Gamma]]}
\bigl(Y_\pi(K_\infty)\widehat\otimes\mathcal O\bigr).
\tag{29}
$$
这是等理想，故任取与 (17) 约定一致的特征生成元后，两者相差
$\mathcal O[[X,Y]]^\times$。若对偶约定相反，先同时作 §3.1 的反演。
限制到 (19) 时这个单位仍是单位，中心值非零。
由于所有低阶项已消失，它只将首个齐次项乘其中心值。
于是 (27)、(5)、(6) 全部传递到 (2) 的**实际** Katz 测度。

此外，Agboola–Howard Corollary 2.1.5（使用 Greenberg）在根数 $+1$ 时
给 $F^-_p\ne0$。这证明的是整条反圆分分支非恒零，
没有给出其中心零阶恰为二。
至此定理 A 证明完毕。

## 6. 为什么这些实际约束仍允许额外 Sha 方向

下面的模型仅说明已经使用的模论、转置对称和主项约束本身不强迫
$r_p=0$；不把模型冒充实际 Katz 插值函数。

在 $A=\mathbb Q_p[[s,t]]$ 上取实际已知块 $M_0$，并令
$$
B=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
\mathcal A(s,t)=
\begin{pmatrix}
sM_0+tM_0^t+(s^3+t^3)I_2&0\\
0&sB+tB^t
\end{pmatrix}.
\tag{30}
$$
它满足
$$
\mathcal A(t,s)=\mathcal A(s,t)^t,\qquad
\mathcal A(-s,-t)=-\mathcal A(s,t).
$$
因此 $f=\det\mathcal A$ 具有相应交换和偶性；
其四次齐次主项就是完整四维 pencil 的行列式。
中心余核维数为四，已知 MW 部分为二，其余可取 $r=2$。
在反圆分线上
$$
\mathcal A(s,-s)=
s\,\operatorname{diag}(M_0-M_0^t,B-B^t),
$$
两块都可逆，故 $f(s,-s)$ 恰四阶而不是二阶。
两个坐标轴分支也都非恒零；三次单位矩阵项保证第一块不因
$\det M_0$ 恰为零而使整条轴消失。

$\det\mathcal A\ne0$ 给出单射 $A^4\xrightarrow{\mathcal A}A^4$；
余核是 projective dimension 一的 torsion 模。
深度引理给其深度至少一，故它没有非零有限长度子模。
因此额外中心维数与这些已证结构条件相容。

还可把第二块改成
$$
(s+t)I_2+(s^3-t^3)
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\tag{31}
$$
交换转置和共同变号性质仍成立，中心余核仍为四维；
但剩余一阶反圆分形式为零，反圆分行列式恰八阶。
这对应 $r=2$ 而 $C_p$ 退化，准确展示 (5) 中不能省掉的条件。
模型没有声称满足实际 Euler-system 原始性、全部整数格或所有临界值插值。

## 7. 二阶系数的实际对数矩与中心临界值

设 $G=\operatorname{Gal}(K(\mathfrak f p^\infty)/K)$，
在 $G$ 上令 $x=\psi_{\mathfrak p}$、$y=\psi_{\bar{\mathfrak p}}$，
$z=\langle x/y\rangle$。按 (2) 的扭转和推前定义，
$$
\mathscr F_p(s):=F^-_p(u^s-1)
=\int_G x(g)z(g)^s\,d\mu_{\mathfrak p}(g).
\tag{32}
$$
这是有界测度上统一收敛的解析积分。
$\log_p z\in p\mathbb Z_p$，故可逐项微分，得到准确接口
$$
\boxed{\quad
a^-_{2,p}
=\frac1{2\log_p(u)^2}
\int_G x(g)\bigl(\log_p z(g)\bigr)^2\,d\mu_{\mathfrak p}(g).
\quad}
\tag{33}
$$
这里分母的 $2$ 是 Taylor 阶乘；$\log_p(u)^2$ 来自 (20)。
$(32)$ 的零次和一次矩均为零，由 §3 的完整 Selmer 下界得出，
无需 Sha 有限。

当 $m\ge0$ 且 $p-1\mid m$ 时，$z^m=(x/y)^m$，所以被插值的字符为
$$
\epsilon_m=\psi^{m+1}\bar\psi^{-m}
=\psi^{2m+1}N^{-m},
\qquad\text{infinity type }(m+1,-m).
\tag{34}
$$
它在 Katz 的范围 $0\le -(-m)<m+1$ 内。
令 $\alpha_{\mathfrak p}(\epsilon_m)$ 完全按
Agboola–Howard Theorem 2.1.1 的周期规范，则该定理给出
$$
\alpha_{\mathfrak p}(\epsilon_m)\mathscr F_p(m)
=\left(1-\frac{\epsilon_m(\mathfrak p)}p\right)
L_{\infty,\mathfrak f\bar{\mathfrak p}}
(\epsilon_m^{-1},0).
\tag{35}
$$
等式按该插值定理的复周期与 $p$-adic 周期比较解释；
不把未正规化的复 $L$ 值直接当作 $p$-adic 数。
这指定了 $V_{p,n}=\mathscr F_p(m_{p,n})$ 的实际输入和全部正规化。

为识别 (35) 的复临界值，利用
$\epsilon_m^{-1}=N^{-1}\bar\epsilon_m$ 及对理想施复共轭，得
$$
L(\epsilon_m^{-1},0)
=L(\bar\epsilon_m,1)=L(\epsilon_m,1)
=L(\psi^{2m+1},m+1).
\tag{36}
$$
两处 ordinary Euler 因子相同：
$$
1-\epsilon_m(\mathfrak p)/p
=1-\pi^m/\bar\pi^{m+1},\qquad
1-\epsilon_m^{-1}(\bar{\mathfrak p})
=1-\pi^m/\bar\pi^{m+1}.
\tag{37}
$$
因此 (35) 的 $p$ 上方总因子为
$(1-\pi^m/\bar\pi^{m+1})^2$。
当 $m\ge1$ 它是单位；$m=0$ 时非异常性也使它为单位。
若把 $L_\infty$ 展开，另有 $\Gamma(m+1)/(2\pi_{\mathbb C})^{m+1}$；
它与 (35) 的周期规范一起读取，不随意丢掉 $m!$。
本序列的 $p-1\mid m$ 还保证 $2m+1\equiv1\pmod4$，
所以 $\psi^{2m+1}$ 的有限导子仍为 $\mathfrak f$，没有新增的坏位 Euler 缺项。

第一项 $m=p-1$ 使用 $L(\psi^{2p-1},p)$。
R24 的单塔权 $2p-1$ 使用的是另一处值
$L(\bar\psi^{2p-1},2p-1)$；两者不能混同。

## 8. 有限证书的证明及它没有解决的无穷性

定理 A 给出 $F^-_p(T)=T^2A_p(T)$，
$A_p(T)\in\mathcal O[[T]]$ 且 $A_p(0)=a^-_{2,p}$。
提升指数公式给
$$
v_p(t_{p,n})=1+v_p(m_{p,n})=n+1.
$$
由整系数直接得到
$$
\frac{V_{p,n}}{t_{p,n}^2}
=A_p(t_{p,n})\equiv a^-_{2,p}\pmod{p^{n+1}\mathcal O}.
\tag{38}
$$
若左边模 $p^{n+1}$ 非零，则 $a^-_{2,p}\ne0$。
反之，若 $a^-_{2,p}\ne0$，取 $n+1>v_p(a^-_{2,p})$，
(38) 使左边具有相同赋值，因而模 $p^{n+1}$ 非零。
这与 (6) 合并即为 (8)。

同一等式给收敛的准确极限
$$
a^-_{2,p}=\lim_{n\to\infty}\frac{V_{p,n}}{t_{p,n}^2}.
\tag{39}
$$
**利用实际 Selmer 奇偶性的更宽阈值。** R34 已证明 $r_p$ 为偶数。
若 $a^-_{2,p}=0$，由定理 A 有 $r_p\ge2$，所以
$F^-_p(T)\in T^4\mathcal O[[T]]$。因此还得到
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\quad\Longleftrightarrow\quad
\exists n\ge0:\ v_p(V_{p,n})<4(n+1).
\quad}
\tag{40}
$$
无限时左边的赋值对每个 $n$ 至少为 $4(n+1)$。
有限时，充分大的 $n$ 满足
$v_p(V_{p,n})=2(n+1)+v_p(a^-_{2,p})<4(n+1)$。
这证明 (40)，也说明单次检验允许比 (8) 更大的赋值；
两种存在性判据仍等价。特别地，首个中央权
$L(\psi^{2p-1},p)$ 按 (35) 正规化后的赋值至多三就已经足够。

若 $a^-_{2,p}=0$，所有 $V_{p,n}$ 仍可能非零；此时只须
$v_p(V_{p,n})\ge4(n+1)$。所以 Greenberg 的分支非恒零，
或任意多个 (36) 的复非零值，都不证明 (6)。

当前跨素数目标可以改写为：对无穷多个目标 $p$，找到一个 $n$
使按 (35) 正规化的中心临界值满足 (8)。
允许 $n$ 随 $p$ 变化；不必给出统一赋值阈值或初级 Sha 为零。
本文已经给出完整 Selmer、真实 Katz 分支、实际中心临界值三者的接口，
尚未给出这种无穷性。

## 来源

- B. Perrin–Riou，*Arithmétique des courbes elliptiques et théorie d'Iwasawa*，
  Mémoires de la SMF 17 (1984)：II §1、§2.2；IV.22；V 开头印刷页 96 的
  hypotheses；V.8（印刷页 106–109）；V.12–V.13；V.17、式 (19)
  （印刷页 116–117）；完整 Selmer 的转置 pencil（印刷页 118–119）。
  [正式原文](https://www.numdam.org/article/MSMF_1984_2_17__1_0.pdf)。
- A. Agboola、B. Howard，*Anticyclotomic Iwasawa theory of CM elliptic curves*，
  Ann. Inst. Fourier 56 (2006)，1001–1048，Theorems 2.1.1、2.2.1、2.4.7、
  2.4.17；Corollaries 2.1.5、2.4.6、2.4.14；Proposition 2.3.4；
  Remark 1.1.8 的对偶作用约定。
  [正式原文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
- K. Rubin，*The “main conjectures” of Iwasawa theory for imaginary quadratic
  fields*，Invent. Math. 103 (1991)，25–68，Theorem 4.1。
  [出版记录](https://doi.org/10.1007/BF01239508)。本文件所需的 twisted 版本
  采用上列已出版 Agboola–Howard Theorem 2.4.7 的明确陈述与完整下降。
- R. I. Yager，*On two-variable p-adic L-functions*，Ann. Math. 115 (1982)，
  411–449。[出版记录](https://annals.math.princeton.edu/1982/115-2/p08)。
  本文使用的单位—测度比较为上列 Theorem 2.2.1。
- 本仓库 R4、R34、R35、R37、R39；
  `notes/2026-11-12-cm-local-inputs.md`。

未把 2026 年新稿中预设 Sha 有限的主项特例当作本结论的外部输入。
