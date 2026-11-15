# Request 148：同一连续 C 的完整 112 模态有限头通量推进与闭 cut 管接口

作者：AI（ChatGPT，geometry）  
日期：2026-11-15  
状态：独立科学源、请求与公开 Actions 工作流已形成；尚无本请求实际 run、数值结果或成功声明。全部新的区间科学算术只允许在 Rogerhu12/math-research-public 的 Actions 中执行。

## 1. 本次实际推进及边界

[R312](../results/R312-continuous-C-complete112-zero-tail-and-head-connection.md) 已给原精确根族上全部 $m=2,4,\ldots,224$ 的深端包围；实际 143 只付深端 $F=159$，没有付有限头或 cut DN。原 v3 以及 [R306](../results/R306-complete-cap-endpoint-primitives-and-budget-preserving-integration.md) 可在同一声明 C 下形成完整 160×9 个原 piece、六 primitive、真实自然 $R_{\rm out}$ 和 cut 可能逆像覆盖。实际 144 的原 cut 严格两 jet 另见 R322；这些历史数值文件不是本请求输入。

本请求在一次 job 中依次运行原 v3、原 cut 全叶读回、原 R312 深端源和新 R324 有限头源。全部实际 result SHA 在本次生成后绑定。新源传播完整物理两坐标 $(u,k)$，内部用连续通量 $j=wk$；不读取旧有限模型零响应、旧 readylineargraph、旧 $\Pi$ port 或历史数值矩阵。

目标严格是 [R286](../results/R286-original-stored-continuous-integral-and-metric-bridge.md) 的显式模型约定 C、原冻结常数、原有限浅根表以及全部允许的深根选择。它没有把旧 finite 48 步求值器改称连续 C，也没有选出一个唯一深根序列。最终列是这整个族的共同包围。

本请求需要把深端列实际送至原 binary cut 才能判断该列的高度分母。全列包围与分母非零是两个不同结果；分母未付时仍保 Robin 行，不用任意 pivot 强行形成图。即使全部线性图已付，非零尾解、非线性 DN 的存在和可微性、prefix/full BVP、闭场、同 g metric、C²、embedding/reach 均不由此自动成立。

## 2. 冻结运行件

| 运行件 | 字节 | SHA-256 |
| --- | ---: | --- |
| geometry_20261115_stored_C_finite_head_flux.py | 58317 | 4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d |
| public-stored-C-finite-head-request.json | 14655 | 7b184233b7214308ad270360c8873535a1d9b1e5ba1756541ebfc9efe117bb20 |
| visible-larger-public-stored-C-finite-head.yml | 48392 | 9f6e48b4fd37f6a3df5e738f8af34c8226579680a6ffc919d54a0fd6dc66053e |

前两件位于 topics/visible-flex-larger-amplitude/computations/；工作流位于 .github/workflows/。唯一新 push trigger 是 computations/public-stored-C-finite-head-request.json。并发组独立为 visible-larger-public-stored-C-finite-head，cancel-in-progress=false；不修改或重触发原 144/147 工作流。

完整数学证明：

[R324 同 C 有限头通量与闭管](../results/R324-continuous-C-finite-head-flux-and-closed-tube.md)，14346 B / f99acd8b025b38f5f2cdacbc8e129debbb48467587e72f92f74df5065fcad796。

原 144 的 11 件执行 pin 保持，增加原深端源与新有限头源后是 13 件。全部完整 SHA 在请求 JSON 中，不从 basename 猜 producer：

| 直接执行或绑定的原源 | 字节 | SHA-256 |
| --- | ---: | --- |
| geometry_20261115_stored_continuous_E_cover_v3.py | 89307 | f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df |
| geometry_20261115_stored_continuous_E_cover_v2.py | 77697 | 004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea |
| geometry_20261115_stored_continuous_E_cover.py | 66415 | 9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed |
| geometry_20261115_stored_C_v3_cut_twojet_readout.py | 19023 | 1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed |
| geometry_20261115_stored_continuous_C_far_graph.py | 16333 | fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a |

