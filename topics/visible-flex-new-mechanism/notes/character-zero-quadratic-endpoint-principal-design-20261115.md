# H_E 二次平端主部：单目标公开 Actions 消费设计

日期：2026-11-15。状态：**新源码与十二个小人工入口已写；尚未执行人工或研究。** 本稿只规定下一次新计算，不预填目标为零或非零。

新工作接 [R234](../results/R234-weight-zero-first-endpoint-layer-cancelled-by-a-zero-pure-response.md) 已付的 true-weight0、canonical mixed $-2$ 代表 $H_{\mathrm E}$，以及 R236 的准确二次端层判据。只有一个新目标；不重算旧十七个一次层、不求响应仿射类的新核、不做固定 profile 求积。

## 1. 准确目标及继承条件

R234 的旧 R126 列编号下，

$$
H_{\mathrm E}
=C_2-\frac18R_0-\frac1{64}R_1
+\frac{13}{32}R_2+\frac1{48}R_3
+\frac5{64}R_4-\frac1{32}R_{10}.
\tag{1}
$$

已有完整证明

$$
\pi H_{\mathrm E}=0,\qquad
\lambda_+(H_{\mathrm E})=1,\qquad
\mathfrak T^{\uparrow}_{0,-2}(H_{\mathrm E})=0.
\tag{2}
$$

本次仅恢复同一个模式 $-2$ 的原式。必须与 R234 fresh 原差的 **2694 项**及 SHA256

~~~text
346ea2a14c74e4a6d831b05288533609b08bf7776782c0964dd66ece9eda96b6
~~~

逐一相符；这只核输入身份，不重新证明 (2)。

取固定首个 f 上升、局部 g=0 的左端 $\xi_0$，令
$x=\xi_0+t$，并保真实物理 t。写

