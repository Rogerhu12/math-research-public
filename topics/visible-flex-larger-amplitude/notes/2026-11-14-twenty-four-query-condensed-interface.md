# 独立24-query入口：从实际74只增加原left-RMS485

分类：独立数值实现与输入/输出契约；本文冻结时尚未执行的新计算。  
作者：ChatGPT（amplitude，AI辅助）。  
日期：2026-11-15 UTC；代码继续沿用本轮`20261114`源名。

## 1. 真实依据与唯一新增查询

实际74从真实72父场构造23-query模型，在原全部检查下接受
$\alpha=1/64$。该次固定权重下merit由`43.6764824644448`降为
`43.67047492812996`，实际下降`0.006007536314839967`，预测比率
`0.9978532859337634`。最近拒绝档$\alpha=1/32$的全部原节点、中点及
23个已建模完整角网格均有效，实际merit确实下降
`0.011961812301919394`；原完整RMS检查只有left-RMS485失效，原
$\beta^2$最小值`-0.00928897249979821`，物理角
`0.08283496254582462`，右RMS族没有无效查询。完整七档回溯与原身份见
[实际74正式结论](2026-11-14-actual-request74-twenty-three-query-nearest-left485.md)。

本入口只把该原left-RMS485的2048个物理角行加入下一优化模型，
保留此前15个left-RMS和全部8个原collocation midpoint查询。
尤其midpoint485继续独立存在，不能用它替代相同cell内的left-RMS485。
实际74更远的$1/4,1/8,1/16$也都出现实际merit下降及同一个left-RMS485
失效；$1/2$与1还失败于其他原中点及已建模查询，未执行完整RMS。
因此新增一组不能预言任意更大步长通过，也不替代完整真实回溯。

当前完整方向的原线性slack均可行，原完整stationarity为
`0.00011211001642311933`；局部及完整径向修复比例均接近1。
这些是已保存浮点模型读数，不是精确QP或BVP证书。本次仍保阻尼270、
512条工作行、200次dual预算和原17档试步；不为该现象改λ、扩大预算
或加入更远试步中出现的其他查询。

## 2. 四份独立源码及冻结身份

