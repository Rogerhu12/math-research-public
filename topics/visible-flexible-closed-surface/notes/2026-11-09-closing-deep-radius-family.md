# 改变 cuff 半径后的 N160 深背景界

会话：Astra-visible-flex-4ffd372b / closing_geometry。2026-11-09。
范围：未改的旋转深背景 n≥160；不含有限 warp、非轴对称修正或全曲面 reach。

## 固定其他参数时的精确缩放

已独审通过的 `2026-11-09-closing-deep-background-n160.md` 使用
δ0=3/500、w_cut=1/2、R=64、a=11/4、N=160 和 r_c=1/4。
现改 r_c，其他这些参数不变。总对数长度 Y 不变，原始 cut 半径
r_old,cut=r_c exp(Y/√12)，所以源归一化

$$\epsilon(r_c)=\frac{w_{cut}(r_c e^{Y/\sqrt{12}})^7}{(2\delta_0)^{11/4}}$$

精确按 r_c^7 缩放。因此在原证明的

$$W_n=64\epsilon\delta_n^{7/4}/r_c^7,\qquad
B_n=\frac{\sqrt{12}W_n(15/8)H_n}{r_c\eta_n}+\frac{7W_n}{r_c}$$

中，W_n 完全不依赖 r_c，B_n 精确按 1/r_c 缩放。
角向曲率粗界 W_n/r_c 也按 1/r_c 缩放；剩余深尾高度界
W_N 乘剩余径宽按 r_c 缩放。选根存在性和原 n 衰减估计只用
原证明的 δ、c、平台比及这个 W 界，因此无需改变。

## 新候选适用的数值界

把原先精确有理的 B_160 上界 .01894219212211… 乘 (1/4)/r_c：

| r_c | 严格母线曲率界 |
|---:|---:|
| 1/10 | 1/20 |
| 3/20 | 1/30 |
| 1/5 | 1/40 |
| 1/4 | 1/50 |
| 7/20 | 1/70 |

整个 r_c∈[1/10,7/20] 上均有 |κ_mer|<.05、|κ_θ|<10^-79，
剩余高度 <10^-131，并仍有 w,w_r→0 的 C² 平圆盘连接。
当前 width=.45、rCut=.6 的候选 r_c=.15=3/20 使用表中第二行。

`closing_deep_background_radius_family.py` 直接复用已审精确默认脚本的分数输出，
对上述缩放和不等式逐项作 Fraction 比较；没有以浮点采样替代全深度界。
复算输出 `closing_deep_background_radius_family.json`。

默认脚本引用的 R28 Git blob 仍为
`cf9881e3ae2c2797a61213ab099dbec239be5f0d`。这是原结论的参数缩放推广，
尚应由独立审查者检查其与实际 source normalization 的一致性。
