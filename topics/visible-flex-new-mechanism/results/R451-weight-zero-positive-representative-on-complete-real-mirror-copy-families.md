# R451：零权正字符代表在固定真实镜对全部副本上的完整补偿及全根七次余量

日期：2026-11-16。**完整原式纸面证明；没有执行新的符号程序、profile、积分、rank、人工检查或科学运行。**

[R448](R448-nineteen-real-mirror-fluxes-and-the-complete-thirty-dimensional-self-remainder.md) 已确定原 49 维响应模块在一个实际非零曲率镜对上的完整 19 维像。本稿不再增加形式维数，而是把原正字符代表 $H_*$ 的**真实 self-cap 目标**放入这个像。

新的结论是：对一个固定物理宽度、一个实际 $u''\ne0$ 的镜对，存在同一个明确原响应 $W_*\in\mathscr M$，使 $H_*-W_*$ 在该镜对的**全部同宽对应副本**上 self partial 同时为零。不是分别在每一点选择成本，也不只是在十九个采样点插值后猜测其余点。加入原完整 cell 的真实 suffix 后，同一结论适用于对应角色的完整标量 $\eta$；其消-self 通道 $C$ 仍按原值保留。

证明的关键是一个完整输出身份：$H_*$ 的 self 中心次数至多八；减去一个对全部母、全部宽度共同的 $K_8$ 系数后，全部 $A_f$ 根的 partial 中心次数都降至七。其它根仍须由同一个三十维 blind 空间同时支付；本稿把其原目标缩为准确的七次系数，而不宣这些系数已经属于该响应像。

## 1. 固定原代表、真实库和共同右锚

沿 [R406](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md)，采用已经构造的原成本
$$
\begin{aligned}
H_*={}&C_2+\frac{649}{768}R_2-\frac{73}{3072}R_3
+\frac{649}{1536}R_4-\frac{821}{768}R_5\\
&+\frac1{64}R_7+\frac{187}{1024}R_9 .
\end{aligned}
\tag{1}
$$
$R_j$ 是 R126 的原 old-column 标签，$C_2$ 是原 static normal
$F_0(0,2,0,0)$。它们不是本稿新造的自由局部密度。已付身份为
$$
H_*\in U_0,\qquad E(H_*)=0,\qquad
\lambda_+(H_*)=1,\qquad
\Lambda_\cdot(H_*)=n_2 .
\tag{2}
$$

在 [R431](R431-common-exterior-degeneracies-in-the-complete-four-constraint-nineteen-target-library.md) 同一从起点选择的母库中，各实际母准确保持 R411 的四个 $q$ 系数，所以 $n_2$ 在它们的全部正仿射像上为零。R406 的完整 $n_2$ 是局部五次密度，故不同不交母的 ordered $3+2$ 系数也为零。因此
$$
\boxed{J^+(H_*)=0,\qquad J^+=(E,\mathcal A,\mathcal O).}
\tag{3}
$$
这里 $\mathcal A$ 只含原实际 self 与所需 ordered 查询，没有额外加入未经支付的辅助母 self。若从起点追加了其它已证明的有限完整目标，仍必须使用保持同一四约束、同一外 cap 和同一有限窗口的那个最终库。

记
$$
\Sigma_V(u)=V(u^2,0),\qquad
p=u',\quad r=u'',\quad t=u''',\qquad
A_u=6pt-2r^2 .
$$
对该实际包的左零 collar $\ell$ 及一个真实 $A_u$ 点 $x_\alpha$，定义
$$
\mathfrak h_{\alpha,u}(V)
=\int_\ell^{x_\alpha}p(x)\,[\Sigma_V(u)]''(x)\,dx .
\tag{4}
$$
这是完整原函数的累计值。一般 V 的平台修正须另保；在本文的 whole-$E$ 核中，原 self 左二次系数为零，所以(4)就是所用 self partial。$H_*$ 的 self 输出本身没有被宣告局部或左紧。

## 2. 原最低两层控制完整 self 的平移次数

