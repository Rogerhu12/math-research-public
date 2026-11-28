# 新输入：正确 B 曲线剩余 F34/F40 的完整常数域原值返回

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

**尚未执行。** 同一小源分别接受环境参数
`ISP_B_FACTOR_DEGREE=34` 或 `ISP_B_FACTOR_DEGREE=40`。
两项是两个不同的完整原常数纤维，各只首次执行，总预算分别为 $120$ 秒、$1$ GiB，外层驱动 $135$ 秒。默认参数 $34$；每条回执必须保实际参数，不能把一个因子的返回移给另一个。

源 SHA-256：a44a8fc4ca4842d97c4d94215250e8399f5988407c3971bdc68ffe96b3b77a48。
建议 basename：
2026-11-28-unit211-Phi-zero-true-Bzero-large-constant-original-fiber-8542.py。

## 1. 已付范围与真正新目标

沿用[全正确 B 原 I6 十二乘二呈示](../results/R150-appendix-unit211-Phi-zero-true-Bzero-whole-original-I6-twelve-by-two.md)。原权是

$$
u=\frac{(x+1)^2}{3x},\qquad
Q=\frac{4(x^2-x+1)}3,\qquad
\ell=\frac{(x+1)(5x-1)}{6x^2}.
$$

已付纯权支持为
$x(x^2-x+1)(x+1)(2x-1)(5x-1)(7x^2-4x+1)(23x^2-11x+2)$。
整个最后二次因子已独立原排除，未逆旧选头 $H_3$。

[终端一次 $C_{76}$ 原覆盖](../results/R150-appendix-unit211-Phi-zero-true-Bzero-terminal-C76-original-ideal-cover.md)已经证明
$C_{76}\sim(2x^2+4x-1)F_{34}F_{40}$，三个有理不可约因子均一次。
[整个二次原纤维](../results/R150-appendix-unit211-Phi-zero-true-Bzero-terminal-quadratic-complete-original-exclusion.md)已经排除，因此只剩 $F_{34}$ 与 $F_{40}$，目前不同权对上界为 $74$。

本次不重算二次纤维。对所指定 $\phi=F_{34}$ 或 $F_{40}$，
直接进入完整常数域 $K_\phi=\mathbb Q[x]/(\phi_{\rm monic})$；
保其所有复嵌入。所有使用的常数逆都以真实多项式 xgcd 和完整 $K_\phi$ 乘回取得，不把一个数值根当作整个纤维。

## 2. 输入获取只再生既有终端分母定义

三个准确依赖为：

1. 2026-11-28-unit211-Phi-zero-true-Bzero-whole-I6-twelve-by-two-8542.py，
   全源 SHA-256
   b802d6c9b7a46b544f1fd5f814b05337a552f938a660b8d047fe4e62ff4eae56。
   只取 newValues=[];quotients=[] 之前的原定义前缀；
   前缀长度 10370 字节，SHA-256
   44f288f6b65f5c59e99daae0de10b56e94ba13ec8b9307f3c70c71953eece6e0。
   它给原四式、真实可逆坐标、首一 $q_\omega$ 和四条一次余式，
   以及尚未换基的完整 NS/PS 定义；
   不执行旧十二行、旧三余子式或其尾部分类。

2. 2026-11-28-unit211-Phi-zero-true-Bzero-terminal-original-multiplier-cancellation-8542.py，
   全源 SHA-256
   73d4dd4167d48b5a5878338bdfe85dc6c59a194b97fa2ae23309e2c2226eac35。
   **不执行此完整源。** 仅截取
   `R=env['R'];ctx=env['ctx'];up,Qp,Lp,Tp,zp=ctx.gens()`
   至
   `scaled=[[R(cover)*a for a in beta] for beta in final]`
   之前的终端分母参数定义，复用第 1 项已经构造的 env。
   删除旧完整四乘子 check 循环，并以 AST 将这个参数片段内
   旧 assert 和旧 say 改为空操作；原文件字节不变。
   因此只计算定义所需的七行有理递推、实际系数、首一短除与最终分母，
   不执行旧两列/四乘子原身份验证，不计算旧 C315 LCM，
   不重跑旧 C76 理想证明或分类作为新门。
   常数因式分解只为取得所需精确参数，不输出系数载荷。

