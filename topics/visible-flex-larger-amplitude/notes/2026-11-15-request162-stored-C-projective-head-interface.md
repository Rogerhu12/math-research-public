# Request162：同一原C完整112双图传播与逐候选cut商接口

维护：ChatGPT /root 与 /root/geometry（AI协作），2026-11-15。

本入口把已证明的[R347](../results/R347-continuous-C-two-chart-projective-normalization-and-cut-quotients.md)接到独立公开Actions实例。原156的C、三份原输入、1440片/六primitive/两闭query、原R312深端112、全部原根族和cut逆像均保留；新科学变化是有限头列的严格双坐标图表示，并明确扩大该步骤的工作资源。它不是把原156高度盒含零改成已隔零，也不从可逆性假定某个区间pivot必能除。

## 1. 动机、真实前驱与未预填范围

[R339实际156](../results/R339-actual156-complete-C-head-and-partial112-cut-transfer.md)的真实run为43724040548/source1ca4196b99b61428bc4ab216bbc713ba2e77023e：C3600秒内全1440及cut两jet返回；深端112完整。原R324已完成m=2,4,6,8四个到cut的列，但整个高度盒含零；m10在共享200000次面板尝试耗尽时停止，真实线性时间170.5882169209999秒。完整闭栈及m12…224后缀已记录，不能归因于1800秒墙钟。

原每个模态所需完整source panel数为14644；112个模态即使不细分也超过原共享200000次尝试。这是明确的完整范围与资源算术，不是新算法必然收窄或在某个时间内完成的预测。新25,000,000次面板上限处理工作范围；R347双图表示处理传播表示，两者责任分开。

原156的巨大临时结果已经清理。本次从真实原输入在同job重新构建C与深端，不以旧SHA假恢复已删数组。153/159各自继续自己的rFar/native/BVP责任，不等待162成为额外接受门。

此接口提交时没有actual162科学结果。新来源/参数仅明确可重现入口，实际run及已读结果另写HANDOFF和正式结论。

## 2. 独立文件与字节绑定

|文件|B|SHA-256|
|---|---:|---|
|computations/geometry_20261115_stored_C_finite_head_projective.py|77731|5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216|
|computations/root_20261115_projective_head_scalar_readout.py|19995|befe77fc70e67260b475073adfa749ebce6e727c956703c7cbc79afe8389e9c3|
|computations/root_20261115_current_C_native_scalar_readout.py（原只读helper）|29751|2f2386afab07e5acc9b6ec155f782cb1ba1c8df5a879607effd5985c151784ff|
|computations/public-stored-C-projective-head-request.json|20703|5b002d6fe786c29e96313129690d7510f9e3e572c1a8b43b88fad01e4de0be18|
|.github/workflows/visible-larger-public-stored-C-projective-head.yml|74330|c9e30f35238e30d307a6253dc1079b9d296bc83d404dcd6c85aa83becc50af08|
|results/R347-continuous-C-two-chart-projective-normalization-and-cut-quotients.md|15106|29f79e1fff0fb872f1ae4920ff4ecbe459ca8aeb84f8dea639dd4bbe42f577f0|

原156 request16157B/8ce21c4d006fe26eb53d4fcba87bf2b72c4f84856bd60be4d128ecb2599d6a92保留，独立新request schema为public-stored-C-projective-head-request-v1，request_number=162，lane=storedCprojectivehead。原13份源pin不改，增加科学driver、reader及其原helper，共16：

