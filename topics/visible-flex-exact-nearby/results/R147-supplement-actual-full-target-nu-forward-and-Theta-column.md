# R147 ABFP：全 B forward residual 与真正完整 Θν 列的实际证书

2026-11-28。**唯一 BFP19 run46118996598/1 已完整成功。**
同一个完整512-mode reference 的前向残差已控制真正全空间
$x_\nu=\mathcal B^{-1}F_\nu$；原完整 $\Theta$ 对它的96维 signed
readout 也已实际保存。本次没有把 BNC 的低96 target coordinates
补零当成 $x_\nu$，没有使用原 low96 的 Θ 误差替代 global error。

## 1. 全件、原 validator 与真实执行

原输入 manifest 为
[2026-11-28-full-target-nu-forward-inputs.json](../notes/2026-11-28-full-target-nu-forward-inputs.json)，
96504 bytes，SHA256 `363c2116c8459e202209503bc40e379f40d502c89c92c3982971112f602e23ce`。
完整303输入（250 current、53 historical）的旧准入已全部通过；
本次后置再次通过原 BFP public `VALIDATOR` 的全件校验，并由 DCP
新322件联合准入完整重读这份303件闭包。该后置过程没有数值包
导入，没有调用任何旧或新的科学目标。

| 全部原输出 | 文件 | bytes | SHA256 |
|---|---|---:|---|
| actual | `actual-full-target-nu-forward.json` | 40099 | `5ab3a6ed22e4f40b47777f0bdbdfef50f5e52f50f211ef889ebb3ecc406dac16` |
| execution | `execution.json` | 31637 | `0bcb393bb071503c23ee4ebb6d38a28ef40a64b61afaafde19dbad5b2fed6c38` |

[全部19项 actual](../notes/full_target_nu_forward_ci/run-46118996598-1/actual-full-target-nu-forward.json)
和 [完整 execution](../notes/full_target_nu_forward_ci/run-46118996598-1/execution.json)
满足 `complete=proved=true`、child returncode0、failure null、timeout false。
`completed_targets` 恰为全部19项；`old_completed_targets_recomputed=0`、
`old_scientific_target_calls=0`，原结果未覆盖或改写。

事件提交 `bec2ddc1b0acf42269959d2bddb2ae2b3552aadb`，真实科学 checkout
`cd4b3ad61cc675e01037c6d98c0ce5bd0336f1ec`；原 source SHA256
`5373c11e41ada727c7b37b4af5a1d68aac16c600cea2741b3c34cb9229223d3f`。
原 Python3.12.14、NumPy2.3.5、python-flint0.9.0 和320-bit directed
arithmetic 全保。科学 document wall3694.9240458639997秒，外层
child wall3696.075648976秒；这些只是实际运行记录。

## 2. 完整实际目标

使用 [BFP 完整证明](R147-supplement-complete-target-normalized-nu-forward-column-by-pullback.md)
的原参数、归一测度、周期 $\pi/2$ 和物理频率 $4n$。原 trial
的512正频、全2048 signed $\widehat w$、全部2560 forward image、
8192真实 compound pullback点及两 independent physical means 均保留。
所有 finite image、积分、alias、coefficient error、flow error、PDE
error 均先完整保存读回，再进入后继式。

以下18个 scalar balls 按原目标顺序逐字复制；第19项是完整96维
signed conclusion，不再复制其可重构长数组。每条 upper 的合法
数值是其整球的上端，而非打印中心。

| 原次序 | 完整目标 | 全部原 outward ball |
|---:|---|---|
| 1 | `complete_forward_nu_w_trial_Wiener_upper` | `[0.987478528407485185048639283465528708166268480227064041449065 +/- 3.65e-61]` |
| 2 | `complete_forward_nu_true_B_inverse_L2_upper` | `[1.33364444467273360485226015984416070636166893452064484674672 +/- 3.90e-60]` |
| 3 | `complete_forward_nu_trial_L2_upper` | `[0.00157919189125496987637410174099984415832853520568037056597150 +/- 4.58e-63]` |
| 4 | `complete_forward_nu_primitive_L2_upper` | `[0.000393979629506299812108928716417841136838453361497186286104737 +/- 1.02e-64]` |
| 5 | `complete_forward_nu_positive_primitive_Wiener_upper` | `[0.000289757965194357562516920040488627894699708992750378604618324 +/- 3.87e-64]` |
| 6 | `complete_forward_nu_pullback_quadrature_square_upper` | `[3.32320515315478991606182522651142530882785643418829771289502e-17 +/- 1.62e-77]` |
| 7 | `complete_forward_nu_pullback_alias_square_upper` | `[8.33419675476349544112490767142292934143577120368105081992001e-110 +/- 7.52e-171]` |
| 8 | `complete_forward_nu_finite_B_residual_L2_upper` | `[5.76472475765737658176852556144135279438330076539691156660093e-9 +/- 4.82e-69]` |
| 9 | `complete_forward_nu_w_Linf_product_upper` | `[0.000136750034028587759395305348364143950129412390909287624649674 +/- 4.56e-64]` |
| 10 | `complete_forward_nu_w_L2_product_upper` | `[2.64868722148425569743813675129586088047410260700682681152779e-5 +/- 1.74e-65]` |
| 11 | `complete_forward_nu_H_minus_G_density_L2_upper` | `[1.83911838529817805659067902064135038663045997313793256057924e-7 +/- 3.49e-67]` |
| 12 | `complete_forward_nu_true_PDE_density_error_upper` | `[4.51820331755314994853862038873189458539029120090046351180261e-7 +/- 2.02e-67]` |
| 13 | `complete_forward_nu_true_B_residual_L2_upper` | `[2.71283691098853471514760659794573746547374844882375046340827e-5 +/- 3.89e-66]` |
| 14 | `complete_forward_nu_true_target_column_L2_error_upper` | `[3.61795987564299842506331516023866512945472977401809006218243e-5 +/- 2.13e-65]` |
| 15 | `complete_forward_nu_finite_model_preimage_L2_upper` | `[0.00157919189133670531197801341417090598446068859390744033493107 +/- 3.41e-63]` |
| 16 | `complete_original_Theta_trial_Frobenius_upper` | `[10.1235448332915322686105017100136648155105056065399629524627 +/- 5.20e-60]` |
| 17 | `complete_forward_nu_Theta_pairing_rounding_upper` | `[9.18997889785439354744411446225957422036473700439362773313549e-15 +/- 3.11e-75]` |
| 18 | `complete_forward_nu_true_Theta_column_error_upper` | `[0.0316537342916386695096334506257890133378727974771563858745881 +/- 4.14e-62]` |

