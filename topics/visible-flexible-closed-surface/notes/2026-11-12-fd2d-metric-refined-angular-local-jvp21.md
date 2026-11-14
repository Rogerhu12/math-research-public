# 21 暖态：K31／固定 tail16／129 节点的局部实际 JVP

## 1. 输入与唯一目的

本次消费已封存的
`notes/2026-11-12-fd2d-refined-angular21-central-restore-field.npz`，
SHA256 `eac2a27ebecd31424bc5880a3870749cb10b8a130b2a61430d94fa83cf604d73`。
该实体是明确中央恢复后的 21 初始暖态。21 主求解后来实际被终止，
退出 `137`、没有新接受步；本次不把这个输入称为收敛场。

任务仅排查 R158 与 R163 组合后的实际维度及列位置：raw 和 central
角阶 `31`，独立 tail 控制数 `16`，物理 profile 参数 `7`，保存节点
`129`。参数为 `central[0:31]`、`tail[31:47]`、`profile[47:54]`，
每个径向节点的 raw `(n,m,l)` 系数长度为 `32+31+32=95`。
计算角网格由实际 provider 给出，为 `512` 点，没有手动改变角网格。

此前 K15 的 JVP、R158 的零填充同函数核及 R163 的重表达核并不自动覆盖
这次 54 参数和新 mesh 的组合。已先与数值主线确认没有重复的同范围实核。
本次没有 BVP、body、全域 Jacobian、Schur 方向求解或完整场认证。

## 2. 原场与原有限公式均保持

用冻结 `fd2d_gc_midpoint_refined_positive_trace_v3.py`
的 `create_midpoint_refined_problem(..., saved_field=..., split_cells=())`
复原明确保存的 partition。空 split 不再插值、不再重新选 gauge；实际
`mesh`、raw coefficients 和参数逐字节核对。所有 candidate、严格
base-radius packet、reference inlet/cache、seed、atlas、R153/R155
窗口及参数布局按真实 21 report 与 NPZ 绑定，未改活动源。

完整实际场是原 lifting 加 P1 correction，经 R153 coast Gauss-l、再经
不相交的 R155 terminal positive-trace 窗。局部 node 与 G2 内点的
Gauss 消费的是这个完整实际场：

\[
G=n\,l-m^2-K.
\]

它对任一原节点或参数方向的导数为

\[
DG=l\,Dn+n\,Dl-2m\,Dm-DK,
\]

其中 `Dn,Dm,Dl` 包含两个非线性窗和全部真实 lifting／profile 链式列。
G2 内点先按原 P1 插值作 `(1-t)y_i+t y_{i+1}`，再执行完整非线性
定义；故其节点列分别乘 `(1-t)` 与 `t`。

Codazzi 调用冻结 `fd2d_gc_gauss_cell_positive_trace.py`。每个完整
cell 包含 R152 已知 affine lifting 的实际 split 求积、R153 非线性
Gauss2 修正、R155 准确 n 端点增量及真实角漂移项。保留模和完整 D2
高模补余同时比较；未将旧 affine-only 公式冒用在整个非线性场上。
所用 residual 和 Jacobian 的数学定义与 21 原 driver 相同。

## 3. 有限局部范围

只选以下四个 cell；每个 helper view 最多持有相邻两个原节点：

| 作用 | cell | 左端 | 右端 |
|---|---:|---:|---:|
| 准确中央柱到第一个自由节点 | 8 | `0.32` | `0.32625` |
| 原 63 的细分下半，coast 入口 rim | 63 | `0.5919999999999992` | `0.6116816746501718` |
| 原 118 的细分下半，terminal ramp | 121 | `1.4694731783581287` | `1.4727231783581287` |
| terminal 全平台及耦合 trace gauge | 124 | `1.4792231783581289` | `1.4824731783581289` |

另在节点 `8,64,122,124` 记录完整实际 node Gauss。每个 cell 再有
原两个 G2 内点的完整角 Gauss 和原完整积分 Codazzi。
这是小行集合；没有保存或构造全域 tall Jacobian。局部 Gauss 直接保留
完整 512 角点读数，用来检验实际完整字段，而非仅保留低角模。

## 4. 五个实际非零方向与原消元

使用冻结 R159 的 `EliminatedFieldMap`，先选真正 free raw 列及全局参数，
再展开到实际场数组：

1. **新增高 raw 模方向**：含 n/l 的 `cos(62ξ)`、n 的 `cos(60ξ)`、
   m 的 `sin(62ξ)`，作用于细分 coast、terminal ramp 以及平台 gauge
   节点。平台方向按 `δl=-δn` 展开，保留 `d=n-l` 的真实变化。
2. **最后一个中央列**：`δcentral[30]=1`。准确中央柱所有 fixed 节点的
   `δn=core_coefficients·δcentral` 一并展开；cell 8 检验进入第一个自由
   节点后的非零 Codazzi 列，避免只在恒零中央 Gauss 上做无效核。
3. **独立 tail 列**：扰动实际全局列 `31,35,38,42,46`，系数分别为
   `.4,-.3,.2,-.1,.5`。这些基点 tail controls 均严格位于原盒内，
   两个方向的微小差分保持同一非负尾族。
4. **全部物理 profile 列**：全局 `47:54`，方向
   `(.35,-.27,.18,.24,-.29,.2,-.16)`，完整支付实际 `K`、算子、
   lifting 和非线性窗口的参数链式。
5. **混合方向**：上述四方向的 `.3,.2,.4,.1` 线性组合。

每个方向显式记录 cut 为零、已删除 coast-l 帽方向为零、terminal
`δn+δl=0`、全部固定中央节点的真实参数映射误差。同时把局部原列
`J·expand(v_f,v_p)` 与 R159 变换后的局部 `A v_f+B v_p` 比较。
这核查的是新布局下原消元的列位置；没有改变消元或有限目标。

