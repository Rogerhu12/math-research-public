# W2C reference：零端点球的非负外包修复

2026-11-20，`visible-exact-astra-ac637-20261120`。本说明只证明包含关系；本地未执行科学计算。

## 已发生的失败

公共 run `44716804300/1` 完成原153个 reference/centre parent、155个比较 panel、4650行/4801闭交覆盖，随后在第一次 `profiles.at(j, whole_box)` 调用 `_segment` 时触发 `true nonnegative segment length`。其科学输出确认 `saved_record_count=0`。原运行的完整失败回执保留，未产生可重算的成功新标量。

`RadialDomain.partial_length` 对全 panel 给出的数学量是 `h*t`，其中真实 `h>0`、`0<=t<=1`。但其通用球表达 `interval(0,1)*full_length` 必须向外取整，表示球的下端可以略小于0。把“真函数非负”和“这个球的下端非负”混同，导致了本次失败。不能直接删除 `_segment` 的校验，也不能对任意有符号长度取绝对值。

## 一、精确几何资格

box `(i,a,b)` 仍表示真实第 `i` 个 panel 上全部 `a<=t<=b`，并检查 `0<=a<=b<=1` 与该 panel 的有向长度下端严格正。prefix 长度的比例范围是 `[a,b]`，suffix 是 `[1-b,1-a]`。

同 panel 的 ordered pair 用 `a<=u<=b`、`c<=v<=d`、`u<=v`。非空条件为 `a<=d`；其长度比例由 `[max(0,c-b), max(0,d-a)]` 包含，完全位于 `[0,1]`。

因此这两类长度的**真值集合**已经证明位于 `[0,+infinity)`。若原有向球为 `X`，取 `X intersect [0,+infinity)` 保留每个真实根、每个 panel 内点和每个 ordered pair。第一 panel 的左端仍是原不确定真实根；没有改成包络端点。

新版 reference 内的 `_geometric_partial_length` / `_geometric_ordered_span` 先验证上述精确条件，再形成该交集的非负球外包。原 `_segment` 的 `api.lower(length)>=0` 校验逐字保留。

## 二、不以粗幂2代替半径的零端点构造

设已证明真值落在 `0<=l<=x<=u`。先调用原 `interval(l,u)`。如果表示球的下端已非负，就原样使用。否则令其有向上端为 `U>=u`，并用原 API 构造对称球

\[
B=\operatorname{interval}(-U/2,U/2)=[-R,R].
\]

这里 `R` 是该外包球的二进制半径端点，不是另选幂2。代码核验 `lower(B)=-upper(B)`，取 `R=upper(B)`，再构造 `B+R`。在当前320位 Arb 接口中这个半径可精确作为中点；代码继续核验

\[
\operatorname{lower}(B+R)=0,\qquad
\operatorname{upper}(B+R)\ge u.
\]

这些后置条件成立时，`B+R=[0,2R]` 确实包含全部 `[l,u]`。若实现未给出这些条件则明确失败，不隐藏舍入问题。扩张只有通常的球半径量化，没有粗幂2替换，也不使用 `abs` 猜测真值符号。这个写法只用现有 `interval/lower` 与普通算术，不新增 `rad()` 或构造器接口依赖。

## 三、同类非负参考量

已有解析不变量给出 `p>=1/16`、`0<=tau<=1`、`sigma>=0`、`H>=0`、`0<=K<=1`。原 `_clip` 一直在这些已证明集合上取交。新版仅把非负交集的最后球表达换为上一节的外包。

同理，`g`、完整 ordered tau products、到右端的传播值是真正的 `[0,1]` 值；其乘法球也可能在零端点微跨负轴。对这些乘积使用相同的已知不变量交集，不改变乘积顺序，不删除任何 panel。所有有符号矩阵和系数仍保持有符号。

reference 内全部 partial/ordered integration length 调用共用经几何证明的入口。单速率与双速率正积分质量的输出也使用同一非负外包。正 impedance、scaled pivot、真实正 panel length 等原来的严格正下端校验仍保留；没有把零或负 pivot 宣称为可除。

## 运行与范围

本次仅修改 reference 的区间表示，固定 WVC definition/diagonal chain、原真实根、真实 eta、S、193 mean/atoms、七 ports、全部 coefficient 支持和父50目标都不变。本地只作 AST、源差异与字节/SHA 元数据检查。新公共运行可以接续尚未完成的三个 L 记录；旧失败运行不改写成成功。

该修复不证明 `L<1/128`、不计算任何有限门或逆，也不提前判断 R139 的预算结果。
