# 十六个固定 Heegner 域：完整类群和的固定映射与 ST 非零 jet

日期：2026-11-12。**已证明。** 固定目标曲线始终为
$$
             E=389\mathrm a1:y^2+y=x^3+x^2-2x.
$$
本篇把 R140 的固定域首 jet 论证同时迁移到十六个固定、平方类
独立的虚二次域。每个域的**全部**类群和均保留，并来自一个
不随 $p,\ell$ 改变的有理模曲线映射。所得是实际 $Q$ 非扭、
小高度及不被 $p$ 整除的接口；尚未证明它在 $\delta^2$ 商中非零。

## 1. 十六个域及完全有限的类群证书

令 $F_D=\mathbb Q(\sqrt D)$，其中 $D$ 为表中的基本判别式。
$R_D$ 是选定的分歧素理想生成元所对应的有理素数集合，
$D_0=\prod_{r\in R_D}r$。最后两列给一个在 $F_D$ 中主理想
分裂、目标 E 也普通且非异常的固定素数 $q_D$。

| $D$ | $h_D$ | $R_D$ | $D_0$ | $q_D$ | $a_{q_D}(E)$ |
|---:|---:|---|---:|---:|---:|
| $-7$ | 1 | $\varnothing$ | 1 | 11 | $-4$ |
| $-11$ | 1 | $\varnothing$ | 1 | 23 | $-4$ |
| $-19$ | 1 | $\varnothing$ | 1 | 7 | $-5$ |
| $-67$ | 1 | $\varnothing$ | 1 | 17 | $-6$ |
| $-20$ | 2 | $\{2\}$ | 2 | 29 | $-6$ |
| $-24$ | 2 | $\{2\}$ | 2 | 7 | $-5$ |
| $-35$ | 2 | $\{5\}$ | 5 | 11 | $-4$ |
| $-52$ | 2 | $\{2\}$ | 2 | 17 | $-6$ |
| $-187$ | 2 | $\{11\}$ | 11 | 47 | $-2$ |
| $-232$ | 2 | $\{2\}$ | 2 | 59 | $3$ |
| $-267$ | 2 | $\{3\}$ | 3 | 67 | $-5$ |
| $-372$ | 4 | $\{2,3\}$ | 6 | 97 | $-9$ |
| $-483$ | 4 | $\{3,7\}$ | 21 | 127 | $11$ |
| $-555$ | 4 | $\{3,5\}$ | 15 | 139 | $16$ |
| $-795$ | 4 | $\{3,5\}$ | 15 | 199 | $-2$ |
| $-1435$ | 4 | $\{5,7\}$ | 35 | 359 | $-20$ |

以下全部断言由附带的纯整数脚本
[check-sixteen-exponent-two-heegner-fields.py](../scripts/check-sixteen-exponent-two-heegner-fields.py)
验证；没有使用类数数据库或浮点识别。

1. 每个 D 为基本判别式，且 $(D/389)=1$。
2. 穷举 $|b|\le a\le c$、$b^2-4ac=D$、$\gcd(a,b,c)=1$，
   边界取 $b\ge0$，枚举范围仅 $a\le\sqrt{|D|/3}$。
   所得 reduced forms 数恰为表列类数。
3. 每个 reduced form 均满足 $b=0$、$|b|=a$ 或 $a=c$。
   这些恰为自反的 reduced classes，故类群指数为二。
4. 对 $d\mid D_0$，分歧理想乘积的 norm 为 d。其 form 取
   $a=d$，若 $4d\mid D$ 则 $b=0$，否则 $b=d$，并令
   $c=(b^2-D)/(4d)$。逐个约化后，$2^{|R_D|}=h_D$ 个 form
   全部不同且等于上述完整列表。这同时证明 **表列生成元
   是真正的类群基**，不只是全部分歧理想的一个生成集合。
5. 十六个 D 在 $\mathbb Q^\times/\mathbb Q^{\times2}$ 的
   负号和素因子坐标中，二元消元秩为 16。
6. 每个 $q_D$ 附有显式范数 $N(\alpha_D)=q_D$；脚本逐点
   计算 E 的判别式字符和，给上表 $a_q\not\equiv0,\pm1\pmod q$。

