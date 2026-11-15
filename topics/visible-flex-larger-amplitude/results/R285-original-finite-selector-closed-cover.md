# R285. 原 stored 背景的实际48层选择器：完整闭区间读回与连续目标的边界

作者：OpenAI ChatGPT / geometry、root（AI-assisted）；日期：2026-11-15；分类：原源定义诊断、有限算法覆盖证明与独立源码接口。

状态：源码及证明已完成，未执行任何科学计算、工厂构造、selector、区间请求或 fixture。没有当前已接受完整场、实际 E 上下界或新的成功证书。原科学源和已发表 a601e5b5 metric consumer 均不改。

## 1. 先确定这次究竟包围哪个对象

本题 README 要求全部曲面对同一个 $g$ 的全域相对误差不超过 $10^{-6}$，并要求固定 $g$、参数和 $t$ 范围的精化继续下降。它没有把当前 stored 实现的浮点返回值定义成一个新的连续度量。

本次亲读的原 source chain 是：

| 来源 | 原 SHA256 |
|---|---|
| tail_frozen_geometry.mjs | db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3 |
| strong_frozen_calibration_factory.mjs | 77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247 |
| closure_bounded_point_cache.mjs | 35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043 |
| closing_weighted_tail.mjs | 740e672edee58cff7a15f89d75e181577dd439c1c62777c57d0d0ab1af32141e |
| closing_recalibrated_tail.mjs | 4a109f26b0e6c9741dfff678c0fe42da4935bfda9c605e55688e97848aef0dd6 |
| tailnext_balanced_tail.mjs | 928567418f411b70c4040be9ee08be2a78b65e147b8d0c5728f4cf6766a28888 |
| general_root_smooth_tail_cells.cjs | d074799099e27401456449343c8f490ec60cdec7eb0d02758f024f541d409575 |
| exact_20261114_closed_background.mjs | be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b |

最后一件是 sharedB/refined 闭场链真正调用的原背景读出，不能与更早 geometric-tail-background-samples.mjs 的另一条 relative-integral 比较选择器混用。其公开只读出处为 commit ce9807e19bb2ea638987e18c6ba5402bf4adc595，Git blob 6a7d64f438f5e51d60b2b0a926e7a545e387f698。旧 relative 版本 Git blob 74077f2c0d8d9be956fd580884c2b2d417471f0e、SHA256 87dadd4d81dc0d87db23c85cb65e4daffe275674862fcb3ee438014a5183b815，本组件不调用它。

原 frozen factory 只替换前160个已保存 calibration $\alpha_n$ 的来源，并固定保存的 global warp alpha。原 source formulas、浮点运算顺序、物理求积以及辅助 far calibration/transfer 仍保留。它不是一份已经给出连续 $E(r)$ 包络的表。

R26 的题名虽含“真实源”，其第1节明确选择 R15 的新固定实背景：积分、指数、对数指实函数，且 $n\ge160$ 的 calibration 取准确 $65/64$。R31第4.2节的全尾背景曲率只覆盖该 R26 对象。二者不能直接替代当前 stored 数值求值器，更不能把 $B'$ 当目标 slope。

现有 strong_frozen_tail_background_stats 及 v2 也明确称其结果为原 finite quadrature 诊断，未给区间求积认证。本次据此区分：

1. 原数值工厂的确定性标量返回；
2. 下文定义的原有限 selector 的实比较延拓；
3. README 所需的同一个连续目标 $g$。

新的源码只认证第2项的值域，第1项在原 binary64 查询点上与它一致。它不把第2项改名为第3项。

## 2. 原 profile.r 与单独 drdx 不是自动一致的导数

原 entry.point 在 warp 小格中使用保存 cumA/cumB，加原 adaptive G8/G16 partial integral。物理返回是

$$
r_{\mathrm{num}}(x)
 = r_{\mathrm{start}}+\mathrm{orientation}\bigl(A_{\mathrm{num}}(x)+\alpha B_{\mathrm{num}}(x)\bigr).
$$

同一次调用返回的 drdx 则直接读 integrand 的 $dA,dB$，不是对上述有限算法求导。即使暂时忽略舍入、并固定单个16点求积的全部分支，对

