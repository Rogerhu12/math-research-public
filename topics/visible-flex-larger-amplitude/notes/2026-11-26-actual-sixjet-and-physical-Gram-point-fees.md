# 同一完整 hDelta 场的六个导数与物理 Gram 点态费用

日期：2026-11-26。完整实现 [so3_axisymmetric_sixjet_point_fees.py](../scripts/resume_20261126/so3_axisymmetric_sixjet_point_fees.py) 为 40459 字节，SHA256 `ceb5d63b0ec19f1fc63295f177be1ebb76656082d86eb3fc12497d0c9ce66db1`。它消费实际 606/7f 完整场及其准确固定目标，把已经分别完成的节点、整段带符号积分、core/cap 与 R694 代数接为同一场的六导数和三项归一化 Gram 费用。

本件尚未在科学运行中执行；静态审查不充作费用数值。当前03b实际候选最大度量误差约0.515，故参数只待用，未把这个高误差场送入昂贵完整认证。完整连续曲面、几何、全t以及精化责任仍须在合格候选上支付。

## 1. 完整输入与准确对象

所有组件使用同一个 `ActualInput`、同一个 `NodeOutwardEvaluator` 和同一个完整 `7f26` 算子对象；禁止将另一场、另一 profile、另一固定材料图的盒或工作值混入。源码逐文件严格绑定：

| 完整组件 | SHA256 |
|---|---|
| 实际节点及 SO3 四 jet | `1371e4936af27d2122a84bb720e8c67db5d0db712df42eec12a4579f91943f89` |
| 全圆正性、core 真逆与 cap | `69c5aae0dea9c15645a4484b3e4bfe9d6809f2a922763ca91c623774fd1e4bb2` |
| 同场完整带符号积分 | `1a46002ad6b1763479340b4f16472983c88d4f11c6530ce5465f78bfc64c3c4b` |
| 完整 hDelta 物理场 | `7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf` |
| R694 准确误差代数 | `30ae7dc70ea836ab6f30e34b9b886f968c6e61c6646c807cd96a8611029c2636` |

实际参考、carrier、scalar输入、原节点、preparation/report/checkpoint及完整canonical模型也全部经原组件绑定。固定 target 为

$$
g=ds^2+a(s)^2\rho_0(\phi)^2d\phi^2.
$$

这里的 $\rho_0$ 是固定参考材料图；当前自由 core 改变的是真逆映射与内部曲线，不改变 $g$。本件保留原全部 omega/core/H，没有删除原坐标或切换观察测度。

carrier 的全部7377个 `a_observations` 与 `a_observation_absolute_error` 由原完整4e源产生；后者在生产时向上取工作word，故取每一真实字面值为有理数后，$[\hat a-e_a,\hat a+e_a]$ 是准确同一 $a$ 的有效盒。入口检查实际文件身份、数组形状、finite、非负误差、全部工作 $a$ 与当前算子一致及严格正下界；不能用另一个数值目标重算分母。

## 2. 同一角批与完整积分

`prepare_core(phi)` 必须在1a46组件已经完成同一角批的全部922胞之后执行。入口和每次 `evaluate` 再次检查 `.complete` 以及全部角的逐字 `float.hex()` 相等。即使数值比较把正零和负零视为相同，也不能据此混合不同字面请求。积分换角批后旧 core/cap 工作数组立即失去调用资格。

core/cap 组件先为当前与固定两条曲率半径各自建立严格正下界，随后用真方程残差盒与全正导数包围同一个实lift根。它输出的真盒与实际六个工作数组之差已经包括完整逆图、三角函数、准确半径carrier及向量算术。$\Gamma$ 使用普通法向角frame，$P$ 使用固定材料角frame，两者不混用。

完整积分给三个角导阶的有理中心 $\widehat I_j$、整段误差 $e_{I,j}$、当前点带符号积分中心与误差。它们来自真实所有节点及完整 signed Peano；未完成全部胞时不允许读取 totals 或查询点。

## 3. 准确 lift 及闭合差费用

每个原物理查询位置有准确符号表示 $s=\alpha S+\beta$。用

