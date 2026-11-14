# R254 完整前缀精确非平面性消费者接口

日期：2026-11-14。

## 状态与对象

[R254](../results/R254-exact-full-prefix-no-planar-germ.md) 给出完整条件证明及完备有限见证集；消费者是 [geometry_20261114_prefix_exact_nonplanarity.py](../computations/geometry_20261114_prefix_exact_nonplanarity.py)。

本 note、proof 和 consumer 在执行环境失联后通过 GitHub 小文本接口重新保全，使用本次真实 blob 身份；没有把失联本地文件的 SHA 当作恢复文件的 SHA。恢复消费者尚未在新 Actions 执行，本 note 不报告不存在的数值或 AST 回执。

证书对象是所有实际物理节点上共享 binary64 值、一阶及二阶 jets 所确定的唯一实 Hermite quintic，保留全部 3M+2 状态及完整 z0。R249 修补场使用已投影的共享 nodal arrays；原场使用未投影数组。浮点多项式系数及位置读出是这一规范形的近似，不能仅凭本证书称其逐位满足所有 C2 等式。

## 在实际接受后运行

优先把实际新闭包的 assembly 和 plan 一起传入，入口规范形从实际 assembly 读取，不在检查时悄悄换面：

~~~sh
python -u "$COMP/geometry_20261114_prefix_exact_nonplanarity.py" \
  --checkpoint "$ACTUAL" \
  --assembly "$NORMALIZED_CLOSED/surface-assembly.json" \
  --plan "$NORMALIZED_CLOSED/surface-plan.json" \
  --out "$OUT/R254-prefix-nonplanarity.json"
~~~

这些路径指本次真正接受的完整场及由它生成的同一闭包，不能指旧 A。执行被限制到 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public。

若尚未生成闭包，也可明确只核该 checkpoint 的指定前缀对象：

~~~sh
python -u "$COMP/geometry_20261114_prefix_exact_nonplanarity.py" \
  --checkpoint "$ACTUAL" \
  --inlet-normalization r249 \
  --out "$OUT/R254-prefix-nonplanarity.json"
~~~

选择 original 则读取原前缀。没有 assembly 时报告不会声称与某个既存闭包的 nodal 字节已绑定。该入口不重解 BVP、不求新尾；构造 reader 所需原有限方程二阶 nodal 读出仍属于实际 Actions 计算。

如果同一 job 已持有完整 SavedPrefix，可避免重复生成二阶 nodes：

~~~python
from geometry_20261114_prefix_exact_nonplanarity import certify_prefix, write_outputs
report, witnesses = certify_prefix(saved, assembly=assembly_data, plan=plan_data)
write_outputs(output_path, report, witnesses)
~~~

这里的 saved 必须是产生所引用 assembly 的同一个明确对象，或有匹配的既存 R249 nodal SHA。

## 精确搜索与返回含义

每个 cell 首先在六个有理径向位置和四个 cardinal 物理圆点中找四个仿射独立位置。位置由精确 Fraction Hermite 插值和有理圆递推合成；不用浮点三角函数、材料角逆图或显示网格。

默认快速搜索未找到时，进入 R254 的完备网格：六个径向位置和 4M+3 个有理圆点。若这个完整网格仍无四点见证，R254 证明该具体精确有限 cell 的像在某个平面内。可选 --cardinal-only 只做快速搜索；此时未找到只能写 unresolved，绝不能写 planar。

全部 cells 通过时返回 0；有证明为 planar 的 cell 或未解决 cell 时返回 2。此返回码是本项证书结果，不改原 BVP 接受旗，也不创设新的 full-DN 接受条件。

## 身份绑定与完整输出

摘要同时记录 checkpoint、reader、consumer、完整 scalar、全部物理节点和三个 nodal 数组身份，并比较 plan/assembly 中的完整 prefix definition。R249 的 normal_form_nodal_jet_sha256 存在时逐一核对。若原 assembly 未事先保存其原 DDY 的 SHA，本次新生成 nodal hash 只给出这个明确新实例的身份，不能反推旧舍入读出逐字相同。

每个 cell 的四个有理参数、精确位置、精确行列式和符号被完整保存。大整数用带符号十六进制分子与正分母记录；gzip 见证按单文件小于 5 MB 分片，并记录原始内容及压缩文件 SHA。摘要不会用一个浮点 determinant 阈值替代整数非零证明。

同一 cell 的四点可来自不同 s。完整角世界坐标带宽是 2M+1，而不是只有高度的 2M。T_m 的状态索引是 M+m，Z_m 的索引是 2M+1+m，m=0 的完整 Z0 一直保留。固定角线性合成与径向 Hermite 插值严格交换；消费者没有用四角插值替换完整角函数。

## 仍然未付的整面条件

全通过只证明这一精确完整前缀没有平面参数开片。在真实材料图正密度、单一整体 SE(2) 配准和 R248 相位定义的条件下，可传递至全相位和反射片。

新的 tail、collar、外 cut correction、完整平面 germ 补集拓扑、marker 的刚性锁定假设、全局嵌入、真实整像变化仍需本次对象的证据。旧 R243 的不同尾部不能借名移用。输出保持 actual_delta_E_certified=false、exact_nonlinear_limit_nonplanarity_certified=false、task_completed=false。
