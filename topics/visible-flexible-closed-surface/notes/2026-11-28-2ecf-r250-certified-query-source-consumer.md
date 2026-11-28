# R250 配套：准确 Q 查询与显式独立的 X+C+Q 源消费者

本记录补完 R250 的实际查询接口，不新增一个数学结果编号，也不记作一次 Newton 接受。原 R250 已在 `8da57114f89202875e0460bb438289932a1bdf12` 发布；全域平滑改动、固定 g、端口两 jets 与几何转移均沿用该证明。本次将**同一个准确定义的 Q**在一份真实 h487 查询集合上向外求值，再以准确计价的 longdouble 加法形成一份有独立身份的源缓存。活动中的原 X+C 求解不被替换。

## 1. 源身份与范围

原源来自完整 M12 manifest：

`2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json`

SHA256 `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`。

准确 Q 完全取 R250 的完整有限 tail 定义：24 个原始块、18,552 个 span、18,551 个内节点、141 个完整 Fourier 系数；每个节点的平滑半宽为相邻准确物理 span 长度最小值的 1/64。其完整准确 jump/window stream SHA256 为

`a64d212afa7bdd19599ff8da5d0ecdd82b5ed940b8cbb6f7a9e1d878b965b5d7`。

本次准确查询的输入是当前实际重生的 h487 查询源，不借用 R245 场的字节身份：

| 输入 | SHA256 |
|---|---|
| 原查询 report | `7d75c93355fb5b79077c8b606294487c02f591e70e40111cac97abcf924da6d2` |
| 原查询 cache | `a98098ed40ffed92cae3f3ca208c91456d8a7f4958b08c4a21973c79dd881c1b` |
| R250 全域 smoothing report | `7c52dc85926d8e9ea8583ca33380ea7b7cf8f6cd2672e4eb2847e3548d65c426` |

新数学源明确为

\[
X_{\mathrm{reg}}=X+C+Q,
\]

其中 X 是原闭曲面的源，C 是旧的确定性 central correction，Q 是 R250 定义的平滑修正。原目标度量 g、材料参数、D3 相位、central curve、true cuff 和 cap 的定义均不改变。Q 在每个原有限 tail 节点上取零的 0/1/2 jets，在有限 tail 的两端附近恒为零；故原共同切口、真实平袖口与粘合两 jets 保持不变。它只把有限 tail 的原分段多项式缝处做光滑化；整个 X+C+Q 仍仅按已证的全局 C2 性使用，不声称整个闭曲面 C∞。

新源 report 使用独立 schema `m12-R250-regularized-tail-query-source-v1`，含完整 `source_regularization` 身份链，并明确 `same_original_tail_source=false`。旧源 report/cache 只保留为下层输入身份。原源上单独成立的全域证书字段不被复制为新源证书。实际求解使用新源时，结果必须保留该 `source_regularization` 字段；只列出旧 manifest 不足以识别新源。

## 2. 准确 flat-switch 查询

新增脚本 `2ecf-m12-smooth-source-query-cache.py`（SHA256 `c05000bd75fa1fdb98498162a289a7df52844e16ae04e1179006147bacfca191`）从实际原查询 report/cache 取出全部准确半径，并从经 SHA256、Git blob SHA1、长度三重核对的原始历史块恢复准确源节点和高阶 jump。

所有节点、物理 span 长度、窗口和查询半径都用 Python `Fraction`；不从打印后的半径相减。Q 的 141 个通道与 0/1/2 径向导数都计算，未丢弃高 Fourier 模式。

对窗口内 \(t=(r-r_i+\delta_i)/(2\delta_i)\)，记

\[
T=\frac1{1-t}-\frac1t,\qquad e=\exp(-|T|),\qquad z=\frac e{1+e}.
\]