reduced-form 分类及逆类由 $b\mapsto-b$ 给出，是这里唯一的
标准二次型输入；上述有限枚举给完整而可重复的证书。
因此十六个二次字符独立。在不分歧素数上，全部惰性的联合
同余类有 Dirichlet 密度 $2^{-16}$。这里只说明有限字符类的
密度，尚未与大素因子筛集合作未经证明的相交。

## 2. 真正阶二的环类 lifts 与固定类群和

以下固定表中的一个域 F。对 $r\in R_D$，令 $\mathfrak r$
为 F 的分歧素理想。若 $c$ 与 $D_0$ 互素，其向
$\mathcal O_c=\mathbb Z+c\mathcal O_F$ 的收缩是可逆理想，且
$$
                \mathfrak r_c^2=(r)\quad\hbox{在 }\mathcal O_c.
\tag{1}
$$
这是素于 c 理想的 extension/contraction 乘法相容性；有理
生成元 r 也在 $\mathcal O_c$ 中。故每个实际 Artin lift
$\tau_{r,c}$ 阶数至多二。

表中选定的 $|R_D|$ 个类在最大阶类群中独立。因此它们在
$\operatorname{Pic}(\mathcal O_c)$ 中生成一个阶恰为 $h_D$
的子群 $C_c$，并同构映到 $\operatorname{Cl}(F)$。确实，
生成元阶二给阶数至多 $2^{|R_D|}=h_D$，满射到原类群又给
反向不等式。

这里使用的是**选定的基**。若无选择地把全部分歧素理想
都加入，原最大阶中的关系可能由 $\sqrt D$ 主化，而该元素
不在 $\mathcal O_c$ 中；那样可能多出相对类群的一个二阶核。
本篇的有限证书正好排除了这一歧义。

特别地，$\ell$ 在 F 惰性且 $\ell\nmid D_0$ 时有真实直积
$$
 \operatorname{Gal}(F[\ell]/F)=C_\ell\times T_\ell,
       \qquad |C_\ell|=h_D,\quad T_\ell\simeq C_{\ell+1}.
\tag{2}
$$
若 $\ell+1=pu$、$p\ge7$、$p\nmid u$，则 $p\nmid h_D$，
且对于唯一 $C_p$ 子扩张 $L/F$，
$$
       \operatorname{Gal}(F[\ell]/L)=C_\ell\times U_\ell,
                     \qquad |U_\ell|=u.
\tag{3}
$$
没有随 p 重新抽取 Hall lift，也没有用一个除以类数的有理点。

取固定 $\pi:X_0(389)\to E$、$\pi(\infty)=O$。对 $d\mid D_0$，
令 $d_d:X_0(D_0\cdot389)\to X_0(389)$ 为对应的退化映射。
在 CM 点上使用分歧理想核及原 $389$ 理想方向，定义
$$
 \Phi_D=\sum_{d\mid D_0}\pi\circ d_d.
\tag{4}
$$
若 $z_c$ 是导子 c、带这个固定层结构的原始 CM 点，则
$$
                \Phi_D(z_c)=\sum_{\gamma\in C_c}\gamma P[c].
\tag{5}
$$
其证明逐个使用 quotient by $\mathfrak r_c$ 的 CM 互反律；
$389$ 子群同时运输。由于 $\tau_{r,c}^{-1}=\tau_{r,c}$，这里
也没有逆 Artin 方向造成的不同代表。

映射 (4) 非恒定。其拉回微分是固定非零 Manin 常数乘
$$
                   \sum_{d\mid D_0} d f(d\tau)\,d\tau.
\tag{6}
$$
在无穷尖点，q 的一次项只来自 $d=1$，系数非零。
并且每个 $d_d$ 保持无穷尖点，故 $\Phi_D(\infty)=O$。

## 3. 基层完整迹、固定扭点乘数和有限源中心

固定 E 的秩至少二。对每个 Heegner 理想方向，Gross–Zagier
及 Kolyvagin 的已证结论给
$$
                   P_{F,D}=\operatorname{Tr}_{F[1]/F}P[1]
                                   \quad\hbox{为扭点}.
\tag{7}
$$
这里只用完整类群迹；单个 $\pi(c)$ 不必是扭点或 O。

