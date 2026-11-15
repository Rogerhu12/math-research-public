# Request125：实际123九控制末点的独立单批续算接口

分类：可执行候选接线；不是共振根、非零场或 native 接受证书。  
作者：OpenAI ChatGPT（amplitude agent）。  
日期：2026-11-15。

## 1. 这次实际承接什么

本请求从实际123已经记录的九个末参数开始，调用同一冻结九控制入口，再做最多8个方向。原123有8个方向、8个接受、17个外层试探，原未加权完整三残差 merit 从738.1754024784359变为431.4178353348037；原 unit、full112、非零场和总success仍为false，未执行native。正式事实见[actual123结论](2026-11-15-actual123-nine-control-eight-acceptances-and-complete-readback.md)。

本次没有添加控制函数，没有更换残差、方向公式或接受条件。新批明确把相对信赖半径重新初始化为0.1；不声称继承123的最后半径，也不猜测那个数值。原半径更新和拒绝规则保留。新批的状态、完整3×9响应、有限差分、域及圆形参考场都重新形成；原123的J、merit、场数组和证书不被拿来代替新求值。

父来源是已完成的run43696642468，source9744b760bff8a83f0c08a1ff910a4eec53796fad：

| 原件 | 原字节数 | 原SHA256 |
|---|---:|---|
| nine-control-curved-status.json | 1841773 | 661703c94d7e0134790cf3d3de7269dd165a88f93323a22f17c09ded8a842280 |
| 正常分段读回的primary JSON | 62682 | 4a2e32af6ebf7d7beaf390686e4ee3eafbf2779c72031714257dda9ffb51d24d |
| 原完整scalar view | 118661 | fb9cef3c9df29c595f0073c5c4652e48bbcbcc36958cd97eb39d3cb40921738f |

这些父原件身份与参数来自主控已核读回。本请求只消费小recipe中的真实参数字面量和来源记录；不重新下载上述原status、完整view或父模型数组，不声称本消费者又独立检查了那些原payload。

## 2. 真正的九参数初点

顺序仍为[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]：

```json
[0.4056906651860799,0.2312823028008991,0.49024979523256484,-0.028725992781639703,-0.028425978180153726,0.6149637073349259,0.1617124076331314,0.13337771251970604,0.04068635480707174]
```

三个eta均来自实际123末点，绝不清零。原前三个偶控制、三odd及三raw quadratic控制全部保留，参数维数仍为9。族的固定描述仍含“new_quadratic_controls=3”等原123族定义字段；本请求另明确其首次引入发生在123，125新增控制数为0。这些历史字段不是声称125又扩了一次维度。

recipe schema保持R259-explicit-nine-control-raw-quadratic-shape-recipe-v1。origin的producer_file、producer_schema和producer_sha256现在绑定当前九控制producer本身；父消费闭包26项等于当前26项。原123首次扩展所用的24→26、六参数父schema、附加三个零以及旧121 fallback来源检查，全部在新独立workflow中按真实123来源改为26→26、九参数父schema和正常primary身份。

## 3. 不改旧源的零eta对照边界

冻结family的zero_added_quadratic_reduction_readback会另构造同一前六参数下的旧六族及eta全部置零的九族，比较它们原evaluate保存数组，排除parameters字段。它不调用旧six.jacobian，不是独立旧六列响应比较。

在本请求的非零eta初点上，这个对照是明确的反事实参考点，既不是当前初点，也不是本次接受状态。main先对真实九参数调用evaluate；随后另做这个参考读回，再由真实state形成initial description。对照不会将真实parameters里的三个eta覆盖成零。新initial description中的完整3×9及旧六列子矩阵读数，仍来自当前真实九参数。

这个读回的数值一致性布尔量不是接受门。但旧冻结程序对该辅助evaluate异常没有单独吞掉的恢复分支；若反事实旧六族或零eta参考点的原求值抛异常，可能在准备阶段终止。当前没有实际证据表明该异常会发生，也不在本地尝试求值。125如实保留这一原执行边界；若实际发生，再按原错误定位修复，不预先修改科学源或假报已通过。

## 4. 保持原算法、预算和最终责任

唯一科学入口仍是geometry_20261115_small_core_nine_control_curved_recipe.py，原schema仍是R259-nine-control-full-three-two-normal-curved-trust-recipe-v1。当前九族不是旧fixed-g身份，原域证书也不被重用。

- 全三条原unit残差和未加权merit保留，原实际方向导数、0.2 Armijo及完整域判断保留。
- 完整3×9响应与12×9正则QR重新形成，全部九列保留；二法向和七切向的曲线路径不改变。
- 初始相对半径0.1；最多8个方向，每方向最多20个外回溯。拒绝方向仍占方向预算，原半径缩放规则保留。
- 原法向恢复最多12轮、每轮20个回溯，原1e-8误差目标是算法内部目标，不增加外接受条件；不把未消除误差手工设零。
- 原候选unit阈值1e-8、699节点、112场模/112尾模、2048物理角格、4096材料和边界角数都保持。
- 末端全部九参数三档有限差分、160bit/depth14完整新scalar Arb域和原完整圆场检查继续实际运行。
- 原完整112右端残差及候选旗标保留；高109块不能从低三进展被静默抹去，也不据控制函数独立性断言响应补秩。
- 原圆场在六个shape系数固定后仍使用三个active坐标和原453维责任；本请求不执行非零lambda场、native、fullDN或新的完整尾接受。

