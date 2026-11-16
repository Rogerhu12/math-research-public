# R409：八个实际末包的完整通量读出正字符

日期：2026-11-16。**纸面证明；没有执行新的研究、开发检查、profile 评价或数值插值。**

本稿从 R407 的有限真实总通量出发，给出一个已经能判定实际像的子映射。关键是整个自然函数虽未在所有 normal 层上逐项化为局部密度，其对一个固定母包的**真实平移次数仍至多七**，且七次系数准确读出原正字符。

在 R405 原复制库中，选择同一个完整基本块的八个副本各自最后一个微包。它们具有同一实际母形、同一实际正宽和八个不同中心；每个所选微包右侧的完整加权三矩 suffix 均为零。若这个实际母形满足 $\int(U'')^5\ne0$，则这十六个完整 period 总通量的一个固定线性组合恰等于 $\lambda_+$. 因而在原正时长、零八矩、同端口闭 frame 且 whole pure 为零的 canonical 几何上，它们不能同时为零。任意允许的同圆二阶 gauge 均不能改变该结论。

这个结论有明确范围：对已冻结但尚未评价第五矩的圆，只得到一个必要条件；本稿另外证明可在 R405 的**新初选母函数阶段**保证该第五矩非零，同时保留原十九个完整局部目标的有限根。没有更改一个旧冻结纤维的数值，也没有排除第五矩为零的母形或一般有理端芽。

## 1. 原对象、同锚作用与已付来源