$$
Q(a,x)=\frac{x-a}{2}
 \sum_i \omega_i f\!\left(a+\frac{x-a}{2}(1+\xi_i)\right)
$$

也有

$$
\frac{dQ}{dx}
 =\frac12\sum_i\omega_i f(y_i)
  +\frac{x-a}{4}\sum_i\omega_i(1+\xi_i)f'(y_i).
$$

这一般不等于 $f(x)$。更不能因为另一字段 integrand 为正，就推当前 adaptive point.r 的严格单调性。实际求积还含接受条件切换、内部 cusp 切分、保存 cumulative constants、warp 格端点特殊分支和 IEEE 运算。本文没有把这些差异抹去。

原 bounded point cache 的代码只复制相同 point 表达式并淘汰旧 memo entries。新组件直接调用原 factory 和原 profile，不以有限指纹采样来证明所有未采点相同；指纹只沿原 factory 作为既有来源检查保存。全函数身份来自实际调用未修改的、全依赖已由原 loader 绑定的源码。

## 3. 真正的有限 selector

原 exact_20261114_closed_background 按以下顺序工作。

1. 构造全部原 source cells，按 cell $n$ 递增、segment $j$ 递减排列。
2. 只将原返回满足 outer > inner 的 piece 放入列表。
3. 查询半径等于 cut 时用原 cut endpoint；等于 cuff 时显式返回 $w=0,E=1$。
4. 否则用首个满足 inner <= r <= outer 的 piece。
5. 等于该 piece.outer/inner 时直接取 $x=1/0$。
6. 其余半径从 lo=0、hi=1 出发，完整执行48轮：

$$
m=\frac{\mathrm{lo}+\mathrm{hi}}2,\qquad
\begin{cases}
\mathrm{lo}\gets m,&\text{原 profile}(m).r<r,\\
\mathrm{hi}\gets m,&\text{否则}.
\end{cases}
$$

7. 取 $x=(\mathrm{lo}+\mathrm{hi})/2$，从原 profile 返回 logw，再按原两条算式计算 w=Math.exp(logw)、E=1+w*w。

原背景还另算 primitive、wr 和诊断性 radialResidual。新组件不把它们当作真正反函数误差或导数证书；只隔离本次 metric 值域需要的 E。原 E 的两个算式逐字保留，没有把 exp(log(flatSlope)) 换成 flatSlope。

原height/splitPrimitive调用不写回E的输入：已亲读的entry.integrate每次新建六分量输出，integrand每次返回新数组；求和与split只留在背景读出器的局部变量。原point缓存只改变同表达式结果的memo命中，bounded缓存也未改profileSource。因此省略这些与E无数据依赖的primitive输出，不宣称它们已计算、已保存或已认证。

### 3.1 为什么此数值对象本身不能直接充当连续 g

48层二分的中点都是有限集合中的 dyadic 数。每个原 profile 中点返回的比较阈值也固定；最终 $x$ 只能取有限个值。piece 的选择和 cut/cuff 例外也只引入有限阈值。因此，在这些阈值之外的每个开半径区间上，该 selector 的 E 返回是常数。

所以将有限 selector 直接作“以实半径比较原 binary64 阈值”的延拓，得到有限阶梯函数。若在一个连通半径区间上取值非恒定，它就不可能同时连续。此处是条件性的结构结论，没有声称当前每条查询都已实际产生非恒定返回，也没有证明任何不可解或误差底线。

这不妨碍数值 selector 是某个连续原 $g$ 的良好近似；但该解释和求值误差必须另行支付，不能只靠 source function 字样推定。

## 4. 新覆盖算法：只需真实阈值，不需要单调性

查询为闭有理区间 $I=[a,b]$。端点可由有限 JSON number 的准确 binary64 值给出，或显式整数/分数字符串给出。算法内部用 BigInt 分数作所有半径区间比较，未把高精度查询端点舍入回 Number。

先从 I 中按原优先级分出 cut、cuff 单点，再按原 positive-width piece 顺序分配尚未拥有的半径。集合减法保留开闭端点，故两个相邻闭 piece 共有的端点仍属于原 first-match 的那个 piece。没有所属 piece 的子域按原源缺口保留，不补插值。

