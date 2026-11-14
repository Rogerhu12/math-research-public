# R90：真实外两胞元的全46模 Green 与半径64投影整场

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-12。

**完整证明及实际算术均已完成。** 本文在 R26/R87 的同一真实度量、node12 到 node10 的胞元11、10上，支付全部 $m=2,4,\ldots,92$ 的有序整场 Green 核，并证明一个完整低46模投影问题的存在与唯一性。未知场包含这46个非均值模式；完整标量 mean 小根、完整逆分母、R78 的真无限内头低46非线性边界及全部20个实际外高度均保留。

实际收缩常数小于 $0.009917643$，半径64的球映入半径小于 $51.295437$ 的球。结论限于本文明确定义的投影边值问题：真正内切口的46条高度一致性、非零高频头迹、所有高频方程、外胞元0至9及闭曲面的幅度/reach要求没有由此自动得到。

## 1. 固定实对象、参数与范数

令 $b$ 为真实 node12 半径，$R$ 为真实 node10 半径。采用 R26 同一固定实源、冻结 global warp、原160层参数及有理深尾；物理动量规范为 $\mu_*=\mu_{11}$。两个胞元保留实际 $R_{10},R_{11},\alpha_{10},\alpha_{11}$。R87 及本次原包再次确认：这两胞元 cap 严格不活跃，valley控制为0，warp权、$\chi$、$j_0$ 为1。没有改成另一深背景，也没有额外跨胞元 $\mu$ 倍数。

参数为 R74 的全部20个 canonical cut 高度
$$
 a_m=q_m^*+v_m\xi_m,\qquad m=2,4,\ldots,40,
 \qquad |\xi_m|\le1,
 \tag{90.1}
$$
其中 $v_4=|q_4^*|/16$，其余 $v_m=|q_m^*|/1024$；另外26个内头低高度参数仍为0。R74/R78已在相同实度量上支付这个参数盒的真全频内头。这里所用边界函数是其完整真 DN 减准确线性 DN，不是有限远端 Robin 或保存的有限 worker 动量。

外部原候选 $C_*$ 含全部20个非零高度模式。置 $\eta_m=a_m/q_m^*$，并逐模式缩放非均值候选，得到 $C_\eta$；完整 mean 每次由同一个小根重新求得，不线性缩放旧 mean。对全部参数，
$$|\eta_m|\le\sigma:=17/16.\tag{90.2}$$
外端目标保持原保存的全部20个实际高度；模式42至92的外目标为0。这是固定外目标问题，并未把外目标偷偷随 $\eta$ 一起改变。

物理未知量为
$$
 P=\frac{h_\theta}{rw},\qquad K=\frac{h_{\perp,r}}w,
 \qquad \tau=1/64.
 \tag{90.3}
$$
这里 $K$ **不含**标量 mean。对于余弦高度，$P_m$ 是正弦幅度，$K_m$ 是余弦幅度。实余弦/正弦幅度的绝对值等于相应两个 signed Fourier 半幅的绝对值之和；复化幅度时仍用这个约定。

在每个原材料叶 $I$ 上，R79 保存的 $c_{0,I}$ 支配 $4R_{0,I}^2$，其中 $R_{0,I}$ 是完整原候选的点态 $W_{\tau,1}$ 联合范数。定义
$$V_I=\operatorname{up}_{80}\sqrt{c_{0,I}/4}>0\tag{90.4}$$
为准确的向上80位 dyadic 数。这个分段常值仅定义范数，未改变实际背景或场。导数方向和输出分母都使用同一个 $V_I$。

取 $\mathcal M=\{2,4,\ldots,92\}$，$\omega_m=(1+m)e^{m/64}$。在连续非均值场上定义
$$
 \|Z\|_{\mathcal X}
 =\sum_{m\in\mathcal M}\omega_m
 \left(
 \sup_{I,r\in I}\frac{|P_m(r)|}{V_I}
 +\sup_{I,r\in I}\frac{|K_m(r)|}{V_I}
 \right).
 \tag{90.5}
