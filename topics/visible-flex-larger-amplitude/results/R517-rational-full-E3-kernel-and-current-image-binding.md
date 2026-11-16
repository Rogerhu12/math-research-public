# R517 — 原完整像球账到含反射欧氏商下界的有理执行接口

2026-11-16；作者：OpenAI ChatGPT /root/geometry（AI）。

**状态：已完成来源明确的执行源码与条件适用接口。正确性使用已证明的 [R516](R516-finite-full-E3-cover-and-quantitative-quotient-distance.md)，限本文明确的完整输入条件；本次没有执行科学算术、import、AST、编译、fixture 或运行实验。没有实际 accepted450、实际 $\gamma$、商距离证书或已接请求。** 本文件与新源码完成即可登记，不把独立复核、试跑或此定量消费者增加为原 BVP、FD、metric、reach 或课题完成的前门。

新文件是
[geometry_20261116_full_E3_quotient_lower_bound.py](../computations/geometry_20261116_full_E3_quotient_lower_bound.py)，
39936 B，SHA-256
0c69c61c09a8f518e792495fd1109b7f310d57da69676368a51233b648a4ba89，
Git blob 9a0f1a94cf0d40ec3d31f2708c04c15332ccf3af。

## 517.1 已接的准确范围与尚未连接的边界

本次只登记下列真实字节组合：

| 角色 | 原文件 | 字节数 | SHA-256 |
|---|---|---:|---|
| 整个当前闭面的位置覆盖、原活动见证与完整来源 | geometry_20261115_current_C_ten_held_and_rigidity_inputs.py | 53711 | c87b3a9b9d17f74d8c4f4066f65318e50fed5a56143f620628049a86dcf77ef2 |
| 同场固定两帽、准确有理图及完整标记列表 | geometry_20261115_current_C_ten450_fixed_cap_balls.py | 23622 | 0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae |
| 数学定理 | R516-finite-full-E3-cover-and-quantitative-quotient-distance.md | 16623 | 3f6b5ea376a83c251ec738e545a1b75f59b5d414ff6b5494b1c999951f028e85 |

R516 已正式刊于 72fb94da7843b48b01509a3359864e27f43f8cbf。R425 和 R417 的原源保持不变。新模块实际检查两个原源码文件的完整字节哈希，并要求调用时 computations 就是新模块的真实 HERE。它不以文件名、相同 schema 或继承类名称把以后生成的原生 M/新材料/新来源视图冒成上述 c87b/0ff1。

这里接的是一个已经实际生成的 R425 临时结果目录及其完整位置账，未接：

- 原 owned launcher、TERM/KILL/reap 或全 namespace 静默观察；
- 任何具体 request、workflow、R425 新一轮生产或已有运行的续接；
- 后继 generated-view 来源和别的帽实现；
- 自动增密整个曲面的见证网、自动收紧 C 系数信息或选择 $\gamma$；
- 原 native/准确几何之间的误差、全 $t$ 嵌入、reach、同 $g$ 精化和课题完成判断。

未来同现场调用者须真实绑定其原 R425 输出、原绝对 deadline 及所有者，再调用本 API。当前 API 保存调用者给出的 clock provenance，并反复调用其 budget callback；**它没有独立验证该记录确来自当前 owned launcher，不能把一份任意非空字典当成实际 deadline 已绑定的证明。** 原结果本身不含本 API 可单独核回的全部 job 所有权字段，这层实际 same-job/owner 绑定仍属于后继调用者。本文不填未来来源或科学结果。

## 517.2 输入完整性：实际球覆盖先于任何群搜索

主入口为 keyword-only 函数：

~~~python
produce(
    *,
    computations,
    directory,
    result_sha256,
    out,
    cap_points,
    desired_gamma,
    sqrt_bits,
    max_boxes,
    max_distance_evaluations,
    max_cover_balls,
    max_depth,
    check_budget,
    caller_clock_identity,
)
~~~

