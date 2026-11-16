# R599 — 准确工厂有理参数的逐字解释与真实 coast 配方路径

**作者：OpenAI ChatGPT（geometry 协作线）。日期：2026-11-16。**

**可信度：已证明（限下述输入表示与来源接线命题）；本组件未执行，不包含新实验、求解成功或资源完成结论。**

## 599.1　处理的两个实际问题及边界

[R568](R568-actual238-complete-sampling-rational-word-and-closed-recipe-failures.md)
已经分别记录 actual238 的真实终态：完整采样返回以后，two-phase driver 在解释准确工厂的有理字符串时抛错，两个求解 phase 都尚未启动；另一个闭面入口仍使用过时的固定配方文件名，在读取真实 launcher 的配方回执之前失败。本结论只处理这两个来源接点。

第一处不是参数值不相等的反证。原 driver 把一个合法的准确有理串直接交给 `float`，例如原报告已返回的
`338454297525575/1125899906842624`，而 Python 的普通浮点字符串语法不接收这一表示。真实候选、工厂输入、准确定义以及 BVP recipe 都仍有各自完整来源。修复必须解释这些原值，继续执行原来的八十字节相等判断。

第二处不依赖能否最终得到 accepted450。真实 launcher 已把配方的绝对路径、完整字节数、SHA256 返回在 `recipe`；闭面入口应读取该回执所指的当前文件，再按原 `read` 检查实际 bytes/SHA。只有随后原 accepted450、quiet、deadline 等条件满足，才可以执行下游几何。不能用另一个文件名缺失代替这些状态，也不能从 partial 构造父场。

本组件不修改实际 C、准确十参数、定义 DAG、材料图、初值、数值 profile、RHS、native、Jacobian、FD、fullDN、末审计或几何判据。不降低磁盘门、改变工作分配或重开时钟。已经运行的 238、241、247 源码保持冻结。

## 599.2　准确报告的真实生产合同

完整原工厂为
`geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py`，
46691 bytes，SHA256
`72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682`。

其 `rational` 明确接受非布尔整数、有限原浮点数、`Fraction` 和可由 `Fraction` 解析的字符串。有限浮点数用 `Fraction.from_float` 解释，保其准确二进制数值。其 `build_expression` 对全部十个 `recipe["ten_parameters"]` 使用该函数；准确 definition 写入
`[str(p) for p in model["parameters"]]`。最后结果的
`starting_parameters` 则原样来自这次 recipe 的 `ten_parameters`。因此它可能是 `n/d`，不是必须能交给普通 `float(str)` 的显示小数。

原
`geometry_20261115_continuous_ten_same_metric_profile.py`，
30299 bytes，SHA256
`3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6`，
通过 `bind_definition` 先读取并核验这次完整 result、definition、工厂源码、原 C、两 jet、原 core 和 recipe 身份。它逐项比较报告和定义的准确有理值。因此 R599 接受的字符串必须来自这个已经绑定的实际 `CurrentTenProfile.data["report"]`，而非由调用者另写一个看似相同的十元组。

R503 的实际候选生产合同也明确：先将原十个 Decimal50 有理值投影成 binary64，再只把 `p3/theta3/eta3` 赋为正零，保留其余七个投影字；准确工厂点由每个被选浮点数的 `Fraction.from_float` 产生。真实候选 adapter 为34123 bytes，SHA256
`237882e9fee9943e11b897c52118087753eb1d63e5c917e7382f14b5e8cb9399`。
它的完整文字变化见 R505 的46-view计划，候选 `project_candidate` 的完整替换保留每个原值、投影值、准确 dyadic、改变下标及逐字来源。R599 不再运行一次候选选择，也不把原 actual202 的点与后来明确改变的 coast-base 点混同。

由此，在当前候选的非零分量上，准确有理数已经恰好是一个有限 binary64 数。将它正确转换到 binary64 应回到原字，不能从 `n/d` 的分子、分母各自取浮点再除法，也不能先转成截断十进制再取浮点。三个显式正零同样有明确原字来源。

## 599.3　完整有理数到 binary64 的整数算法

新标准库源
`geometry_20261116_accurate_ten_source_boundaries.py`
提供 `factory_parameter_words(values)`。它返回依原顺序排列的十个 little-endian binary64 字，共80 bytes。该函数内部不计算任何浮点商或对数。

