# 新总长度 .025 的真实 R205 端口和双轴全角位置场

**有限数值证据。** 沿用[R268 新物理时钟](2026-11-28-2ecf-strong-positive-meridian-length.md)的 H65 混合 own3 原位置和 36 个冻结角半径系数。这次拟合另一个目标长度增量 .025，实际后缀材料长约 .8206739498716914。原端口下，此新度量暖场 G10 原成本 .03908889265173613，G11 metric .168609434161、曲率 18.041388682、held .679595095。与较短新度量的独立峰不能互作同 $g$ 收敛。

## 真实端口重配

令 $F_A(r,u)$ 为[R205 整张弯环](../results/R205-complete-bent-annulus-cut-lifting-and-fixed-collar.md)的原准确式，$A=.8746432018013935$、内平 cuff 高 $Z=.51$。新尾取 $R_{-\beta}F_{A'}(r,u+\beta)$，$R$ 是空间绕竖轴的转动。两次相反转动使 $r<.34$ 的平 collar 按原材料点准确一致。左侧将两套 cut 的 $P,V,A$ 及各自前两角导之差作端点五次 Hermite 提升，左端起点的两 jet 全零，右端等于新 tail 的全部两 jet。cut 至 cuff 用完整新尾替换；原尾六 jet 与旧储包在 G11 上最大差约 $1.53\times10^{-13}$。前端、目标、全部高度／宽度／held／曲率 guide 保留。

按两个 G10 组的原 14 行全成本比较原场加 18 个真实替代（9 个幅相组合，每组两个 Hermite 起点）。改善者为零。最佳非零替代为 $A'=.8A$、$\beta=0$、从 $b$ 起升，全 G10 成本 .0769604188371528，独立 G11 metric .289970018297、曲率 18.041388682、held .656846039。未把弱于原场的替代计作接受。

## 新真实轴形状转入整环

两对称轴的端口不相同：长轴 cut 为 $(.8,.51)$，短轴原 cut 约 $(.73091,.32724)$。用实际两端的位置、单位切向、签名平面曲率建立单位速转角三次样条。两个端切向及端曲率进入夹持 Hermite，剩余系数的值和导数在两端为零。位置按 $\int(\cos\theta,\sin\theta)\,ds$ 构造。拟合 257 点约束、另采 8193 点观察；这里只是平面曲线的数值证据。

* 原 cut 长轴获得独立峰曲率 8.261091387，独立末位置误差两分量约 $(2.5,-1.3)\,10^{-9}$。初次同样的硬约束没找到短轴。短轴改为最小化所需峰曲率并核查三个转角绕数，16 个 span 中绕数零的 G8193 约 10.15715，正负一周均约 17.5。保持绕数零时增至 24／32／48 段，G8193 曲率依次约 9.93707／9.88809／9.79203。48 段端误差量级 $10^{-7}$；最低高度约 .09987。
* 保持同一新 S，真实 cut 改为 $.8A$，24 段短轴峰约 9.53761；改为 $.5A$，24 段短轴峰降至 8.817670，独立末误差约 $(4.1\,10^{-8},-2.4\,10^{-9})$。两者均 $\beta=0$，实际长轴 $y=0$ 的端口位置及径向两 jet 与原场一致。平尾 $A'=0$ 和原弯幅转 $\beta=\pi/2$ 的此次短轴算法没找到可行方向，未推断不存在。
* 将两轴的实际位置、切向、加速度差用全部 45 个夹持径向函数作物理加权拟合。长／短轴水平分别以 $\cos^{2m+1}u,\sin^{2m+1}u$ 延拓，竖向以 $\cos^{2m}u,\sin^{2m}u$ 延拓。二项式展开给实际 M24 全 Cartesian 场；每个候选保留双端零修正两 jet。每种端口取零参考和 $m=1,3,6,10$ 各三种强度，共 13 个全两组 G10 场，以原成本选中后再看 G11。

| 真实全环端口 | 零参考成本 | G10 选择后的成本 | 所选 $m$/强度 | G11 metric | G11 曲率 | G11 held |
|---|---:|---:|---:|---:|---:|---:|
| 原 $A$ | .039088893 | .037569826 | 1／.2 | .179942001 | 19.998677 | .674598736 |
| 新 $.5A$ | .781527792 | .192918540 | 3／1 | .305104424 | 28.261970 | .650101953 |

半弯尾上的两条独立单位速轴曲率都低于 9.5，与这些整环场的真实全角峰不同。减小全 G10 成本也不提供全闭 reach。为检查实际全二维初值，这里已经把两轴真正送进全部点，未停在轴预算。

## 复算

沿用[R268 note](2026-11-28-2ecf-strong-positive-meridian-length.md)中定义的 `common`、`DATA`、`SCRIPTS` 及相同 H65 父态。各入口均正式写出完整参数、此前输入身份及误差，临时数组不提交。会话 `Astra-visible-flex-2ecfcd69-20261128`。

```bash
python "$SCRIPTS/2ecf-strong-new-material-clock.py" "${common[@]}" --delta .025 --output clock-H65-d025.json
extra=(--clock clock-H65-d025.json --observer "$DATA/polar-physical-H65-independent.json")
python "$SCRIPTS/2ecf-strong-clock-r205-port-design.py" "${common[@]}" "${extra[@]}" --output clock-d025-cut-selection.json
python "$SCRIPTS/2ecf-strong-axial-curve-physical-design.py" "${common[@]}" --clock clock-H65-d025.json --output clock-H65-d025-axes.json
for w in 0 -1 1; do python "$SCRIPTS/2ecf-strong-short-axis-minimax.py" "${common[@]}" --clock clock-H65-d025.json --winding "$w" --seed-count 5 --kappa 9.5 --output "clock-H65-d025-short-minimax-w${w}.json"; done
for n in 24 32 48; do python "$SCRIPTS/2ecf-strong-short-axis-minimax.py" "${common[@]}" --clock clock-H65-d025.json --winding 0 --seed-count 2 --spans "$n" --kappa 9.5 --output "clock-H65-d025-short-minimax-n${n}.json"; done
python "$SCRIPTS/2ecf-strong-clock-axis-field.py" "${common[@]}" "${extra[@]}" --long-axis clock-H65-d025-axes.json --short-axis clock-H65-d025-short-minimax-n48.json --output clock-d025-axis-field.json
for i in 1 3 5 17; do python "$SCRIPTS/2ecf-strong-clock-changed-port-axis.py" "${common[@]}" --clock clock-H65-d025.json --selection clock-d025-cut-selection.json --port-index "$i" --spans 24 --minimum --seed-count 2 --output "clock-d025-port-axis-i${i}.json"; done
python "$SCRIPTS/2ecf-strong-clock-changed-port-axis-field.py" "${common[@]}" "${extra[@]}" --long-axis clock-H65-d025-axes.json --short-axis clock-d025-port-axis-i3.json --selection clock-d025-cut-selection.json --port-index 3 --output clock-d025-halfbend-axis-field.json
```

本次输出 SHA-256 如下；含时间的回执重生时以真实参数、组态和报告数值为准。

| 输出 | SHA-256 |
|---|---|
| clock-H65-d025 | `89e3577bc7f3dccb90823ea3d235ac76c80b748bd779516720d453c397e2b04c` |
| clock-d025-cut-selection | `c559a6eb828bff5ffefc5511ee02aaf45628ba986e2ec8bb77b3fd558ef9146a` |
| clock-H65-d025-axes | `8262a7afb2015e5e7855041bee2c45f22ea255fd4e9a80c55727501e7b091faa` |
| clock-H65-d025-short-minimax-w0 | `5b28cdafd93941d094ecac80fe333ec055f2b87e5b785856180fcdffc7630d3d` |
| clock-H65-d025-short-minimax-w-1 | `a82e1e167a33a360ba6889b8f01ff03ad9eb7cc0ea4719ec1261091e4056d053` |
| clock-H65-d025-short-minimax-w1 | `5029b57ea7cc6beb3d8a833e06c155ae1bc7331f89aef777d785f639df43b7b9` |
| clock-H65-d025-short-minimax-n24 | `8c98e69e17907b1a0497a90443361c9be686580eb1bbeb2d10fbfbd609cdb853` |
| clock-H65-d025-short-minimax-n32 | `8d09146cbc681c48f7f6491f804490062ab23ed99c6e1b28aa4a78696e09f447` |
| clock-H65-d025-short-minimax-n48 | `2ee5d47ade64f63a5227266d43d58fc342266f76f012f57409dd58781feea193` |
| clock-d025-axis-field | `c1e3521a1c9c05a33f0480a6509920df02128d3e386e15598e2ac20702194605` |
| clock-d025-port-axis-i1 | `76c7d9c296aba6396ab3f997bcaf88264160f7cb2f968ab65b84be4e35dddd1c` |
| clock-d025-port-axis-i3 | `ea5ca8b00c09ea99bfd72e575f29b0d4619b461f403c2f2440e8c1ada69e784d` |
| clock-d025-port-axis-i5 | `09a35e4312d817da2625ae05a0b47dd8d3d112e35a440e8f2d0dd1c4c9a9c775` |
| clock-d025-port-axis-i17 | `21f397d950e3532bfae084fab3b13a3aa6ea3b5df6e301fa8e284be3d03d46af` |
| clock-d025-halfbend-axis-field | `8a3eb54b32c9119f5a6eef10c97007aba25367773d90ac3ec06726996ab1db07` |
