# 完整永久地点指纹与实际初始自由向量字节：独立纯读取 v2

本条交付完整纯读取源及 run05 两个参数对象。它不执行 F、J、J*、根求解、QP、几何筛或区间科学计算，也不把参数保存等同于实际返回。原 v1 完整源（SHA-256 9202df90d1b9b3f132ebcc85bd00960d4151362fc84e5350e7174d8b49654f02）保留；v2 使用新的文件名和报告 schema，不冒作 v1 已运行。

## 一、实际问题与两种不同身份

重新生成一个 NPZ 可能改变其中记录的 reference、carrier、profile 与路径/来源元数据。不能据整份 NPZ 的 SHA 相异推断自由向量不同，也不能据有限几个浮点摘要相同推断自由向量相同。

本源分别输出：

1. 完整实际 report/manifest 经原 4d9 walker 消费后的地点与 protected 角色指纹；
2. 实际 first606 已保存的 initial-new-field.npz 中全部 core、omega、H 字，按原 7f 完整自由坐标顺序拼接的 array_sha；
3. 完整实际 source、reference、carrier、profile、chart、mesh、原 analytic scalar 参数和原 warm 字节身份。

第 2 项读取现成输入，不重新求解或构造初场。第 3 项仍须分别解释数学目标与工作载体；array SHA 相同本身不是几何证书或精化收敛证明。

## 二、完整历史的精确消费规则

源逐字绑定完整 4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60。Locations.walk、put、grid、angle、tagged、resolve_grid、arrays 及其 stdlib npy_vector 的实际 codefile 均验证同一完整源。

每份输入完整 JSON 都被 walk，不仅提取末端 memory。对单份输入独立 resolve_grid，另外保持未 resolve 的完整有序 union，在每个前缀副本及末端 union 上统一 resolve_grid；此顺序与完整606 all_locations一致。所有 tagged grid 坐标先核实际 carrier 和 N，不把另一观察网格索引重新解释。

指纹包含 curvature、radius、protected 三集合，编码为排序后的 integer cell、float(u).hex()、float(phi).hex()。沿用原字典的 numeric-tuple 去重语义及最终保留的 signed-zero 字，不引入十进制 rounding。各完整输入、各前缀及末端 union 均给 counts/hash，不输出地点数组。

准备报告须为完整4e，M=160、J=923、P=7377、N=2048，reference/carrier 实际文件字节、reference canonical definition、完整 profile canonical definition及来源角色全部相符。每份科学报告须满足明确允许的完整 driver source/schema，核全部 SOURCE_PINS 和实际 source-role map、完整模型、同 reference/profile/carrier。失败报告可以作为历史输入，但不把失败变成成功。

## 三、实际完整初始自由向量

额外两个显式参数指向 first606 的完整实际报告和其已存在的 initial-new-field.npz。该报告必须也是本次完整 manifest 集合的一员，必须是无 restart 的完整 first606；不是从另一段源或另一种模型猜测初点。

完整606 source SHA 为 606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9；原7f meridian SHA 为 7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf。二者先按完整文件字节核；不 import 科学模块。

NPY 解析仅使用 stdlib zipfile、ast、struct：明确接受 v1/v2/v3 header、C-order、准确 shape，所需 float64/int64/Unicode little-endian 数据。拒 object、Fortran-order、其他 dtype、残缺 payload 或非有限浮点字。

实际 NPZ 内完整模型 JSON、canonical model identity、reference bundle identity、固定标量 identity、全角数和积分阶数必须与实际报告一致。实际 reference NPZ 中完整模型和 initial_core、initial_height、mesh 同时读取并核。

原7f中 n=3M+2=482，径向固定槽恰为 0、3(J−1)、3(J−1)+1。程序保留原顺序的其余全部径向槽，再严格按

- core[3:]；
- 所有径向自由槽的完整 482 列 omega 行；
- H；

拼接 hash 流。没有删变量、删均值或作降维。自由量个数必须与原报告 original_variables 完全相等。

初点 core 和 fixed_chart_core 必须与实际 reference initial_core 逐字一致；H 必须与实际 reference initial_height 逐字一致；mesh 亦同。完整 omega 的每个 byte 必须是零，这比浮点近似零更明确，并保持真实 q.initial 的正零字。固定前三 core 字及完整 core/mesh 的原 array_sha 同模型逐项核。

array_sha 完全采用原7f格式：dtype 字串 float64 的 bytes，普通 json.dumps(list(shape)) 的 bytes，随后所有 C-order 原 bytes。这里不使用另造 canonical JSON 替代原 shape 空格约定。输出完整 point hash、原自由量数、core/omega/mesh hashes 和实际 H.hex；不输出 core/omega 数组。

## 四、run05 两次完整参数

第一纯读置于实际 first integral 返回后，显式消费 reference locations 加真实3、17、21、26全报告。第二纯读置于实际 second integral 返回后，再增加真实30全报告。两次均读同一本 run 已保存的 first606 初始 NPZ。

03b 原 fingerprint 没有准入，不能填原 union hash，也不能把05的结果当作原03b集合逐字复现。两次新实际读数只能证明其自身输入及实际消费结果；与原历史的数学义务仍由已登记 source-closed 失败报告空 walker 证明和完整必要再生链承担。未提供、未来或未知报告均不宣称已包括。

原03b28/34/36初根失败报告的完整 walker 空性由另一完整证明处理；本源没有伪造这些报告，没有按 equal count 当集合相等，也不移除任何成功/实际几何方向报告。

## 五、检查状态与边界

完整源由两位代理逐段文字对照，尤其 stdlib NPY、原7f mask、完整 array_sha byte convention 和真实 model/source 守卫已独立审。执行环境仍返回 No usable execution environment，故本条不声称 AST/compile 或实际运行通过。没有 fixture，没有本地科学。

所有输入记录在读取后再核 SHA，输出必须是仓库外新的路径；已有输出不覆盖。现成自由向量字段仅作 byte hash，没有重新求 F 或更新任何模型。完整来源、原 analytic scalar 参数身份与固定 chart 身份分别保留。当前仍没有本题完成标准的精确闭合等距面、连续 metric 界或同g精化结论。

## 六、完整文件身份

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| read_complete_so3_location_and_initial_fingerprints.py | 30400 | e54cad5e7e78f3576412fef82701a3b276fb9af8795ca16d3e016cb9bc0382e7 |
| resume-20261126-run05-history-and-initial-fingerprints-ready.json | 22261 | ebd47e74fcc093f9c9e64874ceb510547638765b4bd854933f29ed32d443f516 |
