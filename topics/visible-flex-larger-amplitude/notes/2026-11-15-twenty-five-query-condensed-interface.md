# 独立25-query入口：从实际79只增加原left-RMS465

分类：独立数值实现与输入/输出契约；冻结时尚未执行的新计算。  
作者：ChatGPT（amplitude，AI辅助）。日期：2026-11-15 UTC。

## 1. 真实依据和唯一新增查询

实际79从实际76完成的优化warm重新线性化，保原24查询和全部门，在
$\alpha=1/32$接受。该模型固定权重merit由`43.57627837509625`变为
`43.5661119869748`，原保存下降`0.010166388121447767`，预测比率
`0.9995443258196769`。最近拒绝档$\alpha=1/16$的全部原节点、中点、
24个已建模完整角网格均有效，实际merit下降`0.02023277691421299`，
原完整RMS检查只发现left-RMS465失效，原$\beta^2$最小值
`-0.421944063367393`、物理角0；右RMS族没有无效点。

原$1/4$和$1/8$同样只有left465使完整RMS失败，而且实际merit下降。
更远$1/2$先在原midpoint487失败，尚未执行完整RMS或实际merit；该点
不加入本轮。所有六档原结果与scope见
[实际79正式结论](2026-11-15-actual-request79-twenty-four-query-left465-limit.md)。

本入口只在新的实际79父场，把原left-RMS465的全部2048物理角行加入
下一优化模型。原16个left-RMS和8个collocation midpoint全部保留。
不保证步长变大或下一轮成功；所有原非线性回溯与完整查询仍决定接受。
阻尼270、512工作行、200dual、LSMR/projection及时间预算原样。