对一个已分配 piece 的内部子域，任务状态为

$$
(J,\mathrm{lo},\mathrm{hi},k),\qquad 0\le k\le48.
$$

这里 J 可有开端点，所有初始查询仍是完整闭区间。原中点 $m$ 只依赖前面路径，与 J 中具体 r 无关。调用一次原 profile(m) 得到真实阈值 v 后，任务准确分为

$$
J_-=J\cap(-\infty,v],\qquad
J_+=J\cap(v,+\infty).
$$

在 $J_-$ 更新 hi=m；在 $J_+$ 更新 lo=m。二者不交且并为 J，等号明确归原 false 分支。

NaN 阈值按原 JavaScript 比较全部走 false；正无穷同样走 false，负无穷走 true。本组件不把这些值替成理想化有限值；叶端 E 非有限或非正时不产生有限范围证书。

到 k=48 后，调用原 profile((lo+hi)/2) 并读取原 E。该任务整个半径子域的数值 selector 返回完全相同，所以这是完整子域的值，不是中点采样结论。

### 4.1 正确性证明

对 k 作归纳。初始 k=0 的状态就是原程序。假设对任务 J 中每个 r，原前 k 步均已到同一 lo/hi。于是下一次原 mid 相同，原调用的阈值 v 相同。源的严格比较 v<r 在两个精确子域上的真假分别固定，且二者完整覆盖 J。因此归纳命题在 k+1 成立。

到48时，原输出 x 和原 profile 调用都固定，故整任务子域的 E 是所记录的原有限数。初始 first-match 分配和全部二分分割均保持原半径域的完整不交责任；合并全部付清叶的最小/最大原 E 值，即包围整个查询闭区间的有限 selector。

该证明没有使用 $r_x>0$、半径真逆存在、Gauss误差小、缓存指纹采样充分、wr 为真实导数或数值源连续等断言。

### 4.2 中点并没有被另一个舍入路径改变

在第 k 层，lo/hi 是分母 $2^k$ 的 dyadic；k不超过48。其和及除以2在 binary64 的53位有效位范围内可准确表示。最后输出也只到分母 $2^{49}$。新组件逐字使用原 (lo+hi)/2，既保运算又不改变中点的确切词。

对于原本接受的有限 Number 半径，BigInt 对该 Number 的准确 dyadic 比较与原 JavaScript 有限数比较一致。对其间实半径，本文只是明确规定这个实比较延拓，不声称原 JSON 输入或整个 IEEE程序自动接受任意实数。

## 5. 原 adaptive 求积所有分支为何没有遗漏

新组件不在一个 x 区间内选择“代表性”的 adaptive trace。每个实际需要的 selector threshold 的 x 已是固定 dyadic；它直接调用原完整 profile(x)，由原程序执行自己的 profile/cap/warp/求积/缓存分支。

这些原算式包含：

- cap 的两端分支及中间多项式、动态 pulse/valley cap、flat override、cut-preserving末两段；
- 全部六个 integrand 分量；原 G8/G16 接受条件同时读六项，不能只拿 A/B 重建判据；
- cusp splitting 的原保存 breakpoints、warp格floor/cum/total边界、原 partial integrals；
- 原相对接受比较、双子区间递归以及深度16原封顶；
- 进入实际物理profile的原start、alpha、orientation及全部浮点加乘顺序。

由于每个比较所需的固定点调用就是原函数本身，其选中的分支无需再由一个近似解释器猜测；所有可能随 r 改变的后续 mid 则由外层完整48树分支继续承担。未遍历到的 mid 对应完整未决任务，不冒已经包围。

本组件不把 G8/G16差值当真实求积误差，不把两个primitive求法接近当积分证书，也未引入一个替代的 Arb 实积分背景。原 factory 可能执行原有辅助线性 calibration 和 transfer，因此输出没有将这些调用数量写成零；只声明不调用新的非线性尾求解或224列 shooting J。

## 6. 一个有实际用途的原常值支路

原 source 有明确赋值：

- flatOuterThroughCell 为非负整数，flatSlope>0；
- n<该层，或 n等于该层且 j>flatOuterStartSegment；
- 随后不是 n=0 的 cut-preserving最后或倒数第二段。