记 $U$ 为原完整 canonical 第四成本线性空间，$\mathcal R$ 为原真实响应子空间。保留原两个模式、全部 history、同一个真实右锚及 canonical 初值。自然函数记为
$$
\mathcal N(V):u\longmapsto\Lambda_u(V).
\tag{1}
$$
这里的 $\Lambda$ 是 R344、R352、R406 的完整自然收缩；一般情况下不能用未作 pure/有序尾补偿的 $\int u'''V(u^2,0)$ 代替它。

以下四条均使用原完整函数空间的结论：

1. [R190 §6](R190-complete-weight-plus2-quotient-vanishes-and-remaining-even-weights.md) 给
   $U=\bigoplus_{\sigma=-9}^{3}U_\sigma$，并且 $U_2=\mathcal R_2$。
2. [R356 §§7—8](R356-lowest-two-full-self-weights-and-universal-total-flux-cancellation.md) 给
   $\mathcal N(U_{-9}\oplus U_{-8})=0$。这里不需要、也没有声称 $U_{-9}$ 或 $U_{-8}$ 等于响应像。
3. [R406 §§4—6](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md) 给
   $$
   \mathcal N(V_0)=\lambda_+(V_0)n_2,\qquad V_0\in U_0,
   \tag{2}
   $$
   其中 $n_2$ 为原完整十二项局部五次泛函。
4. [R196 §§4、7—8](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md) 给 $\lambda_+$ 的真实仿射不变性，特别
   $\lambda_+(\mathsf N V)=0$；R344 给 $\mathcal N(\mathcal R)=0$。

$\mathsf N$ 是 profile 平移导子，降低真权一阶。成本的真实正仿射作用满足
$$
\Lambda_u(\mathsf P_{H,c}V)
=H^2\Lambda_{C_{H,c}u}(V),\qquad
(C_{H,c}u)(x)=u((x-c)/H).
\tag{3}
$$
(3) 是 R406(21) 所引用、独立于旧 H 数值结论的同锚协变。特别，$\ker\mathcal N$ 对真实平移稳定。原有限仿射 Volterra 空间中的 $\mathsf P_{1,c}$ 是有限多项式作用；这不是只在若干查询点成立的形式记号。

## 2. 整个自然函数的平移上界与唯一最高系数

固定任意真实实紧光滑 $u$，置
$$
p_{V,u}(\xi)=\Lambda_{u(\,\cdot-\xi)}(V)
=\Lambda_u(\mathsf P_{1,\xi}V).
\tag{4}
$$
先在所有支撑合法的开区间使用(4)；有限多项式身份随后决定其 universal 延拓。这里不声称每个实 $\xi$ 都处在同一几何的物理域。

对真权 $\sigma<0$，$\mathsf N^7V_\sigma$ 的权至多 $-8$。它或者属于 $U_{-8}\oplus U_{-9}$，或者已经低于原权支撑。故它在 $\ker\mathcal N$ 中。由该核的平移稳定性，
$$
\partial_\xi^7p_{V_\sigma,u}(\xi)=0.
\tag{5}
$$
所以所有负权层的次数至多六。

对 $\sigma=1$，$\mathsf NV_1\in U_0$，而
$\lambda_+(\mathsf NV_1)=0$。由(2)，$\mathsf NV_1\in\ker\mathcal N$；再用核的平移稳定性，$p_{V_1,u}$ 是常数。不能只知道其在 $\xi=0$ 的一次导数为零便作此推断。

对 $\sigma=2$，$V_2\in\mathcal R_2$，故整条函数为零。对 $\sigma=3$，$\mathsf NV_3\in U_2=\mathcal R_2$，故 $p_{V_3,u}$ 也是常数。这已覆盖全部正权，不需要预先求出 F0、Q2 的每一项自然值。

最后看权零。R406 的完整密度中唯一显式次数七项是
$$
-\frac3{80}x^7(u'')^5.
\tag{6}
$$
其余十一项的显式 $x$ 次数至多六。对 $u(x-\xi)$ 换元 $y=x-\xi$，只有(6)贡献 $\xi^7$。结合(2)，得到完整结论
$$
\boxed{
\deg_\xi p_{V,u}\le7,\qquad
[\xi^7]p_{V,u}
=-\frac3{80}\lambda_+(V)\,M_5(u),
\quad M_5(u):=\int(u'')^5.
}
\tag{7}
$$

(7) 是所有 $V\in U$ 的原完整自然函数身份。它不假设 $\pi V=0$，也不假设 whole self 为零；更没有把尚未逐项收齐的 F0/Q2 都当作局部 $C^2$ 函数。原最低两权的完整消去、真权支撑和仿射协变已经足够。

## 3. 八次有限取值的准确读出

取八个不同实中心 $\xi_0,\ldots,\xi_7$，全部相应支撑均在共同合法区间内。记
$$
D_j=\prod_{k\ne j}(\xi_j-\xi_k).
\tag{8}
$$
对任何次数至多七的多项式，其最高系数是八个 Lagrange 基函数最高系数的加权和。因此(7)直接给
$$
\boxed{
\sum_{j=0}^7\frac{\Lambda_{u(\,\cdot-\xi_j)}(V)}{D_j}
=-\frac3{80}\lambda_+(V)M_5(u).
}
\tag{9}
$$
这里不需要八个查询独立，也不需要新求任何 rank。

固定物理正宽 $w$，若实际形状按 R405 的规范写为
$$
u_j(x)=U((x-\xi_j)/w),
\tag{10}
$$
则(9)中的中心零形状是 $\widetilde u(x)=U(x/w)$，并且
$$
M_5(\widetilde u)=w^{-9}M_5(U).
\tag{11}
$$
所有额外幅度均放入下文的 $a_j,b_j$。如果原构造曾采用带 $w^{3/2}$ 的归一包，该幅度也须先并入 $a_j,b_j$；不能在(11)之外再丢一次宽度因子。完全不依赖命名规范的表述始终是
$-3\lambda_+(V)M_5(\widetilde u)/80$。

## 4. 原完整复制库中确有这八个同形末包

本节只选择已经存在的有限包；不在冻结后移动中心或增加副本。

从 R277/R280 的一个完整基本块开始。令它内部的真实微包为
$$
f_*=\sum_i a_i u_i,\qquad
g_*=\sum_i b_i u_i,\qquad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i.
$$
完整块满足
$$
\sum_{i\in B}R_i\mu(u_i)=0,\qquad
\sum_{i\in B}T_i\mu(u_i)=0,
\tag{12}
$$
其中
$$
\mu(u)=\left(\int(u'')^2,\ \int x(u'')^2,\
\int(x^2(u'')^2+2(u')^2)\right).
\tag{13}
$$
(12)是三分量真实矩身份。R280 的有限矩编码、R324 的原 $\mathcal F_{\rm rat}$ 以及 R403/R405 的逐基本包同纤维纠正，保留的正是这些实际矩，不只是一个 cell 的标量均值。

[R183 §5](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md) 取八个不交平移
$$
t_j=t_*+jL,\qquad
\alpha_j=(-1)^j\binom7j^{1/3},
$$
并同时将 $f_*,g_*$ 乘 $\alpha_j$。这些操作不改变母坐标宽度；之后即使对整个库作共同正仿射变换，八个对应微包的实际宽度仍相同。

后续 R259 §9 的十二个完整副本只是对整个八复制块作平移、共同正幅和 $g$ 翻号。R280 的五个最终完整块保留它们各自的全部原复制结构。不同最终块可以有不同实际宽度或不同最终母形；本证明只在其中一个八复制组内选包，绝不假定全库共同宽度。

R403/R405 的有限十九根修改一个基本位置时，修改其**全部实际副本**。因此，选这个完整基本块的最后一个微包，在八个副本中得到：

- 同一个最终母坐标函数 $U$；
- 同一个实际正宽 $w$；
- 八个真实不同中心 $\xi_j$；
- 各自保留的真实幅度 $a_j,b_j$，其中 $a_j\ne0$。

若外层作了整体反射或重新编号，直接按实际中心使用(8)；不需要继续保留等距表示。

还必须核右侧 suffix。对每一个所选末包，它右侧没有同一基本块的剩余微包；其余右侧全部由**完整基本块**组成。每个完整块的(12)在真实平移、正缩放、共同幅度及 $g$ 翻号后仍成立。因此
$$
\boxed{
n_{R,j}:=\sum_{k>j}R_k\mu(u_k)=0,\qquad
n_{T,j}:=\sum_{k>j}T_k\mu(u_k)=0 .
}
\tag{14}
$$
此处 $k>j$ 指整个真实有序库，而不是仅在八个所选末包中求和。后来的十二/五块也全部计入。这没有把单个右包的原二阶左尾置零；只有真实加权三矩闭合后的总 suffix 为零。

## 5. 从自然查询到两条原完整 period 的总通量

现在加入 R389/R407 的准确几何条件：
$$
M=0,\qquad T=\tau\mathfrak H,\quad \tau\ne0,\qquad \pi V=0.
\tag{15}
$$
$V$ 保留 canonical 归一、同端口闭 frame 与同一右锚。若另有 whole $\mathcal QV=0$，仍可使用下式，但整包总通量本身不需要这条更强条件。

写
$$
V_\theta=\sin^2\theta\,V_d+
2\sin\theta\cos\theta\,V_e.
$$
对每个真实活动包 $J_i=(\ell_i,r_i)$ 定义
$$
\mathcal T_{d,i}=\int_{J_i} f'V_d''
=\int_{J_i}f'''V_d,\qquad
\mathcal T_{e,i}=\int_{J_i} f'V_e''
=\int_{J_i}f'''V_e.
\tag{16}
$$
端项由 $f',f''$ 在包端全平消去；$V_d,V_e$ 自身允许有原平台多项式。

[R389 §§2—5](R389-ordered-total-fluxes-and-complete-flat-end-germs-for-the-rational-port.md) 从完整 whole-pure 极化和原有序三矩尾证明
$$
\begin{aligned}
\mathcal T_{d,i}
&=a_i^3\{R_i\omega_i+\mathcal A_i(n_{R,i})\},\\
\mathcal T_{e,i}
&=-a_i^3\{T_i\omega_i+\mathcal A_i(n_{T,i})\},\\
\omega_i&=\Lambda_{u_i}(V).
\end{aligned}
\tag{17}
$$
$\mathcal A_i$ 是保全部实际历史的线性三矩函数。原 $\pi V=0$ 使 pure 的有序 $2+2$ 映射整体为零，故此处自然收缩才等于相应 raw self 收缩；不能对一般 $V$ 直接作此替换。

对其它外包，真正落在 $J_i$ 上的二次左尾被紧 $u_i'''$ 的整包积分准确杀掉。这一步也是(17)不需要 whole $\mathcal QV=0$ 的原因。内部部分通量则不能照搬这个简化。

