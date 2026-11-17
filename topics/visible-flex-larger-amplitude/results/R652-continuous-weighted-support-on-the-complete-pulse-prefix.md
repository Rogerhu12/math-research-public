# R652 — 同一规范化 pulse 前缀的全连续加权支持认证

2026-11-17，constructive_model；连续读者由 geometry_amplification 编写。**唯一固定完整批次已经自然 exit 0：819/819 准确片全部通过，失败、异常及剩余片均为0。** 对 R648/R651 的同一规范化像 $G$，取

$$
A_{1/4}=\operatorname{diag}(1,1,1/4),\qquad
N=G_\phi\times G_s,\qquad n=N/|N|,
$$

则在整个 $[0,1]\times\mathbb S^1$ 上有严格的便用有理界

$$
\boxed{(A_{1/4}G)\cdot n\ge0.3174736.}
$$

同像的正向材料重参数、绕 z 轴旋转及原上下镜像继承此界。当前对象仍是有边的前缀；本条不声称全闭曲面或 reach 已完成，也不把这个界赋给随后新造的闭合初猜。

## 1. 唯一对象及覆盖

输入文件 `parallel-pulse-a5-complete-base.json.gz` 的 SHA256 为

`26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`。

准确 binary 节点和0/1/2jet的 little-endian float64 串接 SHA256 为

`840193a1cdb37f79d04f5f36f5a0c485c4eb50f3fd2a103af8c4c267d5232793`。

它定义 M320、819节点、818个共享五次胞元。构造角数保持4096。仍令 $c=(0,0,Z_0)$、$b$ 为4096个构造节点的准确有限平均速度、$\lambda=a/b$、$G=c+\lambda(F-c)$。每片的 $|\lambda-1|,|\lambda_s|$ 直接使用 R648 已完成的同一819片报告，**没有重新计算任何归一化量、改变标量或换场**。

前817胞各为一个 `all` 片；最后817号胞按准确标量分界

$$
s_*=1-\frac5{2^{60}}
$$

分为 `before/after` 两片。全部819片固定角覆盖8192、每片4个闭径向子区间，共3276个径向子区间、26,836,992个角径向覆盖盒。最后微片按原胞宽先形成导数，再以准确 Fraction 参数限制 Bernstein 多项式；不重新除以微片宽。

已付的5个代表是 `0:all,390:all,498:all,817:before,817:after`，完整批只原样复用。所有其他814片按原计划各完成一次；中断时仅未完成的那一次调用恢复，完整单片报告没有重算。

## 2. 为什么包围的是实际支持量

写 $r=F-c$。程序实际注入

$$
G=c+\lambda r,\qquad
G_s=c_s+\lambda r_s+\lambda_s r,\qquad
G_\phi=\lambda r_\phi.
$$

不能把 $\lambda$ 当径向常数后求导。这里对每个固定 s，$\lambda(s),\lambda_s(s)$ 被看成该片已付区间内的参数；所得各位置/径向/角向分量仍在一个 degree5 Bernstein **参数族**内。程序对整个参数盒统一包围，舍掉相关性只会增宽。

旋转 $\phi$ 架中，各真实分量普通角频最多640。角导数包含移动架连接。R643§8 的分量覆盖用于位置、$G_s$、$G_\phi$：每个角网点使用区间 FFT 求值与一阶角导数，并以三角多项式二导 Bernstein 上界支付邻近半格的 Taylor 损失；径向 Bernstein 凸包同时覆盖该径向子区间。**没有把最终叉乘、三次支持分子或除法假定为640带宽。**

在每个得到的完整连续盒上，程序重新用有向区间运算形成

$$
N=G_\phi\times G_s,\quad
D_N=|N|^2,\quad
P=(G_x,G_y,G_z/4)\cdot N,\quad
S=P/\sqrt{D_N}.
$$

$A_{1/4}$ 与旋转架变换交换，故这些就是 Cartesian 几何量。只在 $D_N$ 的区间下界严格为正时作正平方根及除法；每片保存全部4个径向子区间的结果。所有819片都通过，故有限覆盖的最小下界支付整个连续域。算术遵循冻结 f512 的有向 IEEE interval 运算；原始 Fourier 与标量输入的准确含义沿 R638/R648 保持。

R638 的正 $q_{4096}$ 重参数只使 N 乘正因子，不改变 $P/|N|$。镜像 $J=\operatorname{diag}(1,1,-1)$ 配合负 s 参数给 $\widetilde N=JN$，而 $A_{1/4}J=JA_{1/4}$；因此原点下支持值相同。绕 z 旋转同理。

## 3. 实际终态及最坏盒

实际最小 binary64 严格下界为

```
0.3174736259234383
```

位置在410号 `all` 片，径向范围 `[.955,.9552499999999999]`（准确端点在报告），子区间2，角网格索引2046。该盒的支持分子包围为

```
[1.68892256321334, 1.6898880238286342]
```

法向长度包围为

```
[5.3190859386655776, 5.319883055799535].
```

最坏片报告：`parallel-pulse-weighted-support-recovery/cell-0410-all.json`，SHA256

`a18843c08623a73d2510776a6f6ab306d548abd42213ded27c0fabd865458748`。

