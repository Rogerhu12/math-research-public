# R197 的强幅度材料逆映射：完整计算与全周两 jet 消费

状态：**已证明的 R197 直接应用，且本次强输入的 64 个严格 Taylor 区间已实际完成。**
这里不新增一个曲面存在性结论，也不重复小幅度的 32 格运行。完整物理中央曲线、单位切向和安全种子函数的全周两阶导数有明确区间消费者。主曲面全部度量误差、全局 reach、帽接合和强运动见证仍分别待付。

## 1. 准确输入与实际保存身份

本次两条原始轴是准确的 IEEE 二进制有理数：

$$
A=\frac{6134056590672823}{4503599627370496},\qquad
B=\frac{1265588444388213}{2251799813685248}.
$$

它们对应保存 bits $\mathtt{3ff5cae4581e83b7}$ 与
$\mathtt{3fe1fc2f16a36dd4}$，来自
`notes/2026-11-13-fd2d-R196-strong-gap08-branch-00.json`
（SHA256 `835c4e56d56aba1c41b571de05e9d0b4c7328189075fff23330fbaccb79f89a4`）。
此输入是当前强 gap 设计的固定中央轴；并不令 gap 成为运动时间。

周长平均半径 $a_E$ 直接消费已经完成的强归一化证书：

- `notes/2026-11-13-fd2d-metric-R197-strong-gap08-normalization-01-report.json`，
  23121 B，SHA256 `2f8e8dd37de88688e703d5213cc46ada4b575d576b7a15a8b29b3da1ce186550`，
  字段 `actual_result`。
- `notes/2026-11-13-fd2d-metric-R197-strong-gap08-normalization-01-input.json`，
  3153 B，SHA256 `97b88016327b8ddc05ed5c1cb91b646ae4b21fc5a99bcf76d40de86f832cc9c0`。
  此输入保存准确目标 $a_0$ 的有理端点字符串。
- $a_0$ 的原证书为
  `notes/2026-11-12-fd2d-balanced-moments-taylor-01.json`，
  SHA256 `0da13490030b82f536a921a97083b38f606ab604e7c7195c9053fb7975fa4b03`。
  本次使用已正确转录的整数字符串，不把大整数先转成 JavaScript Number。

本次没有重新计算那个 1.936 秒的强归一化运行，没有重新计算小 gap 的材料 chart，
也没有调用任何 F/J、normal、BVP 或 body 积分。

新准确请求为
`notes/2026-11-13-fd2d-R197-strong-material-chart-incremental-01-request.json`，
23931 B，SHA256 `0aa3647c06cc844b2f33d84a6215a6abba90d22da950c3d899fac45824817622`。
它含完整既有周长证书、准确 $a_0$ 身份、64 格、16 阶、160 位算术，以及前三格的当时真实观察。
后续完成报告另存，不改这个已经发布的请求。

## 2. 原准确问题与逐格余项证明

记 $Q=\pi/2$、$D=A^2-B^2$，并令

$$
\ell(\theta)=\sqrt{B^2+D\sin^2\theta},\qquad
a_E=\frac{2}{\pi}\int_0^{\pi/2}\ell(\theta)\,d\theta.
$$

准确材料角满足

$$
u=\frac1{a_E}\int_0^{\theta(u)}\ell(v)\,dv.
$$

因为 $A,B>0$，此式严格单调，唯一确定完整逆映射。用 $t=u/Q$ 和
$\nu=Qa_E$，原 R197 四通道系统是

$$
\theta_t=\nu v,\quad
s_t=\nu c v,\quad
c_t=-\nu s v,\quad
v_t=-\nu Dscv^4,
$$

其中 $s=\sin\theta,c=\cos\theta,v=1/\ell(\theta)$，且 $\theta(0)=0$。
这四个式子及阶乘归一化的 Taylor 卷积递推与原
`scripts/fd2d_R197_saved_ellipse_material_chart.cjs`
逐字保留；原源 SHA256 为
`3ccca82923ac0ed4cebcd66cc912944e41565d8e27567e0bd08f684a029ff79f`。

若左节点已有严格区间 $\Theta_j$，那么在该格上

$$
\theta(t)\in
\left[
\inf\Theta_j,\
\min\left\{Q_+,\ \sup\Theta_j+\frac{\nu_+}{\min(A,B)}(t_{j+1}-t_j)\right\}
\right].
$$

这只用了正向材料速度、$\ell\ge\min(A,B)$ 和准确第一象限范围。
在左节点盒上求 0 至 15 阶系数，在整个先验角盒上求第 16 阶系数，
Taylor 定理的余项于是覆盖**整格**。传到下一节点后重复此过程。
全部四通道的系数及整格余项都保存在实际 packet 中。查询格内点时消费原多项式和余项；
查询角区间时用已经证明的单调性，不把区间插值当作准确反解。