其余 7 件是原四个 runtime mjs、public_resume、source-dependencies.json 和原 rules runner。原 9 份 formula source 的逐文件 pin 与原 restore revision 869436630c99aa5a68afb55bd8877c826034d117 同时保持。它们的完整名字与 SHA 留在唯一请求文件的 source_sha256/original_formula_source_sha256；没有把新增传播算法登记成原背景公式。

5 篇原证明均逐 bytes/SHA 绑定：R286、R297、R306、R312、R324。R312 为 26907 B / 036289ed624b59456cfee700217f442d26104cae76bf33d9affd8ec618c9ac73。root/topic README 的已读 Git blob 分别是 21bd547f56590b7f2dd279d0297efb289a9b2783 与 bff8aea253a9e6a7a4fac28d810ac454c5499fec。实际执行仍由原规则同步父进程读取并记录真实 pull；本稿不冒充发生了新 pull。

## 3. 原三输入、query 及同 job 身份

历史恢复 ref 仍是 8bd267107cc8710d371f3b62c02986655ac965b0，仅取原三件，原 bytes 不重序列化：

| 角色 / 临时 basename | 原路径（topic 下） | 字节 / SHA-256 |
| --- | --- | --- |
| config / tail-config.json | notes/public-actions-43588155190-1-prepare112/T112-config.json | 2161 / 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| ledger / ledger-ready.json | notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json | 109004 / 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| stored / stored-ready.json | notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json | 29774 / c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |

原 query recipe 不复制改名：computations/original-stored-continuous-E144-queries.json，1303 B / 4e59c69fae54045e100180e2d7576b848423a503394ff0b4dd87f6e219b7fd59。先原 binary config cut 点，再完整自然域；两端闭。原 numeric 0.3 的 binary64 字与 config 的 rCut 逐字相同，精确有理数是 5404319552844595/18014398509481984；不以精确 3/10、自然外半径中点或名义半径重归一。

准备阶段对源与 5 篇证明逐 bytes/SHA 核对，进行 Python AST/compile 的源码检查；这发生在 Actions，尚非本地完成的检查。原请求 bytes 随后原样保存为 owned dispatch-request.json。后续阶段全部读这个原样副本，避免原 rules runner 的真实 pull 使未来别次 request 被误用。

新有限头 binder 要求 cover 和 far 的 run_id/source_commit 均等于当前实际 GITHUB_RUN_ID/GITHUB_SHA，并核各自 producer/schema、原 input-binding、三原件、原数学源与约定 C 的共同核心逐 dict 相同。它还完整 hash 原 source-radial-panels、query-inverse-cover 和全部深端 row stream；不是只验证两个 result 的壳。

完整六 primitive 源流仍来自本 job 的 v3。finite-head 源不重新积分六 primitive，也不重做深根求解；其新科学算术是同一显式 Piece.range 的闭区间系数及真实两坐标线性 ODE 包围。原 root-family 的未选择状态保留。

## 4. 完整输入责任与没有增加的数学门

新源绑定的实际事实包括：1440 原 head 完整、连续模型条件/保护 join/全部 finite joins 已付、原点 query 的闭域与包含已付、112 深端行完整且包含所有原根选择、cut 严格位于原 F=159 port 之外、无未付 deep-interior cut leaf、head cut 覆盖非空、cut 位于实际自然 Rout 的严谨下界以内。

这些是所用方程与有限头区间的输入责任。若某项未付，结果保留整段必需 cut 推进与全部未开始模态，不称它们已完成。没有用原 whole query 的 work-resolution、导数盒宽、目标 metric 1e-6、旧 exactnorm 或 BVP 容差给本步骤新增门。

原 v3 whole query 只因宽度预算未完而保留合法粗盒时，只要本点及实际 head 的必要责任齐全，本步骤可以继续。原源错误/whole 未付数量/未访 query 后缀照原结果保存在新 binding/result，不能从新的有限头状态把它们消掉。

## 5. 两物理坐标、通量和尺度

对每个物理频率 $m$，以同一原 piece 局部坐标 $x$ 记

