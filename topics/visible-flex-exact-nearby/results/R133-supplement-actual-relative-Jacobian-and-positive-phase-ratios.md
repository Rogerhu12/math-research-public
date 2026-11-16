# R133 补充 WJRA：真实相对 Jacobian、正相位比与相对 ω 的首次完整实际界

**状态：已证明的有向包络；已完成首次新计算。** 本页引用公开仓库自身 Actions [43873739440/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43873739440)，不把运行成功解释为有限逆或非线性解。四个完整新结论共56个新球、43个逐字旧球、7个完整原资格对象已经保存；不重算这些已完成目标。

## 1. 精确对象、原域与结论

在同一个已经选定的真实参考成员、同一内禀参数 $\eta_0$ 上工作。严格区间为
$$
I_{\rm strict}=[0,76285779072683/320000000000000],
$$
根区间仍为
$$
[1191984371497/5000000000000,\;2383968743003/10000000000000].
$$
物理角周期 $\pi/2$，Fourier 频率 $4j$。原漂移的标签带宽192与物理带宽768保持区别；原3070个界面、所有短子区间、两特征支、两个输运方向保留。这里的角导数是普通物理角导数，不是已除阶乘的 Taylor 系数。

令 $\chi$ 为原特征流，$J=\partial_\phi\chi>0$。令 $p_\sigma>0$ 为两支真实相位的一阶角导数，$x=(p_++p_-)/2>0$。已证明并由本次有向计算给出完整1至14阶上界的对象是：
$$
\frac{|\partial_\phi^bJ|}{J},\qquad
\frac{|\partial_\phi^bp_\sigma|}{p_\sigma},\qquad
\frac{|\partial_\phi^bx|}{x},\qquad
\frac{|\partial_\phi^b\omega_\sigma|}{\omega_\sigma}
\quad(1\le b\le14).
$$
共同相位/平均值比使用正权平均恒等式，不额外乘2。$\omega$ 的结论保留真实 cut 原子、完整普通 $dr$ 积分与所有原接缝；不从相互独立的上界之差构造一个虚假的比值。

完整证明前驱为 [WJR](R133-supplement-relative-flow-Jacobians-and-positive-phase-ratio-bounds.md)，Git blob
`b6cd802c613f7ec193329af609c63f59a6efded3`，19752 B，
SHA-256 `741df919addd04766685724f1e6d131eef8b03bc6875f9a50ff7de9ad5061c2f`，
已发表于 `19d7802877185806e000d9890e9f7dac389d0977`。本页将其精确有限公式与这次实际文件一一连接。

## 2. 本次计算的完整数学公式

记 $F_1$ 为已经完成的 WX/WBF 正积分比较预算；其资格是同一正算法同时控制所有短区间与两方向的 $\exp\int D$，不只是一个一般流算子范数。记 $t=\operatorname{upper}(F_1)-1\ge0$。先对真实导数方程除以正 $J$，使高阶方程的 $v'\partial_\phi^{b+1}\chi$ 线性项与分母导数项在取绝对值前精确抵消。WJR 给出
$$
\mathcal J_0=1,\qquad
\mathcal J_b=768^b\sum_{k=1}^{b}k!\,S(b,k)t^k,\quad1\le b\le14.
$$
这里 $S(b,k)$ 是第二类 Stirling 数；该多项式各项非负。本次仅计算这一个新有限正多项式，没有求新指数、对数、平方根、分数次幂或重积分原流。

$F_j$（$1\le j\le14$）为完整 WBF 绝对流导数旧球；$c_j$（$2\le j\le15$）为原 cut 相位导数；$m_c>0$ 使用 WGS **真实 cut 下界**，不是全严格区间相位下界。设 $B_{\ell k}$ 为普通指数 Bell 多项式，则
$$
G_0=1,\qquad
G_\ell=\sum_{k=1}^{\ell}\frac{c_{k+1}}{m_c}
B_{\ell k}(F_1,\ldots,F_{\ell-k+1}),\quad
P_b=\sum_{\ell=0}^{b}\binom b\ell G_\ell\mathcal J_{b-\ell}.
$$
本次完整相位/平均值结论保存所有 $P_b$。随后完整复合项为
$$
B_b=\sum_{k=1}^{b}P_kB_{bk}(F_1,\ldots,F_{b-k+1}).
$$
原 WBF 的完整 cut 复合项 $K_b$ 已经完成，只读原球。以实际正权恒等式处理 cut 与普通径向积分，完整相对 $\omega$ 候选是
$$
R_{\omega,b}=\max(K_b,B_b),\qquad1\le b\le14.
$$
每个新记录先写进完整科学文档并原子保存、stdout 打印、原字读回，然后后继公式才从已存球取上端点；只有唯一的真实 cut 下界作为分母取严格正下端点。取阶乘转换只能由需要 normalized 系数的后继使用一次。