| 新独立文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_twenty_four_query_domain_operator.py` | 32451 | `06933e9341664d63b5a9eaeb00998daa1be7b1c1d143a60f1ae2ef05efa9db36` |
| `geometry_20261114_twenty_four_query_condensed_warm.py` | 42798 | `b453b53d4ae759e0bc50d5d789beb04e53c18903adaf427c2a28c0382827d452` |
| `geometry_20261114_twenty_four_query_condensed_response.py` | 2622 | `87261854684d5844c97d59b328db2aa070b015b565baf46dfb7e811808b3bb87` |
| `geometry_20261114_twenty_four_query_collocation_observer_warm.py` | 16732 | `f6639751ea97bd857ad05ad0a36d38d11024dac25f6ecc0610fef2d9fe90cf35` |

四源位于`/tmp/visible-larger-twenty-four-source/`。旁置各`.py.diff`
保留相对冻结23源的完整差异，旧23四源不改。
新domain钉住原23domain
`755d9bf2a01c5c417b28bfd265ee76712bba54a9fdeddf34ea56c4668abefe98`；
新warm钉住原23warm
`1fe5b698e452112583ee82a81ab7890095c7f3f31de05cdfb60c79e35039721c`，
并递归保留原`SOURCE_NAMES/FROZEN`及完整父producer。

原R270库保持
`84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b`；
局部QP保持
`ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173`；
完整QR保持
`596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722`。
完整原A/J、边界、标量profile、338维物理场、112维core/tail及3个
全局control不改，C投影、完整R270、QP与warm引擎的公式不改。

`twenty-four-source-static-check.json`为4614B，SHA
`f4a2cc6f3bf83d1ac48f51ee781bafc84440547ceac8b9abbd2bf9e74646c6ca`。
19个原核心/只读observer函数AST、原mid导数赋值AST与23相同，FD
全文仅名称和身份替换可逆；当前16LEFT/8MID行序、双source pin、
实际74父pair文件SHA均静态核过。这里只做源码、字节及整数布局检查，
没有导入科学模块或执行任何数值模型。

## 3. Typed行序与保持不变的完整支持

每个查询都包含原物理角index0至2047。固定顺序为16个left-RMS，
然后8个原collocation midpoint：

```text
LEFT = (466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485)
MID  = (473,475,477,480,481,482,484,485)
```

left分数保持`0.17267316464601146`；mid分数保持0.5。
`kind/query_index/fraction`进入每个block、model身份、实际角读数和
导出。新增left485为query15，行30720至32767；mid473移至query16，
行32768至34815；mid484为query22，行45056至47103；mid485为query23，
行47104至49151。不得按旧23索引解释当前mid行段。历史父23的typed
身份完整原样保存，当前`row_order`明确16LEFT/8MID。

| 对象 | 新24-query身份 |
|---|---|
| 完整未知量 | 原236036个缩放坐标 |
| 完整B行数 | `24×2048 = 49152` |
| 唯一捕获cell | 16个，与23相同 |
| 实际查询端点 | nodes466至486，共21节点，与23相同 |
| 实际B列并集 | 21个338维物理节点及3个control，共7101列 |
| R270声明连续局部布局 | 同nodes466至486及3个control，共7101列 |
| 当前零布局列 | 无；显式空int64数组 |
| 原C可修正支持 | nodes471至482及3个control，共4059列 |

cell485及端点485、486已经由原midpoint485捕获。新增left485仅复用
同一次原A/J里的端点J/P，没有新的捕获cell/node，也没有另一次完整
Jacobian。实际和声明B支持相等，R270局部维数保持7101，原节点484
仍有真实B列，不恢复更早历史的zero484标记。

每个block的local列映射仍从完整global columns建立，正向与转置使用
同一冻结行块及原scatter。捕获支持不变的说明只限集合和接口；改变
基点会重新建立真实有限模型，不能据此声称不同运行的A/B字节相同。

## 4. 新left-RMS485的实际基点与完整Hermite链

该查询的站点使用原mesh和原left分数，基点使用原一次残差返回的
端点`state.y[485:487]`和`state.f[485:487]`，经同一
`CubicHermiteSpline`评价。它不是`state.middle[485]`；后者属于仍然
保留的原collocation midpoint485。

记固定分数为$\tau$、原cell宽度为$h$，Hermite权重为

$$
h_{00}=2\tau^3-3\tau^2+1,\quad h_{10}=\tau^3-2\tau^2+\tau,
\quad h_{01}=-2\tau^3+3\tau^2,\quad h_{11}=\tau^3-\tau^2.
$$

原查询及其完整一阶变化为

$$
Y_q=h_{00}Y_L+h h_{10}f_L+h_{01}Y_R+h h_{11}f_R,
$$

$$
\delta Y_q=h_{00}\delta Y_L+h h_{10}\delta f_L
             +h_{01}\delta Y_R+h h_{11}\delta f_R,\qquad
\delta f_i=J_i\delta Y_i+P_i\delta p.
$$

若$\Gamma$是该真实查询对物理状态的域导数，$\Pi$为该查询处标量
control直接项，则原编译块为

$$
B_L=h_{00}\Gamma+h h_{10}\Gamma J_L,\qquad
B_R=h_{01}\Gamma+h h_{11}\Gamma J_R,
$$

$$
B_p=h(h_{10}\Gamma P_L+h_{11}\Gamma P_R)+\Pi.
$$

再施原exact inlet/core映射并只除一次原列尺度$S$。全局control、
共享端点及查询处$a$、返回$a'$的直接control链均不省略。端点J/P
来自当前唯一完整A/J构造，原B编译器只读捕获的真实返回值。

全部8个mid保持原`state.middle`与`problem.mid`的直接基点，以及
完整链$\delta Y_m=\tfrac12(\delta Y_L+\delta Y_R)-\tfrac h8(\delta f_R-\delta f_L)$。
原所有查询的complete complex方向、伴随和full/local一致性检查
继续按当前24个typed查询运行。实现检查不替代原全域检查，也不是
连续全角/全站点的精确证书。

## 5. 原C支持、完整outside及完整H响应

C可修正节点仍为471至482及3个control，共4059列。其子问题使用
完整offset

$$
c+B_{\overline{S_C}}z_{0,\overline{S_C}},
$$

包括outside节点466、467、468、469、470、483、484、485、486的全部
实际作用。新增left485的两端都在C物理支持外；不能漏掉它的outside
贡献或因此放宽原完整B。固定C投影可不可行仍由实际子问题决定；
原完整ray、径向修复和同f备份/线段选择保留。

R270路径使用全部7101局部未知量并保持原$g=A^Tb$、pure-global/core
项及外部仿射条件响应；C的固定支持没有施加到完整H候选。
恢复、径向修复和组合后仍用原完整A/AT/B/BT读取实际gdot、全部49152
行slack及R267浮点后验。完整向量径向缩放可改变outside raw部分，
最终outside不宣称保持初值。所有科学非线性门保持原样。

同轮C/H比较、预测和实际merit使用同一固定权重模型；下一父场会
重新冻结权重，不能跨轮直接相减merit。浮点KKT和R267报告没有升级
为精确QP或BVP验收门。

## 6. 首次真实父pair与同schema续接

首次输入严格为实际74的新warm/status：

| 字段 | 原身份 |
|---|---|
| science run/source | `43659610548` / `145d7a53ec05a64d39d0a36ac3e441e3475cb9bf` |
| parent schema | `exact-constraint-twenty-three-query-condensed-complete-H-warm-v1` |
| 原压缩warm | 4849039B，`204b208393218923f8abf9a36b6f03d29306409155447f561b2c2f4c373001a3` |
| 原JSON status | 2532904B，`09d944723fb6be152e90ba283fc44d33d455f1a52bc73787a329fcdc7d97ea73` |
| 公开status gzip | 291640B，`b481c6154bb0359cb4e5e92144728f95acef4e82f0212045965e636d380dc608` |

公开目录是
`notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/`。
工作流透明解压status并核原JSON字节SHA，不重新序列化；warm使用原
压缩字节。原JSON与gzip同时存在时，解压字节也必须相同。
原大status仅通过正常终端或公开Actions读取，不经小文本connector
整取或机械拆块搬运。

新schema为
`exact-constraint-twenty-four-query-condensed-complete-H-warm-v1`。
首次23-schema父必须匹配实际74双SHA；未来真正完成的24-schema
warm/status可用显式新双SHA再进行一次模型调用。原完整producer子树、
mesh、scalar及常值core/control继续由原validator核验。当前独立执行
observer身份与数学24warm身份分别记账，历史23子树不改名。
不把prepared、pending或未接受trial当完成父场。

父场与新warm仍明确`success=False`和
`new_coupled_finite_acceptance=False`；实际优化下降不等于完整DN、
闭面或同g精化成功。

## 7. 精确CLI与原预算

公开Actions恢复原accepted96、699-node prepared112、T112配置及
真正零H全J后执行以下唯一模型调用：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_four_query_collocation_observer_warm.py" \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_OUT/preparation112/prepared.json.gz" \
  --tail-anchor "$T112_TRUE_ZERO_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --resume "$VISIBLE_PARENT74/warm-001.json.gz" \
  --expected-resume-sha 204b208393218923f8abf9a36b6f03d29306409155447f561b2c2f4c373001a3 \
  --parent-status "$VISIBLE_PARENT74/driver-status.json" \
  --expected-parent-status-sha 09d944723fb6be152e90ba283fc44d33d455f1a52bc73787a329fcdc7d97ea73 \
  --out "$VISIBLE_OUT/twenty-four-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512 \
  --condensed-dual-sweeps 200 --condensed-store-root
```

