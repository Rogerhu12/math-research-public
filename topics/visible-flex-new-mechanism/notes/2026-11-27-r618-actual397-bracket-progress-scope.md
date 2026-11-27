# R618：同实际397/硬τ1的显式括号进度修复范围

日期：2026-11-27；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

## 1. 新方法直接来自已付原终态

原固定E run45914497186/job140230360702/source
`414b7662f8cddf8a06fb9aa5595cadd69e05ca3c` 自然失败于首τ1输入的第103个均值根。
科学41.515274441秒，完整失败收据为
`2026-11-27-r618-actual397-hard-tau1-first-terminal.md`。
没有获得完整新工作状态、Jacobian或优化步，不能把这个终态称作已证无根。

旧标量程序的Newton候选只要在开括号内就可接受；这没有统一的括号收缩保证。
原log未保存内部轨迹，因此这里只修这项明确实现缺口，不宣称已观测到某一种循环。
本次在同一个固定E、同一τ1输入上采用具有显式进度的标量方法，随后继续原完整全S求解。
不是一次原失败算法的无改重跑，也不是旧DtN、旧fine或旧诊断的资格门。

原实际397完整source/q/H/amp、全体嘴口和定义、J48及全部2J至96从属项保持。
固定目标仍为
`86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5`，
`H=.5188903877153482`、`amp=1e-5`。
原前1472响应为0、硬τ1的新场继续作为起点；没有降低τ、另造q或借后来normal终态修改E。

## 2. 同分支二分规则与明确的进度界

设当前同号导数分支的标量方程为$F(x)=0$，括号为$[a,b]$。
原端点正域、有限性、导数符号和异号条件全部保留。
仍可先消费一次实际seed；更新该点对应的端点后，每个新候选都取

$$
x_{\rm next}=a+\frac{b-a}{2}.
$$

不再通过一次Newton候选位于开区间就继续作没有统一收缩量的更新。
假定精确函数、精确符号及同分支括号条件成立，则每完成一次midpoint更新，

$$
b_k-a_k\le 2^{-k}(b_0-a_0).
$$

本次trial的参考坐标盒半宽不大于`.2`，trial只会嵌套缩小；故初始全宽不大于`.4`。
由于$.4/2^{42}<10^{-13}$，即使最初seed没有产生任何收缩，42次midpoint更新后
也达到原坐标宽容差。再付一次返回状态的函数求值，仍远少于原80次声明上限。
容差继续是$10^{-13}(1+|x|)$，未改大容差或用残差零代替该进度证明。

实际binary64算术分别记录以下终止原因：

- `floating_endpoint_value_zero`：某实际端点函数值浮点等于0；
- `floating_function_value_zero`：实际内点函数值浮点等于0；
- `declared_coordinate_width`：实际括号宽达到原声明容差；
- `floating_bracket_resolution`：midpoint已等于一个端点，无法再表示更细括号。

最后一种返回两个已观察端点中残差绝对值较小者，并保留真实端点、宽度、
残差、导数和分辨率标志；不会把它称作严格根误差证书。
浮点符号、参考E、角求积及原ODE等误差仍需单独包围，二分进度不支付这些误差。
每次失败也保留当时真实括号与最后尝试坐标，不再只剩一条耗尽消息。

参考E的同根标量函数也使用同一显式规则。它的初始括号是原定义的
$[\min B,\max B]$，不冒称该括号也必定宽`.4`；一般进度界为上述$2^{-k}$式。
原参考root的80步上限和容差照旧，如这个实际参考括号仍未完成，就如实保存失败。
原core Laurent target的独立标量程序未在本次改变，其实际成本和未付误差继续保留。

## 3. 固定E函数没有被重新定义

新 `frozen_reference_metric` 与冻结chain原函数逐项AST核对：
仅将内部标量消费入口从旧 `_root` 换为新 `bracket_root`，并显式使用原chain命名空间；
所有$B$、有理化残差、导数、$E/E_r$、$C/M/K$与同根链原公式均相同。
这里更换的是同一连续方程的数值求根策略，不是换一个节点E表或新的平均泛函。

trial继续调用原 `geometry_from_split` 和原 `_connection`。
对于$W\le1$，仍直接使用准确有理化的$\lambda=s/W$方程；$W>1$仍使用$\zeta=Ws$。
同原参考坐标盒、同号导数盒和嵌套trial盒的构造不变。
首失败半径的$W^2$单位量消减不会通过重新引入$(N/u-1)/W^2$而出现。

