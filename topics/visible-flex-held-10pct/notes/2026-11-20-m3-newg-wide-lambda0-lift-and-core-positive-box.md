# m3：新 g 宽材料窗的 lambda=0 精确 lift 复接与独立核心正性盒

维护会话：Astra-held10-1b6d88ec-20261120。

新多段物理 profile 已在 q=.006 至 .06 的原八条 linear DN 路径上
取得逐步实际有限解。本条从最后 q=.06 的 raw 复接材料核心模型，
设 S=.5、b=.2、目标 k=.2、tau=1，而 lambda=0。实际重新求解通过
原 solver、physical BC 和 metric_l1 门；没有调用真尾。

## 1. lambda=0 的身份范围

`material_flattened_support_core.make_factory` 在 lambda=0 字面返回
原 PlanarSupportCore，所以这个核心本身不依赖 tau。但 portable
custom-core 模型还安装了完整 exact_core_lift：其补偿系数恒为 1，
没有乘核心同伦 lambda。它补回原有限 Fourier 表示遗漏的精确核心
及两阶角导数，因此本次有限场模型不能声称与无 lift 的旧 raw
逐字同一。raw 只是初猜，仍实际通过了原方程和审计。

Newton 返回的 delta 与高阶 support 控制有小更新；没有把它标为
固定物理 g 加密。设 tau=1 是为了后续 lambda 增加时直接指向
k=.2；不先经过耗尽门尚未支付的 lambda=1、tau=0 准确圆片，也不
在已经触发新 profile 曲率障碍的准确 k≈.45 圆片停靠。

## 2. 完整参数与实际调用

小参数文件为 `scripts/resume_m3/multistage_wide_circle_lambda0.json`：
lambda=0、tau=1、S=.5、b=.2、k=.2，quadrature_order=12、
integration_cells=64、transition_cells=24。物理 profile、原桥、
port、固定 chart 和全部数值门与新 g 幅度 note 相同。

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
  --raw-restart "$WORK/newg-q060-linear/inner-00.npz" \
  --core-module "$TOPIC/scripts/resume_m3/material_support_factory.py" \
  --core-config "$TOPIC/scripts/resume_m3/multistage_wide_circle_lambda0.json" \
  --amplitude .06 --warp-reference .06 --modes 8 \
  --angular 256 --audit-angular 512 --nodes 401 --max-nodes 6000 \
  --tol 1e-6 --bc-tol 1e-7 --physical-bc-tol 2e-9 \
  --outdir "$WORK/newg-wide-lambda0-tau1-linear" \
  > "$WORK/newg-wide-lambda0-tau1-linear.log" 2>&1
