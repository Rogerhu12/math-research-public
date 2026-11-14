# M14 紧配点容差因果试验：残差下降而 metric 未改善

2026-11-09，`/root/coupled_prefix`。状态：**数值因果对照；该次进程正常结束，但 BVP `solver_success=False`，且使用冻结仿射 DN，不是真联解。** 该结果不支持把 M14 的 metric 非单调主要归因于原配点容差。它不证明任意更紧容差都无效，也不是不存在性结论。

## 1. 保持什么、改变什么

输入为已经完成的真联解
`db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q256-outer.json.gz`，最终真实尾响应为 `_tail_0004`。

固定同一物理 profile/chart、全部尾背景参数、M14、前缀角积分512，以及已求得的真实尾 DN 值和导数。仅将前缀 `solve_bvp` 请求容差从 $2\times10^{-9}$ 收紧到 $10^{-11}$，保留原2633节点初猜。为避免前一次已观察到的内存风险，本次设资源上限6500节点；没有改变方程或 guard。

这次把尾端函数冻结为原真实 DN 的仿射线性化，目的是隔离前缀配点误差。输出显式保留 `actual_nonlinear_tail=False`、`frozen_affine_dn=True`，不能冒称重新求得了完整非线性尾。

## 2. 真实退出及数据

工具 session98493 正常 exit0。BVP 在第二轮的5890节点上达到未加权最大相对配点残差

$$
1.535762812063138\times10^{-10},
$$

但要求再加5841节点，超过6500资源上限，因此 `solver_success=False`，原始消息为 `The maximum number of mesh nodes is exceeded.`。不能把进程 exit0 当作 BVP 达到 $10^{-11}$。

输出 stem：`db6f-prefix-flat-v17v18-m14-affine-tol1e11-cap6500`。CP SHA256 为

`d8f2385353f39a9af02fccc4d5b03875f4eb04a5f860b2c10c2905fe556d1cee`。

元数据及三片精确系数均已保存；最大 gzip 系数片4,098,101字节，未作系数舍入。reproduction SHA256 为
`280a710ed0c34a8de0572ac834e3d47efb9b09b687c0f21d90e78272a7ae45c0`。
对应脚本为 `scripts/db6f-prefix-affine-replay.py`；所有参数、输入及源码绑定见 reproduction。

## 3. 实际对照

| 项目 | 原完整 M14 真联解 | 本次冻结 DN 的细网格 |
|---|---:|---:|
| 节点数 | 2633 | 5890 |
| 原未加权配点 RMS 最大值 | $1.997899817185576\times10^{-9}$ | $1.535762812063138\times10^{-10}$ |
| 前缀实际 metric 采样/FFT $\ell^1$ 指标 | $7.946154953624402\times10^{-8}$ | $8.00329073343333\times10^{-8}$ |
| 未投影速度与保留速度之差 | $9.52537\times10^{-7}$ | $9.59483418634281\times10^{-7}$ |
| 最高中心支持系数 $c_{14}$ | $1.189214893276175\times10^{-8}$ | $1.1977853720071568\times10^{-8}$ |
| 求得的主支持幅度 | $.09999976437833741$ | $.09999976413133652$ |

本次实际 metric 审计使用11,906个经向点及1024角点，包括保存节点/中点与常规点。它是有限采样与角 FFT 的数值诊断，不替代连续 metric 证书。

未加权配点残差下降约13倍，但 metric 和速度投影缺陷均约增0.7%，最高中心系数也约增0.72%。cut-height 相对冻结 DN 基点的最大变化仅 $2.0222576868275666\times10^{-12}$；这说明该试验确实只做了很小的前缀调整，但没有严格支付其相对于真实 DN 的非线性误差。

## 4. 再看谱残差

独立复用既有 `db6f-prefix-collocation-spectrum.py`，从保存节点与原 RHS 重建计算坐标中的三次配点插值，报告为
`db6f-prefix-collocation-spectrum-m14-tight-cap6500.json`。

- 重建未加权最大 RMS 为 $1.5356735890849312\times10^{-10}$，与求解器记录相差约 $8.93\times10^{-15}$；物理节点/插值重建的舍入差在这个尺度不能称逐位相同。
- 假设未知量以 $1+(3j)^2$ 加权的同状态诊断范数由原 $4.0121171166\times10^{-7}$ 降至 $5.015752065029181\times10^{-8}$，约降8倍。
- 新加权残差仍以 R42 为最大，约 $4.790284994293887\times10^{-8}$；原未加权最大分量仍是 Z3、R3 与 R0。

因此即使高模加权残差已明显降低，当前实际 metric 非单调仍没有被消除。**不据此再启动加权 BVP，也不把更改范数或放松接受目标当作 G5 的支付。** 继续观察增加 Fourier 模式后的实际 E/F/G 及分支连续性更有针对性。

## 5. 与 M16 路径的衔接

旧直接M14→M16首个真实尾 warm 的最近三轮归一残差为

$$
10.69543288432175\to10.122768536092874\to10.104461387631748.
$$

这是连续强阻尼的实际证据。经主会话协调，该路径以 Ctrl-C 中断，工具 exit1；没有产生第一份 M16 真实尾响应，也没有保存当时仍仅在旧 worker 内存中的 Newton 迭代态。全部输入、已加载历史源快照、最终 trace/log 和该限制保存在 `db6f-prefix-flat-v17v18-fixed-m16-d12-p8-s64-q256-outer-from14-interrupted.json`，不得把它写成收敛或数学失败。

下一条路径从原完整 M14 经 M15 单步升频，保持同一 g，启用原子保存的明确 UNCONVERGED 迭代检查点；最终仍检查原方程及 N512 的真实 DN。当前新增频率补零的 cut-height 是中间边值，不能仅凭这类 warm 问题难解就判定完整耦合不存在。

## 6. 重跑命令

在仓库根目录运行，输出使用新的 stem：

```bash
python -u topics/visible-flexible-closed-surface/scripts/db6f-prefix-affine-replay.py \
  --source-root topics/visible-flexible-closed-surface/repro/source-root \
  --checkpoint topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q256-outer.json.gz \
  --linear-port topics/visible-flexible-closed-surface/notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json \
  --out-prefix /tmp/m14-tight-independent \
  --tol 1e-11 --max-nodes 6500
```

本次失败状态和前次内存中断状态均保留，不覆盖，不以新的标签替换。
