# R715 — 参考中心化 normal 表示：准确等价、完整六 jet 与工作误差账

2026-11-26，Astra-larger-e4e2a2bf-20261126 / geometry。

**状态：完整源码只读及解析评估；没有科学执行，没有改动当前入口、原32个共同阶段、变量、观察行、永久点或完成标准。** 本文说明一种独立数值表示如何与 R703/R707 的准确 normal 选择相容。准确参考的存在、唯一分支及连续误差仍使用 R708/R709/R711/R713 的真实适用条件；这里没有把尚未返回的参考场或当前长时间运行归因为数值瓶颈。

## 1. 已核的真实实现及问题位置

本次读到的完整小源为：

| 完整源 | SHA256 |
|---|---|
| supported_unit_meridian_reference.py，39826字节 | 30ea80ec0673f3bdff3e59b97dfb5f7166a296aeb4b989fbca18b2feb5e9544c |
| so3_supported_unit_meridian_operator.py，40705字节 | e1bb7303540b1e807176ca5e71dcb2798b3f1e4e34909cd207cea300a9d4ebc0 |
| so3_supported_unit_normal_lift_operator.py，91472字节 | 5297192216356970140585eb9e56c521d9f35453211fb5a76086b713350eaa67 |

这些文件均小于100KB；只读源和文本，没有读取大 raw 报告。R711 平滑三角后继若采用本方案，也必须独立绑定其实际完整新源，不能以本表冒称已经审过未知后继。

5297 的 _closure_jets 是 $(\Gamma-P+Q_ST)/S$；fields_torch 返回 $P+Q_sT-Q_ST$，而径向导数直接返回 $T,T_s$。这里 $Q_s$ 是原每胞 Gauss 数据的累计前缀和部分 Lagrange 原函数规则，$Q_S$ 是同一规则的完整积分。其参考 provider 自己的端层分片、中央80节点或后继192节点规则并不等于这个原胞规则。因此参考在另一规则中达到工作均值容差，不会使这里的完整闭合残差逐字为零。

e1bb.make_query 中名为 h 的量实际是 $1-S_5(s/S)$。下文使用从0升至1的 lift

$$
\ell(s)=S_5(s/S)=1-h_{\rm source}(s).
\tag{1}
$$

相应 $\ell'=-h_{\rm source}'$、$\ell''=-h_{\rm source}''$。不能把两种 h 的端值或符号混用。

## 2. 冻结对象与准确中心化恒等式

固定准确参考 core $c_0$、高度 $H_0$、材料图 $\theta_0$、准确同一 $a,R,S$，以及完整固定参考 $T_{\rm ref}(s,\phi)$。设它已满足其定义所需的条件，并在整个角圈具有同一分支及所需角二 jet，且

$$
|T_{\rm ref}|=1,\qquad
\int_0^S T_{\rm ref}(s,\phi)\,ds=P_0(\phi)-\Gamma_0(\phi).
\tag{2}
$$

(2) 是 R708/R709 参考构造的准确结论，不是任何一次打印的有限均值残差。对新参考的全域适用条件与误差尚未支付时，后面的准确等价须明确标为以(2)为前提。

令 $x$ 为全部原外自由变量，$u(\phi)$ 为同一条 meridian 的完整六控制；$T(x,u)$ 包含原全自由旋转、当前控制和固定参考。原闭合量与中心化量分别为

$$
\begin{aligned}
C(x,u)&=\Gamma_x-P_x+\int_0^S T(x,u)\,ds,\\
C_c(x,u)&=(\Gamma_x-\Gamma_0)-(P_x-P_0)
 +\int_0^S\bigl(T(x,u)-T_{\rm ref}\bigr)\,ds .
\end{aligned}
\tag{3}
$$

由(2)逐项相加，$C_c=C$。该等式同时适用于两阶角导数、原全部外参数的一阶导数及 normal 所需的混合导数，只要相应经典导数存在并有合法积分交换。冻结参考不随当前 $x$ 改变，因此

$$
D_x C_c=D_x\Gamma_x-D_xP_x+\int D_xT,\qquad
D_u C_c=\int D_uT.
\tag{4}
$$

没有丢掉全自由 core 的隐式逆图导数、自由 H、omega 或上游 normal 控制的导数。

