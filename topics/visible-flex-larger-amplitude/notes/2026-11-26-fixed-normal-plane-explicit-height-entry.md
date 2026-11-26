# 共同固定法向选枝的独立显式 H 初点入口

状态：完整独立三源及参数请求已形成；尚未科学执行。原 normal 的五份锁源均不修改。原 H 的 normal 请求可以先运行，不等待本入口，也不把尚未返回的原 H 结果写成失败或成功。

本次沿已刊 8f375 完整 gamma-H 入口的 fresh-only 双输入原则，只在原 reference / Q / base.initial 全部校验之后复制末 H。法向分段、完整六控制、全部上游角/参数隐式链、目标 g、原所有自由量和外层求解主体不变。

## 1. 明确输入顺序与原始身份

`--initial-height-hex` 为必填规范有限 binary64 字。解析不声称高度可行，正性和原幅度/域要求由原真实物理检查处理。

driver 的原 same-reference 与 new-reference 两分支完全保留。旧 Q 输入用原 `trace_initial_full_point_sha256`；新 ea94 定义用当前 `initial_full_point_sha256`。二者都先核真实完整 base.initial，再构造完整42ea operator 和原norm。不会把修改后的当前 H 写回初始参考摘要、Q definition 或模型。

只有在以下真实状态全为空/零后才选择显式 H：

- `q._root_cache`、`q._current_x`、`q._current_point_sha256`；
- 原 `q.endpoint_counts`；
- 全部实际 `q.normal_counts`；
- `q._last_normal_batch`。

这使用 normal 的真实接口，没有保留不存在的 KKT 或 continuation counters。上述状态仅验证本次入口确实在第一次 endpoint 读取前；它不要求原 H 的 root 先成功，也不另做一遍原 H 的 F/J。

新的 current x 是原点的独立复制，唯一赋值是 `x[-1]=H_literal`。全非 H 前缀逐字检查；原 base.initial 未修改，完整 q/model、base、g、Q、chart 与 reference 身份在修改前后相同。H 仍是后续 QP 的原自由变量。

本源明确拒绝任何 restart 或 direct-base-seed 参数。以后如需延续一个实际返回场，必须使用能完整绑定该真实来源的另一个明确入口；本次不会把新高度混到另一未知种子的其余坐标中。

## 2. 同一有限选枝定义，全导数不变

42ea operator 保持原字节；每个角和候选都使用同一固定准确分段。首版 m=32，段方程仍为
$$
u_i=u_{i-1}+A_{i-1}^{T}\eta_i,\qquad
f(x,\phi,u_i)=(1-\tau_i)f(x,\phi,0),\qquad A_{i-1}=f_u(x,\phi,u_{i-1}).
$$
H 属于当前 x。右端零控制 closure、每个前段控制和 A、终点帽位置所含的 H 导数，仍由未改的完整 $6m/9m$ 隐式链传递。没有为了改 H 把它从导数图中冻结，也没有再计算或重选 Q。

改变初始自由点不会改变同一模型映射 x→F 的定义。准确分段、原六控制范数、根24×18预算、物理closure容差、全部原正权 Gram 行和外层H²坐标都保留。采用另一个显式高度不是已证明的必要条件，也不保证该点在有限法向选枝域内。

参数 ready 沿用已观察的 `0x1.ec0bc59b655d2p+0`。该字来自旧运行实际报告399ae819的工作 Jstar，曾用于原 H-only 请求。这里仅采用一个明确常量；不称它是本次 reference 的准确或工作积分，不继承旧场、旧 root 或旧几何。原 H normal 的实际返回会决定是否执行此 ready，不提前替它归因。

## 3. 全外层循环及报告

新 driver 从68a6完整源派生。`def save_report():` 至 EOF 与68a6及5134逐字相同，完整suffix SHA为
`9b05f8e00c483491ffd9259b2d675af940c6f0b8a8104d6bfcd70ffb0e31b4ee`。

因而原全场初读、全部metric rows、J/J*、完整QP、192选择器、幅度双支、Phase I、真实ray与永久位置集合、拒绝点记忆和最后独立真读均未改变。2557几何adapter与42ea物理operator完全不改。

新增记录沿8f合同：

- 原/新完整初点摘要，原/新H准确hex及Fraction；
- 原/新非H前缀摘要、完整维数、末槽索引、dtype/shape；
- 未修改的model/base/fixed-g/Q/reference身份；
- 两模式中实际用于原初点校验的字段名；
- root/counter/batch确尚未读取；
- 初始高度选择不代表物理场被接受，不继承旧Phi/root/geometry。

这些记录在第一次真实F/根前保存。初次成功统计的当前点摘要与domain H，或初次失败snapshot的当前点摘要，必须对应修改后的点。

新reader保留8381完整normal model/分段/34snapshot/current-vs-latest合同，再纯读新增H记录。它只作来源/JSON/字节摘要归因，不重算F、root、J或完整自由数组，也不把工作断言当作连续证书。若根失败，current数值为空仍保持null；不会从原H或别的点补数。

## 4. 完整来源

| 完整新文件 | 字节 | SHA256 |
|---|---:|---|
| fullclosed_zero_normal_lift_height_so3_qp.py | 71176 | e8e096f9a2a2acd5b08e907aa2b9df1fc9a402d033f67e1420f072dc579c6fe7 |
| launch_zero_normal_lift_height_so3_actions.py | 15860 | b7e56936ba3746fe44c5322464d9c391670df2ea529448132b5c4fbf0018e9f2 |
| read_zero_normal_lift_height_so3_report.py | 52228 | f8261f971d7993534d7e020efaef5ca480c51ba2d2da7861d18e6a18d2af799b |

完整父入口分别为：

- driver `68a6e483a4916d72411d08647622a1e539b26f9eca3c1449b4e7399bec17dd38`；
- launcher `c5f139bac6ecb50aa4b31de0aa8f5da4f2feafc2b26bc821826fc31a0c6f5c46`；
- reader `8381cd9e034fda5917cae5f221f0c3f5420953cab6ca8dd809c82f3de0f7e1e8`。

显式fresh-H原则来源是完整 `8f37529deaa8e07d4561e00371b39b82cb641a4e52e0790d41555b2ae9e320a9`；本次只将其真实未读检查与独立report/schema/pins适配到 normal 接口。SOURCE_PINS 保原normal全部闭包，不添加替代科学实现。

已独立完成完整文字/hash/suffix与字段对照，无所读阻断。launcher的parse_args除install/print两flag后与driver完全一致。当前终端不可用，本次没有实际AST/compile，也没有科学或fixture；不把静态审称为运行验证。

## 5. 队列与同 g 历史

ready 保留原 N2048/M160/J923/P7377、全部自由量与正权行、m32、原一条metric最多16步、四条restoration各64步、15ray、mu=.01及既定geometry/amplitude预算。它只是一个待实际返回后选择的独立初点请求，不把方向预算当作完成标准或能力上限。

参数包含本次reference位置、3/17/21/26/30的全部真实再生报告、gamma-H报告和原H normal报告。任何其后真实新增且有地址的报告须在实际准入时显式追加；若某报告尚未运行或不存在，不能假填来源/空集合。不同raw/model字节、另一个H或另一个root选择都不是删除同g永久位置的理由。

原H normal和本H normal属于同一目标及完整模型映射，然而它们有不同初始自由点，必须分别真读各自baseline。不能跨点借Phi、已存根、曲率/支持、whole-image幅度或连续证书。最终课题的等距精度、全相位闭嵌入、握持幅度、Euclidean商、reach和固定问题精化标准保持原文。