算术仍是
`scripts/fd2d_R188_exact_quarter_primitive.cjs`，
SHA256 `5c04a135eed859a6d6d583877e53681cdc1dddc6102c913152adfc1913a9f97e`：
约分 BigInt 有理运算及向外 160 位 dyadic 区间。没有替换 gcd、舍入模式或冻结数学源。

由周长定义与四分对称性，准确地有 $\theta(1)=Q$。
最后把实际传来的区间与已有的 $Q$ 包围相交，是消费这个独立准确恒等式，
不是调参、shooting 拟合或把未知端值强设为零。完成报告同时保存相交前后的实际区间。

## 3. 恢复执行与当前实际结果

新独立源
`scripts/fd2d_R197_resumable_saved_ellipse_chart.cjs`
为 17515 B，SHA256
`cebb8d2fdbfd9196cd46d392afa8579468c45d96fefb2d0db8c5fb111264898b`。

它只改变执行分段：

- 构造器默认不推进任何格；
- `advance(1)` 实际完成下一整格；
- `checkpointState()` 保存完整已成格及精确数学绑定；
- 重启核对源、参数、分区连续性、全部 row hash、端点及既有格；
- `portablePackets()` 在少一格时明确拒绝声称完整。

SHA 是传输与绑定工具，不替代上述区间证明，也不声称来源认证。
当前运行是 functions.exec 的真实 V8 数学调用，没有 OS 子进程或 shell exit。
64 格的实际耗时逐格保留；其和为 **342.409 秒**，不含发布和调用之间的墙钟间隔。
全部 64 格已完成，最大节点角宽为

$$
\frac{4615008511771471384857931439929609}
{1461501637330902918203684832716283019655932542976}
<3.158\times10^{-15}.
$$

这是本次完整节点列表的最大包围宽度，不是整张曲面的误差指标。
最终 $\pi/2$ 节点宽为
$5/730750818665451459101842416358141509827966271488$。

完整 portable 原始 JSON 为 **1840505 B**，
SHA256 `cefec4974db9096eb2f58fc9366835afca7e894c8090995d11edd8fd8e7f5216`。
完整可恢复 checkpoint 原始 JSON 为 **1873347 B**，
SHA256 `a1bf7fecdc3e0739b03329efc8886eecbaff2dca3c9843d909c2ac1f94b4275f`。
两者均按 `JSON.stringify`、末尾无换行计 hash。

当前大对象保存在实际运行的 store；这里**不声称已有磁盘 gzip 文件或远端数据文件**。
遵守 README §8，未通过 API 上传或拆分这些数组。下面的请求与生成入口足以逐字重生；
恢复终端后应保存 gzip，而不是在对话中传大数组。

## 4. 全周反射以及完整导数

取 $t=u/Q\in[0,4]$。在第 $q$ 个象限，令
$\varepsilon=(-1)^q$，并定义

$$
\xi=
\begin{cases}
t-q,&q=0,2,\\
q+1-t,&q=1,3,
\end{cases}
\qquad
m=
\begin{cases}
q,&q=0,2,\\
q+1,&q=1,3.
\end{cases}
$$

若 $\theta_q$ 是已证第一象限函数，则

$$
\Theta(t)=mQ+\varepsilon\theta_q(\xi).
$$

设

$$
D_0=\operatorname{diag}(1,1),\quad
D_1=\operatorname{diag}(-1,1),\quad
D_2=\operatorname{diag}(-1,-1),\quad
D_3=\operatorname{diag}(1,-1).
$$

准确物理中央曲线是

$$
\Gamma(u)=\frac{a_0}{a_E}(A\cos\Theta(u),B\sin\Theta(u)).
$$

它在每象限等于 $D_q\Gamma_q(Q\xi)$，所以

$$
\Gamma_u=\varepsilon D_q(\Gamma_q)_u,\qquad
\Gamma_{uu}=D_q(\Gamma_q)_{uu},\qquad
\Gamma_{uuu}=\varepsilon D_q(\Gamma_q)_{uuu}.
$$

由弧长定义直接得到 $|\Gamma_u|=a_0$；这里准确归一化改变了有限 seed 的代表，
不能宣称旧 finite provider 的数值两 jet 逐字不变。R193 仍须支付 finite-to-accurate 的实际传播预算。

记单位切向 $T=\Gamma_u/a_0$，则

$$
T=\frac{(-A\sin\Theta,B\cos\Theta)}{\ell(\Theta)},\qquad
\beta=\frac{a_EAB}{\ell^3},\qquad
\beta_u=-\frac{3a_E^2ABD\sin\Theta\cos\Theta}{\ell^6},
$$

$$
T_u=\beta JT,\qquad T_{uu}=\beta_uJT-\beta^2T.
$$

反射下 $T\mapsto\varepsilon D_qT$、$T_u\mapsto D_qT_u$、
$T_{uu}\mapsto\varepsilon D_qT_{uu}$，而
$\beta\mapsto\beta,\ \beta_u\mapsto\varepsilon\beta_u$。
这些是物理 $u$ 导数，不是 $\xi$ 导数，也不是未乘阶乘的 Taylor 系数。
$\Theta_u>0$ 在全周由
$\Theta_u=a_E/\ell\ge a_E/\max(A,B)>0$ 严格保证。