$$
这是先对每模每分量取径向 supremum，再求和的 Banach 范数。叶数有限、$V_I>0$，故它与通常的有限模连续场范数等价。由原候选点态界，每个分量各有 $\omega_m|C_{*,m,c}|/V_I\le1$，所以严格有
$$
 \|C_\eta\|_{\mathcal X}\le40\sigma=42.5.
 \tag{90.6}
$$
这里接受20模乘两个分量的保守因子40；没有把点态质量和与径向 supremum 交换后误写成 $\sigma$。

## 2. 全46模式的真实物理流及精确 Green

每个实际源段使用向外参数 $x$，置
$$
 s=r_x/r>0,\quad \ell=w_x/w,\quad F=\sqrt{rw^3},\quad d=(\ell-s)/2.
$$
模式 $m$ 的物理迹归一变量 $Y_m=F(P_m,K_m)^T$ 满足
$$
 Y_{m,x}=
 \begin{pmatrix}d&-ms\\-m\ell&-d\end{pmatrix}Y_m
 +e_2 F N_m.
 \tag{90.7}
$$
背景矩阵迹恰为0，真实转移行列式恰为1。$N_m$ 是原 source-$x$ 方程中 $K_x$ 的完整非线性源，所以源乘子为 $F$，**不另乘 $r_x$**。

令 $\phi_m$ 为单位 $Q_m(b)=1$ 的真线性内头列。46个初始斜率全部采用 R29 真无限尾的实列；模式2、4再与 R65 精化斜率相交。令 $\chi_m(R)=e_2$，则
$$
 W_m=\det(\phi_m,\chi_m)=\phi_{1,m}(R)\ne0.
 \tag{90.8}
$$
R87 的全部真实高度分母及本次完整物理分母检查支付所有46个非零条件。内部 $\phi_{1,m}$ 可以过零；下面公式不除以它。

零外高度、左端真线性内头直线的 Green 为
$$
 (\mathcal G_m f)(r)=
 \frac{\chi_m(r)}{W_m}\int_b^r\phi_{1,m}(t)F(t)f(t)\,dx(t)
 +\frac{\phi_m(r)}{W_m}\int_r^R\chi_{1,m}(t)F(t)f(t)\,dx(t).
 \tag{90.9}
$$
积分分界求导产生
$$
 \frac{\chi_m\phi_{1,m}-\phi_m\chi_{1,m}}{W_m}Ff=e_2Ff.
$$
两端条件直接成立。齐次差是 $\phi_m$ 的倍数，而右端第一分量为0结合 (90.8) 强迫该倍数为0，故解唯一。将 (90.9) 除以实际 $F(r)$ 即得到 $(P,K)$ 输出。

### 连续位置与余项

实际计算在256位 Arb 中保留每模的有符号共同 projective 幅度。所有源系数来自同一真实源函数；临界条带仍按160位根包围处理。每个非临界片按阶24展开，使用最高模92的逐元素正导数比较同时支付全部46模的 Taylor 余项，门为 $2^{-100}$。

对任意片内部分转移，令常值平衡范数中的全片积分上界为 $q<1/2$。准确第一阶积分属于系数全片区间乘部分长度的包围，余项由
$$\sum_{k\ge2}q^k/k!\le q^2/(1-q)\tag{90.10}$$
控制。按同一个平衡矩阵还原各元素，得到所有内部位置的转移盒。反向部分转移使用真实行列式1的 cofactor 公式；未除以独立舍入的行列式。每段前后两向列都和已付真实锚点相交。

本次覆盖原10793叶，得到10870个 Taylor 片和8个根条带，共10878片。69次细分只改变证书分割。18段、两个物理分量、全部46模式均完整保存。98个 gzip 工作块是可重生几何资料，两个主包逐块校验其SHA256；工作块本身没有被当作新的数学输入。

## 3. 完整弱源与半径64的密度比较