全域另有 $|N|^2$ 的最小区间下界 `0.027558630439173323`、未归一支持分子的最小下界 `0.23475491488997394`，二者都在0号胞。它们与最小单位支持量不必在同一盒。末817号 before/after 两片的单位支持下界分别为 `.40541552466686065` 与 `.40542069642938644`，微片没有漏掉。

终态之后仅作一次 metadata 账核：逐个读取全部819报告，验证 SHA、同一输入/内核/构造4096/证明8192/4sub/β/中心、原径向宽、每片正性及各自所引归一化报告；再用 Fraction 验证片端点连续、首0末1、没有空隙或重复。便用有理数 `.3174736` 小于实际 binary 下界的关系也作了准确 Fraction 比较。该账核没有再次求值曲面。

## 4. 直接可用的 β 转移

沿已刊 β 转移引理，R648 的实际材料图从字面 $z(0)=0$ 出发，$g_{ss}=1$ 且实际 Gram 误差不超过 $4.94\times10^{-7}$，所以同像 $G$ 满足

$$
|G_z|\le\sqrt{1+4.94\times10^{-7}}<1.000000247.
$$

因此对任意 β，

$$
(A_\beta G)\cdot n\ge .3174736-|\beta-1/4|\,1.000000247.
$$

特别是 **β=2/5**，不新增几何扫描即可得

$$
\boxed{(A_{2/5}G)\cdot n\ge
\frac{3349471259}{20000000000}=.16747356295.}
$$

结合 R650 时仍须由未来完整闭面在所有尾段、接缝、平帽和标记处支付同一 β 的支持与曲率。当前开放前缀的支持条件已经完整支付；本条不省略闭合假设。

## 5. 中断账与真实资源

5代表聚合报告 SHA256：

`48d5d0523e0fb3d0d850ccc543cdc25d74feab387c002354fbf85a99f0b03e52`。

第一批97a707在工具会话中断前保存249个完整报告（含5代表）；其最后保存耗时577.1993152400028秒、RSS172556 KiB。不存在成功终态，也没有把消失会话当作成功。随后187c恢复源验证并复用这249项，只调用余下570项，λ调用0。原中断未完成的调用单独记录；此后未扩大网格、预算或择优重试。

续接 session `18950` 已观察自然 `exit_code=0`，完整结果为：819/819、剩余0、失败0、新异常0、fatal=null；其实际耗时1583.0629249939993秒，最大RSS172584 KiB。819份完整单片报告中的科学调用时间求和为2138.668343146008秒；该和不包括被中断未完成调用的时间，也不是杜撰的单进程墙钟时间。各源及参数均在运行期间保持冻结。

## 6. 完整身份与复现入口

原固定计划及源已经冻结：

- 连续科学读者 `parallel-geometry-weighted-support-interval.py`：`f1158760756728ed1cbbdb419ed88a8d47bea2f5fba070bf4c1d7de43d3cfe6b`。
- 原固定批入口 `parallel-model-weighted-support-fixed-batch.py`：`97a707839c3ef45fb47ae9a9d844e0f8f293cb65b4cdd481f84bc48079740f0f`。
- 原819片计划：`a2acf3719692e360f8e5a4d0dce1777882494a05286700ae82c5ff7a5561899b`。
- 本次恢复入口 `parallel-model-weighted-support-recovery.py`：`187c3990b414ebe40a8f8f232720cf943de7e9e3d117f02f922b7930457b6d61`。
- 恢复 manifest：`447150d49573f80b9db282f68fc585c21b4ecd224e33c02467c897e3e13cc814`。
- R648 全部归一化预算索引：`df41433b71147ac11d3f0193be31323d7e23a879cb2b05231d3a3e166b0d88fb`。

最终文件均留仓库外：

- `parallel-pulse-weighted-support-recovery/result.json`：`af8ccd46963230bcc587cd0eab2ab623ddf26a64e2b1ea6999dc9f64e555d4a8`。
- `parallel-model-weighted-support-terminal-summary.json`：`6b33ab61466074becd01a0bdf30424bb5232c53c2de38992553958bf941deaf7`。
- 最终 log 与 journal：均为 `c6df1555334072e3a963a3980ed067902d8a9346df9d73e2d97655dc67210f9f`。

精确 CLI 已在固定计划及中断恢复说明中完整保存：原5代表只运行一次，随后同源固定批补814；若重现实验遇同样中断，恢复入口只复用已有完整报告并补缺项。终态索引逐项给出全部819个科学报告的路径和 SHA，可独立核对每个准确片的完整证据。原始输出不入 Git，本条没有新增科学源或重算原证书。

原固定配方见[完整五代表与批计划](../notes/2026-11-17-parallel-model-weighted-support-fixed-plan.md)及[同额中断恢复](../notes/2026-11-17-parallel-model-second-interruption-recovery.md)。本条消费[R648](R648-continuous-Gram-on-the-complete-pulse-prefix.md)、[R651](R651-continuous-curvature-on-the-complete-pulse-prefix.md)与[R650](R650-positive-definite-flow-support-reach.md)的准确对象和条件，不改变它们的范围。
