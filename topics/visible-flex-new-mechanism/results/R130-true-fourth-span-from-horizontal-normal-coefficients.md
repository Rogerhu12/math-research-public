# R130：真实第四成本商恰由水平正规式的归一化局部系数张成

日期：2026-11-14。**已证明。** 纸面论证，不运行新的研究编译、profile 评价或几何计算。

依据 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md) 的真实任意矩阵/端口桥、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md) 的真实传递与倒行、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md) 的有限真实成本空间、[R109](R109-local-density-of-the-complete-fourth-quotient.md) 的完整局部化、[R112](R112-local-fourth-geometric-derivative-weights.md)、[R114](R114-constrained-static-costs-and-real-zero-matrix-words.md) 和 [R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)。

本稿支付 R129 特别保留的一个逆向门：在正确消掉八矩乘子后，其指定水平正规式的全部状态系数，确实张成完整真实第四成本模已可调响应的商。证明先处理真实低阶端点与群可达性，再使用时长缩放和微幅路径；不直接把形式系数当成独立几何控制。

## 1. 固定有限真实环境与局部密度

继续使用完整两个复相位模式、同一 canonical 目标、共同右锚、零传入历史。令

$$
R=\mathcal R_8,\qquad U=\mathcal U_4.
$$

R105 定义 U 为某固定 scalar 常值 germ、frame $I\to I$ 上全部实际 $M=T=0$ 成本的真实线性 span，并证明这个 span 不依赖 germ。R109 的局部式为

$$
L=v-\mathcal B_mN=L_0+L_2+L_4,\qquad m=m_0+m_2.
\tag{1}
$$

下标是几何导数权。$m_2$ 是速度二次式；完整 L 至三阶 jets。所有状态项、局部势、其真实导数与固定右端原函数全部保留。

在一个固定有限维**真实函数空间** E 中工作，使它包含 R 和 (1) 的全部局部 profile 系数。R105/R109 保证可以这样选，并有 $U\subseteq E$。几何系数微分、有限线性组合及下文的八个静态参考值都仍在 E 中。没有把冗余 formal 原表达式当作一组独立基。

对任意 $\ell\in E^*$，定义局部积分

$$
I_\ell(B)=\int_B\ell(L)\,ds.
\tag{2}
$$

式 (2) 是真局部密度的积分，不是把非零传入历史路径的完整 V 擅自当作可加量。它对平端路径拼接直接相加，因为 L 不含累计二、三阶历史，且所有段保持同一状态、同一 $\xi$ 和同一右锚。

当整条 B 满足 $M_B=0$ 且 $\ell(R)=0$ 时，R109 准确给

$$
I_\ell(B)=\ell(V_B).
\tag{3}
$$

(3) 不要求 $T_B=0$。一般 $M_B\ne0$ 时，本稿不使用这个等式。

## 2. 八矩归一化与十四个状态系数族

按 R114 选八个参考状态

$$
S_i^*=(h,k,\omega)=(1,k,d+k),
\qquad d=0,1,-1,2,\quad k=0,1.
$$

$m_0(S_i^*)$ 是 E8 的真基。令 $a_i:E_8\to\mathbb R$ 为其线性坐标，设

$$
F_i=L_0(S_i^*),\qquad
\Gamma(M)=\sum_{i=1}^8a_i(M)F_i.
\tag{4}
$$

完整归一密度为

$$
\widetilde L_0=L_0-\Gamma(m_0),\qquad
\widetilde L_2=L_2-\Gamma(m_2),\qquad
\widetilde L_4=L_4.
\tag{5}
$$

特别不能只减静态 $m_0$；真实矩阵约束是 $\int(m_0+m_2)=0$。式 (5) 的第二项正是 R124 保留的诱导修正。

写真实水平状态和速度为

$$
S=(h,k,\omega),\quad h>0,\qquad
u=h_s,\quad w=k_s,\quad a=h_{ss},\quad b=k_{ss},
$$

$$
\omega_s=\frac{w}{2h},\qquad
X=\partial_h,\qquad
Y=\partial_k+\frac1{2h}\partial_\omega.
\tag{6}
$$