令 $N$ 是原平移导子，真成本权满足
$$
N(U_\sigma)\subset U_{\sigma-1},\qquad
U_\sigma=0\quad(\sigma\notin[-9,3]).
$$
[R356 §§7—8](R356-lowest-two-full-self-weights-and-universal-total-flux-cancellation.md) 证明的是完整 self 输出身份
$$
\boxed{
\Sigma(U_{-9})=0,\qquad
\Sigma(U_{-8})\subset
\operatorname{span}\{\mathcal T_R,\ r^4\},
}
\tag{5}
$$
其中
$$
\mathcal T_R
=4J^2(r^2t^2)-4J(prt^2)-r^4,\qquad
J(F)(x)=\int_x^{r_*}F .
\tag{6}
$$
式(5)不是由总自然通量零倒推输出零。事实上 $\mathcal T_R$ 有真实非零的仿射左尾。

若 $u_c(x)=u(x-c)$，原同锚仿射输运给
$$
\Sigma_V(u_c)(x+c)
=\Sigma_{\exp(cN)V}(u)(x).
\tag{7}
$$
在合法共同右 collar 的开参数域中先使用(7)，再使用既有有限多项式身份；没有移动实际窗口去容纳一个非法输入。

由 $H_*\in U_0$，
$N^9H_*\in U_{-9}$，且 $N^{10}H_*=0$。所以(5)—(7)给
$$
\Sigma_{H_*}(u_c)(x+c)
=\sum_{j=0}^{8}\frac{c^j}{j!}\Sigma_{N^jH_*}(u)(x).
\tag{8}
$$
因此每个真实根的完整 partial
$$
h_\alpha(c)
:=\mathfrak h_{\alpha+c,u_c}(H_*)
=\sum_{j=0}^{8}\frac{c^j}{j!}
  \mathfrak h_{\alpha,u}(N^jH_*)
\tag{9}
$$
次数至多八。积分端、原 left constant 和所有 self history 都包含在(8)—(9)。

对一般 $V\in U$，同一原谱只能给
$\Sigma N^{12}V=0$，即完整 self 中心次数至多十一。不能把(8)推广到一个任意加入高权响应后的成本。

## 3. 八次系数的原两模板与同一个 K8 校正

由(5)，存在两个由原成本唯一确定的实常数 $\alpha,\beta$，使
$$
\Sigma_{N^8H_*}=\alpha\mathcal T_R+\beta r^4 .
\tag{10}
$$
它们对全部紧 profile、全部位置和宽度共同。唯一性也可直接从原锚看出：$\mathcal T_R$ 的左一次系数为
$-4\int r^2t^2$，非零实包时严格非零；$r^4$ 左尾为零。本文不另做新观察来求两个常数的数字值。

