# m3：`.5→.75` 全谐波初猜的一次真实 state-only 终态

维护会话：Astra-held10-1b6d88ec-20261120。观察日期：2026-11-20 UTC。

## 1. 实际结果与决定

在[真实接受的 `.5` 暖尾](2026-11-20-m3-m24-chord-warm050.md)完整
检查点上，仅作一次已明确授权的独立比较：把第 `j` 对原射击状态
（物理模 `3j`）乘以 `(3/2)^j`，保留原线性入口边界校正，再调用一次
**原 state-only 流与原残差评估**。目标高度逐字取自正在运行的原 `.75`
请求，物理尾和全部有限离散层不变。没有启动另一条 Newton 尾求解。

实际进程 `93992` 已观察 `exit0`，报告为
`original_state_only_residual_returned`：

| 量 | 实际结果 |
|---|---:|
| `state_only_evaluations_attempted` | 1 |
| `state_only_evaluations` | 1 |
| 完整 stage 数 | 1152 |
| 原归一射击残差 | **10783.573616065736** |
| native 流中的 `minA` | .7103966028315585 |
| native 流中的 `minD` | .9993787421107377 |
| Newton 步数 | 0 |
| DN 导数计算 | false |
| `accepted_tail` | false |
| 原射击门 | 2e-9，未达到 |

这一次原 native 域检查完整返回，没有域失败。域余量和初猜幅度并不
保证射击残差很小，实际 `10783.57` 也没有给出改变正在运行路径的收益
依据。因此保留原进程 **54314** 的 `.75` uniform 预测及 bounded-chord-3
续算，不取消、不改源、不再作 probe。

保存本条时，原 `.75` uniform 初猜的首个 fresh Jacobian 尚未返回。
本条不把上一档的 `5216.83995` 冒充本档对照，不据不同暖档数值作定量
优劣比较。原同档范数自然返回后才可补充比较。

## 2. 此次比较的参数与选择条件

输入是原 `.5` 完整响应的 1153 × 48 个状态，最终原射击残差为
`9.47489310856124e-10`。同一目标请求的首模高度之比恰为 `3/2`。
全部 24 项目标高度通过 preparation 源中明确声明的二进制有理数形成
余量判据；最大相对形成差为 `8.70040948786388e-17`。这项判据只选择
初猜，不是 libm 精度证书，也不放松任何射击或域门。

本次显式取 `maxScale=20000`，真实最大幂乘数为

\[
(3/2)^{24}=282429536481/16777216
 \approx16834.112196028233.
\]

只读状态分析中，幂预测后 `j=18,...,24` 相对同节点主模状态对的最大
幅度分别为
`[7.4659562e-4, 6.0385631e-4, 5.6446603e-4, 6.3062883e-4,
9.2125681e-4, 6.8516084e-4, 8.5155900e-5]`。这里状态对的范数是
`max(abs(u_j),abs(momentum_j))`；它不是物理空间中处处的高度范数。
这些数据既没有把任何高模认作纯噪声，也没有预先保证本次残差改善。

原 `linear boundary correction` 实际保留。原参数为
`M=24, spacing=3, physicalDepth=8, shootingParts=16,
quadrature=512, steps=16`，使用两个原 native worker。初猜以外的方程、
原 root 域检查、残差归一化和物理 profile 没有变化。比较源是已冻结的
`probe_full_harmonic_warm_state.mjs`，未为这次结果修改。

## 3. 实际命令及时间

令 `W=/workspace/scratch/1b6d88ecddf3/m3-work`，
`T=/workspace/scratch/1b6d88ecddf3/math-research-public/topics/visible-flex-held-10pct`。
实际完整 argv/env、开始/结束时刻和 `returncode=0` 保存于
`W/probe-warm050-to075-full-harmonic/command.json`。它对应：

```bash
env -u LD_LIBRARY_PATH -u LD_PRELOAD -u GITHUB_TOKEN -u GH_TOKEN \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  VISIBLE_FLEX_NATIVE_MANIFEST="$W/newg-full-harmonic-chord-native/native-manifest.json" \
  VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=5d129668f937eedef6ddb0b214fd1bb15e99adc725347aa6591304c0042630d0 \
  VISIBLE_FLEX_NATIVE_RUN_DIR="$W/newg-full-harmonic-chord-native/runs/probe-warm050-to075-once" \
  node --max-old-space-size=2048 \
  "$T/scripts/resume_m3/probe_full_harmonic_warm_state.mjs" \
  --source-topic "$W/newg-full-harmonic-chord-native" \
  --config "$W/probe-warm050-to075-full-harmonic/tail-config.json" \
  --checkpoint "$W/newg-wide-lambda0p002-m24-actual-chord3-r1/tail_0001.json.gz" \
  --target-height "$W/probe-warm050-to075-full-harmonic/target-height.json" \
  --max-scale 20000 \
  --report "$W/probe-warm050-to075-full-harmonic/report.json"
```

