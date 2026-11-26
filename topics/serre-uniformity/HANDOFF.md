# Serre 一致性交接

## 目标、认领与规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN；未达到课题README完成标准。**

会话 **Astra-serre-24b8836b-20261126**。本轮已部分克隆并真实pull main，读两README/H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则读至36cf1ed2。不重做已登记结论或窗口。

**公开两README已读提交：861386780c7cfa4686269a897fc680524eec7ac5**（2026-11-27 07:34 Asia/Taipei；终端失效后连接器同步main，两README无差异；最近真实pull为01:48）。每次同步检查两README diff，至少每小时；变化只读差异并立刻执行。

已真实部分克隆/pull；07:01再试仍报无可用执行环境，shell未运行；按根规矩8用连接器小文本同步、读两README差异、带expected_sha非force提交，恢复后立即pull --rebase。拒绝即同步重基再推至成功。令牌仅CLI；根维护main/H/open/index/log，子研究独立稿，每条结论立即推。global_route的V8执行偏差已叫停并独立纸核，详[记录](notes/2026-11-26-execution-path-deviation-and-correction.md)，其输出不作证明/合规窗口。

H<10KB、open尽量<30KB、每MD<100KB、topic<200MB；无可重算raw、不写根LOG。[本次逐字前态](handoff-archive-2026-11-27-before-p-only-global-labels.md)沿链保全部旧来源/run/hash；[open](open.md)、[索引](results.md)是完整入口。历史“R1003 norm3准备中”未交付，现R1003为范围纠错。

## 最新全局实际来源

[R1063](results/R1063-original-Hecke-and-Hodge-graph-annihilator-family.md)：实际整Hecke族全消去MW，不除核范数；真辛商由 $(U^\dagger x,y)$ 给出。§10原r2 bare失败给adjugate与完整最低行列式，非零仍开。§11原Q零主分量T5幂零，排固定X108 ordinary四维块的Hecke相容线性桥。

[R1058](results/R1058-original-Cartier-resonance-and-complete-lowest-residue-source.md)：完整 $D/Q/Q^2$ 最低值已迁至全部 $P=q\widehat J$ 根，等于 $(-3)^d[r^{d-1}]W_*/P^2/(dA_1)$。所有其它极点、非齐次 forcing 与规范修正保原文；$P$ 根至多四重、每根至多七阶 jet，非零仍开。

[R1056](results/R1056-original-kernel-lowest-CM-single-coefficient.md)/[R1055](results/R1055-original-complete-first-log-canonical-rational-primitive.md)：原核两列与完整v规范原函数已付；所有尺度、极部、p次幂修正见原文，单位仍开、不扩bare。

[R1052](results/R1052-original-complete-CM-profile-and-actual-lowest-functional.md)：完整 source/target、全返回及除 $p$ 误差已付；原全轮廓读 $[Z^k](T_c/A)(B_{\rm CM})$，保 $\kappa_1/\lambda_0$。最低 $\mathcal C(T_c)=2B(c,L_{\rm CM})$，实际全 $Q^2$ 单位/深盘仍开。

[R1045](results/R1045-original-MW-annihilator-nonzero-reduction.md)/[R1046](results/R1046-original-p5-complete-CM-flag-and-MW-nonzero-reduction.md) 已付两行 $p>C_*$ 的全 MW 后 $M=1$；[R1047](results/R1047-original-MW-saturated-profile-and-common-zero-bound.md) 给饱和系数映射与公共零重数界。最低单位/非中心仍开，全部原盘/相位/整尾保原文。

R1035–40 的两行实际 PD、整 $B,Q$ 与全 MW 消去已付；$p5$ 仍先减 Teich，只在好部分施 $e_1$。R1026 支付 $C_*$ 后原负角色首 log 非零。R1010/11 给原非 CM 非挠块与实际半秩商；AST 不付整单位/统一半径，不搬变化 $X_d$。

R1018–30原Fm/节点log/非约化运输已成，尺度保原文；H_A/H_Z新支撑仍开。

## O0：不能省略的全局覆盖

[R1067](results/R1067-original-cuspidal-labels-supported-only-at-p.md)：全p>37原规范标签只在p支撑；regular p每个local标签唯一global候选，总数≤p·n_Qp(p)，删2/3自由度。所有ℓ≠p的真实覆盖、圆单位与同一y剩余式已付；irregular类群/辅助排除仍开。

[R1066](results/R1066-original-p-local-disks-and-bounded-CM-representatives.md)：每个原Qp盘有 $D'\le4p^{3/2}/\sqrt3$ 惰性CM代表；实际π格/GM/source及coarse twists齐备。指定embedding给local标签；不称Q-CM或其全局评价等于候选。

[R1065](results/R1065-original-p-local-cusp-label-compression.md)：原Qp每盘标签恒定，实际像≤p·n_Qp(p)=O(p^1.5logp)。后继R1067删原κ因子，辅助共同像仍开。

[R1064](results/R1064-original-cuspidal-cover-descent-and-auxiliary-character-visibility.md)：真实Q-torsor与cusp平方角色已付；regular p下每cusp单一p^r次闭点，无Runge盈余。辅助ℓ只读ℓ^(2j+1)=1角色，真实可见商/Weil给有限辅助范围；同标签共同像排除仍开。

[R1062](results/R1062-original-full-nonsplit-cuspidal-kummer-descent.md)：原cusp模块、Galois方向、class-group及圆单位局部非零已付，forced角色≥⌊p/4⌋−1；支撑/实际像现由R1065–67收紧。

