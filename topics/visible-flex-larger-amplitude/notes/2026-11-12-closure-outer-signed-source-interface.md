# 原实际 outer11 候选：逐位置完整有符号非线性源

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-12。

## 已完成的对象

[记录器](../computations/closure_outer_candidate_source_record.py) 已对
cell11 全5545个原真实 material 面板完成执行。它没有改候选、没有
重算背景积分，也没有执行 ODE；原 `tail_outer_candidate_defect.py`
的唯一变化是一个只读结果回调。全部原聚合数学字段逐字复现，只有
运行时间/RSS 两项被明确排除在逐字比较之外。

[完整 summary](2026-11-12-closure-outer-source-cell11-r1-summary.json)
列出九个已完成 gzip、原输入 SHA、源码 SHA、全部7个已通过的门。
[wait4 resource](2026-11-12-closure-outer-source-cell11-r1-resource.json)
记录真实 child exitcode 0、signal null、55.554621 s、峰34,632 KiB；
session96084 又由工具正式 poll 确认退出0。

每个面板保存原位置 $x_-,x_+$、真实 $r,r_x,w,w_x/w$、完整源
$\|N_\perp\|_{\sigma,1}$，以及 $m=2,4$ 的有符号完整 cosine 系数区间。
所有原20个模式均参与计算，完整 mean 根和乘法逆生成的无限高频
没有删去。条带仍为原 $\sigma=1/64$。

**这里的候选仍是原 R48 加权高度候选。** 它使用原保存的 binary
$Q/L$ 和真实五正积分；并未实施 R67 的可选 cut-jet 重设。
若后来真的改变候选，非线性源需对改变后的高度另算，不能把本包
静默转用到新候选。

## 完整有符号源包围的证明

在固定真实面板上使用

$$
P=\frac{h_\theta}{rw},\quad K=\frac{h_{\perp,r}}w,
\quad T=P_\theta,\quad U=K_\theta-P,
\quad E=1+w^2,\quad s=\frac{r_x}r,\quad\ell=\frac{w_x}w.
$$

所有范数都是同一个 Wiener $\mathcal A_{\sigma,1}$ 范数。
权 $(1+|m|)e^{\sigma|m|}$ 次乘性保证该范数的乘法常数为1。
原候选域已支付 $R=\|P\|_1+\|K\|_1<1/32$，故完整 mean 小根 $c$
满足 $|c|\le c_*:=4R^2$。

完整非线性 source-$x$ 方程为

$$
K_x=-\ell(2K+T)+N_\perp,
$$

$$
N=\frac{Q+\Delta Q}{1+c+K+ET},
$$

其中二次多项式

$$
Q=EsU^2+\ell\big[(K+T)^2+w^2(2KT+T^2-P^2)\big],
$$

而**所有 mean 影响**恰是

$$
\Delta Q=\ell\,[2c(K+T)+c^2+2w^2cT].
$$

原 helper 已给正的 leading Wiener 门。设

$$
L_*=c_*+\|K+ET\|_1<1.
$$

分别有可计算正界

$$
Q_* = E s\|U\|_1^2
 +|\ell|\big[(\|K\|_1+\|T\|_1)^2
 +w^2(2\|K\|_1\|T\|_1+\|T\|_1^2+\|P\|_1^2)\big],
$$

$$
\Delta_* = |\ell|\,[2c_*(\|K\|_1+\|T\|_1)
 +c_*^2+2w^2c_*\|T\|_1].
$$

这里 $E,s,|\ell|,w^2$ 全用该原面板的真实区间，没有取另一个位置的
源极值。几何级数的完整逆给

$$
\boxed{\|N-Q\|_1\le
 \frac{\Delta_*+L_*Q_*}{1-L_*}.}
$$

这包含完整 mean 和点态分母的全部高次项，未将 $N$ 替换成有限
Galerkin 乘法。实际候选为实偶函数，故 $Q$ 的实 cosine 系数可由
完整 signed Fourier 字典作有限卷积准确包围。对 $m=2,4$，若
$Q_m^{\cos}$ 为所得区间，则

$$
N_m^{\cos}\in Q_m^{\cos}
 +\left[-\frac{\Delta_*+L_*Q_*}{(1-L_*)(1+m)e^{\sigma m}},
          \frac{\Delta_*+L_*Q_*}{(1-L_*)(1+m)e^{\sigma m}}\right].
$$

该区间还与原完整 $\|N_\perp\|_1$ 给出的同一系数包围相交。
实际除法使用**真实解析权的严格下界**；不能拿原输入范数计算中
向上舍入的权作为更大的除数。对实 cosine 的两 signed 模态，
其质量之和正好是 cosine 振幅，没有额外漏掉或重复一个2。

## 回调和原数学身份

入口锁定以下三件原源码，均没有修改：

| 文件 | SHA256 |
|---|---|
| `tail_outer_candidate_defect.py` | `241104402884d7988df2af8d3881c889cfc4e3d70486de6b3ef6ab76645a45bf` |
| `tail_outer_full_mean_residual_bounds.py` | `16f9d2d5c2e858686aff9d332df4cc565606481ab45a46d6a9080db29317c8af` |
| `tail_outer_candidate_domain.py` | `17d6b7d85be80f8f40b3eec411ae49a73c51c6b624d030df57b94202a7d08690` |

每次回调先调用原完整 helper，再只读计算上面的两个有符号系数，最后
原样返回原 helper 的对象。独立 material 迭代器逐条核对原 segment/
panel 索引和全部输入 hash。每个完整 segment 关闭压缩文件并保存 SHA，
所以中断不会丢失已经完整的源分组。

原 `physical_nonmean_second_source_W1` 是物理**残差**
$(w/r_x)R_K$ 的上界；它与这里的非线性项 $N_\perp$ 不是同一量。
两个字段原样分开保留。后续背景 Green 功能若消费 $N_\perp$，在
R67 的固定 global μ11 gauge 中应乘

$$
(r/r_c)^{m^2-4}\frac{r^4w^2}{\sqrt{12}\mu_{11}}
$$

进入 $v_x$。完整外残差还必须按 R67 的变参数恒等式合并候选线性项。

## 续作入口与未付范围

本包已支付真实源的逐位置区间，尚未计算其带符号、有序 Green 积分。
下一步将从外端高度功能向内推进真实 adjoint 列，与这些同位置源盒
相乘并积分；每个面板的前后方向及径向 source 单位都保持不变。
只有付完这一项，才可把 R67 的整段线性中心数与完整候选非线性源
放入同一个实际参数预算。

本包没有给出外0..11的全频逆、全幅度闭合或整面 reach 声明。