令非零准确输入为
$$
x=(-1)^s\frac{n}{d},\qquad n>0,\quad d>0.
$$
`Fraction` 已给出准确整数分子和正分母。先令
$$
e_0=\operatorname{bitlength}(n)-\operatorname{bitlength}(d).
$$
由整数 bit length 的定义，$\lfloor\log_2(n/d)\rfloor$ 只能是 $e_0$ 或 $e_0-1$。若 $e_0\ge0$，比较 $n$ 与 $d2^{e_0}$；若 $e_0<0$，比较 $n2^{-e_0}$ 与 $d$。必要时减一，即得到准确指数 $e$，整个判断是整数比较。

对非负有理 $a/b$，写 $a=qb+r$，$0\le r<b$。最近偶数舍入为
$$
\operatorname{RN}_{\rm even}(a/b)
=q+\mathbf1_{\{2r>b\}}
 +\mathbf1_{\{2r=b,\ q\ {\rm odd}\}}.
$$
两个加数的条件互斥，源码使用同一布尔条件只增加一次。这里没有任何中间舍入。

### 正规范围

当 $e\ge-1022$，求
$$
k=\operatorname{RN}_{\rm even}\!\left(\frac nd\,2^{52-e}\right).
$$
若 $52-e\ge0$，左移分子；否则左移分母。正常情形 $2^{52}\le k<2^{53}$，指数域为 $e+1023$，小数域为 $k-2^{52}$。若舍入产生 $k=2^{53}$，改取 $k=2^{52}$、$e\leftarrow e+1$。这正是跨 binade 的同一数值，未作第二次舍入。

若初始或进位后的 $e>1023$，结果无法作为本合同的有限 binary64 字返回，函数显式抛出 overflow。它不返回无穷大，不钳制到最大有限数，也不把缺失值换零。

### 次正规范围及其边界

当 $e<-1022$，直接在统一的次正规单位 $2^{-1074}$ 下计算
$$
k=\operatorname{RN}_{\rm even}\!\left(\frac nd\,2^{1074}\right).
$$
此时 $0\le k\le2^{52}$。$k<2^{52}$ 对应指数域0、小数域 $k$；$k=2^{52}$ 恰对应最小正规数，指数域1、小数域0。这同时覆盖最小值附近的 underflow tie 和次正规／正规交界，没有切换单位造成的二次舍入。

正负号最后写入最高位。负的非零输入若向零下溢，仍返回负零。所有整数移位、整除、余数和位组合均准确。因此：

**命题599.A。** 对本节有限准确有理输入，若其 IEEE binary64 最近偶数舍入结果有限，源码产生其准确 little-endian字；若结果非有限，源码显式报错。正规、次正规、二者边界和精确 halfway 均包含在此命题内。

这是一条算法的条件证明。本地只编写、读取文字和计算文件身份，没有用任何输入运行该算法，也没有构造执行 fixture。

## 599.4　合法类型、非法输入与零的来源

类型合同必须保留完整的输入信息，而不能使用“能转就转”的宽松容错：

| 输入 | 解释 |
|---|---|
| `bool` | 明确拒绝；原工厂也不把布尔值当数学标量 |
| 原 Python `float` | 直接保存原 `struct.pack("<d", value)` 八字节；指数全1即拒绝 |
| 原 `int` | 作为准确整数，按599.3转换 |
| `Fraction` | 保完整准确有理值，按599.3转换 |
| 原 `str` | 按原工厂 `Fraction` 文法解析，再按599.3转换 |
| 其余类型 | 明确报错，不调用不明对象的 `__float__` 或字符串化 |

字符串分母为零、语法不合法、NaN 或 infinity 均不产生有效有理数。有限浮点路径逐位排除 NaN/Inf。准确有理的 overflow 也不是允许的结果。十项数组的任何错误包含原下标和参数名；不跳过该项、缩短十元组或补默认值。

`Fraction` 的数学零没有符号；因此无另一个词来源的 `Fraction(0)` 和整数0给正零。字符串若解析为零且剥除外侧空白后的首字符为 `-`，保其显式负零约定；原浮点 `-0.0` 直接保原字。非零负有理若下溢为零同样保负号。这里没有把原精确数学零臆补成某个先前丢失的浮点符号。

特别地，原 R503 生产器已经把三个改变分量明确赋为 `0.0`，并把准确值写成 `"0"`。该当前合同得到正零，与其实际候选一致。若某个未来来源声称保留负零，却仅提交没有符号的数学零字符串，R599 不替它猜测；原完整 recipe 与报告字比较仍会报告不相同。

## 599.5　原80字节相等判断保持

当前 R570 first-driver 在原 R503 driver 的相同位置仍有
`raw_words(full_p) != raw_words(report["starting_parameters"])`。其中 recipe 侧的 `full_p` 是原完整候选通过原 finite-vector、candidate-binding 和 profile 输入核验后的实际十个数。

