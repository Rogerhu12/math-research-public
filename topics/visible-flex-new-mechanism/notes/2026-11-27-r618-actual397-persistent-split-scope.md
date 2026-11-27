# R618 actual397：同一冻结 E 的持久分拆参考与硬 τ=1 实际后继

会话 `Astra-new-mechanism-1f4a61a4-20261127`，2026-11-27。
**实际失败驱动的新数值入口；只在公开 Actions 中求解。**
本地仅作纸推、源码/AST、JSON/字节/散列核对，不运行科学。
这里保持 actual397 的完整 q、H、amplitude、全部原口及同一数学目标 E。
独立原方法后来得到的 actual457 及其细峰交换不改变本目标。

## 1. 真正需要修复的已付末态

原首硬 τ=1 范围在 run45914497186/job140230360702 耗时
`41.515274441` 秒，旧 safeguarded Newton 在参考第103点耗尽80步。
随后[显式二分范围](2026-11-27-r618-actual397-bracket-progress-scope.md)的
run45916740129/job140237670198，source
`1aac95c4b2743c88aea569b0bb707b7519c9f2cb`，自然耗时
`42.15573723200001` 秒；这一次全部435次标量调用完成，包含218个参考根和217个试场均值根。
它仍在完整首工作场完成前失败，尚无完整 Jacobian、接受步、fine 或直接位置读出。

其最后参考点是 $r=.22619626838929574$。原归一化参考根显示值为
`1.2862538949645488e16`；原相对宽度停止留下1262宽的括号、
残差 `-314.71875` 和导数 `-.5`。后续参考 λ 小盒因此不包根。
最后显示 halfwidth `2.3283064365386964e-11` 是失败后再除2的记录，
不是已成功支付的分支半径。此前约 `7.50044e9` 的参考根也留下
`.000732` 宽度与 `-.0001829` 残差，试场 λ 曾补偿约 `-.0001828`。

这说明已有二分进度没有解决**大参考中心的小修正分辨**。
不能把 `root_tolerance` 单独调小：在 $10^{16}$ 附近，binary64 本身的单位间距已经大于1。
新范围保存上述两份唯一原 FINAL 的逐字JSON及全部费用，不重播它们的已付诊断。
旧217份成功 mean 数组和参考 target 没有存成可复用科学数组；必要新链重建如实计费。

第二份原日志474141 B，SHA256
`e5310d103c5c2be424ee19576fe4cc637fad433c12cd5d5310b91b7fdf6cee9a`；
原唯一 FINAL 85187 B，SHA256
`d49f8a308347784b78ad5ce7226c8e260311ccefe9b172d9d3b04536dcd1ee1a`。
它完整嵌套首失败35131 B原 FINAL，旧费用不能与嵌套账再次相加。

## 2. 保持原方程的准确分拆

沿用已发布同根分支记号，在 $W\le1$ 的 λ 图中令

$$
v=\lambda+f_r/W,\qquad
n=\frac{(f_\theta/W)^2}{b(r+b)}
 +\frac{r^2(v-1)(f_{\theta\theta}/W)}{b^3},
$$
$$
S_0=-2v+v^2+(v-1)^2f_\theta^2/b^2,\quad
B=2n+W^2n^2+S_0,\quad N=1+W^2n.
$$

这里 $S_0$ 是标量几何平移，和完整位置缺陷 $S=W_*/\sqrt E$ 区分。
参考未知为 $\xi=(e-1)/W^2$。同一有理化均值式为

$$
\Psi(\xi,\lambda)=\operatorname{mean}
\frac{B-\xi}{u(N+u)},\qquad u^2=1+W^2(\xi-S_0).
$$

新目标保存 $\xi=c+\varepsilon$，但每次消费分别形成
$B-c-\varepsilon$ 和 $(c-S_0)+\varepsilon$；不先形成单个binary64的 $c+\varepsilon$。
均值参考和试场根、整个正分支盒，以及输出网格均消费这同一持久分拆。
参考中心不是新的科学参数；它只改变同一个固定目标的数值表示。