把 R129 的完整分部积分作用于 $\widetilde L_2,L_4$：

$$
\widetilde L_2=D_sP_1+\widehat Q_2(S;u,w),
\tag{7}
$$

$$
L_4=D_sP_3+\overline A_{hh}a^2+\overline A_{hk}ab+
\overline A_{kk}b^2+(H_1u+H_2w)(ub-wa)+\widehat Q_4(S;u,w).
\tag{8}
$$

这里 $\widehat Q_2$ 对速度齐次二次，$\widehat Q_4$ 齐次四次；全部状态导数按 X、Y 作用。$P_1,P_3$ 是 R129 明确给出的正导数权势，在两端常值 germs 上分别为零。

定义 K 为下列 E 值状态函数在所有 $h>0,k,\omega\in\mathbb R$ 上的值的真实 span：

1. $\widetilde L_0(S)$；
2. $\widehat Q_2$ 的三个速度系数；
3. $\overline A_{hh},\overline A_{hk},\overline A_{kk}$；
4. $H_1,H_2$；
5. $\widehat Q_4$ 的五个速度系数。

共有十四个状态函数族；每个族的值可以张成多于一维，故不称 $\dim K\le14$。

**定理：**

$$
\boxed{U=R+K.}
\tag{9}
$$

等价地，完整真实第四商恰为这些归一化水平系数的真实函数 span 模 R。以下先证明最关键的端点约束消去，之后才证明系数分离。

## 3. 先严格去掉第三算子条件，只用于 frame I 的闭端口

固定 $\ell\in E^*$，假设

$$
\ell(U)=0.
\tag{10}
$$

因 $R\subseteq U$，有 $\ell(R)=0$。

取任一同 scalar germ、frame $I\to I$、$M_B=0$ 的实际平端路径 B，其第三算子可以非零。按 R83，真倒行仍具有 frame $I\to I$，并满足

$$
M_{B^R}=0,\quad T_{B^R}=-T_B,\quad V_{B^R}=V_B.
$$

因此 $BB^R$ 是实际 $M=T=0$ 同端口路径；两块矩阵都为零，真实第四传递中的交叉项消失，故

$$
V_{BB^R}=2V_B.
$$

由 (10) 得 $\ell(V_B)=0$，再由 (3) 得

$$
\boxed{I_\ell(B)=0
\quad\text{对同 germ、frame I、M=0 的全部平端路径}.}
\tag{11}
$$

这里尚未对非恒等 frame 或非零矩阵路径作任何零成本断言。也没有用倒行取负第四成本。

## 4. scalar 闭路径的真实端点纤维

现在固定 scalar germ g，允许末 frame 为任意 $A\in SO(3)$，矩阵为任意 $M\in E_8$。

R70 §1 的原命题确实给出：两端 scalar 常值 germs、首末 frame 以及任意有限无迹矩阵目标都可准确指定；并可在目标的小邻域使用同一有限辅助圈数，光滑选择实际路径。R70 使用的分部积分矩阵与 R73 的 $\int m$ 对平端路径相同，相关导数端项分别为零。

设 $B_1,B_2$ 是同 g 的 scalar 闭路径，具有同一端数据 $(A,M)$。用 R70 选一条同 g 的平端路径 C，末 frame 为 $A^{-1}$，矩阵为 $-M$。把 C 从各自末 frame 左旋转后接上。局部密度和矩阵不受这个固定环境旋转影响，因此

$$
B_1C,\ B_2C
$$

都具有 frame I、矩阵零和同一 scalar germ。由 (11) 与局部积分的可加性，

$$
I_\ell(B_1)+I_\ell(C)=0
=I_\ell(B_2)+I_\ell(C).
$$

故 $I_\ell(B_1)=I_\ell(B_2)$。这里 $-M$ 是 R70 实现的实际目标，不是负时间或给 C 的第四成本取负。

于是定义良好的函数

$$
F_g:SO(3)\times E_8\longrightarrow\mathbb R,\qquad
F_g(A,M)=I_\ell(B)
\tag{12}
$$