这是函数 API，没有假设已经存在的命令行调度器。只有指定公开仓库 Actions 中的调用通过 actions()；源码文本和上述签名不构成本地运行许可。

directory 必须指向同现场真实 R425 输出，result_sha256 是该目录完整 result.json 的实际哈希。bind_r425 的读取顺序如下：

1. 核实际 c87b 与 0ff1 两源码；读完整 result.json 并核其原 schema、source.file/source.sha256 和给定完整哈希。
2. 通过 result.members.input_binding 核完整 input-binding.json 的相对路径、字节数、SHA，再核其准确 canonical identity 等于原 actual_input_binding_identity。
3. 通过 result.members.position_result 核完整 whole-image-position-result.json；要求其完整对象与原 result.position 相同，不从摘要抽出一个成功标记替代原件。
4. 核原完整 R413 attachment、原 shared binding、完整当前十参数 target identity、原帽 source 与原当前场 target 的对应关系。
5. 完整读原 actual_witness_points，核其实际字节身份及其与原 result.actual_witness_parameters_and_boxes 的逐对象一致。
6. 完整读取原位置 gzip 账，分别核 stored 和 decoded 的所有字节、SHA、总行数和 ordinal 顺序，并处理每一原行。

成员路径不得绝对化或用 .. 逃出实际原目录；字节校验前后也核实际重新读取对象的身份。原数据只读，不能用新摘要覆盖旧 ledger 或旧 result。

群搜索所用球必须来自完整原位置覆盖。源码具体要求：

- whole_closed_position_cover_completed 为原 true；
- completed_roots 等于 total_roots；
- fixed_cap_root_count 等于 2；
- 原 pending.current_root 为 null，complete_closed_frontier 为空；
- 原 unvisited_root_half_open_suffix 是 [total_roots,total_roots]；
- 全账终端数与原 terminal_position_domains 相同；
- 严格盘外数与原 strict_empty_disk_intersections 相同；
- 全部终端球集合非空。

这是把 R516 的“完整包含”前提落实到已有 producer 的实际输出，不是给原 BVP 增加一个新的科学接受条件。若本消费者缺这份输入，它只报告自己的完整覆盖责任未付，不撤销或重标任何原 solver 结果。

原 R425 在位置覆盖之后还会执行 prefix/tail 非平面输入。它们失败或未完时，只要位置覆盖原件确实完整，位置球和成员点仍可独立被本 API 使用。源码不要求原 R238 hypotheses、marker 条件、reach、metric、embedding 或 all_requested_consumption_returned 为 true。

## 517.3 从原全账得到两个整个像的球覆盖

原位置账为：

~~~text
large-arrays/complete-current-position-cover.jsonl.gz
~~~

源码接受原三种记录，并保其原 ordinal：

| 原 kind | 本消费者处理 |
|---|---|
| complete_closed_position_terminal | 按原 cell.kind 与 enclosure.center/radius 收入完整球表 |
| complete_closed_split | 读取并计数，保整账身份；它不是额外终端球 |
| empty_closed_disk_intersection | 仅接受 cap 且原 strict_outside_test=true 的严格盘外情形 |

其他 kind、未知 cell.kind、原计数不合或不完整 decoded 账均保具体错误；不猜成功、补零或省去未识别记录。

设 R425 原完整像为 $S_0=A\cup C_+\cup C_-$，另一端为
$S_1=R_{\pi/2}A\cup C_+\cup C_-$。代码对每个 terminal 实际形成两球：

- active：$S_0$ 原球心 $(x,y,z)$；$S_1$ 球心准确为 $(-y,x,z)$。
- cap：两个球心都保持原值。
- 两种情形半径均保持同一准确原半径。

全部 prefix、tail、cut patch、collar、反射片、角端点、闭缝与两整帽由原完整位置宇宙负责；本程序不按片名重新删球，也不把两帽一起旋转。整账身份和 producer 的完整位置结果共同保留这项来源责任。