如果当前初点恰为这个冻结参考点 $x_0$，且外旋转与控制均为0，则 $C_c(0,x_0,\phi)=0$。这只适用于真正的参考初点。显式修改 H、从别的完整 checkpoint 开始或换 core 后，仍须用原固定 $\Gamma_0,P_0,T_{\rm ref}$，不得把当前点重新命名为参考以消掉真实闭合失配。

## 3. 工作差分规则及初点精确零的合同

用帽号表示实际工作载体。定义同一完整规则下的参考缺陷

$$
\widehat\delta_j
 =\widehat P_{0,j}-\widehat\Gamma_{0,j}
    -Q_S\widehat T_{{\rm ref},j},
 \qquad j=0,1,2,
\tag{5}
$$

下标 $j$ 指角导数。实际中心化闭合量为

$$
\widehat E_j
 =(\widehat\Gamma_{x,j}-\widehat\Gamma_{0,j})
  -(\widehat P_{x,j}-\widehat P_{0,j})
  +Q_S(\widehat T_j-\widehat T_{{\rm ref},j}).
\tag{6}
$$

数值实现应先在每个完整节点形成差，再按同一规则归约；不能假定分开计算两次大积分再相减与该规则逐位相同。

若初点、固定端点和参考节点的值与角 jet 确实使用同一完整求值路径/字节，则(6)的各项在初点是同字减同字，故可以得到完整角批次上的工作零。为使这句话可复核，至少要绑定：

- 固定参考 provider 的完整 source/model/input、原 $c_0,H_0$ 与原初点摘要；
- 相同的物理 mesh/width carrier、Gauss节点和权、归约规则、角列表及角 jet 阶数；
- $\Gamma_0,P_0$ 必须是同一当前 core/cap 公式在冻结点的工作求值，不能将 provider 的 NumPy端点与 operator 的 Torch逆图端点未经误差付款混为逐位相同；
- 同一固定参考缓存须与外点缓存分开；换当前 $x$ 不重选参考。order升级保原0/1阶字，不从不同角批次或不同 source 借值；
- 若 Rodrigues 的零旋转组合或逆图的前向路径没有实际给出相同字，应保其真实差额，不因理论零、容差小或观察到近似而强置零。也可以完整派生一个代数差分 Rodrigues/逆图实现，但那是需独立核全导数的新源。

这里的“工作零”是所定义规则的结果，不是准确(2)或完整连续费用的证书。有效的误差账仍须包括每条实际求值路径。

## 4. 只改闭合方程会造成何种不一致

若用(6)求根，却仍把旧 cap-anchored 数值场

$$
\widehat P_x+Q_s\widehat T-Q_S\widehat T
\tag{7}
$$

与 $\widehat F_s=\widehat T$ 原样返回，那么在精确的线性规则算术中，根 $\widehat E=0$ 给出的 core值是 $\widehat\Gamma_x+\widehat\delta$，不是 $\widehat\Gamma_x$。这个参考积分缺陷未必等于求根容差。

因此不能仅在 _closure_jets 减去固定残差，而把物理六 jet、core握持、幅度 witness 或现有 geometry guard 当作自动保持。所有真实值和导数都必须来自同一个完整数值重建合同。

## 5. 一致方案A：固定参考 lift

在精确的工作规则算术中，定义

$$
\widehat F^{\,A}
 =\widehat\Gamma_x+Q_s\widehat T+\ell(s)\widehat\delta_0 .
\tag{8}
$$

其完整近似六 jet 应为

$$
\begin{aligned}
\widehat F^{\,A}_\phi
 &=\widehat\Gamma_{x,1}+Q_s\widehat T_1+\ell\widehat\delta_1,\\
\widehat F^{\,A}_{\phi\phi}
 &=\widehat\Gamma_{x,2}+Q_s\widehat T_2+\ell\widehat\delta_2,\\
\widehat F^{\,A}_s&=\widehat T+\ell'\widehat\delta_0,\\
\widehat F^{\,A}_{ss}&=\widehat T_s+\ell''\widehat\delta_0,\\
\widehat F^{\,A}_{s\phi}&=\widehat T_1+\ell'\widehat\delta_1.
\end{aligned}
\tag{9}
$$

若 $\widehat E_j=0$，端点为对应的 $\widehat\Gamma_{x,j}$ 和 $\widehat P_{x,j}$。有限根残差不为0时，帽端差额正是 $\widehat E_j$，另加真实算术费用；不能把其角1/2阶分量漏掉。准确层面 $\delta_j=0$，故(8)–(9)回到原准确单位径向场。