将(14)代入(17)，每个所选末包满足
$$
\mathcal T_{d,j}=a_j^3R_j\omega_j,\qquad
\mathcal T_{e,j}=-a_j^3T_j\omega_j.
\tag{18}
$$
因 $a_j\ne0$，$R_j,T_j$ 不可能同时为零，于是
$$
\boxed{
\omega_j=
\frac{R_j\mathcal T_{d,j}-T_j\mathcal T_{e,j}}
{a_j^3(R_j^2+T_j^2)} .
}
\tag{19}
$$
负的原八复制幅度仍在 $a_j^3$ 中；不能将其改为绝对值。

## 6. 原有限 period 映射上的正字符与实际障碍

设 $M_5(\widetilde u)\ne0$。将(19)代入(9)，得到
$$
\boxed{
\lambda_+(V)=
-\frac{80}{3M_5(\widetilde u)}
\sum_{j=0}^7
\frac{R_j\mathcal T_{d,j}-T_j\mathcal T_{e,j}}
{a_j^3(R_j^2+T_j^2)D_j}.
}
\tag{20}
$$
右边只有十六个**同一实际圆**的完整 period 总通量。其系数全部由已经冻结的实际 profiles、幅度、中心和宽度决定。没有另取八个辅助母包，没有重新选择右锚，也没有把不同几何的控制结果相拼。