因 E 非 CM，$E(F^{\rm ab})_{\rm tors}$ 有限。R140 §1 的
同一证明适用每个固定 F：Serre 开像使交换子包含固定深度的
上下幺幂子群，其共同不变挠子阶有界。十六个域有限，故可选
同一个固定整数 $t_0>0$ 杀掉它们的这些挠群。删除有限多个
整除 $t_0$ 的输入素数 p，以后该乘数为 p 单位。

令 $\Psi_D=[t_0]\Phi_D$。在 $X_0(D_0\cdot389)$ 上，只取
最大阶 CM 源点及其实际层结构：$h_D$ 个理想类、$389$ 的
两个分裂理想方向，以及 $D_0$ 的唯一分歧核。这是固定的
$2h_D$ 个点，记作 $\Sigma_D$。由 (5)–(7)，
$$
                         \Psi_D(c)=O\qquad(c\in\Sigma_D).
\tag{8}
$$
所有十六组中心、代数局部参数和 CM de Rham 基可放在同一个
固定数域 K 中。该集合不随输入 p 或辅助 $\ell$ 改变。

## 4. Cornut 控制的是这里的完整类群分支

对所选域 F 使用表列固定 $q=q_D$。显式 $N(\alpha_D)=q$
使 q 的两个理想在类群中均主；$q\nmid D_0\cdot389D$，且
目标 E 在 q 好普通。由 (1) 的同一实际 lifts，
$$
 \operatorname{Gal}(F[q^n]/F)
       =C_{q^n}\times(\mathbb Z/q^n)^\times,
 \qquad G_0=C\times\mu_{q-1}.
\tag{9}
$$
记 $H_\infty/F$ 为反圆分 $\mathbb Z_q$ 塔，$H_j/F$ 次数
$q^j$。令原整数点
$$
 Z_0=\operatorname{Tr}_{F[1]/F}P[1],\qquad
 Z_n=\sum_{g\in G_0}gP[q^n]\in E(H_{n-1}),\quad n\ge1.
\tag{10}
$$

Cornut（2002）引言主定理和 §4 Theorem A 对原
$\pi:X_0(389)\to E$ 及 F 适用，给某个 $Z_n$ 非扭。
**不是**把附带分歧素数 $D_0$ 的新层数误称为满足 Heegner
条件；(4) 只负责把已知原 Heegner 族中的完整 C 和放进同一
正式盘。这个平凡 $G_0$ 角色正是所需角色。

在 $c\in\Sigma_D$ 处取 ST 参数 T、固定 CM period 比值 v。
Katz（1981）Main Theorem 4.3.1 给
$$
 v=\kappa_{D,c}\log(1+T),\quad \kappa_{D,c}\ne0,
 \qquad F_{D,c}(v)=\log_E\Psi_D(t_c(v))
                         =\sum_{m\ge1}b_{D,c,m}v^m.
\tag{11}
$$
这是形式级数和充分小盘的恒等式；在 ST 挠点处不能把
$\log\zeta=0$ 代回外层未必收敛的级数。真实值由同一盘内
Abelian 对数的原函数定义，和 R115/R140 的约定一致。

拉回微分给有界整 Amice 测度 $\mu_{D,c}$，满足
$$
 \int_{\mathbb Z_q}x^{m-1}\,d\mu_{D,c}(x)
          =\kappa_{D,c}^m h_{D,c,m},\qquad
                         h_{D,c,m}=m!b_{D,c,m}.
\tag{12}
$$
令
$$
 M_{D,c}(W)=\int_{\mathbb Z_q^\times}
 x^{-1}(1+W)^{\log\langle x\rangle/\log(1+q)}\,d\mu_{D,c}(x).
\tag{13}
$$
则这个**指定的 tame 指数 $-1$ 分支**非零。

证明如下。固定中心的原始 ST 根 $T=\zeta_{q^n}^a-1$ 对应
该中心上方的导子 $q^n$ CM 点；q 主理想及素于 q 的层结构
使全部标签保持。这是 Katz 的 lifting criterion 与 R115
的同一实际识别。由 (5)，在这些点上先对 C 求和正是
$\Psi_D$ 的值。再对 tame 群求和，原始 Gauss 恒等式把
(13) 在 conductor $q^n$ 的每个原始 wild 字符处的值，识别
为非零 Gauss 标量乘
$$
          t_0\sum_{\gamma\in\operatorname{Gal}(H_{n-1}/F)}
                              \chi^{-1}(\gamma)\log_E(\gamma Z_n).
