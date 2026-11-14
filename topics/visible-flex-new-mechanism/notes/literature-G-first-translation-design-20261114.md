# R122 最小原式目标：G 的第一个真实平移导数

日期：2026-11-14。独立公开 Actions consumer 设计。源码
[literature_G_first_translation.py](../scripts/literature_G_first_translation.py)
不重编 forcing、W、局部密度或旧 G 分离目标。本次只计算
$\mathsf NG$ 的完整权零响应门，不预先扩为整条轨道。

## 1. 输入身份和目标

消费 run 43645177423 的完整原表达式导出及其 publisher 回执，沿用冻结的 R114 输入校验器和 R117 G 读取器。完整原导出的 gzip/raw SHA、全部根身份、36 个真实三阶模板与旧 $152\to36$ 来源关系继续核对。

额外绑定 R118 的真实成功回执：

- run：43647225907；
- source：b466c3782ae5e3b1a68572065b7505d45e6d8a99；
- 小主报告 13817 字节，SHA256 743594e95eedda896410cc20a30949675899e075bacc262fa5192388dbeba7f9；
- publisher 回执 32065 字节，SHA256 6392f3554aa656c4ab7cadc11c56ed2e4ee5d8a250b857a7d9a1014e8be0e4cc。

只读取它证明 $G\notin R$ 的已完成证书；不再评价旧七列。

在原 Expr/右积分 DAG 上准确实现

$$
\mathsf N\xi=1,\qquad
\mathsf N(q^{(j)})=\mathsf N(\bar q^{(j)})=0,\qquad
\mathsf N I(F)=I(\mathsf NF).
$$

这里不是整个 $\xi$ 导数。profile 与共同右端同时运输，所以原子右积分的端点项由右空 collar 支付。程序拒绝零 profile 次数的原函数和坐标负幂；不偷偷忽略可能的边界或移动极点。两个原 G 模式各自作一次这个真导数，结果必须只有权零。

独立人工接口使用直接有限平移 $\xi\mapsto\xi+d$ 验证幂零指数、嵌套原函数、权降一和与总微分的交换。它不读取真实导出，不评价研究 profile。

## 2. 完整响应、上界与两种有效结论

权零响应必须来自完整八维 $E_8$ 与全部 $W_{36}$，不用旧物理七维子空间替换。准确枚举给 20 个原列。每个原列保持完整外槽和两个对称内槽，两个相位只许同一组实系数。

若 $\mathsf NG$ 已经原式为零或有可证明的 word 零身份，先回原式核验，立即给轨道商维数 $s=1$，不计算不需要的响应。

否则生成这 20 列，在有声 word 代表上作联合有理消元。每条丢列关系必须重新组合**原两模式表达式**并准确验零，才计入真实上界 $r$。代表秩本身不当成真实独立性。

若目标有关系，再从原式复核两个全函数。成功即

$$
\mathsf NG\in R,\qquad s=1.
$$

因为 $R$ 平移不变，以后所有导数都在 $R$，无需继续后面的轨道。

若只剩未消代表，直接以原有理 Volterra 评价这 $r$ 个保留原列和目标。沿用同一实有理 profile 对、同一右锚、两个模式与全部查询点。只有控制模秩达到已证明的上界 $r$，且存在非零 $(r+1)$ 阶增广子式，才报真实非成员并得到 $s\ge2$。原有理 Cramer 泛函由原有理矩阵定义；打印模系数不是有理泛函系数。

模控制秩不足、未出现增广子式或 word 仍有余项而无子式时，都只报未决。即使非成员成功，它也是 universal 权零块结论，不直接排除某一个特殊合法圆。

## 3. 最小公开运行

建议新 lane 名为 g_first_translation。只顺序执行：

~~~text
python -m py_compile topics/visible-flex-new-mechanism/scripts/literature_G_first_translation.py
python topics/visible-flex-new-mechanism/scripts/literature_G_first_translation.py --toy-only --output /tmp/G-first-translation-development.json
python topics/visible-flex-new-mechanism/scripts/literature_G_first_translation.py --output /tmp/G-first-translation.json
~~~

必须先让这一次实际新源码的人工接口成功，再执行研究路径；没有声称本机已经执行 Python 外壳或新 toy。

默认研究预算为 240 秒、RSS 1024 MiB 软轮询，原多项式次数上限 256、1000 万运算检查、24 个查询点、$p=2147483647$、端点幂 8。有理消元位长界沿用 8192 位，仅作为消元的显式界。新的原式组合完成后核最高实际输入 jet，不够的端点正则性直接拒绝。

只处理这一阶。没有自动继续下一个导数，也没有静默加预算或改 profile。

## 4. 输出及失败保留

主输出 G-first-translation.json 小于 90000 字节；完整诊断先保存为
G-first-translation-complete-report.json.gz，压缩上限 2500000 字节。人工检查同样有小主报告及完整 gzip。所有大数据由公开 Actions 终端 publisher 保存，不通过 API 读取 gzip。

小主报告保留来源、运行、当前阶段、NG 原式哈希、已完成列计数、真实响应上界摘要、决定性原式正关系或原式分离子式。全部原依赖的完整有理系数保存在 gzip；若系数异常长，小报告保其数量和 SHA，不把主报告撑破。异常或资源退出仍保存部分 checkpoint 和真实来源；没有结论的阶段不冒研究成功。

原始局部势代表与 frozen profile 都不改。没有执行旧目标再拟合，没有使用 pure m8 投影代替完整两个模式；pure 投影已漏掉 G 的事实正是本次保完整目标的理由。

## 5. 源码冻结

源码 26885 字节，SHA256：

331fea2c1aef154c4d5866e4708f067c555f9fb61f02a11ee32a7f44d25f01f5。

未挂源码 blob 为 2dda7d84b974b73db3ea3824e34e05e04376938c。这里只保存源码和设计；新的人工与真实研究状态均以公开 Actions 的实际回执为准。
