# 动态零模的第一个完整非零有限 tail BVP

会话 `Astra-larger-parallel-16f63c8b-20261117`，2026-11-17。本文是新的数值证据，不登记闭面、全时段、reach 或旧 full112 通过。完整离散均值公式和证明在 [动态均值说明](2026-11-17-parallel-model-dynamic-mean-bvp.md)，已有 R64/R69/R75 的连续恒等式不重报。

## 固定的有限问题

保留 `P=sum p_j sin(2j theta)`、`K=c+sum k_j cos(2j theta)` 的全部 `2M+1` 个未知量；本次 `M=8,N=256`，17 维。第一行与完整有理 K 方程按有限角采样投影。将 K 零模速度设为字面 sampled mean 的隐式导数，取 `chi=0`；每个 RHS 不再解非线性均值根。浅端给 M 行 P、1 行真实离散均值，深端给 M 行 homogeneous 理想线性稳定边界。没有删除任何 K 非均值模，也不把深线性边界称为无限非线性 DN。

背景从旧 smallcut30 参数出发，实际恢复 `closing_weighted_tail.mjs`、`closing_recalibrated_tail.mjs`、验证 loader、9 个 blob 校验依赖及其清单，共 **13 文件、88,053 bytes**，均在仓库外。配置文件是
`computations/alternative-neck-provider-smallcut30-port32-r2048.json`。导出 source 前四个 cell，每个原 segment 64 份，得到 2340 个标量 jet 记录，合并重复端点后用它们定义固定的 C¹ cubic-Hermite `log w(r)`。

这是明确另名的固定近似背景 `g_h=(1+w_h²)dr²+r²dtheta²`，不是把它冒称为原 stored metric。所有本节同 g 比较都保持这份 background JSON SHA 不变。这里 r 是物理参考半径，不是距 cuff。

| 项目 | 数值 |
|---|---:|
| 深端 r | 0.06863598072661437 |
| 浅端 r | 0.30000000000000004 |
| 浅端 w | 0.08 |
| 深端 log w | -10.07660943000742 |
| 浅端 P 的第一正弦系数 | 0.001 |
| 其余浅端 P 系数 | 0 |

浅端对应高度第一 cosine 系数 `-r w P_1/2=-1.2e-5`，所以这一步是非零但小振幅的 tail 求解。

## 两次真正接受的 BVP

第一次用物理 r 坐标。第二次保持 **同一 `g_h`**，仅用以原标量样点索引构造的单调 PCHIP `r(x)` 作数值坐标；所有 RHS 同乘 `r_x`，读出明确除回 `r_x`。这张 C¹ 坐标图只是求解工具，不被用来宣称最终表面有 C² 参数化。

| 项目 | 物理 r | 数值索引 x |
|---|---:|---:|
| 节点数 | 5464 | 4248 |
| 自适应轮数 | 16 | 10 |
| 秒 | 167.7827 | 75.9712 |
| 所用坐标下 collocation RMS | 9.99613883662095e-7 | 9.997185102184373e-7 |
| 边界残差 | 8.470329472543003e-21 | 2.5622746654442585e-20 |
| sampled mean 漂移 | 5.8159392558009004e-12 | 4.496501101688456e-11 |
| sampled max abs P | 0.017675574945320606 | 0.01767560307632136 |
| sampled max abs K | 0.058345140714226626 | 0.05834516809976781 |
| sampled min L | 0.942756507725285 | 0.9427565106674628 |

第二次 sampled `min D=.9999697561403896`、`min S=.9999999936000887`、`min(1+K)=.9416548319002322`、`min N=.9999838936932511`。这些都是采样值，不是连续角分支包络。

两列的 RMS 使用不同数值坐标，**不能以两列 RMS 都小于 1e-6 推出同样的物理残差界**。第二次的实际采样审计如下。

## 实际导数审计与均值事后回缩

`parallel_20261117_dynamic_tail_readout.py` 使用接受结果的公共节点值/速度定义 cubic-Hermite 插值，并读取该插值的真实导数。在每段 `0,1/4,1/2,3/4,1`、角 N=512 共 10,872,320 个点上读出。特别不能只查 collocation 节点和中点：那样会漏掉本次四分点上的大得多的实际余项。

对每个读出点仅进行一次事后均值根回缩（本次至多 3 次 Newton），保持 P 与 K 非均值部分原值，求 c* 使 sampled mean 为零。c* 的导数用 **实际插值的 P_x、Kbar_x** 经字面隐式微分得到，没有拿 RHS 代替它们。此回缩是另一个读出候选，不改原接受解身份。

