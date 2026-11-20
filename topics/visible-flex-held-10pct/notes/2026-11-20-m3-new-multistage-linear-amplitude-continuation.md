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

## q=.030：原过程中暂时停滞后仍真正通过

Q=.03，PREVIOUS=newg-q020-linear，TAG=newg-q030-linear。
上一 checkpoint SHA256 为
`e1d6f4e35183dae1bf4ab9f1a4780d58b3f33516706bd04a6a3280d7d0798795`。
实际 exit 0，solver_success=true，3260 点，13 个网格，约 539.90 秒。
第4至12网格曾在 RMS 约 1.65e-6 至 1.90e-6 上细分而近乎停滞；
没有提前将它判成失败、重启或修改节点/误差门。第13网格原程序
自行返回合格解，因此没有调用备用诊断或暖重采样入口。

| 指标 | 实际值 |
|---|---:|
| 最大 collocation RMS | 9.984644275882486e-07 |
| metric_l1 | 2.947089136789924e-08 |
| flow_defect | 3.569610216610256e-08 |
| Darboux l1 | 0.00013103869600281854 |
| physical BC max | 1.4532768551358674e-16 |
| 曲率采样最大值 | 7.950516416986867 |
| delta | 0.06414241148929038 |

DomainNewton 为 calls=13、accepted_steps=12、merit 拒绝=200、domain 拒绝=0、no_step=8、最小 alpha=7.62939453125e-06。这些聚合计数
不改变实际终态已经通过的事实。物理 c6,...,c24 为

    [0.00011448040791908074, -5.5270311133079374e-06, 1.282850073708944e-07, 2.729718229010271e-08, 5.138239656005629e-10, -2.7298947073734487e-11, -4.0536269649923596e-11]

| 返回文件 | SHA256 |
|---|---|
| raw `inner-00.npz` | `242d3c36a10390ce8c7297302f7f03c03ad7fb72dc51a8b95d2051706ca3adb1` |
| `physical.npz` | `80582bd3dc0f836b9434bb9c907eeca89378c00b9ad899036b8d226a9f09aa00` |
| `checkpoint.json.gz` | `201fa920349aa4aeef9cae6c722000b6d05b8ee52bdf0e4e6a6a87ae455d587c` |
| `run.json` | `7fa5053a7b772f6b244f338658bb1db69e3ab5ed81e4ec90afd8b140d45e5325` |

## q=.040：从 q=.030 真 checkpoint 续算

Q=.04，PREVIOUS=newg-q030-linear，TAG=newg-q040-linear。
上一 checkpoint SHA256 为
`201fa920349aa4aeef9cae6c722000b6d05b8ee52bdf0e4e6a6a87ae455d587c`。
实际 exit 0，solver_success=true，850 点，5 个网格，约 225.38 秒。

| 指标 | 实际值 |
|---|---:|
| 最大 collocation RMS | 9.841842430634182e-07 |
| metric_l1 | 4.0158828797717e-08 |
| flow_defect | 6.99236667881285e-08 |
| Darboux l1 | 0.0009147135708933149 |
| physical BC max | 1.0246677519924534e-16 |
| 曲率采样最大值 | 8.26198079533171 |
| delta | 0.06414070389056908 |

DomainNewton 为 calls=5、accepted_steps=14、merit 拒绝=87、domain 拒绝=0、no_step=1、最小 alpha=3.0517578125e-05。物理 c6,...,c24 为

    [0.0002044362250257394, -1.316983607454654e-05, 4.0979884200357184e-07, 1.1596322679808282e-07, 2.9787153822093634e-09, -7.284483901479636e-11, 1.618061718353057e-10]

| 返回文件 | SHA256 |
|---|---|
| raw `inner-00.npz` | `f20844e478426d98df8bac1837816681656c8a9640a3eff88e870d597acdff4d` |
| `physical.npz` | `deddbd7094145544fb5e42b80300027c2d7c816b636c9172a828f7013c36e7e4` |
| `checkpoint.json.gz` | `4e3c388ea6c2f7d404c3df94d325c9ce2a0bfb7829bdf01ff107951e14466776` |
| `run.json` | `439b61026edee6702513228e1c3dd337af28e7329fa64b16540cff73f97e481c` |

