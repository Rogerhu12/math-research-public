# 真正 λ=1 设计场接原 full-DN / chord3 / native4 的窄协调入口

日期：2026-11-26。会话：Astra-held10-06bbeb39-20261126。

本入口只装配已审的原求解器。当前没有新的 λ=1 输入，没有执行本入口，也没有重跑旧 .25/.5 尾。它不制造新的模型 KIND 或最终数学验收器。

## 输入与调用

源码文件为 scripts/resume_20261126/continue_original_actual_dn_chord.py。在保留真实场的同一 runner 上，调用：

    python -u @REPO@/topics/visible-flex-held-10pct/scripts/resume_20261126/continue_original_actual_dn_chord.py \
      --repo @REPO@ --work @WORK@ \
      --source-run ACTUAL_LAMBDA_ONE_RUN_JSON \
      --tail-config EXACT_BASELINE_CONFIG_BOUND_TO_ITS_PORT \
      --outdir @WORK@/lambda-one-actual-dn-01

默认原 harmonic warm 因子为 .25、.5、.75、.9；可通过 --tail-warmup 明确选择递增因子。原 portable driver 随后始终请求完整未缩 H、完整 J 和 audit，保持最多八次实际外迭代及所有原门。改变暖步不提供速度保证。

默认继承来源中已验证的 streamed/released-LU 执行方式和径向 block；也可显式给 --streamed-rhs-block N，或用 --original-prefix-driver 明确选原直接入口。两者都调用原 portable driver。实际执行 argv、原 portable argv、wrapper/source SHA 与真实 radial-batching.json 分别绑定，原 run.json 不改写，不声称分批浮点逐位相同。

入口首先要求真正 λ=1。原 R53 来源复用 material_design_secant_predictor.accepted_original 的实际 raw/status/RMS/BC/metric、完整 artifact 与 source/input 门，并保持 curvature_blend=1。显式 v5 来源复用 warm_delta_phase_entry_v5.accepted_input，额外要求 SOLVER_RETURN 与 solver_invoked=true；同图零锚不作为新 solver return 接受。其他 family 被拒绝。

## 只复用本 VM 已有的真实准备

- work/chord-source 的 stage SHA 必须与 work/chord-install.json 相等，installer 和源 stage 的 SHA 也核实；保留原 fresh-final-J 合同。
- work/frozen_flow_batch 的字节必须与 recovery-setup.json 及 bootstrap native manifest 的真实绑定相同。旧 M24 manifest 只证明所复用的 executable/source 来源，不用于配置新 M 的计算。
- 由原 prepare_recovered_native.py 在 fresh 目录生成实际 M/spacing/N/steps、workers=4 的新 manifest，逐个核 owned/native 文件 SHA。保留 M<=64 与 N>4*M*spacing 的原硬门。
- 原 source-topic、chord-source、新 native-source 中四份 prefix Python 逐字相同：db6f-prefix-coupled.py、950f-prefix-adaptive-chart-bvp-v2.py、950f-prefix-warped-bvp.py、78718-prefix-fourier-jacobian.py。
- 不重新编译、不重跑 prefix/旧尾、不添加算法或缓存。native-runs 不预创建，由原 evaluator 建立。

先按原 port.source.config_sha256 验证 baseline 配置；runtime 配置完整复制，仅加入 chordMaxCorrections=3 与新的 traceFile。两份配置的 path/SHA 分别保存，原数值与物理设置不改，runtime SHA 不冒充原导出 port 的 SHA。

## 原求解器与真实输出

继承实际来源的 portable argv，只替换 source-topic、完整 source raw 的 raw-restart、runtime tail-config 和 fresh outdir，移除旧 control-record/restart-checkpoint 初猜选项。原 profile、chart、core provider/settings、gauge、angular、mean、pscale 与门保持。δ 和原 core 控制仍是设计未知数，输出明确不是 fixed-g refinement。

原实际 run.json、raw、physical 和尾包保持原样。小 summary 复用原 actual_gate 与 original_finite_checks 报告有限门，并记录 native/config/source 的实际 SHA；任何补充 provenance 检查之前先保存原返回与 artifact 身份，后续错误不会抹掉昂贵求解的原记录。不存在把 v5 线性验收器套到 actual 输出的步骤。

热投影 result 只保必要标量与文件 path/SHA。完整 core_settings、实际 profile 和两条执行 argv 留在 runner 本地；actual_outer_checks 仅投影原 outer/actual_bc/actual_tail 三个标量键，全文仍由原 run SHA 绑定。协调器不加入 summary 大小停止门；现 worker 自行限制投影，不能因此中断昂贵计算或抹除返回。

最后完整尾包按原 seam_audit 的 tail_record 读取，只核其配置、请求 J/audit、真实 source SHA 与记录身份。height-binding.json 在 runner 本地保存该 unscaled physical-endpoint 请求的完整高度及 raw candidate_H，分别记录两者是否逐项相同；不以近似相等替代完整高度身份。原 source mean N 与原 seam_audit 的 64M 网格分别保存，不据后者的 mean 诊断宣称共同 Cartesian mean 两 jet 已通过。完整接缝、无限尾、固定 g 的收敛、闭合、diameter 与 reach 仍未因此获得证明。

## 当前验证范围

2026-11-26 执行环境恢复后，独立 scratch 中的源码已实际通过 python -m py_compile 和 python … --help，两条进程均 exit 0。文件 SHA256 实测为 7a1ce40d5141c08f4d76b2bc201f3113b04d02f12f60c06809a9053ba03321cc，与所交缓存正文一致。这只验证语法和 CLI；没有执行 BVP、native preparation 或尾求解，也没有 λ=1 数值输入。没有真实 λ=1 输入时不得启动实际尾求解。
