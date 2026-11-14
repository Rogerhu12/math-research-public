# Request36：幂二均衡无形成损失，但原方程校正仍失败

2026-11-14。本次计算流程完整完成；**没有得到可用的原 native Newton 方向，没有运行非线性试步，也没有新的成功 native 响应**。

## 1. 实际来源

公开 run [43617334081](https://github.com/Rogerhu12/math-research-public/actions/runs/43617334081)，source `6d19fb8c81bebd411ec3863129585dfee261032e`，job `132515188990`（`Mainline nativeequilibrated`）。输入是已锁 actual28 的同一完整有限 A、r、cut/far 和原 σ；没有重算 J。

Artifact `14122758142`，`visible-mainline-nativeequilibrated-43617334081-1`，ZIP 26,081,691 B，SHA256：

`ebb6d62b955093a618fb1a5e354e3ce30bfea0c320382ed03e87d2f4df2430af`。

实际入口 SHA 为 `8f5cb5da0826e3deedf935eca2e62b91c6628861804b2e66c6f853e9459e1dd3`；算法与绑定见 [接口说明](2026-11-14-native-equilibrated-band-interface.md)。[原 result](public-actions-43617334081-1-nativeequilibrated/captured-native-equilibrated-band-correction/result.json) SHA：

`c20256f770e2c64854a93d9b2fc51b4cc890939fc362706ac5c14dc05e547d6c`。

入口实际耗时 32.480485116 秒，记录峰值 RSS 701,460 KiB。LAPACK factor 耗时 0.603487039 秒；初始 solve 0.062482298 秒。所有结论来自公开 Actions 保存的实际数据，本地只读取 metadata；完整原件由根会话统一下载，独立字节复核另记。

## 2. 均衡确实完成，形成与恢复没有损位

以原节点 σ 的最近幂二尺度初始化后，第一轮的原缩放矩阵行/列最大项 floor-log2 范围都是 `[0,96]`。行步之后列范围为 `[-36,0]`；加列步后，第二轮所有行列所需步量都为零，因而实际只发生一轮非零均衡。

最终行指数范围 `[-46,97]`，列指数范围 `[-97,-12]`。每行、每列实际最大项范围均为

$$[1, 1.9999999999847768].$$

没有零行或零列。对全部 29,030,736 个实际形成项，producer 记录：

| 形成读数 | 实际结果 |
|---|---:|
| 非有限项 | 0 |
| 非零形成值舍入成零 | 0 |
| 逆幂二缩放不能恢复原 bits | 0 |

初始 RHS 没有舍入损失或下溢。初解恢复与后续 correction 恢复各含全部 129,248 项，也都为零非有限、零下溢、零不可逆幂二缩放。

这次结果因此不是新形成时的 ratio 舍入、缩放中间下溢或坐标恢复损位造成。它也不意味着均衡后的全系统条件数小，不能把行列最大项都在 `[1,2)` 当作条件数或求解误差证书。

## 3. 两个完整候选的精确原尺度缺陷

初始 factor/solve 与一次 refinement solve 的 `info` 均为 0。每个候选随后都对**全部 129,248 个原 cut/stage/far 方程**做 exact dyadic 读回，以全部实际原 σ 作整数交叉乘比较。

| 完整候选 | 精确全局原 σ 范数 | 实际最坏原行 | 处理 |
|---|---:|---|---|
| iteration 0，初始均衡 LU 解 | `3.727905535268398551668020511575651933427977800419910423331267609e31` | stage43，row220，Pi109，频率218 | 首个候选保留 |
| iteration 1，一次 exact-residual 修正后 | `4.510783064131982963978587010765632390750087409075695460308293626e31` | stage43，row221，Pi110，频率220 | 未改善，停止，保留 iteration0 |

两行位置都是 rawCell0/rawSegment3。这里范数数值是精确分数的十进制显示，最大值比较没有使用显示舍入。两次全行扫描分别耗时 13.285927205 和 13.147221532 秒。所用保存基态 r 的精确原 σ 范数为

`4.177307820740198810865391958317089789308602682333899003945437350e-2`，

对应 stage10、row206、Pi95。它与原 native 显示的 `0.04177307820740199` 有清楚的 exact-array／浮点除法区别。

初解全局最坏原尺度残差的精确值为

$$-
\frac{562909247053783005852290655791567968057611026625707816161541426202315803943}
{15099879589981486688319888220224381861756928}.$$

同一行的普通原顺序 binary64 multiply/add 读数为 `−1.3877359507108687e31`；完整有理读数为约 `−3.7279055352683986e31`。再次表明不能用浮点点积消减后的数替代精确保存数组缺陷。

最终普通浮点读回的 cut 最大值为 0，far 最大值为 `3.549020399923023e−32`；巨大缺陷在内部 stage。完整两次 exact scan 包含边界，故上表给出的是各自保存有限数组的**全局精确范数**，不是仅取一个样点的下界。

精确修正 RHS 的一次舍入也是实际记录：iteration0 有 129,027 行需要舍入，iteration1 有 129,031 行；二者都没有非零下溢成零，都有 112 个 exact-zero 行。原 exact e、行指数和最终 RHS bits 全部保全，不能据“correctly rounded”就说右端完全没有舍入。

## 4. 真实保留对象

Producer 的 `best_iteration=0`，停止原因为：

> Exact original-sigma norm did not strictly improve; previous complete best direction retained

该 best 只是本次候选中所保留者，不是通过原 native 门的校正。全部 129,248 个方向项 finite，负零数 0。

| 保留件 | SHA256 |
|---|---|
| 完整 best 原坐标 δ | `167d9c503d2d85fbd21c5865fe99d0e24d9fe532da0dfa513e22559eec03e215` |
| iteration1 完整原坐标 δ | `3647f7d189de5298fa8af1a9609592b0a537161dd827cc08cb637b2a40609c60` |
| `direction-checkpoint.json.gz`，1,314,946 B | `1578a417431faa9e3670ac4539966e944577af0264a09d366948039ef961b05f` |
| iteration1 checkpoint，1,313,711 B | `97269b181aa1f0f7d6e5572121449f27318a75f790672b76f4c4b843ec3e20a7` |
| `output-array-manifest.json`，17,001 B | `a34a2a8fbefa6c7bdd4f1a132618ca79c91ad02c34eff3b9fe5e8831e634407c` |
| 最终浮点最坏行的完整 exact witness | `ba1efbc3df2caef5b94c3c13b6338d55807d649f8680145117a73865a2353716` |

最终 checkpoint 与 iteration0 checkpoint 逐文件身份相同。两候选、全部 exact-row ledger、原 RHS、恢复增量、行列指数、pivots 和原 σ 下的普通全行读回均保留。大阵仍只在 artifact。

## 5. 本次结论与必要后继

本次具体的幂二 max-entry 均衡、双精度 pivot LU 和一次精确残差驱动修正，仍没有解好保存的有限原方程。它没有证明这些有限方程无解，也没有量出全系统条件数；同样没有把失败唯一归因为原 RK12 传播或局部 J 的精度。

当前方向不进入原十档 nonlinear trial。新的科学结论是：即使形成/恢复均无损且全部行列最大项已均衡，实际原尺度缺陷仍巨大，且一次 exact-residual 修正没有改善。继续盲加相同修正次数没有本次改善证据支持。

[同原 schedule 的 6+6 模块](2026-11-14-native-same-schedule-windows-interface.md) 提供已准备好的下一项有因小计算：仅在已定位的 stage43/58 原入端，把原12步分成原次序的4个短块，保同 profile、各自原 x/h 算式、完整226中间 state 与原出口端口，保存新短块 J 和旧原坐标输出对照；不重算全部576个 J、不增加 ODE 步、不改 far/H/linearSteps。它检验短传播表示这一明确缺口，尚未声称可以解决本次失败。

按 [R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md)，本次 exact 结论只关于保存有限 A、r 的实代数。原非线性流导数误差、真实 trial 下降、完整端点 J 和 fresh audit 均未核销。`native_accepted=false`，本题未完成。


## 6. 完整保存字节的独立读回范围

33个 raw binary 数组及两份 exact ledger（manifest共35项、27,859,185 B）全部文件SHA、形状与格式匹配。三份577×224完整checkpoint逐节点恢复后与raw方向全字节一致，final与iteration00连gzip字节也一致。两轮ledger各578块/129248行，cut→576 stage→far次序完整，每块原J摘要逐段对照actual28原bytes；global/per-block摘要绑定同一存储行、原σ和方向。16个RHS舍入示例逐项绑定ledger pair、row指数与实际RHS bits；没有在本地重算残差或舍入。

两全局见证及另两单行见证的完整J行、next/current δ、r、σ均与原capture/本轮raw逐bit一致。actual28全部29数组/116chunks/238972680 B与fetch receipt的140个文件、三producer/helper SHA再次核过。未导出的LU及assembled band本体仅有producer摘要，不能宣称独立原bytes核；全局最大选择与RN数学也未本地重算。该核验只确认保存证据身份与完整性，不新增native接受门。
