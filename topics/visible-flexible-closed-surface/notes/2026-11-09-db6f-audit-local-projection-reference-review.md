# 四个冻结投影点：提取与高精度参照独立审查

审查者：`/root/independent_geometry`，2026-11-09。**PASS：两份提取程序的静态逻辑、已保存输入绑定、Decimal 参照定义及独立零 root 重放均通过。** 本审查没有参与原点选取或投影优化。binary64 比较器由 `/root/coupled_prefix` 另行独审；本文不代替该部分，也不把四点诊断扩张成全域误差证。

## 1. 冻结对象与实际执行

全文审读以下源码，并核对原 `general_root_tail_momentum.mjs` 的 `data/evaluateL/root/rhs` 定义：

| 文件 | SHA256 |
|---|---|
| `scripts/db6f-tail-local-projection-points.mjs` | `837a2361bdf17731903fdf31afaadd1c46023db63bcff665feeec0f2f621a377` |
| `scripts/db6f-prefix-one-m14-root-packet.mjs` | `7b28538a9c92b391cddba341b7ca3469fdc3c006eb491788fd31e8259cd68ca2` |
| `scripts/db6f-tail-local-projection-reference.py` | `5ab87f037a40579bae5164ef0b50b9e701d58703411177569a91ec94b810249a` |
| `notes/2026-11-09-db6f-tail-local-projection-comparison.md` | `ef93eb972b9c0fa71279756da7c56344292dec0503e4e87072b222834278a055` |

参照程序独立运行到 `audit-local-projection-reference-observed.json.gz` 和对应 `-summary.json`，真实退出码 0，用时约 1.75 秒、峰值 RSS 32.7 MB。命令、cwd 所需相对路径、退出码及耗时保存在 `audit-local-projection-reference-observed-execution.json`。本次调用 **0 个 moment root、0 个 flow**。更早一份同值本地重放没有完整保留可直接读取的进程退出状态，因此这次使用新输出名明确记录成功状态；不覆盖旧输出，不需要重复提取原 root。

独立只读检查器 `scripts/db6f-audit-local-projection-reference.py`（SHA `2bf9dcd3041c08210b156ba45d4f8668b6dbf85eb2cb38b145760e923e4094e4`）也实际退出码 0。报告 `audit-local-projection-reference-check.json` 的 SHA 为 `9a7b112a7bf4e10fe23dbf3d69b400cb8e7c2554616624ec682144c8c7859dc3`。

检查器核实 54 个不同输入／源码路径的 hash，完整比较作者与重放 reference、summary 的全部数学字段。只排除已单独核实的相对输入路径拼写、运行秒数、重放输出路径及其文件 hash；所有参照系数、矩阵、逐项差和统计完全相同。两个原始输入包及三份作者报告的冻结 hash 均写入检查报告。

## 2. 三个 M15 点与一个 M14 点的身份

M15 程序由冻结 stage-input 的 hash 唯一定位旧失败案，并验证实际索引确为 `cases[4]`。stage35、raw0/segment4、trial step $1/16$、first `sourceX=0/substage=0/ordinaryStep=0` 均吻合。状态是原输入追加两个零 mean，Q、target 和七个实际几何标量逐值相同。

两个失败点分别复制 `failure.target` 和 `failure.rootTrace.lastL`，只调用 `evaluateL`，明确没有声称它们是 root。第三点复制已闭 control checkpoint 的 `states[36]`，程序中只有一次原 `engine.root` 调用；其 minA、minD、minS、residual、scale 与旧已审正 floor 控制报告逐值相同。本审查直接重核状态和这五个保存标量，没有再调用 root。

M14 程序只接受原已收敛 M14/N512 checkpoint，并要求其原 DN residual 低于原 tolerance。数值参数、物理工厂、分段和预定 stage37/raw0/segment4/raw x=.25 有检查。它复制 `states[38]`，只追加两个零 mean，不作端口重新缩放；有且仅有一次原局部 root 调用。已保存 root 为 5 次 Newton、无 roundoff fallback。全部 49 个保守源码／输入绑定均重新核实，状态与 CP 精确相等。

