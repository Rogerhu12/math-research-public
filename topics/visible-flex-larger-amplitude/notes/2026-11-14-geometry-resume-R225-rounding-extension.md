# R225 圆化延至 .9875：固定 g 的 M128/M192 实算

作者：geometry_design，AI 辅助，2026-11-14。

继 `2026-11-14-geometry-resume-R225-rounding.md` 的 `.9075` 结果，实际 M128 场继续外扩到 `.9875`，保持完整 R225 32 模核心。然后把新增的 $a,a',a''$ 节点并入同一种精确 C² 五次 profile，停止反馈，分别从原核心冷启动 M128 和 M192。新增的度量明确区别于此前只定义到 `.9075` 的度量。

共同参数为 DOP853、`rtol=1e-11,maxstep=.0002`。冻结 profile 现在共有 116 个节点、345 条精确右端二阶 jet 接缝等式：

- scalar geometry SHA256：`c58eedddd4799278c95ed7b55e9c753b7d0ec1456466046bb9623118dc02e229`。
- exact polynomial SHA256：`57c3e6e1f55f701628548511f6d50368c68abbd948f4c4bdeba87e235443ffc0`。
- 包含完整核心的固定 metric SHA256：`4b53eb420ad32611ff3040772ae7c1f06f14b9328c6990627c8ca980feb55482`。

| M / N | 最大度量误差采样 | 最大主曲率采样 | 反射开放前缀 $2\max|F|$ | 最小点域余量 | 秒数 |
|---|---:|---:|---:|---:|---:|
| 128 / 1536 | $7.84421905\times10^{-6}$ | 5.32068363 | 3.44732165 | .26009630 | 61.17 |
| 192 / 2048 | $1.08440997\times10^{-7}$ | 5.32103856 | 3.44732126 | .26627381 | 89.55 |

两次均实际退出 0、到达 `.9875`，所有 scalar profile、核心系数及材料角定义完全一致。M192 末端读数为

$$
(a,a',a'')=(1.2209338225906492,
.5655055376942772,.3234667007608959),
\qquad \min_\phi a\kappa_{lat}=.6601913819522689.
$$

实际平均高度 `.9522863601344331`，高度范围 `[.7956514695827469,.983411923009122]`，最大平面半径 `1.4155942072279097`。末纬圈的核心见证距离 `.8501877226928192`，整个开放前缀的最小采样距离仍是核心处 $G=.799999999993045\ldots$。

这一步使上一轮 M128 反馈终止点可以在固定度量下分辨；不意味着继续外扩就一定能闭合。控制器的逐角度导数条件也有保守性：在 M192 末态，`eta=.9,rate=16` 的最小正向加速度上界为 `.3089612891`，略低于冻结度量的实际入射加速度 `.3234667008`；对应角是 $\pi/2$，其 $a\kappa_{lat}=.7061346145$、$\partial_s(a\kappa_{lat})=-.9014317289$。当 rate 改为 24，这个上界为 `.8690862117`。因此不能把某一个选定反馈不等式的失败当成曲率、点域或几何存在性的失败。

## 保存及复现

`2026-11-14-geometry-resume-R225-rounding-extension-fixed-profile.json` 是本次固定度量；`2026-11-14-geometry-resume-R225-rounding-extension-summary.json` 保存两次运行、全部参数及 hash；`2026-11-14-geometry-resume-R225-rounding-M192-checkpoint.json.gz` 保存完整 578 维 Fourier 末态、全部 scalar profile 和全前缀采样摘要。紧凑 checkpoint 省略旧场节点，冷重放会重建它们。

```bash
python computations/geometry_20261114_r225_fixed_profile.py replay --profile notes/2026-11-14-geometry-resume-R225-rounding-extension-fixed-profile.json --M 192 --N 2048 --maxstep .0002 --rtol 1e-11 --out rounding-extension-M192.json.gz
```

另一档只把 `M,N` 改为 `128,1536`。使用此前已推的同一完整求解源码和 FFT 求值核，无滤波或核心截短。

这些是开放前缀和采样结果。完整闭合曲面 $D$、连续 reach、完整图像 Hausdorff、固定 H、包含反射的 E(3) 及所有 t 仍未完成。下一步实际采用双向点域 barrier 允许 $a''<0$，并处理正 Gauss 段的高模匹配；没有把本次 profile 不同的反馈试验混称为同 g 加密。
