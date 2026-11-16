# R458：三个真实同尾角色恢复三矩分量，两种宽度检出第三个有序不变量

日期：2026-11-16。**纸面原式证明；没有执行 profile、求积、符号程序、数学秩、格点枚举、人工测试或研究运行。**

[R456](R456-two-highest-ordered-current-invariants-on-real-mirror-copy-families.md) 已证明：固定一个物理宽度及唯一共同退化镜对，原同角色全部副本的三尾 current 评价商，相对于整个 whole-$E$ 零响应，只剩 $D_5,D_6$。对多宽库，当时准确保留
$
\operatorname{Pol}_{\le3}\subset D(\ker Eval)\subset\operatorname{Pol}_{\le4}.
$

本稿给出其中 $D_4$ 的完整判别。**若两种不同实际宽度各有原三个连续 low、同一个最后 high、至少八个真实完整 copy 中心，则**
$
\boxed{D(\ker Eval)=\operatorname{Pol}_{\le3}.}
$
因此相对于全部保持 whole $E$ 的响应，实际 formal 有序评价商恰是三项
$
\boxed{D_4,\ D_5,\ D_6.}
$
三个右矩不是假设为独立物理输入，而是先由三个已存在的同尾 low 角色恢复。两宽的比较保留全部原十三列；其中用于检出 $D_4$ 的两个系数，在单宽论证中确实可以被旧低列抵消。

这里的“两种宽度”是明确前提。R280/R324 的五块操作本身只是平移与正幅，R455 也允许从起点选择全同宽库；本稿**不声称已冻结库自动有两个不同宽度**。最后另说明，若新增强查询明确取了一个共同合法正仿射窗口中的两种伸缩评价，该前提怎样准确成立，而不把查询扩充说成原 period 已支付。

## 1. 原空间、共同 cap 与实际评价

沿 [R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md) 和 [R454](R454-complete-response-self-principal-trace-and-seven-ordered-current-invariants.md)，在
$
E(V)=(\pi V,\mathcal QV)=0,\qquad\mathcal O(V)=0
\tag{1}
$
下，全部有序跨包累计量具有同右锚的完整局部 current
$
\int_{\ell_u}^x u'\mathcal U_{V,n}''=\mathcal K_{V,n},
\qquad F_V=\frac14\mathcal K_{V,n}\big|_{A_u=0}.
$
$F\in\mathscr C_{39}$ 是三次 jet 多项式，对三矩 $n$ 线性。其十三个原列、六个完整规范代表及七个 $p,r$ 余列，全按 R456 §2(6)—(8)，不只取含 $u$ 部分。

记
$
p=u',\quad r=u'',\quad A_u=6pu'''-2r^2,
$
$
D_F(x)=c_F(x;(1,x,x^2))=\sum_{\nu=0}^6D_\nu(F)x^\nu.
\tag{2}
$
原完整响应像已经闭合为
$
\boxed{\operatorname{im}(\mathcal R\cap\ker E\to\mathscr C_{39})=\ker D.}
\tag{3}
$
这些响应同时杀原全部自然函数，故保持同一 $J^+$。本稿不再重算144列、39坐标、32像或其原核。

[R455](R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md) 的一个固定母 cap 有唯一镜对。经实际正宽 $w$ 输运后，写
$
u= h_w r_w,\qquad p=\pm s_w r_w,\qquad
r_w>0,\ h_w>0,\ s_w>0 .
$
镜点距中心为 $b_w>0$。原协变给
$
h_w=w^2h_0,\quad s_w=ws_0,\quad b_w=wb_0,\qquad
\kappa_{\rm cap}:=\frac{h_w}{s_w^2}=\frac{ur}{p^2}>0 .
\tag{4}
$
公共 profile 幅度不改变这些比值；它可以准确吸收入 $a_i,b_i$。
$\kappa_{\rm cap}$ 不是路径几何曲率。

设所研究的实际查询集含两个宽度 $w_1\ne w_2$；因 $s_0>0$，
$
s_1^2\ne s_2^2,\qquad h_j=\kappa_{\rm cap}s_j^2.
\tag{5}
$
每个宽度须包含下节指定的三个实际角色及八个不同完整 copy 中心。
各宽度仍可有任意其他角色与副本，全部使用同一个成本 $V$。

