# R120 补篇：固定目标径向分量的准确 source 敏感度

2026-11-13，newton_source。**已证明的准确恒等式及实际腰截面界。**

本篇保持当前 R33 候选 $F$ 不变。允许在选定迭代目标时，把原目标改为
$g_0+\phi(r)\,dr^2$；这是选择一个新的固定目标，不是每轮 Newton 任意重选目标。
它对真实标量源的影响有准确的一阶公式，无 $\phi''$ 项。
下面也给整个 $\eta=10^{-9}$ 参数盒、全部实角上的实际腰截面结果。

## 1. 两个真实敏感度系数

所有梯度、Hessian、收缩均用当前真实球面度量 $s$。
令 $\xi=dr$、$H=\nabla_s^2r$、$\tau=\operatorname{tr}_sH$、
$n=|dr|_s^2$，并置

$$
Z=\tau\,dr-H(\nabla_s r,\cdot),\qquad a=\rho^2.
$$

定义

$$
A=-\frac12\mathcal C_s(a\,dr^2),\qquad
B=-\frac a2\{\tau n-H(\nabla_s r,\nabla_s r)\}.
\tag{120S.1}
$$

则任意 $C^2$ 的径向函数 $\phi$ 满足准确恒等式

$$
\boxed{\quad q[g_0+\phi(r)dr^2]
       =q[g_0]+A\phi+B\phi'.\quad}
\tag{120S.2}
$$

这不是小扰动展开；只要新的目标仍为所要求的正度量，恒等式即完全成立。
原目标中 $E,E'$ 通过 $K_0$、连接及其他项出现的有理式必须合在一起，
最终响应确实线性。

证明：对任意对称张量 $T$，记 $Z_T=\operatorname{div}T-d\operatorname{tr}T$，
乘法公式给

$$
\mathcal C_s(hT)=h\mathcal C_sT+2\langle dh,Z_T\rangle
 +\nabla^2h:T-(\Delta h)\operatorname{tr}T.
$$

对于 $T=a\,dr^2$，
$Z_T=aZ+\langle da,dr\rangle dr-n\,da$，故
$\langle dr,Z_T\rangle=a(\tau n-H(\nabla r,\nabla r))$。
同时
$\nabla^2\phi=\phi''dr^2+\phi'H$；其中 $\phi''$ 项的两种收缩完全相同，
准确抵消。剩下的 $\phi'$ 系数为
$a(\tau n-H(\nabla r,\nabla r))$，乘上 $-1/2$ 即 (120S.2)。

## 2. 只用已有二阶几何的 $A$ 公式

把 R118 的平直目标恒等式用于标量函数 $r$，得到

$$
\mathcal C_s(dr^2)=\tau^2-|H|_s^2-2n.
$$

所以

$$
-2A=a(\tau^2-|H|_s^2-2n)
 +2\langle da,Z\rangle
 +\nabla^2a:(dr^2)-(\Delta a)n.
\tag{120S.3}
$$

在材料坐标中 $H_{ij}=-\Gamma_s{}^r_{ij}$、$n=s^{rr}$。
另外 $a=T^{-1}$、$a_i=-2t_i/T^2$，$t_i=F\cdot F_i$。
R117 source 入口已经计算了 $\Gamma_s,s^{-1}$ 及
$\nabla_s^2a$ 的完整有理表达式 `hf`；因此无需新的第三阶几何输入。
程序直接按 (120S.3) 形成一列，不用两个大 source 的有限差分估算它。

在腰部保持反射对称时，新的固定径向目标必须满足 $\phi'(0)=0$。
下面的选择和结论严格保留这一条件。
实际 $B(0,\theta)$ 的完整包络小于 $2.010\,10^{-10}$，包含其由腰反射给出的准确零值；
计算没有把这个小数误当作额外可选的 $E'$ 自由度。

## 3. 实际腰截面：小改 $E$ 不能消去当前的大源

新入口 `scripts/fourfold_phase_newton_target_sensitivity.py` 使用16384个
完整实角格及 R120 的完整 Fourier 余项。它给

$$
E(0)\in(1.229138831251,1.229138831255),\qquad
\|A(0,\cdot)\|_\infty<7.019911.
$$

直接在区间中令 $\phi(0)\in[-\varepsilon,\varepsilon]$、$\phi'(0)=0$，
完整表达式 $q+\phi A$ 给出以下**对所有这些改变同时成立**的下界：

| $\varepsilon$ | 任意允许改变后 $\|q_{\rm new}(0,\cdot)\|_\infty$ 的下界 |
|---:|---:|
| $10^{-6}$ | $0.608179$ |
| $10^{-4}$ | $0.607484$ |
| $10^{-3}$ | $0.601168$ |
| $10^{-2}$ | $0.557088$ |

这些下界直接来自某个连续角格上始终符号固定的完整区间。
没有用浮点求最小值来证明它们。

程序还用浮点 minimax 对区间中点作**候选选择**，再把选出的数冻结成确切dyadic：

$$
\phi(0)=-\frac{2407110556970143}{4611686018427387904},\qquad
\phi'(0)=0.
$$

新的腰部目标值大于1.228616872352，因而在该截面正定。
这个改变相对于原 $E$ 约 $4.247\,10^{-4}$。
对所选确切数重新用全部区间求值给

$$
\|q_{\rm new}(0,\cdot)\|_\infty<0.613653.
$$

原来同一16384格包络为0.617066；改进很有限。
浮点搜索不证明它是所有 $E$ 改变中的最优者，但上一张表的严格下界
已经说明很小的单个径向目标改动不能解决这个截面的 source 大小。
本篇不排除同时调整完整近似嵌入、另一目标分量或使用真正结构化强逆。

## 4. 与旧证书的边界

这里没有安装一个新的全局目标：只给了可能的新目标在腰处的值和零导数。
全局正度量延拓、整个径向的选择及误差必须另外证明。

R101 的真返回、类型固定、R111 的帽变分比较、R105 的低块以及相关
强逆输入都仍附着在原来的目标 $g_0$ 上。若以后安装新目标，
必须计算其引起的曲率、固定型别系数、返回和帽/核心算子的真实变化。
不能把本篇选出的 $E$ 值接上旧逆后宣称已得到一个新的 Newton 证书。

完整输出：`notes/2026-11-13-newton-target-waist-sensitivity-native.json`。
输入、origin、direction、参数分数及源码 SHA 均在该文件中；native运行14.66秒。

```sh
python scripts/fourfold_phase_newton_target_sensitivity.py \
  --out notes/2026-11-13-newton-target-waist-sensitivity-native.json
```
