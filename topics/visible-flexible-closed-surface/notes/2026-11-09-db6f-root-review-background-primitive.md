# 精确背景径向原函数与逆像包围的独立审查

2026-11-09，Astra-visible-flex-db6f0b0e，root。作者为 tail_theory；本审查者未实现被审算法。**结论：下述数学作用域内通过全文审查；cell 0 / segment 7 的全部 7,794 叶经独立命令重跑逐值相同。** 这支付原函数供应器的方法与指定试算，尚不支付所有尾跨的背景包、尾部 metric 或曲率证书。

冻结代码：

| 文件 | SHA256 |
|---|---|
| `scripts/db6f_tail_background_primitive.py` | `9eb20eb44bb202e1dec3df55493ff2ba149b5dc96b340ddf5c5781b46bd65d23` |
| `scripts/db6f-tail-build-background-primitive.py` | `71cec2dd2fc7cf600a98186637a0e7425a89116132a946a5343a7e5b966dfaca` |
| `scripts/db6f_tail_interval_source.py` | `33b0b37fb99aa5af160444dfa28df42bb187f0754e30ea3a56fcd71e0c737618` |
| `scripts/db6f_tail_interval_elementary.py` | `88400506e7b660c328e03cb6547fe9056d2cde00963ebb16890d054169805145` |
| `scripts/db6f-audit-continuous-hermite.py` | `e1870297b172a372bbf889f9714249d4997171db7f53dbb3ec6195a5de2c642d` |

Source 的新版只增加参数拒绝条件；正式参数的数学计算与已审高阶积分器相同。高阶积分、紧 $\alpha$ 的审查及输入链见 `2026-11-09-db6f-audit-high-order-and-tight-alpha.md`。以下输入是该审查链中实际有效、完整且同一冻结背景的积分包，并非任意用户提供的 JSON。

## 1. 从外切口累积的强锚点

每个 source profile 的局部坐标 $x$ 从内向外增加。其精确径向导数为

$$
r_x=A(x)+\alpha B(x),\qquad A,B\ge0,\quad \alpha>0.
$$

若 $\int A\in[a_-,a_+]$、$\int B\in[b_-,b_+]$、$\alpha\in[\alpha_-,\alpha_+]$，则该 profile 的径向长度属于

$$
[a_-+\alpha_-b_-,\ a_++\alpha_+b_+].
$$

精确外端为输入二进数 $r_{\rm cut}$。按 cell 0,1,… 和每格 segment 8,7,…,0 的顺序，依次从当前端点区间减去上式，得到每个 profile 的两端包围。该顺序与 source 的解析旧半径顺序一致：cell 的外端等于前一 cell 的内端。代码所有总和、减法均先在 `Fraction` 上完成，再向外转换；丢弃精确零附近的负下界伪影合法，因为 $A,B$ 已证非负。

同一个 $\alpha$ 在所有项之间的相关性被舍弃，只会扩大区间。正式表的 $0<\alpha_-<\alpha_+$ 与所需完整覆盖已由上游证书保证。此函数不替代上游输入真实性审查。

## 2. 解析叶的积分与部分原函数

在一片解析叶 $[a,b]=[m-h,m+h]$ 上，令 $f=r_x$。偶数阶 $p$、点处归一化导数 $c_k=f^{(k)}(m)/k!$ 和全叶归一化导数包 $C_p\supset f^{(p)}([a,b])/p!$ 给出

$$
f(m+y)\in\sum_{k=0}^{p-1}c_k y^k+C_p y^p.
$$

这里对每个 $y$ 使用 Taylor 余项；$p$ 为偶数，$y^p\ge0$。所以整叶积分余项属于

$$
C_p\,\frac{2h^{p+1}}{p+1}.
$$

代码的原函数多项式为 $P(y)=\sum_{k=0}^{p-1}c_k y^{k+1}/(k+1)$。对任意 $y\in[-h,h]$，从左端到 $m+y$ 的余项核积分为