$$
u=\alpha+\beta/S,\qquad
h=1-10u^3+15u^4-6u^5
$$

求真盒，并保留

$$
h'=(-30u^2+60u^3-30u^4)/S,\qquad
h''=(-60u+180u^2-120u^3)/S^2.
$$

$S$ 的完整准确盒来自同一个实际scalar输入。原 `make_query` 的三个工作word与真盒逐个比较，得到 $e_h,e_{h'},e_{h''}$；不把工作网格跨度或存储长度当准确 $S$。

对 $j=0,1,2$，准确闭合差为

$$
\Delta_j=\Gamma_j-P_j+\int_0^S T_j\,ds.
$$

原 `q._integrate` 对1a46保留的真实节点工作数组重新按原顺序规约，再与原 core/cap 工作word组合，得到实际 $\widehat\Delta_j$。将其与准确有理向量

$$
\widehat\Gamma_j-\widehat P_j+\widehat I_j
$$

比较，得到完整闭合加减与浮点规约误差 $e_{\Delta,j}^{\rm arith}$。因此

$$
e_{\Delta,j}=e_{\Gamma,j}+e_{P,j}+e_{I,j}
 +e_{\Delta,j}^{\rm arith},\qquad
D_j=|\widehat\Delta_j|_{\rm upper}+e_{\Delta,j}
$$

分别是闭合差误差和真 $|\Delta_j|$ 上界。这里没有假设 $\Delta=0$，也没有从单位 $T$ 推出完整场 $|F_s|=1$。

## 4. 完整六导数剩余算术

真实完整物理场由原7f `fields_torch(...,curvature=True)` 独立读取，完整得到

$$
F,\ F_s,\ F_\phi,\ F_{ss},\ F_{s\phi},\ F_{\phi\phi}.
$$

不能假设本次不同batch的工作word与原优化时逐位相同。对每个实际输出，将它与下列由已绑定组件的字面word构造的准确有理向量比较：

$$
\begin{aligned}
F_{\phi^j}:&\quad \hat h\widehat\Gamma_j+(1-\hat h)\widehat P_j
 +\widehat{\mathcal S}_{\hat h}[T_j],\quad j=0,1,2,\\
F_s:&\quad\widehat T+\widehat h'\widehat\Delta_0,\\
F_{s\phi}:&\quad\widehat T_\phi+\widehat h'\widehat\Delta_1,\\
F_{ss}:&\quad\widehat T_s+\widehat h''\widehat\Delta_0.
\end{aligned}
$$

这里 $\widehat{\mathcal S}_{\hat h}$ 使用同一个真实查询、全部积分节点、真实 partial weights 与字面 $\hat h$。准确有理 $1-\hat h$ 不能被未付误差的另一浮点表达代替；完整输出对有理中心的距离会支付原计算这一步以及其余全部算术。所有向量距离用96bit向上平方根，没有声明一个未经证明的机器epsilon界。

R694 随后逐项加入输入费用。对于三个角阶，完整误差为

$$
e_{F_{\phi^j}}=e_j^{\rm arith}
 +|\hat h|e_{\Gamma,j}+|1-\hat h|e_{P,j}
 +e_{{\rm signed},j}+e_hD_j.
$$

其余三个为

$$
\begin{aligned}
e_{F_s}&=e_s^{\rm arith}+e_T+|\widehat h'|e_{\Delta,0}+e_{h'}D_0,\\
e_{F_{s\phi}}&=e_{s\phi}^{\rm arith}+e_{T_\phi}
 +|\widehat h'|e_{\Delta,1}+e_{h'}D_1,\\
e_{F_{ss}}&=e_{ss}^{\rm arith}+e_{T_s}
 +|\widehat h''|e_{\Delta,0}+e_{h''}D_0.
\end{aligned}
$$

原全部normalization、准确Hermite宽、三角函数和Exp费用由1371节点消费者支付；所有有理中心到实际完整输出的剩余差在本件支付。没有假定任一尚缺来源的费用为零。

## 5. 真固定分母与全三项物理 Gram