真零锚仍为原`e788a28d…`完整响应，路径
`public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz`。
实际下降warm保存后，原完整FD重新执行：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_four_query_condensed_response.py" \
  --accepted "$VISIBLE_ACCEPTED" --prepared "$VISIBLE_CONDENSED_WARM" \
  --tail-anchor "$T112_TRUE_ZERO_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --out "$VISIBLE_OUT/physical-response" --angles 4096
```

FD重新测试真实新warm的原完整方向、两阶Richardson及原`5e-5`门。
真零H全J在这里明确只构成affine图；当前非零H并不被标为已有真正
native解。此warm入口没有新增native调用、全DN联解或闭面审计。
原全部节点/中点、两完整RMS族、rho、实际merit和17档回溯都保留。
24组建模查询不能替代这些实际门。

## 8. 原件保全与唯一工作流责任

输出保留原model/trials、typed角读数、原mid及collocation只读observer、
B/Gamma/Pi/原端点捕获、R270局部root/affine/recovery、QP数组、同模型
C/H比较、完整原残差后验、新warm与FD身份。observer只读取原evaluate
返回值与原一次weights，不新增科学调用；观察异常仅记报告，不改原
finite、merit、返回值或决定。

geometry独占`/tmp/visible-larger-request76/`中的唯一workflow/request
草稿；root负责普通Git、真实pull/README检查、推送及唯一实际调度。
本接口不创建第二个dispatch。工作流仍使用原condensed触发路径
`topics/visible-flex-larger-amplitude/computations/public-condensed-qp-request.json`，
父74透明gzip恢复、原环境和全部预算/门沿用，publisher当前冻结为
`22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`。
已交付的唯一草稿及原字节身份为：

| geometry草稿 | 字节数 | SHA256 |
|---|---:|---|
| `visible-larger-public-condensed-qp.yml` | 24481 | `96660ef6f2d7c193341857d268824c87e4389f788ddf53bc31807530e1c2ecbc` |
| `public-condensed-qp-request.json` | 14151 | `ea45ed8054693e21694d07720ee5c519d28863a721f492ab638b7e2f2f8e94ee` |
| `static-check.json` | 13919 | `162801918d7f881f9a5163d800e162d049f09027d9811a73f26500f77b8eafec` |

旁置workflow/request完整diff；该静态回执核51个源pin、11段bash
语法及6段内联Python AST。这里的SHA由实际文件字节核对，未运行科学。

本次只交付新源和静态检查，尚无request76科学读数。实际完成后先读
全部原试步、最近拒绝阶段、新父pair及FD，再记录完整byte reader的
真实范围；附加字节读取不成为暂停主线的新科学门。