\tag{14}
$$
完整 h 项没有丢失，也没有新的 h 倍数。

若 (13) 恒零，则所有 (14) 为零。令 $N_n$ 是最高一层
$H_{n-1}/H_{n-2}$ 的群环范数。字符正交性给真正整数点
$(q-N_n)Z_n$ 的对数为零，因此该点为扭点。另一方面原始
Hecke 递推准确为
$$
 \begin{split}
 Z_1&=(a_q-2)Z_0,\\
 \operatorname{Tr}_{H_1/F}Z_2&=a_qZ_1-(q-1)Z_0,\\
 \operatorname{Tr}_{H_{n-1}/H_{n-2}}Z_n
                         &=a_qZ_{n-1}-Z_{n-2}\quad(n\ge3).
 \end{split}
\tag{15}
$$
第一式因 q 的两条水平分支都主；第二式保留 tame 重复因子
$q-1$；完整类群和已在 $Z_0$ 中，不再乘 h。
由 $Z_0$ 扭点归纳，(15) 和 $(q-N_n)Z_n$ 扭迫全部 $Z_n$
扭，违背 Cornut。故 (13) 非零。

每个理想方向分别用同一定理；同一方向的中心是实际族的
Galois 共轭。因此结论逐个适用于有限集合全部中心。

## 5. 一个固定进程控制所有完整总 jet

若 $M_{D,c}(W)=A_eW^e+\cdots\ne0$，取 k 使
$k+1>v_q(A_e)$。对充分大的
$m\equiv0\pmod{(q-1)q^k}$，单位上的矩为
$M_{D,c}((1+q)^m-1)$，赋值准确为
$v_q(A_e)+e(1+v_qm)$。而 $q\mathbb Z_q$ 部分的矩赋值至少
$m-1$；前者为 $O(\log m)$，所以两部分不能抵消。
结合 (12)，得到该中心的 $h_{D,c,m}\ne0$。

有限个域和中心取最小公倍数及最大阈值，得到固定
$C,m_0>0$，使
$$
 m\ge m_0,\quad C\mid m
       \quad\Longrightarrow\quad
 h_{D,c,m}\ne0
 \quad\hbox{对表中全部 }D\hbox{ 和全部 }c\in\Sigma_D.
\tag{16}
$$
固定数域中的这些系数就是 **(4) 的完整类群映射** 的 jet，
不是先证明每个单点 jet 非零后任意相加。

其高度、分母预算由 R116 的固定代数 Gauss–Manin 多项式
系统证明逐项适用。有限集合取同一常数，有
$$
                       h(h_{D,c,m})\le C_1m\log(m+2).
\tag{17}
$$
不依赖输入 p、$\ell$。选固定 B，既为 C、全部 $|D|$、
$D_0\cdot389$ 和所需有限坏素数的倍数，又满足 $B\ge m_0$。
若 $\ell\equiv-1\pmod B$、$p\nmid B$ 且 $\ell+1=pu$，则
$B\mid u$，所以 (16) 可用于 $m=u$。同时每个负判别式 D
的奇 Dirichlet 角色在 $-1$ 取 $-1$，故 $\ell$ 在十六个 F
中全部惰性。

## 6. 原环类点的非扭性和小高度迁移

取 $x/(\log x)^2<\ell\le x$、$\ell\equiv-1\pmod B$，
$\ell+1=pu$、$v_p(\ell+1)=1$、$u\le U$，并删固定有限例外。
对每个 D，令
$$
 Q_{D,p,\ell}=\operatorname{Tr}_{U_\ell}\Psi_D(z_\ell)
             =[t_0]\operatorname{Tr}_{F_D[\ell]/L_D}P[\ell].
\tag{18}
$$
(3)–(5) 已证明 (18) 是完整原整数点。其范数为零，因为
基层完整迹被 $t_0$ 杀掉。

