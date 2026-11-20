# m3：完整谐波 warm 初猜的受控可选入口

维护会话：Astra-held10-1b6d88ec-20261120。

当前 chord3 真实求解保持不动。本条仅接原首 `.25 H` 完整 checkpoint
做逐模只读诊断、显式可选初猜源安装和参数一致性检查；没有重跑
`.5 H`，没有启动 state-only 比较或新射击。

## 1. 原 warm 路径没有对这条完整 H 谱使用幂缩放

原 `950f-tail-stage-port-v3.mjs` 仅在
`harmonicAmplitudePredictor=true` 且全部高模目标恰为零时，才将第 j
谐波的高度/动量状态乘 `ratio**j`。实际 warm 的高模 H 都非零，因此
当前路径先把全部状态统一乘主模 ratio，再用原完整 linear response
补齐新的 Dirichlet H。

本次 `.25→.5` 的物理目标实际上满足全部24个 `Hnew_j=2**j Hold_j`。
用实际解析后的二进制数作 BigInt 精确有理比较，24项的差全部严格为0。
这只说明另一种初猜的谱关系成立，不说明其内部场残差更小。

## 2. 已保存状态显示不能盲目放大高模

来源是已通过原射击门的
`WORK/newg-wide-lambda0p002-m24-actual/tail_0001.json.gz`，SHA256
`302662026a7e213647d8bfb2813f970174c8c919bb6f4d406e073ef9f3c110de`。
每模量级取全部1153节点上 `max(abs(height_variable),abs(momentum_variable))`；
这是原 shooting 坐标，不是各深度的物理高度。相对量取同一节点相对于
主模该量级的比值，再对全部节点取最大。

| 谐波 j（物理模3j） | 状态对的全节点最大值 | 同节点相对主模最大比 |
|---:|---:|---:|
| 1（3） | 6475.823625758005 | 1 |
| 6（18） | .01581500214221729 | .001549554307352674 |
| 12（36） | 8.477861726000942e-7 | 4.3068505540981234e-8 |
| 18（54） | 1.3134886169678513e-10 | 4.462808676573273e-12 |
| 19（57） | 9.312361908112266e-11 | 9.441626460016702e-12 |
| 20（60） | 3.718739526832641e-10 | 7.189524281644391e-12 |
| 23（69） | 2.2928737258118183e-9 | 2.3229769576104174e-10 |
| 24（72） | 9.525521500112944e-10 | 7.960074993792306e-11 |

高模量级下降后回升；仅凭这些数不能把它们全部判作舍入噪声，也不能
删掉这些模。但 ratio=2 的幂缩放将第24模绝对放大16777216倍。
相对主模，第23/24模的上述比值将分别乘2**22和2**23，达到
9.743271545213204e-4 与6.677394877352609e-4。这可能放大真实截断误差或
数值噪声，因此本条不实际尝试这一步。

全部24个紧凑逐模量级保留于
`WORK/warm025-harmonic-predictor-spectrum.json`。它不含场/矩阵数组。

## 3. 新开关、形成误差判据与原门

新增独立 installer：

    scripts/resume_m3/install_full_harmonic_tail_warmup.py

默认原 worker 分支逐字保留。只有显式设置
`fullHarmonicWarmPredictor=true`，并另给明确的有限
`fullHarmonicPredictorMaxScale>=1` 时，才尝试完整谱判据。
以实际二进制 H 的精确有理值定义 `r=Hnew_1/Hold_1`。每个 j=1,...,M
要求零项模式相同，且

    abs(Hnew_j - Hold_j*r**j)
      <= (32*j+16)*2**(-52) * max(abs(Hnew_j), abs(Hold_j*r**j)).

所有乘幂、交叉相乘和比较都在 BigInt 中进行，避免由普通浮点比较
误判这个判据。该小相对范围是明确的初猜选择容许量，不是对所有
NumPy/libm 乘幂实现的误差证明，也不是把实际不等的 H 强行当作精确相等。
未满足此条件则回原初猜；即使满足，还必须使所有实际幂乘数不超过
显式 maxScale，否则也回原初猜。原已有的“只有主模目标非零”行为仍
按原分支保留，新增上限控制的是这次完整谱扩展。

真正使用新幂缩放后，原 linear-response 边界修正仍按实际 req.height
逐项执行，随后每次试算仍经过原真实 flow、Frenet域、shooting残差和
全部接受门。若新幂缩放产生非有限初猜，会回原统一 ratio 初猜。
trace 明示使用哪一种初猜、逐谱一致性与最大放大倍数。改变的仅是
初猜算法，不是物理 g、边界值或原门。

## 4. 已执行的安装与元数据检查

~~~bash
WORK=/workspace/scratch/1b6d88ecddf3/m3-work
TOPIC=/workspace/scratch/1b6d88ecddf3/math-research-public/topics/visible-flex-held-10pct
python "$TOPIC/scripts/resume_m3/install_full_harmonic_tail_warmup.py" \
  --copy-from "$WORK/newg-bounded-chord-source" \
  --source-topic "$WORK/newg-full-harmonic-chord-source" \
  --manifest "$WORK/newg-full-harmonic-warm-install.json"