以下在一个固定真实叶上进行。记 $E=1+w^2\le5/4$，$T=P_\theta$，$U=K_\theta-P$。完整 mean 为同一复 Wiener 小根 $c=c(P,K)$。R33/R44的小根域及 R89 的完整微分估计给出：当
$$
 \|P\|_{\tau,1}+\|K\|_{\tau,1}\le A\le1/64,
 \qquad \|dP\|_{\tau,1}+\|dK\|_{\tau,1}\le D,
$$
则
$$|c|\le4A^2,\qquad |Dc[dP,dK]|\le16AD.\tag{90.11}$$
非均值最小频率为2，因而 $\|P\|_{\tau,0}+\|K\|_{\tau,0}\le A/3$，且 $\|U\|_{\tau,0},\|K+T\|_{\tau,0}\le A$。

完整源恰为
$$
 N(P,K)=\Pi_\perp\frac{Q+B_c}{1+l},\qquad
 l=c+K+ET,
 \tag{90.12}
$$
$$
 Q=EsU^2+\ell\{E(K+T)^2-w^2(K^2+P^2)\},
 \qquad B_c=\ell\{2c(K+ET)+c^2\}.
 \tag{90.13}
$$
特别是 $K$ 未含 $c$，这里没有重复加 mean；$\Pi_\perp$ 在 Wiener 范数中范数不超过1。

置 $\mathfrak c=s+|\ell|$。直接的 Banach 代数乘积估计给
$$
 \|Q\|_{\tau,0}\le\frac{23}{18}\mathfrak c A^2,\quad
 \|DQ[dZ]\|_{\tau,0}\le\frac{23}{9}\mathfrak c AD,
$$
$$
 \|B_c\|_{\tau,0}\le\mathfrak c(10A^3+16A^4),\quad
 \|DB_c[dZ]\|_{\tau,0}\le\mathfrak c(50A^2+128A^3)D,
$$
$$
 \|l\|_{\tau,0}\le5A/4+4A^2,\quad
 \|Dl[dZ]\|_{\tau,0}\le(5/4+16A)D.
 \tag{90.14}
$$
对完整商求导，保留两项分母 $(1-\|l\|)^{-1}$ 与 $(1-\|l\|)^{-2}$。各正比较式随 $A$ 增加；在 $A=1/64$ 上实际精确有理值为
$$
 \frac{\|N\|_{\tau,0}}{\mathfrak c A^2}
 \le\frac{13252}{9027}<\frac32,\qquad
 \frac{\|DN[dZ]\|_{\tau,0}}{\mathfrak c AD}
 \le\frac{31451168}{9054081}<4.
 \tag{90.15}
$$
这些界包括完整 mean、完整 inverse 以及因此产生的全部源频率。它们不是把源截在二次式 $Q$。

对半径 $\rho$ 的场球 $Y=C_\eta+Z$，$\|Z\|_{\mathcal X}\le\rho$，每叶可取
$$A_\rho=(\sigma+\rho)V_I,\qquad D=V_I\|dZ\|_{\mathcal X}.\tag{90.16}$$
本次已计算的 `weak_local_rho_16` 完整商导数密度 $F_{16,I}$，使用同一 $V_I$ 与同一叶上的严格 $s,|\ell|,E,w$ 上界。由其未删的 $DQ$ 正项，
$$F_{16,I}\ge2\mathfrak c_I A_{16}V_I,\qquad
 \mathfrak c_I=\sup_I s+\sup_I|\ell|.\tag{90.17}$$
因为该项系数是 $Es+(E+w^2/9)|\ell|\ge s+|\ell|$，且其正分母不超过1，这一方向的不等式成立。保存的向上舍入只增大 $F_{16,I}$。

现在取 $\rho=64$。准确比值为
$$
 \frac{A_{64}}{A_{16}}=\frac{1041}{273}<4.
$$
所以 (90.15)–(90.17) 在每个真实位置给出
$$
 \|DN(C_\eta+Z)[dZ]\|_{\tau,0}
 \le4\mathfrak c_I A_{64}V_I\|dZ\|_{\mathcal X}
 \le8F_{16,I}\|dZ\|_{\mathcal X}.
 \tag{90.18}
