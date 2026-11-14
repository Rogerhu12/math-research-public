# actual34：带状重解完成，但原系统精确缺陷仍巨大

公开Actions完成了同一保存系统的完整带状分解和回读。新方向的原σ浮点最坏stage读数为 $4.1558709373255425\times10^{30}$；同一行用保存binary64输入作精确有理计算得到约 $5.2938027944720597\times10^{30}$。后者是完整保存矩阵模型缺陷范数的严格下界，不能归为普通浮点dot读数虚大。它不是原非线性flow真导数的认证，也不是全矩阵条件数。

## 1. 运行和原输入

| 项目 | 实际值 |
| --- | --- |
| 公开run | [43615494107](https://github.com/Rogerhu12/math-research-public/actions/runs/43615494107) |
| Source | `1a9f7197de73b81c076383a625256c8e236a6762` |
| Job | `132509540819`，Mainline nativeband，success |
| Artifact | `14122640178`，visible-mainline-nativeband-43615494107-1 |
| 完整ZIP | 9625572 B；SHA `75091ef33ad51f6d50a07d991d1b5701d4c2b4088ce6dddeca7775d3fb1a0269` |
| 科学源SHA | `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390` |
| 原capture result | `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7` |
| 新result SHA | `5e0d6d7f1b9ddc03565fdd62075d9b8d79a89d15078915e591732a0ce46d7dac` |

输入是[actual28](2026-11-14-actual-request28-native-linear-defect.md)已保存的全部原J/r/δ/base/H/σ/cut/far。J为576×224×224，SHA `394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19`；原完整δ SHA `d3734cf4587acbddbc32c80e49223fc6db4e8077190c8c875c22f218219031f2`。同一个原H与全初场没有重新构造或阈值归零。

31/33只在传输发布失败，未执行band科学计算。34的下载器SHA `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859` 先完成目录移动再只读封存；核同原artifact14120548264/235561097 B/ZIP `0ff8e6f597af60f19243b5457c28e8638096c775551b6f3d044dc2d2f1fabeee`。成功小回执SHA `ff86ee550bc9e8f29d441b71fde4b36957ff74826231bbb0212f612efd8ddb52`。原大包未再次上传到34。

## 2. 完整带阵实际执行

方程次序为cut112、全部576×224 stage、far112；未知量为577个节点完整Q/Pi，共129248维。下带宽112、上带宽335，LAPACK带阵560×129248、579031040 B；far保原112项对角图。

`original-sigma`用原节点σ作列尺度，对应方程按原σ作行尺度，形成浮点带阵后分解。原σ SHA `ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc`。所有比例和形成/恢复信息保留，不冒充保存实数矩阵的精确缩放等价。

| 已存读数 | 实际值 |
| --- | --- |
| 行/列最大条目的范围 | 两者均为 `[1, 1.0680702554420665e29]` |
| 零行/零列 | 0 / 0 |
| 额外行列均衡 | 未做 |
| 矩阵非零舍入零/恢复方向非零舍入零 | 0 / 0 |
| dgbtrf / dgbtrs info | 0 / 0 |
| factor / solve秒数 | `0.6448216479999971` / `0.06419242599999819` |
| 全流程秒数 / 最大RSS | `3.8478358979999996` / `669596` KiB |

LU与输入带阵实际共享存储、指针保持；完整pivot向量516992 B已保，可重建大LU不重复存。未调用新J、native、ODE/RK或任何非线性trial。退出0仅表示诊断完成；native_accepted与task_completed都为false。

## 3. 回原方程的全部浮点缺陷

按[R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md)，完整stage缺陷为

$$
e_n=J_n\delta_{n+1}-\delta_n+r_n,
$$

并包括原cut/far行，再按原σ归一化。原δ和新δ流读同一原J，使用原列顺序浮点乘加。原方向的六个raw/scaled stage/cut/far数组逐位复现28。

| 原σ浮点读数 | 原δ | 新band δ |
| --- | --- | --- |
| stage最大绝对值 | `7.3718085303337e40` | `4.1558709373255425e30` |
| stage有符号值 | `-7.3718085303337e40` | `+4.1558709373255425e30` |
| stage位置 | stage43/rawCell0/rawSegment3/row221/Pi110/frequency220 | 同左 |
| cut最大 | 0 | 0 |
| far最大 | 0 | `1.7745101999615114e-32`，node576/row2/mode3 |
| 全部缺陷nonfinite数 | 0 | 0 |

带主元解确实改变并降低了这个巨大读数，但没有取得原尺度小缺陷。info0不替原方程核验。新δ完整577×224、129248项全有限、负零0，原坐标SHA `cca90e77f21a1783e6d27ee83781cb19156f7575ba141ce7983aa0b1b2493e5b`。node43最大分量为Pi112，值 `2.433567891499097e21`，相对其原σ的已存值为 `8.093178833052677e36`；这里明确只引用node43读数，未本地另求全δ最大。

## 4. 完整224项行的精确有理见证

两个见证都使用stage43/row221全部224个J和下一节点δ条目，加原当前δ/r，再除原binary64 σ。每个binary64作为精确有理数解释，全部点积运算只在Actions执行；原operand bits完整保存。

原方向的精确原σ有符号缺陷为

$$
-\frac{132695946624575346440378348777740545590340599822189929469286039303959956510945}{1800045918224035106697069194343612416}.
$$

原件56位十进制显示：

```text
-7.3718089789340532994625148968109555108299406455223720982E+40
```

新方向的精确值为

$$
\frac{9991973096204451653929466699501574164977153698869892838991201051500962929}{1887484948747685836039986027528047732719616}.
$$

原件56位十进制显示：

```text
5.2938027944720596975662930805088451305401596454082090490E+30
```

两行绝对值各自给对应完整保存模型缺陷范数的严格下界，尚非完整exact上界，更不是原非线性flow的精确导数误差界。新行普通float与exact的原件有符号相对差为 `-0.2149554679926457`，因此后续误差修正不宜只重复用普通float消去结果。原方向exact见证在factor之前已落盘，factor失败也保留。

## 5. 完整字节核验

本地只读核19个数组、合计9827464 B，文件SHA/shape/dtype/长度全符manifest。完整checkpoint的577×224 JSON值及负零侧栏恢复为字节后，严格等于新δ raw文件。两个exact见证的全J行、下一δ行、当前δ/r/σ bits均与原28/新34实际文件对应。没有在本地重算点积。

| captured-native-band-correction下的原件 | SHA256 |
| --- | --- |
| input-binding.json | `e55c1430341a516f7f11e279faf8dadaeff2899447160a84da80c108455411c8` |
| assembled-model.json | `f52214fabe82629e21525b5a2b50c026f807a645c9b418711d091ad7b524295e` |
| factorization.json | `9684906302167d15a1b21e5fe6888389cd46926a6f813aaa81f02c2fda71d245` |
| exact-original-captured-worst-row.json | `3f3c43df7d1a0677727745e648b7c217fc674e8bc985646a4539c13e8db56995` |
| exact-new-floating-worst-row.json | `0ee6ac97937462fe54e8cb4012db213c5cf30f545ec1af4003a095c28d31fded` |
| output-array-manifest.json | `83a61c78cb0dfe161bae148dd436ac89a1874dc6f8bd40419077030571d1aafc` |
| direction-checkpoint.json.gz，1314910 B | `7c5864155fb20215ab634f31f29263c45629c27c376cdcfc84e2596ccb75f6c8` |

完整大数组仅Actions artifact，小结果、输入/数组manifest和完整方向checkpoint入Git。原239MB大输入未再次提交或上传。

## 6. 继续同保存系统的修复

当前已有巨大exact缺陷的明确证据，故不把此方向派去重复原十档非线性trial。下一针对同J/r显式幂二行列均衡及原方程误差修正，避免先形成舍入σ比；按实际原σ范数保全每次方向与改善，不改原方程/far/H/最终native容差，不把exact读回另加为README外接受门。

完整原trial replay和全行dyadic residual组件可供后继实际方向使用，不能替代原full-DN新H/J及fresh audit。本题仍未完成。