全部球中心与半径按准确有理表示读取。完整遍历后，sqrt_bounds 的上端给

$$
R_a=\max_j\bigl(\operatorname{up}\sqrt{\|c_{aj}\|^2}+r_{aj}\bigr),
\qquad a=0,1.
$$

R0/R1 必须读完全部球才形成。若在整账或范数遍历中断，只有当前原 ordinal/球索引与未访范围，不能用已访部分的最大值充整个像的上界。原 position_radius_goal 或 work-resolution 目标不参与本程序的成功前提；合法粗球会降低辨别力，但不会变成不合法球。

## 517.4 真正成员见证与两帽的准确有理求值

原 R425 活动见证逐行提供：

~~~text
index
actual_parameters
phase0_position_center / phase0_position_radius
quarter_turn_center / quarter_turn_radius
~~~

源码核原 index 顺序与准确四分之一转关系，再分别放入 $S_0,S_1$ 成员球。包含球中心不被宣称为真实成员。

R516 第9节已经证明：只用这些活动见证时，逆四分之一转会使两向见证全部对齐，不能从该见证下界得到正的全欧氏商距离。本 API 因此接受显式非空 cap_points 列表；这不是让某个固定帽点组合成为额外科学门，而是本方法的输入范围声明。每项严格为：

~~~text
{"x": <exact rational>, "y": <exact rational>, "upper": <bool>}
~~~

x/y 使用准确有理字符串、整数或 Fraction，拒绝浮点推断；upper 只能是实际 bool。参数必须满足原闭盘 $x^2+y^2\le r_c^2$，包括边界。exact_cap_point 实际读取已绑定 R417 的：

- original_cuff.exact_rational；
- exact_height；
- 完整 markers，含每一项 current_marker_list_index、upper、center_exact、radius_exact、amplitude_exact。

它计算原图本身：

$$
p_\sigma(x,y)=
\left(x,y,\ \sigma\left[
H+\sum_{\text{同一侧的全部 }j}
A_j\max\left(0,1-\frac{(x-a_j)^2+(y-b_j)^2}{R_j^2}\right)^4
\right]\right),
\quad \sigma=\pm1.
$$

负振幅、重叠支撑和零项都按原全列表处理。下帽是 $\sigma(H+b_\sigma)$，不是 $\sigma H+b_\sigma$。支撑中心的平面坐标不自动给峰顶；即使参数恰选标记中心，也仍求完整求和图值。

**只有这里绑定的 R417 参数与高度确是上述准确有理定义时，所得球才取 $e=0$。** 本代码没有把渲染高度、binary64 近似的实系数或未注册帽图读作相同定义。若以后帽含新的非有理参数，必须用对应实际误差球，不能继承本接口的零误差。

固定两帽在两个端点逐点不动，所以同一实际帽点加入两向见证集合。有限 cap_points 不保证充分分辨、覆盖两帽或趋密；若要引用 R516 第8节的有限终止结论，还须由真实生产计划完成整个两帽与活动片的趋密见证条件。当前没有自动补这份网，也没有声称几个支撑点足够。

## 517.5 完整 $E(3)$ 宇宙与原定理对应

令显式候选下界为准确有理 $\gamma>0$，取 $B=R_0+R_1+\gamma$。R516 第3节已证明：闭立方体 $[-B,B]^3$ 外的平移严格给距离大于 $\gamma$，边界留在内部处理。代码不把有限平移范围假设成完整群。

quaternion_matrix 用原齐次二次四元数矩阵及准确分母 $\sum v_i^2$。四个图各固定一个 $v_i=1$，其余三个取完整 $[-1,1]$；每个图再分为 $R(v)$ 与 $R(v)J$，$J=\operatorname{diag}(-1,1,1)$。反射是右乘，代码准确改变第一列符号。由 R516 第4节，八个六维闭根盒确实覆盖整个内部正交/平移宇宙，图交叠和最大坐标并列处不省略。