|完整computations文件名|SHA-256|
|---|---|
|geometry_20261115_stored_continuous_E_cover_v3.py|f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df|
|geometry_20261115_stored_continuous_E_cover_v2.py|004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea|
|geometry_20261115_stored_continuous_E_cover.py|9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed|
|tail_frozen_geometry.mjs|db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3|
|strong_frozen_calibration_factory.mjs|77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247|
|closure_bounded_point_cache.mjs|35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043|
|exact_20261114_closed_background.mjs|be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b|
|exact_20261114_public_resume.py|11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5|
|source-dependencies.json|7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941|
|root_20261114_current576_rules_runner.py|3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde|
|geometry_20261115_stored_C_v3_cut_twojet_readout.py|1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed|
|geometry_20261115_stored_continuous_C_far_graph.py|fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a|
|geometry_20261115_stored_C_finite_head_flux.py|4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d|
|geometry_20261115_stored_C_finite_head_projective.py|5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216|
|root_20261115_projective_head_scalar_readout.py|befe77fc70e67260b475073adfa749ebce6e727c956703c7cbc79afe8389e9c3|
|root_20261115_current_C_native_scalar_readout.py|2f2386afab07e5acc9b6ec155f782cb1ba1c8df5a879607effd5985c151784ff|

原R324源58317B/4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d以及[R324证明](../results/R324-continuous-C-finite-head-flux-and-closed-tube.md)14346B/f99acd8b025b38f5f2cdacbc8e129debbb48467587e72f92f74df5065fcad796继续明确绑定；新driver另绑定实际R347。原[R312证明](../results/R312-continuous-C-complete112-zero-tail-and-head-connection.md)26907B/036289ed624b59456cfee700217f442d26104cae76bf33d9affd8ec618c9ac73仍负责深端。源冻结不是把某一次数值执行声明为证明。

全部科学import、数值算术、实际源码解析及编译只在公开Rogerhu12/math-research-public的Actions中发生。本次本地工作只有源码/完整差异、证明和字节身份；未填写新的本地AST、模块运行或未来Actions通过记录。

## 3. 原C、深端与输入不变

三份原件只从公开历史commit8bd267107cc8710d371f3b62c02986655ac965b0临时恢复：

|作用|B|SHA-256|
|---|---:|---|
|原T112 config|2161|01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5|
|原校准ready ledger|109004|563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6|
|原stored reference|29774|c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d|

原query recipe1303B/4e59c69fae54045e100180e2d7576b848423a503394ff0b4dd87f6e219b7fd59，原formula各模块及revision、R286/R297/R306证明和原模型schema都由request完整保留。新的有限头方法没有另设root choice、把中点当准确C、换自然Rout或改原cut。

同一原f12f7470… C producer：precision256，绝对积分96bits/相对80bits，evaluation_limit100000，value_width24bits，max_depth48，query_depth12，max_panels200000，max_query_nodes200000，budget_seconds3600，analytic_guard_bits8。全160×9及六primitive不删；先原binary config-cut点query，再原whole natural-domain query，完整两侧和粗合法未付范围保。

独立cut两jet reader仍用同一完整原逆像叶，不能以数值代表替换。R312仍F159/物理node160、precision256、全部2,4,…,224；不复用旧零J。C与far result的本次实际bytes/SHA在运行时计算并绑定，任何缺件或source/run不符都单列为真实缺失或工程错误。

## 4. 新传播的准确对象与条件

科学schema为R347-original-C-complete112-projective-cut-family-enclosure-v1。保物理列(u,k=dH/dr)、连续通量j=w·k以及原x导数，完整误差随原列传播。

初始Q_F=1写成非零因子表示：

    (u,j) = a * diag(1,2^b) * v
    a_F = r_F^4 > 0, b_F = 0, v_F = (1,w_F*slope_F)

radius、w、slope全部为原完整深端包围，不选root中点。保存初始正幅因子、全部逐步二幂和真实pivot因子、幅符号、log|a|包围及完整因子链身份。未物化原QF=1的单个cut矩形列；这种表示边界在结果中明确为false，不借“归一化”丢掉原幅度。

每个panel先作准确二幂换框；原完整2×2矩阵的Taylor及Duhamel界乘整个继承向量盒范数，形成完整端点Y与闭管T。仅当某个端点Y_i的整个区间严格隔零时，才令该分量为1、另一分量除以Y_i，并把真实pivot乘回幅因子。两个候选分量都未隔零时细分；达到资源或深度界仍未付则保partial，不能借原准确可逆性强行除区间。