所有传入的有限浮点 jets 从 `Decimal.from_float` 精确转换后再构造
$n,S_0,B$ 和标量均值，不能先用binary64形成大 $B$ 再升级类型。
ζ 图亦按相同原则保 $e-1$ 的大中心/小修正，原 $W^2+e$ 几何分拆保留。
参考的 $E_r$、实际 mean connection 和输出状态按新链的明确入口形成。
新connection保留Decimal的 $e,E,e_r,K,Q,D$ 及同一 $s_r$，
输出网格消费持久保存的 `s_r_decimal`，到最终几何数组才转换。
因此不调用旧connection后再从binary64目标重组大项；
归一化 `eta/eta_inner` 设为None哨兵，避免未声明消费者回读展示值。
原位置和完整参数方向公式消费这同一状态。

这仅修复本次实见的算术分辨口。Decimal近似算术没有自动包围旧ODE/DtN/归一化误差、
连续角均值误差或新参考标量算术误差；源码的根宽与传播量均标为观察。

## 3. 参考误差以小坐标预算停止

新策略预先绑定最少80位、最多2048位、30位保护数字；
精度根据实际有限输入数量级及消减需要选择，全部重试/失败计费。
原 `root_steps=80, root_tolerance=1e-13` 仍传入收据并供原core路径使用；
参考和试场的实际新规则分别是最多256和192步，绝对小坐标预算 $10^{-13}$。
它们不再用 $10^{-13}(1+|\xi|)$ 作为大中心的可接受宽度。
这里参考误差传播与试场根宽各有 $10^{-13}$ 的单项观察预算；
若只合并这两项，保守总额是 $2\times10^{-13}$，并未把两项相加后仍称 $10^{-13}$。

在同一正分支上，参考均值函数的能量方向导数为

$$
\partial_\xi\Psi=-\tfrac12\operatorname{mean}(N/u^3),
$$

相应试场坐标导数是原 $c_0/W$；两张已声明图都使用这个同根导数。
将参考能量括号引入实际小坐标时，用当前分支导数下界与真实试场 $x\times\varepsilon$ 整盒的参考能量敏感度 $M_{\rm trial}$ 传播。
新链先按参考导数尺度、`.01` 分支裕量及安全因子8收紧小offset括号，
随后整盒检查实际传播观察是否不超过 $10^{-13}$；失败直接记录，不能静默把参考残差减为0。

完整式与全盒量词见[持久分拆数值链纸证](2026-11-27-r618-persistent-split-mean-chain.md)。
同一方程的符号零、声明绝对宽度达到、数值分辨或最大步数耗尽分别入收据。
这些浮点/Decimal观察不替连续区间证书。特别零响应定义虽保持原精确零修正，
它也从新持久分拆产生参考几何；本次实际硬τ1初态不是零响应，不会进入该捷径。

## 4. 完整消费路径和身份

新独属源码如下，所有旧已发布源码保持冻结：

- `r618_split_reference_mean_chain_20261127.py`：拥有原chain对象的显式Decimal分拆实现，
  原源SHA和完整数值策略进入descriptor；原函数和module全局均不修改。
- `r618_split_reference_model_20261127.py`：拥有唯一恢复的原StableCoordinateHeight，
  新descriptor在原response model SHA产生之前进入policy。
- `r618_split_reference_consumers_20261127.py`：新精确类型/源码/政策guard，
  真实tail producer消费已预绑定政策的实际original对象；direct查询显式接收新chain实例。
- `r618_actual397_split_reference_20261127.py`：只接线这份实际失败来源和新模型，
  继续调用首范围已发布的完整 `.solve`、`.fine_readout` 和source contract。

原完整evaluate仅增加guard、计数的明确命名空间和
`state_on_output_grid` 到新chain的显式转调；全部投影行和位置公式保持。
完整Jacobian仍走原mean/output/position方向链，并消费新evaluate保存的同state。
它仍是原binary64公式评价，包括目标 $e,E,e_r$ 的最终浮点数组；
本范围不称整个Jacobian已作高精度计算，其舍入/消减误差明确未付。
该Jacobian仅产生试方向，每次实际试步接受仍由新Decimal mean/connection全场重算。
积分中的 `_mean_point_query` 通过wrapper的 `_target/_mean_state`，literal-zero也显式走新链。
双直接位置的原 `_query_positions` 已接受chain参数，直接传新实例，
因此所有补充半径使用同分拆；原 stencil、共享查询和所有原fine行不改。

输入绑定同actual397完整1130q源157609 B，SHA256
`79e6d6ce708687decd47fb8eb7a9668f8ca2ebf2351b2f3109fd571c6d692f9c`；
数学场10778 B，SHA256
`12b2113d13bcc20f8c4813c4aac6e8fef6859eb4de7a1271f44770ca793bc952`；
固定目标SHA256
`86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5`。

