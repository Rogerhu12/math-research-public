# 深端零非均值高度的完整有限尾 BVP

会话 `Astra-larger-parallel-16f63c8b-20261117`，2026-11-17。本条定义并实际求解一个新的有限尾问题，目的是直接支付高度退休；它不声称与无限尾 Robin/DN 等价。背景仍为已登记 best4 的固定 Hermite g，不能把新边界条件的接受继承给旧 far 问题。

## 明确的新边界条件

状态仍为完整 `P_sin(M),K_cos_nonzero(M),c`，没有删掉任何保留的状态方程。浅端固定原 material trace 的前 M 个 P 系数乘 lambda，并施加字面 mean=0；深端改成

\[
P_j(r_{\rm deep})=0,\qquad j=1,\ldots,M.
\]

这给 `M+1+M=2M+1` 行。深端 K 仍是未知解，**没有**额外钉零法向导数，也没有获得 C² flat-cuff 匹配。按 P 定义的非均值高度在该圆消失，但 actual integral-K 兼容化高度仍须付 P 方程插值误差；其真实0/1/2端部 jets 和几何平化成本另行检查。

新源码 [tail_dirichlet.py](../scripts/parallel_20261117_tail_dirichlet.py) SHA256：

```text
e0f3adc49d748068ad53b8cd0bb518e9549f9aa9aa45323a975398b268fc8b1a
```

它明确记录新边界类型和实际初猜 SHA，不需要或暗用任何 far column。原 far 接受场只作为同 g 的初猜，新边界的全部行重新求解。

## 实际接受链

M8/N256，source-index 坐标、tol1e-6，完整 S,D,L,N 分支检查，`--allow-height-turn` 显式启用但本次接受场 y 仍为正。首个运行将原 far lambda=1e-4 接受场缩放为1e-6初猜；之后每次沿新 Dirichlet 接受父暖启动。

| lambda | 节点 | 秒 | solver RMS | BC max | min L | max abs P | max abs K |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1e-6 | 3735 | 12.35 | 4.54784e-7 | 3.15363e-24 | .993809 | .0000753742 | .00699925 |
| 1e-5 | 3748 | 23.20 | 9.87963e-7 | 3.30872e-24 | .936317 | .000753623 | .0678802 |
| 5e-5 | 3907 | 32.02 | 9.95093e-7 | 2.64698e-23 | .621128 | .00376554 | .378825 |

min D 分别为 `.99999745,.99997449,.99987257`。真实四分点插值导数的完整 physical-r K 方程余项最大为 `8.9360e-5,6.8405e-4,.0314238`，mean 漂移最大为 `1.56e-13,1.48e-11,2.47e-11`。这些有限采样量均不是实际 Gram 或 reach 证书。

浅端 K sampled mismatch 依次为 `2.34063e-7,2.34031e-6,1.16948e-5`，故仍未支付原 prefix 的完整0/1/2 jet 接合。这条小 lambda 链也不是已经完成的全幅几何家族。

输出文件与 SHA256：

```text
parallel-best4-dirichlet-scale1e6.json.gz
e392ddfa2ff1a9279efb8265d2ff064c89a77dd0d233d92fb9c2932010b0aa28
parallel-best4-dirichlet-scale1e5.json.gz
654d5d47d004c10688de355c330b434db55bb89e4cc9a247084e284facce2695
parallel-best4-dirichlet-scale5e5.json.gz
2ded20c3a7b277bb2b84290cf029205ef34890dff14ca7d368e1520d2ef76e86
```

直接从原 far 场尝试新 Dirichlet lambda=1e-4 曾**失败**：7151节点后所需加点超过12000，RMS4.00824，mean 漂移.0613，没有形成接受父。完整失败输出 SHA `d419c1778296cb036f658176f1ef374f810d0e699a251c44999255a6d15a62ac`。因此采用上面的小步暖链；原失败文件保留，没有用后续结果覆盖它。

## 复现与固定来源

背景 `parallel-best4-background.json` SHA `487373a8445674658cb36ddbd20445e774612269720f58c0e6db492f38c24e15`；trace `parallel-trace0992-m112.json` SHA `c3a5c53fb090ca842c2aa00304e470da2f4151231b65bde98d21f0bbe9c17c6e`。material 高度 anchor `.9196724087226285`。背景与输入生成沿用 [best4 的完整确定步骤](2026-11-17-parallel-numerical-best4-tail-continuation.md)。

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_tail_dirichlet.py \
  --background /workspace/scratch/16f63c8bce6b/parallel-best4-background.json \
  --trace /workspace/scratch/16f63c8bce6b/parallel-trace0992-m112.json \
  --input /workspace/scratch/16f63c8bce6b/parallel-best4-material-scale1e4.json.gz \
  --modes 8 --angles 256 --scale 1e-6 --allow-height-turn --tol 1e-6 --max-nodes 12000 \
  --out /workspace/scratch/16f63c8bce6b/parallel-best4-dirichlet-scale1e6.json.gz
```

第二次 `--input` 改为这次新接受文件、scale改1e-5；第三次再用第二次的接受文件、scale改5e-5；输出文件如上。三个运行均保留完整新边界、方程与同一 g。首次初猜 SHA `53f16fabdcf1ed7e9555ed2a946f2e2c1c1bdf006ba633a1ef3f9716af9ecbd2`。

dynamic operator SHA `e21034c9f1208506d16f1bed3cc46c470fdf15425c6466eb0f9623ad0fcfa8b5`，fresh-J helper `8b6960119cd978bb7e6208e87934d68f337b9ba5679314c7c048b6cf0cac80ae`。raw、字段和网格只在仓库外。后续真正平化仍须以 actual integral-K/radial map 的端部 jets 与完整 metric/curvature 读出为准。
