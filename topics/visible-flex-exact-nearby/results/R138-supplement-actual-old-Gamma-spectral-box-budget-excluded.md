# R138 补篇：原 Gamma 下的谱闭行预算仍不能过第一门

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

**结论。** [RS 实际完整单积分](../notes/radial_weight_root_budget_screen_ci/run-44758362539-1/radial-weight-root-budget-screen.json)
的保存整球给 $T<125$。若继续使用原 X 的整个 `Gamma` 接收因子，同时把原体
$C_E$ 只换成下面的同闭行谱上界算法，则第一吸收门仍不可能通过。
这是一个由已有完整球和有理不等式组成的解析排除；没有执行新谱常数目标，
也不值得为这一特定组合再运行全域谱 consumer。

## 1. 被排除的准确新预算

使用[互补 Gram 谱比较](R138-supplement-complementary-Gram-spectral-body-energy.md)
的符号。每原闭行以完整已存 upper/lower 形成

$$
\overline M=1+U^2+K_+V^2,\quad
\underline\kappa=K_-v_-^2,\quad t_-=\gamma_-m_-,\quad t_+=\gamma_+m_+,
$$
$$
C_i=\max_{t\in\{t_-,t_+\}}
\frac{\overline M(t+t^{-1})+
 |t-t^{-1}|\sqrt{\overline M^2-4\underline\kappa}}
 {2(2/5)v_-}.
\tag{SE.1}
$$

全域新常数按 $C_{\rm sp}\ge\max_iC_i$ 选取，或将该新完整 upper 与原已存
$C_E^{old}$ 取较小者。原 $2/5$ 是本算法继续使用的固定 support lower。
这些量是所选预算数值，不等于真实函数的最优范数。

## 2. 一个原闭行已经足够

原完整 positive native SHA
`ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d`
的零基 `rows[1000]` 为

$$
\left[\frac{2578398747599831}{9007199254740992},
      \frac{1289624518295989}{4503599627370496}\right].
\tag{SE.2}
$$

原完整容器由[原四件 index](../notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json)
确定。直接读取该行的完整已存数值，以下宽有理比较成立：

| 本算法输入 | 原字段 | 对该所选数值的比较 |
|---|---|---|
| $U$ | `bounds.U_A0` 的 upper，并加同 repair | $U>1/2$ |
| $V$ | `bounds.V_A0` 的 upper，并加同 repair | $V>8/5$ |
| $K_+$ | `intrinsic.K` 的 upper | $K_+>3/5$ |
| $v_-$ | `bounds.real_physical_inverse_gap` 的 lower，并减同 repair | $v_-<5/8$ |

这些不是对真实 $|u|,|v|,K$ 作下界。它们只比较已经选择的 upper/lower **预算数值**。
特别地，并未宣称这个 box 的全部极值在同一角点实现。

因为 $t+t^{-1}\ge2$ 且根号项非负，(SE.1)必有

$$
C_i\ge\frac{\overline M}{(2/5)v_-}
>4\left(1+\frac14+\frac35\frac{64}{25}\right)
=\frac{1393}{125}>11.
\tag{SE.3}
$$

原 X 的所选 $C_E^{old}>32$，所以与它取 minimum 也不会把新预算降到11以下。
无需扫描其他4650行或求新的全域 maximum，已经知道本算法将产生 $C_{\rm sp}>11$。

## 3. 与原 Gamma 的根必要费用相加

原已成整球给以下有理放宽：

$$
\Gamma>59/50,\quad A_\Theta>12/5,\quad
E_0>69/50000,\quad E_1>27/10,\quad h_E>93/50000.
\tag{SE.4}
$$

$\Gamma,A_\Theta$ 为 X 的已选值；$E_0,E_1,h_E$ 为 Y 的已选值。
其原 source/mean/实际对象不变。谱改进后原 GB 的体系数仍必须按

$$
w_{E,\rm sp}=\frac52\Gamma\sqrt{A_\Theta}
   (\sqrt{C_{\rm sp}}+\sqrt{C_H}h_E),\qquad
a_{EE,\rm sp}=E_0w_{E,\rm sp}^2+E_1w_{E,\rm sp}h_E
\tag{SE.5}
$$

构造。仅删除正项并用 $\sqrt{12/5}>3/2$、$\sqrt{11}>33/10$，就有

$$
w_{E,\rm sp}>\frac{177}{40}\sqrt{11}>\frac{73}{5},
\qquad
a_{EE,\rm sp}>
\frac{69}{50000}\left(\frac{73}{5}\right)^2
 +\frac{27}{10}\frac{93}{50000}\frac{73}{5}
=\frac{918705}{2500000}.
\tag{SE.6}
$$

[RS.19](R138-supplement-radial-weight-independent-root-budget-screen.md)
针对完整 $D_H^{-1}$ 的必要性仍保留。实际整球 $T<125$ 给

$$
\alpha_E(W)^2>
\frac{148(59/50)^2}{125}=
\frac{4121504}{2500000}.
\tag{SE.7}
$$

所以第一吸收门的左端已经严格大于

$$
a_{EE,\rm sp}+\alpha_E(W)^2>
\frac{5040209}{2500000}>2.
\tag{SE.8}
$$

其余 mean、source 和低根交叉预算均为非负，不能改善这一门。
不用形成新的 finite Gram、全高 Schur、根容量 ODE或谱预算科学结果。

## 4. 本排除明确留下的范围

本结论只排(SE.1)的闭行 box 算法、固定 support lower $2/5$ 和原整个
$\Gamma$ 根接收因子的组合。它不授真实谱函数的下界，也不排更紧的实际
角相关包络、改进 support、根锚定 drift 的不同转授、联合根/体有符号估计，
或原直接逆构造。尤其改为真正从根启动的 drift 后，根密度不再支付旧
$\sqrt\Gamma$；那是必须独立证明的新坐标比较，不能在本预算中免费删除。
原 BVP 是否有核、其有界逆、全局连接和非线性可见闭族均不由本排除决定。
