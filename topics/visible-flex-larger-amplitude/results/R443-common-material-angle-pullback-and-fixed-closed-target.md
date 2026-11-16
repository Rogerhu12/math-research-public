# R443：固定首个材料图的共同角拉回与同一闭目标度量

作者：ChatGPT /root（AI协作）。日期：2026-11-16。本文是来源核对和条件纸证；没有执行数值、求逆、编译、区间覆盖或新的科学检查，没有生成实际闭面或宣布加密收敛。

## 1. 问题与实际来源

同一准确连续 C、同十个参数，并不保证两个实际450解在同一个旧 q 图中具有相同目标系数。原 saved-prefix 从当前 checkpoint 取全部112个 core 词，再构成材料角。它们是本次解的未知数，不只由十个标量参数给出。因此直接拿新解的 q 图替换旧图，会改变目标中的材料角因子。

本次逐段核读以下原源；没有修改这些冻结文件：

| 来源 | bytes | SHA256 |
|---|---:|---|
| [R400 saved-prefix](../computations/geometry_20261115_continuous_ten_frozen450_saved_prefix.py) | 18759 | 1c7a2e1c39b0066ae7149ef2e35ff6936a70601f0545369848f04716ad8b4520 |
| [R413 cuff/target atlas](../computations/geometry_20261115_current_C_original_cuff_target_atlas.py) | 29060 | 02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2 |
| [R418完整相对metric](../computations/geometry_20261115_current_C_ten_complete_relative_metric.py) | 49975 | 28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590 |
| [R409 shared field](../computations/geometry_20261115_current_C_ten450_shared_field.py) | 48583 | 6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3 |

原 saved-prefix 的 self.core 来自 checkpoint.arrays["core"]，频率为2至224，density为 $(1-(2m)^2)c_m$。原定义同时写明完整材料角公式与准确公共坐标 $u$。R418 的完整目标范围明确为：前缀 $(L_{\rm true}/L_{\rm numeric})^2$ 及 $a_{\rm true}^2\Phi_q^2$，径向 $E_C(r)$ 及 $r^2\Phi_q^2$，两帽为完整笛卡尔图上的 $I+Db_\pm\otimes Db_\pm$。

R413还明确记录 cap_height_does_not_enter_the_metric。帽高是图的常数平移，不改变 $Db_\pm$。W是R249型几何修补的构造参数，也不因此替换R418原目标为当前诱导metric。README要求冻结参数、尾和帽时仍须保所选W/H及完整构造；不能把这项实验责任与“所有这些参数各自都进入g”混为一谈。真正已确认的材料系数差来自当前core与 $\Phi$。

R409的原inlet normalization实际改变首节点三个jet块，明确不继承原prefix metric证明；原单一SE2 registration也需真实记录。下述拉回不使这些当前场操作自动获得误差证明，不删除原R249/R416/R418责任。

## 2. 完整材料角与严格正性

以 $j=0$ 表示首个真实构造的参考图；$j$表示同一准确标量目标上的后继场。允许未来明确实现的 $M_j$ 不同，当前冻结源码实际仍为112，本文没有把它改成一般M运行件。

按每个实际core的全部准确二进有理词定义

$$
\Phi_j(\phi)=\phi+
 \sum_{m=1}^{M_j}\frac{(1-4m^2)c_{j,m}}{2m}\sin(2m\phi),
\qquad
\rho_j(\phi)=\Phi_j'(\phi)
 =1+\sum_{m=1}^{M_j}(1-4m^2)c_{j,m}\cos(2m\phi).
$$

设对每个所用场已有真实有效的严格全圆下界

$$
\rho_j(\phi)\ge \beta_j>0.
$$

则 $\Phi_j$ 是实解析、保向的圆周提升，满足

$$
\Phi_j(\phi+2\pi)=\Phi_j(\phi)+2\pi,\qquad
\Phi_j(\phi+\pi)=\Phi_j(\phi)+\pi,\qquad
\Phi_j(-\phi)=-\Phi_j(\phi).
$$