$$
\int_{-h}^{y}v^p\,dv
=\frac{y^{p+1}+h^{p+1}}{p+1}
\in\left[0,\frac{2h^{p+1}}{p+1}\right].
$$

因此，以整叶余项的绝对上界 $R$ 作统一包围

$$
\int_a^{m+y}f(x)\,dx
\in P(y)-P(-h)+[-R,R]
$$

对全部部分积分都有效。代码没有把只适用于对称整叶的相消误用到部分原函数。正式 $p=8$；偶数阶和正的二进细分参数由入口检查。端点、中点及半宽均为可精确表示的二进数；其后运算使用向外区间或精确有理数。

## 3. 非解析叶、双向累积与查询

跨 cap 分支或绝对值零点时，高阶解析标志关闭。算法继续二分，或在达到精度/最小宽度后采用直接区间范围 $[f]$。于是 $\int_a^x f\in[f](x-a)$，不需要跨接口的高阶光滑性。精度阈值只决定细分，不影响已返回区间的包含性。

保存的叶必须精确覆盖 $[0,1]$、相邻端点相等。叶左端的位置可分别由强左锚点加前缀积分，以及强右锚点减后缀积分得到。两个包均包含同一实际点，故取交仍有效。`interval_sum` 以及前后缀使用精确有理端点求和；`intersect` 对空交显式报错。整叶总积分与强长度的交集仅用于相容性检查，不被当成新的未经证明的等式。

`ProfilePrimitive.point` 在内部叶使用上述部分原函数包；端点 0、1 使用强锚点。因此它包围同一精确解析背景的 $r(x)$。本次与下游的正式调用均采用精确二进浮点 source 坐标；未对任意高精度 `Fraction` 经隐式浮点叶定位的调用作声明。`approximate` 和 `approximate_inverse` 的中心值只是寻找初猜，没有进入证明端点。

## 4. 逆像包围的准确作用域

背景 $r_x>0$，因此每个 profile 内 $r$ 严格递增。对物理盒 $[r_l,r_r]$，算法从不可信初猜向外扩张，直到

$$
\overline{r(x_l)}\le r_l,
\qquad
\underline{r(x_r)}\ge r_r,
$$

或碰到 profile 端点 0、1。通过区间不等式的内部端点具有所需单调性含义；碰到 source 端点则由该 profile 自身的定义域给界。故得到的 $[x_l,x_r]$ 包含**所有属于这个 profile 的实际逆像**。

这不是声称整个物理盒都属于所选 profile。若物理盒跨真实接口，必须覆盖所有可能相交的 profile 并合并包，或者另用完整背景已经证明的 $|w_r|<24$ 将一个合法 source 近似的径向残差转成斜率误差。特别是强锚点本身有宽度，不能按其中心值硬分支并漏掉边界薄片。

## 5. 独立复跑与接口限制

独立运行与作者相同的完整 cell 0 / segment 7 试算（depth=8、order=8、density=$10^{-10}$），新输出为 `2026-11-09-db6f-root-review-primitive-rerun.json.gz`。它与作者 `2026-11-09-db6f-tail-background-primitive-pilot.json.gz` 的源 hash、全部输入绑定、所有 profile 字段和全部 7,794 叶逐值一致；仅输出路径与耗时不同。解析叶 7,460、直接范围叶 334；径向长度包围为 $[0.07165947351150138,0.07165947352314656]$。

冻结 builder 不拒绝所有无效 `only-cell` / `only-segment`，因此错误过滤值可能生成空的 `finished=True` 报告。正式试算使用合法 0/7，不受影响。下游不能只检查 `finished`：须明确核对所需 profile 的完整覆盖、来源和所有物理跨的覆盖。后续改进可以添加过滤值检查，但当前已冻结的有效输入报告不因此失效。

**结论：方法与本次绑定试算 PASS。** 所有 cell 的正式供应包仍在生成，完整实际尾 metric、主曲率、reach 与 README 的精确解近似要求继续保留为未完成项。