只依赖真实端数据。没有先假定路径同态，而是先通过共同实际补偿证明了纤维常值。

## 5. 群同态与同一个矩阵乘子

对端数据为 $(A,M)$、$(B,N)$ 的两条同 g 路径顺序拼接，末 frame 为 AB、矩阵为 $M+N$。局部 L 无累计历史，故

$$
F_g(AB,M+N)=F_g(A,M)+F_g(B,N).
\tag{13}
$$

R70 的局部光滑端点截面使 (12) 在单位元附近连续：辅助圈数和拼接数固定，状态正性与有限 jets 有界，有限局部积分连续。由 (13)，它在整个群上连续。

SO(3) 的连续同态像是实数加法群的紧子群，只能为零；若含非零数，其整数倍就无界。E8 的连续加法函数则是实线性的。所以存在

$$
\mu_g\in E_8^*
$$

使

$$
\boxed{F_g(A,M)=\mu_g(M).}
\tag{14}
$$

这一步没有给任何实际第四成本构造逆元。取差只发生在已经证明相等的实数积分里；全部补偿路径均由 R70 以有限正长度实现。

## 6. 真倒行把结论提升到所有开 scalar 平端路径

取任一平端路径 B，从 scalar germ $g_0$ 到 $g_1$，初 frame I、末 frame A；矩阵不必为零。令

$$
D=\operatorname{diag}(-1,1,-1).
$$

同 k 真倒行的准确 frame 为

$$
F^R(s)=D A^TF(L-s)D,
\tag{15}
$$

scalar 状态为 $S^R(s)=S(L-s)$。它初 frame 为 I，末 frame 为 $DA^TD$，并满足真实水平约束。把它接在 B 后，整体 frame 是

$$
ADA^TD,
$$

**通常不是 I**。这里只因 (14) 已经对全部 frame 成立，才可以继续使用它。

R112 给 m 的导数权仅 0、2，L 的导数权仅 0、2、4。真倒行下每个 j 阶几何导数乘 $(-1)^j$，故逐点有

$$
m_{B^R}(s)=m_B(L-s),\qquad
L_{B^R}(s)=L_B(L-s).
$$

因此

$$
M_{B^R}=M_B,\qquad I_\ell(B^R)=I_\ell(B).
\tag{16}
$$

这里谈的是局部 I，不是假定非零矩阵下的完整 V 也满足同号可加。

$BB^R$ 的 scalar 首末为 $g_0$，其矩阵为 $2M_B$。由 (14)、(16)，

$$
2I_\ell(B)=F_{g_0}(ADA^TD,2M_B)=2\mu_{g_0}(M_B).
$$

即

$$
I_\ell(B)=\mu_{g_0}(M_B).
\tag{17}
$$

乘子不依赖起始 germ。为证此点，用 R70 选 frame I、M=0 的开桥 C 从 $g_0$ 到 $g_1$。由 (17)，$I_\ell(C)=I_\ell(C^R)=0$。将任一 $g_1$ 的 scalar 闭路径放入 $CBC^R$，两边的真实端矩阵相同；由 (14) 比较得 $\mu_{g_0}(M)=\mu_{g_1}(M)$ 对任意 M 成立。任意 M 在 $g_1$ 上可达，故两乘子相同。

因此得到一个固定 $\mu\in E_8^*$：

$$
\boxed{
\int_B\bigl(\ell(L)-\mu(m)\bigr)\,ds=0
\quad\text{对所有真实开或闭 scalar 的平端路径 B}.
}
\tag{18}
$$

这正是此前不能提前假定的零积分命题。

反向也成立：若 $\ell(R)=0$ 且某固定 μ 满足 (18)，则对任一实际 $M=T=0$ 路径，由 R109 有 $\ell(V_B)=0$。所以 (18) 是真实湮灭子条件，不只是充分构造。

## 7. 常态定出乘子，随后才合法分离时长权

在任一常态 S 上取任意正长度的常路径。其 frame 可以非 I，但 (18) 已允许这种端口。因此

