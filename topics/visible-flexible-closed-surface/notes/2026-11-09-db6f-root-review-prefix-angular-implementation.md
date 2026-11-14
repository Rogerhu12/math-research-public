# 第一档前缀角弧证书实现的 root 全文静态独审

状态：**PASS，允许执行已限定的两局部/一次继承接口验证。此时尚无新运行结论。** 审查者 Astra-visible-flex-db6f0b0e，2026-11-09。

- wrapper `scripts/db6f-audit-prefix-angular-metric.py`：SHA256 `42e7d222c40512fec2d4fd757544d630b3e372487322e27eb3571a06519eb2fb`。
- 独立结果检查器 `scripts/db6f-audit-prefix-angular-fixtures.py`：SHA256 `0f4b1e146d137564fac1924f13c8b877691803036a284ca754a4feb706bf7643`。
- 数学前提及全文审稿：`db6f-prefix-angular-metric-refinement-method`、`db6f-root-review-prefix-angular-metric-method`。

## 1. 实际输入和同图范围

已读wrapper全部源码及其复用的 `db6f-audit-prefix-metric-budget.py`，并核对原 coefficient backend 的 `geometry_coefficients`、`value_range`、有理三角函数、common-cut v2和既有 closed-budget v2 的输入接口。

wrapper把基图、共切图、binary数组、实际尾manifest及全部分片、common-cut/tail reader、analytic target/meta/数组、桥参数提取器、唯一精确桥证书、完整原metric报告绑定。原报告的几何/目标/数组及原后端哈希均相符，检查全部原区间数、正a/ρ界和整段覆盖。target binary端点与基几何mesh逐值比较，无容差拼接，且每target区间完整包含于一个实际多项式跨内。

这些检查不会重新证明已审供应器或唯一根；输出明确声明该条件。对未来新图仍必须提供自己的已审原基线和同g供应对象，不能仅更换文件名沿用旧图界。

## 2. 实际数学计算

目标残差形成与已审原程序相同：先在Fourier/径向幂系数域相消，再用局部角范围估计。代码的 $\rho=1-e\cos\varphi$、$\Theta_s=-e_s\sin\varphi/3$ 及三个目标坐标系数均正确。对角分割后的物理误差，复用的 `angular_bound` 精确实现

$$
H_{11}=E_r-2vF_r+v^2G_r,\quad
H_{12}=(F_r-vG_r)/(a\rho),\quad
H_{22}=G_r/(a\rho)^2,\quad v=\Theta_s/\rho.
$$

两条绝对行和最后显式向上舍入。径向Bernstein对整父区间有效；角弧上a/ρ严格正后才除法。geometry模式表示内建三重对称性，metric最高谐波编号2M，故2M项三角表覆盖所有残差和目标项。

新 `trig_table` 仅将调用原 `trig_point` 的缓存参数提前作同样的精确模2化；内部极值仍在未约化原弧上用有理ceil/floor核验。跨周期、负的规范化中心和端点极值都没有丢失。其数值算法与原uniform trigonometry逐弧相同。

## 3. 继承、精确目标转移与分区

完整旧界有效于任何子盒，所以每叶取它、重算父区间界及角弧界中适用者的较小值合法。原target上的源界均是已有binary上端点的精确Fraction；取min/max不产生新的不可表示有理上端点，因此完整输出 `metric_operator_upper=float(source_max)` 仍精确表示该已取得上端点。

桥转移的 $\varepsilon(1+\eta)+\eta$ 则自始至终用Fraction。预算筛选、是否二分、最后达标及汇总均包括这项转移；其打印函数对一般有理上端点作必要的nextafter上调。checked source字段与已经转移字段分开，既有closed-budget v2仍只读取源字段、转移一次。

DFS栈以相反次序压入右/左子弧，使实际写出的叶按角度递增。所有端点和中点均为有理数。写盘后主程序重读全部叶，核实际SHA、父区间、物理端点、角cursor、正分母、目标转移、预算布尔量与最大值；完整角周期/完整选择集合必须结束于零cursor。局部选择明确不提供全prefix metric字段；整体继承则验证原完整target分区。

分母未证正或深度耗尽时只能回退到有效旧界，不会删除盒或假标通过。新角界未达预算仍可输出有效保守完整覆盖，但target_met必须为false。

## 4. 数据和验证接口

gzip分片一次最多512行，逐件小于5MB。最终完成报告只有在所有请求区间与写盘重读结束后生成。没有生成或查看渲染图，也未导出网格；没有运行任何ODE。

独立检查器未导入几何或区间后台。其有理覆盖、逐叶转移、最大值、局部不能冒充全图、两原区间算术及128弧与已闭算例一致性检查均正确。二叉森林的访问数等式 `evaluations=2*leaves-256` 对两个128弧根集合正确；它检查确有二分，而不凭描述认定执行过。宽松完整继承验证明确要求几何对象未构造、原/角后台调用数均为零，且结果与既有完整closed-budget相同。

当前批准的定向运行仅为M12区间0/74预算1e−8、128初始弧/深度1，以及2575区间预算1e−6的完整旧界继承。它们仍需真实退出码和检查结果；不因此批准尚未运行的全域M12加密，也不认证未来M15。
