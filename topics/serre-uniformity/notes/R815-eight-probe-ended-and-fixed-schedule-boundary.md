# R815：八 probe 九维格真实结束及固定调度边界

本条登记一次已完成的公开计算，不重做旧 425-prime CRT、三条精确列、三维格或 49 条已登记否定结论。方法见[原八 probe 九维共同分母格](R815-original-eight-probe-common-denominator-lattice-method.md)，此前三列与分母边界见[三列真实结束](R815-three-known-columns-ended-and-denominator-boundary.md)。

## 1. 真正发生的运行

公开 run **43767171070**、job **132974881457**，source commit **278d19202d30d1057960876b508be2de869e8056**。run receipt 的完成时间为 **2026-11-15T22:29:36.797712+00:00**，core 用时 **18.795483531000173 秒**，process exit **2**，wrapper error 为 null。core 的结束原因是已经消费唯一完整九维格及其全部九个返回行，未获准确 \(M_g\)。

实际完成：

- 新 LLL 调用恰一次；维数九；八 probe 的原索引为 \(10,11,12,13,15,17,20,24\)。
- 整数格基变换逐项核得 \(UH=R\)，实际 \(\det U=1\)，故输出是完整原同余格的基，不是其真子格。
- 九行全部消费，得到九个不同且符合原约束的正分母。八个为新准确候选否定，一个与已完成源中的同一候选相同，直接复用旧否定。
- baseline 的同一旧否定也直接复用；没有重算旧 scalar RR、三维 LLL、425 个素数的算术或旧三条精确列。

八个新候选均在原七点交换恒等式的必要位置
\[
(z,\mathrm{output\ row},\mathrm{input\ column})=(0,0,2)
\]
取得精确非零整数残差；字段 component 为 0。这足以否定该候选，不需要再计算同一候选的余下交换子。

## 2. 否定的范围

真实 flags 为 fixed_nine_row_schedule_exhausted=true、candidate_search_exhausted=true、probe_pair_limit_reached=false。这里的 exhausted 只指预先规定的九个返回基行，**不**指所有格向量、所有线性组合或所有可能分母。

每个候选保原三列 \(0,1,271\)，其余条目采用冻结的中心提升规则。故这些否定既不排除同一分母下别的非中心提升，也不证明 425-prime 模数不足，更不证明原 \(M_g\) 不存在。没有新的分母高度矩形或终止界。原 \(M_g\)、\(\Gamma\)、函数 DAG、极除子、\(\eta\) 与高度均未完成。

原深 CRT run **43748439850** 继续；本固定九行入口不再原样重跑。若后续消费这些否定，仍须核对同一原 current、精确列、\(W\)、候选构造及完整分母，不能仅以相同短 ID 或不同精度下的相同分母代替源身份。

## 3. 实际来源和完整小回执

冻结 core SHA 为 **49f8952f6f7d777c164aa1e461db2b4663a76b69a49b2f7ee1e2878b56615d8b**，wrapper **5f0bc8979d13bef8757a33daf112dd0345b436c347353efd04bc10770555e24f**，method **3f11d09c5c0f2dcffe171011d3d1a96c5cc5b983fabfb71f2a45d11b02dfa348**。本次 configuration SHA 为 **b27a3771140534ed7f7d599e971f3a4a40611b38edea1768fb6be1105466279b**。

| 内容 | 字节 | SHA256 |
|---|---:|---|
| 完整九维格证书 | 344585 | 4914f1178d7fff2c711d82939c6b9ecb1df1d2fe3eb5a91a5be852764fbb2312 |
| 原始 LLL 记录 | 171668 | 05dc164b663fa11ce8aef2b5f656e2da95694a31bcc820035549306580e32990 |
| 九行消费 current | 5132 | 6c9f742d8e95a638149e41a74558327d1ba01583128849438532c958cf00c90b |
| 已成源审计 | 113534 | f139d9e3470fdf3b84d4fb8a280b6c65e0ed54267b6315837b78be916550c4e2 |
| baseline 旧否定复用记录 | 7330 | 2f6be7ad9d9618ae1d6fa50dac7e85babe86ace804946846a3e05d6b13221448 |
| 最终证书（complete=false） | 22964 | f62a760d8288ef03bc8f1da59b026b747978cf039690af60bba55e9f6cd5a91c |
| 完整数学阶段清单 | 6858 | a57adfda816d187fb4b268f67f6a96b24eae758064e4ad0b93399841f4985567 |
| core receipt | 1405 | ff0841202fbe8274bc147652790df0cd50ee40d9b5b17b9db25e3a037e2e22c2 |
| run receipt | 741 | 7c8fea506d6608f7f8081ac83a31c1750ef24f56c66aa0559324952450cfacaf |
| public input receipt | 81531 | 1072ffe49df11225751e6a2cb4e04d38daf135d5d51db4ee9adf5e522a699b64 |
| 全输出 manifest（49 项） | 13463 | d19adcca627272165b8ce1ee0a38457a786d23d2696752882996bf80c0da0704 |
| manifest ref | 364 | fd927d5e81e0c9d536ada76adee21e18d7fc9ac3ad6e9040a5947e1bddc6827e |

