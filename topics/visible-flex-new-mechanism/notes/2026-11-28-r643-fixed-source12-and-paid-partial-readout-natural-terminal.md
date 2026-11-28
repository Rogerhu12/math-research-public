# R643 固定源细网误差及未完位置读数

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。原 [run 46134171516](https://github.com/Rogerhu12/math-research-public/actions/runs/46134171516) / job 140945669998 / source `bc7799966d423e6ee7bb43f19c7a5549c8eb3dbd` 已自然结束。literal FINAL 为 767450 bytes / SHA256 `70ee43cfad39392f013f05ef1404e765eadfcc33405e993d2041b96d20367f61`。本记录只解析已完成结果，没有新科学求值。

原输入、完整费用与可继续字面见[精确接收归档](2026-11-28-completed-receipt-archive-bindings.md)。已有计数可能重叠，不相加伪报独立成本；所有祖先费用和失败继续有效。

## 同一固定 g 的完成部分

原固定目标SHA `86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5`、H=.5188903877153482、幅度单位1e−5、hard_tau=1都未变。1566实际参数排序JSON34141B/SHA `ef327e7d3f2318c1aeee4fe6c1cc89f04d8362fa610b920318feb503a833ec33`，小端SHA `fd52f624848c044ed889d244a7cd101142139ce6b142c3c430551dea7fedeaaa`。

工作网条件η=2.202751809003002e−7；已付1728径×512角细网条件η=2.2061118193341613e−7，取得点(r,θ)=(.3289166666666667,2.061670178918302)。细网F最大9.297804883951894e−11、rG最大3.082201885870602e−8。真实均高改变最大6.568364779267099e−8、斜率1.0025194258141768e−5、二导.004514974359651183；实际共同反射中心偏量1.6773775626419443e−12保留。观察到的法球高度余量 .00022655332483961893 不是全域reach证。

这些小误差为带条件的有限身份读数。原种子、ODE尾、均值、primitive、舍入和全域几何的连续误差债仍在；幅度单位很小，不授宏观完成。

## 费用和真实中断

16819.399119709秒/10新接受，连原2次为12次；原四分之一试点已裁决。11个全J及全因子、341个QR块、10次solve、61次“无可分辨下降”拒绝保留，next_damping=1.8816764231589207e−14，无未接纳trial。

partial_readout 的真实阶段为 complete_fine_coefficients_and_real_mean_height；这部分已经完成，不能重当未做。complete_final_readout=null；两套直接位置stencil尚无完整收据。自然失败记录使用通用RuleChange文字，但实际hourly记录末项是 **TimeoutExpired**，不是已证README修改；前四次pull依次到8485ff4175a42b12ece0fd66db302bbbdde1f654、d6eaf2b581df3774a7253f36380669720773d33b、32cd752bae0a63d665776ad7f4f861cfdb8cdcfa、6eb60310ba818f7f83224568dedfaec2fcc25cb2且规则均未变。没有保留的逐行差异不能事后推造。

续接先继承原partial_readout及complete_consumer_counts，付尚未完成的直接位置部分，再在同固定g推进；已付细网、均高与原四分步不重新归零。
