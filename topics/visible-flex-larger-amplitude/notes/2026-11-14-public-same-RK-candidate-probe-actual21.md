# 公开 request21：候选工厂的 determinant 检查失败，尚无新尾残差

[公开 run 43603818345](https://github.com/Rogerhu12/math-research-public/actions/runs/43603818345)，源提交 `3b5a584e48472e5cfd9bd69ed326134fc8dcafad`，job `132474070289`。实际数值 step 以 failure 结束；artifact `14117411488` 已完整下载，压缩包 SHA256 为 `4d5461607bb37dca470ff01c4c37ad8041955781aca32a876cafcf55209f4439`。本次执行的是[已冻结 v1 接线](2026-11-14-zero-rk-native-probe-interface.md)，没有修改原有限尾方程。

## 实际结果

原输入、source、ready、capacity 和 live identity 核对完成。随后 initializer 在约 `0.217` 秒内抛出：

```text
Zero-RK initializer: nonfinite or numerically singular stage block 12 mode 92
```

stage/mode 为零基索引，即 stage 12 的第 93 模、频率 186。保留的原布局给出 rawCell 0、rawSegment 7、portRatio 1、`mu=1.0048110027994864e-11`；该 stage 的 profile 没有内部 cusp breakpoint。原图/增益在相关节点的实值如下，它们未被候选初猜器修改：

| node | 第 93 模原 graph | 第 93 模到下一节点的原 gain | 原 residual scale |
| ---: | ---: | ---: | ---: |
| 11 | -20254577475.479458 | 267.3321824945263 | 5.176434974219545e-15 |
| 12 | -16657060066.252146 | 3701438.602783984 | 5.183636132881912e-15 |
| 13 | -9311950268.915258 | 1698983.018349616 | 5.196732721955486e-15 |

`factory_constructed=false`、`candidate_constructed=false`、`evaluate_calls=0`，原 native solve calls 也为零。工厂尚未返回，故没有产生 factory identity、完整候选状态、零态线性残差或新原生非线性残差。不是已经观察到的传播下溢，也不是原 native branch guard 拒绝。原数值方法、graphs、gains、far boundary、stage layout 的结束后哈希比较为 unchanged。

原冷初猜已有的无 J norm `13414069.968482966` 只是 request19 基线，不能称为本次候选的 norm。本次更没有新 J、尾审计或接受结果。

## determinant 的证据边界与后继构造

v1 源码先逐项检查四个 $T$ 元素有限，再计算 $ad-bc$，用同一分支拒绝非有限 determinant 或 determinant 等于零。实际合并错误因此只能确认“四个有限元素构成的块触发了 determinant 检查”；原件没有保留该块及两个乘积，无法从当前回执区分 `det==0` 与乘积/差值非有限。这里不宣称已观察到哪一种，也不把浮点差为零当作精确传递算子奇异的证明。

原私有图递推实际上使用

$$
u=a+b\gamma_{n+1},\qquad
\gamma_n=\frac{c+d\gamma_{n+1}}{u},\qquad
Q_{n+1}=\frac{Q_n}{u}.
$$

它没有除以 $\det T$。因而有限浮点 `det==0` 可以作为需披露的块性质，而非必然阻止这个初猜公式；$u$ 非零及各量有限仍是公式的必要计算条件。这不证明 $T$ 可逆，不证明所得块数值准确，也不改变原 native 方程的验收。

后继独立 v2 将保留每块的 $T,ad,bc,ad-bc$ 和尺度化消去量，先留下失败块证据。只有有限 `det==0` 分支不再单独阻止私有图公式；任何非有限计算、零 $u$ 和已定义的非零传播下溢仍明确失败。v1 源、实际结果和全部原 native 边界/缩放/域/容差不改。v2 结果须另由公开 Actions 实算，不能由本次失败推定。

## 原件身份

- `same-RK-candidate-native-probe/summary.json` SHA256：`0c69d072f25c927e32322021e65b717ef6d68089d6332ed4c69c793fec87b481`。
- `same-RK-candidate-native-probe/launcher-result.json` SHA256：`fdad1b960cb3d4717c00b3714836db97baa413993578b9b8c7093344dd04331b`。
- 完整原 graphs/gains/scales、live layout 和 instrumentation 随同 artifact 保留。只读回执、解包和哈希核对在本地进行，没有重跑数值。