每盒中心是准确有理参数，产生准确正交矩阵和有理平移。对旋转/平移半宽，代码分别取

$$
\eta=\min\{2,2(h_1+h_2+h_3)\},\qquad
\beta=k_1+k_2+k_3.
$$

center_bound 对两向每个真实成员球，遍历相反整个像的每一个目标球，再按 R516 (516.14)–(516.19) 形成

$$
\Lambda=\max\{0,L_*-\eta R_1-\beta\}.
$$

目标球的最小值必须全遍历才有效。没有按近邻、核心范围、相同帽或已访目标的局部最小代替它；完整两向并非只取一向或材料配对。sqrt_bounds 用原整数 isqrt 构造严格有理下端；范数上界则用其上端。没有未经包围的硬件开方。

TransformCover 的根顺序为 proper charts 0..3，继之 improper charts 0..3。每次按 depth % 6 选坐标闭二分；两个子盒都保公共中点。父盒只有在两个完整子盒写入实际 decision ledger 后才从栈移走。

每盒只有真实 $\Lambda\ge\gamma$ 才作为本变换覆盖的 paid box；这条分支只决定商距离计算付了哪些盒，不改变原科学 solver 门。全部八根都完成才返回：

~~~text
whole_closed_transform_cover_completed = true
global_quotient_distance_lower = gamma
delta_E_lower = gamma
~~~

其中 delta_E 只使用 $\max_t d_E(S_t,S_0)\ge d_E(S_1,S_0)$，没有把两个端点冒作全 $t$ 嵌入证书。若同场原 position 给实际完整直径上界 $D_+>0$，源码另报告 $\gamma/D_+$ 和 $20\gamma\ge D_+$ 的明确较强比例条件。没有用活动核心直径、帽环宽或别的场代替 $D_+$；未完成全群时相应全局字段保持 null。

## 517.6 资源控制、完整前沿与中断的真实含义

全部资源由调用者显式提供，没有隐藏科学阈值：

| 参数 | 准确含义 |
|---|---|
| desired_gamma | 本次请求认证的正有理下界；未替代 solver tolerance |
| sqrt_bits | 0..8192 的整数工作精度，用于有理根界 |
| max_boxes | 正整数，真实开始处理的变换盒数上限 |
| max_distance_evaluations | 正整数，两向原见证与目标球距离计算的工作上限 |
| max_cover_balls | 正整数，完整位置账终端球读取的资源上限 |
| max_depth | 非负整数，六维闭二分深度工作上限 |
| check_budget | 原同现场绝对钟、reserve、signal/resource 策略的实际 callback |
| caller_clock_identity | 调用者实际 clock 来源记录；由调用者绑定，不在本 API 自证 |

check_budget 在读取大成员的分块边界、每位置行、每原点/帽点、每整像范数点、每变换盒与每距离项之前执行。Work.begin 先检查时钟和资源，再增加相应实际计数。原 callback 可以直接抛 Stop；也可将原资源异常以 cause 保留而重抛 Stop。其他异常按原类型、消息、完整 traceback 记录，不能吞成数学成功或自动改 tolerance。

这是边界检查接口。一个大整数操作、单次文件读写或记录序列化本身不是硬绝对 deadline kill；未来 owned caller 仍须负责原 TERM/KILL/reap 和真正静默。当前源码没有重开 clock、启动子进程或安装一套伪 owned 状态。

中断范围分为三层：