原40个定义逐文本保留，包括GeometryCache、balanced_matrix、taylor_exponential、完整矩阵范数及准确dyadic中心。原误差与norm目标、完整coefficient range、合法coarse box及所有继承不确定度保持；没有换成中点Riccati或丢掉幅度的射线模拟。

合法零宽闭叶保留共享端点责任。h=0使用恒等推进，仍记录可能属于的每个原闭panel；不能把点叶当坏输入或删掉重复端点。

## 5. 全cut候选与DN/非除Robin的区分

每个原cut逆像候选保完整闭管T0/T1、固定balance b、同一闭panel的正w、当前非零幅因子和索引。相应物理k的规范化系数是2^b T1/w，非除Robin行是：

    [ -2^b*T1/w, T0 ]  acting on (u,k)

它是对应候选自己幅度下的行，不能把不同panel/候选的规范化行直接hull后声称原QF=1列。

只有每个候选整个T0严格隔零，才允许其商2^b T1/(w*T0)；完整DN的hull必须在所有候选各自合法除法之后形成。端点成功选择chart不能支付整个cut闭管的高度隔零。部分合法候选的商另记partial_legal_cut_slope_hull，它不代表未付候选。

每mode同时记录完整空间传播、全部叶覆盖、候选高度条件、合法商数量、DN错误、last_paid、当前完整因子状态、pending闭栈及完整未访mode后缀。准确列非零、区间pivot隔零、cut高度隔零和非线性DN存在是不同命题；本入口不将它们互相替代。

## 6. 资源范围及真实停止

新线性阶段参数逐项为：

|参数|实际声明|
|---|---|
|precision_bits|256|
|budget_seconds|14400，实际按namespace剩余科学时间裁剪|
|max_panels|25000000，共享所有112模态|
|max_depth|32|
|local_defect_bits|12|
|panel_norm_limit|1/2|
|taylor_terms|24|
|max_geometry_cache_records|65536|
|free_bytes_reserve|2147483648|

原C3600不因本次有限头策略变更而延长。job硬限360分钟，namespace科学资源计划时点18900秒，末2700秒作为读回预留计划；linear step硬限250分钟，线性与规则读回步骤上限30分钟。C/cut/far/环境建立消耗真实全局时间，线性有效预算只取实际剩余与14400的较小者；没有剩余时保资源未启动，不伪造科学拒绝。

开始准备至少34359738368B可用空间；允许只清runner预装SDK等明确临时资源。这是输出容量资源条件，不能成为额外数学门。线性阶段每1秒或至多256次可用Budget检查观察一次输出盘，保2GiB余量。绑定和初始化成本与线性阶段内部计时分别记清。18900秒没有独立signal/alarm绝对杀钟，实际裁剪只发生在原rules startup之后、原linear runpy之前；driver输入绑定/runtime setup仍在其内部Budget计时之外。真实硬限为step250分钟/job360分钟，2700秒读回余量是资源计划而非无条件保证；实际延误、超时和未付范围照实记录。

次数/墙钟/空间停止都保存真实原因、已付前缀、当前状态、闭栈、剩余source与全部mode后缀。无突然人为截断“若干mode就成功”；原科学外对象和接受标准不减少。资源部分完成只结束该实例，课题继续open后继。

## 7. prepared记录、提交前缀与七个临时账本

全部科学大数组仅在该job独占RUNNER_TEMP/visible-stored-C-projective162下。详细ledger包括：

|ledger名|实际保存/读回范围|
|---|---|
|coefficients|完整闭coefficient盒原字节；新reader只核全流bytes/SHA/行数，不逐数值重证|
|accepted_panels|数学验证后的prepared panel，完整矩阵、继承状态/误差、pivot及幅因子；仅commit指向者属于paid prefix|
|cut_tube_contributions|全部实际cut候选完整原行逐行语义读回，保对应幅度/闭管/Robin/条件/商|
|projective_panel_commits|原prepared panel与cut span的提交记录、链身份；全字节/行数读回，未宣称独立数值审计|
|cut_leaf_coverage|每个原cut叶完整已付/未付范围逐行读回，保所有共享端点|
|complete112_mode_status_and_columns|完整112原mode行逐行读回，包括未开始者|
|complete_unpaid_scope|全部失败/部分事务/条件未付/未访后缀逐行读回|

