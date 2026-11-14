# 当前独立尾参数原生场的薄区间接口与 R125 零端 primitive

## 1. 本件已经提供什么

本件提供**当前场定义的一部分准确区间计算接口**，以及可以接到当前移动角图上的 R125 零端 primitive。它没有给当前强目标候选颁发全域证书，也没有把旧 `NativeLogField` 的结果转记到当前场上。

可用源为：

- `scripts/fd2d_gc_current_native_interval.py`；
- `scripts/fd2d_gc_current_primitive_interval_v2.py`。

第一个模块由已经闭存的 `IndependentTailPositiveTraceNativeField.from_definition` 验证全部原生定义，再只用实际保存的系数、节点、参数、支撑和窗口做本件区间运算。它不以浮点求值结果充当区间输入。第二个模块直接保存准确有理多项式、准确均值和准确两端为零的 primitive。三分量 Gauss–Codazzi forcing、物理材料角与计算角之间的漂移项均保留。

实际小核绑定的原输入是：

```
notes/2026-11-12-fd2d-raw-bump-reuse23-b0004-accepted-0001.npz
SHA256 41b5854938e7273a3109494442e9b96a929f576844b52faf60e96076e407fd82
```

它有 129 个保存节点、31 个 raw／中央角模，54 个参数明确分成中央 `[0,31)`、尾 `[31,47)`、物理 profile `[47,54)`。不存在由 `K+1` 推算尾参数数目的旧解码。入口为已经发布的完整定义：

```
notes/2026-11-12-fd2d-actual-body-native-binding-01-definition.json
```

本件新的 `...current-native-interval-03-definition.json` 包含原完整定义、实际 mesh 的准确有理端点、完整 atlas／R153／R155 窗口定义、原数组和源身份、结构性分片点，以及所有尚未支付的区间项。`binding_sha256` 是本件具体定义包及定位身份的保守绑定；它不声称不同路径、不同字节的定义文档必然得到同一个规范化数学哈希。原有 `locate_bound` 仍以源和输入内容核对定位对象；跨布局复用 primitive 时须先核同一绑定，不能只比较显示名称。

## 2. 为什么旧连续消费者不能直接改一个 factory

| 对象 | 已闭原消费者 | 当前保存对象 |
|---|---|---|
| 径向未知 | `NativeLogField` 的共享值／一导 cubic，变量是 η／ζ | 三独立 raw 分量的保存 P1 系数 |
| 参数 | 旧正 n 消元及旧参数排列 | 中央 31、独立 Bernstein 尾 16、物理 bump 7 |
| 物理径向坐标 | `fd2d-exact-physical-profile-calibrated-clock-v1` | `x=s`，profile 本身含保存的 δ |
| 角图 | 原单一 blend 的 512 模种子图 | R149 的 entry blend／自然 ruling coast／exit blend atlas |
| 实际二基本形式 | 旧 log 场的派生 l | affine lifting + raw P1，随后 R153、R155 非线性表示 |
| cut | 旧对象的 jet 约定 | 准确 tail 角迹；一般径向 II 导数不由 bypass 给出 |

`fd2d-metric-gc-primitive-continuous.py` 仍明确读取旧 log／clock 对象。因此本件没有修改它，也没有复用它的数值报告作为当前对象的证明。[R119](../results/R119-stable-metric-posterior-from-codazzi-defects.md) 与 [R125](../results/R125-cell-primitive-codazzi-metric-posterior.md) 的数学后验适用范围比旧程序广；程序的输入表示范围必须单独补齐。

R164 的 `fd2d_coast_positive_n_certificate.py` 是另一项有用但较窄的已闭消费者：它丢去已证明非负的 plain-tail n 项，给指定保存场的 `raw_P1_n+w*n_ref` 连续下界。它不提供完整 n／m／l 的区间 jet，不提供当前实际 profile 或全部 atlas 的区间。它对某一已闭输入的正性结论也不能仅因新输入结构相同便转用。

## 3. 实数定义与原 P1 全角模

