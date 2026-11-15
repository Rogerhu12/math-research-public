# R323 连续 C 基底上固定 support1/power4 的十坐标接入设计

作者：AI（amplitude）。日期：2026-11-15。  
状态：纸面与原源码接口设计；没有新科学请求、运行、参数选择或接受场。Request178 的八件冻结源不变，也不预填未来178或176结果。

## 1. 最小方案与已读来源

在同一个已绑定的 R300/R323 **准确新基底** $A_*(s)$ 上，保全部九个连续族控制，只加一个明确的新坐标 $\xi$。新增函数采用零起始编号 support_index=1、power=4 的形式；其实际支持来自该新基底的第一速度过渡段，而非旧 finite-Gauss 表的 turn 支持。

这能在准确表达层保持同一个 $a,a',a''$，不复用 R298 的提前选段、clip 或独立 ap/app 标签。它仍是不同于164/178有限旧基底的目标族：旧参数至多作为明确初猜，旧 mesh、基底表、J、尾响应、merit、FD和域记录均不能改名继承。

| 原件 | 字节 | SHA256 |
|---|---:|---|
| [R298](../results/R298-original-finite-Gauss-clip-seam-and-same-target.md) | 15097 | 55f0c6ac9f3b4ecf1ea173c8f62438aac012cda077312128d2596d3abea54af9 |
| [R300](../results/R300-continuous-nine-control-scalar-family-and-cut-calibration.md) | 20787 | 5df99d5de2296fe830b8a51e76f27ea41cce217dd343a9803f7f1a830fec3147 |
| [R323](../results/R323-finite-cut-boxes-and-explicit-uniform-dyadic-windows.md) | 8532 | 3830f0cb1b5ecd4bd4382826068721551140392cb3a29639e2cd9bb308e0922d |
| geometry_20261115_continuous_nine_scalar_factory_v3.py | 42270 | 0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e |
| geometry_20261115_continuous_nine_scalar_numeric_v3.py | 22469 | 7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60 |
| geometry_20261115_continuous_nine_augmented_v3.py | 6138 | d86f6fdf3cf59df3d45c907c655fe54ab830180facd27b7402e649b2e14d151b |

这些文本已实际读取并作字节身份计算，未导入、构造或执行任何数学模块。

## 2. support1、准确自然长度和来源

164/178 的冻结09240b33 family实际定义 CATALOGUE 为三个零基支持与 powers(3,4)的有序积，所以 catalogue index3对应(1,4)。不能将这个1误读成 R300 公式中的第一支撑 $I_1$。

准确 factory 的 build_expression 构造：

| 零基索引 | 物理支持 | 准确来源 |
|---|---|---|
| 0 | $[\ell_0,\ell_0+w_0]\Subset(0,L_0)$ | 原真实 first_support 的 left/stored_width |
| 1 | $[L_0,L_0+\delta_A]$ | tree.constant(end) 与 tree.constant(da) |
| 2 | $[S_1,S_1+L_C]$ | 同一表达树的 $S_1=L_0+\delta_A$ 与准确 $L_C$ |

故本设计固定
$$
\ell=L_0,\qquad w=\delta_A,\qquad x=\frac{s-\ell}{w}.
$$
R323 具体公式选择 $\delta_A=\delta_B=e>0$ 为严格向下的 dyadic。它来自真实 core/cut 包围，不能拷贝178旧turn宽度，也不能因数值节点无法区分就截大。若沿一般原recipe则保其明确正 $\delta_A$；实际执行 R323 时保同一个 $e$。

完整基底仍由同一累计式给出
$$
L_C=\frac{R_A-R_B+I_A+I_B}{\kappa},\quad
S_1=L_0+\delta_A,\quad S_2=S_1+L_C,\quad
S_3=S_2+\delta_B,\quad L_*=S_3+d.
$$
$L_C,L_*$ 保原 $E_0,E_1,E_2$ 语义叶的表达身份；不能将当前包围中点或独立舍入末长度代回成“准确相等”常数。基底、cut、根规则/根族、core、宽度及支持在一个十参数模型内先固定，不随控制系数重新选择。

沿用的是 power4 的**形式及逻辑角色**。旧 $h_{\rm old}(s_{\rm old})$ 与这里 $h_C(s)$ 是不同基底、坐标和支持上的函数，不声明同一实体或同一有限响应。

## 3. 全十坐标、真实微分和端点责任

记 $P(x)=64x^3(1-x)^3$、$t=2x-1$。新增函数准确规定为
$$
h_C(s)=
\begin{cases}
w^2P(x)t^4,&0<x<1,\\
0,&\text{其他}.
\end{cases}
$$
内部的一、二阶物理 $s$ 导数来自同一表达：
$$
h_C'=w(P't^4+8Pt^3),\qquad
h_C''=P''t^4+16P't^3+48Pt^2.
$$