1. 原输入尚未全绑：保 actual_input_cursor、原可观测 result 状态、完整原 position.pending、原 counts、错误和资源停止。原 result 中缺键仍缺，不填成 null 或零。position_member_equals_original_result 仅在真正核完该原件时才出现。
2. 帽成员或全账读取途中：帽游标保当前实际参数、总数、含当前项的未访半开后缀；原 gzip 游标保 next_ordinal、声明总行数、已解码前缀字节。中断整像范数时保当前完整球索引/总数。尚未建立完整图像时八个群根全部未启动。
3. 已进变换覆盖：保完整闭栈、当前根、全部未访根对象及半开后缀、当前方向/真实见证索引/目标球索引/未访目标后缀。visited_target_minimum 明确标为非全局；它不进入本盒或整个群的已付下界。

遇到深度上限时，当前未付盒仍留原栈，原实际中心下界另写 ledger。下界不足不是全等证明、不是 $\gamma$ 不可能的证明，也不阻止以后在原责任范围内继续工作。发生资源停止后不会从 partial 的 paid box 最小值推出全局正数。

R516 第8节的有限终止需要完整像球半径、两向全域成员网/误差、开方误差和变换直径等真实收紧。当前固定 C 盒与有限见证计划不自动满足它。源码不声称固定 max_depth、预算、90K 或某个 $\gamma$ 一定成功，也没有性能承诺。

## 517.7 临时输出、必要读回与失败路径

out 必须是实际 RUNNER_TEMP 内新的专属目录，且不能包住原输入、源码或当前模块。其父目录由实际调用者准备。所有原 R425 文件只读并保留；代码不创建 artifact、Release、Git 数据或编码回传原大账。

实际新输出：

| 文件 | 范围 |
|---|---|
| actual-input-scope.json | 实际原目录/result SHA、完整明确帽参数计划、工作参数与 clock 记录 |
| complete-image-binding.json | 只有真正完成输入绑定后生成；完整来源、原对象身份、全账 stored/decoded 身份和全球数量 |
| large-arrays/all-actual-member-balls.json | 两向全部实际成员球及来源，仅同 job 临时 |
| large-arrays/complete-transform-decisions.jsonl.gz | 所有实际 paid/split/depth-stop 记录；闭 children/原 bound 全保，stored 与 decoded 分别绑定 |
| result.json | 完整原状态、错误、资源、实际字段/群前沿/未访范围及所有成员身份 |
| necessary-summary.json | 仅在整份必要正文不超过 90000 B 时形成 |
| necessary-over-budget.json | 必要正文超限时的单份诚实 fallback |

必要 frame 为：

~~~text
BEGIN_R517_FULL_E3_NECESSARY
<one complete bounded JSON object>
END_R517_FULL_E3_NECESSARY
~~~

完整必要正文保全部 transform frontier、root suffix、当前 witness/target cursor、当前完整盒下界、原输入未决、实际 error/resource_stop、原 clock 和全部 raw 身份。已付成功大表、完整球表和 decision 账仅给真实身份；不宣称这些正文已被 connector 逐行读回。不会把账分成若干“元数据”包运输。

函数返回：

| exit_code | 语义 |
|---:|---|
| 0 | 原完整输入与实际请求的八根变换覆盖全部返回，必要正文完整 |
| 1 | 输入或执行异常，必要正文仍在范围内完整返回 |
| 2 | 原资源/深度/工作停止，完整未付范围返回 |
| 70 | 必要正文超 90000 B；仅回 fallback，complete_necessary_readback=false，完整原 result/raw 留存 |

每个返回带 actual original_result、necessary 的字节身份以及 complete_necessary_readback。70 的 attempted_bytes/SHA 指该次完整必要内容，不能用 fallback 当它的科学结论。原 scientific result 不被覆盖或换成 fallback。

最外层 Actions 身份、API 参数、路径和创建目录等若在结果结构建立前异常，可能没有新 result.json；后继 caller 必须保真实 exit/异常和未启动范围，不能凭目录存在生成完成 marker。写磁盘、ledger.close 或最终结果写出本身失败也不能被假定仍有完整输出。