$$
p=f'=\epsilon_p e^{-c/t}a(t),\quad
c>0,\quad \epsilon_p\in\{1,-1\},\quad
a\in C^\infty,\ a(0)>0,\qquad
b(t)=\frac{a'(t)}{a(t)}.
\tag{3}
$$

原式同右锚展开为

$$
H_{\mathrm E}=P_2+p^2B+p^3\mathscr A,\qquad
\mathscr A=\bigcup_N t^{-N}C^\infty.
\tag{4}
$$

P2 是真实左 collar 多项式，不得任选或删除。新唯一输出是

$$
\boxed{\operatorname{pp}_{<0}(t^4B).}
\tag{5}
$$

R236 证明：在原平台门 $P_2''=0$ 另已付时，(5) 为零当且仅当该二次层的零端通量解可光滑延拓。本次不评价平台、其他端点、总通量或内部退化。

本次的 (3) 不指定某个实际解析圆。采用 universal 的正 c 与有限个 b 的 Taylor 系数；真实 quadratic tail 仍是同一输入的原函数。为零可对所有这类端芽支付 (5)；非零仅表示**这个未再修正的代表**没有得到 universal 零证，不排除 fixed circle 的特殊尾值、其他响应修复或其他权抵消，更不排除所有 $\lambda_+=1$ 的成本。

## 2. 不任选截断阶：从完整可达 DAG 取得界

先遍历 (1) 的完整原 DAG，包括所有 nested primitive 的 integrand。设实际最高 profile jet 为 J。不能只扫描根的外局部项，也不能拿已证 pure 的 jet2 定理替代 mixed 原根扫描。

令

$$
D=2\max(J-1,0).
\tag{6}
$$

R226 精确指数积分和直接微分给

$$
\frac{f^{(j)}}p\in t^{2-2j}C^\infty
\quad(j\ge0).
\tag{7}
$$

因此原表达式中局部 profile 次数 d 的 $p^{-d}$ 系数，其 valuation 不低于 $-dD$。乘法加 valuation，正局部次数的左积分提高 valuation 两阶；次数零的左积分是普通多项式积分，提高一阶。每个原 primitive 在 $\xi_0$ 的完整初值仍作为真实尾函数保留，不能从这个 valuation 规则中删去。

只须 B 的 $t^n$、$n\le-5$。为局部次数 $d=0,1,2$ 分别取上截断界

$$
\boxed{U_d=-5+(2-d)D.}
\tag{8}
$$

该选择形成准确有限 quotient。若某个次数 d 的误差从
$t^{U_d+1}$ 开始，乘次数 e 的任意剩余因子后，至少从

$$
t^{U_d+1-eD}=t^{U_{d+e}+1}
\tag{9}
$$

开始；没有被截项能降回所需范围。左积分又只提高 valuation，故也不会把误差送回。

局部次数至少三的增量永远留在 $p^3\mathscr A$，但**一个高次数原 primitive 的 anchor 初值必须完整保为次数零**。新实现对每个原 atom 都单独加入原初值，这正是没有丢掉远侧历史的区别。

J 不超过二时，$-2D\ge-4$，(5) 由完整扫描后的结构界直接为零；不必执行任何 quadratic NF。若 J 超过 declared budget，必须报告资源退出，不能把它截为八阶或宣零。

## 3. Universal log-amplitude jets 的有限范围

写

$$
b(t)=\sum_{j\ge0}b_jt^j,\qquad b_j=\frac{b^{(j)}(0)}{j!}.
\tag{10}
$$

$b_j$ 是普通 Taylor 系数。任意有限组实数都能来自正光滑 a：令
$\log a$ 在端点具有相应有限 Taylor 系数即可。a(0) 已完整包含于 p 的因子中；本次不独立指定实际 a(0)，也不把它误删出真实尾函数。

令 $F_j=f^{(j)}/p$。有

$$
F_1=1,\qquad
F_{j+1}=(D_t+\lambda)F_j,\qquad
\lambda=\frac c{t^2}+b(t).
\tag{11}
$$

要在 $F_j$ 中保到 $U_1$，逐步递推时给每个尚余步骤两阶余量：
第 j 步保至 $U_1+2(J-j)$。乘 $c/t^2$ 最多降低两阶，求导只降低一阶，因此这个余量足够。

对 J 至少三，只需

$$
\boxed{0\le j\le K,\qquad K=4J-11}
\tag{12}
$$

的 $b_j$。另一种直接看法是：$b_j$ 进入最高 jet 相对于最负的
$-2(J-1)$ 至少提高 $j+2$ 阶；二次目标要达到 $t^{-5}$，须
$j+2\le2D-5$，即 (12)。带 b 导数的项不会比这个界更低。具体左积分递推所需的最大 j 只到 $2D-9=4J-13$，已包含于 (12)。

原右 integral 记为

$$
\mathcal I(E)(\xi_0+t)
=\mathcal I(E)(\xi_0)+\int_0^tE(\xi_0+s)\,ds,
\qquad \mathcal I=\int_r^x.
\tag{13}
$$

**左增量使用加号。** 对 d>0，若被积项为 $p^dR$，令零左积分为
$p^dS$，则

$$
(D_t+d\lambda)S=R.
$$

比较 $t^{n-2}$ 系数，得到有限准确递推

$$
\boxed{
S_n=
\frac{R_{n-2}-(n-1)S_{n-1}}{dc}
-\frac1c\sum_{j\ge0}b_jS_{n-2-j}.
}
\tag{14}
$$

从 $n=-dD+2$ 递增到 $U_d$ 即足够。这里使用 R226 的精确光滑余项定理保证 formal jets 对应真实渐近；不是把形式解本身当存在证明。只在 c 的倒数域运算，c 始终严格为正。

J=3 时有 $(U_0,U_1,U_2)=(3,-1,-5)$，只需 $b_0,b_1$；J=4 时为 $(7,1,-5)$，只需 $b_0,\ldots,b_5$。这些例说明新截断规模小，但实际 J 必须由本次原根扫描决定。

## 4. 真实 anchor、颜色和尾函数

新有限项键是

~~~text
(local_degree d, t_power n, c_integer_power k, sorted_b_Taylor_indices)
~~~

其系数仍是旧 ColoredRing 的**完整原表达式**，在固定 anchor
$\xi_0$ 取值。原环 x 在这些系数中表示 $\xi_0$；query 处出现的
$x^m$ 则准确展开为 $(\xi_0+t)^m$。不得把 x 直接置零或只保常数项。

每个 primitive 的初值直接用原 atom
$\mathcal I(E)(\xi_0)$，保全部 nested integrand，不创建互相独立的尾符号。g=0 只用于当前小区间；右尾里的 q、qbar 仍是不同颜色的完整实际输入。

最终局部次数二项的系数，按总 profile 次数守恒，恰为 degree2 的真实尾函数。只对这些新系数调用已发表 R178/R179 固定颜色余字母表示。转换后才将**外部** anchor profile jets 置零，word 字母内部的 jets 完整保留。所有 shuffle、同锚分部积分和共轭来源都通过该原函数表示处理。

最终行键为

~~~text
(negative_t_power_of_t4B, c_integer_power, b_Taylor_monomial,
 anchor_x_power, complete_true_negative_right_primitive_word)
~~~

不为任一 tail 指定数值，不新增实际 profile 评价。为零是对全部真实尾特化都成立的原式充分证。非零行仍不保证某个尚未指定圆满足该系数的非零特化。

## 5. 七份必要原输入与恢复范围

复用已发表 first-endpoint driver 的输入 reader 和原 mixed 响应公式，冻结其源码；本次不调用其实际研究入口。

| 来源 | 本次用途 | 新工作边界 |
|---|---|---|
| R109 static 完整旧导出，run 43645177423 | 同一八矩 $\Gamma$ 组合 C2 所需静态根及六个 W 模板 | 只必要恢复一个 C2 混合输入；不重 197 个目标 |
| R126，run 43649525432 | 六个指定原 response 的旧标签、W 原 SHA、mixed 原 SHA | 恢复旧 0,1,2,3,4,10 六根；不恢复其他十根 |
| R196，run 43681388902 | 真权零 C2、同参考规范化和来源 metadata | 只核来源，不重完整 38 列 H0 |
| R234，run 43699241372 | (1)–(2)、原 H_E SHA 和实际已付状态 | 只读 metadata receipt；不重十七一次层、pure 查询或 cubic NF |

C2 原 mixed SHA：

~~~text
b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f
~~~

六响应严格保 R126 旧下标；二次/W 标签为：

| old index | 二次算子 | W index |
|---:|---|---:|
| 0 | p0 | 7 |
| 1 | p0 | 17 |
| 2 | p1 | 1 |
| 3 | p1 | 12 |
| 4 | p1 | 16 |
| 10 | p2 | 15 |

恢复只消费 R78 冻结的 mixed $-2$ 原公式，每根核旧真实 SHA。
这些旧 portable DAG 未保存，metadata-only R234 也不存根，所以七根属于必要输入恢复，不是新增响应目标。

R234 source commit 为
ee9e2098c62392ddb709e7db26467bc225642d54，lane
character_zero_endpoint_layer；receipt 49168B，SHA256

~~~text
ea5c31ce431cff1f1765f04dd00ec14b26e6e624230d516485e7e994ea46a62c
~~~

主结果 38943B/SHA
577157ad38ca9744411167bd0fe865838df0360ee2564421b598a82f76fea26b。
driver 将 receipt 的 repository/run/source/lane、旧两源码和 main/dev 的准确 bytes/raw SHA 全核；不会凭 metadata 自行推出 (2)，(2) 的数学来源仍是发表的 R234。

不新增 N0/N2 收缩，不重 v2/v4，不编 3974 forcing，不重 W 空间、原 profile 求值或全 quartet NF。局部次数零、一的**有限中间 jets**是新 degree2 乘法所必需；这不等于重新提取或正规化旧完整一次层。

## 6. 新源码和输出

新 helper：

~~~text
scripts/literature_endpoint_quadratic_principal.py
21175 bytes
SHA256 01efa75bbb691c802e211ddf08fc3804d657af73d53ce428f51ae8b1ef365215
~~~

新 driver：

~~~text
scripts/literature_character_zero_quadratic_endpoint.py
19104 bytes
SHA256 98e8caae918822b95f8f298ed9397f498b97e0cd5aaa0d1ebcec76b137300f3e
~~~

两者均是独立新增文件，不改旧源码。递归绑定从 R234 driver 的
source_identity 继承，再加入两份新 SHA。旧 driver 本身固定为
29604B/bb7be8fc3fa6b98f3f69aca96e5145c6df1f3d581ea85d14aa7fb6ccfefe6a94；
旧 first-layer module 固定为
11829B/cf14e26c215bd93feb43dc4b56b8ecdcf9f9013084236e772229404eb9401b69。

新主 schema：

~~~text
visible-flex-character-zero-quadratic-endpoint-principal-v1
~~~

主结果必须列出实际 J、完整可达 atom/monomial 数、D/U/K、
H_E 原 SHA、全部新 primitive/IBP 费用、新 quadratic 系数数、
原主部系数 hash、完整主部行数及 hash。若不为零，至少打印一条完整原行 witness；短向量完整列于 stdout。只判一个代表，不构造新 response kernel 或 dual。

完整 in-memory certificate 保本次全部 raw-coefficient hash、
true-tail 转换记录和全部准确主部行；只取 bytes/SHA，不保存 payload。
MATHEMATICAL_RESULT 显式打印新数学结论和 scope，避免仅有临时文件而
外部读不到结果。

零的正式含义是：**若原平台门另已通过，则 H_E 对所有本声明端芽
的二次 germ 门成立。** 非零的正式含义只针对这一个尚未重新修正的
universal 代表，不能推出固定圆或整正字符仿射类失败。所有结果保
task_complete=false、full-period/joint 未付。

## 7. 十二个新增人工，尚未执行

新入口只构造极小的人工 quartic：

1. $q'''^2\mathcal I(\bar q^2)$ 的完整 c、b0、b1 主部；
2. 可达 J=3 的 U/K 准确范围；
3. 原 $\int_r^x$ 一次左增量的正号；
4. 两次 nested 左积分跨过主部门限；
5. query x 的 $\xi_0+t$ 全展开；
6. 真 quadratic total derivative 的 anchor 外 jets 归零；
7. 真 quadratic shuffle 关系，不能任赋两个尾值；
8. J=2 临界只用已扫描结构界得到 pp0；
9. 局部次数四不会漏入次数二；
10. J=4 的必需 b5 项确实保留；
11. anchor 外 jets 归零不删除 tail 字母内部导数；
12. 新接口未调用旧 cubic/first-layer NF，也未创建独立 tail 数据。

例如人工直接项的 $t^4B$ 主部为

$$
\left[
c^4t^{-4}-4c^3t^{-3}
+(4c^2+4c^3b_0)t^{-2}
+(-8c^2b_0+4c^3b_1)t^{-1}
\right]\mathcal I(\bar q^2)(\xi_0).
$$

这只检查新算法的极小例，不是本课题原 H_E 的计算。全部新人工先在本公开仓库 Actions 执行；当前没有 passed 回执。

## 8. Lane、CLI 和预算

建议 lane：character_zero_quadratic_endpoint。

四个输入目录：

~~~text
topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient
topics/visible-flex-new-mechanism/notes/actions-43649525432-1-g_first_translation
topics/visible-flex-new-mechanism/notes/actions-43681388902-1-character_head_zero
topics/visible-flex-new-mechanism/notes/actions-43699241372-1-character_zero_endpoint_layer
~~~

人工：

~~~sh
python topics/visible-flex-new-mechanism/scripts/literature_character_zero_quadratic_endpoint.py \
  --toy-only --max-seconds 60 --memory-mib 512 \
  --output "$OUT/character-zero-quadratic-endpoint-development.json"
~~~

唯一实际研究：

~~~sh
python topics/visible-flex-new-mechanism/scripts/literature_character_zero_quadratic_endpoint.py \
  --static-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient \
  --R0-directory topics/visible-flex-new-mechanism/notes/actions-43649525432-1-g_first_translation \
  --head-directory topics/visible-flex-new-mechanism/notes/actions-43681388902-1-character_head_zero \
  --first-layer-directory topics/visible-flex-new-mechanism/notes/actions-43699241372-1-character_zero_endpoint_layer \
  --max-seconds 240 --memory-mib 1024 --integer-bits 8192 \
  --max-profile-jet 8 --max-terms 100000 --max-IBP-calls 300000 \
  --max-cache-entries 250000 --max-summary-bytes 95000 \
  --max-certificate-bytes 8000000 \
  --output "$OUT/character-zero-quadratic-endpoint.json"
~~~

真实研究只允许 GITHUB_ACTIONS=true 且 repository 精确为
Rogerhu12/math-research-public。max-profile-jet=8 是预算门，不是对
未知原根的数学假设；实际超出就报告未完成。

内存、time、rational bits、raw cache、series terms、IBP calls、
主文及 certificate bytes 都有显式上限。资源退出或实现错误会将未完成 decision 移为明确的 uncertified diagnostic，不打印数学完成结论；不授零
或非零数学结论，不声称可恢复一个未保存的 cursor。所有临时输出只由
metadata-only publisher 记录脚本/参数/run/SHA；依根 README 15，
仓库、Release、artifact 均不新增可重算 payload。

完成本门后按实际结果继续完整 period 的下一个未付条件，不把这一
局部代表的有限主部当作课题完成标准。
