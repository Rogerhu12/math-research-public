# 同一实际固定深谷父场的 normalized-parent SO3 来源绑定

本项只修实际父输入的来源绑定与纯读取接口；不重新证明 R690、R694、R695，不把源码准备称作真实场运行成功。

## 1. 已实际返回的证据

公开运行 [45800076687/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45800076687) 的 [part 003](2026-11-26-public-actions-45800076687-1-part-003.md) stage 38 是完整 `d3c35492…` 深谷固定目标父场。它的真实输出为：

- report：`86a79cc29fec40a6e1515fac355e7925c7fcae459dff4a76baddfbadddee45d5`；
- bundle：`d021a50a492b941004ee75f5cba138d5b5bc07092073a642a027bde4f97bb478`；
- 固定 scalar 身份：`0a223b986f35263c168e26d30295fd84048e134c6b053ba90c7cd39beaf1f5cb`。

这些身份取自实际公开返回；本项没有在本地读取 runner 数组或计算该场。

[part 004](2026-11-26-public-actions-45800076687-1-part-004.md) stage 39 运行原 `9b770c78…` launcher，真实 6.164027589999932 秒后 exit 1。只有 command JSON 输出，没有 report、initial-new-field 或 final。stage 40 纯 reader 因以不存在的 final 作为控制器输入而 setup failure，不能另算一个科学失败。stage 41 使用 `ef017af5…` 读取真实旧日志，返回 log SHA `6276a0471e8ae6d22c03cd74046aba82c8ab7641be0a6cf4fd8abe7d1e100311`、4332 bytes；它只取最后一块 traceback，实际得到外层 `subprocess.CalledProcessError`。

stage 42 已使用已刊 `ef60ec41…` 实际读取同一 journal/log 中的有界全部 traceback 块：6.173127965999811 秒、exit 0，输出 `9988458928f0bc7d1271ffca6a3f59721b782ea30f73285db4ab6f77d991b60d`（6089 bytes）。返回明确有两块 traceback，内部先在原 driver 第 127 行 `actual_parent` 抛出 `ValueError: Retain the selected exact deep profile and physical eta definition`，随后才是 launcher 的外层 `CalledProcessError`。真实父、source commit、原 child exit 及 log SHA/bytes 均与 stage 39/41 一致；这次没有科学重跑。结合该同一条件中硬编码的 `383168fb…` 与已返父 `0a223b98…`，这是实际固定 profile 守卫拒绝，未进入完整新场读取。此证据不预先宣称后续其他构造条件均通过。

## 2. 独立静态发现与原有通用检查

原完整 driver `9cf5c825…` 在入口、重建 context、restart、报告和统计中使用一次旧运行的固定常量 `383168fb…`；原 reader `32bdbb6e…` 也固定该常量。这与当前 stage 38 的真实 `0a223b98…` 明确不同。只把常量替换为另一个运行的常量无法表达「每次先核定一个完整父场，再在所有方向中保持该目标」的来源责任。

原 `d80f9af2…` 的 `verify_fixed_target` **没有** 硬写 `383168fb…`。它已经核对 canonical profile hash、e091/4ae/2e 物理定义、初末 context 完整等号、完整固定目标标志和初末谱参数/测度。新的入口直接复用该函数；对真实 `329ebd18…` 多轮 SOC 父场还保留原 `bind_report` 对完整 driver 派生体和所有运行角色的检查。没有复制成另一个放宽版本，也没有把旧 source SHA 标给新函数。

## 3. 新增的输入与实际构造闭环

`so3_same_parent_fixed_scalar_binding.py` 在实际公共 Actions 中接收原完整父报告和完整输入。它先完成原 d80 核验，再把下列同一对象冻结为一个 binding：

1. 原父报告的真实 bytes 与完整源身份、其已证明保持不变的完整 canonical scalar definition；
2. 实际 parent bundle、observation carrier、symbolic node report、scalar input 四项 bytes；
3. e091 definition 内的 `original_input`，必须正好是该 scalar input 和实际 scalar/integer/Hold 三源码；
4. 父 canonical 模型中的四 scalar/observation 源及 dense/batch/observed 全算子源；
5. 原 exact eta、lambda 1、原完整角网格和 symbolic nodes 的目标身份。

这里的 hash 只声明来源与逐字一致性，不声称不同 bytes 的输入在数学上不可能等价；本入口不进行未声明的输入等价迁移。

新 driver 在这些检查通过后只赋值一次局部 `fixed_profile`，其值来自该实际完整父定义。在构造任何新场以前该值已经固定。随后仍调用原 `4ae012fb…` factory 建立完整物理父问题。新增 `bind_rebuilt_context` 独立检查：

- 实际 `context.definition/create_pair` 的代码文件确为原 4ae，实际 scalar evaluator 确为 e091；
- `context.deep.definition` 与先冻结的完整 profile 逐项相同，canonical hash 相同；
- 重建后的 **整个** context definition 与父报告 final definition、父 binding definition 完全相同；
- 四实际输入仍为同一 bytes；
- 完整算子源实际文件与记录一致；
- 实际 bundle 内的 `reference_tail_model_json` 与重建后的整个 canonical definition 一致。

原 driver 自身的 context 等号仍保留。原 `d3f25bb7…` 父 meridian kernel 还会继续核对 actual bundle 中全部 q/core/H、其 shared quintic、所有真实物理 source 函数及完整模型；新 binder 没有替代该独立检查。

## 4. 数学表示与完整优化不变

原三物理源码完全逐字保留：

