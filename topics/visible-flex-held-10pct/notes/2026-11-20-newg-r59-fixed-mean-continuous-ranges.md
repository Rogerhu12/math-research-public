# λ.002 M8 真场：固定 512 点高度均值的连续径向区间界

**状态：区间计算已实际完成并 exit 0。范围针对指定有限均值规则，不是连续角积分替代，也不是整桥或闭面证书。**

输入仍是新软启动 \(q=.06,\lambda=.002,\tau=1,S=.5,b=.2\) 的 M8 物理 quintic。
其 run SHA-256 为
be83041236a3832194d52aae6b21569e2e463b67548e4b0b0b1b8cd683f323a1，
physical SHA-256 为
a0d00429c4a6aac10165b07a4d8048dfe08aad4d3afda0dcbad7c4b30ab5bd5f。
该场 metric 仍未过门，本计算没有修改它。

## 1. 被认证的 mean 对象

固定原 512 个计算角节点及相同正权，记

\[
M_{512}(s)=\frac1{512}\sum_{j=0}^{511}W_z(s,\psi_j),
\qquad
W=V_{\rm normal}+vP_\psi.
\]

节点读取为源生成的 binary64 实数；三角函数由严格区间包围。
这是有限规则本身的连续径向函数。没有在计算中改变节点数、引入材料角权重、
重置高度常数或把 \(M_{512}\) 换成真实角积分。

源的径向背景位置使用字面 64GL 积分函数，而 Frenet 速度中的径向坡度
仍是源手填的 \(-\sin\phi(s)\)。
前者的数学导数不被自动等同于后者。因此本核以自动微分计算上述同一函数的真实 \(M_{512}'\)：
分母中的半径用字面 GL 函数的真实导数，手填坡度作为另一项明确函数求导。
它不直接引用原手填 dW 数组作为严格导数。

与之比较的标量是源转角函数的
\(b(s)=\cos\phi(s)\) 及其真实导数 \(b'(s)\)。
源函数到 R59 真积分参考的坐标、积分和导数差另由独立 bridge 误差证书支付。

## 2. 连续区间核

本核复用 R23 的
[向外数组区间算术](../scripts/finite_closure/m3_m8_closed_map/interval_geometry_kernel.py)：
四则、平方、平方根逐次 nextafter 向外；有限和含舍入误差带。
节点三角常数用 60 位 mpmath 区间求值。
变化转角和相对角的 sin/cos 使用有限 Taylor 多项式及显式余项；
只在已验证 \(|x|\le2\) 时使用，sin 至 29 阶、cos 至 30 阶。

为避免圆背景的尺度依赖过度放大，将截面导数写在材料圆柱正交架中：

\[
U=P_\theta/a,\qquad V=P_{\theta\theta}/a,\qquad
a\kappa=\frac{|U\times V|}{|U|^3}.
\]

圆背景在这个架中恰为 \(U=(0,1,0)\)、\(V=(-1,0,0)\)；
完整有限非均值项、真实角图及其径向导数仍逐项保留。
切向、法向、副法向和 Frenet 平方根均用区间自动微分。
桥上原 exact-lift 窗口恒为零，这一事实不用于删除任何仍活动的 lift 项。

先按实际 PPoly、角图和两个转角接点分段，再只在区间根域或目标差量未支付时二分。
最终 4983 个接受区间覆盖整个桥；共有 9648 次区间评价、4665 次二分，
最大二分深度 8。两个单侧端点极限均被覆盖，不以接缝差很小代替精确 \(C^2\)。

## 3. 已证明的范围

最终统一上界的精确 binary64 值为

\[
\sup|M_{512}-b|
\le\frac{5764080742422785}{576460752303423488}<\frac1{100},
\]
\[
\sup|M_{512}'-b'|
\le\frac{637256918640983}{2251799813685248}<\frac{283}{1000}.
\]

两数的浮点显示分别为
\(0.009999086181306628\) 和 \(0.2829989214707598\)。
上述显示门另用 Fraction 进行了严格比较。

在这 512 个被均值规则实际使用的角节点上，整个径向区间的 Frenet root 还满足

\[
\mathrm{root}\ge
\frac{7207386942435327}{4611686018427387904}
>\frac{39}{25000}.
\]

这是固定节点规则的定义域证书，不称整个连续角上的 Frenet 域已认证。
最终几何图的全角正则性应由完整 R59 第一导数界等另行支付。

七个径向点还与原模型独立 velocity_s 查询作了有限接口核对：
原 mean 及其手填 mean 导数都落入本核的点区间；
区间宽分别不超过约 \(2.8\times10^{-13}\) 和 \(4.7\times10^{-12}\)。
这只是公式接口诊断，严格结论来自上述覆盖整个径向域的区间运算。

## 4. 原函数与剩余契约

取同一入口高度基准，则

\[
J(s)=\int_{s_b}^{s}(M_{512}(\zeta)-b(\zeta))\,d\zeta
\]

满足 \(J(s_b)=0\)、\(|J(s)|<(s-s_b)/100\)。
这一步使用明确的真实原函数，无须 GL6 高度查询，也不涉及入口以前的积分。
用于 R59 的参考变量 \(\xi\) 时，仍须加上真实 \(c\) 与源转角到真参考的差量；
不能把它们在公式中写成零。

本结果与已完成的非均值 Bernstein 全角界可以组合，
但还没有取消以下独立条件：实际绝对入口高度范围、背景到真参考的完整二jet差、
以及保存的分别舍入多项式应如何定义成一个明确的公共 \(C^2\) 对象。
也没有将 M8 原 metric 失败改成通过。

## 5. 可复现性

[已执行源](../scripts/resume_m3/certify_r59_fixed_mean_ranges.py) SHA-256：

    ab08dc1dc7f24f6e92e3d64fcc530767cb66f5ae5a2940f953460a3274b6a1a5

依赖区间核 SHA-256：

    6234c458d303dfd2e47dcf1e1a6ee54a3d466118a8aea4d76f66013154c034e7

实际完整输出 SHA-256：

    bcb418aa609b9b6bf01542280842a5c76278dfac75f1dc03eb45305cf7f71826

实际命令：

    python geometry-work/certify_r59_fixed_mean_ranges.py \
      --source-run m3-work/newg-wide-lambda0p002-tau1-linear/run.json \
      --physical m3-work/newg-wide-lambda0p002-tau1-linear/physical.npz \
      --support-dir math-research-public/topics/visible-flex-held-10pct/scripts/resume_m3 \
      --interval-kernel math-research-public/topics/visible-flex-held-10pct/scripts/finite_closure/m3_m8_closed_map/interval_geometry_kernel.py \
      --out geometry-work/newg-lambda0002-r59-mean-certificate.json

默认 mean_nodes=512、difference=.01、derivative-difference=1；
输出记录的是实际达到的更小上界。实际耗时约 162 秒。
发布后源位于 scripts/resume_m3。可重算输出与场数组未入库。