新composition对象拥有一个真正的旧 `StableCoordinateHeight` 对象；
更深层仍是原唯一factory恢复的完整height对象。
新source SHA和完整 `bracket_progress_adapter` 政策在原模型创建之前进入policy，
随后原response model SHA一次性绑定它们。旧类名、旧source或旧实例身份都不改写。

目标求值与trial均值入口显式转调到新方法；完整height、Jacobian、core方向、
系数、两个primitive及均值积分仍消费已发表公式。
需回调标量根的 `evaluate`、`jacobian`、`coefficient_fields`、
`_mean_point_query`、`integrate_mean_height` 以新wrapper为`self`调用原unbound方法，
从而不会在细网、补充位置半径或积分查询中悄悄回到旧标量程序。
target缓存只接受本新方法已登记的半径；新的来源标签也在消费前核对。

真尾生产者得到的是其policy早已绑定新source的真实原height对象。
双直接位置读出的guard选择新wrapper；其实际位置查询、两组原stencil及诊断计算不变。
新consumer的两个实际执行函数与冻结stable consumer逐项AST相同；只换准确的source/type入口验证。
没有在计算结束后贴上另一个model SHA，也没有修改加载模块的全局函数。

## 4. 新公开范围继续真正求解

保留首范围的全部原工作950×256、fine1728×512、固定mean/core512与canonical高度512。
完整1473列height/Jac仍计算，只有硬τ的零增量准确消元，全部1472活跃列和121600行
进入原完整QR/SVD；所有奇频行和全部奇异方向都保留。
新标量方法之外的方向、函数步长、阻尼/回溯、接受条件以及完整末态读出复用原driver函数。

范围仍为20次更新、science5400秒，其中1800秒留给完整fine、双实际位置与锚定几何。
初damping仍`1e-8`，不伪称已保存上轮未运行的QR状态。
前轮完成102个mean但没有保存完整科学数组，本次必要源重建和新算法求值全部重新记成本；
那41.515274441秒及所有失败计数仍随准确原FINAL身份继承，没有抵消或隐藏。

所有根评价计入原chain分类计数及新的进度计数，失败也先计数后退出。
为避免输出全部径向点与每步轨迹，新进度模块仅保留最近16次标量调用的小收据；
完整总费用始终累积，字段明确这不是全根轨迹。完整场state自身仍有各自root receipt，
原科学数组不因限制日志轨迹而删除。

本次数值真尾合同的`.99≤E≤1.01`仍只是假定整个真实帽至口区间的参考E范围，
不是全body或core的E限制。七类原源误差、参考均值/implicit mean误差、primitive、
角闭合、径向覆盖和reach都未默认0；严格消费器仍拒绝未解决的源合同。
新二分坐标宽达标、完整有限网目标下降或静态小幅根均不等于README宏观完成。

驱动 `scripts/r618_actual397_bracket_progress_20261127.py`；
显式模型 `scripts/r618_bracket_progress_model_20261127.py`；
薄消费器 `scripts/r618_bracket_progress_consumers_20261127.py`；
request `computations/request-r618-actual397-bracket-progress-20261127.json`；
workflow `.github/workflows/visible-r618-actual397-bracket-progress-20261127.yml`。
全部本地准备只含文本、AST、JSON/hash及原已付log解析；没有在本地执行科学探针。

完整新stdin为 `224106 B`，SHA-256
`32e157ee5f7fb8868bf1ccc484a46dfa89535f34a06fe1de28383c4b7dc66dbe`。
其中原参考source和完整数学field文字均逐字保持；旧numerical policy仅增加
`bracket_progress_adapter`，其余所有旧字段逐项相等。准确前失败FINAL文字
`35131 B`/SHA `2b27561b60402679332b45ae8235a02e7aea98a985de8a77c49a0d952bee2856`
作为单独前轮成本记录进入输入，不改参考源文字或目标身份。
request绑定46个源码/工作流/完整定义，全部hash与sparse checkout覆盖已静态核对。
发布时规则metadata可由root按真实已读双仓提交更新，科学stdin不改。

模型及薄消费器已另由 `finite_geometry` 全文独立纸面/AST审读；原参考与trial
两份显式标量消费函数除新根入口及chain命名空间以外的公式均相同，
全部回调及来源身份链通过该审读。没有为此运行任何科学验证门。