固定 $\widehat\delta$ 的全部外参数导数为0；但当前 $T,\Gamma_x$ 及完整根链的导数照旧存在。工作 $\widehat F_s$ 不再是单位向量的恒等式。必须继续实际读取完整 E、B、C 三个Gram分量，不能沿用一个未限定范围的“径向Gram恒为0”工作标志。

## 6. 一致方案B：同时支付有限根残差的完整 lift

为保持有限根残差下的端点合同，更直接的方案是

$$
\widehat F^{\,B}
 =\widehat\Gamma_x+Q_s\widehat T
   +\ell(s)(\widehat\delta_0-\widehat E_0).
\tag{10}
$$

角1/2阶分别使用 $\widehat\delta_j-\widehat E_j$；径向一阶、二阶和混合阶也将(9)中的 $\widehat\delta_j$ 换为此量。**不能在AD图中 detach 当前 $\widehat E_j$**。它包含全部当前变量、当前控制及上游 normal 链；固定参考项才是常量。

把 $Q$ 看作同一线性规则时，

$$
\widehat\delta_j-\widehat E_j
 =\widehat P_{x,j}-\widehat\Gamma_{x,j}-Q_S\widehat T_j.
\tag{11}
$$

因此(10)恰是完整原 closure-lift 形式：

$$
\widehat F^{\,B}
 =(1-\ell)\widehat\Gamma_x+\ell\widehat P_x
   +Q_s\widehat T-\ell Q_S\widehat T.
\tag{12}
$$

e1bb的原hDelta实现已有这个结构，令其 $h_{\rm source}=1-\ell$ 即逐式一致。这里仍需使用 **normal 修正后的** $T,T_\phi,T_{\phi\phi},T_s$，不能误用 base 的未修正 meridian。

实际浮点归约并非严格线性。实现可以直接以(12)及同一已算 total 重建场，这最少改动物理路径；(11)作为分析等式，其不同括号下的真实舍入差另外计费。不要把 $(Q(T)-Q(T_{\rm ref}))$ 与 $Q(T-T_{\rm ref})$ 的机器结果假称完全一致。

在准确参考和准确末阶段根成立时，$\delta=E=0$，方案A、B与原准确 normal 场相同。有限求根误差时，A、B相差 $-\ell\widehat E$ 及相应五个导数。方案B把这项显式纳入所筛查的工作场，端点和全六 jet 一起保持相容。它没有放宽root验收，也没有将一个失败root冒称可用场。

建议先采用(12)作为新独立入口的物理重建，完整真实读出 Gram、曲率、幅度和永久点；这是复用现有完整lift代数的最小方案。该选择尚未实施。

## 7. 端口、准确尾与对称

(1)满足 $\ell(0)=0,\ell(S)=1$，且一、二径向导数在两端为0。因此校准对端点的径向一、二阶和混合 jet 不增加错误的边界项。角值由前节的完整端点式决定。R708既有 core反射与帽端接合条件仍需对同一准确参考/当前omega执行，不能由本小改动自动证明所有前提。

若希望工作校准完全不进入深谷末端，可另选固定 $\ell$：在一个远离core和cap的已固定内部区间 $[a,b]$ 上取 $S_5((s-a)/(b-a))$，此前0、此后1。其一、二阶导数在区间端口为0；在cap侧(12)精确回到旧 cap-anchored 形式，校准不额外改变该侧的径向导数。准确 $\delta=E=0$ 时无论哪种lift都同原场。内部短lift会放大导数费用，必须如实比较，不能只为隐藏尾误差而不付款。

对升段长度 $L_\ell>0$，有

$$
|\ell|\le1,\qquad
|\ell'|\le\frac{15}{8L_\ell},\qquad
|\ell''|\le\frac6{L_\ell^2}.
\tag{13}
$$

这些是可用的完整上界。原全域lift取 $L_\ell=S$。新的内部lift必须作为明确的新数值规则/参数记录，不能静默改变当前源。

冻结参考和两个端点若满足既有的polar反射/半周/周期协变，且完整径向规则与角无关，则(5)–(12)同样协变。角一阶随反射取负号、二阶不取负号，全world正交变换保留。不能把有限角独立求根的偶然近对称当作准确全角同支；共同分支与角拼接仍由R703/R707及参考证书负责。

准确场未变并不赋予未认证的工作场全t reach、无自交或幅度证书。R248等既有相位消费的真实条件仍照原条目逐项支付；本条不重证它们。

