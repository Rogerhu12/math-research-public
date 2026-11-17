# 短桥接 best4 背景的实际非线性尾延拓

会话 `Astra-larger-parallel-16f63c8b-20261117`，2026-11-17。本条是新的固定有限背景上的实际求解，不把线性 source 筛选当成大幅尾解，也不把材料角与物理角的低阶模型互相替代。完整几何读出由径向 integral-K 构造另行检查。

## 背景与深端身份

使用 .992 接受前缀的真实 `r=1.167318285443017,w=2.642575483767545,w_r=48.558078940023854`。新 logw bridge 宽 .01；总 cuff 宽 .6，故 `r_cuff=1.7673182854430172`。其后的同一 scalar source 采用 orientation −1、curvature bound 6、prefixR 8、`pulseCaps=[[.4,.1]]`；valley 前四控制为

```text
1.2334188593749014, 9.06461865389976,
9.814938816563481, 11.999457607393087
```

第4至159号控制均为5，其余 primitive 参数继承 `computations/alternative-neck-provider-smallcut30-port32-r2048.json`。`prefixEnd=15,prefixReturnStart=8,protectCell=160`、`slopeCap=.02,valleyCaps=[.1]`、`warpWeightLevels=[[1,.5,3,.05,1]]` 均明确保留。实际 factory 重新计算全部派生值，包括 prefixRByCell；不能把旧配置浅拷贝中残留的派生数组当本次 effective parameters。

这组控制来自并行 model 的前四 cell 线性设计筛选，**不**是全尾成功：扩到前八 cell 后已有大的内部增益。这里只取同一 g 的前四 cell，64点/源段，固定为 C1 cubic-Hermite logw(r)。深端 `r=1.6884392650708613`，实际 alpha 为 `11.662792953476835`。背景文件 `parallel-best4-background.json` SHA256：

```text
487373a8445674658cb36ddbd20445e774612269720f58c0e6db492f38c24e15
```

深端条件使用这个完整 scalar source 从 far32 向 depth4 传播的 homogeneous 列，每源段512步。材料 M8 使用频率2,4,...,16；物理 M8 使用完整加权广义角频率，不取整。二者均验证背景 hash、实际端口 r/logw/mu；没有把 ideal 图当实际 far 图。

材料深列文件 SHA `2bd9f58404de8f46f9f9ab14c8ee902170d755be9804800d910ed109fe16baf4`；物理深列文件 SHA `e2ffce2ded2ab95dd7d30ab3bb5acd5b7f84290e630299ffa7bdee8dbfcad7c3`。这些仍是**有限线性**深边界，未支付非线性无限尾误差或第4 cell 以后的实际几何。

## 材料 M8 的真正接受结果

浅端固定实际 material trace 的前8个 P sine 系数乘 lambda；其 K 值是待读出的 DN，不额外作为 BC。每次沿相同背景、相同深列暖启动。N256，tol1e-6；全部解在节点与每 cell 四分点实际插值导数上另做诊断。

| lambda | 节点 | 秒 | solver RMS | BC max | min L | min(1+K) | max abs P | max abs K |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| .0001 | 3735 | 45.83 | 9.99854e-7 | 1.73472e-18 | .937141 | .946133 | .0132864 | .0538672 |
| .001 | 4853 | 52.71 | 9.99447e-7 | 2.06464e-21 | .372973 | .527125 | .112563 | .472875 |
| .0014 | 5095 | 54.50 | 9.99433e-7 | 1.38778e-17 | .167929 | .395535 | .142359 | .604465 |

各行 min D 分别为 `.99974783,.99752218,.99644835`。使用 `--allow-height-turn` 的扩展 chart，但这些接受场的 y 仍正，不能把它们写成已经跨越 y=0 的例子。

相对所列缩放参考 K，浅端 sampled mismatch 分别为 `2.34861e-5,2.32336e-4,3.17261e-4`。这说明尚未完成真 prefix-tail C1 接合。完整真实物理 r 的 K 方程残差分别为 `.0383539,3.15177,19.8787`；角截断与窄 pulse 的物理导数代价都保留，绝不能用 solver success 代替实际 Gram 检查。