- `so3_parent_meridian_jet.py`：`d3f25bb74e179865b20f7759bc1ee8dcdf2c2771f062ac096ee4d5398a8be4b9`；
- `so3_closed_meridian_operator.py`：`234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42`；
- `so3_closed_meridian_geometry.py`：`72f3825913c9ac07b30dcbc47f34e4d8ad901c2f6b6cab0cdc50f35ab99a3cc6`。

因此仍是固定父 $T_0=F_{\mathrm{parent},s}/|F_{\mathrm{parent},s}|$ 的 normalized-parent SO3 场，实际 $F=G+h\Delta$；全部 $h'\Delta$、$h''\Delta$ 与角混合项参加全部 Gram、完整 J/J*、几何和幅度读取。它与直接轴对称 T0 入口及零 $\Delta$ 入口是不同表示。本项没有借用它们的 source/model 或证书。

所有原 free core、全部 SO3 shared-quintic omega 自由 jets 和 H 均保留。完整角/径向观测与正权、明确 H² 型坐标范数、原 192 行选择、完整永久 curvature/radius 集、每点双符号幅度筛与全部选择幅度行、全 C common-slack Phase I 和真实非线性验收，仍为原完整算法。历史 literal phi 在此仍按原说明作为固定父材料图的新场地址读取；没有宣称跨模型同一物理点或证书自动传递。

新目标仍是由实际完整父输入确定的同一 $g=ds^2+a_{\mathrm{deep}}(s)^2d\theta_0^2$。新的 SO3 初始化会改变物理场，所以必须重新完整读取初场；不从旧父 Phi 相减，不继承其连续度量/几何。

## 5. 完整源码派生与纯 reader

新增完整 source 文件是：

- `fullclosed_so3_actual_profile_qp.py`；
- `launch_so3_actual_profile_actions.py`；
- `read_so3_actual_profile_report.py`；
- `so3_same_parent_fixed_scalar_binding.py`；
- `derive_so3_actual_profile_entry.py`。

派生器先核原三完整 source 的 SHA。所有 driver 顶层函数/类（除输入绑定与 main 的声明接线）均实际逐 AST 比较相同。main 的完整 diff 只含 actual binder、一次固定 profile、重建 context 验证及其报告字段；优化、线筛、Phase I、J/J* 等科学主体未变。新 source/schema 如实独立，不更名冒原字节身份。

新 launcher 对实际 child 使用 `check=False` 然后按真实 return code `SystemExit`；这样不会再向子 driver 已打印的真实 traceback 后追加一个遮蔽第一原因的外层 Python traceback。argv、计算预算和返回失败语义不变。

纯 reader 逐字核其完整 driver 与所有 source 角色，复核 binding 的 canonical 身份、实际四输入、实际 context、冻结父物理模型和完整固定 profile。初末、每方向起点/接受值及已记录真实 trial 统计均使用同一个从报告完整绑定中恢复的目标身份；不再比较旧运行常量。仍保原 Phase I、全部行和真实几何语义，complete 报告才允许 verify final。reader 不导入 numpy/scipy/torch、不重算 F/J 或科学数组。

## 6. 真实运行参数与紧凑返回

`so3-actual-profile-complete-ready-steps.json` 只准备从已返 stage 38 完整父输入继续的两个步骤：完整 solver 与纯 reader。新 outdir 为 `so3-closed-actual-profile-first`，不会覆盖失败目录或旧报告。

保原 N=2048、全部 923 shared-quintic 节点、完整原频谱变量、Gauss order 8、angle block 8、stage block 64、jet-sum 范数（radial length .05、angular transition 24）、明确 $\mu=.01$、$p=4$；先至多四个全 C Phase I 方向各 max64，再一个完整 metric 方向 max16。Dmarked=4.2、L=.9、H floor=1.01、reach ratio=.03、safety=.992 均保持。此预算完成不代表课题完成。

纯 reader 的控制器 parent 使用已经存在的原 deep final，而非可能尚不存在的新 SO3 final。summary 只发布真正 scalar 叶子；方向列表、counts 字典、幅度字典、永久位置字典均拆成叶子。完整原报告、全部场缓存与日志仍留 runner。

新步骤不请求删除整个 `frozen-parent-meridian-cache`，避免旧控制器把其大量逐文件名列入发布元数据而超过 GitHub 小文本上限；只保原有限 rows 缓存清理。该选择不改变科学结果。

## 7. 验证范围

本地实际只完成源码派生、AST/compile、重复关键字/字典检查、source SHA 与 byte 数、完整 diff 和 CLI 参数声明核对。没有运行科学字段、fake fixture、root 检验或数值证明。

第一异常已由同一实际日志的 stage 42 全 traceback 读取确认；新入口是否通过全部构造、完整初场读取和方向预算，仍必须等待它自己的公共 Actions 返回。高误差场不因此被安排昂贵完整连续 Gram 认证；目标 completion、全域度量、全 t 同场几何与固定参数真实精化责任均未转移。

## 8. 实际队列字节守卫与无损准入修复

02在12:49:39 UTC的实际索引报告 `Followup request must be a complete small repository JSON file`，所以新两step尚未被准入，不是新科学子进程失败。完整队列追加后为98126B；原完整控制器的95000B上限保留。仅去JSON缩进后为80236B，标准JSON解析后与原对象逐项全等，16个完整step、全部命令字符串/数值/summary/清理选择和顺序均保。未删任何步骤/变量/科学行，也没有调整限额或把raw另存成参数。新完整来源绑定重跑仍须它自己的实际返回。
