# R150：一般等权剩余原权点的完整 824 次 QQ 覆盖

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。

## 1. 完整原覆盖

在[一般等权全图六生成元](R150-appendix-unit211-equal-weights-global-original-six-generator-module.md)及[剩余原权点有限性](R150-appendix-unit211-equal-weights-finite-original-weight-and-Gram-locus.md)的准确余图上，令 $C,D\in\mathbb Q[m,Q]$ 为两条[完整原常数列余子式](R150-appendix-unit211-equal-weights-two-original-parameter-cofactor-curves.md)。原解必同时满足 $C=D=0$，且

$$
m(m-1)(2m-1)Q(Q-1)(2m+3Q-4)(2m+Q-2)\ne0.
$$

本附录实际计算固定 49 阶 Sylvester 行列式

$$
R(m)=\operatorname{Res}_{Q}^{(24,25)}(C,D).
$$

它是完整有理系数多项式，不是模素数投影或参数抽样。实际次数为 824，非零项数 691。完整因式乘回给出

$$
R(m)=\gamma\,m^{134}(m-1)^{132}(2m-1)^{78}
(2m+1)F_{236}(m)F_{243}(m),\qquad\gamma\in\mathbb Q^\times.
$$

这里 $F_{236},F_{243}$ 是源码确定的 primitive 整系数因子，各有 237、244 项。只去掉此前已整支排除的 $m=0,1,1/2$，得到所有剩余原解都必须满足的完整覆盖

$$
(2m+1)F_{236}(m)F_{243}(m)=0. \tag{1}
$$

**这三个整因子仍须回原系统。** 本附录不把任何因子当作仅有实根、不选某个复嵌入，也不由必要覆盖直接宣称一般等权为空。

## 2. 首项与全部退化点

源码先从 C、D 实际提取 Q 的最高次系数并逐项乘回：

$$
[Q^{24}]C=\frac1{128}m^2(m-1)^2,
$$

$$
[Q^{25}]D=\frac1{512}m(m-1)^2(48m^3-43m^2+2m+11).
$$

因此 C 在整个允许权图上保持 Q 次数 24；D 的新三次首项因子没有被倒置。计算始终使用符号次数 $(24,25)$ 的固定 Sylvester 行列式。

任何有限同一点 $Q_0$ 上若 $C(m_0,Q_0)=D(m_0,Q_0)=0$，评价向量给相应 Sylvester 映射的非零余核，所以 $R(m_0)=0$。这包括 D 首项为零或次数进一步下降的全部纤维。可能由无穷远引入的额外因子也保留在 (1)，没有以泛型次数假设删掉。

剥除函数每次只除原单位的 gcd，并将商乘回。由于 gcd 的有理规范可选择首一因子，式中只用非零有理常数 $\gamma$ 表示规范差异；不把原单位 $2m-1$ 与其首一版本混作相同常数。

## 3. 精确对象的再生身份

C、D 的定义来自同一原 Gram 的十条六列必要行和全六列 cofactor 乘回。此次源重新生成它们是为了新的完整投影，不是重跑被冻结的旧 QQ Gröbner 门。

完整 824 次 R 的 FLINT 字符串 SHA256：

a8f2c81f180ced8a0bde6ddde577f01079f577224713a10cbf33da1520352dc5

仅剥已付单位后的 480 次多项式 SHA256：

569b8dd33e9861a01b5fe6b904e43b9723b82a283304a7d8056115952162e78a

其完整因式分解的有理 content 是 $-1/34359738368$，三个 primitive 因子身份为：

| 因子 | 次数 | 非零项数 | FLINT 字符串 SHA256 |
|---|---:|---:|---|
| $2m+1$ | 1 | 2 | 87c60beab86fa3f724ddd83b293083412e1fbcf3a2041fbe62b0605f39cf311f |
| $F_{236}$ | 236 | 237 | 146f2143cefe99e4a96b2ae729ba7b4bdc30bd7d30a181d18de1991736befe8a |
| $F_{243}$ | 243 | 244 | 1c2c3bd08d2428ded39b6ee27cf26d783ec0617dd547ec54347c22be17ca1d89 |

完整因子乘积、已付单位剥除和两条首项的乘积均实际核回。源码是精确数学对象的可再生定义；不保存可重算的大系数表。

## 4. 实际执行

自含源：[完整 Q 结式](../notes/2026-11-27-unit211-equal-weight-complete-Q-resultant-8542.py)。

- 源 SHA256：4f3a8529999a42f0b8cd295d027ba154290b3450def1ae2c27ea2a9969df35c2。
- Git blob：0b2d5d182623cb78b903e662b43b89f6ba6f2973。
- Python 3.12.14、python-flint 0.9.0、单线程；180 秒与 4 GiB 边界。
- 首次实际 run 45948417062 / job 140338362302。
- 完整因式乘回于 6.815188603 秒结束；驱动耗时 6.880572798 秒，最大子进程 RSS 58220 KiB，退出码 0。
- stdout 19485 字节，SHA256：48a523df5193c98e0a7b347c5fc0ae60641ef36317b67022fc5eeb3ef3a7cbdf。
- 实际 pull：2026-11-27 05:53:11.548372 UTC，提交 db6548ecb23214eb1dde28b2a4dc378c73a286ab；两 README blob 均无变化。

[实际小回执](../notes/2026-11-27-unit211-equal-weight-complete-Q-resultant-execution-8542.json)保存运行身份与各阶段摘要。结式运算使用 [python-flint 0.9.0 的官方 resultant API](https://python-flint.readthedocs.io/en/latest/fmpq_mpoly.html)，没有使用数值近似。

下一项数学工作为 (1) 三个整因子的原同点返回，尤其保原四二次、NS/PS、Dval 非零及所有原主元零纤维。普通 ISP 的完成状态不变。