每一个保存的 binary64 节点、Fourier 系数和参数首先读成其准确 dyadic 有理数。显示小数不替代这个数。设实际第 j 个 P1 单元为 `[s_j,s_{j+1}]`，`h=s_{j+1}-s_j`，则一列准确系数为

\[
c(s)=c_j+\frac{s-s_j}{h}(c_{j+1}-c_j).
\]

n、l 使用完整的 `cos(2kξ)`，`0≤k≤K`；m 使用完整的 `sin(2kξ)`，`1≤k≤K`。`raw_box` 返回 value、固定 ξ 的 s 导、ξ 一导、ξ 二导及 sξ 混合导。所有保存模都参与，不使用角采样、不截去小模、不重采样网格。

对一个径向子盒，每列系数关于 s 仿射，因此它的值域包含于两个子盒端点值的 hull。s 导是准确常数。Arb 对完整角区间的三角函数作包含运算，再按准确 Fourier 公式组合：

\[
\partial_\xi\cos(2k\xi)=-2k\sin(2k\xi),\qquad
\partial_{\xi\xi}\cos(2k\xi)=-(2k)^2\cos(2k\xi),
\]

sin 分量同理。有限求和与乘法的区间包含性直接给出五个返回盒。节点处必须指定原单元，返回其单侧 P1 径向导数；程序不把两个斜率平均成不存在的共享导数。

`structural_partition()` 保存准确 mesh、所有保存 bump 支撑、seed 权边界、两个 atlas transition／coast 边界、旧 blend 边界、coast 的准确 rim 边界及保存的显示 plateau 节点、terminal start／ramp-stop／cut。由于目前尚未完成完整 base phase-profile 区间 reader，包明确设置 `base_profile_internal_analytic_pieces_complete=false`；不能把这张结构分片表冒作已经覆盖所有 base profile 内部公式片界的全图。

## 4. 窗口和物理 bump 的区间部分

seed／coast／terminal 的 quintic 权使用原定义

\[
S_5(t)=t^3(10-15t+6t^2),\quad 0\le t\le1,
\]

外部准确夹到 0 或 1。其值单调，故子盒值用准确端点值的 hull；一导使用 `30t²(1-t)²/h`。在跨支撑端点的盒上并入外侧零导数，保真实共同迹。

coast rim 读取原程序实际冻结的标量 `float(reference.length*rim_fraction)`，再作为准确 dyadic 常量。上端读取准确保存的 exit。包同时记录

\[
\text{exit}-\text{entry}-\text{stored length},
\]

而不把这一舍入差写成恒等零。exact plateau 边界和保存的 rounded plateau 标签均登记；后续消费者可以使用共同细分，而不静默跨过一个不同的实数分界。

物理 bump 的准确定义沿保存支撑 `[b_j,c_j]` 为

\[
\psi_j(s)=1024q_j^5(1-q_j)^5,
\quad q_j=\frac{s-b_j}{c_j-b_j},
\]

支撑外为零。`bump_increments` 给出 `Σδ_j ψ_j` 到三阶的区间，它**不是**完整 a 的区间。宽度是两个准确支撑端点的实数差；浮点原函数是该明示解析函数的数值求值，数值求值最后一位不重新定义支撑。导数由有限 Leibniz 公式准确得到：

\[
\psi_j^{(d)}=\frac{1024}{(c_j-b_j)^d}
\sum_{k=0}^d {d\choose k}(5)_k(-1)^{d-k}(5)_{d-k}
q_j^{5-k}(1-q_j)^{5-d+k}.
\]

这里仅暴露某些实际计算所需的三导，没有把全曲面 C³ 当成新门。完整 base profile 的积分常数、phase 片界与 a／a′／a″ 仍须由另一个准确标量 reader 提供。

## 5. 区间 jet 合成、物理角及未提供导数

`Jet` 的槽为 `(value,s,xi,xixi,sxi)`，其中 s 指固定 ξ 的原生径向导。缺少的导数以 `None` 传播；常数才有准确零导。乘法、倒数、平方根、sin／cos 都按链式法则做包含运算。涉及二导的平方用显式非负 square 包围；避免 Arb 通用实幂在含零球上产生 NaN 的已观察行为。

