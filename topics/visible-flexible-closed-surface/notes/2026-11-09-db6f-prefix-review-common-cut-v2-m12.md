# 公共接缝 v2 与 M12 全 Cartesian 二阶端迹独审

审查者：`/root/coupled_prefix`，2026-11-09。

**结论：v2 相对已审 v1 的改动，以及本次 M12 精确端迹的 582 个系数区间全部通过。** 这不是 M12 整个闭图的度量、曲率、reach 或无限极限证书；审查者参与过前缀优化，因此本项也不替代最终未参与者的完整核查。

## 绑定输入

- 脚本 `scripts/db6f-root-common-cut-v2.py`：`317e519fda8d78fb70b53f8a8c80d51599dec1ac46e92741cd9b2576a3f4fa7d`。
- 几何定义 `2026-11-09-db6f-root-flat17-common-cut-m12s64.json`：`1fa6c8de825be71b90308e72be166dcc7ee6ae7983456d244d2c5609e3d19858`。
- 完整尾 manifest：`b202b47177bab7491b3bd237c599b7feb7d709828275b3579acd3846a90e7540`。
- 精确桥证书：`1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa`。

全部输出与输入完整路径见 `2026-11-09-db6f-prefix-review-common-cut-v2-m12-fraction.json`。

## 代码变动核对

直接比较 v1/v2 全部差异：几何修正的公式、完整 $Z$ 反射、$ψ$ 到 $θ$ 的 cut 两阶消失、桥的 $λ$ 变换、$r$ 的一二阶导数及 Fourier 符号均未改动。

新增 `validate_tail` 将两类径向输入分别处理。绝对节点格式要求精确 binary 节点严格递增；增量格式要求所有长度与比例为正，并以 Fraction 检查

$$
r_{\rm inner}+\alpha\sum_i\ell_i=r_{\rm outer}.
$$

内外锚点再与正圆领半径、物理 cut 和精确桥 cut 比较。因而不能用展示用浮点径向累加代替定义上的外锚匹配。该 guard 在 make 和 consumer 两侧调用，当前 M12 包满足全部条件。

Fourier guard 要求唯一整数频率，拒绝布尔值冒充整数；平面频率满足 $m\equiv1\pmod3$，实高度模是非负的三倍频率，且共同柱坐标模数必须覆盖原前缀和尾。具体 M12 包含零高度模；独立核查也再次检查了零模与所有频率的覆盖。

`Y=I(old.copy(),old.copy())` 消除了 v1 的上下端点数组别名。旧审查已经证明 v1 受影响的零阶高度均值会在使用前被精确恒等式覆盖；v2 修复后不再依赖该中间覆盖顺序。新的 Fraction 重跑没有发现任何最终区间变窄而漏包的问题。

## 独立精确复算

审查脚本 `scripts/db6f-prefix-review-common-cut-v2.py` 不复用待审 consumer 的端迹积分或坐标变换，而对 18457 个精确径向跨的 141 个尾系数逐项用 Fraction 重算积分。每跨使用

$$
\Delta F=L\left[\frac7{30}(u_0+u_1)+\frac8{15}u_m
+\frac L{60}(f_0-f_1)\right].
$$

随后独立转换 signed planar 频率的 $R/T$ 加减号，反射完整高度，包括零模，使用一个独立 360-bit 有理 $√ E$ 区间与桥证书中的 $λ$ 区间，检查全部 $3(3M+2)=582$ 个 Cartesian 两阶修正系数。零阶高度公共位置也由精确积分均值单独核对。

**582 项全部包含；失败列表为空。** 三个 jet 阶的最大区间宽分别为 $2.22044605\times10^{-16}$、$1.77635684\times10^{-15}$、$1.99840145\times10^{-14}$。Hermite 接缝基的左右端值、一二阶导数及角 cutoff 的精确零二阶端迹均经 Fraction 恒等式核对。

复跑命令：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-review-common-cut-v2.py \
  --geometry topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-root-flat17-common-cut-m12s64.json \
  --out topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-review-common-cut-v2-m12-fraction.json
```

当前输出支持的结论仅是共同 cut 定义、转换与精确系数包围正确。全域连续度量和曲率仍由各自后台及其独立复跑支付，不能从端迹核对中推得。