左侧 \(S-H=z\)，右侧 \(S-H=-z\)，避免在右侧由两个近 1 的数相减。由 \(z(1-z)\)、准确的 \(T',T''\) 直接生成 switch 的一、二阶导数，最后除以准确的 \(2\delta_i\) 及 \(4\delta_i^2\)。若查询恰为原节点，Q 的三组系数严格取零。

指数采用 256 bit 二进有理区间：

1. 若 \(a=|T|\ge256\)，由 \(e>2\) 得 \(0<e^{-a}<2^{-256}\)。
2. 否则将 \(a\) 准确除以 \(2^k\)，使 \(y=a/2^k\le1/16\)。\(e^{-y}\) 的交错 Taylor 级数项递减，第 40 项部分和给上界，第 41 项部分和给下界。
3. 把上下界向外舍入为分母 \(2^{256}\) 的整数，再作 k 次带向外舍入的区间平方。
4. 后续有理运算及乘法全部向外。每个最终 longdouble 存储值由 `as_integer_ratio()` 重新视为准确有理数，与对应准确区间比较；存储误差也计入。

本次自然结束，退出码 0，用时 12.573160813 秒。实际消费的 4,631 个原查询加 546 个原诊断查询，共 5,177 个不同准确半径；204 个准确平滑窗口与它们相交，其中 138 个查询恰为原节点、88 个查询在窗口内部且非节点，其余精确 Q 为零。全部 5,177 个查询均被覆盖。

准确 Q 查询 report/cache 的 SHA256 分别为：

- report：`77b08874685e8c813ed20640b8ad69c571c840efc583afb85e1c14d97163efec`；
- cache：`af21b56d0f0773e4722029c2829cb8525ab96a2396e87823d5b39c1452a82b51`；
- 实际 interval-query stream：`259a552f041fcc0465c25478fe446a539d76aee7f416ed526f0e0e92c3cdeb11`。

## 3. 六 jet 界：全域大小与查询误差分开使用

以下六 jet 均在真实物理材料坐标 (s,u) 下。原 |r_s|≤1、|r_ss|≤6 已被包含，尤其 Qss 使用 Qrr+6Qr 上界。表中的查询误差是所有查询点和全部 Fourier 通道之和的上界，不是单个通道误差。

| jet | R250 全域准确 Q 大小上界（近似显示） | 本次 Q 存储/求值误差上界（近似显示） | 合并进原 stored source 后新增总误差上界（近似显示） |
|---|---:|---:|---:|
| Q | 2.78861607804955e−19 | 3.04778529561171e−42 | 2.28728705381115e−24 |
| Qs | 1.59124806886163e−12 | 8.93364195418677e−36 | 2.18994768754143e−22 |
| Qu | 4.76669695319946e−18 | 2.89360189631967e−41 | 1.00439318591606e−23 |
| Qss | 6.47425512352746e−4 | 3.44982290912516e−27 | 2.31292485322385e−20 |
| Qsu | 1.73220595955717e−11 | 6.96636689484074e−35 | 7.30895481474496e−22 |
| Quu | 1.12518467501432e−16 | 7.86702457056943e−40 | 7.93601186635981e−23 |

机器可用的证书取 report 内 `exact` 有理数字段；表格为近似显示，不替代准确有理数字段。查询目标微分误差 \(\epsilon_{Qs}+\epsilon_{Qu}/r_{\min}\) 小于 8.93383165356558e−36。

第一列在 R250 的**整个有限 tail**上成立，不是由本次有限点查询外推。第二、三列只证本次准确查询集合上的 Q 新增误差，不重新认证原源求值器误差或运行时 sin/cos 误差。这些原有误差仍须在实际消费者中独立支付。

## 4. 独立源合成与准确加法误差

新增脚本 `2ecf-m12-smooth-source-merge-cache.py`（SHA256 `1aee1e34c37c150d0155d07aa268783cc74cf949ccf3558301366bd1ec7bf199`）核对实际原源、Q cache、Q report 和全域 smoothing report 的身份，生成新缓存。所有无 Q 的系数连 signed zero 都逐字节保留。对每个有 Q 的系数，先作实际 longdouble 加法，再用三个存储值的准确有理表示计算

\[
\left|\operatorname{stored}(a+q)-a-q\right|.
\]

径向阶数 d、角阶数 j 的每个误差，按完整模式权 \(|m|^j\) 求和、再对全部实际查询取最大；加上第二节中 Q 的准确求值误差，即得表的第三列。第三列的参照对象是**原存储源系数 + 准确 Q**，未声称包含原存储源自己的既有误差。

合成自然结束，退出码 0，用时 2.224947854 秒。原 4,631 个查询中仅 88 行发生变化，共 37,075 个非零 Q 系数被加入。546 个原诊断行全部未改变。端点准确分子/分母、第一/第二径向导数、完整模式列表、查询半径与其余元数据全部逐字节不变，逐数组记录 SHA256。

新 report/cache 的 SHA256：

- report：`d3c7266402f3bb158ba5d3ee2075992ceaf391161dc4659d667db806f9ce95df`；
- cache：`7aa7e0190f2d6eae445876a2d7c82fbc52a57d1953af713bd9b0a3ddc829ba43`。

## 5. 生产读取器实际消费检查

已实际使用当前生产 `6a65-m12-entire-half-cartesian-bvp.py` 的 `TailQueries` 和 `6a65-m12-global-common-cut-position-recovered.py` 的 `CommonCutSource` 分别读取原/新 report/cache。两者均成功；原/新的 `common_cut_target` 和 `cut_delta` 数组完全相等，而生产 `source_identity` 中实际 report/cache 哈希不同。

在一个非零 Q 的真实查询半径

\[
r=6675473964795353989/18446744073709551616
\]

读取新旧系数，三个径向阶次的最大实际差分别约为

\[
(8.271806125530277\times10^{-25},\quad
1.205133860458389\times10^{-16},\quad
3.499386814352571\times10^{-9}).
\]

该检查自然返回 0，输出记录 SHA256 为 `10ac071cef04fae8cebf95beb5ed65c50e4042fdb5d919063c3684e688dfed58`。它证明已有读取接口可真实消费新源且端口输入未变化，不证明某个尚未运行的非线性步接受，也不证明新源上的实际闭曲面误差已降低。

## 6. 后续消费者必须支付的连续量

如果实际求解选择独立源 X+C+Q，完整候选应写作

\[
Y=X+C+Q+W,
\]

而不能仍称 X+C+W。连续几何转移继续以原 X 为基准，保留原 \(C_X\)，把 Q 的全域 0/1/2 jet 预算加入实际 C+W 的对应预算，再调用相同 R10/R16 转移。R249 的局部全 Fourier 预算可以用于 W，但不会自动包含 Q。对数值目标评估还须加入本记录的 Q 求值/加法预算及原有源求值、角函数预算。

R250 对**明确定义的旧 R245 场 + Q**已给出 reach、held、metric 等完整几何不等式；本记录没有把该几何证书迁移给当前新重生场，没有执行新 Newton 解算，没有声称 g 被 Q 等距实现，也没有满足 README #5 的真实加密收敛要求。

## 7. 复现接口与存储

先按 R250 脚本重生全域准确 smoothing report，然后针对任意实际原查询 recipe 运行：

```sh
python scripts/2ecf-m12-smooth-source-query-cache.py \
  --scripts scripts \
  --smoother scripts/2ecf-m12-smooth-source-seams.py \
  --smoothing-report /tmp/smooth-full-div64.json \
  --source-report /tmp/h487/entire-half-exact-tail-queries.json \
  --source-cache /tmp/h487/entire-half-exact-tail-queries.json.npz \
  --cache-dir /tmp/m12-raw-cache \
  --out /tmp/h487-smooth-source-queries.json

python scripts/2ecf-m12-smooth-source-merge-cache.py \
  --source-report /tmp/h487/entire-half-exact-tail-queries.json \
  --source-cache /tmp/h487/entire-half-exact-tail-queries.json.npz \
  --Q-report /tmp/h487-smooth-source-queries.json \
  --Q-cache /tmp/h487-smooth-source-queries.json.npz \
  --smoothing-report /tmp/smooth-full-div64.json \
  --out /tmp/h487-regularized-source.json
```

命令中的 `/tmp` 是示例重生位置；本次实际数据位于会话 scratch 的 `exact-work`。每份输出要求新路径，避免覆盖身份。完整 raw blocks、query cache 和 merged cache 为可由已固定输入重生的数据，不进入 git 或 Release；仓库只保存源代码、此小型说明和必要参数/哈希。