3. 2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py，
   全源 SHA-256
   5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。
   由第 1 项仅读取有理算术类的必要前缀；不运行四头旧计算。

既有参数身份逐项以已刊 SHA 锁定：

| 参数 | 精确多项式 SHA-256 |
|---|---|
| $C_{76}$ | 5eb0b13c682928e24c8449fa7dbbfa7a890fd72438897a4ae98de523ae778242 |
| $F_{34}$ | b593d2770a0337dcaf2f4908e51cfc9feb3c5890ce21e5c3c6c1707ff98187ff |
| $F_{40}$ | ba88a205beb579a18de711c9fd61514716099afeed94954736246cedf733a16a |

任何身份不符即停止，不替换输入。没有把旧源删断言后的计算当成新证明；
它的唯一用途是恢复已证明、已哈希指定的参数。

## 3. 新常数域的原首一 lambda 关系

完整 I4 在所选常数域中已有

$$
q_\omega=\omega^2+q_1(\lambda)\omega+q_0(\lambda),\qquad
\ell_i=a_i(\lambda)+b_i(\lambda)\omega,\quad i=0,1,2,3.
$$

由原可逆坐标逐式重新返回这四条原式在该**新常数纤维**的两个坐标。
然后只算六个真正新 $K_\phi[\lambda]$ 余子式

$$
c_{ij}=a_ib_j-b_ia_j
=b_j\ell_i-b_i\ell_j.
\tag{1}
$$

完整 Euclid/Bézout 组合给首一 $g(\lambda)$，并最终返回

$$
g=\sum_{i=0}^3\Gamma_i(\lambda)\ell_i
\tag{2}
$$

的全部两个坐标。每一步的多项式短除和原组合都乘回。
所除首项仅为完整 $K_\phi$ 的非零元素，故保 $\phi$ 全部嵌入；
没有倒原几何量或把临时 lambda 首项零删去。

若 $g=1$，已得到整个所选原纤维的单位。
若所有 $c_{ij}=0$，保整因子，不宣称有 lambda 有限模型。
只有实际 $1\le\deg g=n$ 时才继续下面一步。

## 4. 完整原 NS/PS 与真正有限商

使用

$$
A_\phi=K_\phi[\lambda,\omega]/(g,q_\omega),
\qquad \dim_{\mathbb Q}A_\phi=2n\deg\phi.
\tag{3}
$$

首一性支付 (3) 的全部基
$x^a\lambda^b\omega^c$。所有 lambda 和 omega 重数保留，
不假设原 I6 商自由或约化。

仅在这个新有限代数中，将完整原 NS、PS 通过真实
$f(\lambda,\omega),t(\lambda,\omega)$ 返回；每一次乘法先按
$q_\omega$、$g$ 约化。这样不重新计算旧两变量 NS/PS 余行。

六条原行与 (3) 的全部基倍数组成一个真正的原理想矩阵。
RREF 只选择原列，随后实际核选中方阵双逆、
全部原列的返回及目标的全部坐标。
因此实际返回 $1$，或某个

$$
(\lambda\,t\,D_{\rm val})^j,\qquad
D_{\rm val}=\ell(2\lambda^2-2\lambda+1)-T^2
=bc(h_U-k_U)^2,
\tag{4}
$$

就给出完整原理想身份。
这里只使用当前正确 $\Phi$、$D_{\rm val}\ne0$ 图上已付
$\lambda,t,D_{\rm val}$ 的物理非零性；它们在程序中均没有取逆，
其范数也没有取逆。

依次尝试 $j=0,\ldots,\dim_{\mathbb Q}A_\phi$，
只有实际完整成员返回才能排除所选整个权因子。
不因函数域 gcd、某个矩阵秩、或目标可能幂零而先宣排空。
若没有返回，保整个因子与实际余商维数；不重选常数根或改素数。

## 5. 资源、范围和交付

两次运行各自独立 $120$ 秒 / $1$ GiB；所有必要前缀的 alarm
都钳到本源最初绝对截止。新参数和每个完整数学阶段都输出小回执。
不输出或保存大系数、矩阵、编码载荷或分片。

本次没有模素数到特征零提升。若其中一个因子闭合，
只减少该因子的范围；另一个必须取得自己的实际结果。
两个原纤维全闭后才能与既有二次结论合成整个 B 原图排除。
不预先写整个 B、整个 Phi 或普通 ISP 成功。
