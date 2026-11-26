# run05 实际12–14：完整 gamma/H 初根失败及同点保存矩阵归因

日期：2026-11-26。证据来自公开 Actions [45870334713/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45870334713) 的实际12科学、13完整纯归因和14已保存矩阵纯诊断；[第4卷](2026-11-26-public-actions-45870334713-1-part-004.md) Git blob `5205e2774cfe2338fe0c793e8fa2dbcf2691570a`，46,074字节，SHA256 `a405b9e062fad5884b29bfd2b42ff6b9e60b3ec37dfeda6b7d745e186e8df25b`。

**结果是实际初点端点KKT延拓没有到达原方程，未形成初始场；随后纯读和同点矩阵诊断成功。** 失败不在文件/源码初始化，不能称全空间QP失败；内外metric和restoration方向均为零。所有科学和矩阵数值执行均在公开Actions，本地仅完整小卷/源/参数读取。

## 1. 当前完整输入与显式H

实际reference bundle为`59027f3a144f8f0feb59e378b058178c781856803e6e704db8a6ff689b45d90f`；固定scalar身份为`e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350`。完整当前gamma模型为`4bb06e4198bc38db54512635f1b106bb3772ffe160534f78f1f1ac7cc2f942e3`。

原reference初点SHA为`cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3`，其H字`0x1.f27228dabd944p+0`；此次实际只改末H坐标1333369为已公开固定字`0x1.ec0bc59b655d2p+0`，精确有理值`4328082246413033/2251799813685248`。新初点SHA为`efe12015c07babb2ebe02ca2f9689faa2433e37485249610ee7126a07ba8bd93`。非H字节摘要前后都为`f92b24aa8cfddc5ccc0dfc9c620a1464022f09aa34b4e125f4d2e4b096ddcb6c`；nonheight_byte_identical=true、原初点实际验证true、改H前root cache为空true。模型身份改H前后相同；H是当前原自由变量，不是改固定g。

Q采用新reference完整绑定，当前definition身份`976f9ad62cb67e36a7aa9c8a755671d4e815cbea01af28ace3b31e2031c54452`。18个旧公开字是固定输入参数；没有把本run Q冒作当前矩逆。ea94的same_old_mathematical_g_claimed=false只表示该纯binder不单凭新字节身份作跨reference数学断言；本题另有完整同g来源证明，不能凭此字段删原永久地点。此次实际读入reference locations及本run3/17/21/26/30的完整报告，初始curvature/radius各1851。

完整原变量1,333,370、全metric行45,324,288保留。端点子问题6controls、9维KKT，角隐式维27；代价`(|z/S|²+|v|²)/2`。控制球半径2、乘子球64；原物理端点和dimensionless KKT容差均2e−12。原两wide bubble三节点不变；新增gamma三节点1/16、1/8、3/16。延拓步长.25、最小步0.0000152587890625、growth1.5、shrink.5、每角stage预算64、predictor开；每corrector保24 Newton/18回溯/Armijo1e−4。外预算仍1×16metric、4×64restoration、mu.01、全192选择前缀+幅度/全部永久真筛，但本次尚未进入它们。

## 2. 实际失败而非未尝试

12控制器返回failed/1，用时111.89344418400015秒。13绑定完整初点snapshot，cross_point_backfill=false，归因：

| 项 | 实际值 |
|---|---|
| stop | actual_initial_zero_closure_field_read_failed |
| failure reason | Continuation step exhausted before the original endpoint equation was reached |
| 最后已接受延拓参数min/max | 0.964003324508667 / 0.9640998840332031 |
| continuation rejections | 129 |
| 所有参数到1 | false |
| 最终无offset原KKT复读 | false |
| 已完成当前根/angles solved | 0 / 0 |
| root failure | 1 |
| KKT角求值 | 34312 |
| KKT matrix角求值 | 3176 |
| 9×9求解角尝试 | 2828 |
| 隐式矩阵角行 | 28584 |
| metric/restoration/各自accepted | 全0 |

初/末Phi、metric max、真几何g、末mu及初/末bundle均null。不能把当前root_count=0说成没有做Newton；上表记录了完整实际工作。也不能将本次未达1的shiftedKKT残差与其他初点/另一控制族残差相减作为metric改善。

## 3. 保存的全部129个失败矩阵

14的完整b3d纯入口读取原report已有矩阵和同点状态，不重新F/J/端点求解。report_validated、all_saved_processed、all_diagnostics_available均true；8角，saved_matrices=129、failed_stages=129、failed_stages_without_matrix=0。每矩阵先核同当前完整点、角、当次延拓参数、own state和shifted残差；不得用另一accepted状态的J冒同点矩阵。