在这些条件下，profileSource 的 logw 被直接设成同一个 Math.log(flatSlope)，dlogwdx设0。后续 chi/j0只添改别的字段，不再改 logw。所以该 piece 上不论48层比较路径怎样，最终 E 都是同一原有限数。

新代码仅在这个精确源码分支上一次支付整个已拥有半径子域，采用原 endpoint 的实际 logw 与原 exp/平方/加1。它没有凭一个或几个相等样本推常值；也没有将 cut-preserving 的混合段误当常值。其他 cap 平台、深源近零或看起来变化很小的片一律不自动支付。

该快捷分支可能使真实 flat 部分很便宜，但未运行，未填当前支付的格数或实际范围。

## 7. 资源停止与完整未付责任

默认工作资源为600秒、100000个 selector 内节点，可显式调整。这些只是本区间读回器的工作资源，不改原48层 selector、原求积深度或任何 native/FD/fullDN 接受条件。

原factory和单次profile调用不在中途截断；资源只在完整调用之间检查，所以墙钟预算不承诺中断一个正在执行的原调用。

深度优先栈包含所有当前未决 J、所属piece及原lo/hi/depth。资源到期时完整写出该栈；尚未开始的查询保 first/stop 后缀及完整原 query-plan 身份。某原点调用失败时，完整相应半径任务和原错误单列，不从 partial 叶估计整个查询上界。

只有一个查询全部责任付清才输出 certified_finite_selector_E；部分查询仅列 partial_visited_E_range，并将认证字段留空。整份 all_requested_closed_queries_completely_covered 还要求全部请求查询都已有完整报告。资源不足不是几何失败、非单调证明、无根证明或原 $g$ 失效结论。

最坏有限树可达巨大规模，本组件不声称任意非恒定区间都能在默认预算内付清。全域紧包围的后续可行优化必须仍有原函数的值域证明；不能用猜测单调或未证libm误差换取完成标志。

## 8. 新运行件与 CLI

独立运行件：

geometry_20261115_stored_background_finite_selector_cover.mjs

冻结 source 为22356字节，SHA256 65a29ec62834f67a31f8b958304f1f10e0a68023a91d61c05949fec17f3b92aa。

必需输入：

- 原 runtime-computations，含表1前3件和实际 background selector 源；
- 原 source-topic，仍由原 loader 校验完整固定来源；
- 原 config及其完整SHA；
- 原 calibration-ledger ready及完整SHA；
- 原 stored-reference ready及完整SHA；
- 新的本producer输出目录。

所有JSON输入按原文件的magic支持plain或gzip，SHA始终绑定实际原文件；另记decoded bytes/SHA，不将解压后字节冒原压缩身份。可选 plan/queries 均必须同时给真实文件SHA。没有实际闭场时可以省plan；这只运行原背景的有限selector责任，不制造一个已接受场。默认查询为原cuff到cut的整个闭区间。

示例模板不含未产生的未来SHA：

~~~bash
node computations/geometry_20261115_stored_background_finite_selector_cover.mjs \
  --runtime-computations "$COMPUTATIONS" \
  --source-topic "$ORIGINAL_SOURCE_TOPIC" \
  --config "$ACTUAL_CONFIG" --config-sha256 "$ACTUAL_CONFIG_SHA" \
  --ledger-ready "$ORIGINAL_LEDGER_READY" --ledger-ready-sha256 "$LEDGER_SHA" \
  --stored-ready "$ORIGINAL_STORED_READY" --stored-ready-sha256 "$STORED_SHA" \
  --queries "$EXACT_QUERY_FILE" --queries-sha256 "$QUERY_SHA" \
  --budget-seconds 600 --max-selector-nodes 100000 \
  --out "$OWNED_OUTPUT"
~~~

查询 schema：

~~~json
{
  "schema": "original-stored-background-finite-selector-closed-queries-v1",
  "config_sha256": "actual-64-hex",
  "original_profile_fingerprint": "actual-64-hex",
  "queries": [
    {"id": "explicit-closed-query", "left": "actual-rational", "right": "actual-rational"}
  ]
}
~~~

