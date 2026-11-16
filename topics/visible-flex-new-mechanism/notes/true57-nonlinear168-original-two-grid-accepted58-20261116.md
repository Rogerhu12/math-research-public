# 真正57全168非线性任务：原两网接受58并完整保存选点二jets

2026-11-16。本文只读取本次公开 Actions 已有 stdout 及其只读报告；没有本地重算几何、J、优化、符号程序或开发检查。上一点和全部旧账见[真正57](true56-small168-seven-exchanges-original-two-grid-accepted57-20261116.md)，本次事前范围见[完整设计](true57-full168-nonlinear-metric-curvature-design-20261116.md)。

**结论：原两网实际接受58。** 从真正57重新支付当前完整168输入，经两次有限问题/两次全网分离，在固定七个真实坐标非线性预测中选 $\alpha=1/4$，一次原actual pair通过14门和准确172盒。两网最大 $\eta$ 从 $.2660070686486975$ 降到 $.26600541463999305$。这仍不是 $.26$目标、固定 $g$连续等距族、全时reach或README完成。

## 1. 原运行和原报告身份

- 公开run [43859882465](https://github.com/Rogerhu12/math-research-public/actions/runs/43859882465)，research job 133273598120，report job 133280067378。
- source commit `0e6fafbf7bce37cd851dfc972b2de1ff3d0d5881`；workflow `.github/workflows/visible-true57-nonlinear168.yml`。
- request `computations/request-true57-nonlinear168.json`，63362 bytes / SHA256 `543ca3ccccac55e918e3f4c2dd5a08ff3ff853cebbe873367346ae0a175b6c44`。
- 原research日志86358161 bytes / SHA256 `346de3d6027e21e3b3d9dc020b0890c14d65e6dc588c2178ee63eff9f12fca3e`。
- 只读report日志7767080 bytes / SHA256 `b57e9954209d964bc2d3165615792b6e1ba1c670f91ff5c8aaf92d51a48da446`。观察器本身12.801075282秒，独立于科学账。

research完成success；report因8MiB语义上限采用projection2，状态 `semantic-size-limited-incomplete`并exit1。它解码46记录、0 parse errors、0重复唯一tag；COMPLETE与权威FINAL_CLOCK均保有原语义。INPUT/CACHE/MODEL等大数组在报告只留原字节身份，部分长数组/历史省略且显式指明；因此不称整个原日志内容已无损转发。本结论消费的实际点、14门、选点导出状态和最终账均可直接读到，不由job success替代数学验收。

## 2. 真正58的原两网结果

| 原量 | coarse 160×384 | fine 160×768 |
|---|---:|---:|
| 直接最大 $\eta$ | 0.26600541430262403 | 0.26600541463999305 |
| 最大绝对主曲率 | 57.998792638483174 | 57.9997782607127 |
| 归一球半径平方最大 | 0.990531522151362 | 0.990531522195588 |
| 最大 $|y|$ | 0.3899899137879593 | 0.3899899137852399 |
| 有限镜像半径最小 | 0.09760648264200214 | 0.09760648264224142 |
| 最小signed height | 0.02 | 0.02 |
| 原14验收布尔 | 全true | 全true |
| 准确172物理盒 | 通过 | 通过 |

原14门包括cap/盒、curvature lambda、scaled PSD、直接主曲率、ball、strip、outer strip、mirror polynomial及独立mirror、regularity、signed height、previous metric和两个原single-grid合取。保持原容差；帽高affine margin为 $-2.7755575615628914\times10^{-17}$，reconstructed margin为 $-5.551115123125783\times10^{-17}$，只是在原 $10^{-9}$数值门内，**不是准确非负积分证书**。

实际最大下降为 **0.0000016540087044436547**，严格超过原最小下降 $10^{-7}$。两网新的 $13/50$目标仍均false；$\eta$是metric辅助量，不能当作握持后的宏观位移。

metric峰两网仍在 $s=.4725,\theta=0$。粗网曲率峰在 $s=.78,\theta=\pi/2$，主曲率对为 $[-57.998792638483174,-2.6246777430697623]$。**细网峰移到非轴** $s=.78,\theta=4.818744981678094$，主曲率对为 $[-57.9997782607127,-1.9318544339231039]$。这两对数来自原direct结果，不据排序将其中一支命名为径向或角向。后继R511必须使用完整形算子 $B,C$，不能把57的轴公式直接沿用为58全圈结论。

原池保持coarse4454/v15、fine4549/v14，无新学习行，无容量退出；池的原顺序保留。

## 3. 当前身份与真正保存的输入

- 58 physical SHA256：`94950b2bd5d7b5241e14333a4315b073f64840f74849a7909d6de8cb3cc29f54`。
- 58 independent168 array SHA256：`e2d52f849596a5e7bbf596b66d7805587acc944c1549c5648ee4e115548ed2bf`，来自实际选中的LINE_QUERY4且原actual同坐标。
- coordinate definition：`c69967fb9b864f3e95da411610b74d5477c58891352895b493aee6e482d960de`。
- complete field evaluation：`81e6881cd1f36d87a865cd9cc8c51ee8480d2ac8278241d97fb19666486eba8d`。
- 本次objective evaluation：`bbdc448df8f7be0d9f1b506aa7a538c56bc335b69f682bf1cdd6d8ec4978f49d`。
- 原cfg `1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19`、固定 $g$ `fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`、$b_0$ `d61fb298989834c9eb2b4fe3bbff1fb5983d1bb3b3980cb6441f14e6c0299bb5`未换。

接受后先完成原pool learning，再从该次paid ordinary内存导出选点完整二jets。原export status `complete`、coarse/fine均complete、errors空、first_jet_cache_complete与selected_export_complete均true；没有额外ordinary或参数J调用。导出耗时0.1914983280000797秒已在总账内，不能再加一次。

接受CACHE2含原完整 $U,T,e,f$、原radial/theta和当前168状态，并新增按接受后原pool绑定的selected $X,X_s,X_t,X_{ss},X_{st},X_{tt},T$与相应径向metric jets。**这不是完整网格二jets或58的新J**；后继只在真实已存行上复用，不伪填全圈或未知hard点，不跨点搬57的J。

CACHE2 binding `28969794748d9b02fee16b90c775d9b41abba4facdfae0781d95f61e5b9040a1`。原selected导出状态单独报告，保留它与actual acceptance不同的逻辑身份。

## 4. 完整方向、七个新预测与原actual

必要输入为当前57的两次ordinary和两次完整168 selected J。20旧model tag仅继承原ID，导数在57重新支付；两次finite之后总新增23个原metric梯度，旧56/159梯度没有跨点复用。

两次新有限问题均converged，分别42和40次迭代，共82次/164线性系统；两次完整分离。共同方向SHA256 `b58b49d536f4dc2821d9e83e04de643f8323afc8eaa43f01d6ff1a28ea2e15e9`。其 $h=4\|M\Delta\|_\infty$为0.0078124965018671055，完整首阶max为0.26599990330415957、修复gain为0.000007157532041538541；这些是方向预测，不是actual单位步通过。

| 固定 $\alpha$ | 完整非线性预测两网最大 $\eta$ | 预测曲率门 | 满足预测下降/可候选 |
|---:|---:|---|---|
| 1 | 0.26601241222984906 | false | false |
| 3/4 | 0.2660080873526385 | true | false |
| 1/2 | 0.2660057545151524 | true | true |
| 1/4 | 0.2660054146399933 | true | true |
| 1/8 | 0.26600599235131184 | true | true |
| 1/16 | 0.2660064681695544 | true | true |
| 1/32 | 0.26600675282561537 | true | true |

七候选各用其实际rounded168坐标作新的metric和curvature predictor，未沿用旧affine凸性或声称全局最小。每个候选新增2个metric scalar frames/4次完整 $\Pi$、2个curvature scalar frames/6次 $\Pi$、1次height_jets、2次curvature与2次独立principal；首metric候选还付2个baseline frame和一次height密度基读取。全部nested次数保原行，不另计为ordinary，不省略或重复加总费用。

合格query按score排为4/3/5/6/7，预选最多三actual的4/3/5；第一项 $\alpha=1/4$实际接受即停止。该候选预测score为0.2660054165931174，预测eta和actual eta有独立浮点身份，原记录分别保留。实际准确物理步范数为
$2199022270915/1125899906842624=0.0019531241254666654$，在原 $1/128$域内，172盒准确通过。

## 5. 权威费用闭账

FINAL_CLOCK在全部大cache和COMPLETE写出/flush之后采样；其ledger是权威累计：
**185.978494641科学秒，0 overrun**。紧后process sample为185.98191641199992秒，不能与ledger相加，也不把job日历总历时替代科学账。

本次明确计入2必要ordinary、2selected-J、2finite、82iteration/164system、2全网分离、23新metric gradient、7非线性候选、1actual pair/2actual values，全部导入、输入读取、失败路径及导出在同600秒账内。必要ordinary耗时粗104.36695954600009/细18.09809538000013秒；当前selected J粗8.039300320999928/细17.40916539900013秒。实际候选ordinary因同进程已付冷初始化，粗0.22999024799992185/细0.4267456510001466秒；这些阶段均已包含，不能另外相加。

旧祖账2644.800406968秒/143值不重开；加本次4个full values后合计 **2830.778901609秒/147值**。接受58即关闭本任务剩余414.021505359秒和未用次数；不将余额迁移到下一个点或ring问题。0独立源接受重放、0旧159J/optimizer、0开发研究调用。

## 6. 原stdout关键记录身份

下表是原JSON加一个LF的字节身份，不是投影报告的重新编码身份。

| 原记录 | bytes | SHA256 |
|---|---:|---|
| INPUT3，当前57二jets/J输入 | 25009298 | `460472c989efb01fbcec9ba1c99211defd85d41e6324d2dc7fba1774ae3ca9d0` |
| CACHE1，完整首阶方向数据 | 15181746 | `b288d321cbeac5398aac738e0353742a7f37397ed929354a03255bf6acf19c18` |
| ACTUAL_TRIAL1 | 336267 | `2779ed49a4cedfb58f04ed8857fee4a2ca3abc3ec6ae9d802b326e425edb28f1` |
| MODEL1 | 872301 | `717e5209a82b8a2a41fde1ae3bef529a028ee7455ce97b92e51e6a6c3e6f10b1` |
| CACHE2，接受58全部已保存输入 | 33375405 | `9bfdb6d35b131d5b4b1514f0e0902c7f38aa735cabc3288502356b1ba03ffbdf` |
| COMPLETE1 | 5606777 | `e20a2149a50ea86becc177724235b6991d597d541c583fad85df3d1d3a739604` |
| FINAL_CLOCK1 | 199299 | `6a8e4724000f16429ed6c72607a92611647159207a18ce8e6a218b97269113de` |

复原永久field constructor仍只消费原55 COMPLETE：run43832870561/job133182173190/source23b37e90cbc1ac33ca6ff8ac1f91fa7a95c903db；不能把55坐标当58当前点。原数组、系数和长科学记录只留原stdout/临时runner；本文不把科研payload写Git、artifact、Release或cache。

## 7. 每次真实pull和接续边界

research public 11:41:19.273560→11:41:21.059129 UTC实际pull读 `625cf6caa2a5d38a010fcd38407a0129bcef21e1`；private 11:41:22.958103→11:41:23.431348读 `a8ec0e31b9ee75e7ad5cd179c2e9e4eb8cde0885`。report public 11:54:16.938070→11:54:18.493489读 `3d2751614c906e87418fdc8ba66f3b42eb9cf606`；private 11:54:21.544484→11:54:23.856337读 `9474f11d4e9debb4130a8d49d2d010d1fe0f70e1`。两public的根/题README均空diff，private根未变、题README不存在、QUEUE本会话唯一进行中。根/题已读blob仍21bd547f56590b7f2dd279d0297efb289a9b2783 / d0432faff569c8e9af7ed4809847e12880976c11；private根5ba164843b1f5802184178a82d786264404873a3。

当前继续R510/R511的真实58完整峰圈形算子、原17共同系数和完整原172盒问题，再接完整body非线性响应。若不变列排目标 $1000/61$，须改变原径向值/一阶jet，不重解已被排除的二阶中性族。有限成功也不能代替连续全角、全体body、非局部及全时间reach。原固定 $g$、$b_0$、永久reference、全部完成门和失败费用继续保留；主任务仍进行中。