输出文件与 SHA256 依次为：

```text
parallel-best4-material-scale1e4.json.gz
53f16fabdcf1ed7e9555ed2a946f2e2c1c1bdf006ba633a1ef3f9716af9ecbd2
parallel-best4-material-scale1e3.json.gz
a2d689c26cbe5309a61b9ab5de6fcb5b1e18ef703b28b160c01e7723ca35e210
parallel-best4-material-scale0014.json.gz
09d206be0c9c0a47df006920c99f33e8a95e915542f04b068b3899d767549cde
```

材料 trace SHA 为 `c3a5c53fb090ca842c2aa00304e470da2f4151231b65bde98d21f0bbe9c17c6e`，高度 anchor 为材料规范 `.9196724087226285`；本条材料候选不冒充保留完整物理 rho 的 M112 父。

## 同 g 的物理角 M8

物理版本保留真实完整112项 rho，采用物理 trace SHA `36688dcba2bacef79d497b92a118b58141447f2630a9c735e75a63cf4aab719b`，phi 高度 anchor `.9703876955889461`。完整加权零模和新 [fast Jacobian](2026-11-17-parallel-numerical-weighted-jacobian.md) 已用于实际求解，N512。

| lambda | 节点 | 秒 | RMS | BC max | min L | max abs K |
|---|---:|---:|---:|---:|---:|---:|
| 1e-6 | 2884 | 16.27 | 9.92303e-7 | 6.77626e-21 | .990833 | .00226504 |
| 1e-5 | 3586 | 20.09 | 9.99571e-7 | 8.13152e-19 | .901729 | .0225156 |

这两次接受的 sampled weighted mean 漂移分别为 `1.99e-13,1.59e-12`；真实物理 K 方程余项最大 `2.333,22.738`，尚待几何审计。输出 SHA 依次为

```text
parallel-best4-weighted-scale1e6.json.gz
1ea321519a3c01e892d8aa3459f02cc65323758d894eb07f4eb1466e9fbb6c4f
parallel-best4-weighted-scale1e5.json.gz
8f9109bced8c6c4b2202bab2946da8e923d4a5f152a1423b9b54ed75cd301eef
```

直接从初始猜测尝试物理 lambda=1e-4 **失败**：6329节点后建议加7973点超过12000上限，RMS14.3747、min L `.000720675`。失败输出 SHA `c38f4cec2c7b118972bd459b338db5f002ac05705d9e09a96aca6a90b9f82de5`。它不是接受父；另走更小 lambda 暖启动链继续。

每条 homotopy 仅固定缩放后的高度 Dirichlet 数据；它尚未定义一个完整几何家族。物理 phi 的均值一般含一阶加权投影项，runner 所报 `lambda²*K_mean(trace)` 只是明示的比较参考，不是该缩放族已经满足闭圈的真实 prefix K 均值。只有 lambda=1 才与原完整 trace 的这个参考相同，且仍须完成所有 mode 与 jet 匹配。

## 最小复现路径

源恢复固定 revision `790477075070807b1fda90958492c973ceb6d12e`，方法见 [首个 dynamic-tail 运行](2026-11-17-parallel-numerical-dynamic-tail-first.md)。在仓库根目录运行以下确定生成段：白名单之外的所有键均不复制，故不残留 `rCuff,oldCut,epsilonScale,prefixRByCell,constructor` 等派生字段。背景生成器随后按显式 CLI 和实际 trace 覆盖 `rCut,wCut,width,orientation,curvatureBound`。