示意字符串不是可运行伪输入。left/right须为实际有限 JSON number，或准确整数字符串、分数字符串；脚本不接受把任意十进制字符串默默转成浮点。查询可为单点闭区间。

runOriginalFiniteSelectorCover 入口先核 GITHUB_ACTIONS=true 和 GITHUB_REPOSITORY=Rogerhu12/math-research-public。它不会在本地执行。未来workflow应保持原Node版本和source恢复身份，并在 scalar读回后删除自己临时生成的可重算raw；本轮不附新workflow、不派发运行或fixture。

## 9. 输出与原metric消费者的明确隔离

主schema为 original-stored-background-finite-selector-closed-cover-v1。主结果包括本次run/source/runtime、原source/输入/manifest绑定、完整query-plan与piece顺序、结果文件和三本完整临时账：

- selector-decisions.jsonl：每个真实内部mid、原阈值词、任务半径域和lo/hi/depth；
- selector-leaves.jsonl：每个已付域、原输入x、原profile字段及w/E词；
- selector-unresolved.jsonl：所有未决任务、资源或原失败原因。

所有raw均为可重算临时输出；只将紧凑summary、脚本、参数、run及SHA用作长期定位，不上传本次raw。本接口遵当前Rule15。

以下字段始终为false：

~~~text
original_continuous_target_g_identification_or_enclosure_proved
C2_continuity_or_exact_inverse_or_monotonicity_proved
a601_missing_original_continuous_g_producer_discharged
actual_accepted_field_created
~~~

因此这个新结果不会伪装成 a601 接口所需的 same-original-stored-tail-closed-E-envelope-premises-v1。不能仅换schema把有限selector范围塞成原连续 $g$ 已证包络。

## 10. 连续目标下一步确切还缺什么

原README的责任仍是一个固定连续度量。现在缺的不是再加一个外部schema，而是原连续对象与实际数值求值器之间的明确数学接口。

若原设计确实指定某个原连续profile $R_*(x),W_*(x)$，须保全部原校准参数、原cap/flat/weight/保护collar、原start及原深部定义，直接给它们的实区间；不能直接换用R26的不同深源。原有限求积、原48层选择、原source累计偏差和基本函数求值误差都进入与此对象的比较。还须明确一个原连续径向函数 $w_*$ 满足 $w_*(R_*(x))=W_*(x)$；该关系不能由有限selector或drdx字段自动提供。

例如在一个已明确的原连续对象上，若已付

$$
|r-R_*(x)|\le\varepsilon_r,\qquad
|\widehat w-W_*(x)|\le\varepsilon_w,\qquad
\left|\frac{dw_*}{dr}\right|\le L
$$

（最后一个导数须在 $r$ 与 $R_*(x)$ 之间的完整区间真实定义并有界，不能拿原独立drdx字段代替），则

$$
|w_*(r)-\widehat w|\le\varepsilon_w+L\varepsilon_r=:\varepsilon.
$$

于是可在当前真实数值 $\widehat E$ 外加

$$
2|\widehat w|\varepsilon+\varepsilon^2+
\left|\widehat E-(1+\widehat w^2)\right|
$$

得到原连续 E 的值域误差。最后一项可由本producer保存的两个 binary64词准确有理计算；它不是把舍入差置零。前两项仍必须来自同一个原连续对象。

该式只是说明有限读回怎样接回原问题，不宣布上述连续包络已经完成。当前源码中能直接确定的是固定数值工厂和明确的近似读出；R26另行定义了新实对象，不能冒充本处缺失的识别。原目标定义一旦从原设计源付清，应沿它做实际区间包围与求值误差，而非给有限阶梯函数增加一个“连续”标签。

## 11. 静态检查的真实范围

终端在本轮中断，未执行Node --check或任何科学。为排除明显语法错误，仅对新源作V8 async-function语法解析：机械移除shebang/import/export语法并将import.meta.url替换成字面值；函数体未调用。所有Node特有导入、路径、原工厂和实际数值仍须由未来真实Actions按原runtime执行。该解析不是一个已通过的科学运行，也不是新的调度门。

来源小文本通过公开GitHub只读接口获取，没有读取大artifact；新source/note仅按根Rule8保全为小文本blob，未改branch/tree/ref。证明不等待fixture，原任务继续。
