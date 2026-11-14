# R57 准确仿射族的整个实核心目标型别

恢复状态：执行器更换后已从同一准确输入完整重跑全部闭单元。
170个初始单元、两次二分、172个最终通过单元及全部所列统一常数
均与原运行一致；新报告含新的实际耗时，按其新 SHA256 记录。

对象为原始 phase 控制 $c_0+\delta v$、mean 系数 $\alpha_0+\delta w$
在准确实数中的组合，再施加固定 base 的物理权重、显式偶奇平均、
准确 height slope 积分及真实无限 R33 原函数。它不同于逐坐标舍入
checkpoint，也不同于较大的独立控制点盒。

## 准确输入和命题

原点 `type_fixed_step02_d5_jet_interval_inputs.npz` SHA256：

`0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`。

方向 `type_fixed_step02_d5_actual_parameter_direction.npz` SHA256：

`8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`。

对 $|\delta|\le\operatorname{binary64}(.01)$，
$|x|\le R=\operatorname{binary64}(.24)$，恢复后已重新认证的命题为：

$$
K_0<0\quad(|x|<t(\delta)),\qquad
K_0>0\quad(t(\delta)<|x|\le R),
$$

其中仅有一对简单根 $\pm t(\delta)$。这里

$$
E=\langle F_x\cdot F_x\rangle,\quad
g_0=E,dx^2+a^2d\theta^2,\quad
C=a'E'-2a''E,\quad K_0=\frac{C}{2aE^2}.
$$

这是图自身输出的径向 target 曲率，不是实际非径向 Gaussian 曲率。

## 闭单元覆盖与根 collar

共同根证书 `type_fixed_step02_d5_parameter_root_interval.json`
SHA256 为
`b5900c391667b2a1be90912f2abaf58eaea66dfc51c082a8db39ea582b4b94a8`。
它给出整个参数管上的根 $t(\delta)\in[.238394,.2384]$，共同 collar

$$
[c_-,c_+]=[.238152859375,.23864114062500003],
$$

以及 $53.10119<K_0'<67.12731$。因而 collar 内根唯一，根左负、右正。

程序将全部原/反射 knots 及 $0,c_-,c_+,R$ 纳入分割，在
$[0,c_-]$ 与 $[c_+,R]$ 每个闭 span 上，用同一仿射 evaluator 包住
$a,E,C,K_0$。径向 jets 直接取 $S_0^{(j)}+\delta V^{(j)}$；完整
Taylor、直接区间 DFT、无限尾及舍入沿用已审根引擎。只有 $a,E$
下端严格正且 $C$ 符号通过的单元才接受。

重跑170个初始单元经两次二分，174次尝试得到172个通过单元，
0失败、0pending。其重跑安全界为：

| 量 | 重跑安全界 |
|---|---:|
| $\sup_{[0,c_-]}C$ | $<-.00253489$ |
| $\sup_{[0,c_-]}K_0$ | $<-.00050645$ |
| $\inf_{[c_+,R]}C$ | $>.02769604$ |
| $\inf_{[c_+,R]}K_0$ | $>.00552446$ |
| 全正半核心 $a$ | $>1.06871819$ |
| 全正半核心 $E$ | $>1.22857669$ |

每个最终端点还原成准确 Fraction，两个外部区间的首尾和每对
相邻端点必须完全相等。没有使用浮点容差拼接。再接共同 collar
即排除正半轴其他根，准确显式对称性给负侧镜像；腰圈已在严格
负区内。新报告的准确覆盖为 true，全部最终闭单元已重新供给。

## 源和精确重放

已逐字恢复 `scripts/fourfold_phase_affine_target_type.py`，SHA256：

`8acf9d7c89e7a80028d1efae565dcab962b4e7f56b5226bbd99d4b7d1ca3205e`。

重跑报告 `type_fixed_step02_d5_affine_core_target_type.json` 的 SHA256 为
`33385f661f1ab87cac0533343baafad5d80c3516c6f2d2d7858e58f74852b436`。
原丢失报告 SHA 为 `96ffed8f00e574701472dc9af94451549beab261a98a0ba5c59c37d373af7336`；
新报告的运行耗时不同，不冒用原哈希。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_affine_target_type.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --frozen-direction topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --root-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_parameter_root_interval.json \
  --parameter-left -.01 --parameter-right .01 --right .24 \
  --quarter-nodes 256 --minimum-width .000001 \
  --out /tmp/visible-D5-affine-core-target-type.json
```

新运行可用 `--resume`，但源、依赖、原点、方向、root 证书和参数
必须完全匹配现存进度；已丢失的旧进度不能恢复。结论不代付实际
返回、复参数管、正帽、全频逆或精确闭合可见等距族。