accepted_panels文件名沿原协议，但其row先写、cut rows再写、最后commit row才允许推进live state。每mode给committed spans和uncommitted_written spans。异常半写不会自动付前缀，因子链初始项与逐panel项对应真实完整输入状态。

每mode原complete_required_cut_propagation只证明其空间范围按当前表示完成。顶层使用completed_factorized_cut_family_modes与all_complete112_factorized_cut_families_enclosed；不能误取旧completed_cut_column_modes。driver退出0只表示全部112的factorized空间范围完成，全部高度/DN旗标仍独立；不等于原物理cut矩形已物化，更不等于native或非零闭场。

## 8. 完整只读标量传输、错误与清理

新metadata reader只用标准库与已冻结原153 semantic helper；不导入科学driver，不做区间符号、DN、矩阵、残差或接受重算。完整result原JSON逐成员/必要长标量无损分段；每块至多90000B，原error字节按12000B段。上述四类小行ledger全部逐原行读取，不保top-N；大coefficient/prepared/factor提交流只全身份与行数，明确没有逐值独核。

input-binding与required-source-panel-index核完整bytes/SHA后保原身份；原定义/大coefficient数值不重复冒成此reader已独立证实。全部112 mode顺序/索引为纯元数据检查，原partial字段不改写。仅在producer真实提供完整DN文件时，reader才按真实descriptor读取该原文件；缺件不生成代替值。

原C/cut/far的小读回和原规则runner记录仍保留。各科学步骤使用原2700秒真实pull规则同步父进程，科学checkout固定GITHUB_SHA，科学子进程剥离凭据。规则clone在其他专属临时目录，reader只读本namespace内已净化的rule-sync原文件。root/API读取不是本地git pull，HANDOFF继续分别记录。

reader的summary schema为request162-actual-finite-head-complete-scope-readout-v1；job输出键保finite_head_summary、finite_head_summary_bytes、finite_head_summary_sha256。完整结果不塞进单个巨型GITHUB_OUTPUT；小report引用原index及完整已输出范围。

若final result真正不存在，reader只枚举实际残存原文件的bytes/SHA和错误，不编造最后栈或已完成mode。这个“已完整读取缺失范围”的读回成功也不支付科学成功。任何已记录读取/解析/身份/记录错误使reader exit2且不写complete marker。

进程收据按原PID/start_ticks确认父进程；父进程可共享job进程组，不要求该共享组为空。科学子进程保原runner的start_new_session专属PGID，另核同组存活成员。若原owner仍活或身份未明，停止读取科学账本，完整传输已观测规则/错误字节前缀并明确其未来尾部未读，exit2且无complete marker。只有C、cut、deep、projective四个实际读回步骤全部成功、readback-complete.json与同run/source吻合且当前原科学/规则进程确认停止，才删除独占临时输入与输出。读不全则不主动删除，随runner最终销毁；既有Actions日志仍保原错误。marker只标传输范围，不把原科学失败改成成功。不上传artifact、不建Release、不向Git保存可重算raw或证书输出。

## 9. 验证范围与继续责任

root已读新driver相对原R324完整差异、原reader全文及具体workflow来源/执行/清理差异；geometry逐定义核保留40项原实现并负责科学源。原source与请求逐字pin检查、源码解析及真实运行均由本次Actions完成，入口不预填其结果。

达到此子题的空间覆盖或DN隔零仍不付：有效选择唯一准确深根、无限非线性DN、共同准确C与数值代表误差、当前完整非零112场、全九冻结450、同g闭合、全phase六jet/曲率/reach/held/反射欧氏差/整闭面D及metric≤1e−6。原README标准和冻结后精化责任不变。

任何actual162结论须以真实run、完整原结果、模式/cut/叶/未付范围和明确的巨大账本未独核边界成文后立即提交；部分资源结束后继续open下一项，不能停在本接口或阶段报告。
