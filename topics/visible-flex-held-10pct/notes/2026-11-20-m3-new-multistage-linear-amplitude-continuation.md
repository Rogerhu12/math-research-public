# m3：新多段物理 g 的原八条 linear DN 幅度延续

维护会话：Astra-held10-1b6d88ec-20261120。

起点是 `2026-11-20-m3-new-multistage-q006-original-linear-dn.md`
记录的真实 q=.006 场。每一步只从上一真正通过 solver 与原 metric
门的完整 checkpoint，经原物理角度 pullback 与原幅度初猜缩放续算。
八条末端条件都是原 linear DN，没有 H 初始化替换、放宽门或冷重启。

源、安装后的新 profile provider、原 ShortBridge、固定 chart、原
q060 物理 tail/port 均与起点 note 相同。参考 profile 是归档文件
`scripts/resume_m3/multistage_profile_linear_root.json` 的精确字节。
每步 q 和 warp-reference 同变，delta 与高阶 support 系数仍作为
设计变量；本路径不冒称同一个冻结 g 上的族或固定 g 加密。

统一重现命令如下，Q、PREVIOUS 和 TAG 按各节的实际值代入。完整
路径沿用起点 note；移植环境可按 provider note 的 bootstrap 重建。

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
  --restart-checkpoint "$WORK/$PREVIOUS/checkpoint.json.gz" \
  --amplitude "$Q" --warp-reference "$Q" --modes 8 \
  --angular 256 --audit-angular 512 --nodes 401 --max-nodes 6000 \
  --tol 1e-6 --bc-tol 1e-7 --physical-bc-tol 2e-9 \
  --outdir "$WORK/$TAG" > "$WORK/$TAG.log" 2>&1
```

以下有限审计都是原 s/角节点上的 FFT l1/采样指标。曲率采样不等于
全域 K；真实非线性尾、圆化、完整角谱存在证明、冻结 g 的连续族、
闭面和整体 reach/held 均未由此支付。所有可再生场仅保存在 scratch。

## q=.012：从 q=.006 真 checkpoint 续算

Q=.012，PREVIOUS=newg-q006-linear，TAG=newg-q012-linear。
上一 checkpoint SHA256 为
`806d9d11827e696899727e41519ff07a28c28e780cabf90ca910e98bdda4fa18`。
实际 exit 0，solver_success=true，603 点，5 个网格，38.77 秒。

| 指标 | 实际值 |
|---|---:|
| 最大 collocation RMS | 9.793280840668886e-7 |
| metric_l1 | 1.1331833947569318e-8 |
| flow_defect | 1.4237759496965246e-8 |
| Darboux l1 | 4.934667640953694e-5 |
| physical BC max | 1.4538016045875087e-16 |
| 曲率采样最大值 | 7.402421276048871 |
| delta | .0641440396964114 |

DomainNewton 为 calls=5、accepted_steps=9、merit 拒绝=2、
domain 拒绝=0、no_step=0、最小 alpha=.5。物理 c6,...,c24 为

    [1.8229238018573788e-5, -3.517571598139732e-7,
     3.2470172663308963e-9, 2.7741233992403076e-10,
     2.087739923334842e-12, -5.6100888315506345e-14,
     5.712511711696416e-14].

| 返回文件 | SHA256 |
|---|---|
| raw `inner-00.npz` | `2c7cb11d07ea876759a4152d99c3c06fa504603cd6a9d45a9ef953a73217b584` |
| `physical.npz` | `eadbea3eb176464d91f07a94960dd1566778fbd23c417da0a3d0915005fac2b8` |
| `checkpoint.json.gz` | `5ca98350a642a1a91357d6ecf4f2dcb7aaf205dc6255a577b3d0df97c78c630c` |
| `run.json` | `d13c3084823dc13649c7b08b0bdadba79fc4ef6764c69280d997c293a44f26dc` |

## q=.020：从 q=.012 真 checkpoint 续算

Q=.02，PREVIOUS=newg-q012-linear，TAG=newg-q020-linear。
上一 checkpoint SHA256 为
`5ca98350a642a1a91357d6ecf4f2dcb7aaf205dc6255a577b3d0df97c78c630c`。
实际 exit 0，solver_success=true，606 点，约 38.74 秒。

| 指标 | 实际值 |
|---|---:|
| 最大 collocation RMS | 9.902730133880437e-07 |
| metric_l1 | 1.922357432294268e-08 |
| flow_defect | 2.3759624134162797e-08 |
| Darboux l1 | 5.7333593546182935e-05 |
| physical BC max | 3.380797256861475e-19 |
| 曲率采样最大值 | 7.644144412833039 |
| delta | 0.0641435131224618 |

DomainNewton 为 calls=5、accepted_steps=9、merit 拒绝=2、domain 拒绝=0、no_step=0、最小 alpha=0.5。物理 c6,...,c24 为

    [5.0718763578483217e-05, -1.6315816447078136e-06, 2.5149996544378052e-08, 3.5764858515911243e-09, 4.4771871841168306e-11, -1.984965149367476e-12, -6.627889361400373e-12]

| 返回文件 | SHA256 |
|---|---|
| raw `inner-00.npz` | `0fae2cca1511135acf13ac2aa416b162caf1045cdcf29e284d132e8cb20cc1b3` |
| `physical.npz` | `da3a9dbc68a76d21ba49732509d9502265a778d2b797a8a686c4e9813fe258a8` |
| `checkpoint.json.gz` | `e1d6f4e35183dae1bf4ab9f1a4780d58b3f33516706bd04a6a3280d7d0798795` |
| `run.json` | `e43d1e6dd58476f48f6a541114001d649983c733d139d884294087e180ef5424` |
