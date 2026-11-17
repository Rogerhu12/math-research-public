# best4 物理角 M64：完整 QR 有限预算终态未接受

维护：Astra-larger-parallel-16f63c8b-20261117 / numerical_route。

## 有限终态

原 best4 固定背景上，保留完整 $\rho_{112}$、取物理状态 $M=64,N=2048$、
浅端幅度 $\lambda=.001$ 的完整 weighted BVP，在原 `max_nodes=14000`
预算内明确失败。退出 `success=false,status=1`；不是进程被杀或仅等待中的检查点。

| 网格轮次 | 实际节点 | collocation 最大 RMS | 边界最大残差 | 请求新增节点 |
|---|---:|---:|---:|---:|
| 1 | 4853 | $1.26\times10^{-3}$ | $4.16\times10^{-17}$ | 1456 |
| 2 | 6309 | $1.82\times10^{-3}$ | $4.16\times10^{-17}$ | 3471 |
| 3 | 9780 | $.01608216732464$ | $9.2616277\times10^{-17}$ | 8755，超预算 |

最后完整 Newton 点被保留；后续加密将需要 18535 节点，未执行。
实际耗时 5812.82 秒，19 次完整全局 Jacobian 因子，日志最大 RSS 为 1431132 KiB。
`counts.jac=8516` 是分块局部 Jacobian 回调次数，不是 8516 次全局因子。
没有扩大预算、改门或把小 BC 残差当作完整方程通过。

完整 129 条 ODE 与全部 129 个边界条件均保留；仅将浅端 $M$ 条高度条件及一个均值条件
置于左侧，以 `left_count=65` 使用仓库已有 separated QR。
`--allow-height-turn` 只允许高度斜率的符号分支扩展，仍检查完整 $S,D,L,N>0$。
本次终态采样实际 $1+K\ge .52713$，所以没有用到跨零高度斜率。

终态是**未接受场**。每个最终胞元的两个端点及三个四分点、配 $N=2048$ 的诊断包括：

- 最大字面 weighted mean：$3.34963\times10^{-7}$；
- 完整物理 $r$ 方向 $P$ 残差 $1.61918\times10^{-4}$，完整 $K$ 残差 $30.37086887$；
- 插值系数相对径向残差最大 $.0333954$；
- $\min D=.99749977$、$\min S=.99999968$、$\min L=.28414529$、$\min N=.99927572$；
- $\max|P|=.11260571$、$\max|K|=.47286993$。

这些采样不是连续区间或几何证书。没有把该终态送作新接受几何父，也没有新 nonlinear DN。
失败只针对本次固定输入、初始化和有限预算。
旧 best4 强 $\lambda=1$ 接合另已由 R633 的长度条件排除；本次弱场失败不是那个严格障碍的证明，
也没有启动同一旧强候选的更大预算追算。

## 固定输入与复现

使用已接受材料 $M=8,\lambda=.001$ 场，经完整 $\theta(\phi)$ 变换和物理 Fourier 投影
作为**未接受初猜**；目标始终是实际物理 trace、全 $\rho_{112}$ 和本次实频率深列。
三个初始化采样点的投影差为 $P_{\rm tilde}$ 的 $4.17438\times10^{-6}$、
$K$ 的 $3.19492\times10^{-7}$；没有将跨角投影标成同一接受解。

输入 SHA256：

- `parallel-best4-background.json`：`487373a8445674658cb36ddbd20445e774612269720f58c0e6db492f38c24e15`。
- `parallel-trace0992-physical-m112.json`：`36688dcba2bacef79d497b92a118b58141447f2630a9c735e75a63cf4aab719b`。
- `parallel-best4-physical-m64-columns.json`：`459233720da384d12be4e148877cbe8769d8704eb848cc633b6abb65e1daeff6`。
- `parallel-best4-material-scale1e3.json.gz`：`a2d689c26cbe5309a61b9ab5de6fcb5b1e18ef703b28b160c01e7723ca35e210`。

前三输入/材料父的定义沿用已刊 best4 和物理角续接记录；深列为同一来源的有限 far 模型，
不声称非线性无限尾 DN。实际物理高度均值 anchor 是 `.9703876955889461`。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-larger-amplitude/scripts/parallel_20261117_weighted_tail_qr.py \
  --background /scratch/parallel-best4-background.json \
  --trace /scratch/parallel-trace0992-physical-m112.json \
  --deep-columns /scratch/parallel-best4-physical-m64-columns.json \
  --material-input /scratch/parallel-best4-material-scale1e3.json.gz \
  --modes 64 --angles 2048 --scale .001 --fast-jacobian --allow-height-turn \
  --tol 1e-6 --max-nodes 14000 --batch 32 \
  --out /scratch/parallel-best4-weighted-m64-scale1e3.json.gz
```

`/scratch` 替换为实际仓库外目录；其余使用脚本默认 `source-index`、`mesh-stride=1`。
新 runner 源 SHA256：`14af29744d1941caec5c3c0225d57319bc6cd7f9026dd7a4d969044fcb091303`。
完整输出保存了启动时所有依赖 SHA；其中安全 Newton 为
`8b6960119cd978bb7e6208e87934d68f337b9ba5679314c7c048b6cf0cac80ae`，
原 DiskQR 为 `c76bde190ff67a9e148d230c8e5e7d7a7899324c055e67faac6679b8fba10e39`。

最终未接受输出 `parallel-best4-weighted-m64-scale1e3.json.gz`：
`b6eedace6828d1fb171dd48c0d3923539ec6b16d55fac5d5f79a2d6a2effa742`。
完整日志 `parallel-best4-weighted-m64-scale1e3.log`：
`00a5d04bc7e0ca9b53e2e0b7f97dce688f0ea775c7143073b17f52fe3e605226`。
状态、检查点和日志保留在仓库外；只刊最小求解源与这条有限负结论。