## 2. 四个独立冻结源

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_twenty_five_query_domain_operator.py` | 32768 | `55fe72b1bad9cf3ee26b1d29a1a6cefb7f0f62f2570d7703bb8f3dfcd01b2260` |
| `geometry_20261114_twenty_five_query_condensed_warm.py` | 43409 | `5dbd5948f815a1fcf4eaf2a08f7d130407ce52c96b25240738d26c6476b48b0c` |
| `geometry_20261114_twenty_five_query_condensed_response.py` | 2622 | `8d55ce7f29520318db39de5dcdb0790cdce43452dc29085ec26cbfe042dfa75d` |
| `geometry_20261114_twenty_five_query_collocation_observer_warm.py` | 16732 | `be6815071387c34fb25b4f064508af2ab65691bba4ff512d1fa999236a1f4d55` |

交付目录`/tmp/visible-larger-twenty-five-source/`，各`.py.diff`为相对冻结
24源的完整差异。旧24源不修改。新domain钉原24domain
`06933e9341664d63b5a9eaeb00998daa1be7b1c1d143a60f1ae2ef05efa9db36`；
新warm钉原24warm
`b453b53d4ae759e0bc50d5d789beb04e53c18903adaf427c2a28c0382827d452`，
递归保留原全部`SOURCE_NAMES/FROZEN`和父producer。

R270库、localQP和原完整QR分别保持：

```text
84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b
ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173
596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722
```

静态回执`twenty-five-source-static-check.json`为5909B，SHA
`3a5eac2c3dcfc8476e9d25b3410af1861138e974209de6bdf85c8a3ad4045ac1`。
23个原核心或只读observer函数的AST逐项相同；domain构造器除两条
诊断文字的query/cell计数更新之外，全部AST相同。原FD全文只反向
替换名称/schema即逐字等于24。当前typed顺序、22节点布局、原父79
双SHA及status透明gzip原字节已静态核。没有导入科学模块、构造数值
fixture、执行模型或触发Actions。

## 3. 当前typed行序、实际捕获和完整局部支持

```text
LEFT = (465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485)
MID  = (473,475,477,480,481,482,484,485)
```

先17个left-RMS，再8个原collocation midpoint，每query按原物理角
index0至2047排列。left分数保持`0.17267316464601146`，mid分数保持
0.5。`kind/query_index/fraction/station`继续贯穿每个block、梯度、
实际角读数、模型身份与完整分块导出。新增left465为query0、行0至
2047；原所有left索引后移1；mid473从query17开始，mid485为query24。
不能用旧24的索引解释当前行段，历史父24记录保持原样。

| 对象 | 当前25-query身份 |
|---|---|
| 完整缩放未知量 | 原236036 |
| 完整B行数 | `25×2048 = 51200` |
| 唯一捕获cell | 17个，即上述LEFT集合；MID均已在其中 |
| 实际查询端点 | nodes465至486，共22节点 |
| 实际B列并集 | `22×338+3 = 7439` |
| R270声明连续局部布局 | 同nodes465至486加3个全局control |
| zero-layout | 空int64数组；全部声明列有实际查询块 |
| 原C可修正支持 | nodes471至482加3个control，共4059列 |

相比父24捕获，新增cell465和端点465；端点466已存在。两端原J/P
来自同一次原完整A/J构造中的捕获，不能声称捕获集合没变，也没有
另一次完整Jacobian。complete B支持扩张是明确的新算法模型身份。
其正向/转置继续使用同一完整global列块、同一local映射和共享节点
scatter-add。当前B和声明布局相等，不恢复历史zero484标记。

## 4. 新left465的完整原Hermite链

站点来自原mesh和原left分数；查询基点来自原一次evaluate返回的
`state.y[465:467]`和`state.f[465:467]`，经同一`CubicHermiteSpline`。
没有用原collocation中点或两个节点的算术平均替代。

在固定$\tau$和原cell宽度$h$下，

$$
Y_q=h_{00}Y_L+h h_{10}f_L+h_{01}Y_R+h h_{11}f_R,
$$

$$
\delta Y_q=h_{00}\delta Y_L+h h_{10}\delta f_L
              +h_{01}\delta Y_R+h h_{11}\delta f_R,
\qquad \delta f_i=J_i\delta Y_i+P_i\delta p.
$$

$h_{00},h_{10},h_{01},h_{11}$是同一原cubic Hermite基函数。原B编译保
查询物理状态域梯度$\Gamma$及查询处标量control直接项$\Pi$：

$$
B_L=h_{00}\Gamma+h h_{10}\Gamma J_L,\qquad
B_R=h_{01}\Gamma+h h_{11}\Gamma J_R,
$$

$$
B_p=h(h_{10}\Gamma P_L+h_{11}\Gamma P_R)+\Pi.
$$

原exact入口/core映射保留，原列尺度$S$只除一次。所有全局control、
共享端点和查询处$a,a_s$直接链都保留。8个原mid仍直接使用
`state.middle`和`problem.mid`，导数链仍为
$\tfrac12(\delta Y_L+\delta Y_R)-\tfrac h8(\delta f_R-\delta f_L)$。
本次不引入新公式；原实模型和实现检查只在公开Actions执行。

## 5. C outside、完整H和原接受门

C可修正支持保持4059列，其实际约束offset仍为

$$
c+B_{\overline{S_C}}z_{0,\overline{S_C}}.
$$

完整outside物理节点现在包括465、466、467、468、469、470、483、
484、485、486。新增left465的两端都在C物理支持之外，完整贡献必须
进入offset；不能把新节点465删掉来保持原维数。局部C投影是否可行
由实际子问题决定，原完整ray、径向修复、备份和同f线段选择仍在。

完整H路径使用全部7439局部坐标，保原$g=A^Tb$、pure-global/core项
及外部仿射最优响应。C固定支持不施加到H候选。恢复、径向和组合
之后仍实际读取原完整A/AT/B/BT、gdot、全部51200行slack和R267浮点
后验。全向量径向缩放可能改变outside方向，因此最终outside不宣称
不变；最终经缩放的H向量不自动称精确外部条件最优。

每次真实trial都保原全部节点/中点、rho、两完整RMS族、原实际merit
与17档回溯。25个建模网格不是原全域检查的替代物。新FD仍按原完整
方向、步长、Richardson与`5e-5`门重跑。浮点KKT、R267、source或
payload保全不增加新的BVP验收门。

## 6. 首次实际父79与未来own-schema

首次输入严格绑定实际79：

| 字段 | 真实原身份 |
|---|---|
| run/source | `43663293492` / `31d2ad909638aa3eb3211a9ea0feed632c0e9a2b` |
| 父schema | `exact-constraint-twenty-four-query-condensed-complete-H-warm-v1` |
| 原压缩warm | 4868398B，`565e2487317ffbc85560dd01efa2cfb4e479447d51a17216deb4ef61f55b4504` |
| 原JSON status | 2683314B，`e790e998ed6eebdc084546131e206dd4e5d723aebf7f92830b3153f82a25a8c0` |
| 公开status gzip | 312135B，`aea13404a1cd1109f207cbb2a6f3c46fb885518ab7e29c480ba332ea21d756b6` |

公开目录为
`notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/`。
status透明解压后核原JSON字节SHA，不能重序列化；若直接JSON和gzip
同时存在，也必须逐原字节相同。原大status通过CLI或公开Actions
读取，不经小文本connector整读或切块搬运。

新schema为
`exact-constraint-twenty-five-query-condensed-complete-H-warm-v1`。
首次24-schema父严格钉上述双SHA；未来完成的25-schema优化warm可
显式新双SHA再调用一次模型。原全producer、mesh、scalar以及常值
core/control契约由原validator完整保留。历史父24子树不改名，当前
数学25入口与只读执行observer的source身份分开记账。

## 7. 精确CLI、原预算与输出

在原公开Actions恢复accepted96、699节点prepared112、T112配置和
真正零H fullJ后，唯一模型调用为：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_five_query_collocation_observer_warm.py" \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_OUT/preparation112/prepared.json.gz" \
  --tail-anchor "$T112_TRUE_ZERO_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --resume "$VISIBLE_PARENT79/warm-001.json.gz" \
  --expected-resume-sha 565e2487317ffbc85560dd01efa2cfb4e479447d51a17216deb4ef61f55b4504 \
  --parent-status "$VISIBLE_PARENT79/driver-status.json" \
  --expected-parent-status-sha e790e998ed6eebdc084546131e206dd4e5d723aebf7f92830b3153f82a25a8c0 \
  --out "$VISIBLE_OUT/twenty-five-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512 \
  --condensed-dual-sweeps 200 --condensed-store-root
```

