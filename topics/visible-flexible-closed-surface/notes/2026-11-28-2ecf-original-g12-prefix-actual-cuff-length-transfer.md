# 原 G12 拼合前缀的袖口长度勘误与全域定量转移

完整 158 个元素的前缀回执采用 $T_0=S+\operatorname{dyadic}(.6)-\operatorname{dyadic}(.15)$ 计算校正场的单位坐标。原尾清单的真实 cuff 是存储的 $.14999999999999997$；其 cut 为存储的 $.6$。原 R226 校正界、R236/R249/R253 坐标及有限尾的全域证明采用清单的 $T_1=S+r_{\rm cut}-r_{\rm cuff}$。逐项按准确二进有理数读取给
$$
T_1-T_0=2^{-55}.
$$
前缀元素的 158 个连续包络是对 $T_0$ 位置的完整证明。下式把它们转为原清单所定义的真实 $T_1$ 场。实际校正仍是同一份 5778bee4… 的完整 C² 保存系数，原 $X+C$、目标 $g$、准确 $S$ 和物理经线 $0\le q\le S$ 都相同。

记 $S\in[S_-,S_+]$ 为原回执的准确桥长度合成，$h_i=T_i-S$、$t_i=S_-+h_i$、$z_i=q/T_i$。令
$$
d_{\rm inv}=2^{-55}/(t_0t_1),\qquad
d_z=S_+d_{\rm inv}<9.185\,10^{-18}.
$$
这给全前缀的 $|1/T_1-1/T_0|\le d_{\rm inv}$ 和 $|z_1-z_0|\le d_z$，包括两端及穿越任何 W knot 的情形。[R226](../results/R226-m12-normalized-reference-and-continuous-cartesian-bounds.md) 的同场回执给全部 $M_{ij}=\sup|\partial_z^i\partial_\theta^jW|$ 的相应上界及准确材料角 $|\theta_u|\le U_1<5.031$，原目标半径满足 $f\ge r_{\rm cuff}$。在固定的目标正交坐标下，实际两个导数列的差之和不超过
$$
d= M_{20}d_z/t_1+M_{10}d_{\rm inv}
       +M_{11}d_zU_1/r_{\rm cuff}.
$$
这是由 $W_z(z_i,\theta)/T_i$ 及 $W_\theta(z_i,\theta)\theta_u/f$ 直接微分所得。原场在每个 knot 共享二阶 jet，因此均值不等式可跨所有内部 knot。设旧归一化 Gram 与单位阵之差的谱界为 $U_0$，则旧归一化位置微分的算子范数至多 $\sqrt{1+U_0}\le 1+U_0$。展开实际 Gram 后，全前缀的附加谱误差至多
$$
2(1+U_0)d+d^2 <2.085\,10^{-18}.
$$
实际 $T_1$ 前缀上界小于 $1.235520846\,10^{-9}$。在同一物理接口 $q=S$，其准确单位坐标现为 $S/(S+h_1)$，与原尾共用。原 B 为 $2\,10^{-9}$。真实全尾仍使用自身连续回执。

以下 `SCRIPTS` 为公开课题 scripts，`WORK` 为持有原前缀回执与 G12 场目录的位置，`OUT` 为新回执文件路径。

```bash
python "$SCRIPTS/2ecf-m12-prefix-actual-cuff-length-transfer.py" \
  --prefix "$WORK/g12-prefix-composed.json" \
  --correction "$WORK/h2-c2-m48-g12-04r1/correction-bounds.json" \
  --manifest "$SCRIPTS/../notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json" \
  --out "$OUT"
```

本次实际运行退出 0，输出给出每个上述量的准确分数。源码 SHA-256 为 `cf4242f7483d5141c70cb6707cb96335ef61981bb929d8a2b538eb887334be62`，有理回执 SHA-256 为 `ae41d242d61e20731fc362fe46c245e87657d45cbe6408bf71c256c7b9ee4f31`。