| 指标 | 结果 |
|---|---:|
| 回缩前 mean 最大绝对值 | 4.496501131504016e-11 |
| 回缩后 mean 最大绝对值 | 1.4582519219930035e-17 |
| 最大 abs(c*−c) | 4.4976041716892484e-11 |
| 最大 abs(c*_r−c_r) | 2.9478764490179177e-4 |
| 原场完整 P 方程物理 r 余项 | 3.5847479514139653e-4 |
| 原场完整 K 方程物理 r 余项 | 7.889581162822085e-3 |
| 回缩场完整 P 方程物理 r 余项 | 3.5847479514139653e-4 |
| 回缩场完整 K 方程物理 r 余项 | 7.81286699610031e-3 |
| 原场 coefficient-wise 相对物理 ODE 余项 | 4.7798707544708595e-4 |

因此本次索引坐标结果没有通过 `1e-6` 的物理 ODE 判据，更没有通过曲面 metric 判据。小 mean 漂移乘以很大的 log-slope 导数会污染 K 零模；事后回缩确实恢复均值，却不能抹去实际插值的全部误差。接下来的改进必须用真实物理误差、加密和几何 Gram 读出约束，而不能只报告改坐标后的 solver success。

## 可重复源、命令与输出身份

背景 SHA256：

```text
b24084c47f03ab87af2f22edeb641d9f50b8a8bbce01d7e9578b2796c5298a3d
```

13源实际恢复自固定提交 `790477075070807b1fda90958492c973ceb6d12e`；恢复器 SHA256 为 `08e8c9b80a85db59e9c7445cdb5f300a8b45310b2639a0801da77670c80735ff`。

源文件和当前 SHA256：

```text
parallel_20261117_tail_background.mjs
713c17a5831f1735c4ba89eeb31d26eadeabe7b434366748df10326e7951f9de
parallel_20261117_dynamic_tail.py
205853250b8bd158fdd77c2462b06051c222d07cc91f0dd91e9f44655d4818ba
parallel_20261117_dynamic_tail_readout.py
0ab4cb79d2b2e1f7e6049e79f5d37d7be81a4b5726f7c6193655a2c848b9a9d5
```

首个物理 r 运行源为未加索引坐标/加密读出的版本，SHA `81c2eff2a9c5e949ffa8d357a62b02edbdc5a21d59cb486473c0b4f03975a35c`。当前版本保留 `--coordinate physical-r` 的同一完整方程；额外正分支检查在已接受场内均不活跃。第二次接受运行与上述当前源 SHA 完全一致。

```sh
python topics/visible-flex-larger-amplitude/scripts/parallel_20261117_restore_tail_sources.py \
  --repo . --revision 790477075070807b1fda90958492c973ceb6d12e \
  --out /workspace/scratch/16f63c8bce6b/parallel-tail-source

node topics/visible-flex-larger-amplitude/scripts/parallel_20261117_tail_background.mjs \
  --source /workspace/scratch/16f63c8bce6b/parallel-tail-source \
  --config topics/visible-flex-larger-amplitude/computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --depth 4 --steps 64 --modes 32 \
  --out /workspace/scratch/16f63c8bce6b/parallel-tail-d4-s64.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_dynamic_tail.py \
  --background /workspace/scratch/16f63c8bce6b/parallel-tail-d4-s64.json \
  --modes 8 --angles 256 --amplitude .001 --coordinate source-index \
  --out /workspace/scratch/16f63c8bce6b/parallel-dynamic-d4-m8-a0001-scaled.json.gz

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_dynamic_tail_readout.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-dynamic-d4-m8-a0001-scaled.json.gz \
  --background /workspace/scratch/16f63c8bce6b/parallel-tail-d4-s64.json \
  --angles 512 \
  --out /workspace/scratch/16f63c8bce6b/parallel-dynamic-d4-m8-a0001-scaled-readout.json
```

物理 r 接受输出、索引坐标接受输出、加密实际读出的 SHA256 依次为：

```text
4fc1a7cdcde9a6f1d0c8fb07cc61cde6dba366c3e8a13b55eaa1a4e167424648
b20ac12d0eaf9f7efb97e9166a55a4909af59f38d7718b4ea9b720a5729ffd70
244381b54c8f071178c57bb1ad2463cecf4af625cc34b907e35bc4edcd3934cc
```

所有 raw 状态、背景表、日志均只放仓库外 scratch。新的实际大幅 prefix cut 接入、orientation−1 外侧 cuff 和非零 trace homotopy 另记；本 note 不提前宣称它们已通过。
