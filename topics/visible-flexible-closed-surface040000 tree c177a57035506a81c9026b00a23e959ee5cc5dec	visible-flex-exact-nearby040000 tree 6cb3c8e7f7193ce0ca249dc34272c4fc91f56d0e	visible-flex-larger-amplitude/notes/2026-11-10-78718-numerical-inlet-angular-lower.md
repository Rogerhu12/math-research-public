# 实际 finite prefix 入口的角向误差下界及其对所有后续接合的保持

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / numerical_recovery。

**结论：已证明的有限图局部下界。** 本文直接读取已经生成的 M14 mirror
prefix 的定义性 nodal jets，得到
$$
\left\|g_*^{-1/2}(F^*e-g_*)g_*^{-1/2}\right\|_{\rm op}
>1.3311420566797905\times10^{-8}>2\times10^{-9}
\tag{1}
$$
在入口的一个点成立。此下界不需要先算尾、桥根或全域区间上界；在保持
该入口与指定目标度量的每个 common-cut 延伸中都成立。它给新候选一个
快速的必要条件检查，不增加原题的完成条件，也不代替已有的全域检查。

这里的对象是**实际保存的 finite Cartesian prefix**，不是从 CP 中取出的
原未投影 round background。故其数值与 geometric_closure 的 CP 入口
$G$ 下界略有不同；两者定义分明，未被写成同一个数。

## 1. 定义性输入

本次实际输入目录为
`notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/`。

| 文件 | SHA-256 |
|---|---|
| `prefix-base.json` | `11cd5569b3c2218591a757aea966f9aa25963fa1a3ec69fbb0b6729cb141a42d` |
| `prefix-target.json` | `dbfb5c348a6921b078c1ee25c9aa5874856de303afd11b1e6277ac1eebdbbd8c` |

完整实际数据容器及每件无损分片都由 reader 重组并核对 logical SHA；在
终端内读数组，不把数组放入报告或对话。原 geometry 的源码是
`78718-prefix-fullxyz-hermite-storage-v1.py` 与
`78718-prefix-mirror-hermite-storage-v1.py`。目标源码是
`78718-prefix-metric-supplier-storage-v1.py::Target`，其 exact clamped
spline 使用有理数解，flat profile 从保存的 binary 参数按精确有理公式定义。

程序逐件核13份源码、9项输入（去重后）；其中包括 geometry、target、原
CP/port 和实际 storage 闭包。这是输入值对应关系，不是要求任何人先做
独立审查才能使用本结论。

## 2. 完整角向点公式

按原 finite shared-jet map 的圆柱基，入口水平曲线是
$$
F(0,\psi)=R(\psi)e_r(\psi)+T(\psi)e_\theta(\psi),
$$
其中
$$
R=r_0+\sum_{j=1}^{M}r_j\cos(3j\psi),\qquad
T=\sum_{j=1}^{M}t_j\sin(3j\psi).
\tag{2}
$$
所有 $r_j,t_j$ 是实际 `jets[0,0,:]` 的 binary64 数，解释为准确有理数。
高度系数在入口按原 mirror 定义准确为0。由于
$e_r'=e_\theta$、$e_\theta'=-e_r$，
$$
F_\psi=(R_\psi-T)e_r+(R+T_\psi)e_\theta.
\tag{3}
$$
不能删掉这里的 $R$ 项，它来自圆柱基自身的旋转。

在 $\psi=0,\pi/3$ 取 $\sigma=1,-1$，所有正弦准确为零，故
$$
F_\psi(0,\psi)=L_\sigma e_\theta,\qquad
L_\sigma=r_0+\sum_{j=1}^{M}\sigma^j(r_j+3j t_j).
\tag{4}
$$
无需浮点 $\pi$ 或三角函数；$|e_\theta|=1$ 是准确几何恒等式。

原 exact flat target 在 $s=0$ 有 $a(0)=1$。目标 angular spline 的首值
准确为1，cutoff在0准确为1，因此原固定 angular chart 满足
$$
\Theta(0,\psi)=\psi-\frac{8q_{\rm ref}}3\sin3\psi,
\qquad
\rho_\sigma=\Theta_\psi(0,\psi)=1-8\sigma q_{\rm ref}>0.
\tag{5}
$$
$q_{\rm ref}$ 也是从实际 geometry 保存值解释出的准确 binary 有理数。
程序核首 spline 节点和值、flat profile、$0<q_{\rm ref}<1/8$，并核 target
绑定的是同一 geometry 和源码家族。