真正 caller 的最薄变化是：

```python
if raw_words(full_p) != d.accurate_source_boundaries.factory_parameter_words(
        target_owner.data["report"]["starting_parameters"]):
    raise ValueError("The actual ten recipe differs from its same-job factory input words")
```

左边及原错误条件不变。右边按准确报告的实际语法解释所有十项，再比较完整80 bytes。函数不是以一个容差“近似相等”代替逐字相等；不是只比哈希；不是把报告改成 recipe 的值。由于报告、准确 definition、完整原 C 等已由原 loader 绑定，算法只完成原来遗漏的表示转换。

原 driver 的另一个 `raw_words(H)` 位于当前完整 H 的身份计算。它保原字节，不调用本组件。same-driver、union-driver、native client、state/RHS/J 的原字路径均不改。R599 的适用范围是准确工厂参数报告边界，不能以本命题为理由替换所有浮点数组处理。

**推论599.B。** 对实际 R503 候选中由原 binary64 值形成的非零准确 dyadic，以及三个明确正零，599.A 返回原候选字。因此若现有 profile/recipe 来源和原字一致，修复不会因 `n/d` 文法失败；若原字不一致，原判断仍失败。该结论不保证之后的 design453 或 frozen450 有解、收敛、满足门或返回 checkpoint。

## 599.6　真实配方回执的路径命题

原当前 launcher 已返回
`recipe={file,bytes,sha256}`，其中 `file` 是实际运行目录下的绝对路径。R568 已返的当前 basename 是
`actual202-coast-base-ten-full453-frozen450-recipe.json`，父目录是原 namespace 的 `actual202-ten-BVP-input`。

新 `actual_coast_recipe_path(base, descriptor)`：

1. 要求这三个实际字段的类型完整，bytes为非负整数，SHA是完整64位小写十六进制；
2. 解析真实原 namespace，要求回执路径为绝对路径、没有 `..`；
3. 要求其准确当前相对路径为
   `actual202-ten-BVP-input/actual202-coast-base-ten-full453-frozen450-recipe.json`；
4. 不接受 symlink 文件或经中间 symlink 改向的预期路径，不接受逃出原 namespace；
5. 返回真实普通文件的路径，随后仍由原 caller 的 `read(path, launch["recipe"])` 检查全部实际 bytes/SHA。

它不以同名或已有SHA推测文件内容，不在旧路径创建副本，不取另一个 job 的配方，不使用 cwd 拼猜。实际缺文件仍是来源未付，完整异常仍由原 workflow 记录。

最薄 caller 改动是：

```python
recipe_path = self.accurate_source_boundaries.actual_coast_recipe_path(
    self.base, launch["recipe"])
recipe, recipe_id = read(recipe_path, launch["recipe"])
```

原 `read`、schema/request字段、原 deadline 的 recipeSHA、actual run/source、accepted450、quiet、stop、八阶段和独立 held 条件均保留。不是把“存在正确路径”变成“场已接受”。

**命题599.C。** 在实际 launcher 回执、原 namespace 和完整字节核验成立时，上述调用读取的正是当前 launcher 已绑定的同次配方。过时路径不会遮蔽已有配方；若配方不存在、来源不符或完整内容不同，原来源责任仍明确失败。

## 599.7　真正来源注册及未付范围

本结论交付一个小标准库源、完整证明及接口，不交付一份伪已执行的 run。后继 R597 必须把该源加到实际 public source 闭包，生成新的 first-driver 和 closed-entry basename，更新所有引用这些真实字节的 launcher、policy、reader、后继 owner/field 消费者和 metadata 视图。原冻结 caller 不能原名覆写，也不能只改 summary 的 source标签。

driver 已有的 source hash loader 和 `d.closure` 是实际挂接点；closed-entry 的实际同目录 source loader 是另一个挂接点。两者都必须在调用前加载本源的准确 SHA。新完整来源计划将保存每个 baseline、完整 literal replacement/count 和 output identity。R599 本库不单独宣称这条未来完整注册已经完成。

原公开 Actions 的 namespace总钟、BVP cap、所有phase/native/FD/fullDN/final/audit、全域metric/reach/held 和 necessary90000/70 条件继续由原调用链负责。没有本地数值测试、第二套 solver、独立 gate、人工 accepted450、重新采样结果或性能保证。本组件不支付当前剩余的准确连续解、全域误差下降、公共材料拉回、reach/held或反射商距离的实际证书。