$$
\ell(L_0(S))=\mu(m_0(S)).
\tag{19}
$$

代入八个参考状态，唯一得到

$$
\mu(M)=\ell(\Gamma(M)).
\tag{20}
$$

所以 (18) 变成

$$
\int_B\ell(\widetilde L_0+\widetilde L_2+L_4)\,ds=0.
\tag{21}
$$

固定一条 scalar 轨迹，按 $s=\delta\sigma$ 改变真实时长。水平关系仍成立，首末仍是平端 germs；实际 M 和 frame 一般改变。但这已不再是漏洞，因为 (21) 已经对这些变化后的全部开平端路径成立。

由 R112，

$$
\delta A_0+\delta^{-1}A_2+\delta^{-3}A_4=0
\quad\forall\delta>0,
$$

其中 $A_j$ 是相应固定轨迹上的标量积分。乘 $\delta^3$ 得一个恒零的 $\delta^2$ 多项式，故

$$
A_0=A_2=A_4=0.
\tag{22}
$$

因此 $\ell(\widetilde L_0(S))=0$ 对每个 S 成立，且由 (7)–(8) 的真实零端势，

$$
\int_B\ell(\widehat Q_2)\,ds=0,\qquad
\int_B\ell(\mathcal N_4)\,ds=0
\tag{23}
$$

对所有开平端路径成立。没有在原来的零矩路径类中擅自独立缩放三个成本。

## 8. 真实微幅路径准确分离所有剩余系数

固定任意状态 $S_*=(h_*,k_*,\omega_*)$，$h_*>0$。取任意光滑紧支撑速度 U、W，定义

$$
u_\varepsilon=\varepsilon U,\qquad
w_\varepsilon=\varepsilon W,
$$

$$
h_\varepsilon=h_*+\varepsilon\int U,\qquad
k_\varepsilon=k_*+\varepsilon\int W,\qquad
\omega_\varepsilon=\omega_*+
\int\frac{\varepsilon W}{2h_\varepsilon}.
\tag{24}
$$

积分均从路径左端开始。对充分小的 $\varepsilon$，h 保持正；状态为 $S_*+O(\varepsilon)$，两端有开常值 germs，水平微分关系准确成立。末 scalar 状态无需等于初态，且不额外强加 frame 或 M 约束。它们已经由 (18) 处理。

所有系数对状态光滑。以下只取小幅极限，不微分一个未受控的余项，也不把固定状态的 jets 当作独立实际路径。

### 8.1 速度二次式

在 (23) 第一式除 $\varepsilon^2$ 后取极限，得到

$$
\int\ell(\widehat Q_2(S_*;U,W))\,ds=0.
$$

取 $U=\alpha\psi,\ W=\beta\psi$，其中 $\psi$ 是非零光滑紧支撑函数。由于 $\int\psi^2>0$，相应关于 $\alpha,\beta$ 的二次式恒零，故三个标量系数分别为零。S 任意，所以 $\ell$ 杀 $\widehat Q_2$ 的全部系数值。

### 8.2 加速度二次式