沿向量 $v=\partial_\psi$，相对 metric 误差的 Rayleigh 商为
$$
\Gamma_\sigma
=\frac{(F^*e-g)(v,v)}{g(v,v)}
=\frac{L_\sigma^2}{\rho_\sigma^2}-1.
\tag{6}
$$
因而相对误差算子范数至少为 $|\Gamma_\sigma|$。此结论即使其它方向有
交叉项也成立，只需 $g$ 正定。程序对(4)–(6)仅做 `Fraction` 的有限次
加、乘、除，得到准确分数；不从 sampled 最大值推断连续下界。

## 3. 为何不需要桥根或全域尾

最终的径向重新参数化为 $\sigma_r=\lambda s$，$\lambda>0$。取新的图
$F_*(s,\psi)=F_0(\lambda s,\psi)$，在 $s=0$ 有
$$
\partial_\psi F_*(0,\psi)=\partial_\psi F_0(0,\psi).
\tag{7}
$$
原 exact bridge 只修正末端的径向桥参数，主体 flat profile 的入口依然是
$a_*(0)=1$。相同 angular chart 在重新参数化后仍有(5)的入口值。
因此(6)对最终 exact target 的入口完全不变，**不出现径向导数下界中
必要的 $\lambda^2$ 因子**。这与已有 R81 的径向轴点论证是两个不同方向
的 Rayleigh 商，彼此不冲突。

原 common-cut 的源码
`78718-prefix-common-cut-storage-v1.py::install` 将校正只加在
`correction_start_index` 及其以后的径向区间。对当前数据、原 width=.15，
该索引准确为6124，大于0；校正因此在入口附近恒为零。任意尾 endpoint
误差、末端模式扩充或 correction 系数不会改变(4)。mirror 也只更改入口
高度 jet 的奇偶性，保存的水平零阶 jet 不变。

故凡是继续使用这张 base prefix、原 common-cut 支撑规则、正径向尺度、
相同入口 target 的延伸，都有同一个角向下界。**不需要假设那个延伸已经
构造成功或是闭嵌入**，这个必要条件已经阻止它满足原 $2\times10^{-9}$。
这不是对其他 prefix、其他求解结果或精确无限解的不可能性论证。

## 4. 真实计算和可直接使用的命令

脚本 `scripts/78718-prefix-inlet-angular-lower-v1.py` 为12,292 B，SHA-256
`8d62095b36b383bbbbf9d7f94be4d1488b5011c1da63dace781d5012e78a3277`。
在 repo 根实际执行：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
 topics/visible-flexible-closed-surface/scripts/78718-prefix-inlet-angular-lower-v1.py \
 --geometry topics/visible-flexible-closed-surface/notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base.json \
 --target topics/visible-flexible-closed-surface/notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-target.json \
 --out topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-inlet-angular-lower-01.json
```

真实工具 **39ef67 自然 exit0**，约0.247秒。报告14,305 B，SHA-256
`aebc6fe0c746f1455f2166389a8b49f038ea7444d7b5d8cc2ef7f19efa114e99`。
完整实际 argv/工具回执保存在
`2026-11-10-78718-numerical-inlet-angular-lower-observed-01.json`。
零 BVP、零 DN、零 ODE、零 producer。

最坏的两个已查轴点中，$\psi=0$ 给(1)。随后的实际有理比较
**d463c5 exit0** 验证显示用的十进有理数
`0.000000013311420566797905` 严格小于报告的准确分数，且准确分数严格
大于 `1/500000000`。这回不把 binary64 最短十进字符串自动当作向下端点。
$\psi=\pi/3$ 的绝对误差准确小于
`0.000000000050877930892846`，该轴自身未超过预算。

今后新的实际 M15（或更大 M）prefix 和 target 一旦生成，直接把同一命令
的两个输入换成该新对象、输出换为未使用路径即可。它兼容原单容器和已用
无损 storage 两种表示；若入口两轴都小，不代表全图通过，还需按原计划
继续全域检查。本文没有计算任何新 M15 候选，也没有改动其当前运行入口。