这是原实际调用记录，不应在已有输出目录直接重演。若有独立复现需要，
须使用 fresh native run 和 report 路径，保留原记录。完整 source/native
安装步骤见[此前 preparation](2026-11-20-m3-full-harmonic-warm-predictor-preparation.md)。

输入 `target-height.json` 的 `height` 逐项复制自
`newg-wide-lambda0p002-m24-actual-chord3-r1-worker-trace.jsonl` 中
`event="request", call=2` 的实际 `height`，没有重新按近似数值形成。
`tail-config.json` 从原 `tail-settings-chord3-r1.json` 复制，只把
`initialCheckpoint` 指到已通过 `.5` 响应、`traceFile` 指到本次独立
目录，并显式设置 `fullHarmonicWarmPredictor=true`、
`fullHarmonicPredictorMaxScale=20000`。probe 自身直接调用一次
`tail.evaluate(..., false, scales)`；没有调用 `tail.solve`。

native batch 从 **14:25:54.303** 至 **14:30:43.065**，实际 native
process seconds 为 `288.72731050899995`；完整 probe 用时 `321.407`
秒。两路同时运行的实际时间不构成算法加速基准。

## 4. 来源与哈希

| 对象 | SHA256 |
|---|---|
| 冻结 `probe_full_harmonic_warm_state.mjs` | `433616953af3878f72c512ebf43ec2aa496b91586a6abcbef681d54e3af08fba` |
| 原 `.5` 响应 | `12674cc4fe86fc221d42dc5cb85c51699e7cfc0808a39b94ae91472eec125a53` |
| 实际 native manifest | `5d129668f937eedef6ddb0b214fd1bb15e99adc725347aa6591304c0042630d0` |
| 本次 `command.json` | `3ccc693ba7e4ddfeb93bf13c11d08a651e3c181c58e00b4b255caffc55df5f48` |
| 本次 `tail-config.json` | `4b8c4bbe055d3435ef9d3d8973cf0f03f505fcf6a40d17402a4192b05cbcbf2f` |
| 本次 `target-height.json` | `235160fb47357be8eab9a9251b3ed66fc921c6a133f86d707daef6ec6939f484` |
| 本次 `report.json` | `47b5e3b053702d838e6b3e585f9da4efba03d2cdce6282e719d6de2dcbb6a312` |
| 本次 state-only input | `a0e469e0023ffa6d2b4caa92a297d3307080c161b343706b51058b8aa6093fac` |
| 本次 state-only output | `cc79c95b2505c831da85754fb6a19c8133f788904ffe1ce0adda06cfaf1cd580` |
| 只读幅度风险小 JSON `warm050-to075-harmonic-predictor-spectrum.json` | `d28a845a451af744959fb19b144ca167135731f04ccce038c14789389603870e` |

完整 binary output 和原逐 stage native 诊断留在上述独立 run 目录；
标准错误文件为空，原进程返回 `0`。可再生数组及大记录不入仓库。
此条仅支付一次初猜的真实有限 residual/domain 比较，不增加任何
DN 接受、同一固定度量精化、连续尾、闭面或严格存在结论。

## 5. 14:36 UTC：原同档初猜自然返回后的对照

没有增加评估。原 `54314` 进程的 `.75` 请求在 native fresh Jacobian
call `11` 完成后，于 **14:36:22.417 UTC** 记录真实 iteration `0`：

| 原 `.75` uniform 初猜量 | 实际值 |
|---|---:|
| 原归一射击残差 | 6438.708166133377 |
| `minA` | .7146263080783993 |
| `minD` | .9993759476445716 |
| call `11` native process seconds | 926.3459396989997 |

因此对同一 `.75` 目标高度和同一原有限尾层，本次全谐波初猜与原
uniform 初猜的初始范数之比确为

\[
\frac{10783.573616065736}{6438.708166133377}
 =1.6748039106331436.
\]

本次全谐波初猜没有降低这个实际初始残差；这支持保留正在运行的原
路径，不是对一切可能暖初猜的普遍否定，也不是两种完整 Newton 算法
的性能比较。原进程已在 `14:36:33.678 UTC` 进入 call `12` 的 state
校正，未中断、未切换；没有新增 probe。

这次只读同档比较保存为
`W/probe-warm050-to075-full-harmonic/same-target-comparison.json`，SHA256
`32c9d958e31607613d5e6ebb843bfae44b659e6747698e54370e0dfc986126df`。
它绑定原 iteration 行和已保存 probe 报告；新增 flow 数为 `0`。

[精简真实终态](2026-11-20-m3-full-harmonic-warm-probe-execution.json)保留1/1评估计数、原域和原残差。