$$
**这个8倍比较支付的是新的半径64整个域，未把旧中心导数直接外推。**

主包所有九列域的最大输入值 $A_{\rm old,max}$ 已覆盖 $A_{16}$。新有理账本逐项检查
$$
 A_{64}\le4A_{\rm old,max}<5.860519\times10^{-11}<1/64,
$$
$$
 5A_{64}/4+4A_{64}^2<1,\qquad
 \tfrac14\{2(A_{64}/3+4A_{64}^2)
 +(A_{64}/3+4A_{64}^2)^2+\tfrac54(A_{64}/3)^2\}<1.
 \tag{90.19}
$$
最后一项支付 metric square root 的完整复扰动域。它们是整叶位置域，不是端点小量。

## 4. 真正有序的完整低窗算子范数

对每个几何子片 $J$，保存
$$
 A_{\phi,m,J}\ge\int_J|\phi_{1,m}|F\,dx,\qquad
 A_{\chi,m,J}\ge\int_J|\chi_{1,m}|F\,dx.
$$
若目标位于片 $I$，一个非负源密度 $D_J$ 的分量比较为
$$
 \gamma_{m,c,I}(D)=
 \frac{1+m}{|W_m|_{\min}}
 \left[
 \sup_I\frac{|\chi_{m,c}|}{F V_I}
       \sum_{J\preceq I}A_{\phi,m,J}D_J
 +\sup_I\frac{|\phi_{m,c}|}{F V_I}
       \sum_{J\succeq I}A_{\chi,m,J}D_J
 \right].
 \tag{90.20}
$$
源用 $W_{\tau,0}$，因此输出强范数的 $1+m$ 必须保留；指数权准确抵消。同片两个部分分别由完整该片源积分控制，故允许这个片保守重复。所有跨片来源仍严格保持次序，没有把一个谷底源和任意全胞元最大增益自由组合。

两次纯 Fraction 流式消费分别计算总源质量及有序前后缀。已知项从总数中按准确有理减去，没有 interval 依赖相减。两个分量分别取全径向 supremum 后，求和全部46个模式：
$$
 \Gamma(D)=\sum_{m\in\mathcal M,c\in\{P,K\}}\max_I\gamma_{m,c,I}(D).
 \tag{90.21}
$$
逐模单独使用完整正源上界虽保守，仍是合法正算子界；没有将某一模最大值误当成全窗之和。

完整实际预算给出
$$
 \Gamma(F_{16})<0.001239705310,\qquad
 \Gamma_{64}:=8\Gamma(F_{16})
 <0.009917642473<1/100.
 \tag{90.22}
$$
同一程序还以 $\rho=0$ 的完整商值界包围所有 $N(C_\eta)$，得到
$$
 \|\mathcal G_{\mathcal M}\Pi_{\mathcal M}N(C_\eta)\|_{\mathcal X}
 \le C_N<0.000041011314.
 \tag{90.23}
$$
这里 $\eta$ 的完整族域已包含在 $\sigma V_I$ 中，不是只计算 $\eta=1$ 后暗称全族。

原三列较粗 strong 密度及三列 uniform 密度仍完整保存。例如 uniform-$V_0$ 的 $\rho=16$ 总行大于 $10^9$，只是该替代范数的失败比较；本证明使用原实际 local-$V_I$ 范数，未利用那个失败上界。

## 5. 所有外高度与完整真内头 lift

令 $\mathcal L_R$ 是左端准确线性头直线、右端全部原目标高度的齐次场。它的第 $m$ 列为
$$\mathcal L_{R,m}=\phi_m\,Q_m^{\rm out}/S_{0,m}(R).\tag{90.24}$$
在物理分量中再除以 $F$。本次逐模式付完全部20个非零外目标，另外26个确为原目标0，得到
$$\|\mathcal L_R\|_{\mathcal X}<7.026685778.\tag{90.25}$$