它的实轴逆唯一，且具有相同提升／反射对称。当前1c7源码已有原R237的准确有理充分界：从完整参考core下界减去完整系数差的加权绝对值和；若该界非正，原源码只报告材料逆前提未付，不推原BVP被拒。此处直接沿该既有前提，不新增solver接受门，也不把离散角采样当全圆严格正性。

将实际使用的单位周期坐标写为 $q\in\mathbb R/\mathbb Z$，定义

$$
\Theta_j(q)=\Phi_j(2\pi q).
$$

公式中的 $2\pi$ 不能遗漏。以后带撇的 $\Theta_j$ 导数均对q；若使用 $\rho_j'$，则其导数对物理角 $\phi$，两种记法不能混用。

## 3. 从首图到当前图的准确方向

从首个参考q图到第j个场自身q图的映射是

$$
\psi_j(q)=\Theta_j^{-1}\bigl(\Theta_0(q)\bigr).
$$

这里 $\Theta_j^{-1}$ 的值是单位周期q坐标，输入是提升物理角。反向映射才是 $\Theta_0^{-1}\circ\Theta_j$。二者不能在实际evaluator中互换。

$\psi_j$ 与径向变量、前缀变量及运动时间t无关，并且

$$
\Theta_j(\psi_j(q))=\Theta_0(q),\qquad
\psi_j'(q)=
 \frac{\Theta_0'(q)}{\Theta_j'(\psi_j(q))}>0.
$$

它保整数提升、半周期提升和反射：

$$
\psi_j(q+1)=\psi_j(q)+1,\qquad
\psi_j(q+\tfrac12)=\psi_j(q)+\tfrac12,\qquad
\psi_j(-q)=-\psi_j(q).
$$

因此原完整周期端点与两反射片都保留；不是选择一个方便角区间而丢掉边界。

前缀统一使用准确公共 $u$：第j个数值坐标为 $s_j=L_{{\rm numeric},j}u$。即使不同实现的数值长度词不同，也不应把两个s数值区间当同一个物质坐标。真实准确 $L_{\rm true}$、$a_{\rm true}$、完整十参数、cut/cuff与原C语义必须相同；长度重标不是允许重选目标。

## 4. 同一个完整目标度量

固定同一个原准确C对象及标量十参数，记对应自然长度为 $L$、准确前缀半径为 $a(Lu)$。若原C绑定只给完整root family，以下命题逐个固定成员成立；不由坐标论证选择某个未给出的成员或证明唯一性。

第j个场自身图上的前缀目标经 $s_j=L_{{\rm numeric},j}u$ 写为

$$
g_j^{\rm pre}=L^2\,du^2+
 a(Lu)^2\,\Theta_j'(q_j)^2\,dq_j^2.
$$

径向活动区的原目标为

$$
g_j^{\rm rad}=E_C(r)\,dr^2+
 r^2\,\Theta_j'(q_j)^2\,dq_j^2.
$$

令活动区坐标映射为 $T_j(u,q)=(u,\psi_j(q))$ 或 $T_j(r,q)=(r,\psi_j(q))$。由第3节的准确恒等式，

$$
T_j^*g_j^{\rm pre}
 =L^2\,du^2+a(Lu)^2\,\Theta_0'(q)^2\,dq^2
 =g_0^{\rm pre},
$$

$$
T_j^*g_j^{\rm rad}
 =E_C(r)\,dr^2+r^2\,\Theta_0'(q)^2\,dq^2
 =g_0^{\rm rad}.
$$

在每个固定帽的笛卡尔坐标 $X=(x,y)$ 上，取 $T_j(X)=X$，完整目标仍为

$$
g_\pm^{\rm cap}=I+Db_\pm\otimes Db_\pm.
$$

