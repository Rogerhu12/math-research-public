# v12 的完整幂等元平方复用与耗时范围

## 1. 实际输入与回执范围

本条只改变已认证原 primary 商中的一次局部重复计算。原函数为
[scripts/original_ys_closed_point_tools.py](../scripts/original_ys_closed_point_tools.py)
的 `_lift_idempotent`，该完整源码 SHA256 为
`7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb`。

原 v12：run `46033409751`、job `140622660136`、source
`048e20343a5f7ec65db9089d824d0635d6815b2b`。
最终完整日志由根读取为 5694056 bytes、12522 行，SHA256
`80552d07f846435ca65e372cba161a4c0240e820abec053c3589d969239ce907`。
22:15:38 UTC 收到 signal 15 / exit 124，命中 21000 秒 host 门限。
它已返回 30 个完整原 HNF，均为整个输入的 prime-subfield descent，
以及六个完整长度 612 的 cusp primary；尚未返回完整四交、Norm 和
18-by-9 最终证书。本条不将此回执改记为几何 PASS。

## 2. 唯一局部改动及完整正确性

记原商的完整规约为 $r$、完整乘法为 $m$。原算法先计算
$e=r(e_0)$ 及 $m(e,e)-e$；每一非零误差循环又重新计算同一个
$m(e,e)$，随后计算三次乘积并更新。

替换后只保留如下一个局部变量：

$$
s=m(e,e),\qquad \operatorname{error}=s-e.
$$

每轮依次执行

$$
e_3=m(s,e),\qquad
e_{\mathrm{new}}=r(3s-2e_3),\qquad
s_{\mathrm{new}}=m(e_{\mathrm{new}},e_{\mathrm{new}}),\qquad
\operatorname{error}_{\mathrm{new}}=s_{\mathrm{new}}-e_{\mathrm{new}}.
$$

循环入口的不变式始终是 $s=m(e,e)$，且这里的等号是整个原商的全部
306 个多项式坐标等号，不是剩余域、首项、迹或某个读者的等号。
原 `quotient_context` 的乘法先规约两输入，再调用原完整环乘法，
最后规约全部输出；它不修改输入向量。因此归纳给出原、新两算法
在每轮相同的 $e$、$e_3$、误差、步数和最终返回。

保留原全部判断：

- 初始误差的整个 small-fiber 投影为零；
- 原 `norm_exponent` 给出的完整步数上界，越界仍抛出原异常；
- 每轮实际比较完整误差是否为零；
- 最终整个 small-fiber 幂等元返回；
- 原 receipt 的全部字段，包括最终完整元素的 hash。

若实际执行 $s$ 轮，原函数调用完整商乘法 $1+3s$ 次，新函数调用
$1+2s$ 次。零轮时均为一次。恰删除每轮已经计算过的同一当前平方，
不删除任何验证等式。函数外 `complete_projector_ideal` 的平方
及全部 reverse/HNF/degree 门在本改动中仍原样执行。

新增适配器只在显式调用时替换 `closed._lift_idempotent` 这一属性；
固定原源码，经四个精确一次文本替换生成新函数（其中一个仅改函数名）。
没有跨方法或全局乘法缓存，没有保存计算矩阵，没有改变数学输入。

## 3. 与真实日志相对应的成本

24 个 cusp 局部分量，在其 maximal-kernel 返回和 thick-projector
返回之间均恰有六条完整 direct-product 回执。固定调用图给出
$1+3s$ 个 lift 乘法、一次累计正交乘法、一次 projector 幂等性乘法，
故这些分量各实际执行一轮。

第一分量中，direct product 37/38 连续重复同一完整平方：
均为 44253 个实际非零 unordered pairs。两返回时间分别为
18:36:45.5742287 与 18:37:25.3397995 UTC。
相同的局部重复在 24 个分量全部存在。其两返回 marker 间的时间
合计为 750.508 秒：18 个窗口约 38--43 秒，六个稀疏窗口约
0.4--0.94 秒。该数是旧进程中重复计算对应的观测窗口，
包含其相邻规约费用；不是新运行的速度保证。

此前已发现的 captured-return 绑定修正是另一处改变：
对这 30 个 HNF，只会加速恢复原二次常数域后的第二次全生成元回验；
第一处 prime-field 回验仍按原后端执行。它没有覆盖上述环乘法重复。

## 4. 其它成本目前能确认到哪里

`complete_projector_ideal` 在 quadratic bind 之后生成自己的
namespace，已经捕获正确的全余数、全坐标和完整乘积 wrapper；
其两次 `_sparse_left_product` 与最终
$H=C I+H(1-e)$ 返回也已走该 wrapper。没有在此发现第二个与
HNF 相同的过早捕获旧别名问题。

24 个 projector 的末次 suffix marker 至最终返回尚有约
112--219 秒的未细分区间。它同时包含完整 span 闭包、
`_monic_determinant`、全生成元余数、两次完整乘积、
全坐标及其回乘、最终返回和全部 digest。当前日志没有这些操作之间
的计时点，不能把这段时间全部归给某一操作。

`_complete_native_matrix` 确实在每次使用时对原矩阵与不可变快照
作完整等值比较。当前 primary/projector 构造没有为原
`primary.basis` 建立不可变性保证；只有缓存内的副本被设为
immutable。因此本次不跳过该比较，也不凭数学上的“不应改变”
冒认 Sage 的实际 immutable 状态。

## 5. 单独软件核验的范围

新小检查只用完整的
$\mathbf F_{29^2}[t,x]/(t^e,x^2-x)$，$e=1,2,3,9$，
并保原二坐标基和真正非素域系数。它对比：

- 原、新完整幂等元与 receipt 全部字段；
- 每一次保留的完整乘法输入和输出、原顺序；
- 删除调用恰好是已算当前平方；
- 零轮、多轮、重复调用均无跨调用状态；
- 故意不足的 nilpotence bound 仍按原异常拒绝。

这只是软件正确性检查，不构造原曲线，不替代原 six primary、
四交、Norm 或最终 shadow 接受门。