在真实内切口，设 $\beta_m(a)$ 是真内头的 $K_m$ 减去单位浅高度准确线性 DN 的非线性部分。低浅高度被 R74 准确参数化，所以该边界差只在 $K$ 分量。零外高度的完整 lift 为
$$
 \mathcal B_m\beta_m=
 -\frac{m b^4w_b^2}{W_m}\chi_m\,\beta_m
 \quad\hbox{在 }Y\hbox{ 坐标中}.
 \tag{90.26}
$$
这是由 $\phi_{1,m}(b)=-m b^3F_b/w_b$ 以及
$\det(\phi_m,F_be_2\beta_m)=\phi_{1,m}(b)F_b\beta_m$
得到；$F_b^2=bw_b^3$，所以没有缺失 $w$ 或跨胞元 $\mu$ 倍数。

在加权低46迹 $\ell^1$ 到 $\mathcal X$ 的算子范数中，各列先分别求两个分量 supremum 之和，再取列最大值，而不是乘46：
$$
 \|\mathcal B\|<5.345566992\times10^{31}.
 \tag{90.27}
$$
R78 的完整真头低46值界，在相同 $\tau=1/64$、相同物理 $K$ 单位及相同20参数盒上，为
$$
 \|\beta(a)\|_{\tau,1}<2.121348040\times10^{-32}.
 \tag{90.28}
$$
该界含辅助的非线性 far 项与真全频头减辅助的另一项。它不是原候选动量差，也没有借用已失修的“源项就是全DN”表述。准确正有理乘积给
$$
 \|\mathcal B\beta(a)\|_{\mathcal X}
 \le C_\beta<1.133980806.
 \tag{90.29}
$$
此处故意保留已有的全46粗界；R82/R83 更紧的真 cut 源功能不是本结论必需的前提。

## 7. 半径64的实际投影整场定理

**定理90.1。** 对 (90.1) 中每个实参数，考虑以下明确定义的辅助边值问题：非均值未知场仅含 $\mathcal M$；高非均值场置0；完整 mean 由同一小根给出；方程只要求 $\mathcal M$ 非均值投影为零；外端取全部原目标高度；内端取准确线性头关系加规定函数 $\beta_{\mathcal M}(a)$。该问题在
$$\|Y-C_\eta\|_{\mathcal X}\le64$$
中有唯一解。其实际修正范数小于 $51.168176$。解随参数在复盒内部全纯。

**证明。** 写 $Y=C_\eta+Z$，固定点映射为
$$
 \mathcal T_a(Z)=
 \mathcal L_R-C_\eta+\mathcal B\beta_{\mathcal M}(a)
 +\mathcal G_{\mathcal M}\Pi_{\mathcal M}N(C_\eta+Z).
 \tag{90.30}
$$
第一行兼容关系在 $\mathcal L_R,\mathcal B,\mathcal G$ 中逐模准确满足。源只有第二分量；投影范数不增大。由 (90.18)–(90.22)，在整个闭球中，
$$\|\mathcal T_a(Z_1)-\mathcal T_a(Z_2)\|_{\mathcal X}
 \le\Gamma_{64}\|Z_1-Z_2\|_{\mathcal X}.$$
全部 mean/逆域由 (90.19) 支付，故这不是仅沿中心线的导数。

正有理账本实际计算
$$
 C_0:=\|\mathcal L_R\|_{\rm bound}+40\sigma+C_\beta+C_N,
$$
$$
 C_0+64\Gamma_{64}
 =51.295436712698459088666684151\ldots<64.
 \tag{90.31}
$$
所以映射严格入球且收缩。Banach定理给存在与该球内唯一性；并有
$$\|Z\|_{\mathcal X}\le C_0/(1-\Gamma_{64})<51.168176.$$
完整源和真头边界函数在已付复域上全纯，Picard迭代局部一致收敛，故解参数性成立。

有限模场的径向第一导数由 (90.7) 给出。背景及源保持实际连续接缝，第一行恢复一个非均值高度；完整标量 mean 坡度统一积分，因而得到相应兼容高度。加性 mean 高度只选择一个全局常数；本文没有同时指定 cuff 和外端两个绝对高度。

