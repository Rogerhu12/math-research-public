# 恢复段起点的第二个表示边界层

状态：**启发式网格设计与可复跑数值定位，不是连续误差认证。** 不改冻结物理度量，不重新 shooting，不把单 stage 的 $\theta=0$ 诊断当成整图结论。

作者：`/root/tail_theory`，2026-11-09。

## 1. 独立比较给出的新位置

`coupled_prefix` 对同一最终 M12 CP 的两档 critical 图作精确公共分割后的连续 C² 比较，$rr$ 差上界为 $6.120923\cdot10^{-4}$。最坏公共跨位于 $r\in[.5277879619574253,.5277881171726982]$；随后 97×512 点局部采样在 $r=.5277881139390467,\theta=0$ 观察到实际 $rr$ 差 $1.891935\cdot10^{-4}$。参考 `db6f-prefix-tail-m12-critical-r01-r005-c2.json` 及其 `-worst.json`。

这与之前约 $.520937$ 的 raw0/segment5 内部极值层不同。已有源探针在新位置定位到 raw0/segment7 恢复段、stage7，其原 profile 范围为 $[0,1/4]$。stage 坐标约 $.0232866866358$，即原 profile 坐标约 $.005821671659$。该 stage 没有登记内部 `integrationBreakpoints`，所以前两档 critical 网格仍主要依赖均匀分割来表示这里。

源探针 `db6f-tail-critical-source-m12-second-worst.json` 给背景 $w_r\approx1.509302033$，高度扰动 $V_{rr}(\theta=0)\approx-.155321699160$。五个平面有限差分步长下，高度值完全一致；其高度公式本来就不用平面有限差分。因此这里的主要高度误差不能归因于平面 $rr$ 的差分 stencil。

## 2. 端点层网格提案

新的单 stage 脚本 `db6f-tail-boundary-height-grid.mjs` 保留原内部极值层提案，并在背景经向曲率绝对值很小的端点向内寻找达到 3 的第一个距离。这里只把这个距离当作网格尺度，不把近似根当成解析断点或严格证书。

本 stage 的起点半径约 $.5277876988744847$，背景经向曲率为 0，达到 3 的 stage 坐标距离约

$$
\lambda=.04035660907590666.
$$

在均匀基本网格之外加入

$$
x_k=\lambda\,\operatorname{expm1}(k\rho)
$$

中仍位于 stage 内的点。这个形式在起点附近加密，在远离起点时恢复较宽的间隔。恢复 smoothstep 的导数从二次阶开始，以及正的背景径向基线，使这里可以出现明显的过渡尺度而没有内部 $w_x$ 零点；该机制与数值定位相符。

## 3. 实际运行结果

所有试验固定同一个 M12 CP、N512 角求值、source 最大步长 $1/256$，只更改单 stage 的表示节点。用共享端点 $F_r,F_{rr}$ 加物理中点 $F_r$ 的原 quartic 导数插值，在每个物理跨的 $1/4,1/2,3/4$ 处与源高度两 jet 比较。

| 基本均匀步数 | 端点 $\rho$ | 节点数 | 高度 $F_r$ 采样差 | 高度 $F_{rr}$ 采样差 |
| ---: | ---: | ---: | ---: | ---: |
| 64 | 无 | 65 | $9.954\cdot10^{-12}$ | $1.892207\cdot10^{-4}$ |
| 128 | 无 | 129 | $3.196\cdot10^{-13}$ | $1.424906\cdot10^{-5}$ |
| 256 | 无 | 257 | $9.850\cdot10^{-15}$ | $1.094937\cdot10^{-6}$ |
| 128 | .2 | 145 | $2.665\cdot10^{-13}$ | $1.423119\cdot10^{-5}$ |
| 128 | .1 | 161 | $1.594\cdot10^{-13}$ | $2.007879\cdot10^{-6}$ |
| 128 | .05 | 193 | $4.387\cdot10^{-14}$ | $5.973077\cdot10^{-7}$ |
| 128 | .025 | 258 | $2.610\cdot10^{-15}$ | $3.739190\cdot10^{-8}$ |
| 128 | .0125 | 388 | $1.801\cdot10^{-15}$ | $7.112184\cdot10^{-9}$ |

粗档 64 的局部高度误差与独立两档实际图差几乎一致，支持遗漏端点层这一定位。更细端点网格把该诊断的二阶误差降到约 $7.1\cdot10^{-9}$，同时一阶数据差已经接近浮点与角向 root 的精度范围。当前不继续压低这个局部指标。

两次完整运行均实际退出 0，输出为 `db6f-tail-boundary-height-grid-m12.json` 和 `db6f-tail-boundary-height-grid-m12-fine.json`，各自保存参数、CP/source hash、全部局部最坏点和阶段端一阶误差。其命令分别为：

```bash
node scripts/db6f-tail-boundary-height-grid.mjs \
  notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m12-d12-p4-s64_tail_0018.json.gz \
  notes/2026-11-09-db6f-tail-boundary-height-grid-m12.json \
  --source-root repro/source-root --radius 0.5277881139390467 \
  --angular-nodes 512 --flow-steps 256 \
  --uniform-steps 64,128 --ratios 0.2,0.1,0.05

node scripts/db6f-tail-boundary-height-grid.mjs \
  notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m12-d12-p4-s64_tail_0018.json.gz \
  notes/2026-11-09-db6f-tail-boundary-height-grid-m12-fine.json \
  --source-root repro/source-root --radius 0.5277881139390467 \
  --angular-nodes 512 --flow-steps 256 \
  --uniform-steps 256 --ratios 0.025,0.0125
```

## 4. 尚未由该试验支付的部分

这里没有重求 CP 的边值方程，没有生成第三档完整 XYZ 图，也未作整个 stage/全部角度的连续差证书。局部数据不证明源 ODE 的精确性、无限尾存在或完整 C² Cauchy 性。两档实际有限图的连续比较仍以原报告为准。

等更高频真实联解确定最终候选后，可以把这条端点提案加入其表示网格，再运行已有严格有限图后端。当前主 G5 工作仍是同一冻结度量下的频率、真实 DN 与求解精度收敛；本局部二阶试验不阻塞该主线。
