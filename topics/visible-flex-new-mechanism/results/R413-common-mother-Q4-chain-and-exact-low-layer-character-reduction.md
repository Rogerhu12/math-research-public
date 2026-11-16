# R413：共同母库的 Q4 查询四链与增强负权正性的完整低层归约

日期：2026-11-16。**纸面证明；没有执行新的 profile、求积、符号程序、秩、原根、人工检查或科学运行。**

[R411](R411-positive-analytic-mothers-blind-to-the-weight-zero-natural-affine-orbit.md) 已构造真紧正解析偶母，使完整零权自然函数 $n_2$ 的整个正仿射轨道为零。本稿增加一个可以从同一起点保留的严格开条件，并精确分析**共同母库**的 Q4 查询，而不把多个逐母结论拼成一个未经证明的联合结论。

新结果如下。可以同时取 $n_2$ 仿射全零及 $D-E>0$；若全部最终母保持同一非退化 $D:E$ 比例，则 whole $E$、全部这些母的仿射自然查询及全部不交有序 $3+2$ 查询上的 Q4 像恰是一条四链，唯一平移头在权 $-2$。因此增强权 $-6,-4$ 的任何实际正字符，必在完整最高几何导数层上为零。它的全路径正性准确化为：**同一个由原静态 cocycle 唯一确定的八矩乘子下，一个静态标量和一个速度二次矩阵逐态非负。**

这没有排除该低层正字符。原 $F_0$、三个 $\widehat Q_2$、原 $N_0,N_2,\Gamma$ 及全部真实边界仍须求值；旧 pure/self 响应等像不删除新增自然像。本稿不宣布 actual 联合截面已经完成。

来源：[R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)、[R163](R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md)、[R164](R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md)、[R323](R323-full-pure-self-cone-and-complete-negative-weight-response-control.md)、[R382](R382-universal-cancellation-of-the-corrected-H-total-flux-and-independent-Q4.md)、[R386](R386-complete-quartic-velocity-natural-flux-and-a-new-mixed-direction.md)、[R393](R393-nine-dimensional-natural-Q4-affine-image-and-two-character-heads.md)、[R406](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md)及 R411。

## 1. 完整自然函数与三个不同的联合范围

保持原共同右 collar、真实成本空间 $U$、响应空间 $\mathcal R$ 及
$$
E=(\pi,\mathcal Q).
$$
$\mathcal Q$ 是 universal 左二次 self 函数，不是整个 self 输出。自然读出仍为原
$$
\Lambda_u(V)=
\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
\tag{1}
$$
有序三矩尾 $\mathscr G$ 与正式 pure 的规范保持原样。式(1)杀全部真实 $\mathcal R$。

对偶紧母 $u_i$，可以取全部合法正仿射输入
$$
C_{a,c}u_i(x)=u_i((x-c)/a),\qquad a>0.
$$
同时可加入不交实紧输入 $v,w$ 的有序系数
$$
\mathcal O_{v,w}(V)=[s^3t^2]\Lambda_{sv+tw}(V),\qquad
\operatorname{supp}v<\operatorname{supp}w .
\tag{2}
$$
这里 $s,t$ 是实幅度变量，非几何坐标。加入一个有限母库及所需有限有序查询的完整正仿射闭包后，得到有限维实际映射
$$
J(V)=(E(V),\mathcal A(V)).
\tag{3}
$$
有限性来自 $U$ 已有有限维性；不把查询标签数称为秩。其核在原正仿射作用和有限真权投影下稳定。有序函数的仿射输运保同一个真实右锚。

下面须区分：

1. 单个母的全仿射查询；
2. 多个母的共同全仿射查询；
3. 在第2项上再加(2)。

第1项不自动推出第2项；第3项只在已证明的局部层上可作简化。对完整 $F_0,Q_2$，本稿不假设(2)为零。

## 2. R411 母可同时满足一个严格的 C2 开条件

记
$$
p=u',\quad r=u'',
$$
以及 R393 的两个同权函数
$$
D(u)=-\frac12\int p^2r^3+\frac12\int xpr^4
-\frac3{20}\int x^2r^5,
$$
$$
E_5(u)=-\frac12\int xpr^4+\frac7{20}\int x^2r^5.
\tag{4}
$$
本稿以 $E_5$ 区别此函数与联合映射 $E$；它就是 R393 表中的 $E$，下标不表示新的成本权。