令 $d=a\rho_0>0$，真盒来自同一个 $a$ 盒与固定材料图的 $\rho_0$ 盒。若局部 $\rho_0$ 盒下端不正，仅允许与已经独立证明的全圆严格正盒取交；交集异常则拒绝，不删除局部宽度。工作分母 $\hat d$ 是本次真实完整 `fields_torch` 返回的固定 $\rho_0$ word与原 $\hat a$ 的真实乘积word。

本件读取物理相对Gram

$$
\widehat A=\begin{pmatrix}
\widehat{|F_s|^2-1}&\widehat{F_s\cdot F_\phi/\hat d}\\
\widehat{F_s\cdot F_\phi/\hat d}&\widehat{|F_\phi|^2/\hat d^2-1}
\end{pmatrix}.
$$

没有角轨道重数，没有用于残差向量打包的 $\sqrt2$ offdiagonal因子。将全部字面 $\widehat F_s,\widehat F_\phi,\hat d$ 在 Fraction 中代入同一公式，和三个实际Gram工作word相减，得到对称误差矩阵 $E_{\rm arith}$。完整谱算术费用取

$$
e_{\rm arith}=\max(|E_{11}|+|E_{12}|,\ |E_{12}|+|E_{22}|),
$$

所以不会把一个标量entry误差误称整个operator-norm误差。

若 $U\ge|\widehat F_s|$、$W\ge|\widehat F_\phi|$，真分母下界为 $d_->0$，$\delta d=\max(|d_--\hat d|,|d_+-\hat d|)$，则

$$
V=W/\hat d,\quad e_v=e_{F_\phi}/d_-+W\delta d/(d_-\hat d).
$$

写 $e_u=e_{F_s}$，由 R694 得三个非负entry界

$$
A=2Ue_u+e_u^2,\qquad
B=Ue_v+Ve_u+e_ue_v,\qquad
D=2Ve_v+e_v^2.
$$

完整Gram谱误差为

$$
e_G=\min\left\{\frac{A+D+\sqrt{(A-D)^2+4B^2}_{\rm upper}}2,
\max(A+B,B+D)\right\}+e_{\rm arith}.
$$

对实际工作矩阵三个word $e,f,g$，其准确谱范数为

$$
\frac{|e+g|+\sqrt{(e-g)^2+4f^2}}2.
$$

96bit向上平方根与减去 $2^{-96}$ 的非负下界给严格上下盒；再上下加减 $e_G$，得到同一准确场的真实相对Gram范数上下界。某已处理点的严格下界超过阈值可反证该场满足整面阈值；有限点全部上界小于阈值仍只认证这些点。

## 6. 完整CLI、恢复与公开范围

默认覆盖全部原7377个观察地址与原513个quarter-angle工作地址；外层angle block8，内层observation block32。可通过明确schema提供原观察整数索引与canonical角hex，只声明该有限集合。不能把重复地址当新增覆盖。每次先完整全圆chart正性，再准备该角批922胞积分和core，随后才读取完整场。

每个完整point block把实际六导数、全部分项费用和完整Gram盒写在runner的gzip文件中，再写带输入/来源/查询身份的hash-chain journal。恢复逐块核文件SHA、literal地址、完整scope、六项与Gram最大值，复用已提交块；新执行调用计数与历史已处理块分开。尚未处理任何点时，各点误差最大值为 `null`，不把空集合当已知零误差。若外部中断恰发生在raw原子写完而point journal尚未登记之间，本版本遇到该未登记raw会拒绝覆盖并报错；这会阻断该次恢复，不会丢弃或伪造已支付数据。积分组件自身已支持相应逐胞原子孤块恢复。

600秒是自然准入预算；部分积分或部分点直接返回可继续的真实计数，不称完成。即使默认所有有限点全部完成，`continuous_metric_or_geometry_certified` 与 `closed_isometry_accepted` 仍为false。尚需对合格候选接连续空间误差、全部接缝/帽、全t几何和固定参数实际精化。这个组件也不适用于把5b4零闭合修正场当作原7f场；零闭合分支须独立接其真根与隐式导数误差。
