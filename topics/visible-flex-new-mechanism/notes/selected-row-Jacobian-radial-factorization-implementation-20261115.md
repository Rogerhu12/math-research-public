# 原 159 维几何的选定行 Jacobian 径向因子化：实现与首次公开执行协议

作者责任：本稿与四个新源由本课题工作代理编写；根代理负责完整源码审读、公开 Git 提交及 GitHub Actions 调度。本稿是新实现的来源与执行规格，不是尚未运行的通过回执。

## 1. 本次唯一改变

本次把已发表的[径向因子化设计](selected-row-Jacobian-radial-factorization-design-20261115.md)落实为新的选定行 Jacobian 评价器。完整普通几何值、原固定度量与高度基准、真实原行号、物理约束、两网验收、线性规划目标、SOC 校正和成功 SOC 持径规则继续调用既有实现。

入口仍在原物理 163 维族中使用同一 159 个独立坐标：

- $u$ 的 $9\times9=81$ 列；
- 原 $v$ 的 $9\times8=72$ 列；
- 第 $153$ 号独立切向 $Q$ 列；
- 五个准确有理零积分高度坐标。

新方法没有增加几何自由度。它先对每个角模式求三个径向 jet 虚方向上的标量行微分，再恢复该模式的九个径向列。生产路径不再生成全 163 列的向量几何 Jacobian，也不先生成全 159 列的向量几何 Jacobian。最终被 LP 使用的选定标量矩阵仍是原行号顺序、159 列。

浮点加法次序改变，因而不能承诺历史 LP 解、选行、步长或终点逐位相同。能比较的是同一数学模型、真实门、预算与新旧评价定义，以及本次实际日志报告的成本和进展。

## 2. 已有来源与当前已公开观察

实现只使用公开源和已经完成的容量/持径流程。原成功执行为：

- source：a934b45c33f7f4807a307b6a556bf32b76db675d；
- run：43712266529；
- geometry job：132806237214；
- 人读记录：[首次容量与成功 SOC 持径实际](height159-capacity-and-successful-SOC-hold-first-actual-20261115.md)。

该次首次实际最终持住的半径尚未被后继模型使用；不能据此声称收敛改进。新入口也不把那次终点哈希设成必须重现的目标。因规则 15 不保存重算报告，本次需要按冻结实现与完整参数恢复输入一次，再从本次真实合格终点继续。

该次 fine 选定 Jacobian 费用较高是实现动机。本次不重新执行旧比较实验，不把恢复输入的进展算成新因子化的进展，也不增加原阶段的 LP、完整值或活跃时间限额。

## 3. 四份新源及执行边界

| 文件 | 作用 |
|---|---|
| frame_selected_row_radial_jacobian.py | 完整角模式、三个径向 jet、选定行收缩、原列展开、普通值绑定 |
| frame_metric_height159_factorized_rows.py | 原成功 SOC 目标函数的子类，只换 coarse/fine 选定 Jacobian 入口 |
| frame_selected_row_radial_jacobian_development.py | 新小几何、原 API、全 11 组行、当前高度与缓存检查 |
| frame_metric_height159_factorized_rows_audit.py | 七次必要输入恢复、准确新 handoff、唯一新阶段、原双网终检与输出 |

本稿冻结时，各源只进行了源码编写和静态审读；尚未在本地执行、导入或声称通过新人工/科学检查。首次执行全部在本仓库公开 Actions。

### 3.1 冻结源

| 文件 | 字节 | SHA256 |
|---|---:|---|
| frame_selected_row_radial_jacobian.py | 27752 | e487cdfe3e508e572850217230ebd406736d360fd7e9d8e33b60ad50ba3e2632 |
| frame_metric_height159_factorized_rows.py | 13777 | b6c9fff497c0f22c5a12546c47349cc0274ed493f895547fc5c65cf99ba3d403 |
| frame_selected_row_radial_jacobian_development.py | 19243 | 46aeefbbd7549150d8d03018b0038ec4389a7392a9efc2d7f25299c7575c8d39 |
| frame_metric_height159_factorized_rows_audit.py | 72407 | a4298bcb5191c7baa850e5568354060555ff13d037308425121d912f50067eed |

最后一份 driver 如因根审发现具体接口问题而修订，应更新本表、请求中的对应 SHA 与新 diff；不能将本版本未经执行的状态写成通过。