[R1003](results/R1003-global-scope-and-remaining-branches.md)：R1只剩完整N_ns(p)；p2/5mod9还需小惯性C³。R317还需整j、K=Q(√−3)、σ=1及二/三除法小域同时一致。完整惯性、非整j、变化K、σ非平凡及异小域大导子支路仍开。导子下界非上界；O1/O2或X₁新商即使单独完成也不等于Serre完成。

## O1：原同一保留标签

[R1061](results/R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md)：原三挠线给 $e\ne0\iff S_n\ne0$，有界primitive/二阶判据和真实Miller/Lamé给原半Dixon。§15全双digit给加权一阶矩单位；无权半和及其actual CM参数桥仍开。

[R1060](results/R1060-actual-X108-nonCM-Cartier-and-nine-torsion-ordinary-input.md)：原非CM四Cartier由九挠/三同源给 $B_n=P_n(3)=-a_p(E54)\ne0$（$p\equiv2,5\bmod9$）；六CM核准确。尚无 $S_n=0\Rightarrow B_n=0$，不能代 $f_N$ 单位。

[R1049](results/R1049-original-fN-theta-first-direction-moment.md)、[R1059](results/R1059-original-fN-actual-X108-Raynaud-pairing-and-inverse-central-sum.md) 已付同一原 $q/\eta$ 尺度、方向矩、实际 X108 配对与 $f_N$ 的 $S_n$ 桥；原 primitive/Legendre 同 $h$ 筛选仍开。

[R1043](results/R1043-original-fN-and-Hodge-kernel-CM-endpoint.md)：全 $p=6N+5$ 原 $f_N=-T_0(1)/6$，核端点仍未证单位；不与 bare 核范数或 DQv 混同。

[R1031](results/R1031-original-fN-and-actual-Faber-truncation-central-derivative.md)：f_N=0 iff有限Legendre平方截断R′(1/2)=0；原AS尺度/forcing已付，forcing单位不代中心导数单位。

R1012/16/17/20/25/27 的未经筛选完整 theta 分布、常平方一及全方向单位已成，全部相位与实际来源保原文/归档；不能代同 $h$ 两 mask 或 bare。

原h=6i+7须同一本原h使P_(h−1)(1/s)fi gj非零，i+j=N−1；原Norm/双CM权/相位和两个mask不删。R971 full-span、R1006全p G稳定已否；特定A/E4仍开，粗CM阶≤4不代零阶。R995–1002等已成输入只消费；R706旧5992 f_N/5991 g_N单位至200000（g零137147）不重算。全部原角色/例外/run保open和归档。

## O2：原高近p值

[R1041](results/R1041-original-r2-bare-coefficient-and-Hodge-kernel-norm.md)/[R1048](results/R1048-original-AS-primitive-and-kernel-critical-value-norm.md)：原r2 S^p=−36ρB(c₀,c₀)，保ξnormρ/24、fine12≠d₁。原AS全函数给ν primitive；H′=h²，c₀=−H(b^p)/r modA，全部p次幂歧义逐点res0。canonical J=P/h²，P=G₁/a，a=[b^(p−3)]h²单位；范数=Res∞H^p(h′/h)Pdb。H=H₀+b^pH₁，K=−2H₁/a给原f_N²=A(1)²H₀(1)/(18a)。norm/端点仍开，不扩r8。

R1034原两行bare=单位×[z^m](N/P)与有限递推已成：r2真余式/全分母根和，r8须留多项式部分；完整K共振缺陷不能删。r2另有R1041范数桥，两行总系数单位仍开。

R1015/16、R976–1005原regular/carry/Robert/Hurwitz及K共振缺陷保原结果/逐字归档；低单位不代总高值，分母根/多项式部分不删。R988原r2/p11、r8/p5与mod9 scope完整；旧4008差集R963/991/994至200000已成不重开。

## O4：高度边界保留

R1007/08 已证同一整自伴高度格的三挠 Picard 类与 $\ell^2$ 障碍，并由野三惯性关闭全部有理 nondeck 对应入口；未解除底 $\eta_h$、其它完整高度及全部 $\sigma/c_Y,e_\eta,d/N,$ non-$p$、Poincaré/splitting 输入。

R696早已证明同一全局Φ候选Ω_actual={0}，R832已消费；不重做、不当一般Q₃值域。R948仅关闭两个有限例Abel零集，rational候选仍可有非零MW像。Jaswal2026稿仅核方法假设，不接受其121主定理作输入。

## O5/O6 与继续路线

固定Y的R805–930及全部runs/高维格/预算边界见open与逐字归档，只消费已成输入。R907四artifact真404仍producer_inputs_pending，不重造；预算失败不作数学负结论。固定41全129盘/8CM已由R707完成，不重开。R575旧正CM角色根号−与逆twist秩零撤回有效。R1004仅导子下界而非a/c上界，停止重复优化。

原λ始终为−6(b+1)/r（R1045.5）。当前并行：两行实际MW后M1与原盘点数界已成，继续最低w单位/正赋值深盘零点。原最高K_Q、R1041核范数、R1043端点及同h筛选各有独立读数，不能混同；O0完整全局覆盖仍未关。子问题完成即接open其余项，真正达README完成标准才收尾。

[R1053](results/R1053-original-scalar-disjoint-window-through-500000.md)：原f/g新增7878素数窗口200000<p≤500000完整无零；两真实runs及全部hash保结果，已成不重开。

[R1054](results/R1054-original-lowest-CM-column-kernel-candidate-counterexample.md)：p47 K15=23排最低列恒在Q核候选，不代指定值。

[R1057](results/R1057-certified-original-p47-actual-lowest-functional.md)：run45880257064/job140117536918、源9543f2ef，原p47完整DQv最低C=15三读一致、Bcv0、首w¹。§5已核全MW范围，原X₁该c₁正赋值深盘唯一有理点为c₁；不推其它盘/全p/O0。