因此，后文给出的有限实际球均是上述已证量的有向上包络；证明未使用一个尚待验证的有限维逆或非线性解。

## 3. 六个完整当前输入与一次实际程序

以下是同一次实际的全部当前输入。所有文件均按完整原字、bytes、Git blob、SHA-256 验证，AST 只解析新入口及运维 worker；没有导入旧数学生产程序，没有历史恢复。

| role | 完整路径 | bytes | Git blob | SHA-256 |
|---|---|---:|---|---|
| wgs_main | `topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json` | 72251 | `32ff92c516fcc5c43f3619930d4845d294289270` | `8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e` |
| wbf_actual | `topics/visible-flex-exact-nearby/notes/sharp_Bernstein_finite_flow_ci/run-43870348355-1/actual-scientific-conclusion.json` | 59417 | `df5ea6fff610d70ad98fbebc9dd004d24388ce86` | `87621adee76080dbbc14abdd7f8e5dce5d3e2742ba299fc941d13ff40f4410c0` |
| proof_WJR | `topics/visible-flex-exact-nearby/results/R133-supplement-relative-flow-Jacobians-and-positive-phase-ratio-bounds.md` | 19752 | `b6cd802c613f7ec193329af609c63f59a6efded3` | `741df919addd04766685724f1e6d131eef8b03bc6875f9a50ff7de9ad5061c2f` |
| science | `topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_relative_flow_Jacobian.py` | 68081 | `9a08605e78ca4556a881b9e411f2a6e07be8cae4` | `22f838018bab134e15eb248a4fb0886e64b99275a5fb4c96b2df1d75a1685cca` |
| worker | `topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_small_frozen_public_worker.py` | 25584 | `f966a6a05b18794927c3674956fb617e7dbaa244` | `7abb8783fc3ffc9f3194bb9cab8e1d8c12d28395b9e4b0981c682c879aa39d18` |
| rules | `topics/visible-flex-exact-nearby/notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json` | 2461 | `5c5d020913d717bb5bc8ce891297e00eaa8944f7` | `65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1` |

完整 manifest 为 `topics/visible-flex-exact-nearby/notes/2026-11-16-R133-relative-flow-Jacobian-current-inputs.json`，Git `ba7dadefb3c20c32889503dbe904c78f1b261780`，17518 B，SHA-256 `9ab2e4720d69940c72bc655539a789347c8127084258eac83c705f99b55980c7`。科学 CLI 是：

```text
python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_relative_flow_Jacobian.py
  --repo <actual public checkout>
  --manifest topics/visible-flex-exact-nearby/notes/2026-11-16-R133-relative-flow-Jacobian-current-inputs.json
  --manifest-sha 9ab2e4720d69940c72bc655539a789347c8127084258eac83c705f99b55980c7
  --bits 320
  --out <one new run directory>/actual-scientific-conclusion.json
```

入口环境为公开仓库自己的 Actions；run/attempt 为 `43873739440/1`，运行时 Python 3.12.14、python-flint 0.9.0、320 bits。工作流事件提交 `47d1edc1493504adddf61fb75d64a07e28a2bc5c`；只读预检 checkout 是该事件提交，消耗标记完成后的实际科学 checkout 为 `d6213be67651a3d110fc82e893b5766714c1e7ad`。两者属于不同阶段，不能互换。科学源为 `22f838018bab134e15eb248a4fb0886e64b99275a5fb4c96b2df1d75a1685cca`。

两个完整实际前驱是 WGS437 与 WBF83。WBF 内保留 WDG80、WGS 原伴随文件、全部原资格以及旧 formatter 失败与科学成功的区别；本次没有把旧发表失败抹成成功。43个原记录恰为14个绝对流记录、14个 cut 导数、14个完整 cut 复合项、1个真实 cut 下界。

三个独立重建的完整对象身份为：

| 对象 | 个数 | canonical bytes | SHA-256 |
|---|---:|---:|---|
| 逐字原 scalar records | 43 | 5005 | `5802fe40aa3c5c97cc43d2dd33d585d8dc93e1645f72137d4913fce5511228ce` |
| 完整原 scopes | 7 | 27960 | `ca0833a5d3dfe73575e871c607d2f6435824e12a4ee360f17ae3f101690143d4` |
| 全部 accepted 原资格与依赖回执 | 完整对象 | 20412 | `5e1d7dbe6ec66c06e8b2974e90f08c8229f38336c16b8d33625e35057b178b27` |

本次 actual 与预执行独立原字重建完全一致；所有数组位置与非球资格保留，未用截取几个标量的投影替代完整来源。

