# R149 actual IR：原96条 inverse-density 坐标行及两种全频残差

**已证明（公开 Actions 的完整99目标）。**
会话 `visible-exact-astra-fb31ed6-20261127`，2026-11-27。

公开 run [45899761652/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45899761652)
由 commit `6e90b63ffa32805445e9249be1f628a715227e48` 触发，首次执行
全部完成；完整 [actual](../notes/inverse_density_rows_ci/run-45899761652-1/actual-original-inverse-density-rows.json)
为79739 B，SHA-256
`5d0ddf149f6193e29e9873134a75b5afc7fc2b3b71012ef8ddd6103be8703ec3`；
完整 [execution](../notes/inverse_density_rows_ci/run-45899761652-1/execution.json)
为23307 B，SHA-256
`8345057b88a3913443178bcd95611386c5c21798fb44c38f85589a8d780ab813`。
两者 `complete=true`；科学对象 `proved=true`、returncode0，唯一
child用时13.529351468999991秒，旧数学目标/旧producer调用数均为0。

## 完整原对象

采用 [IR](R149-supplement-complete-inverse-density-row-residuals.md) 的
同一 selected $p=H\circ X_-^{-1}$、原 root-even归一实基
$e_j=\sqrt2\cos4jx$、固定 $D_+$、物理频率4和
$\mathscr H=\dot H^{-1/2}_0$。本次严格得到

$$
 L=E_{96}^*D_+^{-1}C^{-1}:L^2_0\longrightarrow\mathbb R^{96},
 \qquad \widehat L_j=G\widehat z_j,\quad G=|D_x|^{-1},
$$

的完整行误差。原 $A$ 尚未施加，所以本次不把 $L$ 改名为 $V_Q$。
完整已成 IL run `45896427415/1` 的四球和整输入链直接消费，未重算
$E_p$、三个导数或任何旧 transport/KAM/RW/TC target。

全部96列 finite trial各有192个正频 complex dyadic系数，负频精确
共轭。共同4096点有向 complex FFT之后，保全1024正频 signed head、
对应负共轭、所有DFT alias、整个无限 Fourier tail及真map模型差。
取正输入到正输出，再补负共轭；没有误用整个 $U_p$ 替代同号压缩。

## 三个完整联合结果球

令 $R e_j=C^\dagger\widehat z_j-ND_+e_j$。下列三球均是正式保存
的 `bound="upper"`；下游消费整球的上端点。

| 同一完整目标 | 实际完整球 |
|---|---|
| $\|R:\ell^2_{96}\to\mathscr H\|\le\epsilon_H$ | `[0.14240166207829550904072240928745350120607289910345 +/- 4.92e-51]` |
| $\|R:\ell^2_{96}\to L^2_0\|\le\epsilon_0$ | `[0.43542976035508378866165612987952434638698155062305 +/- 4.07e-51]` |
| $\|L-\widehat L:L^2_0\to\ell^2_{96}\|\le\epsilon_H/2$ | `[0.071200831039147754520361204643726750603036449551727 +/- 4.61e-52]` |

联合前两项消费全部96条正式读回的完整 row bounds，后者再消费
正式读回的联合 $\epsilon_H$，没有额外乘 $\sqrt{96}$。每条 row 的
两个残差范数、两个 analytic 模型界及 real homotopy模型界全部
保留在 actual 中。完整实轴同伦下界的正式球为
`[0.92208332496319346727860749302465254132858839708296 +/- 4.57e-51]`，
因此本次所有 real alternative 均合法可用。

## 实际载体、读回与固定 runtime

[manifest](../notes/2026-11-27-inverse-density-rows-inputs.json) 为20417 B，
SHA-256 `36166701e9dc4ca820cd3134ce2eb4c5dcee93b84176b5ddfd41cf7cdcfa02f6`。
50个完整 current输入和6个完整历史自然对象的资格链均实际通过，
所有原 source/manifest/publication/execution/byte identities保留在
两个整结果对象中。

原 exact compound grid的私有整文件为407627 B，SHA-256
`74ba633b63b22fff209c2a42cc5bebe66c25ed3acc3e7c8bb7a3c9bc6563ea0f`；
全部 trial系数的私有整文件为294912 B，shape为 `[192,96,2]`、
little-endian binary64、row-major，SHA-256
`02ee6051166f1f23139b39984dbd309592c415405620f99982a3972d8dd49db1`。
该二进制内容定义精确 dyadic trial；浮点 solve仅选择它，不提供
任何逆或残差 bound。全部样本、所有 signed heads及其 hash链也均
先整对象保存、读回，再进行每条严格残差计算。数组未公开或上传。

runtime是原 immutable Python容器、Python3.12.14、NumPy2.3.5、
python-flint0.9.0、320 bits、Haswell/单线程。owner提供独立
`choose_complete_dyadic_trial_bytes`，使后继可仅重物化该同一有限
载体并严格核原SHA，无需重跑已完成的96条残差或其norm目标。

## 下游范围

这两个完整联合残差是
[DB.24–27](R149-supplement-complete-Theta-row-regularity-and-negative-window-density-inverse.md)
所需的同一输入。必须再消费原同号 Toeplitz $A$ 的完整 signed
作用、其近似误差、以及原 $\overline G$，才能得到真正
$\Theta=V_Q\overline G$ 的实际 signed行和one-loss误差。

本次未解决 physical两个means、真实PDE signed matrices、正侧逆、
$\nu$/phase Schur或非线性嵌入族，未宣称课题完成。
