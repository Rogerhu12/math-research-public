# 同 actual22 方向的五个完整角网诊断

源：`computations/geometry_20261114_full_angle_domain_direction_probe.py`，
SHA256 `794788a17db22189b80d65b7def84f3515ca587ea59ffce96fe8887a071665e8`，
27,821 B。

本入口接续[actual22 真实角向域限制](2026-11-14-actual-request22-multiline-tangent-and-angular-domain-limit.md)。
它不添加第四个保护点，不重解 LSMR、完整 BVP 或 native 尾，不
创建 warm，也不设置新接受门。唯一目的，是区分旧实际方向的
角向失域能否由完整一阶变化预报，还是由更大的非线性余项造成。

## 精确输入和调用

输入基态仍是 **base20**，不是 actual22 已走一步后的新 warm：

- base20 SHA256
  `0036063ff99e7b3624e494b29430b9a3a8ec3eaae15f277447efcc71b8cc5e71`。
- actual22 `direction-00.json.gz` SHA256
  `9a5916d9419df61ade98d89a917ef6778ac1d75b42977ce3ed110ec123a58873`。
- actual22 `model-000.json` SHA256
  `a5120beeac90342fdfd0f1596caa6b0549bb19bb459c5ec6b9ed5c9e6c85083d`。
- actual22 `domain-rows.json` SHA256
  `07b14e3485d3579609cd3b98eb35cac468d601fdb201ecb5715b9dc9efb138cb`。

同目录的 intent、status、原 operator-check 与实际新 warm 也各自
固定 SHA；入口核对完整 producer 账、原场/标量公式、整个 global
core/p、原 mesh 及方向的 scaled/coefficient 两份定义。原四输入
仍为已硬锁的 accepted M96、prepared 699、已完成 T112 零 H 全 J
与原 T112 config。只读取现有 J 建立同一问题身份，不调用尾。

```bash
python -u computations/geometry_20261114_full_angle_domain_direction_probe.py \
  --accepted "$A96" --prepared "$P699" \
  --tail-anchor "$ZERO112" --tail-config "$CFG112" \
  --base-warm "$W20" \
  --run-directory "$TOPIC/notes/public-actions-43604874829-1-trustmultiline/multiline-warm" \
  --out "$OUT/full-angle-domain-direction"
```

输出目录必须为空。本入口先逐值重建 actual22 接受的 alpha=`2^-9`
那一步的完整 699 节点 states，并与原实际新 warm 对照；方向或
基态字节混用会在科学诊断前被识别，不能换成另一个方便的方向。

## 局部完整链和角范围

只看五个已实际失域的 interval：473、475、477、479、480；径向
查询均为原左 RMS fraction `0.17267316464601146`。
所需端点合起来恰是 **9 个原节点 473…481**。每次批量重算它们
完整原 augmented RHS，不反复作 2048 次全场求值。

先从 `z/chart.scale` 核对已保存 coefficient direction，再用原
`chart.lift_direction` 得完整 deltaY，包括 inlet/core 和每节点的
同一 global p。complex 扰动直接加到这个完整 augmented state，
不通过会实数化的 `chart.expand`。原 flow 的一次 complex 方向
评价得到两个端点的完整 deltaf，包含 physical 和 p 的链。

对 `(Y,f)` 与 `(deltaY,deltaf)` 分别使用原 `CubicHermiteSpline`，
得到同一个查询的 q 和 deltaq；另记录原四项 Hermite 公式的
舍入差。对 q 与 deltaq 各调用一次原 `q.jet`，得到完整 N2048
的 d、e、deltad、deltae。原 FFT 已包含旋转 frame 导数，不能再
添加一次角旋转项。

实际 beta² 仍取原 normal-vector 表达式。交叉积等价式只用于
完整方向导数和同角舍入对照。令 Q=d·d、W=|d×e|²、nu 为原返回
的 ap，完整方向导数为

```
Bz = -2 nu Q³ delta_nu/(a² W)
     -3 nu² Q² delta_Q/(a² W)
     +2 nu² Q³ delta_a/(a³ W)
     +nu² Q³ delta_W/(a² W²),
delta_Q = 2 d·deltad,
delta_W = 2(d×e)·(deltad×e+d×deltae).
```

`(delta_a,delta_nu)` 来自原 control_jets 与完整 query 参数方向，
不能遗漏 scalar 直导或两个端点 p 链。此处无需把返回的 ap 当成
另一个有限 Gauss 半径公式的精确导数。

完整 nodal complex → Hermite → 原 normal beta² 的独立方向读数
同时保留；与 R262 公式逐角对照。三个原保护点还分别对照原
actual22 保存的 covector action。全部差值只报告，不新设 BVP 门。

## 每角输出及辨别方式

每个 interval 独立保存一个 gzip 包，包括：

- 2048 个原物理角、基线 beta²、Bz、完整 complex 方向对照。
- 对 Bz<0 的每角一阶 first-exit `-base_beta²/Bz`；其余用 null，
  不伪造一个有限临界步。另列最早 16 个候选角。
- actual22 原来实际尝试的全部 10 档 alpha，1 到 `2^-9`。
  每档都从原 exact coordinates 重建后重新计算局部端点 RHS，
  再过原 Hermite 插值，保存所有角的实际 beta²。
- 同角的 `base+alpha Bz` 和
  `actual-base-alpha Bz`，实际/线性最坏角、负值重合与不重合数量，
  最大余项及除以 alpha² 的读数。
- 原报告最坏角及三个保护点的直接重放差值，以及原 query RHS
  是否有限。不能把负 beta² 的值删去，也不能凭一个新 argmin
  代替全角列表。

因此若一阶预测在某批角已为负，可区分其与实际失域的重合；若
一阶仍为正而实际为负，才有针对这次方向的非线性域余项证据。
该比较只覆盖这五处原 N2048 **格点**，不自动成为连续角域证书，
也不代替原全部节点、中点、另一 RMS 组或 rho4096 检查。

`summary.json` 同时从固定绑定 actual22 model 原标量，在 Actions
内实际记录 [R263](../results/R263-projected-KKT-and-damped-model-error.md)
的 E、Delta、E/Delta 和方向误差上界。它们只针对那一个固定
阻尼二次模型；没有新算 J/LSMR，没有新增科学接受门。

没有保存可冒称新解的 state 产物。`exit0` 只表示这些只读诊断
完成，所有 full BVP / native / closed / continuation 接受标志
仍不存在。源交付时只做 AST 和静态代数/接口核；全部数值必须
在本公开仓库 Actions 运行。局部计算预计为秒到分钟量级，不
再付完整 699 节点 Jacobian 或 576-stage native 遍历。
