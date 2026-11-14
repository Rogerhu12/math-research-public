# 独审：M14/W14 的条件闭图入口与实际尾导出

审查人：`/root/tail_review_continued_2`，2026-11-09。

结论：**PASS，限于条件协议及其实际接口。** root 稿完整、输入对象
选取正确，M14 模式/字节计数正确，通用背景转包与完整新图认证链
能够按所列条件连接；无须改写旧 M15 计划或为此新增强制 refinement
门。本稿没有运行条件链，没有新候选、几何或正向 certificate。
`G5=false`、最终独立复跑未完成、README 未完成。

## 1. 对象与审查范围

全文审查
`2026-11-09-db6f-root-final-m14-w14-entry-and-export.md`，SHA
`174991707495b531b44e3f53fdf00de1c098d0d907b9ded28d9fa2162f59f060`。
其 2 件 publication SHA 为
`8c27e37ff6d33c309352ef9c779fccc811c15ae18cb16d758a05263e655db7cb`，
24 来源清单 SHA 为
`c2ea97cafa8f44b9393b6468f289420ac75856e939c99e49c9fa45fe42d9649f`。
本次对这些实际文件逐件重算 hash 与字节数。

全文阅读 endpoint exporter、transfer-v3、paired closed-budget-v3、
common-cut-v2、whole-v2，以及旧 M15 最小流程、G5 充分性/轴说明、
最终独立流程、prefix 风险顺序。正常 terminal 的来源表、同 g
candidate 接口、精确末端比较和 CLI 也逐段核读。M14/W14 原入口及
新 LU 分支沿用本会话的完整源码独审；新分支审查报告为
`2026-11-09-db6f-tail-review-spectral-true-m14-release-lu.md`，SHA
`cd2f088a7c83ef61e3800fd1fb777b38f7cfc01313106623bff03a789e19b689`。

本审是 root 条件稿的全文独审及相关接口核查，沿用已审后端公式和
结构定理，并未重新执行这些后端或重证明全部前置定理。对于来源
清单中的实际数值数组，只读哈希、所需 metadata 和少量标量/维数，
不输出数组。新 55 文件来源清单随本报告封存。

## 2. 正入口与 exporter 真正需要的对象

协议先要求真实一次 M14 联解自然退出，并由匹配该实现身份的 final
auditor 连同 root 实际工具观察通过，再允许导出。这一顺序正确。
必须同时关闭 prefix CP、全部物理 PPoly 分片、实际 outer、它自己的
最后 Jac/audit、runtime Newton 和物理 callbacks。首 DN、旧真 seed、
程序捕获异常后留下的文件或内部 success 字段均不足以进入正入口。

原 v1 仍要求原 Newton。单行 LU 分支已经另有完整源码与身份独审，
但本审没有运行它；若以后选它，必须用新的 selector/preparer/auditor
和新运行自身的 root 完成观察。不能把它的函数指针嵌进旧 v1 后沿用
旧身份关闭门。资源 guard 也由实际运行单独绑定，未由此协议放宽。

exporter 的第一个位置参数确实是**这次成功 CP 的
`tail_seam.tail_record` 指向的最后真实尾响应**。源码解析顺序为
`rec.response ?? rec`，随后取 `checkpoint`/`tail_checkpoint`，并明确
要求其有 `parameters` 与 `states`。它不是 prefix CP reader。

为了避免仅凭名字判断，本次只读检查了已封存旧真 M14 的真实配对：

| 旧对象，仅用于格式核查 | 实际性质 |
|---|---|
| prefix SHA `3df8eefb18c4271283c7ae2b076afcda3fb42b169c8a7296ee4bce3e3b3ad3d0` | `parameters` 为长度 14 的列表，没有 staged `states` |
| 自有 final tail SHA `009bf5472ca412fae7d900d4ec18d26cd217221138666c2899dfceb3ead8f762` | `response.checkpoint.parameters` 为 M14/P8 字典，865×28 states，13×28 raw states |
| prefix 的 `tail_seam.tail_record` | 解析后正是上述 final tail；真实 request 的 jacobian/audit 均为 true |

这只是格式和配对事实，不能把旧 seed 升格为未来新候选。未来必须
重新核新 prefix→own final tail 链；单独成功尾包仍不足。

