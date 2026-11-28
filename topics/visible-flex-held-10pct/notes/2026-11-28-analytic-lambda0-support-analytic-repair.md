# R87 原 lambda-zero 支持列：真实小步噪声、完整解析三 jet 与独立接线

**可信度：固定材料三jet公式由完整链式法则证明；误差大小为数值证据，未证明非线性收敛。**

本记录接真实 R87 严格恢复的 `lambda000_m8`，不重做旧 q=.06 输入。
数值诊断唯一锚是原第 9 次组 J 前保存的 **765 点未接受完整状态**，
SHA `e13909bf4981deae02e0024de06e58c3923f37815cb704085e63ce7257ee01c1`。
它不是已接受 BVP。此后旧求解器又产生的 812 点交接状态属于另一个真实
后继输入；这里没有把 765 点诊断冒作对 812 点的重复检查。

## 实际原因及改变范围

`material_support_factory.make_factory` 在 lambda=0 返回原
`PlanarSupportCore`，不带正 lambda 的 `jet_parameter_derivatives` 属性。
原 portable 的实际分支因而进入 `exact_core_lift` 的完整参数差分，
V5 的正 lambda 解析安装器此时根本不调用。此前独立 delta 诊断已确认这一点；
本次不补造该属性，也不把 lambda=0 改标为正 lambda。

真实 7 个支持参数尺度为

```
[0.000144, 0.000001728, 0.000000020736,
 0.000000001, 0.000000001, 0.000000001, 0.000000001]
```

这次原归一参数差分步均为 `2e-5`，最后四个物理系数步只有
`2.0000000000000003e-14`。完整 RHS 中需要相消的量仍是普通浮点量，
不能把这些微小步的结果当成可靠解析列。真实七点比较中，原各支持列
L2 约为 `3e-9` 至 `8.2e-9`；新公式对应的完整列在不同模式下仅
`2.5e-12` 至 `1.52e-9`。这给出了具体差分污染证据，
没有证明它是旧阻尼很小的唯一原因。

新入口只将支持控制列换成以下完整解析导数。原加性 delta 差分、完整
RHS、状态列、边界、定义域、网格加密、所有物理门均不改变。

## 同一原核心的完整固定材料导数

令 $m_j=3(j+1)$，原支持函数与材料弧长为

$$
h(\phi)=1+\sum_j c_j\cos(m_j\phi),\qquad
u=\phi+\sum_j\frac{1-m_j^2}{m_j}c_j\sin(m_j\phi),
\qquad \rho=h+h_{\phi\phi}>0.
$$

写 $e_r=(\cos\phi,\sin\phi,0)$、
$e_t=(-\sin\phi,\cos\phi,0)$，则原表示满足

$$
\Gamma=h e_r+h_\phi e_t,\qquad
\Gamma_u=e_t,\qquad \Gamma_{uu}=-e_r/\rho.
$$

对每一个物理支持系数 $c_j$，固定同一个材料坐标 $u$，令

$$
\sigma_j=\frac{1-m_j^2}{m_j}\sin(m_j\phi),\qquad
\dot\phi_j=-\sigma_j/\rho,\qquad
\dot\rho_j=(1-m_j^2)\cos(m_j\phi)+\rho_\phi\dot\phi_j.
$$

链式法则给出全部三个导数：

$$
\begin{aligned}
\partial_{c_j}\Gamma
 &=\cos(m_j\phi)e_r-\frac{\sin(m_j\phi)}{m_j}e_t,\\
\partial_{c_j}\Gamma_u&=-e_r\dot\phi_j,\\
\partial_{c_j}\Gamma_{uu}
 &=-\frac{e_t\dot\phi_j}{\rho}
   +\frac{e_r\dot\rho_j}{\rho^2}.
\end{aligned}
$$

第一式还直接复用原类的 `parameter_derivatives`，不另造位置导数。
三式覆盖全部实际系数及全部实际角节点，未删任何高模式。
它们不是固定法角导数：$\dot\phi_j$ 正是材料坐标变化的必要项。

