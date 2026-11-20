# m3：新 g 宽窗 M8 实际全场谱与完整 lift 的 M16 返回

维护会话：Astra-held10-1b6d88ec-20261120。

本条只读诊断前条 lambda=.002、tau=1、S=.5、b=.2 的实际 M8 场。
其 metric_l1=3.193207022812077e-5 已未门。下面的独立 operator 与
Frenet 残差均取这份完整 physical.npz，保 exact lift、物理坐标、
新 profile 和固定 mean512 规则，未重复求解原 M8，也没有真尾。

## 1. 真正 operator 缺口

1392 个同一物理 s 断面，角网格分别 512、1024，均实际得到

    max ||g^(-1/2) (F*g_E-g) g^(-1/2)||op
       = 2.686827735609576e-5.

峰在 s=.15854560225148653、psi=theta=pi，其对称相对 metric
矩阵的三个分量 (ss,st,tt) 为

    [-2.686827735609576e-5,
      7.768239327371685e-17,
     -8.638444584097016e-7].

两个角网格共同节点的三个分量差均为 0。这一实际节点本身已经
超过 1e-6，所以当前场的缺口不能归结为 FFT l1 上界保守。
ss、st、tt 的原有限 FFT l1 分别为
3.1932070282820225e-5、9.834123544808857e-6、
2.656926310440995e-6。此处没有宣称 M8 整个函数空间不可能达标。

这仍是数值原 profile 与声明的 mean512 规则下的有限扫描；没有
连续角度、径向区间或真实积分 reference g 的完整误差证书。

## 2. 原投影补空间中的主缺陷

同一实际场的全未投影 Frenet 残差最大值为
.0002575654559151586，512/1024 两个网格得到相同值。
原 native 投影内的径向残差最大值仅 7.187681769761972e-8，
扣除该原投影后的余部最大值为 .00025758860809373986。
原投影分解按原 basis 作出，没有把 physical theta 的频段误认成
求解器 psi 的表示空间。

| psi 笛卡尔频壳 | 残差向量系数有限 l1 最大值 |
|---|---:|
| 0 | 2.509436151117918e-13 |
| 1–3 | 8.995415539717837e-8 |
| 4–25 | 3.661095387135273e-8 |
| 26–50 | .0005432218106737324 |
| 51–100 | .00012881215611654204 |
| 101–200 | 4.539776884530411e-6 |
| 201–512 | 1.3769373341667835e-7 |

最大向量系数包含 psi=±26、±28、±32、±34；它们在原 M8 的
笛卡尔表示范围外。物理 theta 频壳也独立计算，其中 26–50 的
有限 l1 最大值为 .00048432608185327214，51–96 为
.00011017542962612516；它和 psi 表不同，不能混用。

Rz 的零模最大值为 1.2047654540658925e-15，固定 mean512 与
评价网格均值的差不超过 1.2212453270876722e-15。当前主残差没有
来自另一个自由均值参数。切向 C² 直接求导诊断的
|T·R_theta| 最大值为 6.290310907081098e-5，与 DFT 角导数的
差不超过 3.26366414663405e-9；两者仍都是有限数值诊断。

## 3. 完整可复现审计命令

沿用前条的 REPO、WORK、TOPIC：

```bash
FIELD="$WORK/newg-wide-lambda0p002-tau1-linear"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_m3/audit_full_relative_metric.py" \
  --model-adapter "$TOPIC/scripts/resume_m3/actual_m3_metric_model.py" \
  --model-config "$FIELD/run.json" --physical "$FIELD/physical.npz" \
  --mean-nodes 512 --angular 512 1024 \
  --out "$WORK/newg-wide-lambda0p002-metric-audit.json"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_n4/audit_full_frenet_residual.py" \
  --model-adapter "$TOPIC/scripts/resume_m3/actual_m3_metric_model.py" \
  --model-config "$FIELD/run.json" --physical "$FIELD/physical.npz" \
  --metric-loader "$TOPIC/scripts/resume_m3/audit_full_relative_metric.py" \
  --mean-nodes 512 --angular 512 1024 --physical-cutoff 96 --batch 8 \
  --out "$WORK/newg-wide-lambda0p002-full-residual.json"
```

两项实际 exit 0。相对 metric 审计源 SHA256 为
`e128f3a5eed4b38ea1a97eb26cba9560ab254127d06884a1a976a72f780c36aa`；
全 Frenet 源为
`cd9812395eb8bfd55bb02c558255fae7c2e26283eb166778565f9a92f31010c6`。
两个实际输出记录 SHA256 分别为
`1aebba5e74d67da00ff1862a6424cb8b782e6e75897d97f739d4fa39ece6f69c`、
`e4514a3325cb93acdf6f67e60d25e59cd62a9d1b6a5e0d3ab31d2f50ee75b48f`。

## 4. 实际 M8→M16 完整场转移

上述谱支持试 M16，以覆盖主导的 psi=26–49 部分；这只是选择离散
规模的依据，不是 M16 将达标的保证。原 M8 未合格场只作初猜。
先按已有 R48 恒等式转移完整参考场：

    Y_new = embed(Y_old) + a*chi*(I_new-embed(I_old)).

补偿系数为 1，核心 lambda=.002 不能再乘进去。原 q、delta 增量、
低七个物理 support 控制和完整角坐标均保留，新增控制初值为 0。

```bash
env -u LD_PRELOAD -u LD_LIBRARY_PATH \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_m3/prepare_lifted_mode_restart.py" \
  --source-run "$FIELD/run.json" --tail-config "$WORK/bootstrap/q060-tail.json" \
  --modes 16 --angular 512 --check-angular 2048 \
  --outdir "$WORK/newg-wide-lambda0p002-m16-transfer"
```