源保存表示的 metric 样本、CP residual 和最终 audit 只用于诊断。
它们不能互换，也不能替代完整连续图上界。root 稿没有把样本越门
直接提升为精确方程不存在，相关措辞适当。

## 3. M14 设置、完整模式和文件体积

exporter 从 `p.modes` 读取 M，以 `K=2*M` 解释 staged states，按
真实 `rawNode[D]` 检查 subdivided stage 数。它没有 M15 专属数组
维数。M14/P8 的下列初档与既有 P8 proposal 完全一致：depth8、
steps32、flow-steps32、N512、degree192、critical raw0、base64、
内部 ratio `.05`、endpoint ratio `.025`、difference-step `.00005`、
audit-angular128、audit fractions `.25,.5,.75`。

独立整数算术给出：

| 量 | 实际计算 |
|---|---:|
| signed planar modes，`−192≤m≤192, m≡1 (mod 3)` | 128 个，最小 −191、最大 190 |
| height modes，`0,3,…,42` | 15 个 |
| 总系数 C | 143 |
| stride `3+4C` | 575 |
| 1000 行原始 float64 | 4600000 B |
| common-cut 完整柱模下界 | 64 |

N512 满足源码的 `N≥2*degree+4`（这里右侧为 388）。common-cut
需要 64 的原因是平面转换 (j=(m-1)/3) 取到 −64；M14 只是求解
未知模数，不能据此删掉最终 Cartesian 表示的更高平面模。
`common-cut-v2` 从真实 tail modes 自动取足够的柱模并再检查不遗漏，
协议的连接方式正确。

1000 行 raw 大小小于 5MB 是整数体积事实，不是未来压缩文件的成功
证明。现 exporter 每片最多 1000 行、下一片从第 999 个间隔开始，
以共享行衔接；实际 gzip 写前另检查 `<5000000 B`，并记录 SHA/bytes。
root 稿继续要求实际每件检查与压缩，未拿体积估算替代运行证据。
其它 prefix、packet、mesh 文件也仍须各自支付同一大小限制。

旧 P8 proposal 是实际已存的 M15-quarter **背景网格规划**，不是未来
M14 导出。本次读盘精确重算为 576 stages、21031 unique nodes；唯一
endpoint stage 为 15，对应 rawCell0/rawSegment7/rawLeft0、rawRight
1/8，共 168 个节点。root 稿正确限定其用途。没有运行 `--plan-only`；
该入口本身会计算背景 profiles 和局部径向增量，不能被误称为纯
metadata 检查。

flow-steps 只限制 exporter 在每个表示跨上重积分的最大 source-x
步长；源码使用 `ceil((xb-xa)*flowSteps)`。增密表示节点会改变分段
重积分路径。固定 CP 的两档导出因此不是严格纯插值实验，且不能
把 native shooting steps32 改名为真 steps64 联解。root 稿已说明。

## 4. 同一物理背景与本张新图的证明债务

transfer-v3 的白名单包含 `modes` 以及审过的数值/簿记字段，所有
其它参数按键存在性和 JSON 类型敏感比较。paired consumer 明确
pin producer SHA `bdf6307f…`、原 base SHA 和 policy SHA，重新核
相同白名单，不允许在新报告里伪留旧 source identity。

六个背景绑定是 checkpoint、calibrations、alpha、cell_zero_A、
inner_A、outer_B。producer 重核全部文件，consumer 和 terminal
还核其冻结 hash 与解析来源连接；这六项定义同一背景，不能把其中
旧 background checkpoint hash 改成新 M14 求解 CP。新实际有限尾
由自己的 `finite_tail_manifest_sha256` 独立绑定。

真正 transfer 分支要求已完成的新 manifest、同物理端点、实际
exact-sum 网格，并用原背景值包作 Fraction 交分割/向外二进邻接。
`--check-parameters-only` 不产生新几何转包，也不能作为 final 输入。
所转移的只是 (w,w_r) 的值包；不转移旧图的 V、metric、曲率、
support，更没有声称这些 packet 多项式的导数是背景高阶导数。