两份提取程序没有调用 RHS、RK、flow、DN 或变分 flow；它们的工厂构造及已有物理校准不应误称为额外 moment root。提取合计两个原局部 root 是作者已经完成的操作，不是本次审查重新执行。第四点是预定控制点，不是搜索得到的全尾最坏点。

## 3. 两个高精度参照的数学定义

`Decimal.from_float` 把冻结 binary64 的 E、w2、p、pt、L、U 解释为精确实数输入；此层没有重派生 E、w2 或物理系数。两个参照只改变角基底：

- `rounded-table` 使用实际保存 binary cs/sn 的精确 Decimal 值；该表的正交缺陷保留。
- `ideal-grid` 用 Machin 公式的高精度 $\pi$、真正 $\sqrt2$ 的高精度近似及四分之一周期 Taylor 表。整数模 N 索引和四象限旋转正确处理负号与周期，M/N/spacing 的缓存键不会混用两个基底。

若 $K=L_v-P_\theta$，原 q 的多项式部分恒等于

$$
\frac{K^2+EP^2}{2}+KP_\theta
=\frac{L_v^2+EP^2-P_\theta^2}{2}.
$$

该恒等式不需要重新施加 E 与 w2 的关系。参照保留同一 $T,u,S,D,A$ 和原 fc/gc。由 $D=1-u$，原 B 中 `expm1(-1.5*log1p(-u))` 的实数值为 $1/(D\sqrt D)-1$；程序使用此式。**B 的单位阵项仍是原数值定义的 I，未错误替换成 rounded-table 的 Gram 矩阵。** 冻结 E/w2 的参照只比较原 B 定义，不另声称它是一套改变后物理模型的精确 Jacobian。

又由 $1-\sqrt D=u/(1+\sqrt D)$，gc 等于 $1/(S\sqrt D)-1$，所以保存的 nonlinear flux 参照为

$$
UK+U(1+K)\,gc
=\frac{U(1+K)}{S\sqrt D}-U.
$$

物理 pref×frequency 也按冻结 binary 乘子计算。它只是完整 momentum RHS 的非线性部分，不包含其线性项或任何积分误差。逐分量 q、moment、B、flux、三个孤立多项式及两种表模型的差值统计均与源码定义一致；B 的对称填充和最大绝对行和正确。

80/120 位计算分别使用相应精度，基底另有保护位。全部四点、两种模型中的 A/D/S 均在原 `.05` guard 之上。Taylor 截止和 Decimal 舍入没有构成有向区间证明；两档最大差只是数值稳定性证据。报告明确保留这个限制。

## 4. 数值结论与解释范围

独立检查器重算 binary moment 差与原 scale 的比值，四点最大值为约

$$
4.768284752036642\cdot10^{-16}<4.77\cdot10^{-16}.
$$

两档参照的全部受检量最大差约为 $1.18473\cdot10^{-78}<1.19\cdot10^{-78}$。这不是严格的真值误差界。

原 L 固定时，failed-last 的新残差仍大于 $.022$；两个成功控制的新 moment 残差仍小于原 $8\cdot10^{-14}$ 相对停止门。所有四点的 analytic 投影在 quad、B、nonlinear flux 的全分量最大差上更接近理想表参照，然而第一个点最高单个 quad 模略变差。原说明没有混淆“最大值改善”与“每个模改善”，也没有把原尺度换成余项尺度。

这些检查支持作者的有限结论：四点投影舍入差不能消掉已经保存的失败残差。它们不证明改变 Newton 后的收敛性，不量化全 shooting 的放大，不解释 continuation 停滞原因，不改任何 guard 或 engine，也不支付 G5。

本审查的数学推导、输入重核和 Decimal 重放与 `/root/coupled_prefix` 对 binary64 比较器的另份审查互补。完整链引用两份审查时仍须保持各自范围。