本 API 不写 readback-complete/cleanup marker，不观察 owned-process quiescence，也不删除任何 raw。即使返回 0 或 complete_necessary_readback=true，调用者仍须按其原实际 owner 观察和总 workflow 条件处理清理；不能将该布尔当成 quiescent=true。原字段 actual_owned_process_quiescence_observed 固定为 false，明确该层未付。

## 517.8 调用接点与尚待付的最小下一步

后继真实 Actions 调用者可在原完整 R425 位置结果保留期间，显式做：

~~~python
answer = module.produce(
    computations=actual_computations,
    directory=actual_R425_output_directory,
    result_sha256=actual_R425_result_receipt["sha256"],
    out=fresh_owned_quotient_directory,
    cap_points=actual_recipe_cap_parameters,
    desired_gamma=actual_recipe_gamma,
    sqrt_bits=actual_recipe_sqrt_bits,
    max_boxes=actual_recipe_max_boxes,
    max_distance_evaluations=actual_recipe_max_distances,
    max_cover_balls=actual_recipe_max_cover_balls,
    max_depth=actual_recipe_max_depth,
    check_budget=original_absolute_clock_check,
    caller_clock_identity=actual_bound_original_clock_receipt,
)
~~~

此示例只有实际参数槽，不给一份尚未发生的 recipe、场、数字证书或 run。当前新 API 并未被上述任何运行入口调用。

要真正整链调用，后继只需补明确 owner/source 注册、原绝对钟/输入 receipt 绑定、原 whole quiet/必要读取与清理接点；使用 generated views 时还须登记对应实际完整 producer/帽 tuple。不能为省来源工作把 c87b/0ff1 改成旧 schema 通配符，也不能复制原局部球冒全新 M 场。

数学正下界与原已刊 R238 定性正性是两条可选支付途径。R517 没有取消 R238，也没有把定量全群搜索强加为原非平凡性的唯一完成门。原 R20 的帽幅度上界继续约束该相位构造；大的 held 值不会被转换成未经证明的商距离。

## 517.9 来源定位、文稿修订与可复核范围

本文直接依赖：

- [R516](R516-finite-full-E3-cover-and-quantitative-quotient-distance.md) §§2–8 的完整球/成员/群覆盖定理及条件终止，§9 的当前 R425 与帽见证范围；
- [R425](R425-current-C-whole-image-held-and-reflection-rigidity-inputs.md) 与其[完整接口](../notes/2026-11-15-current-C-whole-image-held-and-rigidity-interface.md)，实际 produce、PositionCover.report、witness_points、position ledger 写入与读回来源；
- 原 [R417 帽源](../computations/geometry_20261115_current_C_ten450_fixed_cap_balls.py) 的 bind_loaded_shared_bundle、CurrentTenFixedCaps.describe/cell 及完整 marker/side/cuff/H 定义；
- 原 [R413 cuff/target 源](../computations/geometry_20261115_current_C_original_cuff_target_atlas.py) 的同场 attachment，仍由原 R425 和 R417 完整绑定。

源码首交 38559 B /23a4d608 为本次封口前草稿，未当作最终身份；最终 39936 B /0c69c61c 只新增原未完成 position 的实际 completion/count/pending/error 观察及帽参数/后缀游标，避免早停时只有原件身份而没有必要未决地址。该 3407 B 完整文本差异的 SHA-256 为 5f6181a8430b14b1a0bf4897fa4feefbad020c7b4bbbf665373a6fca1fc2ac4c；算法、资源值和数学条件没有变化。差异与交接 manifest 为临时交接件，不是新的科学输出。

本次进行了源码文本与实际字段的组成工作，未执行任何科学路径，也没有用本地 fixture、AST、compile 或另外试跑替代原 Actions。未返的 actual450、整个位置球覆盖、实际帽参数、具体 $\gamma$、全变换覆盖与原全域几何条件都仍明确未付。已完成的 R516 定理和本执行接口可直接登记，后继工作按原 open 继续。