R197 的安全种子令 $e_u=(-\sin u,\cos u)$，
$\cos\delta=e_u\cdot T,\ \sin\delta=\det(e_u,T)$，并取正的
$c_{1/2}=\sqrt{(1+\cos\delta)/2}$。完整象限几何保证
$c_{1/2}^2\ge1/2$，故没有 atan 分支或分母退化。于是

$$
h=\frac{\sin\delta}{c_{1/2}}=2\sin(\delta/2),\qquad
h_u=c_{1/2}(\beta-1),\qquad
h_{uu}=-\frac h4(\beta-1)^2+c_{1/2}\beta_u.
$$

反射下 $h\mapsto\varepsilon h,\ h_u\mapsto h_u,\ h_{uu}\mapsto\varepsilon h_{uu}$。
完整曲线、切向与种子在四象限交界和 $0,2\pi$ 上按这些式子匹配。
这给 256 个全周严格区间及 257 个闭合节点的定义；不需要重新积分四次。

## 5. 可直接调用的两 jet 消费者

新源
`scripts/fd2d_R197_full_circle_material_consumer.cjs`，
6175 B，SHA256
`3676715bea0c5e49001d73754e6152f30118c94e9d76c2c19b1fe622f2fb7d4e`。

调用：

```js
const whole = createR197FullCircleMaterialConsumer(chart, {
  exact_interval: request.chart_spec.target_mean_radius_identity.exact_interval,
  identity: request.chart_spec.target_mean_radius_identity
});
const point = whole.point(["1", "3"]);
const box = whole.box(["63", "64"], ["65", "64"]);
```

输入是准确 $t=u/Q$ 的有理字符串/整数对，范围 $[0,4]$。
构造器只接受真正完成的 quarter。跨象限查询显式分片再取区间包络。
输出含 $\Theta,\Theta_u,\Theta_{uu}$、准确归一化和物理曲线到三阶、
单位切向到二阶、$\beta,\beta_u$、物理中央曲率和 $h,h_u,h_{uu}$。

唯一的小消费实际运行 **141.060 秒**，9 个点（四个相互反射点和全部象限端点）
加一个跨象限盒。所有预定反射等式、周期两 jet、单位速率恒等式的区间包含、
切向正交恒等式包含和材料导数正性均通过。没有有限差分替代导数，没有新 F/J。

该次点查询的物理 $\Gamma_{uu}$ 最大包围宽为约
$4.309\times10^{-15}$，$h_{uu}$ 为约 $1.731\times10^{-14}$。
这些明确是**该次点查询**的宽度，不把它们冒作全曲面连续误差界。
整盒能力来自第 2 节的整格余项和本节精确反射，不来自这 9 个采样点。

## 6. 终端重生和续算

`scripts/fd2d-R197-strong-material-chart-run.cjs` 是另名 Node 重生入口，
语法已在 V8 编译，当前无执行环境，**未声称 Node CLI 已实际运行**。
它使用上述已经实际运行的核，逐格写一份当前 gzip checkpoint，不打印大数组。

从本题目录运行：

```sh
node scripts/fd2d-R197-strong-material-chart-run.cjs \
  --request notes/2026-11-13-fd2d-R197-strong-material-chart-incremental-01-request.json \
  --out-prefix notes/2026-11-13-fd2d-R197-strong-material-chart-node-replay01 \
  --expected-report notes/2026-11-13-fd2d-R197-strong-complete-material-chart-01-report.json
```

可加 `--cell-limit 4` 做自然短批；下一次以同请求、同 prefix 加
`--resume <prefix>-checkpoint.json.gz` 只续未成格。
输出 owner 核对请求与数学 binding；检查点和 portable 原始 JSON 的 hash 可与本次 V8 输出比较。
CLI 自己记录真实 Node 版本、时间与实际完成状态，不借用本次 V8 的耗时或不存在的 shell exit。
checkpoint 内的 `OS_process_created:false` 指纯构造器不创建子进程；
Node 宿主身份由重生报告另记，外部退出仍由真实执行工具记录。

## 7. 结论的准确范围

强原始轴、准确目标 $a_0$、原周长定义均未改变。这里已经补齐：

1. 强中央椭圆完整材料角逆映射的整格严格 packet；
2. 明确物理材料坐标的全周曲线/切向/种子两 jet 消费；
3. 实际可恢复执行记录、生成源、准确输入与完整大数据 hash。

它可供 R193 的连续误差预算消费。它不支付剩余物理 profile、全径向/全角完整位置积分、
全域度量误差、强 Newton 存在性、全闭核 reach 或所有时刻的强见证。
既有强 gap 与中央曲率准确证书继续独立适用；本次没有把有限输出误差改名成精确解。