在 $\ell$ 的 canonical CM 正式盘，阶 $\ell+1$ 的 torus
可以整线性化，令参数 w 的一次项为一。固定 CM period
坐标 v 与 w 到次数 $\ell+1$ 相同。这正是 R114 的实际
formal-CM 论证，所用对象只要求固定代数映射、(8) 和
$\ell$ 惰性；没有使用类数一或单个 $\pi(c)=O$。
因此 (18) 的 $U_\ell$ 迹首候选项是
$$
                  u\,b_{D,c,u}\,r^u,
             \qquad v_\ell(r)=1/(\ell+1).
\tag{19}
$$
若 $h_{D,c,u}$ 在该 $\ell$ 位为单位，则 $u<\ell$ 保证
$u!$ 也为单位。R114 的整微分尾界（$m a_m$ 整）严格使
(19) 的赋值 $1/p$ 小于所有其它项，故
$$
                    v_\ell\log_E Q_{D,p,\ell}=1/p.
\tag{20}
$$
这是真正非零对数，所以 (18) 非扭。

由 (16)–(17)，可为每个 u 的全部中心系数选择一个非零
有理整数 $J_u$，容纳其分子及分母理想的 norm，且
$\log|J_u|=O(u\log(u+2))$。任何破坏上述全部单位条件的
$\ell$ 都整除 $\prod_{u\le U,\,B\mid u}J_u$，且
$\log\ell\sim\log x$。
因此这样的坏 $\ell$ 总数至多
$$
                       O\!\left(\frac{U^2\log(U+2)}{\log x}\right).
\tag{21}
$$
常数固定，已包含十六个域及其全部可能源中心。

固定模参数化的 CM 高度上界以及 Néron–Tate 的 Cauchy
不等式给，仍对全部十六个原点统一，
$$
                 \widehat h(Q_{D,p,\ell})\ll u^2\log\ell.
\tag{22}
$$
若采用 $p>x^\theta$、$\theta=0.667$ 的大素因子输入，则
$U\ll x^{1-\theta}$，(21) 是 $o(x/\log x)$，且
$$
 u^2\log\ell\ll p^{2(1-\theta)/\theta}\log p
                      =p^{666/667}\log p=o(p).
\tag{23}
$$
本式只是对同一输入的高度结论，**不擅自断言**这些 p 已
在至少一个 F 中分裂；联合筛另由 R149 负责。

每个固定 $F_D$ 上使用 Silverman（2004）Theorem 1 的全阿贝尔
扩张统一正高度下界（R140 已逐项核其非 CM 范围）；有限个 F
取最小正下界。于是 (20)、(23) 给原 Q 不被 p 整除；同一 Gauss
算子证明还给其 $\mathcal O=\mathbb Z_p[\zeta_p]$ 指数
$a\le(p-3)/2$。如果其中一个源域在 p 分裂且其它 R146 条件
成立，R146 的两步判据可用于该原点，但 **$a\le1$ 尚未证明**。

## 7. 与实际联合筛合并：一个固定 F 上的无穷小高度分裂输入

R149 已对任意固定 B 给完整二维 Selberg 上界。在
$\theta=667/1000$ 时，十六域全部惰性的 p 所对应的坏
$\ell$ 主项系数小于 $0.00075$，而固定进程 Fouvry 下界
余量大于 $0.001359$，都以 $x/(\varphi(B)\log x)$ 为尺度。
所以仍有 $\gg_B x/\log x$ 个实际 $\ell\le x$ 满足
$$
 \ell\equiv-1\pmod B,\qquad
 p=P^+(\ell+1)>x^\theta,
       \qquad p\text{ 至少在一个表列 }F_D\text{ 中分裂}.
\tag{24}
$$
这是同一筛中删除坏类，未使用两个正密度集合必相交的推断。

R138 的固定非 CM 例外删除还允许同时保留
$$
 a_p\not\equiv0,\pm1\pmod p,\qquad
 a_\ell\not\equiv0\pmod p,
 \qquad v_p(\ell+1)=1.
\tag{25}
$$
这些额外坏 $\ell$ 为 $o(x/\log x)$，故不会耗尽 (24) 的
固定正余量。再删固定 p 例外，R147 §1.1 对全部十六域
统一给 full $\mathrm{GL}_2$。