八条新否定记录依次为：

| candidate ID 后缀 | 否定记录字节 | SHA256 |
|---|---:|---|
| 7179aa67aa0e1e79f447086a51c64778 | 5318 | db9d15a3ae453952b4ebd409e82d8d6646a3f3665ab3d4532b1d1e5a28109595 |
| f0c426dd0a71cd1d5723f2eb30fd0f5a | 5323 | b407c7d8572450a82a4243df27c07c1f3c55ad3f049b72b4ca9899ec9b9fb2ec |
| a945c7a3814dcab1a0e50f6dd663a808 | 5321 | 31f3a7b81940500b7ad28cee2333cde595f3b8835280c39e3f4100d540da27d9 |
| e16d06cad4979669c1a791df194d283f | 5322 | 7869938b8316f87ac445a5d5c234b909f2b315933efff116719efd89ee5eb3e6 |
| f08e067f9de620641084bb9ddb1dbe45 | 5320 | e850362769ba8fa2e360c203b420ca32a28350f69f2a8a6db4b8a56d8cab6b92 |
| 3a3634d3f1b128576d83e5a7f2529856 | 5317 | a0162962aab3dde1867b7985a51b6ad0d98412ff3c0becd16ad9c610c4cc6945 |
| 4ef4e0b476d10b00e64ad5e2fa2dfdf4 | 5325 | 2e7e3c103b4bb7b110bd7eb832a7f03c9399f8b2a1dcc0a060526d18f5135123 |
| fc82b743f3faa7711dc2532dbabd2981 | 5316 | 4ffb5162400af5e486a041bafba07989fb73a712c49041d8b1c9e41933588a42 |

每条均准确指向其 candidate definition 和 early-exact-entry-00，后者均为 complete、zero=false，并声明该位置属于所需完整七点恒等式。

## 4. 保存范围和后续消费

artifact **14183811013**，名为 serre-global-R815-original-normal-derivation-operators-43767171070-1，共 **2732374600 B**，ZIP SHA **21cf154d7f57ac4301dcfab55826530b0e7687401d30283b16acb0a3adbc8d17**；到期 **2026-11-16 22:29:38 UTC**。ZIP 51 项，其中全输出清单 49 项。

必要 source carrier：

- 已成三列及小阶段：12384866 B，SHA **370d937ada432aba918a86ef86ba46e061100c3b4018dc80187219f1b814708e**。
- 原 source bundle：2715514274 B，SHA **4c9a6d1e3c2c462efecabeba826697efbbc04a3357db1a74d8bd06027804a1b5**。
- 前次 probe source：1689309 B，SHA **a5eac0d510a18fd1c1456600bb9cce7022b9e2837232a4d511af6c9e4531f428**。

原 current 仍为 561995095 B / **402379e2b5a0d4b225fda74d798bbb164d77ce7c3001eddca789d0fe602ef27c**，原三列仍为 4423807 B / **ffa005aef7bbcdd32b526db012b9413c85d901dd06d780bed4281bdf10fbfb46**。没有以新失败证书覆盖这些已成输入。

本地仅通过 13 次 range 读取 48 个小文件（含 manifest/ref），传输 2799853 B，逐文件核字节和 SHA，并读取以上实际 schema；没有执行新的数学算术或下载/重算大载体。raw/机器输出仅在一日 artifact，不进 Git、Release 或悬挂 blob。继续原 CRT 及 R836/R837 的独立精确除子路线；主目标仍 OPEN。
