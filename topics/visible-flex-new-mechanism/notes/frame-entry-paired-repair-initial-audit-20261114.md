# 固定选中度量的成套入口修复：独立实现与初态审计

状态：新模块和完整审计主路径仅在人工输入上检查通过；尚未评价本课题的真实选中候选。本文件不记录新的等距、嵌入或 reach 结论，也不把入口 leading 修复当作已完成的 Cauchy 延拓。

## 1. 这次只改变入口表示

公开实际 `actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json` 已把原来的大缺口明显降低，但最细径向/角网格上的实际度量算子误差仍约为 $0.714$，峰在 $t=0.105$；曲率峰在 $t=0.0975$。两者相对开核终点 $t_c=0.036$ 分别为 $0.069$ 和 $0.0615$。原始 JSON 的字节身份和全部旧源码由公开回执及独立 provenance 审计锁定。

本次严格重放那个报告后，保持其已冻结的完整 $a(t)$、准确椭圆核 $A=1,B=7/25$、六帽及原始 $c_0$ 锚不变。162 个剩余参数的 binary64 值也原样使用，但在下述新入口基场与加权自由空间中解释。**这是新物理场的初态，不是原场在同一空间中的精化**。没有优化步骤，没有重新设计 $B$，没有重选度量系数。

共同高度使用已独立发布的固定分区原函数评价器，消除查询径向网格改变积分分区的问题。新入口修复与该数值评价修正分别记录：旧选中场先用固定原函数重放，再与新入口场在同一网格上比较。

数学依据为 [R64](../results/R64-convex-core-entry-seventh-tangent-and-sixth-center-jets.md) 及已冻结的 [成套修复设计](elliptic-entry-paired-base-repair-design-20261114.md)。准确六帽和全帽法弦预算仍引用 [R44](../results/R44-S9-six-cap-exact-embedding-and-normal-chord.md)；这些局部帽证书没有自动扩展到连接区。

## 2. 新场的准确定义

记 $x=t-t_c$，本次固定支持长度

$$
\ell=\frac{81}{500}=0.162.
$$

它等于旧径向样条的两个结点间隔。取 $\chi=1$ 于 $0\le x\le\ell/3$，在 $\ell/3<x<\ell$ 上取

$$
\chi(x)=1-S_9\!\left(\frac{3x/\ell-1}{2}\right),
$$

在入口方向以外取零。平台截止点是 $t=0.09$，支持结束点是 $t=0.198$。这只是针对实际峰位置选择的首个明确有限支持，**不假定七阶截断在整个 $0.162$ 范围已逼近真实延拓**。

设 $u_0,v_0,b_0$ 为原始不可变 $c_0$ 自然帽参考场；当前选中参数与 $c_0$ 的 $u,v$ 系数差分别为 $d_u,d_v$。令 $J_j$ 表示右侧入口 Taylor 截断，并设

$$
a'(t_c+x)=-C x^3+O(x^4),\qquad
U_4=-\frac{C k_\theta}{4a_0 k^2},\qquad
V_7=\frac{\mathrm{side}\,C^2 k_\theta}{7a_0 k^3},\qquad
B_6=-\frac{\mathrm{side}\,C^2}{2}\langle k^{-2}\rangle.
$$

新固定基场为

$$
u_* =u_0+\chi\,[u_{\rm core}+U_4x^4-J_4u_0],
\qquad
v_* =v_0+\chi\,[V_7x^7-J_7v_0].
$$

现有原始基场的 $U_4$ 已准确嵌入，其其余非入口桥函数从五阶起；原 $v$ 固定基场在入口邻域为零。因此实码只需减去原 $c_0$ 的 $u$ 样条三、四阶项及 $v$ 样条三至五阶项，再加入完整函数 $V_7(\theta)x^7\chi$，没有把 $V_7$ 裁成有限 Fourier 模。

新高度固定速度为

$$
b_* =b_0+(B_6-b_{0,6})x^6\chi,
\qquad
b_{0,6}=-\frac{\mathrm{side}}2\langle\beta_3^2+v_3^2\rangle.
$$

$\beta_3,v_3$ 来自原始 $c_0$ 的完整入口场，不来自本次选中参数。两个角平均在物理定义中均是准确积分，数值角节点数只属评价身份。

令

$$
W_p(x)=1-\chi(x)+\chi(x)(x/\ell)^p.
$$

全部当前参数场为

$$
u=u_*+W_2\sum_j(d_u)_j B_j,\qquad
v=v_*+W_5\sum_j(d_v)_j B_j,\qquad
b=b_*+W_4\sum_j c_j C_j.
$$

旧自由基在入口均为 $O(x^3)$，故新自由项分别从 $x^5,x^8,x^7$ 起；它们不会再覆盖已支付的 $U_4,V_7,B_6$。入口之外 $W_p=1$，切向场与所有局部速度导数恢复原选中场。共同 $z$ 原函数的新增积分只留下一个常量高度平移。因此尾部原有实际度量/曲率误差不会因这一局部入口修复自动下降。

## 3. 原函数、Jacobian 与身份

新中心函数只由一个全局积分给出：

$$
z(t)=z(0)+\int_0^t b_0(s)\,ds
 +(B_6-b_{0,6})\int_0^t x(s)^6\chi(s)\,ds
 +\sum_j c_j\int_0^t W_4(s)C_j(s)\,ds.
$$