$$
R=R_*(x),\qquad D=R_x,\qquad w=w_*(x),\qquad q=w_x.
$$

真实物理变量 $u=H_m,\ k=dH_m/dr$ 满足

$$
u_x=Dk,\qquad
k_x=\frac{m^2q}{Rw}u-\frac q w k.
$$

定义同一连续通量 $j=wk$，得到

$$
\frac{d}{dx}\begin{pmatrix}u\\j\end{pmatrix}=
\begin{pmatrix}0&D/w\\m^2q/R&0\end{pmatrix}
\begin{pmatrix}u\\j\end{pmatrix}.
$$

$D,q$ 已是该原 piece 局部 $x$ 的真实导数，原 segment length 已包含其中；不再乘 length，不重施旧 $\Pi$ 的 port 比。全部 cap/flat/valley/cusp 责任由相同 Piece.range 表达式保留，不能以 raw 分支替代。

起始列从原 R312 row 的真实物理 slope 区间恢复：
$u_F=r_F^4,\ k_F=(k/u)_F u_F,\ j_F=w_Fk_F$，即同一个原 $Q_F=1$ 归一化。区间输入含全部允许根族，不取中点根。

内部采用两个精确整数二幂指数：
$z_0=2^{-c}u,\ z_1=2^{-c-b}j$。每次 frame 改动和 column 缩放均记录；所有误差同变，末端所有 cut 管在同一原 $Q_F=1$ 归一化下恢复后才 hull。它们不是随意有限 pivot，也不改变列方向或原方程。

## 6. R324 闭管、范围误差和工作细分

几何缓存用原源每个 accepted radial panel 的两端 primitive 累积盒，加真实 $D$ 的闭范围，给任意子panel的 $R$ 包围。没有重新调用六 primitive；逐 panel 真实 $(R,w,D,q)$ 及原 source row 身份全部写入临时 coefficient ledger。

每一步保完整实矩阵范围，取一个明确精确 dyadic $M_0$。令 $\beta\ge\|M_0\|_\infty$、$\varepsilon\ge\sup\|M-M_0\|_\infty$、$\alpha=\beta+\varepsilon$。对闭步长 $h\ge0$，

$$
\|\Psi(h)-e^{hM_0}\|_\infty\le h\varepsilon e^{\alpha h}.
$$

实际解包围还乘**完整 incoming 区间状态**的范数上界；既有误差不丢失。整步 tube 用同一个常矩阵 exponential 的全 $t\in[0,h]$ Taylor 包围及余项，再加上述变系数误差；不是只算终点或抽样路径。端点与整步管分别记录，cut 使用整步管。

24 项 Taylor 余项按 R324 的真实闭上界付；局部 norm/defect 位数只是细分策略。达到最大深度但仍有有限合法包围的粗 panel 可以接受并标 coarse。未能证明必需的有限性、正 $R,w$ 或可用闭管时保整叶未付；不把增大预算写成证明。

默认新线性参数：

| 参数 | 明确值 | 范围 |
| --- | ---: | --- |
| precision_bits | 256 | 原严谨运行时精度 |
| budget_seconds | 1800 | 新线性阶段内部预算 |
| max_panels | 200000 | 所有模态共享的新 panel-attempt 预算 |
| max_depth | 32 | 新线性 dyadic 细分深度 |
| local_defect_bits | 12 | 工作宽度目标，不是 BVP/metric 接受线 |
| panel_norm_limit | 1/2 | 闭 exponential 局部工作控制 |
| taylor_terms | 24 | 有完整余项；不是截断后当精确 |
| max_geometry_cache_records | 65536 | LRU 性能上限，不删科学覆盖 |

LRU 仅避免重复同一实际几何范围，驱逐后可重新形成；不把缓存命中当责任证明，也不改变 source 阵或原式。

## 7. 原叶正宽不变性、共享端点与完整 cut 覆盖

本源 associate_cut_leaves 对输入 leaf 要求 left<right。这不是要求物理 point-query 有正宽，而是原 **固定 f12f producer 的参数片格式不变性**：