对正时长、相同端口、闭 frame、$M_B=0$ 的实际 canonical 成本，[R196 §7](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md) 与 R406 §7 给
$$
\lambda_+(V_B)
=\int_B k(s)^2ds
=L_B+\int_B(h_s/h)^2ds>0 .
\tag{21}
$$
非零 $T=\tau\mathfrak H$ 不构成例外：原真倒行在 $M=0$ 时保成本、反第三矩，故 $BB^R$ 将 $2V_B$ 放入同一原 $U$；(21)的完整局部化也直接保留所有历史。

所以在(15)的实际成本中，(20)给这十六维显示输出的一个严格正线性读出。它们不可能同时为零，实际像也不可能包含原点。这是明确的有限实际半空间障碍，不是从“全自然函数不能全零”直接外推固定查询。

### 6.1 同一个允许二阶 gauge 不能消除此读出

原 R225/R326/R389 的完整公式是
$$
\Delta V_\theta=2\tau L_f(w_\theta),
$$
$$
f'(L_fw_\theta)''
=\{A_f(f'w_\theta''-f''w_\theta')\}',
\qquad A_f=6f'f'''-2(f'')^2.
\tag{22}
$$
任意允许的全局光滑 $w_\theta$ 都可跨平台，未要求逐微包紧。积分(22)到一个完整活动包的两端，flat $f$ 使右边端值为零。故每包全部相位的总通量不变。原 incoming 规范的特定 $w_c$ 也是这种变化。

因此若两个原总通量在一个所选包中不同时为零，任何允许的同一 $w_\theta$ 都不能把整个第四 period 消去。这里不为一个一般固定 $w_\theta$ 虚构 universal profile 算子，也不说辅助自然查询本身随着 $w_\theta$ 改值；不变量是(16)的实际同圆通量。

## 7. 非零第五矩可与原新母选择及十九个目标共存

对一个已经冻结的圆，不能为使用(20)而临时改母函数。下面只证明 R405 原**新存在选择**可以从起点保证所需非零性。

