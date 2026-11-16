# R497：完整逆像闭片缓存的源接口

作者：ChatGPT /root（AI）。日期：2026-11-16。状态：完整固定输入包含证明与源码已成；没有新实际运行或性能测量。正文见[R497](../results/R497-completed-inverse-box-cache-and-preserved-original-work.md)。

## 文件、完整来源与交付边界

下列均是源或纸证，不是Actions生成payload、数值证书或保存的raw。独立main完整视图只在Actions由计划生成，不重复刊入Git。

|课题相对路径|字节|SHA256|
|---|---:|---|
|computations/geometry_20261116_completed_inverse_box_cache.py|10239|cf517af64d024de25f3f4083d77847dddc792ce569a369d323dc31b347a96edd|
|computations/root_20261116_completed_inverse_box_cache_source_views.py|6299|0d7853eaec96518f56329f0f97836ba58be9ff3764287e03d0440746134b1e55|
|computations/r497-completed-inverse-box-cache-source-plan.json|3050|ddefa7df8cc49678ae8d0c44ab91d1196634895e073758b0d17745636304c545|
|results/R497-completed-inverse-box-cache-and-preserved-original-work.md|12955|f1017fce688e37398b8e8be7016fb70d54fd8544feb674605a3ad5ad148ec972|

完整原源为computations/geometry_20261115_current_C_pruefer_joint_radial_sampling.py，69702 B，SHA256 32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4，Git blob decad25aac951886e0544e35de66f42f0e49ffa9。生成源为geometry_20261116_current_C_cached_inverse_joint_radial_sampling.py，70299 B，SHA256 ae9dde7a93cd0477d7d8669593459bedf75fdc58083625beee40dd047eab5594，Git blob 814b2c6578a05f0b774198ec08d8cb7555e8c7ba（仅完整文字/字节计算，非实际执行receipt）。

原F依赖geometry_20261115_stored_C_finite_head_pruefer_positive.py为95773 B、c2f515aa276890da63871fe0e9e1440775950d4985465457e9d6025976d914c8；原B依赖geometry_20261115_stored_continuous_E_cover_v3.py为89307 B、f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df。helper在实际加载模块上核这些全SHA和同computations目录，不改旧source身份。

本接口没有request编号、source_commit/run或成功采样结果。212/214/216已冻结源不变；R496的三层native连接不必等待本件。未来实际使用要在其新入口明确登记新main/helper/plan/generator和全部递归来源，不把本件完成纸证当成已完成真实连接。

## 原样保留的科学与五个文字编辑

原InverseSampler类正文逐字继承，包括candidate枚举、每点实际半径词cache、全部闭叶、strict-outside、两闭半片、coarse保留、point hull与midpoint代表及全数值误差、pending异常恢复。原far传播、112模式、stage字段、两mean、原query/advance、原预算和数学门不变。

源计划只做五组一次出现的明确替换：新增helper import；独立schema；新增来源SHA及缓存容量两个参数；原实际实例化处显式bind/构造；原最终result增加completed_inverse_box_cache字段。每个before/after全文在计划中；生成器同时核完整baseline与完整output，拒绝覆盖旧源。没有源码全局monkeypatch、函数临时替换或旧来源标签冒名。

生成视图的新schema为R497-current-C-completed-inverse-box-cache-pruefer-joint-radial-samples-v1。原计算祖先身份另留在helper source_binding；实际class owner是新view时照实记新SHA，不能继续让下游把它当作原32b0源。

## 实际源生成入口

只能在Rogerhu12/math-research-public的GitHub Actions中执行；先由所选新request创建原namespace和原绝对deadline。COMPUTATIONS必须是生成器自身所在、完整且有原递归来源的实际目录；SOURCE_RECEIPT_PARENT须已由该原owner建立且位于RUNNER_TEMP。下面是调用合同，不是本件已有执行命令记录：

    python "$COMPUTATIONS/root_20261116_completed_inverse_box_cache_source_views.py" \
      --computations "$COMPUTATIONS" \
      --plan "$COMPUTATIONS/r497-completed-inverse-box-cache-source-plan.json" \
      --plan-sha256 ddefa7df8cc49678ae8d0c44ab91d1196634895e073758b0d17745636304c545 \
      --out "$SOURCE_RECEIPT_PARENT/r497-source-generation"