## q=.050：从 q=.040 真 checkpoint 续算

Q=.05，PREVIOUS=newg-q040-linear，TAG=newg-q050-linear。
上一 checkpoint SHA256 为
`4e3c388ea6c2f7d404c3df94d325c9ce2a0bfb7829bdf01ff107951e14466776`。
实际 exit 0，solver_success=true，903 点，5 个网格，约 71.33 秒。

| 指标 | 实际值 |
|---|---:|
| 最大 collocation RMS | 9.973606912128662e-07 |
| metric_l1 | 7.910156737892718e-08 |
| flow_defect | 4.590147335650989e-07 |
| Darboux l1 | 0.0010892670514440596 |
| physical BC max | 1.4520699626774153e-16 |
| 曲率采样最大值 | 8.578556472634498 |
| delta | 0.0641382174100334 |

DomainNewton 为 calls=5、accepted_steps=7、merit 拒绝=22、domain 拒绝=0、no_step=1、最小 alpha=0.5。物理 c6,...,c24 为

    [0.00032130266107415915, -2.5898001260616118e-05, 1.0143677529736615e-06, 3.584958430248947e-07, 1.199016259534776e-08, 6.861664543747142e-11, -1.5760476813986656e-09]

| 返回文件 | SHA256 |
|---|---|
| raw `inner-00.npz` | `e24f16260aa7d4c3d86df8ffd97bbf2422f2fc1951250c3899cfa7a04f918d1c` |
| `physical.npz` | `9726c59db6ed27fed83569750a761afe1c6a497d3fd88d7d95fac07bff6ae750` |
| `checkpoint.json.gz` | `ade5865bc8fdc7e22a29fef229cb6ee75d648e732f3cd7f5d68cae874851e62d` |
| `run.json` | `036bdff387b0d75c0571896225033ff171b2b678f255eda32d330ca4df4e4052` |

## q=.060：新 g 的完整幅度暖锚

Q=.06，PREVIOUS=newg-q050-linear，TAG=newg-q060-linear。
上一 checkpoint SHA256 为
`ade5865bc8fdc7e22a29fef229cb6ee75d648e732f3cd7f5d68cae874851e62d`。
实际 exit 0，solver_success=true，622 点，5 个网格，约 98.45 秒。

| 指标 | 实际值 |
|---|---:|
| 最大 collocation RMS | 9.912228419659946e-07 |
| metric_l1 | 4.0915716285294446e-07 |
| flow_defect | 2.2710106762803862e-06 |
| Darboux l1 | 0.0006569682836882621 |
| physical BC max | 1.0186975093434908e-16 |
| 曲率采样最大值 | 8.900697822270415 |
| delta | 0.06413471898892625 |

DomainNewton 为 calls=5、accepted_steps=12、merit 拒绝=33、domain 拒绝=0、no_step=1、最小 alpha=0.03125。物理 c6,...,c24 为

    [0.0004660413545445234, -4.513133403089269e-05, 2.1365381257287638e-06, 9.165669175004054e-07, 4.3695810197724855e-08, 7.099644019307281e-09, 1.2891436997542135e-08]

| 返回文件 | SHA256 |
|---|---|
| raw `inner-00.npz` | `0ab581024f94d79edc6278683f5ab7471e88af5ea509cf40aa6e2f0225fca215` |
| `physical.npz` | `f36f099ece34fff885539142991fa7fdda8132ee582181973a5a153c279c09e3` |
| `checkpoint.json.gz` | `4ebecc79f0401947dd76800ac2957cdf029ffdb6236fc2d67e9e9adaa4f7b35f` |
| `run.json` | `104f6cf51469874e7f9a49bff72896e76aa9394d7b070107bc16a16fae4445fd` |

这里原 metric_l1 门通过，但 flow_defect=2.27101e-6 单列为其实际值，
没有把它改名成更强的全角流方程门通过。c9、c12 等也已超出旧 R53
控制盒；旧盒的具体曲率/相位数字不能移用。后续新宽窗材料入口
设 S=.5、b=.2、目标 k=.2，先在 lambda=0、tau=1 复接完整精确
lift 模型，再从小正 lambda 求解；不经过未经耗尽门支付的
lambda=1、tau=0 准确圆片。该后续过程独立记录，本幅度表不预报其成功。
