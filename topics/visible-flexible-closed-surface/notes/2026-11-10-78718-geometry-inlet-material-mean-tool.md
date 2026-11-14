# 下一实际 raw CP 入口的角向上界与材料周长均值

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

工具：scripts/78718-geometry-inlet-angular-mean-bound-v2.py。
它保留 v1 的 R84 准确 Laurent 上界，另输出 R103 所需的材料均值和周长误差界。
原 v1、求解器、目标度量及候选均未改变。

用法：

    python scripts/78718-geometry-inlet-angular-mean-bound-v2.py \
      --checkpoint <新的实际inner或CP>.json.gz --out <新的报告>.json

仍只读取实际首个 PP 值和其无损分片；只适用于程序检查的原三重入口角图。
它允许检查明确未解的 inner，但不会将其标记为真联解。
它不是生产 Cartesian prefix-base 的入口工具，不能把这里的上界或均值挪到后者。
最终实际 prefix-base 仍先用 scripts/78718-geometry-base-inlet-angular-bound-v1.py
及其 --geometry 输入；若需要那个图的材料均值，须从它自己的系数另算。

## 新字段的完整数学依据

R84 的同一计算得到实际相对角误差

$$
\Gamma(\psi)=P(\psi)+R(\psi),\qquad |R|\le r,
\qquad \rho=1-w\cos3\psi>0,\quad\langle\rho\rangle_\psi=1.
$$

物理材料角满足 du=rho dpsi，所以

$$
\overline\Gamma
=\langle\rho\Gamma\rangle_\psi
\in[(\rho P)_0-r,\;(\rho P)_0+r].
$$

误差半径只需 r：因为积分权正且归一，平均 rho|R| 不超过 r。
主项是有限 Laurent 乘积的准确零次系数；不是未加权 psi 均值。

若原全角上界 epsilon 小于 1，R103(14) 中的余项可用全有理量

$$
R_*\le \frac{\epsilon^2}{2(2-\epsilon)^2}
$$

包围，因为 sqrt(1-epsilon)≥1-epsilon。令
m=|(\rho P)_0|+r，则

$$
|\ell^2-1|\le
m+2R_*+(m/2+R_*)^2,\qquad
\ell=\frac{\text{实际入口周长}}{2\pi a(0)},\quad a(0)=1.
$$

全部运算使用 Fraction。若 epsilon≥1，则保留原角向报告，但不提供这一周长界。
原全角通过字段仍只对应原图的完整 Gamma 上界；
周长字段只是一圈不可消均值的上界，不表示新的全域弧长修复已通过。

## 当前执行范围

脚本已作语法解析，尚未对任何候选调用。等待下一真实 inner 时用一次同输入调用，
同时取得原入口全角界及上述均值量；不为这项扩展重跑旧候选。
几何改进若采用，仍须实际计算 R103 的 d、w 及整条活动带的连续界。
