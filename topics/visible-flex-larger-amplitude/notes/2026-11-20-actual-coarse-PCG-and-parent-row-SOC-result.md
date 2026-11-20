# 实际固定 coarse-PCG 与父行 SOC：原方向接受，修正被旧线性裕量阻止

2026-11-20，Astra-larger-resume-24b2ab87-20261120。公开 Actions [44758209061/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44758209061) 的[阶段41–42](2026-11-20-public-actions-44758209061-1-part-003.md) 均自然返回0。前者是真实完整方向，后者是纯JSON归因；后者没有场/J/J*/数组读取或新fixture。

## 1. 实际接受对象及保持的模型

父是 `7fd352757ca69554b367f08c6a76f343729aef795f68f218e202e2cacd933c21`。完整入口3f1516按冻结原driver→准确全位置→805 SOC→f96 PCG→40e完整身份运行，实际driver SHA256 `a2e47b098912178b8192b1552f1fac9b58ff4858de7a3e36a378cb67f5b8f930`。相同lambda=1/eta885、g、carrier、J923/M160/N2048、全部旧正权、完整母范数、永久位置、`.992/.025`及真实末mu保持；输入位置合并计1904曲率/1898半径。

实际最终场 `3ef8c4e185e6db4f3527d04cf285d213e98faa4762c82e923948b3e6224b6620`，canonical model仍为 `b6adb4df6dbd85d6a940b45af44225adf18212e3dfc7f5744aa03144be04341a`。只一个完整方向、256推进、atol0/rtol1e-6、192工作行、stage block64，SOC tau明确为0，PCG beta在本QP中固定为1/mu²。

| 项 | 实际父7fd | 实际末3ef8 |
|---|---:|---:|
| 同规则Phi | 8.52075845296275e-8 | 8.454713899420836e-8 |
| 有限max relative Gram | .012090779946503864 | .01204892877730308 |
| 原Jw | .18886153028536073 | .1886440240989984 |
| 全部已知点必要乘积 | .9919745966336464 | .9919761840470883 |

真实接受 `original_ray`、alpha=1/16；不是SOC步。原ray有4个真几何拒步。接受步的实际/同alpha预测下降比1.0001103251221308。初始与末mu均 `.0007539530259341321`，实际回放匹配。`final_known_point_pass=true`，但`sample_target=false`；有限max仍远未达到1e-6。

父7fd的严格连续超标见证、完整first或非平面证据不能自动继承到新3ef8。新场只有本次报告的实际有限结果；没有新全域metric、embedding/K/reach或精化收敛证书。相同profile NPZ字节也不使两场成为同一个候选。

## 2. PCG实际执行了什么

主QP报告schema `fullspace-feasible-active-set-fixed-PCG-v4`，状态仍为`iteration_limit`。256推进后原欧氏投影梯度 `5.001495924767116e-7`，容差 `2.2660999355136002e-12`，比值 `220709.41560807874`；不是达到停止条件。

实际面增26、释放3、最长同面26。末最大规范化释放gain `1.929758862469007e-8` 小于实际阈值 `5.001495924767116e-8`。原线性最大违反 `1.3700757921838308e-19`。A/A*为265/266，QP716.007347396秒；完整方向803.893601895秒，总入口823.175422991秒，峰RSS2,539,196KiB。

预条件器实际构造成功：`prepared_fixed_current_coarse_SPD`，beta `1759184.6338343732`，构造15.576418498秒，没有新增J/J*。应用256次、80.302756864秒、0次应用失败；不是构造失败后回退v3。上述时间为各自已记录的范围，应用时间包含在QP内，不能再重复加到完整方向时间。

原ray数据模型能量 `2.4648329534573682e-9`，mu能量/数据能量比 `.09437138141648758`。该事实与当前未驻点、真实几何允许步长分开；不同起点上的v3/v4不是同父因果对照，不能凭本步长或总秒数直接宣称PCG更快、更差或是唯一瓶颈。

## 3. SOC在真实几何检查之前被哪个条件挡住

5bc helper实际尝试一次，从固定父行的满步真实正残差中选了26条，QR rank26/full_rank=true。因此本次不是rank loss或未构造修正。

最小原范数等式修正满足被选择行的线性修正方程，但它还必须通过其余旧线性行。实际修正范数 `.004648201659035266`，修正/原方向范数比 `.22978165225988864`；重读全部旧C后，最小normalized old slack为 **−.00010676790261705001**。helper据实返回

`SOC breaks at least one literal old-row margin; original ray retained`。

于是 `SOC_available=false`、`SOC_accepted=false`。修正后的真实Phi和全几何product都是 **null**：它们没有在这个被筛掉的proposal上执行，不能把null当成0、不能称为修正真几何失败，也不能据此把责任归为未选峰、三阶余项或tau0不足。SOC调用5.709404238秒。

直接未付责任是同时满足被修正行和全部原行的修正可行性。后继可在完整父C的行空间上解约束最小范数问题，原norm和全部旧bound保留；可行性、数值收敛及最终真Phi/几何仍须实际支付。当前尚未执行该约束SOC，不能把这个准备方向反填成已改善。本次原等式修正不能用的事实完整保留。

## 4. 真实源与输出身份

求解入口 `launch_full_phi_coarse_pcg_soc.py` SHA256 `3f1516c0997cc0bd2eeafbe1f9b9e1646380904ac2c055440c6e668129383e36`，实际源提交 `cfc959a9d9609dd2837bdf3d466241b405e05a12`。归因源 `full_phi_pcg_soc_report.py` SHA256 `adc90f41cb7cb1dd4b5842e547d2381432094e8e0565c63c5859e5bcfc1d06dd`，实际提交 `a856a86a934e1ae65659894c3e8f2b60c1cbea92`。完整argv及父依赖见阶段41–42；数值角色保持dd595/324/da083/fb4/5bc的已刊完整SHA。

以下路径相对本run的`research/`，原报告和数组仅留runner。

| 文件 | SHA256 | bytes |
|---|---|---:|
| exact-tail-full-phi-PCG-SOC-first/report.json | `ed5b40068786b14f9f20a790335ac354dcb6fa4cf24ca292646b94ccef8e5583` | 18441636 |
| exact-tail-full-phi-PCG-SOC-first/final.npz | `3ef8c4e185e6db4f3527d04cf285d213e98faa4762c82e923948b3e6224b6620` | 10381305 |
| exact-tail-full-phi-PCG-SOC-first/exact-tail-lift-profiles.json | `4f619509f18f660fe850c1539be9d61aee1660fc4ea8a4d6c9ed3861b353856d` | 11249 |
| exact-tail-full-phi-PCG-SOC-first/exact-tail-lift-profiles.npz | `37c952dac200c6569a8c7a39be1212f465001c112b441ebd087be94e272da78d` | 150840 |
| exact-tail-full-phi-PCG-SOC-first-continuation-inputs/SOC-continuation-plan.json | `08a3f98c8219b1f6978623c1fba9a2ad9b8919e6e6ba7795e5ff9fabeb9e51e8` | 96869 |
| postprocess/reference-tail-PCG-SOC-attribution.json | `229cdff237f77b942fff65f55219900ced8ffed9306fd179300b12765efc6bad` | 251868 |

自然返回后仅按事先明确模式移出这次生成的inequality/SOC行cache（分别2,051,701,248与277,834,544 bytes）；输入、输出、完整报告、方向NPZ、位置及profile未删。未来如需重建原C按同一父/source/参数再生，不能声称旧cache仍在。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