```python
import json
from pathlib import Path
base = Path("topics/visible-flex-larger-amplitude/computations/"
            "alternative-neck-provider-smallcut30-port32-r2048.json")
p = json.loads(base.read_text())["parameters"]
keep = ("rCut", "wCut", "width", "curvatureBound", "orientation",
        "prefixR", "prefixEnd", "prefixReturnStart", "protectCell",
        "slopeCap", "capTransition", "calibrationSteps", "warpSteps",
        "cuspAwareQuadrature", "quadratureTolerance", "capMode",
        "valleyControls", "pulseCaps", "valleyCaps", "maxCachedBetas",
        "warpWeightLevels", "spacing")
cfg = {key: p[key] for key in keep}
cfg.update(prefixR=8, pulseCaps=[[.4, .1]],
           valleyControls=[1.2334188593749014, 9.06461865389976,
                           9.814938816563481, 11.999457607393087] + [5.0]*156)
Path("/workspace/scratch/16f63c8bce6b/parallel-best4-config.json").write_text(
    json.dumps(cfg, indent=2) + "\n")
```

此规范化配置 SHA 为 `c776b7453496272129b29b52c07624e9f9c3b1af6417638123e2d03c3ef2365a`，与历史含派生字段的实际配置文件字节不同。已实际用该生成段重新构造背景，`parameters,stats,rows,bridge,boundary,inner,sampled_background` 与本次历史背景逐项完全相等；仅来源配置 hash、耗时等运行身份字段不同。新传播须指向自己这份重建背景，从而与随后 BVP 的背景 hash 一致，不能混用旧背景生成的 column 文件。

背景生成命令是

```sh
node topics/visible-flex-larger-amplitude/scripts/parallel_20261117_prefix_tail_background.mjs \
  --source /workspace/scratch/16f63c8bce6b/parallel-tail-source \
  --trace /workspace/scratch/16f63c8bce6b/parallel-trace0992-m112.json \
  --config /workspace/scratch/16f63c8bce6b/parallel-best4-config.json \
  --depth 4 --steps 64 --width .6 --bridge-width .01 --curvature-bound 6 \
  --out /workspace/scratch/16f63c8bce6b/parallel-best4-background.json
node topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-calibrate-tail.mjs \
  --source /workspace/scratch/16f63c8bce6b/parallel-tail-source \
  --input /workspace/scratch/16f63c8bce6b/parallel-best4-background.json \
  --depth 4 --far 32 --steps 512 --modes '[2,4,6,8,10,12,14,16]' \
  --out /workspace/scratch/16f63c8bce6b/parallel-best4-material-columns.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_prefix_tail_bvp.py \
  --background /workspace/scratch/16f63c8bce6b/parallel-best4-background.json \
  --trace /workspace/scratch/16f63c8bce6b/parallel-trace0992-m112.json \
  --deep-columns /workspace/scratch/16f63c8bce6b/parallel-best4-material-columns.json \
  --modes 8 --angles 256 --scale 1e-4 --allow-height-turn --tol 1e-6 --max-nodes 12000 \
  --out /workspace/scratch/16f63c8bce6b/parallel-best4-material-scale1e4.json.gz
```

后两次材料运行分别增加 `--input` 指向前一接受文件、将 scale 改成 `.001,.0014`、max-nodes 改16000。物理版改用 weighted runner、物理 trace、物理深列、N512、`--fast-jacobian`，scale先1e-6后1e-5。

实际配置文件 SHA `6e6e7684b963ebec3500df4d9c5be924d1d4854704d4f8d9aa21ff9f98765aaa`。背景生成源 SHA `9abed37501b4a6ee55757082b1dd206626cf1ae5d25f9dee41aebf7baf15727d`；far 传播源 SHA `9f2b98321e22ca71ab343de9f8aa01bee68beaee1d731705a156ed6664618f8f`。本次先将后一源码完整复制到 scratch 冻结，再执行相同代码；其原文件同 SHA 可公开复现。传播的 seconds 和输出运行时间不作为数据内容不变的要求。

材料 runner SHA `1a838ec97447664a2187fa0b942b1d668da36029403f570f270935b76203353a`，物理 runner SHA `1daac938d529a1f87f7eccba81ca4e0753fc27bbe2bfcc827d69ef0b57199746`。operator SHA 详见 Jacobian note；两 runner 均用 fresh-J helper `8b6960119cd978bb7e6208e87934d68f337b9ba5679314c7c048b6cf0cac80ae`。所有 raw、场、网格、派生背景表仅在仓库外；本条没有闭面、全时 reach、held .2 或完整同 g 的 metric-refinement 结论。