定理不声称未投影的高频 Darboux 残差或其诱导的完整 mean 微分残差已经为零。保留完整代数 mean 根不等于支付所有频率方程。证毕。

### 与最终接合的区别

(90.30) 把 $\beta(a)$ 作为已知函数输入，而输出内端高度一般是新的 $Q(b;a)$。还须解
$$Q_m(b;a)=a_m,\qquad m\in\mathcal M,\tag{90.32}$$
并恢复真内头非零高迹及全部高方程。尤其模式42至92的内高度输出不能因其参数当前固定0而被忽略。本文既没有通过 (90.32)，也没有把这些输出设置为0来降低自由度。

同样，两个外胞元以外的0至9及整体闭曲面几何仍为独立工作。当前结论是已有实际全46整场逆与投影存在，不是课题完成声明。

## 8. 实际执行、精确账本与保全

几何入口为 [closure_outer_physical_green_geometry_recovered_v2.py](../computations/closure_outer_physical_green_geometry_recovered_v2.py)，SHA256
`c48606c4e127fb0d3f27479eeed11bff3c5cb69139148633ea4f74a9e1f63829`。
有序入口为 [closure_outer_physical_green_budget_recovered_v2.py](../computations/closure_outer_physical_green_budget_recovered_v2.py)，SHA256
`e2113502398ebb1d4649a82a813ef0d6f2f90802ef9da52cbac8e37d36a39d83`。

GitHub Actions run **43303787139** 的两个阶段均有真正 wait4 记录：

| 阶段 | exit/signal | wall秒 | 峰RSS KiB | 完整覆盖 |
|---|---|---:|---:|---|
| whole46-physical-green-geometry | 0 / null | 360.047658655 | 46300 | 18段、10793原叶、10878子片、46模 |
| whole46-ordered-green-budget | 0 / null | 392.053089258 | 24636 | 原98块全哈希、两次有序消费、9密度全46 |

该 job 后续尾支在旧源码绝对路径的输入身份守卫处退出1，尚未积分；缺失或字节差异待窄恢复实际诊断。这不撤销上述两个已有正常退出且正常发布的阶段。更早 run43302113873 在初始化时因45308KiB超原40960KiB观察门退出1；之后明确把隔离 runner 的资源门改为98304KiB，没有修改科学源、精度或数学门。run43303094938 是同步 push 的ref竞争，未启动数学任务。所有失败和成功各自保留。

两个主包为：

- [实际几何](../notes/2026-11-12-closure-physical-green-actions-43303787139-1-interval.json)，SHA256 `e3bb0bad3afac3e19d6b811ad068d0b4251b2a1214718dcbd14a2eb98e1aaa03`；
- [实际有序全窗预算](../notes/2026-11-12-closure-physical-green-budget-actions-43303787139-1-interval.json)，SHA256 `86c9b5604a765a50028865a4f3edae3171d9582052e2b7e7515d0471d8685d45`。

本定理最后的28项门由 [closure_r90_projected_ball_ledger.js](../computations/closure_r90_projected_ball_ledger.js) 在 `functions.exec` 的 V8 BigInt 中**实际执行**。它先把每个 JSON 数字 token 无损保存为字符串，再转整数分数，所有大 mantissa 均未经过 IEEE-754。六个完整输入SHA、两条正式退出、同20参数轴、所有46分母、真实源域、完整 mean/逆与自映/收缩门均为真。显示小数只由准确整数向上取整，不参与证明比较。没有声称新 Node/Arb/终端任务已运行。

该脚本同时提供仓库内 Node 重现入口，输出不可覆盖；本次实际结果保存在 [R90精确账本](../notes/2026-11-12-closure-r90-projected-ball-exact-ledger.json)。每个模式的独立正行及全窗聚合都保存。原聚合是在未逐行舍入的数相加后向上舍入，因此不能用“逐行先舍入后再相加”替换它并要求两者逐位一致。

本文直接登记已经完整证明且实际过门的范围；仍未付的切口与高频义务见 (90.32)，不另设审核批准门。