R153 使用完整原背景的

\[
\tilde l=(1-w)l+w\frac{K+m^2}{n},\qquad \tilde n=n,\quad\tilde m=m.
\]

当权和它的一导在盒上准确为零，直接保留原背景；否则区间商必须有实际正的 n 下界。保存的有限求解 floor `.05` **不**代替连续下界。粗盒未给正下界只返回 `UnresolvedInterval`，不是 n 真实变负的见证。

R155 活动内部使用

\[
h=\sqrt{(n-l)^2+4m^2+4K},\qquad
E=\frac w2(h-n-l),\qquad (n,m,l)\mapsto(n+E,m,l+E).
\]

一般平方根 jet 需要该盒实际正的 h 下界。盒靠近零曲率 cut 而未能给出此下界时，本接口不硬套一般导数公式。K_s 未提供时，R155 的 n_s、l_s 也保持未提供；之后需要 n_s 的残差接口会明确拒绝。它不会默写 K_s=0。

设实际材料角 `u=U(s,ξ)`，`H=U_ξ>0`、`v=U_s/H`。准确变换为

\[
f_u=\frac{f_\xi}{H},\qquad
f_{s|u}=f_{s|\xi}-v f_\xi,
\]

\[
f_{uu}=\frac{f_{\xi\xi}-f_uU_{\xi\xi}}{H^2},\qquad
f_{su}=\frac{f_{s\xi}-v f_{\xi\xi}}H
-\frac{f_\xi(U_{s\xi}-vU_{\xi\xi})}{H^2}.
\]

各 atlas 片使用真实单侧 s jet。接口值／角 jet 的共同迹是 R149 已声明的整函数条件，不以 U_s 连续为前提。`physical_jet` 只有在相应盒全部提供时才返回混合导；它不因某个用途无需混合导而添加新的求解要求。

`ProfileBox` 和 `ChartBox` 仅是明确的区间参数接口。调用者必须给出实际完整函数的连续盒。把浮点值放进一个半径零的 Arb 数，不会因此得到其真实解析函数的区间证书。本件的 definition 与返回包持续设置 `continuous_global_certificate=false`。

## 6. cut 全角二阶迹可以单独准确消费

当前 cut 的开放邻域中原角图已经回到 `u=ξ`，保存 cut correction 准确为零，尾使用显式独立 Bernstein controls。因此 `exact_cut_angular_box` 可以不依赖未完成的内部 affine 区间器，直接包围**完整准确 cut 角迹**。

令 `r`、`c`、`b` 是冻结尾对象的 cut_radius、flat_radius、width 常量，`q=(|r sin u|-c)/b`。活动段的曲率为

\[
\kappa(u)=\frac{630}{b}q^4(1-q)^4
\sum_{j=0}^{P-1}p_j{P-1\choose j}q^j(1-q)^{P-1-j},
\]

在 `q≤0` 或 `q≥1` 为零。函数在这些连接点有足够共同零阶数，故其一、二角导通过各片的导数 hull 连续包围。正／负 y 分片分别使用准确符号，跨零区间并入恒零片。最终

\[
n=\kappa\cos^2u,\quad m=-\kappa\sin u\cos u,\quad l=\kappa\sin^2u.
\]

角值、一导、二导全部由同一式得到，包含平尾的零弧和零曲率端点。此方法返回的 s、sξ 均为 `None`。它不声称 cut bypass 的 `E_s=0`，也不证明任意保存内部 R155 场的二阶角迹已经连续收敛到这个值。后者仍需真实一侧控制；参考 R156／R157 的端点论证时必须核对应的实际假设。

## 7. 完整 Maurer–Cartan forcing，包含 Gauss 分量

当前目标是 `g=ds²+a²du²`，当前物理 s 没有旧 clock 缩放。定义