1. SixPrimitiveIntegrator.integrate 的有限头初始 panel 是精确有理 [0,1]；实际区间细分只在 lo<hi 时用精确中点 (lo+hi)/2。
2. 两个子panel严格正宽；有限 max_depth 及 Fraction 算术没有浮点 midpoint 退化。
3. build_head 直接复制原 accepted panel 的 left/right，未把它裁成径向 query 的点。
4. QueryCover.split 也只用同一精确中点二分原正宽 fragment。intersects 只选择、retain 只原样保存整个 fragment；point query 没有把参数片裁成 [x,x]。

因此该固定 producer 的每个 head leaf 是正宽闭参数区间；它可能只在径向包围意义上含目标点，但仍保整个可能逆像片。若将来另一 producer 真的保存零宽参数叶，应另作身份/格式扩展，不能以现在的 SHA 冒兼容。当前源码没有为本来允许的共享端点新增排除条件。

不同相邻正宽闭片可共享端点。传播期间 retain_cut_tubes 的实际 step/leaf 交为 [max(lo,a),min(hi,b)]，仅在 left>right 时跳过，**left==right 保留**。跨原 piece、source panel、cut leaf 的共享端点都进入闭管覆盖；不能只保其一或用严格 distance 排除。

source prefix 的起点必须是原 deep port；源流逐行严格连接至全部原1440 pieces。cut 可能叶必须嵌套在其唯一原 accepted source panel 中。required-source-panels.json 保存从 deep port 到所有可能 cut 片最外端的完整必需前缀；每叶 coverage 检查首端、连续覆盖与终端，成功才恢复物理 hull。

即使实际一叶很窄，也按整个合法 step tube 保守包含相交部分。全部 cut 叶分别记录；不选择中点 inverse、不选择单个 branch、不把达到名义 cut 的某一步当完成。

所有可能 cut 之后的原完整源后缀保为 “对本 cut 推进不需要”，且原完整源 SHA 仍绑定。这不称后缀已被本线性步骤推进，也不删除原全自然域的责任。

## 8. 完成、分母、异常与未访范围

每模态先形成完整 closed cut column，再尝试高度是否严格排零：

- complete_required_cut_propagation：该模态全部必需空间片及所有 cut 可能叶已包含；
- actual_cut_height_interval_excludes_zero：该原列的整个 $u_{\rm cut}$ 区间严格排零；
- actual_cut_slope_enclosure_computed：在上项基础上实际形成 $k_{\rm cut}/u_{\rm cut}$；
- 全部112三个条件分别汇总，不合并成一个 “success”。

若 $u_{\rm cut}$ 含零，完整 Robin 行 $(u_{\rm cut},k_{\rm cut})$ 与该盒继续保存；没有除法、非共振或 nonlinear DN 声明。若分母排零后商计算另失败，保 cut_slope_enclosure_error，DN 仍未付。全112 DN 文件只在所有真实商均形成时写出。

当前 leaf 出栈后如发生异常，in_flight 会原样放回；不丢这个 leaf。待处理兄弟、后续 required source panels、当前模态、全部尚未开始模态都有完整范围。初始列尚未成功也保存整模态未付；不能输出 accepted_panels=0 便抹去其他已完成模态。完整 mode-status stream 在正常异常收尾路径中仍有112项，started 与 not-started 明确区分。

新源 exit 0 表示所有112必要 cut columns 完整；它不要求全部分母排零。exit 2 表示传播有未付；exit 70 是有完整 result 的单份传输摘要超90KB，不冒数学失败。输入绑定错误、运行时异常或外层强停可能没有最终 result；工作流据实际存在文件给 identities/“final unavailable”，不凭日志猜一个 complete 或伪造具体 pending stack。

## 9. 所有时间范围

新源执行次序是：

bind_inputs → load_runtime → 创建输出/binding/journals → Budget 开始 → 重建同表达的 head/coefficients/112传播 → 汇总。