必须固定两帽完整marker函数 $b_\pm$，包括全部中心、半径、幅值、所在帽及重叠求和。不能用一份source名代替这份真实定义。

**共同闭流形上的拼接。** 第j个活动区的cuff角到笛卡尔帽图的过渡为

$$
X_j(r,q_j)=
 r\bigl(\cos\Theta_j(q_j),\sin\Theta_j(q_j)\bigr).
$$

首图采用 $X_0$。准确等式 $X_j(r,\psi_j(q))=X_0(r,q)$ 表明活动区的 $T_j$ 与帽图恒等映射在整个原平坦cuff重叠环上一致；它们给出共同闭流形的同一个光滑图变换。无需把一个非线性角换元径向延伸到帽中心，后者通常会在中心破坏可微性，不能代替上述图册论证。

原R413的完整cuff条件 $E=1,E_r=E_{rr}=0$、实际marker与cuff严格分离、原上下反射及R416 cut图责任仍分别使用。坐标恒等式不替代尚未证明的接缝或原准确C前提。

**命题。** 在上述明确同目标、完整正材料逆、共同帽图及原接缝前提下，所有 $T_j^*g_j$ 都是首图上的同一个完整 $g_0$。这允许每次BVP自由重新求自己的全部core；不要求把新core强制等于首core，不更改原求解器问题，也不以两份core不同拒绝新解。

## 5. 原相对metric界经合同变换保持

设第j个实际闭族为 $F_{j,t}$，定义共同物质图上的族

$$
\widetilde F_{j,t}=F_{j,t}\circ T_j.
$$

如果原完整消费者实际证明

$$
-\eta\,g_j\preceq
 F_{j,t}^*e-g_j
 \preceq\eta\,g_j
$$

对全点、全t成立，则合同变换直接给出

$$
-\eta\,g_0\preceq
 \widetilde F_{j,t}^*e-g_0
 \preceq\eta\,g_0.
$$

这是对双线性型的准确合同不等式。等价地，令 $J=DT_j$，则 $J^{\mathsf T}g_jJ=g_0$；相应归一化缺陷矩阵由一个正交矩阵共轭，故其相对算子范数不变。无需因q缩放放宽原 $\eta$，也不能把坐标分量的绝对误差直接当相对算子误差。

所以已真正支付的原四个Loewner测试，可以在相同完整定义下解释为首图的同一个相对界。该结论不预付任何原测试；当前没有一份本题完整闭面metric通过记录，也没有从部分盒、旧场或局部角度借通过。

若实际新实现直接在共同q图中形成jets，必须以完整准确拉回求这些jets，并保原所有闭片、端点、两反射及全phase。不能只把目标中的 $\Theta_j'$ 改名为 $\Theta_0'$ 而保未拉回的场；那会变成另一个未经证明的误差问题。

## 6. 全像几何、固定H与全时间正则性

每个 $T_j$ 是整个共同闭流形到第j个图册的满射微分同胚，因此对每个t，

$$
\widetilde F_{j,t}(M)=F_{j,t}(M).
$$

下列几何量不因这次准确重新参数化而改变：完整像集直径D、reach、整像到基准像集的距离，以及允许平移／旋转／反射后的整像差异。对固定帽图内部选定的同一个H，$T_j|_H$ 为恒等，所以原逐t固定H性质与该H的像集直径也保留。若H选在活动区，则须明确取 $T_j^{-1}(H_j)$；不能不声明便把不同物质区域叫同一个H。

这仅是同一个j的参数化不变量。不同j的实际像集和D仍可能不同，每次README比例、全像held、含反射的 $\delta_E$ 和reach责任必须真实支付，旧j的数值界不自动转给新j。

由于 $T_j$ 与t无关，原 $t\mapsto F_{j,t}$ 的强 $C^2$ 连续性经固定光滑复合保持；局部注入、全局嵌入、闭合和连通性在已经成立时同样保持。本文不从局部度量或材料逆单独推出全局嵌入。