\[
G=ln-m^2-K,
\quad R_n=n_{s|u}-\frac{m_u}{a}-\frac{a_s}{a}(l-n),
\quad R_m=m_{s|u}-\frac{l_u}{a}+2\frac{a_s}{a}m.
\]

`connection_box` 只要求这里真正需要的 n_s、m_s、m_u、l_u；不为了这个后验额外索取 l_s。其完整 skew forcing 为

\[
\mathcal H=a
\begin{pmatrix}0&G&R_m\\-G&0&R_n\\-R_m&-R_n&0\end{pmatrix}
=\widehat{h},\qquad h=(-aR_n,aR_m,-aG).
\]

其中 `hat(z)v=z×v`，重建连接 `A=hat(α)`，`α=(m,-l,0)`。当前实际场不是全域 Gauss 准确解，所以第三 forcing 分量不能删除。两个非线性窗口的 Gauss 恒等式也不等于整个实际闭曲面已满足全部 Gauss 方程。

## 8. 在当前移动角图上保持 R125 的准确零端相消

在准确物理小片 `[s_0,s_1]` 上取 `t=(s-s_0)/h`，`h=s_1-s_0>0`。给定有限准确有理 Fourier 多项式

\[
P(t,\xi)=\sum_{j=0}^dP_j(\xi)t^j
\]

作为完整三分量 forcing 的一个近似。**选取 P 不支付真实误差**；真实 `h_vector-P` 的连续包含须另给。准确均值及 primitive 为

\[
\bar P(\xi)=\sum_{j=0}^d\frac{P_j(\xi)}{j+1},\qquad
q(t,\xi)=h\sum_{j=0}^d\frac{P_j(\xi)}{j+1}(t^{j+1}-t).
\]

全部系数用 `Fraction` 构造，因此

\[
q(0,\xi)=q(1,\xi)=0,\quad
q_s|_\xi=P-\bar P
\]

是准确代数恒等式；全部端点角导也准确为零。程序逐个系数核这个恒等式，并把准确系数写进 primitive packet。端点查询直接返回恒零，不用一个可能因区间依赖而略宽的数替代已知恒等零。

沿固定物理材料角 u，有

\[
q_{s|u}=P-\bar P-\frac{U_s}{U_\xi}q_\xi.
\]

取 `Q=hat(q)`，R125 的修正 defect 方程含

\[
\mathcal E=\mathcal H-Q_{s|u}+[Q,A]
=\widehat{\bar P+(h_{\rm vector}-P)
+\frac{U_s}{U_\xi}q_\xi+q\times\alpha}.
\]

这正是 `conditional_box` 的计算式。省去 `U_s q_ξ/U_ξ` 会改变当前自然 ruling atlas 上的后验，因此该项不可从旧静态角图的程序照抄掉。Gauss 第三分量、commutator 和 `Qe_1` 也都保留；

\[
\|Qe_1\|=\sqrt{q_2^2+q_3^2},\qquad\|Q\|_{op}=|q|.
\]

每个小片的 primitive 两端为零，所以在原 P1／atlas 片界可拼接而不加入假的 primitive 跳量。真实场／角图仍必须符合既有共同值与角迹要求。片界仅有单侧径向导完全允许；这不是一个全局 C³ 或 II 全局 C¹ 新门。

若真实连续包给 `|E|≤b`、`|Qe_1|≤p`，初端 frame 缺陷上界为 d、材料位置切向缺陷上界为 k，则原 skew 传递给出

\[
d_{next}\le d+hb,\qquad
k_{next}\le k+hd+\frac{h^2b}{2}+hp.
\]

在对应正半径下界 `a_*` 下，材料相对 metric 误差可用

\[
2k/a_*+(k/a_*)^2
\]

包围。`propagate_piece_budget` 只做这个条件递推，不能省去真实初端 frame／位置相容缺陷，也不替调用者证明盒覆盖或端口闭缝。

## 9. 实际小核运行与保存的失败

最终入口是 `scripts/fd2d-metric-current-native-interval-check-v3.py`，命令：