真实下降warm保存后，完整FD为：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_five_query_condensed_response.py" \
  --accepted "$VISIBLE_ACCEPTED" --prepared "$VISIBLE_CONDENSED_WARM" \
  --tail-anchor "$T112_TRUE_ZERO_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --out "$VISIBLE_OUT/physical-response" --angles 4096
```

原零锚SHA`e788a28d…`的完整真响应/J这里只构成明确的affine图；不能
把当前新H标为已有native解。warm/status继续
`success=False/new_coupled_finite_acceptance=False`，一次优化下降不
等于完整DN、闭面或同g精化。原model、全部trial、B/Gamma/Pi、捕获
端点、R270局部root、原响应/恢复、QP数组及两个只读observer继续保存。
只读observer不额外评价RHS/J或trial，异常不改原返回/finite/接受决定。

## 8. 唯一调度与后续实际读取

唯一request84 workflow/request草稿置于`/tmp/visible-larger-request84/`，
root负责完整审读、普通Git及唯一实际发布。该草稿沿现有condensed
触发路径
`topics/visible-flex-larger-amplitude/computations/public-condensed-qp-request.json`；
它不另行dispatch，也不修改旧计算源。原环境、78源恢复、prepared、
锚、solver命令全部沿用，只有当前四入口、父pair、typed身份和输出
目录更新。冻结时暂无request84运行或科学读数。

独立25完成原件读取器随后只读实际artifact，完整身份为
[25-query读者接口](2026-11-15-twenty-five-query-completed-artifact-reader-interface.md)。
原结果先保存和解释；附加byte审不成为主线新科学门。