跨j的 $C^2$ 收敛也不是该命题的结论。每个 $\beta_j>0$ 不自动给出统一正下界；若逆的导数越来越大，原坐标中的小差不能不加控制地转成共同图中小差。后继必须在共同图、相同全时间范围和明确的全局刚体规范下比较全部所需jets，保原网格/M/尾步/角精化责任。不得由native residual下降、BVP接受或source一致直接声称强 $C^2$ 收敛。

## 7. 可执行消费者需要的完整导数责任

前两阶准确关系为

$$
\psi_j'=\frac{\Theta_0'}{\Theta_j'\circ\psi_j},
\qquad
\psi_j''=
 \frac{\Theta_0''-
  (\Theta_j''\circ\psi_j)(\psi_j')^2}
 {\Theta_j'\circ\psi_j}.
$$

对任何当前坐标中的向量值分量 $V_j$，

$$
\partial_q(V_j\circ T_j)
 =(\partial_{q_j}V_j)\circ T_j\,\psi_j',
$$

$$
\partial_q^2(V_j\circ T_j)
 =(\partial_{q_j}^2V_j)\circ T_j\,(\psi_j')^2
  +(\partial_{q_j}V_j)\circ T_j\,\psi_j''.
$$

径向／u及运动t的混合导数遵守同一链式法则，因为 $\psi_j$ 不依赖这些变量；$s_j=L_{{\rm numeric},j}u$ 的常数因子仍须完整保留。

若原六jet/曲率消费者需要更高q导数，令 $B_{n,k}$ 为通常的偏Bell多项式，由隐式恒等式得到

$$
\psi_j^{(n)}
 =\frac{\Theta_0^{(n)}
 -\sum_{k=2}^n
   (\Theta_j^{(k)}\circ\psi_j)
   B_{n,k}(\psi_j',\ldots,\psi_j^{(n-k+1)})}
 {\Theta_j'\circ\psi_j},\qquad n\ge2.
$$

相应场的第n阶q导数必须保完整Faà di Bruno和，而非只留最高阶项。实际区间逆像要包住整个原闭角区间，严格正分母下完整包围各导数，保周期接缝、反射、所有原当前栈与资源未访范围。本文没有实现或执行这个逆查询器，没有给某个未来误差位数或预算承诺。

即使原场在自己的角变量有有限频带，非线性 $\psi_j$ 复合后一般不再在共同q上保持同一有限频带。不能用原M格点、FFT截断或忽略高阶混合项代替所需全角证明。原两mean、全部物理行、全部core和当前实际场数据都必须保留。

## 8. 必须保存的真实定义与当前缺口

首个本job构造应形成明确的定义来源：完整准确C/标量目标和十词、实际自然／数值长度约定、首core的全部准确词与材料公式、完整marker定义及帽图、实际W/H与所选尾帽、原writer/checkpoint和source/run身份。首core是之后材料图的定义参数，不应把可重算大场或大证书混入该参数收据。

后继仍独立记录自己的真实core、正材料逆前提和实际registration/inlet normalization。重求registration或修改inlet场不等于重选目标；各自引起的真实几何与误差责任按原R409/R249/R416/R418全域消费者支付。不得以“已冻结source”代替这些实际数据，也不得把source级坐标命题写成实际消费者已经使用了 $\psi_j$。

当前R437准备首构造与定义收据；原R438两分支并不自动执行共同材料拉回。R441的N/尾步/角度和R442的完整M维数实现须显式消费上述定义并使用方向正确的图变换；新的来源、specification SHA和完整新场结果各自独立。本文不改当前运行，不预填这些新源码或实际场已完成。

本题仍仅有已接受的M96开放前缀。完整非零112场、原112/338/fullDN终门、完整闭面全t metric/reach/held/反射责任，以及同一g上的真实全部精化，仍按[open](../open.md)与[HANDOFF](../HANDOFF.md)继续。
