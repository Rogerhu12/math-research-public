# R44 实际圆弧半径的首负 K 保护窗：R40 的单调推论

状态：**已证明的局部参数推论；本次只核保存初猜的有理参数，没有重算积分或求解。**
新 trace 空间允许弧上控制不为零，不能直接套用 R40 的 $q$ 区间。
正确输入是 R44 的实际半径 $R=1+8q+t$。以下证明只使用这个半径和原经线 ramp。

## 1. 参数化结论

取 R40 的同一个 outward flat ramp，$v=9/20$、$\varepsilon=2/5$、
$\eta=1/20$。也可把这三个数换成 R40 §5 已分别验证的实际 binary64 精确实数；
两种约定各自固定，不在一次推论内混用。
设

$$
\delta\ge\frac3{50},\qquad R\ge\frac{164}{125},\qquad 0<Rv<1. \tag{1}
$$

若核在法向角 $|\phi-\pi/3|<21/100$ 上是半径 $R$ 的精确圆弧，
则 R5 首负 K 加速段的特征损耗满足

$$
\boxed{\frac{\chi(L)}R>0.2108827779904414>\frac{21}{100}.} \tag{2}
$$

这里 $L=\varepsilon\delta/[v(1-\varepsilon)]$ 是该加速段长度。
在所有 R5 正则性、旋转度量与完整 Cauchy 数据假设满足时，(2) 意味着已知圆弧
数据的保证保护锥在该段结束前已耗尽。它不证明外部圆弧实际消失，也不证明完整解存在。

## 2. 证明及对 R44 的应用

沿用 [R40](../results/R40-small-q-actual-flat-ramp-characteristic-window.md)
式 (4) 的同一 $F,P,d$，置

$$
B=\frac{\delta\varepsilon}{1-\varepsilon},\qquad y=Rv.
$$

R40 式 (6) 的恒等式对任何 $R>0$、$0\le y<1$ 都成立：

$$
\frac{\chi(L)}R=J(B,y)
=\int_0^1\sqrt{\frac{B\,d(z)}{(1+BP(z))(1-y^2F(z)^2)}}\,dz. \tag{3}
$$

它不使用 $R=1+8q$ 这一特殊参数化。在同一 ramp 下，$P,d,F\ge0$，
$F\le1$，并且

$$
\frac{\partial}{\partial B}\frac{B}{1+BP}=\frac1{(1+BP)^2}>0,
\qquad \frac1{1-y^2F^2}\text{ 随 }y\ge0\text{ 非减}.
$$

所以 (1) 使 $J(B,y)$ 至少为 R40 已证参考点
$R_-=164/125=1+8(39/1000)$、$\delta_-=3/50$ 的值。
该参考点的完整 2000 段有理下和，分别在十进制有理参数及实际 binary64 参数两种
约定下，都已经严格大于 (2) 中所写下界。本条引用该证明，不重新计算同一下和。
条件 $Rv<1$ 保证 (3) 全段的分母严格为正；R40 原先的半径上端只用于保证这一点，
不是单调下界的必要上端。

在 R44 新空间中，弧上支撑扰动为

$$
b=t+(u-t)\cos(\phi-\pi/3).
$$

因此 $b+b''=t$，精确半径是 $R=1+8q+t$；$u-t$ 只平移圆心。
同一偶/C3 与低均值约定保持材料中心 $u_{\rm mat}(\pi/3)=\pi/3$，
保护弧的材料半宽为 $R(21/100)$。故 (2) 比较的正是
$\chi(L)>R(21/100)$，不把法向角与材料长度混为一谈。证毕。

## 3. 已保存 q060→R44 初猜的参数核对

输入是已经完成的 `q060_circle_trace_initializer_terminal.json`，
SHA-256 为 `8c478f12c2472a3df75017613e606adf801282a7d5f413aec48e14705bc5aa75`。
这是初猜诊断记录，不是新的已接受 BVP checkpoint。

从完整八参数与七尺度逐项相乘读取全部实际控制，而非从诊断半径读取，得到

$$
q=0.05210565550627671,\quad t=0.04377938275497506,
\quad R=\frac{26312274100032071}{18014398509481984}.
$$

前两个小数标识实际 binary64 数；记录保存其精确有理表示。
原最终 frozen profile 的 $\delta=0.06104275721220832$，新初猜 $p_0=0$；
没有把旧历史 $p_0$ 再加一次。三个 ramp 参数的精确 binary64 实数逐项等于 R40
已验证分支。精确有理交叉相乘核得

$$
R\ge164/125,\qquad\delta\ge3/50,\qquad Rv<1
\quad(Rv\approx0.6572810820623349).
$$

由此该保存初猜通过 (2) 的局部门，不需调用新 core 或反函数。
后续 BVP 会自由改变 $t$、$u$ 和 $\delta$；其最终参数必须重新核对 (1)，
不能把本条初猜结论直接搬到未来终态。

## 4. 复现与边界

只读参数核对源为
`scripts/resume_closed/bind_trace_arc_ramp_window.py`。使用新输出路径运行：

```bash
python topics/visible-flex-held-10pct/scripts/resume_closed/bind_trace_arc_ramp_window.py --out /tmp/trace-arc-ramp-binding.json
```

它检查完整来源、七控制乘法、R40 已登记下界的来源身份和 (1) 的有理比较；
不导入 core，不调用原积分、不运行 collocation、Jacobian、BVP 或新尾。
紧凑执行记录为 `scripts/resume_closed/trace_arc_ramp_binding.json`。

本条不支付 R38 的握持比例、全曲面直径、reach、活动矩、同 $g$ 等距或闭合，
也不把局部保护锥耗尽当作不存在障碍已被完全解决。

本次参数核对工具记录为 `7487a2`，真实退出码 0，六项有理门全部通过。
输出 SHA-256 为 `4dad9c57c3d5f6e06fdb3ab156e12a482bb23ce5931a74dd69feb09c4f996bc8`；
该退出只记录新参数绑定，不冒称重跑了旧 R40 下和。