实际 exit 0。原线性 port 以同一物理尾参数重建为 16 模，数值
quadrature=128→256，保原 N>4*M*spacing 条件；物理参数逐项相同。
102 个 s 点、2048 角点的完整参考六个 jet 差分别不超过

    position 3.245e-16, psi 3.493e-16, psi_psi 7.773e-16,
    s 2.702e-16, s_psi 6.002e-16, s_s 4.108e-15,
    rho 0.

这是连续转移公式的有限数值校验；输出仅存节点初猜，新 BVP 插值
本身尚未与原 quintic 逐点恒等。没有把补零 y 误标成完整 lift 转移。

| 转移对象 | SHA256 |
|---|---|
| 转移脚本 | `c1f7741ee1882bd8413a04f280df759da4165792291f5419b243b7deed2882fe` |
| `initial.npz` | `d8cc629ab994e617758fe1ca86593efa270b99a56e580647651780d057f09842` |
| `linear-port.json` | `b87fa615602aa01382a09f2073e303c38ebd3a75f4cd7f31c9867c62be1189f6` |
| `tail-settings.json` | `bc3172f2bee245a7e32eb698166beb2c44ff48322cfe96b5efdebec8200bb201` |
| `transfer.json` | `22fea40ed13a35104d0dbd157ade252e780febac0c72755d71c834e43cc4b09c` |

## 5. 原 M16 设计求解的实际命令

从上述 initial.npz 实际启动原 portable driver，source/profile/桥/
chart/core module/config 与 M8 相同，只采用新 16 模 port、M=16、
angular=512。其余仍是 tol=1e-6、bc_tol=1e-7、physical_bc_tol=2e-9、
max_nodes=6000、audit-angular 请求 512。原审计会按 M 自行选择满足
最低要求的实际角数，最终返回中必须据实记录；后验比较均值仍明确。

实际输出目录为 `m3-work/newg-wide-lambda0p002-m16-linear`，同名
`.log` 保存 stdout。此时 delta 和全部 support 控制继续是设计
未知量，所以没有声称冻结 g/c 的收敛证明。M8 的七控制正性盒不
自动覆盖新八个自由高模。实际调用为：

```bash
env -u LD_PRELOAD -u LD_LIBRARY_PATH \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_m3/portable_prefix_continue.py" \
  --source-topic "$WORK/multistage-source-v2" \
  --short-bridge "$WORK/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py" \
  --profile "$WORK/multistage-linear-root-profile.json" \
  --chart "$WORK/bootstrap/reference/chart.json" \
  --port "$WORK/newg-wide-lambda0p002-m16-transfer/linear-port.json" \
  --raw-restart "$WORK/newg-wide-lambda0p002-m16-transfer/initial.npz" \
  --core-module "$TOPIC/scripts/resume_m3/material_support_factory.py" \
  --core-config "$TOPIC/scripts/resume_m3/multistage_wide_circle_lambda0p002.json" \
  --amplitude .06 --warp-reference .06 --modes 16 --angular 512 \
  --audit-angular 512 --nodes 401 --max-nodes 6000 \
  --tol 1e-6 --bc-tol 1e-7 --physical-bc-tol 2e-9 \
  --outdir "$WORK/newg-wide-lambda0p002-m16-linear" \
  > "$WORK/newg-wide-lambda0p002-m16-linear.log" 2>&1
```

## 6. M16 已真正返回，metric 下降但仍未门

实际 exit 0，2 个网格、628 点，约 60.99 秒。DomainNewton 共
3 个完整 alpha=1 接受步，0 domain/merit 拒绝、0 no_step。

| 指标 | 实际值 |
|---|---:|
| 最大 collocation RMS | 9.927099309991536e-7 |
| 原 metric_l1 | 4.272493000646559e-6 |
| flow_defect | 6.044523746326128e-5 |
| Darboux l1 | .009928837443327974 |
| 原十六条 linear DN physical BC max | 2.816603799153149e-19 |
| delta | .06413464053002277 |
| 原 metric 审计实际角数 | 784 |
| 原 metric 审计 s 点数 | 1404 |

metric_l1 虽由 M8 的 3.1932e-5 降到 4.2725e-6，仍高于 1e-6；
本次不是合格前缀，也没有真尾验收。控制与 delta 都曾重解，不能
把这个下降直接称为固定同一物理 g/core 的收敛率。

实际 c6,...,c48 为

    [.0005029999361611398, -.000040759505922218074,
     -.0000017003787133407946, .0000005688419711169701,
     .000001125411763795071, -.0000001552480772574999,
     -.0000003723243500686583, .0000001720664157274996,
     .00000011487256967115228, -.00000009937354506064637,
     -.00000009561349253659195, .0000004868195373976758,
     .00000005605570564160573, -.00000007837093641943915,
     -.000000020453371530180812].

| 实际返回对象 | SHA256 |
|---|---|
| raw `inner-00.npz` | `9086f6e121f560c4e20a5a69e50a0a0a7397eb0faf349879e774277d690ddbc6` |
| `physical.npz` | `9cceea7db560886a81c60d0cf39f838356725bf007f4e2d61c51ea0356160a60` |
| `run.json` | `b769d61e6d94883583c0a9e629972986c8de2af02c7c237ad574f49e22973a0e` |

后续固定 mean512 的实际 operator/频壳读取这份新 M16 场；不会用
M8 的谱替它预签更高 M，也不增加 lambda 或放松任一门。