## 4. 单角模式与三个径向 jet

固定当前真实切向场与当前物理 $a(s)$。对一个角模式 $Y(\theta)$，令 $T_q$ 表示原 $q=u$ 或 $v$ 坐标对单位切向场的导数。记

$$
F_j=\partial_s^j(T_qY),\quad j=0,1,2,
\qquad
F_\theta=\partial_\theta(T_qY),\qquad P_j=\Pi_NF_j.
$$

先在完整原角网格上计算 $F_j,F_\theta,P_j$，再选原网格点。不能先取角子集后再积分。$\Pi_N$ 是原 periodic_operator；不把离散 $\partial_\theta\Pi_N$ 偷换为恒等。

对径向系数 $R(s)$，各真实位置 jet 的变分为

$$
\begin{aligned}
\delta X&=R\,aP_0,\\
\delta X_s&=R(a'P_0+aP_1)+R'aP_0,\\
\delta X_{ss}&=R(a''P_0+2a'P_1+aP_2)
 +R'(2a'P_0+2aP_1)+R''aP_0,\\
\delta X_\theta&=RaF_0,\\
\delta X_{s\theta}&=R(a'F_0+aF_1)+R'aF_0,\\
\delta X_{\theta\theta}&=RaF_\theta .
\end{aligned}
$$

原代码直接定义的 $X_\theta,X_{s\theta},X_{\theta\theta}$ 沿用原式；本实现不从某个去零模积分反推这些式子。

每个原标量约束在同一个真实普通几何点对这些 jet 线性化。调用原 selected_spectral_parameter_jacobian 得到三组标量系数 $L_0,L_1,L_2$，然后按原 radial-major/angular-minor 顺序恢复

$$
J_{i,m}(s,\theta)=L_{0,m}R_i+L_{1,m}R_i'+L_{2,m}R_i''.
$$

当前实现依次处理 $u$ 的 9 角模式、$v$ 的 8 角模式和单独 $Q$ 模式。最大的虚参数轴为 $3\times9=27$。不把 154 个切向列同时存入六个向量位置 jet。

## 5. 高度与原普通几何身份

原独立坐标为 159；旧 SingleQ 标量场读取器的物理坐标必须仍是 163。新 helper 从当前 159 坐标调用 reference_evaluation_state：

- 当前 154 个切向坐标全部保留；
- 原九个高度槽使用被冻结的准确高度参考；
- 当前五个零积分高度的真实贡献由原 height_jets 和本次已经绑定的普通几何缓存保留。

这不是把当前高度归零。选定标量行的普通系数来自当前真实 coarse/fine 值；新 helper 独立核当前 $b,b_s,b_{ss}$ 与真实缓存一致。五个高度导数仍分别为 $Z,D,D'$，只进入 $X,X_s,X_{ss}$，其余位置 jet 的该变分准确为零。

原 coarse physical_geometry 会裁剪底层 FiveHeightField 元数据，只留下 state/radial/theta 和几何字段。因此仅在显式 owner=coarse-current-cache、该缓存确实含当前 state 的分支，允许缺少 coordinate_definition_sha256，并通过拥有它的固定 Field/当前状态/完整网格绑定代替。fine 缓存和独立 helper 检查仍要求原完整坐标身份。不能为所有缺失字段开放宽松回退。

每批保留完整原角网格，并补径向全局两端用于原 primitive/center 约定；实际选行仍使用原 ID。重建的普通位置六 jet 与 $T$ 逐项和当前缓存比较。中心基准来自当前已绑定原普通缓存；不假装另作了独立 center 求积。

## 6. 原目标函数与缓存

FactorizedHeight159Objective 继承 SOCHold159Objective。生产只覆盖 constraint_jac 和 fine_derivatives。普通 evaluate、fine_decision、linear_rows、acceptance、行池增长、SOC LP 和持径控制均继承原方法。

每个选定矩阵缓存除父类的 state/pool_version 外，还绑定：

- 当前状态的完整 binary64 字节；
- 全部原行 ID 及其顺序；
- 完整径向/角网格哈希；
- 新评价定义和因子化定义哈希；
- coarse/fine 所属缓存。

父类 accepted_cache 回退仍搬运同一 state/pool_version 缓存。新类额外验证所有标记；不同状态、角网格、行顺序或评价定义均不得复用。

原 constraint_jac 的固定辅助 $\zeta$ 列沿用原 PSD 行公式。物理 LP 仍使用前 159 列；$\zeta$ 仍是原固定值，没有成为新的自由变量。

旧 active_derivatives 返回的是完整几何导数字典，不能把新选定矩阵冒充它。新类对该旧接口明确拒绝。当前冻结生产 loop 经 linear_rows 调用 constraint_jac/fine_derivatives，不调用这一旧完整缓存接口。

## 7. 必要输入恢复与第七阶段真实接续

新 driver 原样承接现有请求的 24 份输入及 decoded SHA。七个必要阶段各调用一次：

1. frozen growth；
2. frozen strip reserve；
3. frozen SOC scaling；
4. frozen body103；
5. frozen tail154；
6. 同完整已声明容量的 height159 producer；
7. 同完整已声明容量的 successful-SOC hold。

第六、第七阶段仍按已发表容量实现各作其原本一次的声明。这是恢复已有完整算法输入，不是在新因子化阶段增加容量。新第八阶段不再调用 reserve_initialization。

driver 显式保存第七阶段使用的 prepared_hold，而不是从结束报告里的浮点系数重建 Field/H。handoff 检查原报告来源、配置、24 输入绑定、本 job/run/source、真实独立 159 与依赖物理 163 准确坐标、固定 $g,b_0$、参考九高度与 $H$、原耦合盒、最后真实接受点、全部原行池和完整终检。

容量正文回执含 executed_configuration_sha256，而配置中的 history 保存原 record。handoff 先逐条去掉这一额外正文键后精确比较历史，再独立核当前回执的 executed_configuration_sha256 和 new_fine_capacity；不能因为两种真实结构有一键差异而误拒成功输入。

### 7.1 保留真正 SOC 持径

第七阶段 controller 由 inherited159_controller_without_reset 起逐模型回放。每条完成更新使用冻结 next_soc_hold_trust 和其真实 trust_after_original_controller，核完整返回字典。

不能用较早 next_mapped_trust 代替。那样会把已付成功 SOC 的持径重新减半。本次新 handoff 保存实际终末半径、成功计数、所有真正持径的模型号，以及最后未完成反馈的标记。未完成末模型不冒充一次成功，也不重置到某个更方便的半径。

新阶段明确调用 run_soc_hold_recovery。原阶段若已低于原最小半径、行池实际超限或其他真实门失败，按原条件如实退出；没有隐藏重试或扩容。

## 8. 唯一新阶段、预算与实际输出

成功 handoff 后实例化新目标函数，原各项配置的数值不变：

| 项目 | 原值或规则 |
|---|---|
| LP 调用 | 12，primary 与 SOC 共用 |
| 完整值调用 | 40，共用原初始化与真实试步 |
| 优化活跃时间 | 120 秒 |
| 单 LP 时间 | 10 秒 |
| 独立终检 | 原 coarse/fine 各一次 |
| metric target | $13/50$ |
| 既有合格预算 | $167/625$ |
| 硬曲率门 | $58$ |
| 实际最低接受改进 | $1/10000000$ |
| 边界/镜像/物理盒等门 | 原 cfg，逐字继承 |
| 原行池容量与既有 ID | 第七阶段真实最终值；本阶段不追加声明 |

这不是简单增加旧优化循环的次数。新增工作是一个数学等价但浮点评价顺序不同的 Jacobian 路径；效果只能从其首次公开实际判断。

输出把新 coarse/fine 的 scalar fields、ordinary replay、角 kernel、选定标量收缩、null-height 和总费用分开；报告最大虚参数轴、批数、实际存储字节和 replay 差。旧粗全几何批计数仍保旧范围，不能把新三虚方向批次冒称旧 163 列批次。峰值 RSS 是整个进程，包括必要恢复，不冒新 helper 的独立 RSS。

保留原全部模型、试步、实际门、SOC 总位移与校正位移、持径理由、行池变化、最后准确坐标和失败异常。main 临时完整报告不发布；stdout 继续原详细人读数值并追加新因子化摘要。不能仅据 workflow success 宣称新目标达到或效率改善。

## 9. 仅新人工与 API 检查

入口 --check-factorization-only 聚合三组新增检查。它不调用任何旧 developer_check。

### 9.1 新小几何与原 API

正负 port 两侧、完整 8/16 角网格、非零 $Q$ 与非零五 null-height，比较原数学方法与新选定矩阵：

- 全 11 个原行组；
- 含真实端口与活动区间边界的径向点；
- 非排序与重复的原行 ID；
- 三类切向块及五高度块；
- 原全 163 列经准确映射的人工比较值；
- 当前场方向导数与小人工有限差分；
- 原辅助列；
- 只需一阶的位置分支；
- 错 state/坐标/角网格/bool ID 的准确拒绝。

原全 163 列只在这些新小人工的比较分支使用。人工通过时也不能宣称任何研究曲面可行。

### 9.2 真实父类缓存协议

使用真实父目标函数和相同小人工 Field。核相同行值、组序、容差、选定 J 和辅助列。缓存专门演练相同状态复用、池版本变化、真实父类 accepted_cache 回退。

人工直接布置的 cache container 仅用于回退协议，不调用 accepted_point，也不声称该小点满足实际几何约束。生产没有该人工布置。

### 9.3 新接续与 IO

复用已有 labelled-array fixture builder 的准确形状，新增对第七接续的检查：

- 同 runtime Field/H、独立/物理坐标和全部池保持；
- 所有容量历史与预算不变；
- 完整成功 SOC 持径回放，拒绝误换旧减半控制；
- 物理 163 坐标、参考、旧行或控制半径被篡改时拒绝；
- 最后未完成反馈保原状态；
- 七次字典 stub 恰各一次，成功才调用新入口；
- 原第七阶段错误在临时文件清理前完整打印并保留；缺失或 None 的 selected point 只报告未知哈希，不遮住该原错误；
- 成功/失败后临时输入报告清理。

stub 不是七次研究计算。只有之后 research 模式才调用真实七次必要恢复，并且新开发流程不会先运行那些科学前缀。

## 10. Actions 接线与准确参数

建议 lane：

    metric_height159_factorized_rows

driver：

    scripts/frame_metric_height159_factorized_rows_audit.py

开发参数：

    --check-factorization-only
    --out @OUT@/metric-height159-factorized-rows-development.json

实际参数严格复制 a934b45c 的 computations/request-continuation.json 中 jobs.metric_height159_capacity_soc_hold.research 共 98 项；唯一替换为：

    --out @OUT@/metric-height159-factorized-rows-audit.json

独立交给根代理的 request fragment 已逐字保留全部 24 个路径、预期 SHA 与 24 个稀疏目录；不另加预算参数。

| 接口 | 准确值 |
|---|---|
| 主 schema | same159-selected-row-radial-factorization-after-seven-restorations-v1 |
| 主 stage | metric_height159_factorized_rows_stage |
| 完成 status | complete-two-grid-height159-factorized-selected-J-audit |
| 原生 summary | metric-height159-factorized-rows-audit-summary.json |
| 开发 schema | 主 schema + -development |
| 开发通过 | passed=true 且 development.all_passed=true |

request fragment 明确列 42 个科学源码 SHA：原几何请求的 34 个源码、新 helper 直接依赖而原请求未列的 4 个底层源码、4 个新源。workflow/publisher/print 的最终 SHA 由根代理在唯一接线后加入，不能在此沿用修改前的旧 SHA。各旧 driver 的 implementation_hashes 递归来源绑定继续原样存在，未被这份显式请求表替代。

编排工具必须接受 audit 后缀，避免旧 print_research_outcomes 的 glob 漏掉新真实结果。首次开发失败就停该 lane 的 science，保存真实错误元数据；不自动运行旧 suite 或换输入。

## 11. 文件/权限/结果范围

全部新源只是小 UTF-8 文件，终端不可用时依据根规则 8 保存未挂 blob；根代理独占 tree/commit/ref 和公开调度。没有 PAT 被传入 native 工具参数。

没有新 recomputable payload 保存到仓库、Release 或 artifact。七次输入恢复和新完整报告仅在 runner 临时目录，stdout 保必要人读结论与源/参数/run/SHA。已有旧输入按原规则消费，不重新发布。

本次没有声称：新几何已经优化；目标已经达到；持径改善已经实际发生；连续曲率/全局 reach 已获证明；或新的 J 重排产生逐位相同的历史轨迹。首次实际到达后按其真实结果继续主目标。