## 5. 差分与记录约定

只做一次实际 fixture，对每个方向使用中心差分步长 `1e-6` 与 `5e-7`。
每条记录同时给出非零解析作用的 L2 范数、差分范数、最大绝对误差以及
以 `max(1, ||Jd||)` 归一的误差。不把接近零的代数 Gauss 行用其微小
分母放大，也不隐藏这些行的绝对误差。

两个步长不是连续证明，较小步长也可能加大舍入消减。实际数值结果会在
报告中逐方向、逐 block 保留；不把它们提升成整个候选场通过或全域残差界。
结束时只复查同一局部 residual 与输入字节及源码身份未改变，不重复组装
全域 `F/J`。完整向量方向与全部局部解析/差分见证写入小 NPZ。

复现命令：

```bash
python scripts/fd2d-metric-refined-angular-local-jvp-check.py \
  --field notes/2026-11-12-fd2d-refined-angular21-central-restore-field.npz \
  --run-report notes/2026-11-12-fd2d-raw-bump-refined21-b0001-report.json \
  --out-prefix notes/NEW_UNIQUE_STEM
```

## 6. 唯一实际运行结果

运行于 UTC `2026-11-12T16:28:18.725286` 启动，
`2026-11-12T16:30:27.997216` 正常完成。执行器 session `64182`，
初始 chunk `28a839`，最终 chunk `970ec4`；wrapper 和被调脚本均真实
退出 `0`。内部耗时 `122.22958408100021 s`，wrapper 耗时
`129.2719601739991 s`，峰 RSS `148112 KiB`。

实际查询为 4 个 node-G block、4 个完整 endpoint-C block、4 个内部
G block。每个 node-G 有 `512` 行，每个 endpoint-C 有 `256` 行
（保留加 D2 高模），每个内部 G 有 `1024` 行（两个 G2 点各 512 角）。
各块最大原列数仅 `2×95+54=244`；未将这些局部行拼成全域 Jacobian。

| 方向 | 各块中最大解析作用 L2 | 步长 `1e-6` 的最大相对 L2 差 | 步长 `5e-7` 的最大相对 L2 差 |
|---|---:|---:|---:|
| 新增高 raw 模及 terminal gauge | `101.95109199204504` | `4.139484010721151e-8` | `8.742863593940293e-8` |
| 最后一个 central 参数 30 | `159.99999910563963` | `1.6971944364545728e-10` | `3.23749663704455e-10` |
| 独立 tail 切片中声明的五列 | `5.789095083303647` | `8.703897570674916e-8` | `1.8285019437204542e-7` |
| 全部七个物理 profile 参数 | `1310.008991179183` | `1.3776287704477814e-9` | `5.2780704790834605e-9` |
| 四类方向的混合 | `131.10269037485324` | `4.309125751191388e-8` | `8.33378108898445e-8` |

最大相对 L2 差来自 tail 方向、步长 `5e-7`、cell `124` 的完整
endpoint-C：解析作用 L2 为 `0.9852173011605166`，差分作用 L2 为
`0.9852173044504968`，最大逐行绝对误差
`4.890915949323782e-8`。它是实际非零作用，不能归为只核恒零行。
较小步长的误差更大，完整两步长记录保留，不据此声称精确导数的
数学误差小于某个连续认证界。

高 raw 和混合方向的最坏归一读数来自 terminal 平台 cell `124` 的
内部 Gauss：这里解析导数只有约 `4.3e-15` 和 `1.3e-15`，完整场
Gauss 本身约 `5.6e-15`；中心差分除以小步长放大浮点消减。
对应逐行绝对误差仍完整保留。该同一方向在其他选中块的实际作用明显
非零，表中没有把近零 Gauss 作用冒作整体 JVP 的非零证据。

R159 原列作用与消元后局部作用的最大相对差为
`2.9831114548155546e-16`。五个方向的全部中央映射、cut、删除的 coast-l
列以及 trace-pair 和均精确读为 `0`。结束后的全部原局部 residual
复算变化为 `0`；输入向量字节和冻结的 18 个 source SHA 都未改变。

实际原局部 residual 并不小：例如细分 coast cell `63` 的完整
endpoint-C 峰 `22.99500024290804`，内部 G 峰 `4.181218070115243`；
terminal ramp cell `121` 对应 `12.379855649816426` 和
`0.5606522185088081`。本次只给新组合的代码链式和索引提供实证，
没有将暖态的局部或全域残差认定为通过。

## 7. 冻结交付

实际检查源码 `scripts/fd2d-metric-refined-angular-local-jvp-check.py` 为
`18740` bytes，SHA256
`a5dd12451b105a94e1656807e91506a86d1535738ef0bd2de5e89a22ee4ff2b4`。
来源表、120 条逐方向／步长／block JVP 记录和选中块身份保存在
`notes/2026-11-12-fd2d-metric-refined-angular-jvp21-01-report.json`。

全部实际方向和解析／差分作用见证为同 stem 的 `-witnesses.npz`，
`263748` bytes，SHA256
`61c97625fb729a5e0d5b55f8914f5e6ca0ff84716cf71a6a02fd39f5551b954b`。
同 stem 的 `-exit-receipt.json` 及 `notes/process-observations/` 下
console 保留真实运行结束身份。上述实体、本说明及原始输入身份统一列于
`notes/2026-11-12-fd2d-metric-refined-angular-jvp21-closed-manifest-01.json`。

没有修改 21／22 driver、v3 factory、原 consumer 或 native reader。
这次局部结果不要求主线等待独立审核，也不新增完成门或重复运行要求。