`planar_support_exact_parameter_jets.py` 将这三个完整数组交给已经存在的
`analytic_adaptive_core_jac.install`。该安装器继续支付原角坐标复合、
参数尺度、完整 reference lift、初值投影相减、状态 Jacobian、
`frame_jvp` 及 convection 项。支持列以原 `pscale` 运输；
delta 列仍用原同一中央差分。

## 已执行检查，及其精确限制

第一项实际运行在原 765 点中取真实索引
`[0,127,255,382,509,637,764]`，保留每点全部 25 个状态分量和全部 8 列。
未重组完整 collocation J，未调用 BVP/native。真实报告
`r87-real-support-columns-20261128-a/comparison.json`
SHA `60d130f64b8502b8915c1bbbb292f92a08abae0b31a3224b1b11420ff7c56ab3`，
耗时 `9.70861531699984 s`、峰 `78892 KiB`；工具实际终态为 exit 0。
其中全部状态列、原 delta 列及最后恢复的完整 RHS **逐位相等**。

第二项真实检查在同一原核心的 **256 个实际角节点** 上，对全部 8 个
物理系数和全部三个 jet 作中央差分，物理步为
`1e-6,3e-7,1e-7`，共 72 组完整数组比较。
真实完整报告 SHA
`3a3b52a1d4afb9157261ae15d180f9ab0ddb2c39ae560c5c700ad0c7895d09d7`；
记录实际耗时 `5.276420863000112 s`、峰 `73268 KiB`。
原核心及完整 RHS 均逐位恢复。

在 `h=1e-7` 上，各阶跨全部 8 系数的最大相对 L2 差分别为

| jet | 最大相对 L2 差 | 最大绝对差 |
| --- | ---: | ---: |
| $\partial_c\Gamma$ | `2.6618363612518046e-9` | `7.095560722314431e-9` |
| $\partial_c\Gamma_u$ | `1.3662791351755814e-9` | `5.1057956085287515e-8` |
| $\partial_c\Gamma_{uu}$ | `3.971776841571462e-9` | `3.1196299232760794e-6` |

这些是有明显信号的核心三 jet 检查。与之不同，完整 RHS 的前两支持列
本身只有约 `2.87e-11` 和 `9.73e-12`，相消很强。另用
`1e-4,3e-5,1e-5` 物理步作窄核时，大步截断误差按约 $h^2$ 缩小，
第一列最后绝对差 `2.4731182153174002e-12`，第二列最后绝对差
`2.0682324335157653e-10`。本记录**不**将这两列说成高相对精度 FD
验证通过，也不拿它们的相对误差冒作三 jet 公式错误。全部实际值在小 JSON
中保留；完整原非线性验收仍是下一次实际求解的门。

没有连续区间导数证书、非线性收敛证明或完成声明。

## 独立实际入口

`analytic/zero_planar_support_analytic_driver.py` 是新的独立 base-driver，
原 hash-bound driver 不改。现有 QR3 命令只需将 `--base-driver` 指到它，
其余真实初猜、profile、chart、port、容差和完整检查点合同保持。
它在原 `exact_core_lift` 返回后，以预先捕获的**原**解析安装器设置支持列，
因此不会误触 V5 的正 lambda delta hook。入口明确拒绝非零 lambda、
其他核心工厂和非线性尾请求。自有全局 hook 在 `finally` 恢复。

实际安装及所有来源写入输出目录的
`zero-planar-support-analytic-execution.json`，没有重贴原 `run.json` 身份。
注意下层旧 V5 sidecar 的通用 scope 文本仍提及正 lambda delta；
本入口记录实际 lambda-zero 分支及空的正 lambda 安装路径。

新 driver 实际 `py_compile` 和 `--help` 均成功（工具 `19c173`）；
此记录冻结时未在该 driver 执行 BVP。已交给设计代理在核清旧进程退出后
使用它保存的**最新真实 812 点**继续，不能退回本诊断的 765 点或初始网格。

四个新源码的准确 SHA 及全部实际报告绑定见同名 JSON。大型/可重算数组
仅在 scratch，不进入仓库。
