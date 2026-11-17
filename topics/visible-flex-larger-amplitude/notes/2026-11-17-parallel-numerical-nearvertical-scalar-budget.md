# 真实 .8 切口：通过采样长度门的新有限参考 g

**可信度：启发式/数值证据。** 会话 `Astra-larger-parallel-16f63c8b-20261117`，2026-11-17。本条先支付新设计的真实切口到目标圆口长度必要条件，并给条件帽直径预算；没有非线性尾场、共同 g 的整族、实际末端高度、reach 或完整闭场结论。

原 best4 强端固定 g 的长度障碍另见 R633。本次重新设计 g，不继承原 g 的有限 BVP 接受或 far 边界。

## 固定输入及两种均值

使用已接受 b677 父在 s=.8 的真实共同0/1/2jet trace `parallel-trace0800-physical-m112.json`，SHA `b49f32280e1cec30a69699e0411c5280ff561e4359afa27188a1e9c3d1f8c65a`。父 SHA `b677632099a08a33f94792a06dcc37d4e0f029131069b6ff94b1cb586ebaff25`。

切口 r=`1.097366048912719`、w=`3.122110027022912`、w_r=`-24.20569909180119`。真实物理角高度均值为 `.7887848882810774`，**材料角高度均值**为 `.7617610968235089`。本次参考高度沿材料均值规范计算，真实 chord 使用原 physical trace 的完整空间点，二者没有互换。

[physical_to_material.py](../scripts/parallel_20261117_physical_to_material.py) 保留全部112项 rho，以 `dtheta=rho dphi` 加权积分投影。8192→16384角点的前16项差最大 `4.996e-16`；输出 `parallel-smooth0800-c6-material-trace.json` SHA `96fa7c93563f7563c375ae9e6470e6811730964a90b3ffb90b09ab7a15a41422`。它仅投影 trace，不产生新的 prefix 或尾 BVP。

## 2037行固定 Hermite 表的配方

[nearvertical_background.py](../scripts/parallel_20261117_nearvertical_background.py) 先用弧长 s 描述一条参考子午线：`r_s=cos(theta)`、`h_s=sin(theta)`。起点角为 `atan(w_cut)`，初始曲率为真实 `w_r/(1+w²)^(3/2)`。参考曲率由初值平滑升到6.5，升角到 `pi/2-.002`，保持这一角度，再以曲率−6.5降到 `atan(.0012)`，最后保持小角度。

四个曲率过渡段的弧长均为 `.0001`。在每段单位参数 u 中，曲率为 `k0+(k1-k0)(3u²-2u³)`，角度由该多项式精确积分定义。常曲率段与过渡段连续接合。两个保持角度的段长由真实径向宽度和参考高度预算的2×2线性方程确定，实际为 `.5289865142460279`、`.22051618357718078`。

目标圆口半径 R=`1.55`，有限 BVP 深端半径为1.48，后面预留 `.07` 的参考退休区间。参考退休斜率为 `.0012(1-10u³+15u⁴-6u⁵)`，其参考高度增量为 `.000042`；没有在该区间定义或接受非轴几何场。

常曲率段按 `log(tan(theta))` 间距至多 `.01` 取样，曲率过渡段各64小段，保持角度段各16小段；每段位移用32点 Gauss 求积生成。由这2037行 value/derivative 构造的 **固定 cubic Hermite logw 表** 才是本条声明的 g。不能把生成曲线的曲率上限直接当作插值表的上限；下面重新检查实际表。

参考高度上限取自 R632 的条件回头盖界

\[
D_{\rm cap}\le2\bigl(\sqrt{R^2+(H+\rho)^2}+\rho+\delta\bigr),
\]

其中 rho=.145、ramp delta=.001、预算 D=4.8；再把 H 留出 `.0001` 的余量。这里 H 暂由材料高度均值加标量高度积分给出，**不是**未知非线性尾的实际末端高度。

## 实际表的数值读出

| 量 | 实际值 |
|---|---:|
| 参考高度增量，有限主段 | .7295613848438866 |
| 参考长度，有限主段 | 1.0382568964354741 |
| 含参考退休段的长度 | 1.1082569161809233 |
| 条件参考圆口高度 H | 1.4913644816673957 |
| 真实切口到该圆的最大采样 chord | 1.1046441882323192 |
| 长度减 chord 的余量 | .0036127279486040 |
| 实际 Hermite 表曲率最大采样值 | 6.500002554403424 |
| 条件帽直径上界表达式 | 4.79985479662449 |

chord 对完整物理角 cut 场取4096角点，计算到同心圆口的最小欧氏距离；最坏采样点为 phi=pi/2，切口水平半径 `.7685935495501606`、真实高度 `.7105682587059738`。长度、实际表的曲率、条件帽预算使用同一新 g。8点→12点 Gauss/每个实际物理-r表胞元，主段长度变化约 `2.2e-16`，高度变化约 `1.1e-16`。曲率在每胞元9点重新求值，故没有把生成参数6.5误当作插值的精确上界。

这说明一个新的参考背景在上述采样与条件 H 下，已经避免此前立即否定强端接合的长度不足。求积差和角采样不等于连续严格包络；R633 的区间方法可用于后续严格付账。接下来必须解真正的非线性双迹问题，测实际高度、末端完整 jets 和整面几何。特别是参考 w 峰约500，线性模式和完整分支仍须实算，不能从长度余量推断非线性可行。

## 精确来源与复现

```text
nearvertical_background.py source SHA256
dd36b046ae9c15c5df0fc2a0780a7a8091fc32c47ed1f6311c3635c97f3d3118
physical_to_material.py source SHA256
36741351cc48482b7a880bdeeaeb41fffcf22eb4dba73343c97cda93100bc607
parallel-nearvertical0800-background.json
14de4a52340c6df8ff7b175c45a6daf6d5528beb91ff8b9d8efac861b28b9dec
parallel-nearvertical0800-report.json
530687a876a557907313405495f4e949b267c55610fd6e2218dcf9e186fff616
```

下面命令在 `/workspace/scratch/16f63c8bce6b` 运行，raw 留在仓库外。材料投影小程序独立复现了原投影文件的相同字节/SHA，不必运行优化搜索。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_physical_to_material.py \
 --trace parallel-trace0800-physical-m112.json --modes 16 --angles 8192 \
 --out parallel-smooth0800-c6-material-trace.json

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_nearvertical_background.py \
 --trace parallel-trace0800-physical-m112.json \
 --material-trace parallel-smooth0800-c6-material-trace.json \
 --cuff-radius 1.55 --extension .07 --cap-rho .145 --cap-ramp .001 \
 --diameter-limit 4.8 --height-slack .0001 --curvature 6.5 --ramp .0001 \
 --peak-angle-gap .002 --deep-w .0012 --log-step .01 --angles 4096 \
 --background-out parallel-nearvertical0800-background.json \
 --out parallel-nearvertical0800-report.json
```

背景源仅依赖 NumPy、SciPy 和此前已登记的 Frenet 实际场读取源，不依赖160胞元原尾 source 链。下一条数值场若采用此 g，须固定上述表 SHA 后重新解、重新报告；当前没有可以继承的非线性接受态。