第四正规式在 (24) 上，加速度二次项为 $\varepsilon^2$，H 项为 $\varepsilon^3$，速度四次项为 $\varepsilon^4$。先除 $\varepsilon^2$ 取极限，再取同向速度 $U=\alpha\psi,W=\beta\psi$，利用 $\int(\psi')^2>0$，得到

$$
\ell(\overline A_{hh}(S_*))
=\ell(\overline A_{hk}(S_*))
=\ell(\overline A_{kk}(S_*))=0.
\tag{25}
$$

因为这在每个状态上都成立，加速度二次部分在后续标量计算中**处处恒零**；其状态变化不会污染下一阶。

### 8.3 两个非对称速度—加速度系数

现在除第四式的 $\varepsilon^3$，取极限。取定义在对称区间上的非负、非零、偶的光滑紧支撑函数 $\psi$，并令

$$
U=\psi,\qquad W=\psi'.
$$

记 $A_\psi=\int\psi(\psi')^2>0$。真实一次分部积分和奇偶性给

$$
\int U(UW'-WU')=-3A_\psi,\qquad
\int W(UW'-WU')=0.
\tag{26}
$$

所以 $\ell(H_1(S_*))=0$。交换 U、W 后，两项分别为 $0,3A_\psi$，得到 $\ell(H_2(S_*))=0$。

此处不把 H 项称作全导数。正是 (26) 证明，若它对全部开平端路径积分为零，其两个标量系数必须分别为零。

### 8.4 速度四次式

(25) 及 H 的结论在每个状态上成立。余下第四式除 $\varepsilon^4$、取同向速度 $U=\alpha\psi,W=\beta\psi$，得到

$$
\ell(\widehat Q_4(S_*;\alpha,\beta))\int\psi^4=0.
$$

$\int\psi^4>0$，故这个二元四次式的五个系数均被 $\ell$ 杀掉。

综上，从 (10) 严格推出

$$
\boxed{\ell(K)=0.}
\tag{27}
$$

## 9. 反向及真实 span 等式

反过来，设 $\ell(R)=0$、$\ell(K)=0$。由 K 的定义和 R129 完整分部积分，

$$
\int_B\ell(\widetilde L_0+\widetilde L_2+L_4)\,ds=0
$$

对任一平端路径成立；所有显式正权势在各端分别为零。利用 (5)，

$$
I_\ell(B)=\ell(\Gamma(M_B)).
$$

因此对每条实际 $M=T=0$ 同端口路径，由 R109 得 $\ell(V_B)=0$，即 $\ell(U)=0$。

于是，在有限真实环境 E 中，

$$
\ell(U)=0
\iff
\bigl(\ell(R)=0\ \text{且}\ \ell(K)=0\bigr).
\tag{28}
$$

有限维子空间由其湮灭子唯一确定，(28) 给出 (9)：

$$
\boxed{U=R+K.}
$$

这也说明归一化后的各个实际系数值确实属于 U 的真实线性 span。证明没有计算每个值由哪些实际路径相加减表示，也没有赋予这些相减一个实际拼接实现。

若将状态系数按有限 Laurent/log 单项式收集，实际值的 span 与这些系数向量的 span 相同：有限函数族
$h^p(\log h)^j k^a\omega^b$ 在 $h>0,k,\omega\in\mathbb R$ 上线性独立；先分离 k、omega 多项式，再令 $h=e^t$，使用有限指数多项式独立性即可。若实现采用其他有冗余的状态基，须先支付其真实依赖，不能仍把每个形式标签都当独立方向。

## 10. 可直接使用的结论及边界

本稿把后续完整商计算确定为：

1. 使用原 L0、L2、L4 和同一个八矩密度；
2. 保留 $\Gamma(m_2)$，作 (5)；
3. 按 R129 的真实水平导数作完整分部积分；
4. 对上述十四个状态系数族，在真实 R 响应商中确定其函数 span。

如果这些完整原式系数全部属于 $R+\operatorname{span}\operatorname{Orb}(G)$，则由本稿及已知反向包含，准确得到 $U=R+\operatorname{span}\operatorname{Orb}(G)$；届时才可把 R122 的有限轨道控制应用到整个 canonical 第四成本。当前没有计算或宣称这个最终成员事实。

若某完整正规系数严格不在一个已知可达子空间中，本稿保证它是实际成本**线性 span**的新方向，而非只有 formal 几何系数意义。但还须另行处理正成本锥、实际有限基准、连续可调性和同一有限设计的精确支付。非负泛函的条件不是 (10)；本稿不把 R127 的正泛函自动当零泛函。

全部论证采用 universal 真实函数空间。每次使用 R70 的有限路径或小参数族后，可以选择共同正物理区间；没有要求任意预给窄区间或统一几何控制盒容纳全部构造。空间末位移不在本算子定理中指定。

最后，(9) 只处理完整第四 characteristic 周期成本的真实 span。它不支付第四逐 s ruling、双 collar、后续阶与收敛，更没有闭嵌入、reach、宏观幅度或主课题完成结论。