两端也定义为0。$P$ 在0、1都有三重零，故零、一、二阶左右极限全为0，准确零延拓为 $C^2$。不使用带容差的提前mask，不把 $x$ clip 回端点。它不必为 $C^3$，本设计不作这种声称。

按原顺序保留
$$
z=(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3,\xi)
$$
并定义
$$
a_z(s)=A_*(s)+\sum_{i=0}^2
[p_{i+1}B_{i,0}(s)+\theta_{i+1}B_{i,1}(s)
+\eta_{i+1}B_{i,2}(s)]+\xi h_C(s).
$$
原九个 $B_{i,k}$ 正是 R300 的准确函数。第一、第二导数为整式逐项微分；第十列完整为 $(h_C,h_C',h_C'')$，不可仅加到半径。$\xi=0$ 精确退化的是**新连续九族**，不是164/178旧有限Gauss九族。

新增支持从 $L_0$ 到 $S_1$，不改变 core 内部或 $L_0,S_1$ 两jet；它在最后过渡/collar/cut的邻域恒为0，故全部原cut三次collar及尾目标两jet恒等保持。特别是
$$
v=-E_0^{-1/2},\quad b=-E_1/(2E_0^2),\quad
q_{\rm cut}=E_2/(2E_0^{5/2})-E_1^2/E_0^{7/2}
$$
及原 cut 多项式 $P_{\rm cut}(\zeta)=R+v\zeta+b\zeta^2/2+q_{\rm cut}\zeta^3/6$ 所给 $E(P_{\rm cut})(P_{\rm cut}')^2$ 的 $(1,0,0)$ 两jet关系不变；这里的 $P_{\rm cut}$ 不与控制多项式 $P(x)$ 混用。

自然长度仍为 $L_*$：它由固定基底累计式定义，控制项端点零jet保相接；不能每改系数就另选长度。任意大十系数的正半径/亚单位速度不由此推出，仍须真实全域评价。若一个九参数点已有准确全域严格余量，则连续性给它新增 $\xi$ 的某个开可行邻域；这不是当前数值范围或新增接受门。

形状在支持1内部与 $k=0,1,2$ 线性独立，不能由此推完整三方程响应补秩。

## 4. 公共材料 u 与有限数值影子

准确公共坐标及目标是
$$
u\in[0,1],\quad s_*=L_*u,\quad
g_*=L_*^2du^2+a_z(L_*u)^2d\theta_{\rm material}^2.
$$
导数合同为
$$
\partial_u a_z(L_*u)=L_*a_z'(L_*u),\qquad
\partial_u^2a_z(L_*u)=L_*^2a_z''(L_*u).
$$
新增支持在公共域是 $[L_0/L_*,(L_0+w)/L_*]$，必须与准确长度表达绑定，不能用旧网格同名 $s/u$ 冒同一材料点。

原numeric v3用当前cut叶盒的中点编译binary64系数和 $L_{\rm num}$，明确只是有限搜索影子。其 jets_u 用 $L_{\rm num}$ 做数值链式变换，导出同时保准确 $L_*$ 表达。新实现应保三层区别：

- 准确定义中的真实语义叶、准确累计长度和准确三jet；
- 独立圆整分段多项式及其形式导数的数值评价；
- 数值系数/长度误差、接缝word比较及仍未付的准确误差外包。

点/batch共用求值体不证明数值影子全局准确 $C^2$ 或等于准确目标。新控制的准确零jet也不修复数值基底的独立圆整接缝；后续同一 $u$ 下的连续metric比较仍须支付这项差别。

系数若来源于持久Decimal字符串，就明确按这些有限字符串定义的准确有理数冻结；若来源于binary64字，就按准确dyadic冻结。数值profile投影词另存，不可先隐式float化再冒原参数。当前尚未选择实际十参数或投影口径。

## 5. 最小准确 factory 接点

采用独立源码/schema，旧0d89370d不改。无需重写 R323 cut 或准确core：

1. build_expression 的独立recipe改为十参数；原 core_pieces、Tree、pieces、cut叶、roots、三supports和构造公式保留。
2. 完整控制描述表为九个旧项加一项，不能将 range(3)粗暴改为range(5)而多出未声明控制：

~~~python
control_terms = [
    {"parameter_index": 3*k+i, "support_index": i, "power": k}
    for k in range(3) for i in range(3)
] + [{"parameter_index": 9, "support_index": 1, "power": 4}]
~~~

3. 原 bump_polynomial(order) 的准确卷积已支持4；同一多项式加 differentiated 形成三jet。piece_range 按10条表取参数，沿原闭支持交集/跨界并0处理。
4. prove_domain 保所有闭pieces、未决叶和未访stack；普通充分区间证书不改成新BVP门。新项与既有support1同端点，无需移动物理分割，但整个支持贡献必须进入包围。
5. definition/CLI 明确十参数、顺序、10项控制表、power4公式/零延拓/支持表达根和新source。真实core、continuous_tail、recipe、根规则及R300/R323责任保留，不能沿nine schema通过旧消费者。

准确 $x$ 使用真实 $s$ 形成；numeric编译后的支持词不能反向替换准确定义。

第十形状为degree10，后续连续目标消费者也必须从同一10项表生成真实多项式和包围，不可让硬锁nine参数/degree≤8的旧schema消费它。冻结后同一目标的再采样保原中心、宽度、十系数和准确长度，不在换网格时重造支持。

## 6. 数值及完整物理流接点

原7cfab12e numeric的具体接点是：

- NumericContinuousNineProfile.__init__ 的9参数/schema/源检查、控制表和compilation身份；
- control_jets 的(3,9)改为新类(3,10)，按上述10项表形成全部列；
- raw_jet 的参数检查和顺序：前九仍按(0,1,2,4,3,5,6,7,8)，最后加 $\xi$；profile、batch、u调用同一个新体；
- export_specification/description 导出完整十系数、准确新族、数值编译、真实长度和支持，不能只修改计数；
- 新 FrozenSevenShapes 固定原六shape加 $\xi$、保前三active；新 FrozenTen 固定全部十系数，两者都从同一新raw体取三jet。

原多项式导数函数可以复用其明确代码。不能使用旧0924的 TenControlProfile(original_nine,3)：其构造要求旧0865的 original_three/bumps，并继承旧有限Gauss基底，语义不同。

原d86f6fdf物理薄层硬锁旧numeric SHA、三个旧class及参数数(0,3,9)。需新增独立薄层绑定新十族/固定视图及(0,3,10)，scalar_jets仍逐实际节点调用新raw_jet，完整FFT、physical、Jacobian和invalid-column政策继承原f76b9c37。不能原样调用旧层后伪改身份。

112模下，全十是设计/响应对象；原三个标量目标的方阵检查用“七shape固定、前三active”的453维视图，全部十系数真实参与。全部冻结后是450维同目标视图。不能把460维十active状态直接送入原453边界合同。

当前C尾的Robin、完整112响应及cut分母须来自同一个明确C目标/当前状态；profile本身不产生它们。不能以原zero-tail anchor J、旧prepared或178固定J支付新C的非线性响应。原fullDN/native、fresh当前H FD、finalJ/audit及完整几何门保持。

## 7. 178 literal层不能直接搬用的位置

178 producer实际调用 family.old.setup，从旧prepared mesh/anchor形成原九模型；再用8cb8352b的 LiteralTenModel(old_model,extended_original_model,...)。这个构造器复制旧 x/h/mid/base/base_mid/J/target/gamma/eh，并核所有非shape数组等于旧九。699节点、原完整112及对角假设都是其真实固定合同。

因此不能只换一个profile对象便称“178改用连续C”。未来须独立建立：

1. 新准确族和明确数值近似层的完整节点、中点、基底及十列三jet；
2. 当前C的真实完整末端响应、目标和cut尺度；
3. 新模型primal/全十forward/FD及全部原full3 merit与真实接受；
4. 新source/schema/input binding，分清从旧链复用的公式与当前数据。

七状态传播、完整112末端公式及R378的线性代数可在前提适用时复用，但旧表和对角性不能由来源字符串代付。若当前C终端是一般完整矩阵，须按完整对象传播，不能借旧exactly_diagonal条件删耦合。

新的很短 $\delta_A$ 可能使相同 $\xi$ 的响应与178旧支持明显不同；函数独立、$w^2$规范化和旧十列有限奇异值都不证明新响应可用。网格也必须实际表示新pieces和支持；不能将旧699点仅改末长度就叫同一profile。这里不预选网格、尺度、半径、lambda或初猜。

## 8. 完成范围与下一实际入口

本设计给出准确函数、同一三jet、两端零jet、公共u/自然长度合同，以及三个v3层和178旧literal层的具体接点。未创建科学workflow、未改冻结源，未重算C/cut/域/J/任何试探，也未增接受前门。

下一独立实现可以在收到真实候选位置后，明确将其十参数作为新连续族初猜，沿同job真实C/core/cut→准确新定义→当前数值profile→完整响应→原求解门推进。178无论是否接受，都不能跳过新目标身份与当前方程责任；也无需把旧有限基底的178成功当作构造这个明确新族的额外前置门。