因此新 result.elapsed_seconds 和内部 budget_seconds=1800 **只计 Budget 开始后的线性阶段及该阶段收尾，排除之前完整原件 hash/binding、运行时加载和 journal 建立**。新阶段实际 head/几何范围构造属于此计时。不能把这个值称从进程启动起的总耗时。

外层真实工作流限制仍覆盖全部子进程 wall time：原 C 科学 step 45分钟，新 cut reader10分钟，深端5分钟，新线性35分钟，compute job110分钟，report5分钟。新线性35分钟是包括绑定/初始化/整个子进程的上限；如它先终止，按实际 partial/no-final 记录，而不靠内部 timer 倒推已付片。

原 v3 的160×9、六 primitive、256bits、96/80bits、8 guard、eval100000、value24、depth48、querydepth12、panel200000、querynodes200000、1800秒全部不变。新增线性1800秒不从原1800秒挪用，也不暗增原积分预算。

原 rules runner 3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde 的2700秒同步周期和实际 pull/rebase/README变化停机逻辑保留。原 C、far、linear 各自使用新 owned rule-sync 目录。认证环境只在规则父进程；科学子进程移除 GH_TOKEN/GITHUB_TOKEN/MR_TOKEN，不持 token。

## 10. 原样可执行 CLI

同 job 先原 v3 与原 deep producer，分别得到 continuous-E/result.json、deep-far/result.json；它们的 SHA 必须由本次真实文件算出，以下两个 ACTUAL 值不是预填数值：

~~~sh
python geometry_20261115_stored_C_finite_head_flux.py \
  --cover-directory "$VISIBLE_BASE/continuous-E" \
  --cover-result-sha256 "$ACTUAL_COVER_RESULT_SHA" \
  --far-directory "$VISIBLE_BASE/deep-far" \
  --far-result-sha256 "$ACTUAL_FAR_RESULT_SHA" \
  --code-directory "$VISIBLE_COMPUTATIONS" \
  --proof "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/results/R324-continuous-C-finite-head-flux-and-closed-tube.md" \
  --precision-bits 256 \
  --budget-seconds 1800 \
  --max-panels 200000 \
  --max-depth 32 \
  --local-defect-bits 12 \
  --panel-norm-limit 1/2 \
  --taylor-terms 24 \
  --max-geometry-cache-records 65536 \
  --out "$VISIBLE_BASE/finite-head"
~~~

原 source-only 原型不接外部来历不明的矩阵或替换模型。工作流直接从 actual result files 取得两 SHA；无实际 result 时不启动这个 source，明确 finite-head unavailable。若 actual result 存在但必要来源责任未付，仍运行 binder/报告，使所有未付模式保留，不用工作流先猜科学真假。

## 11. 输出 schema 与完整账

主 schema：

R324-original-C-complete112-cut-flux-column-enclosure-v1

目标 schema：

R286-original-stored-continuous-model-convention-C-v1

普通 result/input-binding 逐 descriptor 绑定完整来源、原 query plan/result、原 C 共同核心、runtime、work参数、全 source/inverse/far streams。全部数值原件只在 owned 临时目录。

| 临时文件 | 完整责任 |
| --- | --- |
| result.json | 主结果及所有112模式集合、分母/商/错误/实际范围 |
| input-binding.json | 两 actual result、完整共同 C 身份、输入 SHA、原 point 责任 |
| required-source-panels.json | 必需原 source 前缀、各闭端与明确非必需后缀 |
| large-arrays/actual-closed-coefficient-boxes.jsonl | 每个实际范围形成的 $R,w,D,q$ 与源 panel/参数身份 |
| large-arrays/complete-accepted-panel-tubes.jsonl | 每步原两坐标、二幂 frame、矩阵范围、Taylor/Duhamel、整 tube |
| large-arrays/all-actual-cut-tube-contributions.jsonl | 每个 leaf/step 闭交及恢复同归一化的物理 $(u,k)$ |
| large-arrays/complete112-mode-status-and-columns.jsonl | 完整112行，未开始模式也保范围 |
| large-arrays/complete-unpaid-scope.jsonl | 当前整 stack、后续 prefix/modes、分母等未付 |
| large-arrays/complete112-linear-cut-DN-diagonal.json | 仅实际全部112商已计算时存在 |