## 8. normal 选择与全部一阶参数链

新完整阶段方程应全部采用同一中心化量，包括零控制target：

$$
C_c(u_i,x)-(1-\tau_i)C_c(0,x)=0,\qquad
u_i=u_{i-1}+A_{i-1}^{\,T}\eta_i,\quad
A_{i-1}=\partial_u(C_c/S)(u_{i-1},x).
\tag{14}
$$

不能一部分阶段使用旧未中心化target，另一部分使用新差分。仍用同一共同准确分段、全部六控制、每阶段三根及完整角二jet，全上游 $D A_{i-1}$ 链保持。

由(4)，在同一准确点的 frame 与旧方程相同；准确阶段方程也相同，所以在已声明的同一唯一性域/所选分支内，准确normal选择不变。在工作层，新的常量偏移可能改变所走分支，这是独立数值scheme，应记录自己的source/model/work-rule身份，不能冒旧run的控制或证书。

初点工作target确为0时，$u_i=\eta_i=0$ 是各阶段的候选，但**不能据此删除32阶段、强置旧root记录或跳过隐式矩阵可逆性**。即使forward根为0，一阶外参数响应通常非零；准确零支的公式含完整 $A(\phi)$ 与 $b(\phi)=f_xh$，角一、二阶还含它们的全部角导数。已有C1缓存讨论只在其严格同字/同图合同下适用，不由本条授权缩减链。

当前 _implicit_jet_value 给的是数值根处完整方程的一阶隐式线性化，不是有限Newton迭代图；本方案必须保持这个区别。方案B的 $-\ell E$ 也走同一完整AD图。所有 full-space QP、H2母范数、正mu、原C、PhaseI、SOC和真实筛均保留。

## 9. 完整误差账：先给不依赖取消的安全界

令准确参考为(2)的那个对象，准确当前控制是与工作根正确关联的同一分支。把 R707 根/角jet传播与 R710/R713 参考费用合并后，设已有同场上界：

- $e_j(s)$ 包围当前 $\widehat T_j-T_j$，$j=0,1,2$；
- $e_s(s)$ 包围 $\widehat T_s-T_s$；
- $A_j(s)$ 包围 $Q_s\widehat T_j-\int_0^sT_j$，包括完整参考/旋转/root节点误差、部分规则误差、真宽度/节点carrier与全部归约费用；
- $G_j,P_j$ 分别包围当前core/cap角jet工作误差；
- $D_j$ 是(5)实际固定字向量范数的向外上界，$R_j$ 是实际 $\widehat E_j$ 范数的向外上界；
- 所有真正六jet末端加减乘及lift工作值/导数的误差另记 $\varepsilon_\bullet$。

在准确 $\delta_j=E_j=0$ 的前提下，对方案B可用 $H_j=D_j+R_j$。方案A取 $H_j=D_j$。于是

$$
\begin{aligned}
e_F(s)&\le G_0+A_0(s)+|\ell|H_0+\varepsilon_F,\\
e_{F_\phi}(s)&\le G_1+A_1(s)+|\ell|H_1+\varepsilon_{F_\phi},\\
e_{F_{\phi\phi}}(s)&\le G_2+A_2(s)+|\ell|H_2+\varepsilon_{F_{\phi\phi}},\\
e_{F_s}(s)&\le e_0(s)+|\ell'|H_0+\varepsilon_{F_s},\\
e_{F_{ss}}(s)&\le e_s(s)+|\ell''|H_0+\varepsilon_{F_{ss}},\\
e_{F_{s\phi}}(s)&\le e_1(s)+|\ell'|H_1+\varepsilon_{F_{s\phi}}.
\end{aligned}
\tag{15}
$$

如果实际用(12)直接求值，亦可用其逐项 $G_j,P_j,Q_s,Q_S$ 的真实误差界；两种合法界可取较紧者，但不得在无共同依赖信息时假设误差抵消。

上式没有要求先证明 $\widehat\delta$ 很小才能执行求解。其实际字范数在准确(2)成立时就是偏离准确零的直接上界；不过这不支付 $\widehat T_{\rm ref}$ 自身的误差，更不替代准确参考存在/同支的前提。若该前提还未付，只能把(15)作为条件接口。

所有范数必须统一为vector Euclidean和对应induced operator范数，或明确付从coordinate infinity到Euclidean的转换。不得把矩阵/张量最大单元素当完整算子范数。