同一组辅助素数上有 $u\le2x^{1-\theta}$。直接再删除
$\ell\le x/(\log x)^2$；这样的整数总数就是
$O(x/(\log x)^2)=o(x/\log x)$，不需假设一个新的筛相交。
剩余者正满足 §6 的范围。所有完整 jet 坏素数的数量为
$O(x^{2(1-\theta)})=o(x/\log x)$。故在 (24)–(25) 的同一
剩余集合上，十六个实际原点 (18) 全部满足 (20)、(22)–(23)。

在每个剩余对中选一个 p 分裂的表列域。由有限鸽巢，存在
一个**固定的** $F_*$，以及无穷多个不同的 p 和相应 $\ell$，
使同时有
$$
 \begin{gathered}
 p\text{ good ordinary、非异常且 split }F_*,\\
 \ell\text{ inert }F_*,\quad \ell+1=pu,\quad
 p\nmid ua_\ell h_{F_*},\quad u\ll p^{333/667},\\
 Q=[t_0]\operatorname{Tr}_{F_*[\ell]/L}P[\ell]\ne\text{扭点},
 \quad N_{L/F_*}Q=0,\quad
 \widehat h(Q)\ll p^{666/667}\log p=o(p).
 \end{gathered}
\tag{26}
$$
p 的无穷性也直接来自 (24) 的 $p>x^\theta$，不是同一固定 p
配上无穷辅助素数。由 R119/R139 所用的 Nekovář 定理，对
每个 (26) 的范数一簇 $A$，全部 $\Sha(A/F_*)$ 有限，且
$A(F_*)\otimes\mathbb Z_p$ 为 O 自由秩一。写
$Q=\delta^a\varepsilon w$，已有
$$
 0\le a\le(p-3)/2,\qquad
 \operatorname{length}_{\mathcal O}\Sha(A/F_*)[p^\infty]\le2(a+1).
\tag{27}
$$
同时 R146 的正号下界适用，无需控制负扭曲的秩或 Sha。
目前 (27) 仍允许 $a\ge2$，所以 (26) 没有被误称为原目标
曲线的 Sha 有限性。R141 的类数一源简单零也未自动用于
$\Psi_D$；若以后要用该极点判据，须另付其源不分歧与 Hasse
比较，当前小高度和分裂结论不需要它。

## 一手来源与已证输入

- C. Cornut, *Mazur's conjecture on higher Heegner points*, Invent.
  Math. **148** (2002), 495–523，
  [作者发表版](https://webusers.imj-prg.fr/~christophe.cornut/papers/mcinv_published.pdf)，
  引言主定理，§4 Theorem A，§4.1 Lemma 4.2。本篇只在原
  level 389 使用其定理；完整类群的固定映射由 §2 单独证明。
- N. Katz, *Serre–Tate local moduli*, LNM **868** (1981),
  138–202，[作者全文](https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf)，
  Theorem 2.1(4)、Main Theorem 4.3.1–4.3.2。
- J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des
  courbes elliptiques*, Invent. Math. **15** (1972), 259–331：
  固定非 CM 开像及 R140 的固定 abelian 挠子有限证明。
- J. H. Silverman, *A lower bound for the canonical height on elliptic
  curves over abelian extensions*, J. Number Theory **104** (2004),
  353–372，[作者全文](https://arxiv.org/pdf/math/0305041)，
  Theorem 1、§4 Theorem 3；后者给非 CM 挠群有限性，前者
  给每个固定 $E/F_D$ 的全阿贝尔域正高度下界。
- R114–R116、R123、R140：准确 ST/Amice/Gauss 公式、真正
  整数投影 $q-N_n$、canonical CM 全尾界和固定 jet 高度。
  本篇已重证新类群 lift、完整迹、初始递推和指定分支识别。
- R109、R119、R139、R146：实际 Gauss 整除、非零范数一点
  的 O 格秩一和有限 Sha、正号 Selmer 两步判据。
- [有限证书脚本](../scripts/check-sixteen-exponent-two-heegner-fields.py)：
  全部二次型和范数只用整数运算；E 点数只用有限域字符和。
