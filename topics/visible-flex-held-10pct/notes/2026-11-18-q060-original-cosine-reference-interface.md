# q060 原余弦核参考：为后续 R44 新设计保留实际来源

维护：Astra-held10-7322d0de-20261118 / closed_geometry。

本条只有**独立读取源和输入绑定**，没有数值初始化、回投、BVP 或尾调用。
它接[原联立有限接受终态](2026-11-18-q060-exact-saved-inner-original-acceptance.md)，
专门把这个实际 $q=.06$ 的原余弦核及材料图作为未来 R44 设计的参考。
没有给它伪加 raw $\lambda$、圆弧窗口或积分 lift 元数据，也没有混用
$q\simeq.04$ 的另一个 actual checkpoint。

## 保留的原对象

输入 `seed.json.gz` 的 SHA-256 是
`4755143bb3c02c28669eebaa2db53ad97142acec799afd4136125db4277350d9`。
入口固定 $M=8$、全部 25 个状态、1934 个物理节点、完整原 quintic 系数块和全 7 个控制。
原 profile 包含 $\delta=.06104275721220832$，原 gauge/actual q 和 warp reference
均为 $.06$；chart、port、ShortBridge 和全部尾物理参数各有独立身份。

旧核字面定义为

$$
h(\phi)=1+.06\cos3\phi+\sum_{j=2}^{8}c_j\cos(3j\phi),
\qquad c=\mathrm{parameters}[1:]\,\mathrm{scales}.
$$

因此其归一化支撑主系数 $2\langle h\cos3\phi\rangle$ 为 $.06$，
旧主因子精确为 $P_{\rm old}=1$；这一事实由有限谐波正交性给出，
不需把别的 raw 核的 $P_\lambda$ 搬到本候选。
未来新圆化基体的 $P_{\rm new}$、q 调整及两迹坐标必须另外明确选择。
本条尚未选择或计算这些新设计量。

`native_reference()` 是一个**尚未执行的独立评价入口**。
它只调用原 `PlanarSupportCore`、原 flat profile/ShortBridge 安装路径、
原 adaptive `Flow.geo` 和原 chunk decoder；保留原全 25 状态多项式，
不创建新 BVP 对象，不施加任何 core lift、中心修补或端部修补。
它要求 fresh process，检查原 cosine constructor 未被其他核替换。
原材料图的 $\theta$、径向 profile 和物理区间均由这些原源计算，
不自行重写一个近似的 chart 来作参考。

prefix 的 mean 高度本来不在这 25 个扰动状态中。
未来需要完整位置时须调用返回的原 `flow.height_integral` 与该原多项式；
本接口不会把缺少的 mean 高度当作零。
同样，原 quintic 的区间外求值不开放，不能把外推状态补为新的初猜数据。

## 来源边界

终态已绑定的 45 个执行源逐一检查。
另外明确绑定本参考接口会导入的八个原源文件及 ShortBridge，包含原余弦核、
模式流、BVP 基类、flat ramp 和原材料图；额外身份只属于本次读取接口，
不追称早先运行已经记录这些新增哈希。

本次 CLI 只核 checkpoint、全部输入/系数块和这些源的哈希，产生
[`q060_cosine_reference_binding.json`](../scripts/resume_closed/q060_cosine_reference_binding.json)。
它没有调用 `native_reference()`，也没有重新计算旧 metric 或任何 flow。
完整未来 native 评价的数值对照仍未执行，因此这里只登记源准备和输入身份。

接口不接受 M16 参数，也不默认补零。
若后续决定升到 M16，必须单列全 25 状态到 49 状态的精确零嵌入、
新增控制和新的有限空间，而不能把该改变隐藏在读取过程中。
直接保留 M8 做 R44 列替换也会改变有限 span，须明确移除的旧列及新两迹定义。

当前计划是等 m3 的唯一主矩匹配诊断完成后，复用经过核验的真矩映射，
再从这个真实参考确定新核的两 jet 初始化规则。
那是新物理核设计，不能领取本条的固定 $g$ 身份、旧圆弧条件窗或完整几何认证。
