# m3：新多段物理 g 的 q=.006 原八条 linear DN 首解

维护会话：Astra-held10-1b6d88ec-20261120。

这次实际求解使用 R55 及其宽盒补充所用的多段低曲率起步 profile，在其原 mode3
线性根附近直接求原八条 linear DN；没有借用旧 g 的 H3 初始化边界。
有限 BVP 与原 metric 门均通过。这是新物理 g 的第一个实际暖启动场，
不是原非线性尾、严格等距存在、闭面或 held/reach 完成证书。

## 1. 固定源、物理输入和完整命令

新 provider 与线性根的完整定义、真实接口检查及可执行重建入口见
`2026-11-20-m3-multistage-profile-provider-and-interface.md`。
本次使用安装完成后冻结的源副本 `m3-work/multistage-source-v2`。
原 ShortBridge 的 curvature=4、peak_fraction=.2，原 port 的物理尾
参数保持不变。该 port 的首 valleyControl=4.625，因此不能引用
首 valleyControl=3.125 的旧 R21 数值曲率/支撑预算。

实际命令如下；输出目录创建前不存在，没有 raw/checkpoint 冷替换：

```bash
REPO=/workspace/scratch/1b6d88ecddf3/math-research-public
WORK=/workspace/scratch/1b6d88ecddf3/m3-work
TOPIC="$REPO/topics/visible-flex-held-10pct"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_m3/portable_prefix_continue.py" \
  --source-topic "$WORK/multistage-source-v2" \
  --short-bridge "$WORK/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py" \
  --profile "$WORK/multistage-linear-root-profile.json" \
  --chart "$WORK/bootstrap/reference/chart.json" \
  --port "$WORK/bootstrap/q060-port.json" \
  --amplitude .006 --warp-reference .006 --modes 8 \
  --angular 256 --audit-angular 512 --nodes 401 --max-nodes 6000 \
  --tol 1e-6 --bc-tol 1e-7 --physical-bc-tol 2e-9 \
  --outdir "$WORK/newg-q006-linear" \
  > "$WORK/newg-q006-linear.log" 2>&1
```

可移植重建时，上一 note 的 bootstrap 新输入目录名是 `inputs`，
对应替换这里的 `bootstrap`；物理 profile 可直接用已提交的
`scripts/resume_m3/multistage_profile_linear_root.json`。数值 chart 是
原旧 profile 生成的固定坐标函数，只改变坐标表示，不把它的
`reference_profile` 当作本次物理 g。

| 输入或源 | SHA256 |
|---|---|
| portable continuation | `6dafa9551d5ae4a4f4d59e1b2d4c177efdc6b823e0a7ade826974e4ecdc5c9ea` |
| 新 provider | `887a8d04157dfcee504f80d8cc2e7b66d9ae430775b4bc1df0bfea70bd49ceed` |
| 安装后的 flat 分派 | `c8a6372954f6db3e83a373864fbc877e5df6eca7c4e95ccb2b6e92512801a9c0` |
| 原 ShortBridge | `7e00a3336a302ba94c751c09e6f75749d6973c86605269538c8f0b44c60779b4` |
| 新线性根 profile | `3f4042ffe0666bf8ba5b09dca3d056f9b0604b8e4ab3367e537d924bb7b0cfcc` |
| 固定 chart | `dc85dda524e03896b4afa552bd1f859b73cf96f88033565ff910e227034f2f93` |
| 原 q060 port | `aa482f3bbd9506b90e307df72a7890f02f933338a4b3dec230f90b10765b09a5` |

## 2. 真正返回的有限解

进程实际 exit 0，五个网格为 418、492、540、591、598 点，约 119.43 秒。
`run.json` 和 raw 均记 solver_success=true；没有仅凭进程返回码认定通过。

| 项目 | 实际值 |
|---|---:|
| 最大 collocation RMS | 9.980239911427089e-7 |
| 原有限 metric_l1 | 5.590336976660327e-9 |
| flow_defect | 7.111939897111425e-9 |
| Cartesian Darboux l1 | 3.5799278904629264e-5 |
| 原八条 linear DN 物理残差 max | 7.437680867776107e-19 |
| Frenet root 最小采样值 | .0038979523830345864 |
| 角坐标 rho 最小采样值 | .952 |
| 曲率采样最大值 | 7.223030798712659 |
| 半径采样最大值 | 1.0668987845306082 |
| 高度采样最大值 | .8507903104136367 |

metric_l1 的审计使用 1344 个 s 点与 512 个角点。它是原离散
FFT l1 审计，不是连续角度上界。曲率采样值也不替代全域 K/reach。
原 DomainNewton 统计为 calls=5、accepted_steps=15、no_step=0、
domain 拒绝=0、merit 拒绝=51，最小接受 alpha=1/8192。

非线性设计返回

    delta = .0641442543020649,
    delta 增量 p0 = -7.07621153300075e-8,
    q = .006.

实际 support c6,...,c24 为

    [4.554208165842986e-6,
     -4.3934738817853786e-8,
     2.0261355779996295e-10,
     8.659926518857019e-12,
     3.252834699801811e-14,
     -6.990119849775805e-16,
     1.7269672321188408e-15].

这些是 normal-angle support 的物理系数，不是未乘尺度的 Newton p。
本次 q 与 delta、支持高矩都是设计变量；没有声称这是冻结一个 g 后的
连续非刚性族。末端第一 H 系数为 -1.6073818587992746e-5，来自本次
真正返回场，与旧 g 的历史 H3 条件无关。

## 3. 原始返回保存与下一次输入

所有完整可再生场留在 scratch 的 `m3-work/newg-q006-linear`，不提交数组。

| 对象 | SHA256 |
|---|---|
| `inner-00.npz` 原始返回 | `5a64bd2a51a3159632b6514198d54d6cc4a6cc5d23b914b7a43d83ac8f25c588` |
| `physical.npz` 完整物理 quintic 场 | `7363e531bc19b1d1841af8ff8a4cebd11b706fd35b76fd215a43ec345b4cd780` |
| `checkpoint.json.gz` | `806d9d11827e696899727e41519ff07a28c28e780cabf90ca910e98bdda4fa18` |
| `run.json` | `389d7edd78f01659f236d8aa17539d6bee994261a2a316c2ce08fbb50b7365cf` |

后续幅度步骤从此实际 checkpoint 通过原物理角度 pullback 生成初猜，
保持八条原 linear DN 和全部 solver/metric 门。通过当前初猜不等于
下一幅度已存在。新 g 的原非线性尾、材料圆化、完整角谱、固定 g 的族、
闭面及整体几何条件仍待支付。