## 5. 同一实际科学范围

仍从原5893 B实际response JSON起：1473项全部0而最后τ项1，SHA256
`9235b41ebcd2322c2005b542a0548f25db28ee8d2bb0b9cb9b7bcb24b1ebfb4d`。
这是原非零物理阶段，不降τ、不改amp、不重选E，不把原失败转成资格。
初damping仍 `1e-8`，hardτ方向准确消元 $\Delta\tau=0$；
全部1473解析列计算，1472自由列进入完整QR/SVD，无秩/奇异方向截断。

完整原work950×256、121600位置行保持；fine1728×512保持，
工作奇频1…127、fine奇频1…255均保，固定mean/core512、全部原内口/原源/六jets、
全部独立post2…48及从属core至96保持。a1全平尾及其cutoff/自由列不变。
费用预算仍5400秒、末1800秒预留、20个新接受步上限、100分钟job；
独立fixed-E串行组不与原height正常/细峰交换路线互相冒充。

同场末读出仍包括全部fine、完整D/V/L/2J、mean/Nyquist/closure、
同一真实响应的tail anchor及完整mean-height积分、两原步长actual-position读数。
旧变E闭合R615 observer不挪到本目标；不加一次旧诊断或入口探针。
新科学stdout保实际已接受态、pending试步、完整失败/部分计数与末16标量小收据，
不保存raw数组artifact/release，不写git。

## 6. 剩余量词与停止资格

true-tail source contract里的 `.99≤E≤1.01` 只量化整个真实cap→mouth尾部，
不是全body/core范围。七类原source误差仍explicit unresolved，严格消费者仍会拒绝。
分拆算法也没有证明同一连续 $E_*$ 容纳所固定的非圆τ1 core trace、
没有证明可增角频空间上的一致逆或最终非零精确根。
[同E误差传递纸证](2026-11-27-r618-same-fixed-E-angular-transport.md)只在同目标和同支假设下传播误差，
不赋予这些存在性结论。当前范围须先求出真正实际响应，按原真终态决定后继。

无论Actions退出码是否成功，本范围的实际科学状态、根/分支失败和未付误差均按原日志登记。
小幅固定E离散响应也不等于README要求的宏观族、统一连续metric、完整几何或完成标准。

## 7. 冻结绑定

以下绑定已经纯文本/AST/JSON/字节核合；没有导入或运行科学模块。

| 文件 | 字节 | SHA256 |
| --- | ---: | --- |
| `r618_split_reference_mean_chain_20261127.py` | 36093 | `40e8e1b07a286a573dcd52549909e1b208d9c16e8232b52afce7448ca8a75238` |
| `r618_split_reference_model_20261127.py` | 14869 | `753b3b5791f56b5b4365a3ed79297fff52b7f1061095e5980526b0c54cf21926` |
| `r618_split_reference_consumers_20261127.py` | 7648 | `337771c7a36e888e3eea362d1ac0ed34edca35527523be04082ad5083f072183` |
| `r618_actual397_split_reference_20261127.py` | 15431 | `332671f1ffe211fd3164f5a999a1f3833733ca82f451f2847378cfeb69c1052f` |
| `visible-r618-actual397-split-reference-20261127.yml` | 7521 | `c1dcefedc844aafd6c634c87c18a723311643d1d75ed86363e1b3906fb6ac552` |
| `request-r618-actual397-split-reference-20261127.json` | 380549 | `f9629f9a9f8c6ab5c350c723ea3367de685beaebc459d661f4c6b83d6824996f` |

实际stdin 316494 B，SHA256 `3599d21ed6e788227c45b1bf97f5b246d5cf9f3c52c3cad1b1ec6849513f269d`。
全部 51 份 source bindings 与 sparse-checkout路径核合；旧绑定全部逐字保留。
新policy由源码AST中的真实descriptor提取，未手抄遗漏新增项。
当前规则readSHA：公开 `f0d8e9ec936756e3d0267078d88f39e8c8b8483e`，私库 `249dc30670d8c084c764d7a4e60b2db6d69f748c`；主线程发布前可更新为实际最新读SHA，科学stdin不变。

批计数记录已完成的角运算和有独立attempt记账的调用，不冒中途失败的完整逐点总数；
科学总clock覆盖失败前的全部实际工作。已完成目标时间与精度重启时间字段不作为完整耗时的替代。

