# R149 ABGR：完整 signed Gram 与 B 逆96行误差的实际改进

2026-11-28。**唯一 BGR3 run46117818798/1 已完整成功。**
同一个 DWTB96 trial 的9216个 signed Gram entries 已全部算出、
保存、读回。新 whole operator norm 及 whole coefficient product
给真正全空间 $R=E_{96}^{a*}\mathcal B^{-1}$ 的另一完整96行误差。
原 DWTB9 与 BNC7 均保留，未重算任何已成科学目标。

## 1. 完整实际证据

原 [manifest](../notes/2026-11-28-target-B-Gram-inputs.json)
75836 bytes、SHA256
`0205e488d6932e2348725306f7be7e13d9829461b84cdedfe170e3cadeab24d3`，
包含185 current、51 historical 的完整输入。其原完整准入于启动前
全部通过；本次 whole actual/execution 又通过原 public `VALIDATOR`。
后置只读整件并核身份，没有重新运行 Gram 或原 DWTB reducer。

| 全部原输出 | 文件 | bytes | SHA256 |
|---|---|---:|---|
| actual | `actual-target-B-Gram.json` | 8635 | `901e3855e776ca5065bd681067a409afa48fcaddd30154a6d66abcb1359a874a` |
| execution | `execution.json` | 30664 | `2a8018cd8e11ffdcd397efd0fd1b43910f197f280bb0825ce687b86909c084c2` |

[完整 actual](../notes/target_B_Gram_ci/run-46117818798-1/actual-target-B-Gram.json)
和 [完整 execution](../notes/target_B_Gram_ci/run-46117818798-1/execution.json)
给全部3项 complete/proved、child0、failure null、timeout false，
旧 completed targets 与 old scientific calls 均为0。
事件提交 `a0a130784edba0f29dd01e433bb618b030cea173`，真实 checkout
`a25d47200e3bc238250e37230000df43dd0f5cdd`。
科学 source SHA256
`14587219b010a722d416dceb6b8bf9cee584055d8cf29fd40eaf331688eeb197`；
320-bit directed arithmetic 和原 Python/NumPy/flint 版本保留。
科学 wall4941.281153954秒、外层 child wall4942.244019781秒。

## 2. 同一个整个算子的三个新整球

沿 [原 BGR 证明](R149-supplement-complete-target-B-trial-Gram-and-joint-row-error.md)，
$\widehat r_j=|\partial_\phi|^{-1}\widehat y_j$，原全192正频、
对应负频 conjugates 和所有96行均保留。物理周期 $\pi/2$、
归一实 $L^2$ 内积及频率 $4n$ 没有改变。

\[
 \Gamma_{jk}=2\operatorname{Re}\sum_{n=1}^{192}
       \overline{(\widehat r_j)_n}(\widehat r_k)_n,
 \qquad \|IY\|=\|\widehat R\|\le g.
 \tag{ABGR.1}
\]

完整96×96 Gram 的 whole receipt 是1087491 bytes，SHA256
`11256cd945b42d6b6a633b298527d4f3a97899fb372c6e3fe7e1ed695309e8e7`。
全部9216 signed sums 在取绝对值前完成；原 signed entries 全部
保存读回后才做 BGR.4 的完整 Gershgorin bound。没有采用列最大值
替代 operator norm，也没有假设这些 trial 行正交。

| 原次序 | 全部新目标 | 全部实际 outward ball |
|---:|---|---|
| 1 | `complete_DWTB_trial_primitive_Gram_operator_upper` | `[1.03260516394490672655913578036233834783467378225070425895241 +/- 2.83e-60]` |
| 2 | `complete_DWTB_target_w_Linf_operator_product_upper` | `[0.358416478244095309225411641063129533472732375113539336760820 +/- 1.94e-61]` |
| 3 | `complete_DWTB_inverse96_Gram_row_error_upper` | `[0.0968997081979596314717776134869657054117713775409789193865709 +/- 2.98e-62]` |

原 $e_{w,\infty}$、$e_{w,2}$、$F_H$、HS product 和 L2 product
全部直接读取 DWTB9 的整记录。实际三个选择分别为
`new_complete_Gram`、`new_complete_Gram_Linf_product`、
`new_complete_Gram_row_error`。它们依次使用

\[
 P_g=e_{w,\infty}g,\qquad
 P_* =\min(P_g,P_{\rm HS},P_2),\qquad
 e_R^{\rm Gram}=\tfrac12F_H+\tfrac14P_*.
 \tag{ABGR.2}
\]

原完整 row error0.857445102118870…和新完整0.096899708197959…
候选都在实际对象中保留。新值是
$\|E_{96}^{a*}\mathcal B^{-1}-\widehat R\|_{L^2_0\to\ell^2_{96}}$
的全空间上界，不是一个96×96截断 inverse 的误差。全部193–2240
finite residual、2048之后的 infinite coefficient tail、true source
及相位、cohomological divisors 和 alias 费用仍在原整输入中。

原必要 row carrier SHA256
`a55176484d67a63e7ecf74d2eff287bd3d45b796746e6917f92f969d4518e1d3`
与 y trial SHA256
`b12281fc1b7419662c67b1bc44a94745481bab16e202fde1418ae7cacaa6d160`
均未改变。新证明不要求再恢复它们或重算任何已成功的目标。

## 3. 对已成 BNC7 的合法直接应用

BNC7 的整 parent identity 与同一 DWTB9 一致。设其已存完整费用为
$e_{\rm PDE},e_{\rm compound},e_{\rm alias},e_{\rm disk}$，原 physical
receiver 为 $B_H$，原 NP physical trial bound 为 $N_0$。则新的
完整正公式恰为

\[
 e_{\rm row,new}=e_R^{\rm Gram}B_HN_0,
 \quad
 e_{\nu,\rm new}=e_{\rm row,new}+e_{\rm PDE}
                +e_{\rm compound}+e_{\rm alias}+e_{\rm disk}.
 \tag{ABGR.3}
\]

四个旧整费逐字保留，不能从原 joint upper 中相减来制造新费用。
全部96 exact rational centers 和两独立 density means 从整个 BNC7
原 signed record 复制。这些原中心不是宽 symmetric display ball
的打印中心。旧 BNC joint error 候选仍独立保留；只有在新的 saved
consumer 实际完成后，才报告 ABGR.3 的新数值及整候选选择。

这一步仍是 $E_{96}^{a*}\mathcal B^{-1}F_\nu$，不是
$\Theta\mathcal B^{-1}F_\nu$。BFP/DCP 的全目标列与 Θ 作用另有
自己的完整证书。完整 physical high/finite/cross、mean/phase/height
与 true ν Schur 继续保留；本次3项 actual 的 full-Schur/final-family
false flags 没有改变。
