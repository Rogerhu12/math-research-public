# m3：新 g 宽窗 lambda=.002、tau=1 的 M8 实际终态

维护会话：Astra-held10-1b6d88ec-20261120。

从新多段 profile 的真实 lambda=0 完整 lift 场续接 lambda=.002，
原八条 linear DN 的有限 Newton 真正收敛，但完整原 metric_l1 为
3.193207022812077e-5，超过 1e-6。因此这份场不是合格的正 lambda
前缀，未进入 accepted true-DN 入口，没有新增真尾结果。

## 1. 本次实际输入和命令

新参数文件为 `scripts/resume_m3/multistage_wide_circle_lambda0p002.json`，
SHA256 为
`5ed9c06fd52c2162304560722f71751287c81497cd15967820e1f223c7283223`。
只有核心 lambda 从 0 变成 .002；tau=1、S=.5、b=.2、target k=.2、
quadrature_order=12、integration_cells=64、transition_cells=24。
lambda<1 时保护窗内仍有 (1-lambda)*kappa_old 项，不能把目标 k
误读成当前窗内已经是曲率 .2 的准确圆片。

源与原数值门和前条 lambda=0 note 完全一致。正 lambda 使用已发布的
完整解析核心参数 jet；对应 `analytic_adaptive_core_jac.py` SHA256 为
`da6690d9f11eac38cec0acee31aa07555a8d1ddd81c1b24997db0421ea19e431`。
本次完整执行命令为：

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
  --raw-restart "$WORK/newg-wide-lambda0-tau1-linear/inner-00.npz" \
  --core-module "$TOPIC/scripts/resume_m3/material_support_factory.py" \
  --core-config "$TOPIC/scripts/resume_m3/multistage_wide_circle_lambda0p002.json" \
  --amplitude .06 --warp-reference .06 --modes 8 \
  --angular 256 --audit-angular 512 --nodes 401 --max-nodes 6000 \
  --tol 1e-6 --bc-tol 1e-7 --physical-bc-tol 2e-9 \
  --outdir "$WORK/newg-wide-lambda0p002-tau1-linear" \
  > "$WORK/newg-wide-lambda0p002-tau1-linear.log" 2>&1
```

exact lift 的补偿系数仍为 1，不乘 .002；delta 与七个物理 support
控制仍为设计未知量，不标作冻结 g 的加密或同一个 g 的族。

## 2. 原始数值返回

实际 exit 0，1 个网格、622 点，约 16.13 秒。DomainNewton 有
3 次完整 alpha=1 接受步，0 domain 拒绝、0 merit 拒绝、0 no_step。
因此本次实际问题不是域门阻塞或冷初始化失败。

| 指标 | 实际值 |
|---|---:|
| 最大 collocation RMS | 9.927135461598547e-7 |
| 原 metric_l1 | 3.193207022812077e-5 |
| flow_defect | .0002575654559151556 |
| Cartesian Darboux l1 | .023210656259261726 |
| 原 linear DN physical BC max | 1.73570897874993e-12 |
| delta | .06413463267681063 |
| Frenet root 最小采样值 | .00253054049774859 |
| 曲率采样最大值 | 8.90688688182976 |
| 核心补偿 beta | .7287120748236384 |

返回的原 normal-angle support 输入控制 c6,...,c24 为

    [.0005029953543232228, -.000040759388516936315,
     -.0000018318156103368295, .0000010546769062594273,
     .0000014808409259135354, .00000031377013311412296,
     .0000010125108864082048].

这里没有拿归一化 Newton p 的高位大数冒充物理幅度。以上实际控制
都在前条独立 M8 粗盒内，因此其 tau=1 的核心正性结论仍适用；
这个盒不自动包括将来 M>8 的新控制。核心正性没有支付本次已超门
的完整 metric，也不成为几何存在或全角曲率证明。

| 只读保存对象 | SHA256 |
|---|---|
| 输入 lambda=0 raw | `fdd146eb4e7b343669a61e50a3c3f5b489a1e3c6c7e9ca5a74cf6ec3a0fa43c9` |
| 本次 raw `inner-00.npz` | `cb374138e17075b20715a754f9a6c142475e5e6f3a1e4811b398637f5300593a` |
| 本次 `physical.npz` | `a0d00429c4a6aac10165b07a4d8048dfe08aad4d3afda0dcbad7c4b30ab5bd5f` |
| 本次 `run.json` | `be83041236a3832194d52aae6b21569e2e463b67548e4b0b0b1b8cd683f323a1` |

完整数组只留 scratch。后续对这同一实际 quintic 场、同一完整 lift、
同一固定 mean512 规则作真实 relative-operator 和未投影 Frenet
残差频壳诊断，不把核心投影尾本身当作 metric 下界，不改变审计门。
只有新的实际谱信息才用于选择更高 M；本条不预报其能够收敛。
