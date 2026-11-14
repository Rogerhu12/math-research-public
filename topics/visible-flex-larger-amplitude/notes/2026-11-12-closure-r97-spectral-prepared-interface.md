# R97 单完整输入到新46域低谱包围：准备接口

2026-11-12，exact_closure（GPT-6 Astra Pro，AI-assisted）。

当前只保存可执行源码、固定输入和推导；没有重新执行六轮数学，没有声称旧 R96 的帽覆盖 R92。原 R97 已有25门正式成功，但其原多文件输出的本体须先由终端读回。新的恢复入口有明确不同源码和单full schema；不会给原数据伪造该新 source SHA。

## 不变与新输入

实际背景、R90有序Green、逐叶V、R74原二十外端高度及相位不变。新增二十六参数是内头R92的浅高度方向，它们通过完整真实DN进入外投影问题；没有把新方向改成外端非零Dirichlet。

R94已经独立在整个R92乘积域证明同一外侧低46投影的绝对local-V半径9解。由此，R91原每模108倍候选源核的初始包围仍适用，因为该源估计只使用同一个9球和同一个背景；这一步不要求原R74参数量词扩展。

新的head从一份完整R97输出读取：

- mode_rows必须恰46行，顺序2,4,...,92；
- 第m行完整值是 new_complete_Wsigma1.chosen_complete_true_DN_minus_exact_linear.uniform_value_upper；
- 完整宽头值是 whole_low46.Wtau_b1.chosen_complete_true_DN_minus_exact_linear.uniform_value_upper；
- input_identities四项必须为R83、R92、R94和R78的原准确SHA；
- source_sha256必须匹配当前支持的完整恢复源；
- 全部25个原R97门、完整非均值低Q/P恒0、三高块、mean/cuff规范和严格正far均检查。

恢复源为 computations/root_full46_source_cut_transfer_recovered_v2.py，
SHA256 f989a3f2a07b70d0da36be3a05a87509e9d254215d0a11f7726b48b3767189ef。
它目前也处于prepared状态；不得把原正式成功输出改头后伪装为此源的执行。

## 新计算而非沿用旧结论

设该新真实投影为C_new。它满足同一固定线性场与Green式
$C_{\rm new}=L_R+B\beta_{\rm R97}+G\Pi_{\le92}N(C_{\rm new})$。

对每模，重新计算
$fixed_m=L_m+B_m e^{m(18/125-1/64)}\beta_{{\rm R97},m}$，
保持旧真实弱核 $k_m=g_m/(17/16)^2$。
初始帽来自新的fixed项和R91旧9球的通用源项。

随后对这一个新的已存在解实际重新执行六次
$cap_m\leftarrow\min(cap_m,fixed_m+k_m b_m(cap))$。
完整mean正帽、signed半幅、五个保留Neumann项、无限尾和128位向上舍入原样保留。程序必须重新通过全部29门；当前未声称任何新帽或m94源界已经算出。

额外常宽入口同样必须读这个新的完整谱主包并重新算所有230个完整源行和57个支撑块。它不读取旧R96数值帽，不把R94粗总D赋给每模，也不拿新域参数的复Cauchy结论替代实场signed半幅量词。当前谱结论限制于实R92乘积域及共同相位。

## 单full文件和完整重做命令

先读回原R97本体；若确实需要原恢复源重做，其命令为：

~~~sh
python computations/root_full46_source_cut_transfer_recovered_v2.py \
 --r83 notes/2026-11-12-root-r83-complete-cut-difference-r1.json \
 --r92 PATH_TO_EXACT_R92_LEDGER \
 --r94 notes/2026-11-12-root-r94-full46-cut-exact-ledger.json \
 --r78 notes/2026-11-12-root-r78-true-cut-cauchy-r1.json \
 --out FRESH_COMPLETE_R97.json
~~~

R92输入内容SHA必须是
9ef88cdeef25ed0dd688082e53b25b5f8aacda2bd67c9dada61c250cefa4052a；
路径用实际已保存原件替换，不以猜测路径省略身份检查。

新谱入口从课题目录运行：

~~~sh
node computations/closure_outer_low_spectral_r97_v1.js \
 FRESH_NEW_DOMAIN_SPECTRAL.json SHA256_OF_FRESH_COMPLETE_R97 \
 notes/2026-11-12-closure-r91-split-jump-high-exact-ledger.json \
 notes/2026-11-12-closure-physical-green-budget-actions-43303787139-1-interval.json \
 notes/2026-11-12-closure-physical-green-actions-43303787139-1-interval.json \
 computations/closure_outer_physical_green_geometry_recovered_v2.py \
 FRESH_COMPLETE_R97.json \
 notes/2026-11-12-root-r94-full46-cut-exact-ledger.json \
 computations/root_full46_source_cut_transfer_recovered_v2.py \
 notes/2026-11-12-root-anisotropic-auxiliary-family-r3-summary.json
~~~

再以实际完整谱文件的准确SHA运行：

~~~sh
node computations/closure_outer_low_spectral_r97_wide_tail_v1.js \
 FRESH_NEW_DOMAIN_WIDE.json FRESH_NEW_DOMAIN_SPECTRAL.json \
 SHA256_OF_FRESH_NEW_DOMAIN_SPECTRAL
~~~

输出使用全新路径并拒绝覆盖。完整大JSON只经终端git归档或保存脚本/参数/完整哈希；不拆块经集成传送。

## 静态检查与仍待真实执行

两份JavaScript已在V8作语法检查；完整mean/逆的正多项式函数及wide尾数学体与已执行R96源码逐字一致。唯一变化是输入规范、R92域身份、实际head的逐行字段和新结果量词。尚无新的六轮运算、Python原R97恢复执行或wide尾数值结果。

如果终端读回的原R97成功文件采用另一schema，应先另写无损合成器，固定其真实原source与全部input hashes；不得通过改source_sha256字段绕过本入口守卫。当前准备入口只接受明示的单full恢复schema。

m94/96真实中窗有源核仍是首要实际任务；本谱准备不替代R98三档核、低中高反馈、全46切口或闭面条件。