```

| 新增或间接依赖源 | SHA256 |
|---|---|
| 参数 JSON | `1168a390edc052530d5b2b0dcca02242a79e8c02006662e523cbef6ce6ba1144` |
| portable material factory | `29d3b1e74c26a1195034546e4e47bcf784f106021e9a840ea1736445c5597c53` |
| 完整 support 材料同伦核心 | `1d655f2bdad53e1d320c1115a9873abe399a9b7ba930722c415d02dedb9b1f20` |
| exact_core_lift | `28936553078df9d1a2c6486fab1613c20fd7cfdb9b4134d4c95e1d60fa5623f5` |

本次 lambda=0 工厂使用 lift 的既有中心差分参数列；正 lambda
工厂才进入已发布的完整解析材料核心 jet 列。这里没有修改任一源。

## 3. 真正终态

实际 exit 0，1 个网格、622 点、一次完整 alpha=1 Newton 步，
0 domain 拒绝、0 merit 拒绝、0 no_step，约 21.44 秒。

| 项目 | 实际值 |
|---|---:|
| 最大 collocation RMS | 9.912237632439218e-7 |
| 原 metric_l1 | 5.455339816840456e-7 |
| flow_defect | 2.251780858502794e-6 |
| Cartesian Darboux l1 | .0005228819011588886 |
| 八条 linear DN physical BC max | 2.484381515614753e-18 |
| delta | .06413471901461168 |
| 曲率采样最大值 | 8.900697880594983 |

返回的 c6,...,c24 仍是原 normal-angle support 的物理输入系数：

    [.0004660414295730199, -.000045131343392585816,
     .0000021384781818533233, .0000009091811621402126,
     3.811562757151465e-8, -5.930923764459097e-10,
     -1.0782358516630774e-8].

| 完整 scratch 返回 | SHA256 |
|---|---|
| 输入 q060 raw | `0ab581024f94d79edc6278683f5ab7471e88af5ea509cf40aa6e2f0225fca215` |
| 本次 `inner-00.npz` | `fdd146eb4e7b343669a61e50a3c3f5b489a1e3c6c7e9ca5a74cf6ec3a0fa43c9` |
| 本次 `physical.npz` | `6cbf6d6441045aba8dcb99101d7873ba82d54e11cfaa1095300f1a5f17115768` |
| 本次 `run.json` | `37ce9f4f2592cc4e64153b49ec1824b3f5719fabfaa032abedbfda02751dabbe` |

完整数组保存在上述独立目录，未提交。raw 的有限门通过不把
flow_defect 改称更强门通过，也不付真尾、连续角度等距或闭面。

## 4. 不依赖旧 R53 控制盒的新核心正性盒

新 g 的 q060 控制已经越过旧 R53 的小盒。下面另取独立粗盒，
仅支付核心正性，不沿用旧盒的中心最小性、曲率上界或相位预算：

    .0599 <= q <= .0601,
    |c6| <= .001,
    |c9|, |c12|, |c15|, |c18|, |c21|, |c24| <= .0001.

无 lift 的 q060 与本次 lambda=0 实际控制都位于此盒。原 support
曲率半径 rho=h+h'' 的三角界在每个角上满足

    |rho-1| <= 8*(601/10000) + 35/1000
               +(80+143+224+323+440+575)/10000
             = 6943/10000.

所以严格有 rho∈[3057/10000,16943/10000]，核心在整个参数盒内
正曲率，且 kappa_old≥10000/16943>1/5。这个算式用 Fraction
实际核过，只有有理数加乘，不需要节点采样或向外舍入假设。

沿 tau=1 固定 k=1/5 的 R53 材料同伦，令 chi 为该文保护窗函数，
则

    beta = integral chi*(kappa_old-k) / integral (1-chi) >= 0,
    kappa_lambda = (1-lambda*chi)*kappa_old
                   +lambda*chi*k+lambda*beta*(1-chi) >= k.

分母为正，因为 S+b=.7<pi/3，窗口外仍有开区间。故对于盒内每个
旧 support 核与所有 lambda∈[0,1]，材料新核 kappa≥.2。完整同伦
的均值/周期闭合构造仍引用 R53 与对应源码，不在这里重复登记。
若后续控制离开此盒，必须重新支付界；本条不替后续轨迹预签通过。
核心正性不推出 Frenet 域、非线性 BVP 存在、全角误差、整体 K 或 reach。

## 5. 新 g 真尾源的独立绑定

为避免旧 helper 从原 bootstrap 自动取回旧 profile，另在
`m3-work/newg-native` 实际执行既有 shared、periodic、native
安装器，输入源严格是 `multistage-source-v2`。完整调用和输入 hash
保存在该目录 `bootstrap.json`；`inputs/q060-profile.json` 是本次
新线性根 profile 的原字节，port、tail、chart 均为既有相同输入。
没有调用前缀或真尾求解来冒称安装验证。

native source 为 `newg-native/native-source`，manifest SHA256 为
`1196048f5086a2791eb78e9dff6ff07e2ef17665e457e8ba5d0f5fdacac4bcfe`，
复用的原 CLI SHA256 为
`1b47ed47e70e35a08f11173b1f17a5d1c2ee046f59f54f235ee5fa56de07af94`。
M=8、spacing=3、quadrature=128、steps=16、workers=2。
复制后新 provider 与 flat 分派逐字保留；清除 LD_PRELOAD 与
LD_LIBRARY_PATH 后 Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0
导入实际成功。所有 true-DN 接续仍需原 gate 的独立实际结果。