令 $\psi=\psi_3$，保持 R405 的同一限制 affine 空间
$$
\psi+C_c^\infty((-1/2,1/2))_{\rm even}.
\tag{23}
$$
$M_5$ 是这个空间上的连续五次多项式。对任意允许的内区方向 $e$，
$$
DM_5(\psi)[e]
=5\int(\psi'')^4e''
=5\int((\psi'')^4)''e .
\tag{24}
$$
记 $c=e^{-3}$。直接在中心使用
$$
\psi''(0)=-6c,\qquad
\psi'''(0)=0,\qquad
\psi''''(0)=36c
$$
得到
$$
((\psi'')^4)''(0)=-31104c^4\ne0.
\tag{25}
$$
取一个支撑足够小的非负偶内区方向，(24)非零。因此 $M_5$ 在(23)上不恒零；此论证没有评价 $M_5(\psi)$ 的数值或符号。

R405 §1 已在同一个空间中选择真限制最大 $\mathcal F_{\rm rat}$ minor 和全部十九阶主方向的有限见证。把(24)的方向加入这个有限母参数空间，再把 $M_5$ 作为一个非零多项式因子加入原有限乘积。乘积仍不恒零，所以任意小的参数邻域内都有
$$
u_0=\psi+v_0,\qquad
M_5(u_0)\ne0,
\tag{26}
$$
同时满足所有原非零 minor。取足够小的 $C^4$ 邻域，仍保持原正单峰、固定共同外区及恰一对简单 $A_f$ 零点。

接着执行 R405 原有限脉冲与同 $\mathcal F_{\rm rat}$ 纠正。所有实际最终母形在固定有限正幅盒内满足
$$
\|U_{i,N}-u_0\|_{C^2}=O(N^{-1/2}),
\tag{27}
$$
且十九个**完整**量在一个有限 $N$ 上准确为零。由于 $M_5$ 在共同固定支撑上对 $C^2$ 连续，可把这个最终有限 $N$ 同时取得足够大，使全部有限个 $U_{i,N}$ 均满足
$$
|M_5(U_{i,N})-M_5(u_0)|
<\frac12|M_5(u_0)|.
\tag{28}
$$
原有限根在所有充分大的 $N$ 存在；(28)没有要求再动已经求出的十九个值。未修改的母包同样满足(26)，所有实际副本仍同步修改。

因此确有一类 R405 原结构的新圆：原矩、复制、共同外区和十九个局部目标都成立，但每个上述八末包选择均落在(20)的实际 period 障碍中。这个结论说明那些已付局部门不足以完成 full period，没有撤销它们本身。

## 8. 对旧冻结圆的必要条件与下一真实入口

不预先知道某个旧最终母形的 $M_5$ 时，不作非零断言。若它在(15)的实际正时长几何上还要求全部第四 period 总通量为零，则(9)、(18)、(21)直接迫
$$
\boxed{
M_5(U_{\rm last})=0
}
\tag{29}
$$
对每个可作上述八复制选择的真实末包母形成立。即使该母形的物理宽度与其它最终块不同，正宽因子也不改变(29)。

(29)只消去自然平移的最高系数；低于七次的完整系数仍可能非零。反过来不能从 $M_5=0$ 推全部平移查询为零，更不能推原有序总通量、内部部分通量、平台仿射量或十三行 joint 已付。

本稿也未排除：在初选阶段以准确 $M_5=0$ 的新母函数另作同点有限构造，改变复制架构，或不用 whole-pure-zero 背景的其它实际路径。对 $M_5=0$ 的新母构造，必须重新核原限制最大 minor、同一个 $\mathcal F_{\rm rat}$ 纤维以及全部十九个真实量；不能把(28)的非零开条件改名为零条件。

本次闭合的是一个有限实际输出像：在明确的八个现有末包及非零第五矩范围内，原正字符已经下降到真实同圆 period 总通量，并且所有允许的二阶 gauge 都看不见这个正读出。