R411 的真平移系数 $q_1$ 为
$$
q_1(u)=-\frac14\int ur^4-\int p^2r^3
+\frac{15}{8}\int xpr^4-\frac{63}{80}\int x^2r^5.
$$
直接按四个完整局部积分合并：
$$
\boxed{
D-E_5-\frac{40}{63}q_1
=\mathcal J(u):=
\frac1{126}\int(20ur^4+17p^2r^3-24xpr^4).
}
\tag{5}
$$
这不是 principal 关系；全部泛函均连续于 $C^2$。

对 R411 的非负偶分段二次原型
$$
u(x)=
\begin{cases}
(ab-x^2)/2,& |x|\le a,\\
a(b-|x|)^2/[2(b-a)],&a\le|x|\le b,\\
0,&|x|\ge b,
\end{cases}
\qquad 0<a<b,
$$
中心区 $p=-x,r=-1$，(5)的被积式为 $20u+7x^2>0$；两外区有 $u\ge0,r>0,xp<0$，三项均非负且不全为零。因此
$$
\mathcal J(u)>0.
\tag{6}
$$
这仍只是原型积分。用 R411 的非负偶真紧 mollifier 得到实际光滑母时，$p,u$ 一致收敛，$r$ 在每个有限 $L^m$ 中收敛且一致有界、支撑共同有限，故(6)保留。其 $M_5$ 两个严格号也按原证明保留。

若 $v$ 偶，则 $\int v'(v'')^4=0$。因此(5)中唯一显式坐标项在平移时所加的常数倍积分为零，准确有
$$
\mathcal J(v(\cdot-c))=\mathcal J(v).
\tag{7}
$$
R411 的十六个不交实际包因局部五次性按第五幅权相加。所有幅权严格正，所以其真四根母 $u_*$ 满足 $\mathcal J(u_*)>0$。再作原 $\psi_3$ 正多项式逼近与同一四变量 IFT，充分小的 $C^2$ 误差保留这一严格号。

最终四个 $q_j$ 全零，特别 $q_1=0$，于是
$$
\boxed{
n_2(C_{a,c}u)=0\quad\forall a>0,c,\qquad
D(u)-E_5(u)=\mathcal J(u)>0.
}
\tag{8}
$$
这里只增强 R411 的起始母选择，不改动已发表的原结论。任一后继同点构造若从起点允许有限连续 $C^2$ polynomial 观察，可以把 $D,E_5$ 纳入其观察纤维；不得在一套已经冻结的母库上无偿改变这些值。

## 3. 完整 Q4 的平移像：单母四链