一次流程成功只说明该次已运行的步骤结束。候选是否达到原阈值、为何停止、各trial结果及所有false旗标，都以本次原输出为准。不存在下降、找到根或满足最终场门的预先保证。

## 5. 可直接落入仓库的三件接线

| 路径 | 字节数 | SHA256 |
|---|---:|---|
| computations/actual123-explicit-nine-control-resume-parameter-recipe.json | 2289 | ed40e690ba00550abedba7d4a65e09e217e6e433e8ced0efc956321e823ccd8b |
| computations/public-small-core-nine-control-resume-request.json | 38786 | 31bd23125d7fc7aa90032d2976ec7436130b7b596627c0f6128062b4aed2515a |
| .github/workflows/visible-larger-public-small-core-nine-control-resume.yml | 17934 | 1dfa0c4500c4ce68dc27d723f10d86a83b6908f5049e0d7c3aa1e2e330dc30a5 |

computations路径均相对于topics/visible-flex-larger-amplitude；workflow位于仓库根.github/workflows。新push trigger只匹配新的resume-request.json，不修改或触发原123 request；concurrency另用resume组。它只会由主控实际发布后启动，当前交付不含未来runID。

原83份科学source映射及2份辅助source映射逐项与123 request相同。三项关键SHA为：

| 固定源 | SHA256 |
|---|---|
| geometry_20261115_small_core_nine_control_family.py | 086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629 |
| geometry_20261115_small_core_nine_control_curved_recipe.py | 824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf |
| root_20261115_small_core_nine_control_curved_scalar_readout.py | f57a7dfae95f3e629aa412003e10ea4e32a9821b754c3d575318f97b09b7317d |

原规则runner保持3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde。两README的已读blob仍分别为74c08a36f6c997d0bc1e64a7956b42276f5fa5d7与bff8aea253a9e6a7a4fac28d810ac454c5499fec；运行时逐字核对，发现变化按原规则停止并读取。HANDOFF的唯一规则同步行与大小界限照原runner负责，不绕过；每2700秒真实pull/rebase、科学checkout不变。

## 6. 输入、运行与清理

四项原数学输入及SHA、大小全部沿123 request，使用公开历史8bd267107cc8710d371f3b62c02986655ac965b0按原路径临时恢复，逐SHA和字节数核对。原78份公开数值源只恢复到本次独立RUNNER_TEMP缓存，不因旧main清理而更换输入、改hash或默用不同配置。

科学CLI由request逐字给出accepted、prepared、tail-anchor、tail-config、parameter-recipe及recipe SHA，然后传原initial-relative-radius、candidate-steps、backtracks、normal-iterations、normal-backtracks、normal-target-tolerance、candidate-resonance-tolerance、interval-bits、interval-depth。输出仍是本次临时目录下small-core-nine-control-curved/nine-control-curved-status.json，不将父123原输出改名作为新结果。

Python3.12.14/numpy2.3.5/scipy1.17.0/python-flint0.9.0及BLAS单线程都不变。科学step75分钟，compute90分钟，独立report10分钟；资源截止/prepare异常是相应中断，不冒成已付完所有回溯、无根证据或数学拒绝。

原小读回先运行，再清理本请求自己的临时科学目录、四输入和78source缓存。清理只在RUNNER_TEMP下、核属主且不跟随顶层symlink，恢复请求自有目录的用户写权限后删除；不删除其它任务。清理成功不代表读回成功。

## 7. 完整trial读回与发布边界

冻结分段reader保持所有outer direction的完整trial_rows。每个段使用原BEGIN/END标签、独立字节数/SHA和组重构身份，单段不超过90000B；reader stdout直接进入compute日志，不能只输出段SHA而丢正文。primary只保原初末/FD/域/圆/来源及段描述器，不重新拼接全部outer组以塞入job output。

report job只接三项原scalar_summary、bytes、SHA，并核UTF-8 JSON字节；其BEGIN_VISIBLE125_SCALAR_SUMMARY和配套SHA事件形成独立本轮读回。若无compute输出，返回明示未完成的小摘要，不制造新status或继承父FD。原全部direction段仍在compute日志中。没有原payload上传artifact、Release或main，也不保存node_modules等无关目录。

## 8. 已完成的源码工作与实际待付范围

这次已完成原123公开请求/workflow的精确小文本变换、JSON一致性、UTF-8 SHA、29项workflow替换逐项计数和逆来源对照。83+2 pin映射、四输入、运行版本及除真实参数外的全部数值预算相同；科学argv构造正文未改。两份完整diff随交付供主控直接阅读。

当前终端不可用，没有声称重新执行Python/Bash AST、导入数值库或本地数值测试。原123已执行的源不变，实际源字节/AST校验仍由新workflow原preflight执行。这些来源检查不增加科学接受门。交付只创建未引用的Git blobs，未创建tree/commit、未更新ref、未派发或执行科学。后续实际125结果由公开Actions日志如实给出。