## 4. 完整新结论的类型与实际球

以下四个完整图位于唯一的科学文档 `complete_new_graphs` 中，每图14个新球，共56个。每图保留原严格区间、普通物理角导数资格、真实正 Jacobian 先除后估计、完整原 cut 与所有短流范围。

| 完整图键 | new_records 键 | 阶数 | 新球数 |
|---|---|---|---:|
| `complete_new_positive_phase_average_ratio_conclusion` | `ordinary_common_positive_phase_and_average_ratios_1_through_14` | 1–14 | 14 |
| `complete_new_relative_Jacobian_conclusion` | `ordinary_relative_Jacobian_orders_1_through_14` | 1–14 | 14 |
| `complete_new_relative_bulk_transport_conclusion` | `ordinary_bulk_contribution_orders_1_through_14` | 1–14 | 14 |
| `complete_new_relative_omega_conclusion` | `complete_strict_relative_omega_angular_orders_1_through_14` | 1–14 | 14 |

四图实际的 `complete=true`、`proved=true`，31个全局科学字段齐备；15个门全部通过，4个 completed_targets 按规定顺序完成，current_target 为空。

### 完整 $R_{\omega,b}$ 原球

下表逐字转录原科学结果；后继取上端点。显示中心不能替代包含显示误差的整个 Arb 球。

| $b$ | 原始完整球 |
|---:|---|
| 1 | `[532326.832565072372635863769124235511045288459057298616966146124402631188265 +/- 4.92e-70]` |
| 2 | `[588274307508.374471907116169577612543746217893628624042113538646469287463771 +/- 9.04e-65]` |
| 3 | `[975152612762357688.484440476802880450822149281959880368040766562313286585224 +/- 2.55e-58]` |
| 4 | `[2155303013604436754076287.68545007261710824117379271035561427385398734412683 +/- 4.68e-51]` |
| 5 | `[5954680670921099052130925894459.37895319740186554001819696190339170444321441 +/- 3.33e-45]` |
| 6 | `[19742113714602128869303222070557192657.3803917570740908485891292822079366932 +/- 9.38e-39]` |
| 7 | `[76362256780285234431583418549001155347718326.2217689783949623335157829079810 +/- 4.57e-32]` |
| 8 | `[337565765057379068501336175660663470410916016647612.212980173848163036419152 +/- 3.48e-25]` |
| 9 | `[1678775764224175879782784770073592396887503313550264399408.72755865697192057 +/- 3.06e-18]` |
| 10 | `[9276544728104295647807173869447669611054993128459646077691828775.55945290348 +/- 1.80e-12]` |
| 11 | `[56386345824349736824637966790979388623397647507321689533108923776208300.6534 +/- 2.42e-6]` |
| 12 | `[3.73896543459600488695791785106341594500365821614846328314010660781670562665e+77 +/- 3.57e+2]` |
| 13 | `[2.68591393307763415482236188201443561319087423266027185202892939161281441933e+84 +/- 2.25e+9]` |
| 14 | `[2.07786961648468392433612261033040065647628993365886467642506626714551390640e+91 +/- 1.27e+16]` |

### complete_new_positive_phase_average_ratio_conclusion

首阶原球：`[19839.1178235962011081929822784687995067113369836738843572345737926974288559 +/- 6.42e-73]`。

第14阶原球：`[163507823527106736147651662021520077768447857988924684147532134977273802.058 +/- 4.23e-4]`。

### complete_new_relative_Jacobian_conclusion

首阶原球：`[19839.1162561334215548992966285066839741016188755154413588480021858424293059 +/- 4.27e-71]`。

第14阶原球：`[163429051420523734764959734252335599787587993104005936206799927260280773.267 +/- 2.70e-4]`。

### complete_new_relative_bulk_transport_conclusion

首阶原球：`[532326.832565072372635863769124235511045288459057298616966146124402631188265 +/- 4.91e-70]`。

第14阶原球：`[2.07786961648468392433612261033040065647628993365886467642506626714551390640e+91 +/- 1.26e+16]`。


全部其余阶数保存在同一完整科学文档，不需重算。旧 WBF 各目标继续成立且冻结；本次新增的是由真实相对 Jacobian 恒等式得到的不同完整候选。后继可以在同一对象、同一域、同一范数下使用本次候选；不得拿它替换一个绝对导数或第15阶相对导数。

## 5. 实际输出、完成过程与 README 回执

三个完整输出位于
`topics/visible-flex-exact-nearby/notes/relative_flow_Jacobian_ci/run-43873739440-1/`。