R393 用九个完整函数
$$
(A,B,C,D,E_5,F,G,H,K)
$$
呈示 Q4 自然像。其原真权依次为
$$
-7,\ -6,-6,\ -5,-5,\ -4,-4,\ -3,\ -2.
$$
对 $L=p-xr$，例如 $F=\int L^4u'''$、
$H=\frac14\int rL^4$、$K=\frac15\int L^5$。
R393 的完整平移作用为
$$
NA=0,\quad NB=-2A,\quad NC=8A,\quad
ND=-3B,\quad NE_5=3B-C,
$$
$$
NF=-4D,\quad NG=4D/3-2E_5,\quad
NH=F/2-3G,\quad NK=-4H.
\tag{9}
$$
本稿不重新计算该九维原式或其秩。

取(8)的偶母。由 $M_5=0$ 及奇偶，
$$
A(u)=B(u)=C(u)=F(u)=G(u)=K(u)=0.
$$
记 $D_0=D(u),E_0=E_5(u),H_0=H(u)$。沿真实平移，(9)逐次积分给
$$
\boxed{
\begin{aligned}
D(u_c)&=D_0,& E_5(u_c)&=E_0,\\
F(u_c)&=-4D_0c,&
G(u_c)&=(4D_0/3-2E_0)c,\\
H(u_c)&=H_0+3(E_0-D_0)c^2,&
K(u_c)&=-4H_0c-4(E_0-D_0)c^3 .
\end{aligned}}
\tag{10}
$$
全部 $A,B,C$ 平移值仍零。因为 $D_0-E_0>0$，各权 $-5,-4,-3,-2$ 的像都非零而各只有一维。正缩放区分四个真权，所以这四维不是只在一个中心的采样下界。

更准确地，(9)在此商中是一条连续的四链：$N$ 从权 $-2$ 到 $-3$、从 $-3$ 到 $-4$、从 $-4$ 到 $-5$ 均非零。因此
$$
\boxed{
\dim \mathcal A_u(\mathscr A_4)=4,\qquad
\text{唯一非零平移头在权 }-2.
}
\tag{11}
$$
权 $-6$ 的像本身为零；权 $-4$ 的像非零，但它已经是 $N$ 像，不能把二者混说。

## 4. 共同母库的准确差矩阵，以及何时出现额外头

现取有限个偶母 $u_1,\ldots,u_m$，每个都满足 $M_5=0$，并设
$$
\mathbf d=(D(u_i))_{i=1}^m,\qquad
\mathbf e=(E_5(u_i))_{i=1}^m,\qquad
\mathbf h=(H(u_i))_{i=1}^m.
$$
假定 $\mathbf d-\mathbf e\ne0$，并记
$$
r=\operatorname{rank}(\mathbf d,\mathbf e)\in\{1,2\}.
$$
由(10)，共同 Q4 像各权的维数准确为
$$
\begin{array}{c|cccc}
\text{真权}&-5&-4&-3&-2\\ \hline
\text{维数}&r&r&1&1 .
\end{array}
\tag{12}
$$
权 $-5$ 的两列是 $\mathbf d,\mathbf e$；权 $-4$ 的两列是
$-4\mathbf d$ 与 $4\mathbf d/3-2\mathbf e$，这个两列变换可逆。权 $-3,-2$ 各只有原 $H,K$ 一个生成函数，且其二次、三次项由 $\mathbf e-\mathbf d\ne0$ 保证非零。

从权 $-4$ 到 $-5$ 的 $N$ 像满；从 $H$ 到权 $-4$ 的像则只有
$$
6(\mathbf e-\mathbf d)c.
$$
所以
$$
\boxed{
\dim\mathfrak h_{-4}=r-1,\qquad
\dim\mathfrak h_{-2}=1,
}
\tag{13}
$$
其余平移头全零。特别，各母各自满足 $D-E_5>0$ **不够**推出共同权 $-4$ 头消失；若两向量不成比例，(13)仍有一维新头。

若从起点令所有母保持共同 $D_0,E_0$，或保持同一非一比例 $E_5=\rho D$，且 $\mathbf d-\mathbf e\ne0$，则 $r=1$，共同像仍恰为(11)的四链。实际幅度和正伸缩分别使两函数共同乘第五幅权与同一缩放因子，因为它们具有同一真权；原包中心已在全仿射查询里。因此不同实际宽度、幅度和位置不改变这个比例条件。

如果某母是共同初始母的同 $F^\star$ 变形，加入 $D,E_5$ 必须作为**从起点规定**的两个连续 $C^2$ 观察。这是对允许任意有限此类观察的后继定理的条件应用，不在本文替代其最大秩、十九个根或临界点论证。

## 5. 有序 3+2 查询对这一层准确为零

R386 的完整 Q4 自然公式是
$$
\Lambda_u(\mathcal Q_S[\gamma,\delta])
=-\frac1{32h^8}\int
\{1+(hx+d)^2\}
[\gamma u'-(\gamma x+\delta)u'']^4u'''.
\tag{14}
$$
它是一个真实局部五次泛函，已包含全部原 pure 与 Green 补偿，没有待定尾余项。

若 $v,w$ 的实际支撑不交，则(14)准确等于
$$
\Lambda_{sv+tw}(\mathcal Q_S)
=s^5\Lambda_v(\mathcal Q_S)+t^5\Lambda_w(\mathcal Q_S).
$$
故
$$
\boxed{\mathcal O_{v,w}(\mathcal Q_S)=0.}
\tag{15}
$$
所有 affine 输运后的不交查询也如此。于是，在第4节共同比例条件下，加入任意有限个这样的有序查询及其共同 affine 闭包，仍不扩大 Q4 的四维像或其头部。

(15)只属于这个已证明局部的层。它不删除完整 $U$ 中的有序 $3+2$ 读出，不把 $F_0,Q_2$ 的 primitive 当作局部函数，也不宣称所有实际 mixed period 只由 self 决定。

## 6. 两个候选负权字符在完整最高层上必须为零

