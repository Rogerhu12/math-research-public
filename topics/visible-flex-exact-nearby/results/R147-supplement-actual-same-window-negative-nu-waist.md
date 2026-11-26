# R147 补篇：同固定负窗的 selected ν 普通源与腰部贡献已实际完成

2026-11-26，visible-exact-astra-198c63d-20261126。

公开 [run45781137624/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45781137624) 已完整成功，job139776609104。唯一科学子进程 returncode0；4/4 条新记录完整、proved=true、failure=null。本文消费实际整件，未重算任何旧源积分、Cauchy 增长、strict 传播、Green 或 inverse。

## 1. 完整实际原件

- [science](../notes/negative_nu_waist_ci/run-45781137624-1/actual-negative-nu-waist.json)：blob 20e79d1dcc04cd9d69b584f67ca68b9ad427b46a，15210B，SHA256 1a06d01060a63eac98aeaa330f130a8ee766ab5ac878634e637f9cea30e1cb70。
- [execution](../notes/negative_nu_waist_ci/run-45781137624-1/execution.json)：blob 686e746cf0708b3f2415da6ce080e34fe5fb010e，13970B，SHA256 eeb4ed157912e742e8d773ca32b04570296973b924f4a92b1a4ec153c30efe2b。
- [whole manifest](../notes/2026-11-26-negative-nu-waist-inputs.json)：11815B，SHA256 b697e8665801a6e4d5120ca312d72a339cc28a2516d6dabd255f56ee79690f2d。
- 新 owner source SHA256 87cade88d1e5844575487c49130cf7806d82a8b5556635f9db3dab7e4f31866d；worker SHA256 17cb1a5c838cba72571880d871df533aad18577b08e28a8b92d9f681f78aff39。
- event commit 586539efadeeb0d8e3694a28f116a4e241bbb51a，实际 scientific checkout 795445705dca5a2a6057737bc6406ed735aa428c。运行实际核 Python3.12.14、python-flint0.9.0、320bits。

29件完整输入逐字绑定；原 S0 summary/process/manifest/source/pilot、D/SP/PW各 execution/manifest/source、全部 source/domain/selected 证明和当前 Nov20 规则均保全。原实际 D/SP/PW 的嵌入 science 逐字重建其原 output hash；旧 manifest 的历史规则记录不修改。原 pilot 的 PHASE_RIGHT 及完整 source aggregate 调用由 AST 核定，两个源确为同一固定有理窗口。

## 2. 四个完整新保存球

下列原样列出实际文件的全部 ball strings，方向均为 upper。它们是 upper-bound 数值的完整包围；后继使用完整球上端，不使用表中显示的中心。

| 记录 | 完整原球 |
|---|---|
| selected_negative_source_from_original_whole_body_upper | `[3.720477284078205826363263120819575147923817247067805056069052375402020e-6 +/- 1.02e-76]` |
| selected_negative_source_from_same_fixed_window_upper | `[1.307203460168587720551204206986607362242082072722582307747455370603530e-6 +/- 2.39e-77]` |
| complete_negative_ordinary_L2_to_waist_density_gain_upper | `[171.3517135268474481583762355259048431303050492388317372209290525707127 +/- 3.96e-68]` |
| selected_negative_nu_ordinary_to_waist_density_upper | `[0.0002239915528281115819208341985044388484638350797922050863083722264407415 +/- 1.59e-74]` |

前两条分别是原 global-to-negative-window 转授与新 same-window 转授；第三条是完整负侧 ordinary 接收常数；第四条是第二、第三条正式写入并读回后的上端乘积。每个候选球先整件保存、读回并核含原 directed upper，才加入 completed prefix。

由这些完整球可直接读出保守严格有理界
$$
 F_G<3.720478\,10^{-6},\qquad
 F_N<1.307204\,10^{-6},\qquad
 G_N<171.351714,\qquad
 D_{\nu,N}^{\rm ordinary}<2.24\,10^{-4}.
$$
原 R147 global 严格界保持；新同窗 full source 严格更紧。这里没有把两个上界相减。

## 3. 对象、真实窗口和完整源域

依[NW](R147-supplement-same-window-selected-nu-source-to-complete-waist.md)，
$$
 s_\delta=F_\nu(Q_\delta,\nu_\delta)-(\partial_r-A_\delta)Z,\quad
 Q_\delta=Q_0+\delta Z,\quad \nu_\delta=\nu_0+\delta,\quad \eta=\eta_0 .
$$
原 centre 为440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47，direction 为6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04。选定参数是原43588332723/1、loss1/250的同一 implicit member，未改为中心或区间端点。使用
$$
 |\delta_*|/10^{-10}<936826/10^6,\quad
 I_N=[0,2383968743003/10^{13}].
$$

原43613560173完整source中同窗full-through160球给 $S_N$；43713242980完整差源给 $D_N$。本次实际组合 $F_N=S_N+(936826/10^6)D_N$，保完整二分量、moving mean、repair和参数 bump，不将 $\delta=0$ 的源免费转授给改变后的背景。

[SC2](R149-supplement-signed-finite-columns-and-full-negative-residual-sources.md) 将原 E.6/E.12 完整二源域接回同 N/SP/PW。根窗第二非均值源未丢弃。把同一 raw $L^2(dr;L^2_\phi)$ pair 限制到 $[0,r_c]$ 和 $[r_c,r_*]$，$r_c=r_+-1/200$，输入分割的平方和给
$$
 D_{\nu,N}^{\rm ordinary}
 \le \sqrt{C_O^2+C_2^2}\,F_N=G_NF_N.
$$
旧 $C_O,C_2$ 整球由 SP/PW literal copies 接入。输出是同一个原腰部 primitive pair 与两个 physical-density means，未加 principal-angle normalization。

## 4. 已付部分与后继范围

这一次只支付所述 ordinary source 的零根、零独立 impulse 线性分量。正侧源和真实根回传、独立 germ/interface/impulse、height/Robin/mean/phase matching，以及完整 incoming inverse 仍独立。不能把这个 waist density 范数改称 raw state、whole-core $C^0$ 或完整 $q_\nu-Z$ 误差，也不能直接与后者的0.005门混用。

旧计算调用、新数组、artifact和Release计数全为0。该四球目标已完成并锁定，只读复用；后续继续真正其余输入及 full inverse，不重跑本目标。题目要求的精确闭嵌入非刚体族尚未完成。