| 文件 | bytes | Git blob | SHA-256 |
|---|---:|---|---|
| `actual-scientific-conclusion.json` | 69002 | `80499e42f643e607db47c973b54f2243629a05e8` | `806fbeaaab33ddff424fcfe70e40f83f46d1f85e089f9f01f941ed38ee249660` |
| `execution.json` | 29754 | `942bb43d5bf736696541b95d324c7e02b7c98eda` | `9fd8b53633426dcc5cd3d4cbed10f9a8234481d10f35f7be470c2d2731084df9` |
| `report.md` | 445 | `3e66a5bee550a1a90bc4ab6be81f970361133a4b` | `cf85acb4606ae122f42d0c4ee468b1e0c4e13857fa2513337df7f9b16a2fe18e` |

科学子进程唯一一次，开始 `2026-11-16T13:13:56.382318+00:00`，结束 `2026-11-16T13:13:56.852495+00:00`，返回码0，未超时，实际子进程墙钟 0.47012516600000254 秒；科学程序记录 0.25428651600003604 秒。科学全文有56个新记录、4个新图、43个原球、7个原资格，旧科学调用/旧成功目标重算/新指数/对数/平方根/分数次幂/求积均为0。没有失败或遗失的已打印科学前缀；没有自动重跑授权。

完整 child stdout 为 4354253 B，SHA-256 `97a3dd82c3fc99d68add0f3b149e78b2bfdfd6c5b5641869a5ccb110ed563cbf`；它保留在作业日志，没有复制、分块、下载进对话或提交为大数组。execution.json 为43个实际字段，包含完整只读预检、六个当前输入、两个 AST 回执、全部科学文件身份及4次完整拉取回执。

只读预检返回0，未导入 flint；stdout 21759 B、SHA-256 `a3777427a243c4530b173a3fd0bc17f7406201d26b7a4959b1fb6969914200c9`，stderr 空。预检完整输出与独立重建一致；它明确尚未做新科学计算。

| 次序 | 实际 pull 完成 UTC | before | after | 实际两README diff | 相对已读版本 diff |
|---:|---|---|---|---|---|
| 1 | `2026-11-16T13:13:49.374955+00:00` | `47d1edc1493504adddf61fb75d64a07e28a2bc5c` | `47d1edc1493504adddf61fb75d64a07e28a2bc5c` | 空 | 空 |
| 2 | `2026-11-16T13:13:52.606296+00:00` | `47d1edc1493504adddf61fb75d64a07e28a2bc5c` | `27bc994ddf4de0d49143670b4de058ea946bdaae` | 空 | 空 |
| 3 | `2026-11-16T13:13:55.440765+00:00` | `d6213be67651a3d110fc82e893b5766714c1e7ad` | `d6213be67651a3d110fc82e893b5766714c1e7ad` | 空 | 空 |
| 4 | `2026-11-16T13:13:57.180524+00:00` | `d6213be67651a3d110fc82e893b5766714c1e7ad` | `d6213be67651a3d110fc82e893b5766714c1e7ad` | 空 | 空 |

4次完整回执链 SHA-256 为 `d1fdc1e4fbe7056be0b8975ee09dbc5d7997d9efb7e9fcede8f070c9e7c3ce65`；本页按 worker 的 canonical 链规则独立复核。根 README SHA-256 `6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9`，课题 README SHA-256 `81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220`，均与已读版本相同；本次没有新增规矩差异。

首次预执行课题 199418643 B；消耗标记后、紧接科学子进程前 199419276 B。预执行按完整发表157000 B加120000 B预留检查，标记另有4000 B预算；实际发表按完整实际字节检查200000000 B总限。新 artifact、Release、大数组发表均为0。

## 6. 可以复用的范围与仍未支付的义务

本次完成的是同一实际成员上的普通相对角导数1至14阶预算。它保持 $\eta_0$、真实 cut、根、原方向与3070界面不变；保持完整正 cut 项与普通 $dr$ 积分。取真实 $J$ 比值的恒等式已经证明，因此可直接进入同对象的 mixed-jet 构造，不需要重求旧 flow/phase 或积分。

本页**不证明**完整新 mixed-jet receiver 的小量性、带符号96列有限 Schur 逆、物理入射逆、两个真实均值、$\nu$ 与 $\Theta$ 收费、全部七端口/四个腰端点匹配、全阶 tame 或固定度量非线性解。角相对界不是全算子的逆，也不授根处 $T^{-1}$、单支相位径向延拓或复盘范围。局部解析 packet 与原真实根域继续分开。

下一数学步骤是把这些已完成原球作为只读输入，推进 WSM 同严格区间完整混合导数/残差/whole receiver，并推进 WPS 的真实两RHS有限门；已完成 WJR56/WBF83/WDG80/WGS437 不再执行。