令 $J$ 是(3)的共同映射，并满足第4节的比例条件。取 $\sigma=-6$ 或 $-4$，设 $\lambda$ 是经 $J$ 下降的、杀 $\mathcal R$ 的单权平移不变泛函。此时尚不需要正性。

R323 已付
$$
E(U_\sigma)=E(\mathcal R_\sigma).
\tag{16}
$$
所以若 $V\in U_\sigma$ 的全部新增自然查询为零，可选同权 $R\in\mathcal R_\sigma$ 使 $E(V)=E(R)$。自然查询又杀响应，故 $J(V)=J(R)$，于是 $\lambda(V)=0$。换言之，本权 $\lambda$ 对每个子族的作用只取决于它的**新增自然查询像**，不能受旧 E 坐标额外污染。

由 R350、R382，完整三加速度平方族及两个更正后 H 族的全部自然函数为零，故
$$
\lambda(\bar A_{hh})=\lambda(\bar A_{hk})
=\lambda(\bar A_{kk})=\lambda(H_1)=\lambda(H_2)=0.
\tag{17}
$$
这里各式在全部实际状态上成立，$\lambda$ 自动取相应真权。

Q4 在本共同查询商中没有权 $-6,-4$ 平移头，(11)—(15)及 $\lambda N=0$ 因而给
$$
\lambda(F_{4,i}(S))=0\quad(0\le i\le4,\ S\text{ 任意}).
\tag{18}
$$
综合：
$$
\boxed{
\lambda\text{ 杀完整几何导数权四的全部正规式。}
}
\tag{19}
$$
本式保原 $P_3$ 零端势；不能把它改写成单独 raw $v_4$ 为零，或漏掉原 $\mathcal B_{m_2}N_2$。

若不付第4节的共同比例条件，(18)对权 $-4$ 一般不成立；剩余一维头的 Q4 action仍为 R393 的
$-c\gamma^2\{\gamma^2+(d\gamma-h\delta)^2\}/(32h^8)$。

## 7. 全路径正性现在等价于一个静态标量与一个二次矩阵

保持 R130/R163 的同一归一化
$$
F_0=L_0-\Gamma(m_0),\qquad
\widehat Q_2=\operatorname{IBP}(L_2)-\Gamma(m_2),
$$
$$
L_2=v_2-\mathcal B_{m_0}N_2-\mathcal B_{m_2}N_0.
\tag{20}
$$
两端常值 germs 上 $P_1,P_3$ 都为零，即使起末状态不同也成立。

假定第6节的 $\lambda$ 还是实际正字符。R140 给同一个规范化八矩乘子 $\mu$，对所有原真实开平端水平路径
$$
h>0,\qquad \omega_s=k_s/(2h)
$$
有
$$
\int\{\lambda F_0-\mu m_0+
\lambda\widehat Q_2-\mu m_2\}\,ds\ge0.
\tag{21}
$$
(19)已准确清掉其完整四阶导数层，而不是以慢路径近似它。

定义
$$
A_\lambda(S)=\lambda F_0(S)-\mu m_0(S),\qquad
B_\lambda(S;\nu,w)
=\lambda\widehat Q_2(S;\nu,w)-\mu m_2(S;\nu,w).
\tag{22}
$$
固定任一实际平端形状，把时长乘 $a>0$。R140 的原时间缩放给
$$
a\int A_\lambda+a^{-1}\int B_\lambda\ge0
\quad\forall a>0.
$$
所以两项积分分别非负。常状态段于是给 $A_\lambda(S)\ge0$。

对任一固定状态 $S_0$，取紧支光滑速度
$(h_s,k_s)=\varepsilon(\nu,w)\psi$，按原方程积分 $\omega_s$。两端为真常值 germs，允许不同末状态；当 $\varepsilon$ 足小时 $h>0$。将 $\int B_\lambda\ge0$ 除以 $\varepsilon^2$ 并令其趋零，得到
$$
B_\lambda(S_0;\nu,w)\int\psi^2\ge0.
$$
故 $B_\lambda(S;\cdot,\cdot)$ 的真实对称 $2\times2$ 矩阵逐状态 PSD。

反过来，若同一 $\mu$ 满足这两个逐态条件，则(21)直接成立；连同 $\lambda(\mathcal R)=0$，R140 给真实闭成本锥上的非负性。因此
$$
\boxed{
\lambda\ge0\text{ 于原实际成本锥}
\iff
\exists\text{同一个 }\mu:
A_\lambda(S)\ge0,B_\lambda(S)\succeq0
\quad\forall S .
}
\tag{23}
$$
此等价仅在(19)已经支付的本查询商/本两权范围内。没有把一般含四次层的正性错误拆成逐层点态非负。