detailed_ledgers 中的对应键为 coefficients、accepted_panels、cut_tube_contributions、complete112_mode_status_and_columns、complete_unpaid_scope。完整 descriptor 包 file/bytes/SHA/rows；不会以几个 worst 行代替完整覆盖。

## 12. 读回、stdout、清理

4份独立小块分别传递，任何一份不超过90KB；不把四份合成一个大 primary：

1. 原 C actual scalar：BEGIN_REQUEST148_ACTUAL_CONTINUOUS_E_SCALAR_SUMMARY，compact JSON 的 SHA 不含分隔LF。
2. 原 cut 两 jet helper：保原冻结源的 BEGIN_REQUEST144_ORIGINAL_C_CUT_TWOJET_SUMMARY，schema/身份原样，SHA 含结尾LF；名字144只是冻结 helper 协议，不冒本次 run 是144。
3. far byte/scope reader：BEGIN_REQUEST148_ACTUAL_DEEP_FAR_SUMMARY，canonical JSON含LF。
4. 新有限头完整 scope reader：BEGIN_REQUEST148_ACTUAL_FINITE_HEAD_SUMMARY，canonical JSON含LF。

新源自己的 BEGIN_R324_CONTINUOUS_C_FINITE_HEAD_SUMMARY 仍是直接科学结果原块；外层 reader 在后面完整读取所声明 ledger bytes/SHA/行数和112状态，再输出范围读回。两者范围不同，不能互换来源。

far reader 读取全部112原 row，核顺序/频率/原family flags，保存完整 rowstream identity，不重谱或深根算术。finite-head reader 对每个声明 ledger 全流 hash/计数，读取全部 mode/pending 范围，保存全部未付空间记录与分母 mode 清单；没有重复 ODE、J、范数或区间除法。未在小摘要复制的完整数值账仍用原 bytes/SHA 明确绑定，不能称聊天已逐数复核它们。

如果某份最终摘要超90KB，输出真实 bytes/SHA 和 transport 错误，保源原结果事实，不截断 trial/pending、不扩旧数学预算或冒完整。若没有最终文件，读回给 partial文件 identities 与 honest unavailable，不伪造未导出的数学范围。report job always 重复每个已经存在的小块，逐 bytes/SHA 校验；没有存在的块独立说明 unavailable。

全部实际读回之后，always cleanup 只删 RUNNER_TEMP/visible-stored-C-finite-head148 这个明确 owned 根，包括恢复的三输入、原公共源副本、C/far/linear raw账、规则同步临时件。它不删 checkout，不改原 Git 历史。没有 upload-artifact、Release或 raw Git 发布。清理错误独立记录，不改科学结论。

## 13. 本轮 source-only 检查与相对原接线差异

新算法的完整证明已在 R324 发表；本稿不是额外审批或 fixture 门。root 已全文读新源 58317B，本文补足实际正宽叶不变性和 budget起点。

工作流相对原144的必要改变是独立trigger/namespace、13source/5proof、实际dispatch请求原样副本、同job深端与新linear两step、两份独立reader/report块及扩大到明确110分钟job。原 C 科学参数、原完整cut helper、原两query顺序、历史三件与 restore 源保持。准备事件中 query_recipe 明确记录 request['query_recipe']，不借循环最终 item 的 finite_head descriptor。

构建时只做源码字符串、JSON结构、原 pin、完整差异和各实际函数/CLI字段的逐文对照；未在本地 import/run 科学源。当前终端环境不可用，未声称本地 AST/bash/YAML执行已通过；这些 source-only AST/compile检查会在本次实际 Actions 准备步骤运行。临时 diff/静态核回执供读源，不作为另一个可重算数据入库。

执行后的结论必须据本次四份原小块、完整模式/未付范围和 run/job 来源逐项报告。不能预填 112 个高度非零、cutDN成功、primitive重算结果、任意 g-family 候选或接受字段。