```
python scripts/fd2d-metric-current-native-interval-check-v3.py \
  --definition notes/2026-11-12-fd2d-actual-body-native-binding-01-definition.json \
  --out-prefix notes/2026-11-12-fd2d-metric-current-native-interval-03 \
  --precision 256
```

实际 session `82889`，初 tool chunk `86687f`，终 chunk `e1ac92`，自然退出 0。脚本报告 1.6119230900003458 秒，进程峰 RSS 86132 KiB。结果保存于 `...-03-report.json`，`passed=true` 仅表示本件小核通过；该报告明确 `continuous_global_certificate=false`。

本次做了以下必要局部核：

- 对原 saved cells 0／63／73／121 的四个径向盒、完整 31 模及五个 jet，用独立高精度有限求值检查 108 个三分量 jet 点项；未改 mesh 或保存数组。
- 对实际 7 个 δ 的四个物理点，按准确有理 bump 导数公式核对 16 个值／导数。
- 对完整准确 cut 的四个角盒，检查零弧、正／负活动弧、靠近最高点的角值和两导；径向 II jet 继续缺省。
- 对独立的小解析函数核 R153／R155 五个 jet 的链式法则，并核缺 K_s 时不会默赋零。
- primitive 使用原保存数组中的若干准确 dyadic 作为非平凡测试多项式系数，准确核两端零及导数恒等式。它**不是**宣称该测试多项式已近似当前真实 forcing。
- 原 arrays 与原 native definition 的前后 SHA 完全相同。

先前真实失败均保持原字节：

1. 首 checker 在解析阶段因一个未闭括号退出 1（tool chunk `13639b`）；没有读入原保存场或做任何区间数学。原 checker 留存，修复另名 v2。
2. v2 checker 已读实际输入并完成 raw／cut／jet 部分，但 primitive v1 用 `sqrt(sum(square(box)))` 得到非有限值，随后正确拒绝。原因是 Arb 对一个非负值域的 midpoint-radius hull 可带极小负下端，不能直接向 sqrt 传这个球。该实现没有假 pass。新 primitive v2 先取每分量的 `abs` 上端，再平方求和，最后只对非负准确上端开方；这是向外的欧氏范数上界。原 v1、失败报告与 exit receipt 保留。

这些有限比较是实现证据；区间包含性来自前述准确系数和区间运算公式，不来自采样覆盖假设。

## 10. 接往最终后验仍需的最薄输入

本件已经把“用哪个保存场、哪些节点和参数、哪个 atlas／非线性窗口、哪些 primitive 系数”固定下来。下一层须实际提供以下未付盒，之后可以直接调用本件组合式，而不用重新设计 R119／R125 定理：

1. **base physical profile。** 根据原 candidate 明确的 shared Hermite／phase 片与准确积分常数包围 a、a_s、a_ss。在 R155 活动开片真正需要 n_s 时，再给其实际 K_s；显式 phase／bump 可以局部计算所需三导，不增加曲面正则性要求。
2. **full atlas。** 用固定 seed 的准确矩／512 模余项与 R139 ruling 公式，包围 U_ξ、U_s 及所需角 jet；entry／exit 使用整函数凸组合，片界侧迹显式选择。不能把浮点角反解误差或 cached reference 点作为其连续定义。
3. **full affine lifting。** seed、plain tail、frozen coast 全函数先按原权组合，再与 raw 相加，最后在同一盒作用 R153／R155。R164 非负 n 项省略法适合正性下界，却不支付 n／m／l 的完整 residual jet。若仅对独立项粗包围导致严重依赖膨胀，应先在 Fourier／多项式系数层保准确相消，再估共同余项。
4. **真实 forcing remainder 与初端相容。** 每个准确 primitive 片须有完整 `h_vector-P` 余项、域覆盖和一侧 cut 的实际可积控制。保存的小测试 polynomial 没有这项资格。初端 D／C 缺陷、完整 tail 接缝及最终几何要求沿原完成标准继续支付。

因此当前 deliverable 的用途是可绑定、可直接组合的区间构件与准确 primitive；它不把尚未收敛的有限求解场转换为连续证书，也不停止主线的真实求解。