## 8. 乘子不是八个额外自由参数

R164 的真实八矩缩放生成元是
$$
R_D=\operatorname{diag}(-1,0,1,-3,-2,-2,-1,0)
$$
，对应原次序 $(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$。设八参考状态与坐标为原 $S_i^*,a_i(M)$，定义
$$
\mathfrak c_D(M)=
\sum_i a_i(M)
[(h\partial_h-\omega\partial_\omega)F_0(S_i^*)],
$$
$$
\mathfrak c(M)=
\sum_i a_i(M)[\partial_\omega F_0(S_i^*)].
\tag{24}
$$
任一实际可行乘子必须满足
$$
\mu R_D=\sigma\mu+\lambda\mathfrak c_D,
\qquad
\mu R_N=\lambda\mathfrak c.
\tag{25}
$$
对 $\sigma=-6,-4$，$w_j-\sigma$ 全非零，故
$$
\boxed{\mu_j=\frac{\lambda\mathfrak c_D(E_j)}{w_j-\sigma}.}
\tag{26}
$$
两组分母依原次序为
$$
\begin{array}{c|cccccccc}
\sigma=-6&5&6&7&3&4&4&5&6\\
\sigma=-4&3&4&5&1&2&2&3&4 .
\end{array}
\tag{27}
$$
仍须保(25)的平移式；不把形式解(26)自动当作可行乘子。R164 证明可行乘子在这些权唯一；本稿不在不同路径、不同状态或不同层之间重新选它。

由原 cocycle与该协变，(22)的静态标量及完整二次型享有同一缩放、平移规律。也可只在积分层应用协变，再按第7节的常路径及小速度唯一性逐态恢复。因此可写成
$$
A_\lambda(h,k,\omega)=h^\sigma a_\lambda(k),
$$
$$
B_\lambda(h,k,\omega;\nu,w)
=h^\sigma
\left\{
b_\lambda(k)(\nu/h)^2+
c_\lambda(k)(\nu/h)w+
d_\lambda(k)w^2
\right\}.
\tag{28}
$$
此处 $\nu=h_s,w=k_s$，未改水平条件。于是(23)等价于
$$
a_\lambda(k)\ge0,\qquad
\begin{pmatrix}
b_\lambda(k)&c_\lambda(k)/2\\
c_\lambda(k)/2&d_\lambda(k)
\end{pmatrix}\succeq0
\quad\forall k\in\mathbb R,
\tag{29}
$$
并保原(25)及原函数关系。式(28)不是删除 $\omega$ 原历史，而是同一个完整成本、同一 $\Gamma$ 与同一乘子共同相消后的协变结论。

## 9. 真正尚需消费的低层与已付输入

本稿没有证明(29)只有零解。剩下的原对象明确是(20)及其三速度系数，含全部 $N_0,N_2$、参考减项及 $\Gamma(m_2)$；不是重做 A/H/Q4。

已发表 [R207](R207-complete-weight-minus6-pure-image-equals-three-dimensional-response.md) 与 [R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md) 的公开 stdout 给全部十四族原 pure 列的准确响应坐标。它们不是只有维数；但当时新增的是 pure 收缩，不能将其 pure 原列冒充已经保存的完整 mixed 正常根。

若后继确需执行，最小新增对象应是所缺低层的完整 self/natural 收缩。可复用原完整静态、$v_2$、$N_0,N_2$ 与已付 pure 响应坐标；对必要势只新增
$\mathcal B_E(N)(u^2,0)=2N(E(u,u);u,u)$ 的原外槽收缩，随后取得真实同锚 $\Omega$ 并作既定 pure 校正。不需重做旧 pure 像、旧秩、旧响应表或完整两 mode 的其他目标。未归约的多字或真尾仍只能报告 unresolved，不能凭有限母值替代普遍关系。

本稿已准确支付(8)、共同差矩阵(12)—(13)、局部有序零式(15)、最高层消去(19)以及完整正性等价(23)—(29)。实际联合闭锥与有限截面仍取决于原低层的真实符号问题；不能把这一严格缩减说成已经完成 whole $E$、自然总量、内部 partial 和同一个二阶规范的全部 period。