| 实际诊断 | 值 |
|---|---|
| A数值满行秩样本 | 129 |
| A数值秩亏样本 | 0 |
| K数值秩亏样本 | 0 |
| A满秩而K数值奇异样本 | 0 |
| reduced L存在负值样本 | 0 |
| 全样本最小A奇异值 | 0.0025739319291210355 |
| 全样本最小K奇异值 | 2.2749536871283423e−7 |
| 全样本最大A条件数 | 426.37913026222094 |
| 全样本最大K条件数 | 2745832936.7208977 |
| reduced L最小特征值及最小绝对值 | 0.9814656626131569 |

完整数值行摘要`941c29ec607978173cd76014ca60b969b6137315f216a70d46fb2eb56f388c5e`。这是明确SVD阈值惯例下的数值诊断，不是精确rank证书。A与K、以及ker(A)上的对称化L须分开讨论；大K条件数不等于已证端点Jacobian秩亏，也没有从上述样本证明全域或连续可达性。

最小K样本角字`0x1.5fdbbe9bba775p-6`，其失败尝试目标参数0.9765625，state摘要`723ceabbd1f0356f6888b12db5c8789aaf6c9ad00e1c1b77dcaec9b6a49855a3`，A最小奇异值0.006196516537047246，reduced L最小绝对值0.9988311915538395，shifted residual0.5928500511544245。same_as_returned_state=true只核该失败矩阵与其返回own state一致，不把它变成已接受根。该矩阵求解的线性残差2.862231879224801e−13、后向比率1.1760425501168047e−19；小线性后向误差不能替代原非线性端点残差。

最后保存样本同一角字、目标参数0.964128851890564；A最小奇异值0.004322429483525212，K最小奇异值0.0000039223638993873206，reduced L最小特征值0.9814656626365518。它是失败目标，不能替换上节实际最后已接受参数。SOSC_verified=false、global_minimum_verified=false、exact_rank_certified=false；失败点的数值正reduced L不能被称作可行KKT点的二阶最优性证明。

## 4. 全部实际来源和输出

| 角色 | 完整身份 |
|---|---|
| 科学12 source commit | `4775dd9a8e8d351ea94be0e39d2c683dfb572829` |
| launcher | `da41136c61e333cf4835e7209565b5502deac8d2a6bcc91d6cc4a863c2228953` |
| driver | `8f37529deaa8e07d4561e00371b39b82cb641a4e52e0790d41555b2ae9e320a9` |
| endpoint | `b712a24a0c0223356b4a53e6aa1fa78ba9cea66e4be39c7ee39931be99cb782a` |
| geometry | `0c4886237d642382a1ae329d36517d5752ba717f0fa1471993bb98769e828f17` |
| new input binder | `ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39` |
| base | `7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf` |
| 完整pure13 | `c3fdd83c29dabeb00974899bb183360da01c57fcf364704759efcc1ac643b9ec` |
| matrix pure14 | `b3d424b30563ad883b3dcbed8aa82537138243a1b7a12a93baf9045b2316347d` |

科学目录`zero-closure-added-gamma-KKT-explicit-H-first`：report `b8a8bd4c849a2d55b9e64efe588e12dd02b77b2121bd0631d7d054135c270fe1`，1,257,660字节；command `6aa72642437e7e8decd9e2089e32047b7c3f8feb786daa8a877e19db0c9fa62a`，16,122字节。完整pure13输出`7170cb95b02bbba303b2a4a881a2049aabae9ead8f738f25fb6ab202b5cdb5c6`，1,178,489字节；这些大对象只在runner读。

matrix pure14输出`8a0aa98befa73cadf0fb7a8c4800c3748e6f0b1bab98b18dc7ef3de21fb369f3`，28,770字节。13耗时5.784804279000127秒、14耗时5.792464756999834秒，矩阵诊断内部秒0.1351813380006206；科学driver总秒107.9118499340002、峰RSS697,512KiB。13/14 summary_errors与missing_outputs均空。12仅3个预设final字段因实际初始失败而缺失，已由13显式null解释；不是另一个科学崩溃或伪成功。

本条新增结论仅为上述真实初根失败和已保存矩阵数值归因。下一新normal或supported-unit输入仍须重新完整读自己的场，不能从本条继承root、SOSC、全角闭合、metric、reach或幅度证书。
