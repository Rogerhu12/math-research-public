# 实际完整固定标量的物理长度与核心初始律

会话 Astra-larger-e4e2a2bf-20261126（AI）。2026-11-28。

## 真实读出与范围

在原公开 Actions 46108296054/1、job140865899880 上，原science和pure自然返回后，以既有完整输入报告做只读。第一读出0/5.94083467100063秒，完整对象22358B/SHA ebc93a65362b42d90c3aa6cae945926ece7591423ec957ed5a3975611bf92e84已写；控制器的13个whole对象summary因只允许标量而报错，完整原错误未删。随后同一完整读出源、同一原输入，仅换新输出及完整标量leaf选择，实际退出0/5.89206177000051秒，90/90字段均返回，summary_errors和missing_outputs均空。

第二次实际source为 `95f8de55264e1bf1ef3d8de6308631847c953eb4`，读出源码
`scripts/resume_20261126/read_complete_existing_fixed_scalar_metadata.py`，7320B，
SHA256 `50ffbff8d2e2980295b2db1641c5ce0fbb874805fdfff5b5ed3ba9ea3d094b32`。
完整源码调用原 maker 的 `read_preparation`，逐个核对原完整参数/来源/输出对象；不重做积分、F、J或normal根，相关调用数全0。完整读出对象22366B/SHA
`038b92a34f6a33a40efeac7da4bff53e710ce22a999fe02c70f7b23ae26a9151` 留原runner。

完整实际命令、90个原标量、所有输入/输出身份及前一投影错误在固定完整小卷：
[run28 第2卷](https://github.com/Rogerhu12/math-research-public/blob/106767818ea8aed67cf6f74880abd9cee73d3dd2/topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46108296054-1-part-002.md)，
52652B/SHA256 `47cf7953ed91408f689a58e70fc290fa931a46a652b418a16c5a86fb52300b6a`/Git blob `9d4f30eae551516c9ee5357d3ec46f19606eb548`。
这是整个文件的身份，不是最后一节的截取身份。

## 全物理域长度与原起点

物理长度来自完整 FullHold 的 `metadata().S`：

$$
\frac{296412483966226858607817}{125000000000000000000000}
\le S\le
\frac{2371299871729836522645511}{1000000000000000000000000}.
$$

两端的近似值分别为2.371299871729815、2.3712998717298364。直接有理比较给
$237/100<S<119/50$。这不是 integer oracle 的精度缩放常量 $h.S$，
也不是工作mesh末点、局部段长或重新选择的径向域。

原 analytic origin 的字为 `0x1.fae147ae147aep-1`，准确值
$4458563631096791/4503599627370496$，其十进制打印为0.99。
完整固定标量定义含416个原knot，末knot的实际值仍为
$s=0.99$、$a=1.1666064106120295$、$a_s=0.357948638910307$、
$a_{ss}=-2.0101206107275877$；未重新拟合或删除旧点。

## 完整初始律的三个原参数

| 原字段 | binary64打印 | 原完整字 | 准确二进有理值 |
|---|---:|---|---|
| length | 0.9 | `0x1.ccccccccccccdp-1` | $8106479329266893/9007199254740992$ |
| velocity | 0.3 | `0x1.3333333333333p-2` | $5404319552844595/18014398509481984$ |
| k0 | 0.2 | `0x1.999999999999ap-3` | $3602879701896397/18014398509481984$ |

FullHold 原源在核心用完整initial_law重算首jet，并未将保存的浮点K/S/R作为新初始数据。核心径向参考第二jet所需的原 $\kappa_0$ 应从该准确初始律和原参考切向定义读取；例如所用 $a_{ss}(0)$ 为上述准确k0，不能以末段曲率K替代。

## 原包围的完整来源边界

FullHold source SHA256
`a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670`；
integer oracle
`babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0`；
hold source
`ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1`。
原metadata保128 Simpson panels、完整余项、准确cut/durations、K/alpha/plateau/R/height各完整包围及未把浮点目标作为输入的声明。其全部90标量仍在上述固定完整小卷。

本次读的原输入准备报告65325B/SHA
`c04003dc4e5e0eb6024df422507e6d5df4ecd3a0ceaa27d1280783363d277945`；
其完整scalar输入40488B/SHA
`2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189`；
完整参数投影身份
`e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa`；
固定目标
`957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9`。

**原metadata里的R是原FullHold半径。** 它的近似两端
0.5647341753865778、0.5647341753870307不能冒充修改后的R690半径。
R690半径应继续使用[原完整R690标量输入](2026-11-26-actual-deep-valley-complete-scalar-input.md)的准确$10^{-72}$包围。
同样，本次metadata的reference_height_increment是从cut起的局部原参考增量；
新构造的声明高度1.947054437068418来自自己的完整参考准备报告，不能把二者混为同一个量。

本记录只支付完整既有标量输入的真实取回和身份，不支付新参考的角向度量、全域reach、
normal32、整像Euclidean非全等或README完成标准。完整原raw、13final与typed未被修改。
