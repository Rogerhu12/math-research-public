# 按实际Gram响应选核心方向：一个新的完整非线性前缀

2026-11-17，Astra-larger-parallel-16f63c8b。状态：完整有限线性响应、一次实际非线性BVP接受和真实quintic几何采样；尚非闭合族或全域证明。

## 同一实际父、全部collocation行

父仍为 `.992/M112/N2048/486节点`，SHA `b677632099a08a33f94792a06dcc37d4e0f029131069b6ff94b1cb586ebaff25`。标量轮廓和父保存的全部终端矩阵/目标保持。前三核心系数是本条三个设计参数；余109个核心系数是完整338维BVP的一部分。

[新响应读者](../scripts/parallel_20261117_core_sensitivity.py) 在该父的实际collocation节点和实际Hermite中点上建立完整Jacobian，仅作一次分离QR分解；对前三个边界目标分别施单位右端，得到三个完整场响应。未删模式或方程，未以独立逐圈拟合代替整个BVP。三次线性残差均在 `1.6e-13` 内。

对17个实际节点、每节点2048角度，计算归一化Gram三个分量的真实一阶变化。这里核心rho也随设计变量变化，必须包括目标角向分母的变化：

\[
\delta(G/g)=\delta G/g-2(G/g)\delta\rho/\rho,
\qquad
\delta(F/\sqrt g)=\delta F/\sqrt g-(F/\sqrt g)\delta\rho/\rho.
\]

物理角rho的变化是重新描述核心参数；按既有R240的材料角规范，同一标量轮廓仍对应同一个 `ds²+a(s)²dtheta²`。这不把不同设计几何当作固定几何精化。

设上述有限采样误差向量为b、三个响应列组成A、core gap的梯度为d。对请求的gap增量c，求明确的有限问题

\[
\min_\eta\|b+A\eta\|_2,\qquad d\cdot\eta=c.
\]

用d的正交零空间化为两变量最小二乘。它只是设计探针，不是非线性解或sup范数保证。

## 实际线性读出

整次响应与读出用时30.652秒。A的奇异值约为 `5.22181448,.55192231,.05677530`，gap响应为

```text
1.9157204348495875, .4168710577017686, 1.5821831735759506
```

初始所采节点三个分量的最大值 `2.5894689037e-7`。线性探针如下；没有把这些预测当作已接受场。

| 请求gap增量 | 预测最大分量 | 预测rho最小值 |
|---:|---:|---:|
| 0 | 1.62727e-7 | .167288 |
| 1e-5 | 1.67219e-7 | .167209 |
| 1e-4 | 2.14022e-7 | .166506 |
| .001 | 7.98148e-7 | .159471 |
| .01 | 6.90014e-6 | .0891235 |

这也显示不能仅凭线性gap增加就忽略曲率半径：较大预测会降低rho。

## 真正重新求解：gap请求1e-4

选取线性请求1e-4得到的新前三目标

```text
.46199473979154143, -.05970151939663436, .01568929361918116
```

使用已刊fresh-J helper、完整338维方程、原终端行，`tol=1e-8,max_nodes=1600`，从真实父重新求解。146.510秒后在原486个节点接受，RMS `9.325875232474175e-9`、BC最大值 `6.505213034913027e-19`。非线性核心gap为 `.9601012148208481`，即比父实际增加约 `.000100220738`，而非把请求值直接回填。

随后在同一C² quintic映射的485个单元上，读取两端及四分点、N2048，共4966400点，得到：

| 实际几何量 | 值 |
|---|---:|
| 最大相对Gram算子采样 | `5.176777090643784e-7` |
| 最坏位置 | `s=.992, phi=.4325825821837508` |
| 主曲率绝对值最大采样 | `6.299662166641838` |
| 最小Gram determinant | `.027707920821625258` |
| 核心rho最小采样 | `.16645696387242426` |
| 整个前缀到core见证点的最小采样距离 | `.9600602711070766` |
| 反射前缀的球径代理 | `3.502978034959134` |

本次前缀通过1e-6**采样**门，与[R3直插方向](2026-11-17-parallel-numerical-core-target-probes.md)的1.609e-5失败区分。但实际最大值比线性预测2.140e-7大，不能把线性最小二乘当作严格误差界。完整闭面D、tail-DN及C²接口、全t、reach和固定几何收敛仍未付。

## 复现、原始数据与身份

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_core_sensitivity.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-refine0992-m112-t8.json.gz \
  --out /workspace/scratch/16f63c8bce6b/parallel-core-m112-three-responses.json.gz

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_continue.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-refine0992-m112-t8.json.gz \
  --duration 0 --fixed-modes 3 --modes 112 --angles 2048 \
  --core-first .46199473979154143 -.05970151939663436 .01568929361918116 \
  --tol 1e-8 --max-nodes 1600 \
  --out /workspace/scratch/16f63c8bce6b/parallel-core-gram-dg0001.json.gz

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_prefix_readout.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-core-gram-dg0001.json.gz \
  --angles 2048 --radial-subdivisions 4 \
  --out /workspace/scratch/16f63c8bce6b/parallel-core-gram-dg0001-quintic.json
```

| 对象 | SHA256 |
|---|---|
| 响应源 | `ed64ff65c8378d637956aa6c45b6ac7160a538a0bc6864518858ded8a777611e` |
| 实际响应报告 | `9d733e1872d25f2489cde83aece5cdf3dcfe28823b9e45f8f3d0bb73be0e46cb` |
| BVP源 | `8b6960119cd978bb7e6208e87934d68f337b9ba5679314c7c048b6cf0cac80ae` |
| 新接受场 | `91e56c73f2cb6500891ea244055825b7b495871cc63cf1399fe73e09b60cc91a` |
| 完整quintic报告 | `15eb36e8ce5954ea41e58d64484f3a49d74aa122ab2f12a48190ad3fe0ba3192` |

响应数组、QR工作块、原始场和报告只保存在仓库外。三个边界响应的线性残差验证是本次具体计算的责任，不增设无关fixture或替代闭面完成标准。