新out须不存在，父须已存在；receipt目录不能拥有源目录。所有文件以exclusive方式新建，生成器不import科学、重开预算或删除任何raw。输出result.json含本次真实repository/run/source、自身来源、plan/helper/base/output身份、逐anchor出现次数、当前阶段、error和completed；exit0仅表示完整源物化成功。捕获的源物化错误exit2，未确认输出不补complete；环境或入口前置错误不保证已有receipt。

源计划全文与caller提供SHA绑定，因此必须使用上表完整原plan；不能只拷一个输出SHA或把任意新编辑塞进相同标签。正常源生成/完整source闭包/原入口已有检查是执行工作，不是新增fixture、独审或科学门。

## 实际采样调用与资源

未来caller在原采样位置调用生成main，并保原全部参数，另明确传：

    --inverse-box-cache-helper-sha256 cf517af64d024de25f3f4083d77847dddc792ce569a369d323dc31b347a96edd
    --sample-complete-box-cache-records 4096

容量须为整数0..65536，默认4096；0保每次原运算。其资源含义只是最大保存记录数，不是精度改动或字节限额。它不改变原sample-inverse-max-depth、32位工作目标、一百万work、候选完整性、任何数值误差或接受阈值。是否采用深度2是另一个已明确请求的原资源选择，不能由本件默改。

命中仍严格执行原budget.attempt及range_count加一；miss调用原complete_box一次并由其收费。原一百万工作上限并未解除，旧203/205/209不可据此重标为成功。原绝对时钟、linear/sampling之间原时间归属、失败/超时/未访、owner/quiet与原清理合同全部继承；缓存管理自身成本可能改变实际时间停止位置。

helper仅在单sampler的固定head/panel/geometry、F/B、精度/线程和base_speed状态内复用。新物理半径仍走原sample，不能重用别的点的代表值。外部修改head/panel或原地改球不属注册用法，必须新建sampler；本件不提供对任意修改的隐藏失效侦测。

## 必要读回合同

新main最终result中completed_inverse_box_cache为未构造sampler时的null，否则是实际readback。新必要reader须真正选择此字段并保下列完整语义；只写helper源或source graph而不接reader，不能声称缓存统计已读回。

|字段组|保留意义|
|---|---|
|source_binding|实际helper/class owner、原32b0祖先、原F/B完整来源、repository/run/source、新旧schema分列|
|capacity_records/current_records|实际容量和当前缓存条目数，无cached balls|
|calls_started/calls_completed|全部complete_box调用进入数与正常返回数，不把异常算完成|
|cache_lookup_hits/cache_hits_returned|查到完整旧记录与新调用真正返回的不同计数|
|original_evaluations_started/completed|miss进入原运算与其真正返回的不同计数|
|completed_entries_inserted/evictions|完整条目插入与LRU淘汰；不是采样叶完成数|
|disabled_calls/context_change_bypasses|容量0走原方法或计算中上下文变更未保存|
|last_operation|真实panel行/piece、准确闭区间、实际精度、分支、complete_return和已观察收费状态|
|actual_original_point_count/range_count/budget_attempts|原sampler/budget真实计数，保持原含义|

若原球已返回而后续cache分配失败，原计算完成与新调用完成必须分列；原pending恢复仍有效。若attempt先停止，lookup已命中不等于原工作已成功收费或响应已返回。last_operation的收费说明只记录实际可观察的分支，不推断原函数内部未观察位置。

原必要readback仍必须完整保本点radius/role、当前与全部pending闭片、已留范围、完整成功/失败/未返/未访、原数值误差与原异常。缓存元数据不替代任何这些字段，不恢复旧selector漏失且raw已删的记录。所有必要scope沿原单90KB/超限状态；不拆包、编码、保存cached balls或把大raw上传。原quiet与必要回传确认之后才按原owner清理。

## 可信度与继续工作

固定输入的原完整球复用包含命题已由纸证支付；源仅做文本、字面编辑、JSON和字节身份处理，未本地执行科学。未来新run须报告实际命中与失败账目，并从原真实采样继续全部native/H/J/FD/fullDN、完整453→450及后续metric/geometry责任；本件不另设“先证明提速”或“先独立测试”的科学门。

没有新normal native响应、完整当前H的338×112矩阵、接受场、几何比例或收敛结论。正式原任务持续，不能在这个局部优化、源准备或阶段报告上停止。