原参数列误差的完整分解是

\[
 \delta_X=B_{\mathcal B^{-1}}
  \left(e_{\rm finite}+P_w+e_{\rm flow}+e_{\rm PDE}\right),
 \qquad \|x_\nu-\widehat X\|_2\le\delta_X,
 \tag{ABFP.1}
\]

其中 $e_{\rm finite}$ 已包含整个 quadrature 与两条 alias 费用，
$P_w$ 只在已完整保存的 Linf/L2 两候选间整选。其实际保存值是
上表 `complete_forward_nu_true_target_column_L2_error_upper`；
这是一条完整 $L^2$ 列误差，不是低96投影误差。

原 [BFP.22](R147-supplement-complete-target-normalized-nu-forward-column-by-pullback.md)
的全部误差槽由此次实际值给

\[
 \|\Theta x_\nu-\widehat d\|_{\ell^2_{96}}
 \le (B_{\widehat\Theta}+E_\Theta)\delta_X
      +E_V B_{\rm model}+E_M B_x+E_{\rm pair}.
 \tag{ABFP.2}
\]

整球是上表 `complete_forward_nu_true_Theta_column_error_upper`。
原 $E_\Theta$ 是真正 global850.945862…候选；原 low96≈.31698
从未放入该槽。第19项保留所有96个 exact signed rational centers
及全部96个 signed enclosures、ABFP.2 的共同半径和两独立 density
means。显示为宽对称球的项仍使用原 rational center，不能读成零。

## 3. 原完整私有载体的身份

以下完整对象在唯一 run 中保存并读回，公开保留其 whole receipt；
它们不是新的公开数组文件，也不需要下载已丢弃的 artifact。

| 完整原载体 | bytes | SHA256 |
|---|---:|---|
| `complete-alias-components.json` | 523 | `1a4ce83f816b35ec2de4cd100974bf813935a450d8614249e82903034667fa17` |
| `complete-forward-Theta-pairings.json` | 3077 | `5386cfca3a542ae613902c7ca66af04539d933a64580009b011975aa8fb27df8` |
| `complete-forward-image.json` | 4097293 | `de94373a375b154f361839b3cd91ebfb228a741d7af710edc7fd953ed75c35d0` |
| `complete-forward-target-coordinates.json` | 15933 | `528701ecdc1709fdf41c0bc7edce542d9e6454d4bf47b4e0edab510271813be8` |
| `complete-forward-trial.json` | 54179 | `020e57440ed00a3aaa088e63075d49dc4776eeda2093ecb80c2197ddc5778852` |
| `complete-physical-source-coefficients.json` | 2990 | `3d03d929bc576e0a6e1721e824175ee4f07e193db233bde63daa8141c28a29e2` |
| `complete-pullback-input-points.json` | 2088432 | `04660901adf166f4648e883006a1d36bf62318d2edf6b9bef019c9c487f81f8d` |
| `complete-pullback-integrands.json` | 139354 | `63fd221b2fcddaa6ff8f3cf77ccbeb8ebc17c5336dd1f88030a1f252936db33c` |

同一个 UACT whole actual 为
`17c721993bb6488ec48918c50caf70c84785ca54cb004fbc51d11de1c6eb14bc`。
恢复必要系数、grid、trial 或 model 时必须匹配这些全 SHA，不能
重新调用已完成的 BFP forward image、norm、quadrature、alias、
row pairing 或 scalar target。

## 4. 已可执行的直接后继与保持的范围

已成 [WMA](R149-supplement-actual-complete-weighted-model-Theta-receiver.md)
给同一 global $E_\Theta$ 的新完整候选。WMT14+BFP19 的 saved
consumer 只将这一个槽改为两份全候选的完整较小上端，保留 ABFP.2
其余所有槽、全部96中心和两 means；在其自己的实际输出保存以前，
这里不宣称新的 joint error 数值。

[DCP](R149-supplement-particular-density-Theta-and-complete-opposite-leakage.md)
进一步对这同一512-mode reference 计算新 signed density-adjoint
particular 与完整 opposite leakage，替换 ABFP.2 的有限 particular
费用；它的实际目标亦与本次19项不同。本次成功提供其已付全父项，
不预报它的计算结果。

真实 homogeneous physical96、完整高逆/low-high/cross、普通有限
complement、两 means、真正 ν/phase/height border 与全 physical
Schur 仍须分别完成。ABFP.1–2 本身不授完整 regular inverse，
不改变原 actual 的 `full_homogeneous_inverse_or_physical_Schur_proved=false`
与 `topic_completion_proved=false`。