env -u LD_PRELOAD -u LD_LIBRARY_PATH python \
  "$TOPIC/scripts/resume_n4_tail/native_extended/prepare_recovered_native.py" \
  --source-topic "$WORK/newg-full-harmonic-chord-source" \
  --dest "$WORK/newg-full-harmonic-chord-native" \
  --native-cli /workspace/scratch/1b6d88ecddf3/n4-work/frozen_flow_batch \
  --modes 24 --spacing 3 --quadrature 512 --steps 16 --workers 2
~~~

两项均真实 exit0，相关 JS 已 node --check 通过。另对实际保存的
`.25/.5` 两组 H 只运行纯 eligibility helper：

- 显式 cap=16777216：24项精确相等，形成差为0，谱判据通过；
- 显式 cap=1024：实际以 power-scale-cap 拒绝2**24放大；
- 只把第8谐波新 H 乘(1+1e-8)：实际拒为谱不符。

前一项只是元数据检查，不是建议或执行该巨大放大。小结果为
`WORK/full-harmonic-warm-eligibility-check.json`。

| 对象 | SHA256 |
|---|---|
| 新 installer | 48bb70b4e90d0fd3303dc74a0422074e493711e3f0a22710787a21426dce7b21 |
| 原 unnative worker | 4e5f7f4cd31c81b633c826a24b208bc8a0aa2b791132c73238a5a61cf0e2a398 |
| 新 unnative worker | 893533dd70a774793fdaf3426f17191b49c19dbf2fcff62ad48c0538048dd151 |
| 纯谱 eligibility helper | 362bfc92b5fe54e95507c4f47efb10a3a876aefdea10c8a66e3c259fd0d7980f |
| 独立 native manifest | 5d129668f937eedef6ddb0b214fd1bb15e99adc725347aa6591304c0042630d0 |

实际 source-topic 就是 `WORK/newg-full-harmonic-chord-native`，不是其下
额外的 native-source 子目录。此绑定尚未启用数学 batch，也没有选择
下一真实目标或maxScale。以后仅在新的真实 warm checkpoint 已返回且
其初猜缺陷证据仍支持时，才考虑一次原 state-only 比较；比较本身不能
拖延已在进行的完整 full H/trueDN，也不作为必经流程。

## 5. 只算一次原 state flow 的独立入口（尚未执行）

另备 `scripts/resume_m3/probe_full_harmonic_warm_state.mjs`，SHA256
`433616953af3878f72c512ebf43ec2aa496b91586a6abcbef681d54e3af08fba`。
本次只实际做了 `node --check`，没有运行其数学入口。

它先要求完整已通过原 shooting gate 的真实 checkpoint，核同物理
参数与同 M/depth/parts/quadrature/steps，再作上面的完整谱有理判据
与显式放大 cap；沿用原 remesh、幂初猜和原 linear boundary correction。
随后只调用一次原 `tail.evaluate(initial,target,false,scales)`，返回完整
原 normalized residual 与 native 域信息。它不做 Newton，不生成 DN
导数，明确 `accepted_tail=false`。即使这个初猜的残差低于原射击阈值，
也不能替代必须完成的 fresh-J 和其余原审计。attempted/completed 次数
分别记录，避免把中途异常的调用冒称从未尝试。

未来若选择使用，CHECKPOINT 必须指届时真实返回的文件，TARGET_HEIGHT
是该次明确目标的24项物理 H JSON，MAX_SCALE 是据该检查点量级另选的
显式上限；本条没有预选这些参数，也没有发出该执行命令。入口形式为：

~~~bash
# Only after selecting a new actual checkpoint/target and a fresh owned native run directory.
env -u LD_LIBRARY_PATH -u LD_PRELOAD \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  VISIBLE_FLEX_SPARSE_PYTHON=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  VISIBLE_FLEX_SPARSE_LINEAR_HELPER="$TOPIC/scripts/nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py" \
  VISIBLE_FLEX_NATIVE_MANIFEST="$WORK/newg-full-harmonic-chord-native/native-manifest.json" \
  VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=5d129668f937eedef6ddb0b214fd1bb15e99adc725347aa6591304c0042630d0 \
  VISIBLE_FLEX_NATIVE_RUN_DIR="$FRESH_NATIVE_RUN" \
  node --max-old-space-size=2048 "$TOPIC/scripts/resume_m3/probe_full_harmonic_warm_state.mjs" \
  --source-topic "$WORK/newg-full-harmonic-chord-native" \
  --config "$WORK/newg-wide-m24-port/tail-settings.json" \
  --checkpoint "$CHECKPOINT" --target-height "$TARGET_HEIGHT" \
  --max-scale "$MAX_SCALE" --report "$PROBE_REPORT"
~~~

FRESH_NATIVE_RUN 的父目录需先存在，运行目录本身应全新。是否实际调用
仍由新 warm 返回后的真实缺陷与预计收益决定；当前 session54314继续
原已冻结的 chord3 路径，不为可选比较停算或附加验收流程。
