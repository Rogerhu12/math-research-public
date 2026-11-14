# 独立审查：正则切口的平均斜率与完整二阶接口

2026-11-09，Astra-visible-flex-950f9f73 / independent_audit。
审查者未参与宏观前缀或本引理的构造。

**结论：PASS，限于原文假设下的精确条件引理。** 审查对象是
`2026-11-09-950f-prefix-cut-mean-uniqueness.md`；冻结文件哈希及
独立有理算术核验写在 `2026-11-09-950f-audit-cut-mean.json`。

## 独立推导

从正定水平投影与所选 inward 分支出发，令
$L^2=a^2-v^2$，则水平经向系数为 $-uv/L$ 和 $a\sqrt Q/L$。
比较 $F_{\theta s}^{xy}=F_{s\theta}^{xy}$ 的切向分量时，
$u_\theta v$ 两项精确抵消，其余项给出

$$a\alpha/L=-a^2uw/L^3-(a\sqrt Q/L)\phi_\theta.$$

因此原文的切向转角公式符号及 $a,L$ 因子正确。对平均斜率
$c$ 求导后，用 $u=c+u_0$ 与 $Q+u^2=L^2/a^2$，分子恒等式为

$$\frac{aw}{L^2}Q+u\left(\alpha+\frac{auw}{L^2}\right)
=\frac wa+\alpha u.$$

这独立重现原文的 $\mathcal H'(c)$。条件 $u\ge u_{\min}>0$、
$\alpha<0$、$\|w\|_\infty/a<(-\alpha)u_{\min}$ 使分子的负值
有统一正下界 $\eta$；因为 $0<Q\le1$，确有
$\mathcal H'(c)\ge\eta>0$。所选区间内的转数条件
$\mathcal H(c)=1$ 至多有一个解。定量不等式是均值定理的直接结果，
并不需要给出解的存在性。

同一度量的 Christoffel 符号为
$\Gamma^s_{\theta\theta}=-a\alpha$、
$\Gamma^\theta_{s\theta}=\alpha/a$，Gaussian 曲率为 $-a''/a$。
代入高度 Darboux 恒等式后恰为

$$z_{ss}(w+a\alpha u)-(u_\theta-\alpha v/a)^2=-aa''Q.$$

分母 $w+a\alpha u\le-a\eta<0$，故二阶高度 jet 的商式正确。
由于 $Q>0$，R6 所需的水平角速度 $T=L>0$ 和水平法向经向
分量 $b=a\sqrt Q/L>0$ 都满足，且两侧分支一致。因此在原文
已假设两侧都是精确等距浸入时，匹配高度迹与非恒定斜率会先
匹配平均斜率，再匹配完整高度二阶 jet，最后可使用 R6 作单次
水平刚体对齐，得到 Cartesian 二阶接口。

## 有理算术核验

独立脚本 `scripts/950f-audit-cut-mean.py` 从保存的 M12 trace
binary64 数字的精确分数构成 Fourier 三角不等式，而非再次采用
原作者显示的上界。所得

- $\|z_\theta\|_\infty\le0.003925296165132$；
- $\|z_{\theta\theta}\|_\infty\le0.012132742008387$；
- $\|u_0\|_\infty\le0.012456261350808$；
- 保存的平均斜率 $0.4473363144188365\ldots\in[0.4,0.5]$。

原文的粗域由精确分数核得
$Q>0.7295$、$\eta>0.306$、$w+a\alpha u<-0.1838$。
还额外核查了一个包含保存的 binary64 半径与 $E$ 的小有理区间，
在该区间中三个粗界仍成立；因此打印的 $a=0.6$、$E=1.25$
与实际保存数字的末位差异不会影响此域检查。

## 采用范围

这是一项补足 R6 假设的局部工具，可以采用；它不能从采样度量
残差推出精确等距，不能把任意高度数据积分成浸入，也没有证明
无限尾。当前 trace 域检查只对所保存的有限 Fourier 多项式有效。
每次非线性耦合改变 trace 后必须重新检查该域。

定量平均差界要求比较同一个高度迹和同一个 $u_0$ 的两个
$\mathcal H(c)$。若实际数值比较的非恒定迹也有误差，还须计入
这些误差对 $\mathcal H$ 的影响。近似 Cartesian 二阶接口仍需要
直接重放，或 R6 所述的 C1 度量缺陷控制与明确常数。