## 10. 中心化误差可怎样更紧，以及现有producer未支付什么

准确 $C_c=C$。对其工作误差，一个完整三角上界是端点差分误差，加上

$$
\bigl\|Q_S(\widehat T_j-\widehat T_{{\rm ref},j})
 -\int_0^S(T_j-T_{{\rm ref},j})\bigr\|,
\tag{16}
$$

再加真实浮点差分/归约费用。可以直接对完整差分integrand用R694 Peano账，也可分开包两项；只有真实共同分割、相同输入与严格代数消去允许更紧的取消。不是在两个已失去相关性的独立interval盒上任意消公共误差。

当前construction的准确均值producer所针对的对象是

$$
L_c\widehat v+\int_{\partial U}
 N((1-\chi)T_0+\chi N(\widehat v))
 +\int_{U^c}T_0-P_0+\Gamma_0
\tag{17}
$$

及其两total角jet。它的中央 $L_c\widehat v$ 是均值方程定义；它不自动等于实际 provider 使用 $\widehat\lambda,\widehat d,\widehat w$ 和另一套节点逐项生成的中央积分。R713真实profile矩误差、lambda/d/w/根三jet误差，以及参考在outer原胞Gauss/cumsum上的完整规则误差须另行接入，才能支付(5)与(16)。不能把(17)的已包残差直接当 $\widehat\delta_{\rm ref}$ 的完整付款。

部分原函数同样需要独立费用：当前 _integrate 的 $Q_s$ 是Gauss采样的多项式原函数规则，而 direct $T$ 是非多项式场的直接求值。数值返回的六jet是对同一准确连续场六jet的近似；它们不是自动等于“把有限浮点 $Q_s$ 当定义后再精确微分”的六jet。若要另定义一个有限多项式场，就必须真正返回该多项式的导数并重新付端口/Gram，这不是本方案。本文保持原准确连续模型，使用R694/R707对这些近似逐项付款。

## 11. 更完整的基线原函数方案

若能独立提供同一准确固定参考的原函数

$$
F_{\rm ref}(s,\phi)=\Gamma_0(\phi)+
 \int_0^sT_{\rm ref}(v,\phi)\,dv
\tag{18}
$$

及两角jet，那么准确场也可写成

$$
F(x,u;s,\phi)=F_{\rm ref}(s,\phi)
 +(\Gamma_x-\Gamma_0)
 +\int_0^s(T(x,u)-T_{\rm ref})\,dv.
\tag{19}
$$

其径向导数仍是 $T$。这能把一般的当前求积负担变为差分integrand；初点只读固定参考primitive。完整可执行实现需要reference primitive在所有grid与任意永久点都可求值，并给全角/全部径向piece、准确尾、全部0/1/2角jet及carrier费用。

中央可利用当前准确profile矩/分段primitive，外补集可复用原准确标量primitive；端层的归一化blend一般仍需要完整向外积分，不能假设存在已刊闭式。当前30ea只给四个T参考jet，**并没有提供这个完整primitive接口**。因此(19)是可实行的更大后继，不应在本次小改动中用一个插值数组冒充。

也可以先用(8)作为工作reference primitive，再在(19)只积分差分；那仍需在其径向导数保留 $\ell'\widehat\delta$，不能借“reference primitive”名称重新把工作Fs冒单位。

## 12. 最小完整实施边界与结论

一个合格独立后继至少需要同时修改/绑定：

1. 完整新normal source的reference差分data、全部closure/target角jets与source/model身份；
2. 同一当前修正后T的六jet物理重建，优先复用(12)完整lift；真实closure_defect与centered_root_residual分别记录，避免混同；
3. 完整frozen-reference工作记录：原初点、provider、角/规则、基线端点及delta三jet；只runner保存可重算raw，公开紧凑身份/真实标量；
4. 新geometry/driver/reader的严格source边界，保全部原变量、原C、完整历史、N及正权目标；工作径向Gram恒等旗标改为false，准确数学旗标只在明确原根条件下陈述；
5. 失败仍保实际report；同字零未实现、参考根/角jet失败、normal矩阵失败或实际几何失败均如实返回。没有增加预先fixture，没有放宽根/几何门。

本方案不会证明当前root失败全是求积偏差，也不会据等待时间断言预期提速。它提供一个准确上等价、工作上完整且可支付误差的新数值表示；是否改善真实可执行性，须由独立新source的实际完整方向回答。