因此 root 要求本次尾 manifest 的 first bounds、full metric/κ、
必要的 metric-only、实际 collar、全 rows/覆盖检查，方向正确。
新前缀也必须按自己的 CP 重新生成 shared-jet/mirror 表示、target、
基础 metric、exact bridge、公共 cut 和完整 geometry/metric/moment。
旧图的报告不能沿用数值身份。common-cut 还保留完整两 jet 的精确
定义、mean gauge 和开始端消失到二阶的修正，实际新 metric 仍由
完整新图后端支付。

先依据新图源诊断和实际未解盒安排必要精化，是计算顺序；它没有
降低最终完整覆盖要求，也没有把 pilot 当验收。旧风险稿中关于
source metric、实际图误差和区间包装宽度的区分，在 M14 同样适用。

## 5. whole、正常终门、G5 与独立最终复算

whole-v2 组合的是同图所有完整界，普通 metric 门仍为 (10^{-6})，
且源码明确 `fixed_g_convergence_gate_5_paid=False`、final mesh 未付、
README 未完成。root 稿正确继续要求 normal terminal，而没有把
whole exit0 改写为原求解容差已达到。

normal terminal 的入口是 `--whole`，不是 `--check-m12-negative`。
它按精确 Fraction 使用

\[
B=1/500000000=2\cdot10^{-9},
\]

核本张新图完整上界及旧真实 M12 点下界所给的严格实际下降。
源码还要求正确新图/同 g/源/所有完整报告身份，不能只传一个任意
小标量。此次只独立检查冻结常数的精确算术及接口，没有调用候选
分支、制造小上界或签发 future PASS。

terminal 正向通过仍只支付一项末端界和一项严格下降；统一 G5
还需要同 g 原 refinement 记录、轴含义、原求解容差和保留的失败/
非单调历史。M14 当前 Nθ512 不要求为了历史形式另造 Nθ256 联解；
常正对角 W14 不增加 Fourier 未知模数。可选同 M/N/g 的 native
32→64 对照按实际剩余误差需要判断，不自动成为新增完成门。
旧 M8 原生径向记录、旧 M8→M12 真下降和已审 G5 解释保持原作用域。

全时性继续依赖同一已审材料相位/空间旋转作用、完整 C3 与精确
公共两 jet；固定帽必须逐点不动。几个 t 的网格只是另外的数值
交付，不替代全时证明。未来网格必须来自实际选定的新闭图，重新
核闭有向流形、PL 嵌入、共同 mask/固定顶点位模式与单件尺寸。

独立最终流程必须由未参与候选优化者，使用生产者实际成功命令的
真实前置 seed 和同一冻结算法重新求解，随后重新导出/转包/认证/
组合/建网格。不能切到最终 CP 做零步读取，也不能只重抄各报告。
若选 LU 分支，其新身份也须实际重放。root 稿是现有独立流程对
M14 的适用说明，没有取消任何步骤或把作者重跑冒充独立计算。

## 6. 实际检查、格式风险及结论限度

独立标准库脚本
`db6f-tail-review-final-m14-w14-entry-and-export.py`
实际 tool receipt **`92702d`，exit 0**。输出报告 SHA：
`210363c3536079b9a2025709378f6aa7e4b76dc72a4a2312d3259d298d9a4be8`；
55 文件来源清单 SHA：
`344cfb7c5bc49abe0895e6d4631e06457e315174a5983745896ba6a2723e836c`。
原 24 来源、root 2 件、terminal 所 pin 的实际源码、旧格式示例、
既有 P8 proposal 均重核。所有 solver/root/RK/flow/background
factory/exporter/transfer/geometry/continuous backend 调用均为 0。

另有作者正在检查 shared-Hermite 容器的单件大小风险。该工作尚未
成为本协议的既有格式输入，本审没有把未完成的无损分片适配算作
已通过来源。若未来原容器实际超过大小门，需另封存并审查真正的
无损格式、对应 reader/consumer 和来源身份；不能降低表示模数后
把结果称为同一精确有限图，也不能悄改旧 terminal 来源常量。此项
是实际文件条件，不是数学完成标准的新门。

因此 root 稿作为**真实候选关闭后的条件执行协议**通过。它没有
声称当前已进入正入口，没有降低 normal (2\cdot10^{-9}) 终门，
也没有把有限数值下降提升为严格无限非线性尾存在定理。最后仍须
如实报告数值近似与精确无限存在之间的缺口，并遵守 README 的
更强目标继续研究要求。
