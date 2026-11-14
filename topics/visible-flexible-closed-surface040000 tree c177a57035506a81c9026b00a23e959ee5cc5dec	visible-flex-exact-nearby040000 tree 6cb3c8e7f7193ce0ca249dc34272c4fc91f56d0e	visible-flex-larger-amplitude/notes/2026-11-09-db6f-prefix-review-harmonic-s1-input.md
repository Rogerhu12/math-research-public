# 对 tail-theory 的 s=1 逐模初猜构造器的独立全文审查

审查者：/root/coupled_prefix，2026-11-09。

**结论：PASS，仅支付输入构造和原 loader 接口；候选仍为 UNSOLVED。** 本审查未参与被审构造器的实现，未改其源码、方法或输入。它没有运行任何 root、flow、RK、DN、prefix BVP 或连续几何后端，没有生成另一份候选状态。

## 1. 冻结对象与来源核查

完整阅读了以下三件正文，并沿其真实 worker、core、subdivision、remesh 源核查了接口：

- scripts/db6f-tail-prepare-harmonic-s1-warm.py，SHA 66094a71fd7669faf15e78584c55159e9cd244479b1dada6cffe476181ae75f6；
- notes/2026-11-09-db6f-tail-harmonic-warm-interface.md，SHA 194b992a7f13d73138b1c288e6e3c6e84d81af3a3b2f3561c3452ce64fbca5aa；
- notes/2026-11-09-db6f-tail-harmonic-s1-from-call9-preparation.md，SHA 957eb4cf8a537a22ddbc2346760025691271cd602242f56d7a6a21f3bd7f6d20。

原保存的 input.json.gz 的 SHA 为 c6a4c0e504802885f358c340c1a23a34355476ee4d241e3ea6b14069b2b4f927。源 call9 的真实残差是3.796278258536727e-10，其原请求没有 Jacobian／audit；不能将这些旧响应性质移植到新候选。

独立检查器重新哈希全部77项定义绑定，并从原66项 launch、闭 call9 审计及其闭文件、原审计脚本、方法和构造器重新组装该77项并集。记录的八项实际响应源也逐个与当前冻结源码匹配。原 source/config/target 的身份和闭合审计残差一致。

## 2. 数学坐标和实际乘法

原每节点 shape state 有30项：前15项是 Q，后15项是保存坐标 Pi。原 cutJets 在调用局部 root 前才对 momentum 施加固定的端口倍率；原 cellFlow 则在自己的端口完成相应规范化。两个 gauge 都与本次同模的常数乘法可交换。因此本构造直接对保存的两半乘相同因子是合法的初猜变换，不应额外插入 r、w、r的四次方或 portRatio。

因子指数为存储谐波编号1到15，而非 Fourier 角频率3j。它不是 nonlinear moment、slope、second jet 或几何量的缩放定律；这里只重新指定下一次求解的初猜值。

自有检查器用另一种索引路径逐个重算：每一行第 col 项使用原第 col 项乘 factor[col mod 15]，不复用作者的两个 broadcast slice 赋值。因子表按作者明确的 binary64 幂规则独立形成，并核其 hexadecimal 编码。总计 **25950个数**与已保存候选逐个以64位位模式一致，包括可能的符号零。没有把 Python 宽松数值等号当作这一项的位一致性证据。

完整 parameters 与原 call9 参数按 canonical JSON 逐类型相同；rawNode 是13个非 bool 整数72n；rawStates 从同一份新 states 抽取，13×30项有限且非 bool。新目标独立从固定 affine goal 复制，不使用旧请求累计放大来替代 s=1 目标。

## 3. 原 loader 与同网格 remesh

原 worker 的选择顺序优先 response.checkpoint、seam.tail_checkpoint，然后才是顶层 checkpoint。新记录只采用最后这个明确的 checkpoint 分支，并且没有 response、seam、旧 request 或旧成功结果字段，因此不会误选旧已解节点。

本例同为 M15、physicalDepth12、parts8、steps32、N256。subdivision 的 rawSegment 从8到0、part 从7到0；remesh 的 rawLeft*8 为精确整数。对每个 raw cell 的71个内部节点，原索引式

$$
72n+(8-j)8+8-k
$$

恰等于新节点索引。独立小循环核了852个内部节点，连同13个 raw 节点，覆盖全部865节点且为恒等复制。没有补深或变模，因而 remesh 的 RK 插值路径不进入。这个结论不等于整个未来 worker 初始化零 root：原 startup 与真正 solve 仍照常执行。

cutHeight 是准确的新请求标签，所有15模非零。原 worker 首模请求除相同标签得到精确比例1，从而不会把已经逐模放大的状态再次统一放大。原 correctInitialBoundary 缺省真保持，随后仍用 H/c⁴−Q0 计算原线性补偿。这只处理初猜边界，不代付真正 shooting 残差。

## 4. 运行配置与诚实性

配置与原 continuation02 的逐类型差异恰为五个 I/O 键。原36轮、2e-9容差、默认0.05 guard、默认边界修正和全部物理／数值定义保持。参数对象中的旧 I/O 保留为 provenance，不能当作新执行 config；作者稿已正确区分。

新候选顶层为 UNSOLVED_HARMONIC_WARM_ONLY，preparation_only 为 True，actual_solver_runs 为0。没有复制旧 jets、Jacobian、audit、residual、history 或 converged。preparation 的 source_observed 只描述旧 call9，未冒称新候选成功。保存原目标标签不等于保存经过验证的新物理 cut jet，scope 已公开这一区别。

作者先前静态稿讨论 audit=False 的旧 trial-run，只将其称为普通 warm 入口；新增实际构造稿已明确下一次完整 audited 请求应使用 continuation-client，Jacobian 与 audit 都为 True。两份稿按发生顺序并不冲突。新输入不能塞进要求真实成功响应的 continuation --resume-checkpoint，也不能套用原 continuation02 完成身份。

## 5. 独立执行与可复跑接口

自有脚本 scripts/db6f-prefix-review-harmonic-s1-input.py 实际退出0，工具收据 b7abb5，耗时约0.207秒。它只读取已存 JSON/源码，核标量乘法、位模式和索引公式；没有导入原数学 engine，也没有调用作者 builder 生成第二份候选。

    cd /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface
    python scripts/db6f-prefix-review-harmonic-s1-input.py \
      --out notes/2026-11-09-db6f-prefix-review-harmonic-s1-input-independent.json

输出必须使用新的未存在路径。报告仅包含身份、计数、标量和通过范围，不含原 shooting 数组。复跑不读取活动 continuation trace 或状态。它不宣称新初猜满足 guard、不比较两种初猜的残差、不保证收敛，也不支付 final prefix、actualXYZMetric 或 README 完成标准。
