# 固定 inward 度量、真实椭圆核心与独立末盘高度

日期：2026-11-14。入口是新脚本 `scripts/inward_collar_search.py`。它复用已公开的 `InwardMeridian`、三种表示和真实 shape-operator Jacobian，不改动已有稳定求解脚本。实际优化只允许在 `Rogerhu12/math-research-public` 的 GitHub Actions；本地仅运行 `--smoke-only` 的小型表示/导数检查。

## 1. 这个 BVP 固定了什么

物理核心是半轴 $(A,B)=(1,.3)$、高度 $|z|\le h_0$ 的椭圆柱，平均周长半径为

\[
a_0=\frac{2A}{\pi}\operatorname E(1-B^2/A^2)=.6980392675284104\ldots.
\]

半侧连接长 $L_c=.8$，圆端口半径 $r_c=.28$。以 B 参数为默认：$h_0=.23$、$\eta=1.53$、第一段比例 $.67$。inward 参考确定唯一的 $a(s)$，以后全程固定目标 $ds^2+a(s)^2du^2$。全径向区间长 $2(L_c+h_0)=2.06$，核心区间为 $[.8,1.26]$；两段径向样条继续共用 `controls-6` 个自由径向函数，未因拆分而加倍变量。

**实际末盘高度独立于圆参考高度。** 默认实际两平盘位于 $z=\pm .30$；圆参考的上端只有 $.0927053952$，不能直接作为强椭圆闭曲面的实际高度。B 的活动长为 $.7368576415$，平圆领长为 $.06314235851$。若半侧参考高度为 $z_{\rm ref}(t)$，实现使用初始试场中心

\[
z_{\rm trial}(t)=z_{\rm ref}(t)+
(.30-z_{\rm ref}(L_c))S_5(t/L_{\rm active}).
\]

$S_5$ 在 $[0,1]$ 外常值延拓，所以抬高项在整个末端开平领恒定，在核心连接处和开平领处均有零的一、二阶导数。目标 $a(s)$ 不改变。内部的 $a'^2+z_{\rm trial}'^2$ 不预设为 $1$，这是求解器必须修正的初始位置误差，不是新度量设计或参考等距证明。

解析 Cartesian 的核心位置、材料角向一/二阶导、径向一/二阶导全部锁定。unit/signed 则锁定准确的核心角切向场，但位置仍由有限角 FFT 原函数重建；两者不是连续解析核心位置证书。新报告专门保存 `pinned_piece_jet_audit`，不隐藏这项差别。

## 2. R4 在求解前筛选实际边界

默认使用绝对 reach 设计预算 $.069$，并始终至少施加由核心直径给出的任务必要值 $.06$。默认上盘必须满足 $C_z\ge h_0+.069=.299$，所以取 $.30$。脚本会拒绝更低的默认几何输入。该 screen 也验证入口横移 $.72$ 不超过曲率转向允许的 $.7606150535$。

这两项只是准确目标问题的必要条件，不是存在、嵌入或 reach 的充分条件；它们不能直接作为有限 $C^0$ 度量误差场的测地线曲率证明。对 C 参数改用 $h_0=.25,\eta=1.5,\lambda=.68,C_z=.32$，同样保留 $.001$ 的高度余量。

这里末端是完整平盘，$C_x=C_y=0$；不依赖 R128 非对称尾，也不要求非零端口偏心。相位族若将来构造成功，必须另验实际整体几何和固定握持位移，不能将本段必要条件当作那些验证。

## 3. 已完成的廉价开发检查

以 `controls=10,modes=2,angles=32,radial-order=2`，不执行任何最小二乘，检查残差 Jacobian 的随机方向中心差分：

| 引擎 | Jacobian 相对差 | 128 角核心/圆领全二 jet 最大误差 |
|---|---:|---:|
| Cartesian，真实曲率权重 $.01$ | $4.90\times10^{-10}$ | $8.9\times10^{-16}$ |
| unit | $1.77\times10^{-9}$ | 位置 $4.67049\times10^{-6}$；其余已报告 jets 约机器精度 |
| signed | $2.40\times10^{-9}$ | 与 unit 相同 |

对应三个小 JSON 为 `notes/inward-collar-smoke-{cartesian,unit,signed}-20261114.json`。unit/signed 的位置差来自强椭圆的有限 FFT 原函数；其角向导数字段不等于严格连续原函数导数证书。需要精确核心的首轮优先使用 Cartesian。

零自由系数初场的 metric 误差约 $2.3$–$2.7$、曲率很大，故不把它写成可行候选；这些 smoke 只验证表示、物理尺度、实际边界和 Jacobian 接口。尚没有运行该固定度量的新优化。

## 4. 最小 Actions 输入

以下从仓库根运行。每条都保存完整固定参数和源 SHA-256。先小规模比较三种表示；更换 `--engine` 后不是同一离散未知量，不能直接用另一引擎的系数作 resume。参数相同的原引擎可用 `--resume`；改变物理边界或度量会被拒绝，必须作为另一个明确标识的 BVP。

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/inward_collar_search.py \
  --engine cartesian --ellipse-major 1 --ellipse-minor .3 \
  --core-half-height .23 --connection-length .8 --cut-radius .28 --port-height .30 \
  --inward-overshoot 1.53 --inward-first-fraction .67 --reach-budget .069 \
  --controls 14 --modes 6 --angles 128 --radial-order 8 \
  --curvature-limit 13 --curvature-weight 0 --max-nfev 200 \
  --out "$VISIBLE_OUT/inward-cartesian-B.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/inward_collar_search.py \
  --engine unit --ellipse-major 1 --ellipse-minor .3 \
  --core-half-height .23 --connection-length .8 --cut-radius .28 --port-height .30 \
  --inward-overshoot 1.53 --inward-first-fraction .67 --reach-budget .069 \
  --controls 14 --modes 6 --angles 128 --radial-order 8 \
  --max-nfev 200 --out "$VISIBLE_OUT/inward-unit-B.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/inward_collar_search.py \
  --engine signed --ellipse-major 1 --ellipse-minor .3 \
  --core-half-height .23 --connection-length .8 --cut-radius .28 --port-height .30 \
  --inward-overshoot 1.53 --inward-first-fraction .67 --reach-budget .069 \
  --controls 14 --modes 6 --angles 128 --radial-order 8 \
  --max-nfev 200 --out "$VISIBLE_OUT/inward-signed-B.json"
```

`--curvature-weight 0` 只是不在这轮目标函数中加曲率惩罚；报告仍审计真实 shape operator。若后续在同一固定问题加正权重，这是求解目标的权衡试验，不能声称曲率限制已被严格强制。圆参考的几何报告始终独立，不能移植给任何实际非圆输出。