## 2. 三个真实 low 角色，不是三个自由矩输入

先固定一个宽度。原 R295 §§2–2.2 的最右正布局，
最后 $k=K-1$ 子块中最后 high 为 $j_H=L-7$，其前的
$
j_H-1,\quad j_H-2,\quad j_H-3
\tag{6}
$
都是 low。它们的 $R,T$ 完全相同，右侧 low 与其方向成比例。
对三者，所有更右的完整 cells 的二次矩加权和均为零。
所以其有效 suffix 都是同一个真实非零常数乘最后 high 的矩：
$
n_i=\lambda\,\mu_H,\qquad
\lambda=\epsilon_{K-1}B^2(4\sqrt2+3/2)\ne0.
\tag{7}
$
正幅、整块 g 翻号与复制权按 R456 §6 的原非零因子保留。

(7)使用完整 cell 的
$\sum R_i\mu_i=\sum T_i\mu_i=0$，
不是从八个 cubic 差分系数的交替号推二次闭合。
所选三个 low 均在完整 cell 的最右内部副本中；
其右侧没有遗漏的内部副本。这与 R456 所用角色是同一个实际来源。

令这个固定参考 cell 中的 high 矩为
$
\mu_H=m(1,\eta,\eta^2+\sigma^2),\qquad
m>0,\quad \sigma^2>0.
\tag{8}
$
这里
$
\sigma^2=
\frac{\int(x-\eta)^2(u_H'')^2+2\int(u_H')^2}{m}.
$
三个 low 的中心为不同的 $\xi_1,\xi_2,\xi_3$。
对整 cell 的平移 $t$，其矩输运准确为
$
n_i(t)=\lambda m(1,t+\eta,(t+\eta)^2+\sigma^2).
\tag{9}
$
三个 $n_i(t)$ 相同，**没有**假设它们本身是三个独立向量。

以 $\varepsilon=+1$ 表示左根、$-1$ 表示右根，其物理位置为
$x=t+\xi_i-\varepsilon b$，且 $p=\varepsilon sr$。
在此位置把(9)改写成
$
\frac{n_i(t)}{\lambda m}
=\bigl(1,\ x+\delta_{i,\varepsilon},
\ (x+\delta_{i,\varepsilon})^2+\sigma^2\bigr),
\qquad
\delta_{i,\varepsilon}=\eta-\xi_i+\varepsilon b.
\tag{10}
$
对每个固定方向 $\varepsilon$，三个 $\delta_{i,\varepsilon}$ 真实不同。

写
$
r^{-3}F(x,hr,\varepsilon sr,r;n)
=\sum_{j=0}^2n_j F_{j,\varepsilon}(x).
\tag{11}
$
各 $F_{j,\varepsilon}$ 的次数至多五。
原幅度归一仍是 R456(35) 的 $4\delta_{\rm copy}\gamma_{\rm copy}^7a_i^3r^3$；
这些因子非零，右锚和累计常数不改。

假定三个角色的两根都在至少八个原 copy 中心上为零。
每个角色的完整 $t$ 多项式次数至多七，故它先成为恒等式。
换成共同变量 $x$ 后，准确是
$
F_{0,\varepsilon}(x)
+(x+\delta_{i,\varepsilon})F_{1,\varepsilon}(x)
+\bigl((x+\delta_{i,\varepsilon})^2+\sigma^2\bigr)
F_{2,\varepsilon}(x)=0
\tag{12}
$
对 $i=1,2,3$ 成立。

对固定 $x,\varepsilon$，左边是 $\delta$ 的至多二次多项式。
三个真实不同的 $\delta$ 迫它恒零，其三系数依次给
$
F_{2,\varepsilon}=0,\quad
F_{1,\varepsilon}+2xF_{2,\varepsilon}=0,\quad
F_{0,\varepsilon}+xF_{1,\varepsilon}
+(x^2+\sigma^2)F_{2,\varepsilon}=0.
$
因此
$
\boxed{F_{j,+}(x)=F_{j,-}(x)=0
\quad(j=0,1,2),\quad\text{对全部 }x.}
\tag{13}
$

这是从实际 suffix 联动推出逐矩分量镜盲；没有在物理布局上另造 $n$。
若只有一条角色，不能直接使用(13)。

## 3. 完整十三列在两个宽度上的约束

由(13)，可以分别分析一个 $n_j$ 分量。
其六规范参数记为 $A_0,A_1,A_2,B_0,B_1,C_0$，并保七个旧列的完整系数：
$
F=F_{\rm can}
+z_0p^3+z_1p^2r+z_2xp^2r+z_3pr^2
+z_4xpr^2+z_5x^2pr^2+z_6S_7,
\tag{14}
$
$
S_7=2xp^3-5x^2p^2r+3x^3pr^2.
$
这些系数在两个宽度上是**同一批数**。
不能为每个宽度分别重选 $z$。

除 $r_w^3$ 后写
$
F(x,h_wr_w,\varepsilon s_wr_w,r_w)/r_w^3
=E_w(x)+\varepsilon s_w O_w(x).
\tag{15}
$
由 R456 的完整(7)，odd 的 $x^5,x^4$ 系数依次为
$2A_2/3,5A_1/3$。旧七列至多 odd 三次，因此镜盲先给
$
A_2=A_1=0.
\tag{16}
$
没有借用仅 principal 的次数。

此时 odd 三次为
$
O_{w,3}=-4(A_0+B_1)/3+3z_6.
$
镜盲给
$
z_6=4(A_0+B_1)/9.
\tag{17}
$
even 二次给
$
E_{w,2}=(3A_0+5B_1/2)s_w^2+B_1h_w/6-5z_6s_w^2 .
$
合(4)、(17)准确得到
$
\boxed{14A_0+(5+3\kappa_{\rm cap})B_1=0.}
\tag{18}
$
这条在两个宽度上相同，单独不能杀 $B_1$。

### 3.1 第一个真实宽度差：even 常项

完整 even 常项为
$
E_{w,0}
=(A_0+B_1/2)h_ws_w^2-C_0h_w/6+z_1s_w^2 .
$
两宽镜盲要求同一个 $z_1$ 满足
$
z_1=\kappa_{\rm cap}C_0/6
-\kappa_{\rm cap}(A_0+B_1/2)s_w^2 .
$
由(5)与 $\kappa_{\rm cap}>0$，得
$
\boxed{A_0+B_1/2=0.}
\tag{19}
$

### 3.2 第二个真实宽度差：odd 一次

odd 的一次系数仍要保 $S_7$ 中的 $2xp^3$：
$
O_{w,1}
=\{-2A_0-(1+\kappa_{\rm cap})B_1+2z_6\}s_w^2
+2C_0/3+z_4 .
$
代(17)，两个宽度给
$
\boxed{
-\frac{10}{9}A_0
-\left(\kappa_{\rm cap}+\frac19\right)B_1=0.
}
\tag{20}
$
若只保 $S_7$ 的最高 odd 项而漏掉 $2xp^3$，会得到错误的例外比值。

由(19)，若 $B_1\ne0$，(18)强迫
$\kappa_{\rm cap}=2/3$，而(20)强迫
$\kappa_{\rm cap}=4/9$，矛盾。
因此对每个原 $n_j$ 分量，
$
\boxed{B_1=A_0=0,\qquad A_1=A_2=0.}
\tag{21}
$
其 $c$ 系数只剩
$
\boxed{c_j(x)=C_0^{[j]}-2B_0^{[j]}x.}
\tag{22}
$
没有任何正 $\kappa_{\rm cap}$ 例外，也不要求两个宽度相距很大。

## 4. 同一个共同盲提升完成精确等式

将(22)代入 $D=c_0+xc_1+x^2c_2$，即得
$
D(\ker Eval_{\rm two\ widths})\subset\operatorname{Pol}_{\le3}.
\tag{23}
$

反向不能用分别的单宽右逆。R456(40)已给两个同一个 $\kappa_{\rm cap}$ 下的完整形式提升：
$
B^{(0)}=\frac{\kappa_{\rm cap}p^2r-ur^2}{6},
\qquad c(B^{(0)})=1,
$
$
B^{(1)}=(ur-\kappa_{\rm cap}p^2)
\left(\frac p2-\frac{xr}{6}\right),
\qquad c(B^{(1)})=x.
\tag{24}
$
它们是六规范代表加原七列，不是新定义的自由成本。
在每个实际宽度的两根都有 $ur=\kappa_{\rm cap}p^2$，故(24)准确为零。

任意 $d_0+d_1x+d_2x^2+d_3x^3$ 都可由
$
(d_0n_0+d_2n_2)B^{(0)}
+(d_1n_0+d_3n_2)B^{(1)}
\tag{25}
$
取得同一个 D 值。
这个提升对所有位置、所有宽度和所有 suffix 都盲，不仅对用于证明必要性的三个角色。

所以，追加任意其它同 cap 宽度、角色和副本也不改变结论：
$
\boxed{
D(\ker Eval_{\rm all})
=\operatorname{Pol}_{\le3},
}
\tag{26}
$
只要其中确实包含本稿两个宽度的 witness 组。

由(3)，完整 formal 评价商因而是
$
\boxed{
\frac{Eval_{\rm all}(\mathscr C_{39})}
{Eval_{\rm all}(\mathcal R\cap\ker E)}
\simeq
\frac{\operatorname{Pol}_{\le6}}
{\operatorname{Pol}_{\le3}}
\simeq\mathbb R^3 .
}
\tag{27}
$
不宣整个 actual 成本空间必映满这三维。

对任何满足(1)的具体原目标，其全部这些 ordered $\mathcal C$
可被同一个 signed whole-$E$ 零响应清掉，当且仅当
$
\boxed{D_4(V)=D_5(V)=D_6(V)=0.}
\tag{28}
$
充分性按原方式构造：用(25)取 $B_D$，使目标 current 减 $B_D$ 属于 $\ker D$；
原 R434 证书给同一个真实响应代表其负值。
(25)对全库盲，故一次消掉全部角色的有序余行。
该响应的完整 self partial 代价未被删除。

## 5. 从有限原值直接读取新增 D4

本节把(28)中的新增项写成确定的有限原查询，避免只报商维数。

首先，对三个角色各自的八个真实 copy 中心作 degree7 多项式插值。
按(10)把变量换成共同 $x$，再在三个真实不同 $\delta_i$ 上作二次插值，
即可准确恢复(11)的三个 pair 多项式。
所有归一系数来自已固定的幅度、cap 和真实 $\mu_H$；
不改变物理输入，不执行新的研究插值计算。

对某个恢复出的 $n_j$ 分量，在宽度 $w$ 定义(15)的
$E_w,O_w$。先从任一个宽度读取
$
A_2=\frac32[x^5]O_w,\qquad
A_1=\frac35[x^4]O_w .
\tag{29}
$
用 R456(7)的**完整**两个规范代表从两个宽度的 pair 同时扣去它们。
下面 $E_w,O_w$ 均指这个准确扣除后的值，不仅扣最高单项。

令
$
\Delta=s_2^2-s_1^2\ne0,
$
$
\begin{aligned}
L_*&=18\left(\frac{[x^2]E_1}{s_1^2}
+\frac53[x^3]O_1\right),\\
U_*&=
\frac{[x^0]E_2/s_2^2-[x^0]E_1/s_1^2}
{\kappa_{\rm cap}\Delta},\\
V_*&=
-\frac{[x]O_2-[x]O_1}{\Delta}
+\frac23[x^3]O_1 .
\end{aligned}
\tag{30}
$
逐项代(14)—(15)，所有旧 $z$ 与 $C_0$ 恰消，得到
$
L_*=14A_0+(5+3\kappa_{\rm cap})B_1,\quad
U_*=A_0+B_1/2,\quad
V_*=\frac{10}{9}A_0+\left(\kappa_{\rm cap}+\frac19\right)B_1 .
$
因此
$
\boxed{B_1=16U_*-\frac32L_*+\frac92V_*.}
\tag{31}
$
公式无 $\kappa_{\rm cap}-2/3$ 或 $\kappa_{\rm cap}-4/9$ 分母，覆盖全部正 cap 比值。

最后原三分量合成给
$
\boxed{D_4=A_2^{[0]}+2A_1^{[1]}-B_1^{[2]}.}
\tag{32}
$
$D_5,D_6$ 可继续用 R456 的真实高两项读出；
也可由已恢复的 $A_1,A_2$ 直接按原(10)取得。

(29)—(32)是一个有限线性读出，系数完全由同一真实库确定。
whole-$E$ 零响应改变其它低值时，它们准确保持 D 的三个值；
允许二阶 gauge 也不能改变原各 Af 点累计量。
这里不把全部单点值本身称为独立原观察。

## 6. 哪些实际库满足两宽前提

本稿所需完整条件只有：

1. 同一 R455 母 cap 的实际正宽 $w_1\ne w_2$，原最终形状保持这些 cap；
2. 每个宽度至少有原最后 high 前三个连续 low 角色；
3. 每个角色随完整 cell 有至少八个不同中心；
4. 所有更右完整 cells 的 R/T 三矩和准确为零；
5. 原幅度、g 翻号和共同右锚按 R456(34)—(35)保留。

在这些条件内，宽度之间的间距、relative centers、$\mu_H$ 大小与方差
都可以不同。证明不要求两个宽度的 suffix 向量彼此成比例；
它只在每个宽度内部使用三 low 共用同一个 high。

需要区分已经存在与可以新增：

- R280 §§3、7、8 使用一个共同母宽度，五个最终 block 是平移和正四次幅权。
  R324 §§6、8、9 保这套复制和同纤维结构；它本身不证明当前物理库出现两种不同宽度。
- R455 是从起点的新母库定理，保已经选定的实际宽度。
  它没有把上述两宽条件自动加到所有旧冻结对象。
- 因此若所问最终库实际只有一个宽度，应使用 R456 的准确二维商。
  不可为了应用本稿而移动冻结母或在解后重新伸缩部分 block。
- 如果一个确已给定的有限库包含本节两组，则本稿直接适用。
  不需额外假定右矩可独立指定，也无需新科学运行来检验旧整数编码。

## 7. 正仿射查询闭包中的用途

另有一种清楚不同的使用方式。若后继要将原 partial 查询扩成正仿射不变的有限函数值映射，
可以从起点固定一个共同合法窗口，包含所有 profile、右锚和待用 controls，
并在该窗口允许的一个非空开参数域内取共同正仿射输运。

只要其中有两种不同伸缩 $H_1,H_2>0$，同一个物理母库的两个**查询输运像**
就具有两种不同 $s^2$，且各保原三 low/high、copy 数、共同 $\kappa_{\rm cap}$ 和三矩闭合。
(26)—(32)随即适用于这个扩大的评价映射。
有限维性允许用有限忠实查询表示该闭包；本证明已经给出一组明确有限的检出数据。

这不是说原冻结圆本身有两套物理 profiles，也不是说必须同时嵌入两个新的首阶圆。
它说明：若真实成本控制的联合目标从起点加入这种 affine 查询闭包，
其响应商必须保留第三个系数 D4；不能沿用单宽两行商来省去它。

还必须另证这一新增联合映射的正成本锥、原型基准、
同一个固定有限词截面及合法窗口。
原 $J^+$ 截面没有免费支付新增 partial 闭包；
signed (28)也不替代实际实施。

## 8. 与完整 period 的关系

本稿没有把 universal natural 全零当背景，也没有把 self cap 当成单点局部多项式。
所处理的是原消-self 组合 $\mathcal C=RH_e+TH_d$，其局部形式由 whole $E$ 与全 ordered $\mathcal O$ 准确产生。

如果某个真实或 signed 原目标已经有 $D\equiv0$，本稿不再制造新的有序障碍：
(3)本身即可一次用响应清其全部 formal current，甚至不需先分镜点或宽度。
但这个响应可能改变剩余 self 通道，必须按同一成本保留其代价。

后继仍是同一实际母库的完整 self partial、所有简单 $p$ 零点的局部 inverse、
Af 点的已识别累计条件、平台仿射与 $k$ 值闭合及十三行共同规范。
本稿只关闭多宽 ordered 商中此前唯一未判的 D4，准确给出其真实有限读出与 signed 支付条件。