[R330(18)](R330-two-actual-packet-degenerate-fluxes-and-twenty-observation-control.md) 的完整同锚身份是
$$
2\mathcal T_R=-\frac13r^4-\frac23L_u\{P(u,u)\},
\qquad P(u,u)=J(r^2).
\tag{11}
$$
这里 $P(u,u)$ 有真实左常数，不能当紧输入。原全区间通量身份
$$
p\,L_u(w)''
=\partial_x\{A_u(pw''-rw')\}
\tag{12}
$$
对这个非紧 w 仍成立；左平端以及 $A_u(x_\alpha)=0$ 都使真实边项为零。

另外，两次保端分部给
$$
\int_\ell^{x_\alpha}p(r^4)''
=4pr^3t-\frac45r^5
=\frac8{15}r(x_\alpha)^5 .
\tag{13}
$$
由(11)—(13)，
$$
\mathfrak h_\alpha(\mathcal T_R)=-\frac4{45}r_\alpha^5,
\qquad
[c^8]h_\alpha(c)
=\frac{-4\alpha+24\beta}{45\,8!}r_\alpha^5 .
\tag{14}
$$
同一个归一系数作用于全部根，镜点的 r 相同，所以两镜点的归一最高项也相同。

现在取 [R435](R435-complete-local-self-currents-and-joint-actual-internal-flux-control.md) 的原轨道
$$
K_0=\frac13\mathcal B_P[P,S],\qquad K_n=\delta^nK_0,
\qquad NK_n=n(n-11)K_{n-1}.
$$
其完整 self 为 $\Sigma_{K_0}=-r^4/3$，故
$$
N^8K_8=8!\,\frac{10!}{2}K_0 .
$$
定义
$$
\boxed{\gamma_*=\frac{\alpha-6\beta}{8!\,10!}.}
\tag{15}
$$
直接用(10)—(11)得到完整函数身份
$$
\boxed{
\Sigma_{N^8(H_*-\gamma_*K_8)}
=-\frac{\alpha}{3}L_u\{P(u,u)\}.
}
\tag{16}
$$
因此
$$
\boxed{
\deg_c\mathfrak h_{\alpha+c,u_c}(H_*-\gamma_*K_8)\le7
\quad\text{对每一个真实 }A_u\text{ 根}.
}
\tag{17}
$$
这里没有除 p 或 r；即使 $r_\alpha=0$，(14)、(17)也有效。对这些根，$H_*$ 自己的八次系数已经为零。

(15)是一个共同的原成本系数，绝不是根据每个退化点另选一个 $K_8$。它也不需要将实际 profile 的第五矩非零作为假设。

## 4. 固定非零曲率镜对上的所有实际副本

把一个固定物理宽度吸收到实际偶 profile u 中，固定其一对真实根 $\pm b$：
$$
u(-b)=u(b)=u_*,\quad
u'(-b)=p_*,\quad u'(b)=-p_*,
\quad u''(\pm b)=r_*,
$$
$$
r_*\ne0,\qquad p_*\ne0,\qquad
s=p_*/r_*,\quad h=u_*/r_* .
\tag{18}
$$
它们是原冻结的根，不在证明中重新选位置。对应副本可写成
$\rho_i u(x-\xi_i)$，$\rho_i\ne0$。若原记号是
$U((x-\xi_i)/w)$，则(18)使用真实 $p_*=U'/w$、
$r_*=U''/w^2$、$b=wb_{\rm ref}$。

把(9)改写为实际根坐标 $x=c-b$ 或 $x=c+b$ 的两个多项式：
$$
P_-(x)=r_*^{-5}h_{-b}(x+b),\qquad
P_+(x)=r_*^{-5}h_b(x-b).
\tag{19}
$$
它们次数至多八，八次系数由(14)相同。

R448 给出同一个原 49 维成本空间 $\mathscr M$ 的准确镜对像
$$
\operatorname{ev}_{s,h}\mathscr M
=\{(P,\mathsf T P+Q):P\in\operatorname{Pol}_{10},
\ Q\in\operatorname{Pol}_7\}.
\tag{20}
$$
其中 $\mathsf T$ 由完整 K 左逆定义，保每个多项式次数和最高系数。
因此(19)满足
$$
Q_*(x):=P_+(x)-\mathsf T P_-(x)\in\operatorname{Pol}_7.
\tag{21}
$$

使用 R448 的全部原-source 右逆 $\mathscr K[P]$ 和 $L_0,\ldots,L_7$，
定义同一个完整响应
$$
\boxed{
W_*=\mathscr K[P_-]
+\sum_{j=0}^{7}[x^j]Q_*\,L_j .
}
\tag{22}
$$
它的系数由(1)、(4)、(19)和已付原右逆唯一确定。
也可以用原真实十九点读取(19)，因为(8)、(21)已经先证明了完整次数；并不是由十九个数值反推一个未证的函数身份。

由(20)—(22)，对于该镜对的每一个合法对应副本，
$$
\boxed{
\mathfrak h_{x_i^\pm,\rho_i u(\cdot-\xi_i)}(H_*-W_*)=0 .
}
\tag{23}
$$
真实值包含第五幅 $\rho_i^5$，不以归一值冒原 raw 值。

实际上(22)中 $K_9,K_{10}$ 系数为零，$K_8$ 系数恰为(15)，所以
$$
W_*=\gamma_*K_8+W_{\le7},\qquad
W_{\le7}\in\operatorname{span}\{K_0,\ldots,K_7,L_0,\ldots,L_7\}.
\tag{24}
$$
这使(17)在减去整个 $W_*$ 后，仍对所有其它根成立。

全部(22)成本来自 R443 的准确 53→85→144 原关系及 K 原轨道，且
$$
J^+(W_*)=0,\qquad C_{i,\alpha}(W_*)=0
\quad\text{对当前圆的全部包和根}.
\tag{25}
$$
又因为全部原响应自然函数为零，R406 的正字符因子化给
$\lambda_+(W_*)=0$。结合(2)—(3)，
$$
\boxed{
J^+(H_*-W_*)=0,\quad
\lambda_+(H_*-W_*)=1,
}
\tag{26}
$$
并有(23)的全部对应 self 门为零。
所以这些同镜对全部副本的 self 查询，仍不能使 $\lambda_+$ 下降。
这是同一真实 profile 库上的 signed 线性见证，不是把(26)称为实际路径。

## 5. 共同外 cap 允许使用全部最终内区修正母

R431 的最终最细母不必在内部一字相同。
不能仅凭相同的根 jets 就把其 self 目标替换成同一母。

这里使用 [R407](R407-connected-moment-fibers-fix-self-caps-and-retain-the-actual-total-fluxes.md) 的完整变分结论。
沿真实保持全部三矩的内区路径，极化二阶场
$Z(u,\dot u)$ 在两侧外区准确为零；whole $\mathcal Q=0$ 使
$\partial_t\Sigma_V(u_t)''$ 在共同两侧 cap 上为零。R431 已为其同一有限正常纠正/集中构造保留这些路径与外 cap。

故左根的(4)沿该路径不变。右根使用
$$
\int_\ell^{r_*}p\,\Sigma_V(u)''
=\int_\ell^{r_*}t\,\Sigma_V(u)
\tag{27}
$$
再从右 cap 读取。对 $H_*$，实际端点母的四 q 条件给(27)为零；
对任一 $W_*\in\mathcal R$，它对全部紧母本来为零。
于是两侧 partial 都等于同一共同参考母的准确 cap 值。

因此(23)也覆盖同一个 R431 共同 cap、同三矩连通构造中的所有最终内区修正母，只要比较的是同一个物理宽度和同一个外部根角色。
没有把 R407 推广到不连通纤维，也没有把参考母换成另一个三矩不同的 bump。

## 6. 完整 suffix、两 period 通道与对应 cell

保原完整 raw 两通道及其组合
$$
\begin{aligned}
H_{d,i,\alpha}(V)
&=a_i^3\{R_i\,s_{i,\alpha}(V)+\mathcal K_{V,n_{R,i}}(x_{i,\alpha})\},\\
H_{e,i,\alpha}(V)
&=-a_i^3\{T_i\,s_{i,\alpha}(V)+\mathcal K_{V,n_{T,i}}(x_{i,\alpha})\},\\
C_{i,\alpha}(V)&=R_iH_{e,i,\alpha}(V)+T_iH_{d,i,\alpha}(V),
\end{aligned}
\tag{28}
$$
其中 $s$ 是(4)，$R_i=a_i^2-b_i^2,T_i=a_ib_i$，
$n_{R,i},n_{T,i}$ 是后方全部真实包的三矩累计。
没有把它们换成裸 cell 均值。

不除可能为零的 $R_i$，定义
$$
\eta_{i,\alpha}(V)
=\frac{R_iH_{d,i,\alpha}-T_iH_{e,i,\alpha}}
 {a_i^3(R_i^2+T_i^2)}
=s_{i,\alpha}
+\frac{R_i\mathcal K_{n_R}+T_i\mathcal K_{n_T}}
 {R_i^2+T_i^2}.
\tag{29}
$$
只有在 C 已零时，清 $\eta$ 才等价于同时清两条内部通道。

[R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md) 的完整 ordered current 在一个固定 Af 根、固定 n 下，显式位置次数至多五，且对 n 线性。
真实三矩的共同平移是
$$
\begin{pmatrix}\mu_0\\\mu_1\\\mu_2\end{pmatrix}
\longmapsto
\begin{pmatrix}
\mu_0\\ \mu_1+c\mu_0\\
\mu_2+2c\mu_1+c^2\mu_0
\end{pmatrix},
\quad
\mu_2=\int(x^2r^2+2p^2).
\tag{30}
$$
故完整对应布局的 suffix 项位置次数至多七。

为准确应用这个界，取 R397/R435 的一个固定完整 cell 角色及其共同宽度对应副本。该 cell 含原全部最细 R/T 编码，原
$\sum R_i\mu(u_i)=\sum T_i\mu(u_i)=0$ 已逐实际三矩成立。
后续完整 cell 的贡献因此为零，当前角色的剩余 suffix 由同一个内部布局按(30)输运。
外幅平方进入 suffix，外槽三次幅进入 current，合为与 self 同一个第五幅。
若整个 g 副本反号，$T_i,n_{T,i}$ 同时反号，所以(29)中的该项不变。
这才给同一角色的真实多项式；不能对任意散选的包假设 suffix 都相同。

因此(19)中用完整 $\eta(H_*)$ 替代 self 后，两侧仍是次数至多八、共同八次项的多项式。
用(22)的同一原右逆重新定义 $W_*^\eta$，得到
$$
\boxed{
\eta_{i,\pm}(H_*-W_*^\eta)=0
\quad\text{对该角色全部同宽对应副本},
}
\tag{31}
$$
并仍有(25)—(26)。它对 C 完全没有代价，但也不改变原 $C(H_*)$。

特别：

- 完整 cell 的末包有 $n_R=n_T=0$，故原 C 已零，(31)清两条完整内部通道。
- 完整 cell 的首包有
  $(n_R,n_T)=(-R_i\mu_i,-T_i\mu_i)$，原 C 同样为零；这时(29)保留 self 与本包三矩 current 的真实差，不把它删成裸 self。
- 内部其它角色的 C 不因此为零。需原实际 C 联合前提，不能由(31)替代。

以上是同一角色所有副本的函数身份，不要求为了证明而改变真实中心。
不同角色可有不同 suffix 多项式；不能为每个角色分别取 $W_*^\eta$ 后宣成一个共同成本。

## 7. 全部其它真实根的剩余目标已缩为七次

固定上面一对参考根并取同一个 $W_*$ 或 $W_*^\eta$。
由(17)、(24)和 R448 原完整局部 current，所有其它 Af 根的剩余 self 中心次数至多七；加入同一对应角色的真实 suffix 后仍至多七。

其准确 self 系数可直接写为原原型读出
$$
b_{\alpha,j}(w)=
\frac1{j!}\int_{\ell_w}^{x_{\alpha,w}}
u_w'\,[\Sigma_{N^j(H_*-W_*)}(u_w)]'',
\qquad 0\le j\le7 .
\tag{32}
$$
这里 $u_w(x)=U(x/w)$ 使用真正物理宽度；若清的是(29)，再加 R433 原 $\mathcal K$ 和(30)给出的对应七次系数。
没有把(32)替换成 $n_2$ 的十二项密度。后者只决定完整总积分，不决定本段 cap。

R448 的三十维 blind 空间有确定原-source 投影
$$
\Pi_0C=C-\mathscr K[f_C^-]
-\sum_{j=0}^7[x^j]\{f_C^+-\mathsf Tf_C^-\}\,L_j .
\tag{33}
$$
它在所选参考镜对全部对应副本上都为零。
由原列 $V_i$ 的显式 x 次数至多七，(33)的生成列也只需 $K_0,\ldots,K_7$ 和原 $V_i$；因此它们在其它每个根的真实值也至多七次。

于是剩余任务可在每个实际宽度、每个其它共同外根上，比较(32)的八个原 cap 系数与(33)同一个三十维成本空间的八个系数。
当一个对应角色具有至少八个不同实际中心时，普通 Vandermonde 单射使该系数条件与该角色全部真实副本条件完全等价。这里没有新增 rank 计算。

本稿没有证明这些剩余向量已经在三十维像内，也没有证明某一向量在像外。
已经完成的是：原 $H_*$ 目标的八次公共部分由一个共同 $K_8$ 准确支付；全部参考镜对副本由一个原成本准确支付；其余全根不再留下未知的八至十一次位置项。

### 7.1 r 零根与不同宽度

在 $r_\alpha=0$ 的实际简单根，$p_\alpha\ne0,t_\alpha=0$。
(14)已给 self 目标次数至多七，但 R448 的 $r\ne0$ 十九维逆不能用于它。
R452 的独立纸面结论给这些镜点的原像为六个左系数与三个右系数；
若采用其完整 $\mathsf T_5$，准确多余条件是左六、七次两系数，
以及扣左逆后的右三至七次五系数。本文不称这七个原值已零，也不预设其非零。

不同真实宽度时，(15)仍是同一个 universal 系数；
但(22)的低七次右逆使用该宽度的真实 $(s,h)$。
分别对不同宽度构造的补偿不能自动合成一个成本，须使用(32)—(33)的共同矩阵。

## 8. 先付 C 或升级 actual 时不能偷换作用域

若原 C 已由一个 $R_C\in\mathcal R\cap\ker E$ 响应支付，新的基线是 $H_*-R_C$。
只有在 $R_C$ 是原真权零成本，或已有单独证明其相关八次项也按(14)统一，才可直接复用本稿的完整次数论证。
任意混权响应可能含正权，原谱只给 self 至多十一次；不能因为它属于 $\mathcal R$、自然函数全零，便把它的内部 cap 次数也置零。

本稿的(26)、(31)给一个准确 signed 核见证，说明原正字符不经这些有限真实查询下降。
它没有单独证明增强全部 copy / 全部根观察的原响应等像，也没有把十九行实际截面延长为任意多行实际截面。
R448 已付的十九行 actual $C^1$ 截面继续有效；加入更多行时，须在同一观察商上保全部正字符、原型基准、两次校正及共同合法窗口。

特别，原 prototype 与 whole-$J^+$ 后校正本身可产生其它内部值。
这些值必须放入同一个有限实际方程，不能把每个 signed $W$ 当成零基准路径。
原一般 $w_\theta$ gauge 也不改变这些 Af 通量，不能用 gauge 绕过剩余目标。

## 9. 只有一对根的母与四个 q 约束尚不能拼接

[R410 原完整稿](https://github.com/Rogerhu12/math-research-public/commit/8581b007d3a1b4b8d310f2bd8047676e66ff619a) 给了 $M_5=0$、严格单峰、恰一对 Af 根的新母及十九个完整目标。
它只强制 R411 的最高系数 $q_0=0$，没有强制 $q_1,q_2,q_3$。

R411 的四系数零构造则先用四个半径处的两种原型及镜像，获得真实四维正核，再作正解析逼近和有限四根纠正。
这证明四约束零流形存在正解析 regular 点，但没有证明该点只有一对 Af 根。
R412/R431 只需有限多个简单根；R431 此后固定全部外根邻域，中心有号集中不再新增根，却也不会删除既有外根。

因此不能把 R410 的一对根母与 R411 的 q 四根母视为同一个母。
准确的新构造门是：在“正偶、单峰、恰一对简单 Af 根”的同一个开形状类内，找到
$$
q_0=q_1=q_2=q_3=0
\tag{34}
$$
的真实 regular 点，且四个正常方向能在保护根之外使用。
若还需共同 D、E 与从起点的 $F^\star$，其 restricted 最大秩和随后的十九或二十根也必须在这个同一点重建。
一个一般解析母上 Dq 满秩，或在 $M_5=0$ 上单个正常方向非零，都不足以证明(34)在该开形状类非空。

本文既不证明(34)不可能，也不借两份独立构造宣布它已经成立。
若将来这个真正共同构造闭合，并保(18)的非零 r，且同一 actual C 前提也闭合，本稿的一个镜对全部副本结论才可以覆盖该母的全部 Af 根。
在此之前，全部其它根仍按第7节保留原真实目标。

## 10. 已闭结果与下一原来源

本稿的核心是(16)、(22)、(31)：它们从原完整 U 的最低层、真右尾和一个固定正字符代表出发，给出了具体原目标在 49 模块中的一段准确像，而非再次增加形式方向数。

仍未将整个 $H_*$ 的 all-root cap 写成单点二阶 jets 多项式。
R433 的局部性是 ordered current 的结论；R446 的 self 局部性是原 144 联合核的结论；两者都不能未经证明移到 $H_*$。
所以不能用“H* 真权零”再推 r 零根的 self 次数至多三，或直接删掉(32)的高次系数。

若第7节的同一目标确实超出三十维余像，下一合法原来源是尚未并入此 49 模块的完整响应，例如原 $\Theta_{71}(\ker\Pi_{71})$ 的外部项；不是再把原已付 144+K 的生成上界说成全部 $\mathcal R$。
本稿不执行该新映射，也不将未做的像比较列为已成功。

已经冻结的母、实际中心和宽度、原 ordered totals、C 与同一个十三行规范系统均保持其原范围。所有新判断只使用已付原式和本文的纸面分部、谱与多项式恒等，没有任何新增科学费用。
