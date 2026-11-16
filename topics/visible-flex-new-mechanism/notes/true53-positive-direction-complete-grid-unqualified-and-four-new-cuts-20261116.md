# true53 已付 finite 正方向：完整双网不合格及四条新约束

日期：2026-11-16。唯一公开执行 [run 43821568604](https://github.com/Rogerhu12/math-research-public/actions/runs/43821568604)，research job 133145590135，read-only report job 133148800350，二者成功。执行源提交 `323f36fefc0380898aa1e3c0f195e08a32f1fbc1`，工作流 `.github/workflows/visible-true53-positive-direction.yml`。

**本次完整离散一阶方向不合格，未进行标量搜索或 actual 试步，物理接受点仍为53。** 已得到四条确实新增的原始双网行梯度，接下来纳入一个增加这些约束的有限主问题。这里没有不可行性、连续网格或主课题完成的结论。

## 1. 不改原问题的唯一新执行

入口、九个模块、225个源码绑定及全部固定上限见[事前设计](true53-positive-direction-full-grid-and-actual-design-20261116.md)。原 finite 主问题的正方向来自 [既付观察](true53-all-paid-finite-master-positive-primal-20261116.md)，方向SHA为 `3fade7f704238c45a9eca095af36035ab10c4741e059d000359cc9d0600f5e09`。

本次先在原独立159坐标做真实 binary64 加法，再用 candidate−state 得到实际试方向。其SHA变为 `62b27d0586b4c1fc3eeca5770565db8afe0e02715b5a42204c6c286cc8a0f87b`。只有这一条方向接受了完整双网一阶扫描；没有再扫描未舍入理想p。

原 physical 163盒、2937条hard、652条物理范数行、160个上下界均保留；共3909个原domain行，最大残差0，hard最大残差−6.087407892690975e−15，exact163原盒通过。本次只是方向域通过；未评估、未接受该单位candidate。

## 2. 完整两网结果

原两网为160×384和160×768，分别覆盖61440和122880点；每点保原两个谱分支，另保常数target=.26。源完整一阶基值为0.26601514422985395。扫描结果如下：

| 网格 / 分支 | 原flat row | 径向参数 | θ/π | 源branch值 | 原方向斜率 | 单位一阶branch值 |
|---|---:|---|---|---:|---:|---:|
| coarse / 0 | 43322 | 237/400 | 157/96 | 0.26548958508152787 | 0.0007999452218489967 | 0.2662895303033769 |
| coarse / 1 | 91304 | 9/25 | 37/24 | 0.2660127165686538 | 0.00026394255964753293 | 0.2662766591283013 |
| fine / 0 | 86645 | 237/400 | 629/384 | 0.26564815669795666 | 0.0006799979700888418 | 0.2663281546680455 |
| fine / 1 | 182607 | 9/25 | 197/128 | 0.265966257520003 | 0.0003214184384876244 | 0.2662876759584906 |

因此完整离散线性最大值为 **0.2663281546680455**，未惩罚一阶gain为 **−0.00031301043819154106**。原物理范数h=0.2500000110990837，μ=1e−6，范数成本2.500000110990837e−7；最终修复gain为

**−0.00031326043820264013 < 0**。

原guard合法α区间仍为[0,1]，原精确目标区间与原数值容差区间一致，但完整一阶gain不合格，故不进入scalar或actual阶段。原 finite 的正gain7.0414711481267545e−6只属于当时的9658条有限约束，未错误提升为完整网格下降方向。

## 3. 四条新原行梯度

四个branch attainer都未在此前已付行集中。本次仅对这些原行计算完整独立159梯度，每行保原row ID、径向有理参数、精确θ/π、谱分支和源U/T链式来源。没有重算旧hard J、旧finite LP或旧分离方向。

| 原行 | 完整gradient159数组SHA256 |
|---|---|
| coarse / 43322 | `2298b02f46aa14dd4045d61efc27626f2dc73ab131e920e2c0f11288dd07f6df` |
| coarse / 91304 | `b06a196a4abd0187b13ab24556f64f0abb6ad92da303df7944674c0178e9d670` |
| fine / 86645 | `22d0871c16245aa042bbe3f20f8fdc7186de59e5449fa7ff565dbe382812dc65` |
| fine / 182607 | `45daa170424c14eb45f1156feb9bd32c57ab963176874050324913cb4235a3d4` |

原链式比较使用刚已计算的同一JVP，没有额外方向或几何执行；最大绝对差7.26415455565288e−18，源e/f输入差0。四条新梯度含完整de159/df159及必要链式信息，均只在原stdout。它们改变后继有限主问题；不能以这次不合格单方向推断加入新行后的问题不可行。

## 4. 已付输入缓存与状态

本次必要U/T输入恢复一次；没有源点普通geometry、位置/二阶jet组装、旧selected-J调用、旧first-jet重放或159参数轴全网张量。原必要输入及完成的de/df保于唯一CACHE，binding为

`75e07691773d43a00f4aa4192499721ff9490784feaaf18d983ef621e95893e7`。

原MODEL binding仍为 `e095e93d1455302af6904e703e762adad05d9cdef7220761c468e3ea0efca9a1`。大数组、完整检查点和原log没有提交Git、artifact、Release或跨run cache；这里仅列来源和哈希。

接受点53的旧实际记录保留：η细=0.26601514422985384、双网最大κ=57.9992694544513、物理SHA `9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e`。这两个实际数来自原已付接受点，不能以本次一阶基值最后一位的差异替换普通评价记录。原g/b0/159→163族/reference、guard B=.00025、pool及bank/learning账户未另开或改名。

future_positive_direction_checkpoint 是原完整checkpoint更新新方法来源后的对象，canonical子树3424335B/SHA `1bcd1814ae2c336b38b03e448472a88602b759d1930794b342de8422494269e4`。这是规范化子树摘要，**不是原stdout字节摘要**；后继仍以本次FINAL_CLOCK累计数为权威。

## 5. 全费用与原输出身份

唯一新科学钟从imports和source读取前开始，包含输入恢复、新JVP、四条gradient、失败路径及输出。FINAL_CLOCK报告：

- 新科学时间 **50.40678669899998秒**；祖先1608.573003992秒，总计 **1658.9797906909998秒**。
- 必要input restore 1，pair JVP 1（完成两个grid），新原行gradient 4。
- scalar session/query 0/0，actual pair/value 0/0，必要源普通geometry 0。
- 原普通值累计仍128；旧HiGHS/Hildreth/SOC/cone/paid finite调用全部0。
- 新600秒上限未到；全部已启动调用和输入/输出均在同一账内。
- 原记录分段：imports1.2196846630000096秒、两来源log读取3.11145376799999秒、原24输入prepare14.466936099999998秒、必要first-jet输入29.303735292秒、新完整pair .06696294799999691秒、CACHE序列化输出1.5778542639999955秒。分段嵌套，不能再加到总时间。
- 峰值RSS620168KiB；FINAL_CLOCK前数学stdout34680147B，随后FINAL_CLOCK34073B（JSON+LF）。

research原log共 **34802985B**，SHA256 `cde578ee3e7c1046adbf2f7652aa8243679dca3ee1d1f7439938b82adb9c3454`。只读report读取该原log一次，无科学import/重算，未把大数组转发到对话；它的成功不替研究结果作结论。

以下均为原tag后**字面JSON加一LF**，不是规范化子树：

| 原tag | JSON+LF字节 | SHA256 |
|---|---:|---|
| JET_INPUT | 23182 | `b3237220b897a14c1aed9269f71f697ff0838321e50ff9897a2e5dca84ee5d4e` |
| FULL_GRID_SCAN | 56230 | `f6f50ef8de93c4557d2d9d839ef0f28026018773fb099685460267be619d45f1` |
| ATTAINER_GRADIENT #1 | 8467 | `ff90aeae35ed1b498b45967c181a43ab1422217b68fbbf20ca60a34ba727cf59` |
| ATTAINER_GRADIENT #2 | 7413 | `cc7ef9e365226471982d71f48e0d184b6ceb331d232f86c1b60628a490061c90` |
| ATTAINER_GRADIENT #3 | 8450 | `083067d2cc0dc4d141974b4dffb73caeb49eee26342fb941b7cfe2395bcd1567` |
| ATTAINER_GRADIENT #4 | 7442 | `1737644444a0fc8a7d6595031676386aaab0e85235029ea116e133c656363e35` |
| CACHE | 30232607 | `0c1826ad8f554b6eb2c440e54a5582a9711a05b023f4e2756c300d947d854b40` |
| COMPLETE | 4164232 | `e75b0e004db38e57f767603e3f9ec0d00af409e0a87d5b0c74e9f84b1a9461f3` |
| FINAL_CLOCK | 34073 | `4aa795cc7408dd99a4df132d9168d884f56ac58e746a81f67e0df824c1c17d2e` |

## 6. 实际pull与规则差异

研究job在07:07:55.970619→07:07:57.701801 UTC真实执行公开pull，从源323f36fe…到bc1f9608eec4cd1a6461d2ee9c228e5b9a67f04e；根/题README diff都为空。随后私有07:07:59.573012→07:08:00.679095实际pull到e7f96a08a5053b82534b79da96127f7845f44227，私有规则未变、QUEUE本会话唯一进行中。

只读report再次真实公开pull：**07:16:10.728410→07:16:11.300266 UTC**，从323f36fefc0380898aa1e3c0f195e08a32f1fbc1到已读 **d5cf6ec08d71b6b7a7240f051198c9800f5d8c06**，rc0；根blob21bd547f56590b7f2dd279d0297efb289a9b2783、题blobd0432faff569c8e9af7ed4809847e12880976c11，两个diff均为空。

私有同report在07:16:13.147748→07:16:13.478714实际pull，before=after d3d1ace30e939c512b59486f2b69d34eb02f8e8a，根blob5ba164843b1f5802184178a82d786264404873a3未变，题README不存在，QUEUE唯一进行中。没有发表私有正文。下一次actual pull最迟 **08:16:10 UTC**；有变化只读差异并立即照做。

## 7. 本条结论后的实际工作

完整方向结论已闭：这条已付finite方向不合格；四条新梯度和U/T输入已付。现在继续增加这四条真实约束的有限主问题及必要的新完整网格分离，复用已付cache，不重跑本条方向或旧solver任务；若得到合格新方向才接原guard/scalar/全部14门。

η=.266015…是原metric恢复辅助量，并非δhold。固定g误差1e−6、全时C²嵌入、reach比例及精化下降等主完成门仍未达到。理论R471/R472/R473及其它s段问题并行继续，不因本次有限结果、600秒预算或阶段报告停止。