第一项积分复用 `frame_fixed_height_primitive.py` 的固定结构结点加均匀分区；其余是逐片多项式积分。加权高度基在每片的次数不超过 18，十点 Gauss 在准确算术下精确；当前 binary64 实现仍保留舍入误差，不把这句话当区间证书。查询点只查询固定 prefix 和本片局部积分，不重分长区间。

当前参数的全位置二 jet Jacobian 使用新的 $W_2B_j,W_5B_j,W_4C_j$ 及其导数和共同原函数。旧通用切向 helper 的最后 $T_{ss}$ 基列直接读取原始共享 $B_{ss}$；独立新模块仅为这项补上新旧加权 $B_{ss}$ 的差，不修改旧文件。高度参数对 $X$ 的导数是新 $\int W_4 C_j$，对 $X_s,X_{ss}$ 的导数分别是 $W_4 C_j,(W_4 C_j)'$；没有误用“高度 evaluator 修正不改 Jacobian”来忽略新基改变。

源样条浮点入口由 `cf*L` 计算，准确有理入口转 float 可能相差一 ulp。实码在源样条自己保存的左结点取右 Taylor 导数，避免落在 `extrapolate=False` 的定义域之外；物理结点仍由原准确身份定义。这一细节在人工主流程中确实暴露并修复，未改任何真实报告。

新身份含完整原始模型、准确 $c_0$、支持长度、权重、准确角函数/平均定义、新高度基和完整冻结 $g$。GH、角积分、固定分区和 Gauss 阶均单独属于评价配置。新旧场身份不同；所有评价精化实例必须保留同一个新物理身份和同一组准确有理参数。

## 4. 人工检查及其范围

`frame-entry-paired-repair-check-20261114.json` 使用人工温和椭圆和小参数。六个位置量 $X,X_s,X_\theta,X_{ss},X_{s\theta},X_{\theta\theta}$ 的方向 Jacobian 相对差最大约 $1.26\times10^{-8}$；directmetric/ball-strip Jacobian 相对差约 $7.24\times10^{-9}$。加权高度原函数的差分导数误差约 $8.83\times10^{-12}$。

同一人工点的核心完整二 jet 不变；稀疏与稠密查询的六位置量差为零。入口外非位置导数差不超过 $2.13\times10^{-12}$，位置扣除一个共同竖直平移后的差小于 $1.7\times10^{-16}$。完整冻结度量字典逐项相同。

`frame-entry-paired-repair-audit-check-20261114.json` 另外执行与正式研究相同的完整主路径：严格原报告载入、旧/新粗细网格、完整端口查询、角加倍、五项独立评价精化、原子 JSON 保存及读回。全部通过，优化器调用和参数步数均为零。这不认证真实候选，不认证任何连续求积误差，也不说明新表示会改善实际残差。

## 5. 公开 Actions 初态审计

新主脚本 `scripts/frame_entry_paired_repair_audit.py` 只允许在公开 Actions 中评价研究输入。本轮无非线性 solve。原始选中报告及原始 $c_0$ 报告须先通过旧 18 源 SHA、准确参数、完整模型/度量/空间与输出 raw SHA 的重放验证。

审计依次保存：

1. 同一查询无关原函数下的旧选中场与新入口场粗网格结果。
2. 同一 $121\times384$ 网格的两场实际 $E,F$、曲率、面积、ball/strip、signed height 和入口/主体/补丁分区极值。
3. 固定参数 $121\times768$ 及完整端口插点；四稀疏/全查询的共同高度一致性。
4. 五个相互隔离的评价精化：入口准确平均节点数、固定分区 Gauss 阶、固定 Gauss 阶下分区数、原始 $b_0$ 角平均节点数、无限热定义的 GH 阶。每个实例逐项检查物理身份不变。

每完成一项即原子保存；所有比较都标记为有限数值差。旧 $R$ 不重新作为目标。这里也不把有限空间的线性预测当作改善，因为没有应用任何一步。

高度筛单独输出共同帽高 $h$、全场采样最小 signed height、镜合内盘法弦上界 $|h|$，以及准确核心点与六帽顶点的两法向公式。对当前 $B=7/25,R=137/500,w=1/50,\tau=61/1000$，若完整 C² 嵌入和所要求 reach 都成立，标准正帽高须满足

$$
h\ge \frac{81+\sqrt{3685}}{1000}.
$$

该式使用准确几何点；**把一个未认证数值 $h$ 代入仍只是诊断，不能据此宣布严格 reach 排除**。当前审计不加高度罚项，也不把不同径向尾圈分别平移。未来若采用高度约束，它对当前独立高度系数是一个全局线性条件，梯度为 $\mathrm{side}\,I_j(L)$。

公开运行命令（输入 SHA 由 workflow 同时钉住）：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_entry_paired_repair_audit.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json \
  --anchor-input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --expected-input-sha256 c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46 \
  --entry-length 81/500 --entry-mean-nodes 1024 \
  --uniform-panels 120 --primitive-order 8 \
  --refined-panels 240 --refined-order 12 \
  --radial-nodes 121 --angular-nodes 384 \
  --out "$RUNNER_TEMP/frame-entry-paired-repair-initial-audit.json"
```

## 6. 下一判断只依赖真实输出

若入口缺口仍大，要区分有限 leading 截断、支持区截断及主体变量相容性，不能据人工 Jacobian 通过就重复求解。若新场破坏帽高或球/条带预算，要保留真实高度与共同积分证据，不能靠每片重平移消掉。局部入口之外的补丁仍有独立缺口；本次数学修复只消除了一个已明确的有限入口 Taylor 表示障碍。
