# R792 后继：用已成四响应消费原 β 的准确表达式

日期：2026-11-15。状态：**本文是已有 R791(791R.16)、R792 与原
unit-chart 证明的源绑定消费接口，不把消根公式登记为新定理。**
新工作是把已经成功的四个 CM 响应接成可执行的准确表达式图，明确
其有限点、分母与原同源尺度，并划清后继需要的准确零判。
本接口不把模有理重构候选改称准确展开坐标。

来源：

- [R791 的实际原 Hom、切向与同源输入](../results/R791-certified-original-Hom-descent-and-eta-inputs.md)，
  尤其 (791R.3)–(791R.6)、(791R.8)、(791R.14)、(791R.16)。
- [R792 的原点、共轭方向与指定实嵌入](../results/R792-original-beta-composition-and-Galois-cube-root.md)，
  尤其 (792.2)–(792.7) 与 §8 的同源边界。
- [原 unit-chart 准确表达式](R787-original-unit-chart-exact-expressions-and-CM-value-consumer.md)，
  SHA-256 `8d5b58a5f6e9748805af3c032de1bae955543b1855535b6c51f0ca9cd6947820`。
- [四响应的执行接口](R787-implicit-CM-value-consumer-interface.md)。

本次四响应的原公开运行是 `43773420733`，source
`c3bcfc0dbbcd3a045349ec4500886100851a0d84`，核心 SHA-256
`d0e94bee98802169b9e1dfec186143deda7745bf2cdad420e683a75eb1969ddc`。
其实际最终证书 SHA-256 是
`5de210b5ebb2a8a7fefcc8799888a68353c9c2ac10725fafa239d2bd1082d20c`。
该运行证明原 $B_0$ 在全部十四个指定剩余域分支均为单位；
原 $518$ 位的 $y,y'$ 完成全部十四坐标乘回；准确展开标志仍为
`false`。后继按真实 manifest 和证书中的文件/SHA 读取，不凭本文
摘要构造缺失产物。全部新算术仍仅在本公开仓库 Actions 执行。

## 1. 准确四响应与模数值是两种不同对象

保持原 $f=f_4:X_1\to C/L$、$\deg f=1206$、$f(c_0)=O$，
$C:y^2=x^3+b$，$c_1=4424$，粗参数 $z=a-1$。记

$$
K=\mathbf Q(\zeta),\quad \zeta^2+\zeta+1=0,
\quad s=1+2\zeta,\quad F_b=\mathbf Q(b),\quad L=F_b(s).
$$

原 unit-chart 证明固定同一个 $2420\times2420$ 矩阵 $M$、右端
$r$ 和原 free direction $1186$。准确解 $\xi=M^{-1}r\in L^{2420}$
由原单位 minor 与全部关系核维数 $28$ 唯一确定；其对应原
$A/B$ 的全部 $129\times280$ 关系是该证明的结论。
四响应是如下准确域元素：

$$
A_j=\ell_{A_j}\xi,\qquad
B_j=c_{B_j}+\ell_{B_j}\xi,\qquad j=0,1.
\tag{DAG.1}
$$

这里 $\ell_{A_j}=(e_j,0)$，
$\ell_{B_j}=(0,(e_jZ)_{P_S})$，$c_{B_j}=(e_jZ)_{1186}$。
$e_0,e_1$ 来自同一原 $\mathcal L^5$ 基的准确 CM 值、粗一阶导数；
$Z$ 的原 pivot 行已经带负号，不再改变它。准确表达式叶子保留
这些来源、选行、free/pivot、原字段与线性响应，不把同名的模
$\ell^{518}$ 数组当成准确有理坐标。

可等价使用已定义的 bordered determinant

$$
\Delta(\ell,c)=
\det\begin{pmatrix}M&r\\-\ell&c\end{pmatrix}
=\det(M)(c+\ell M^{-1}r).
\tag{DAG.2}
$$

不需要物化 $M^{-1}$、伴随矩阵或 $2420$ 个展开系数。
本次证书的 $B_0$ 单位见证与 (DAG.1) 是同一个准确对象的约化。
因而 $B_0\ne0$，原 $y_0=A_0/B_0$ 有限，且

$$
y'_0=\frac{A_1B_0-A_0B_1}{B_0^2}.
\tag{DAG.3}
$$

这里只需要一个真实非零约化便能证明特征零非零；本次实际给了
全部十四个单位分支。这个论证不使用有理重构猜测。

## 2. 直接消费 R791(791R.16)，不重新取三次根

原已成切向记为

$$
h_0=\left.\frac{f^*(dx/(2y))}{dz}\right|_{c_1}\in L^\times.
\tag{DAG.4}
$$

准确读取 R791 第四号原切向；其已算零标志为 `false`，
`original_c1_slash_count=1`。不重新收缩十二组 Hom 微分，不再乘
一次 $\zeta^2$。原 R791(791R.16) 已经给出
$x_0=3(y_0^2-b)h_0/y'_0$。现在所需的分母非零全部有独立来源：

1. 本次 $B_0$ 单位见证给有限的原点 $f(c_1)$。
2. R792(792.3)–(792.7) 对这个原点给
   $y_0=sv_0$、$v_0\in F_b$，并在原指定实嵌入下
   $y_0^2-b=-3v_0^2-b<0$。故 $x_0\ne0$；不需要宣称 $F_b$
   的全部嵌入为实，也不需要展开 $v_0$。
3. 原微分恒等式 $dy=3x^2\,dx/(2y)$ 是正则微分恒等式，在
   $y_0=0$ 时也成立。结合原 $h_0\ne0$，有 $y'_0=3x_0^2h_0\ne0$。

因此设置

$$
Q=A_0^2-bB_0^2,\qquad N=A_1B_0-A_0B_1
\tag{DAG.5}
$$

时 $B_0,Q,N$ 全部非零。准确原点可用以下有限表达式图输出：

$$
\boxed{\beta_C=f_4(c_1)=
\left(\frac{3h_0Q}{N},\frac{A_0}{B_0}\right).}
\tag{DAG.6}
$$

这是把 (791R.16) 代入已经成功的四响应，新增的内容是其来源与
可消费表示。所得 $u_0=\zeta x_0$ 自动是 R792(792.6) 中唯一的
$F_b$ 立方根；本接口不运行 R792 的二十一次因式分解，也不另选
一个 CM 方向。由原曲线与微分身份还得到可供后继使用的准确关系

$$
N^3=27h_0^3Q^2B_0^2.
\tag{DAG.7}
$$

该身份的证明来源是原映射，不是有限精度检验；有限精度代回只能
另作模证书。

若共同局部帧改变使 $(A,B)$ 同乘一个局部单位 $\lambda(z)$，
则 $Q,N$ 同乘 $\lambda(0)^2$；$\lambda'(0)$ 两项在 $N$ 中抵消。
故 (DAG.6) 与同一原粗参数下的 R790 正则帧相容，不产生新的
尺度或相位。若 $A_0=B_0=0$，则本接口不能由第一 jet 得到
$y'_0$；那一支须原 R792 的共同零阶处理或更高准确 jets。
本次 $B_0\ne0$ 已排除该支，不能把模零误作准确共同零。

## 3. 原三次同源与实际下降点

只消费 R791 已证的 $\alpha_3=1-\zeta^2$、$\alpha_3^3=3s$，
不再计算其 Norm 或乘法常数。原 $f_R=[\alpha_3]f$ 的点为

$$
x_R=-\frac{\zeta x_0(y_0^2+3b)}{3(y_0^2-b)},\qquad
y_R=\frac{y_0(y_0^2-9b)}{3s(y_0^2-b)}.
\tag{DAG.8}
$$

代入 (DAG.5)–(DAG.6) 后可直接保存较短的表达式：

$$
\boxed{
x_R=-\frac{\zeta h_0(A_0^2+3bB_0^2)}{N},\qquad
y_R=\frac{A_0(A_0^2-9bB_0^2)}{3sB_0Q}.}
\tag{DAG.9}
$$

分母仅使用已经证明非零的 $s,B_0,Q,N$。原共轭关系保证
$x_R,y_R\in F_b$；不以一次模 Frobenius 检验代替此下降证明。
将这些原 $F_b$ 点及其实际运输共轭组合，得到 R728/R791 的
原 primitive Weil 模型中的 $q_R[c_1-c_0]=v\beta$。
其原极化尺度仍是

$$
\kappa v^\dagger v
=3870+711s_1-801s_2-360s_3+612s_4+864s_5.
\tag{DAG.10}
$$

不得设 $\kappa$ 或 $v^\dagger v$ 为一，不得把一个选定同源核
原像宣布为原抽象 $A$ 上的完整坐标。原 $c_0$ 已映 $O$，这里
不增添平移。点表达式也没有人为添加 Weil 限制中非 primitive
的第七个椭圆因子。

## 4. 最小表达式消费者与字段换基

新消费者用独立 `result/source/configuration`，仅有以下输入：

| 输入 | 实际用途 |
|---|---|
| 已成 CM 最终证书、源审计、准确表达式及值/jet 索引闭包 | 定义同一个 $M,r,e_j,e_jZ$ 和四个准确叶子 |
| 已成 A/B 模响应、$B_0$ 单位见证、原模商 | 保已有约化见证；不重做原 $518$ 位收缩、逆元或有理重构 |
| R791 原切向、Hom/下降与源证书 | 读 $h_0$、原共轭、三同源和 $\kappa v^\dagger v$，不重算这些对象 |
| 上述纸面证明的准确文件/SHA | 给每个逆元节点的非零理由和原点身份 |

字段保持原 $b$。若 DAG 数值适配器使用 $B_{\rm fld}=\lambda b$
及 $s$ 基，而切向源使用 $b^i$ 与 $\zeta b^i$，则只使用准确
同构

$$
\sum_{i=0}^6(a_i+d_i\zeta)b^i
=\sum_{i=0}^6\lambda^{-i}
\left(a_i-\frac{d_i}{2}+\frac{d_i}{2}s\right)B_{\rm fld}^i.
\tag{DAG.11}
$$

表达式本身可把这个同构保为一个有源节点，毋须重新生成旧切向。
整数公共分母、content 与 $246^3\kappa^n$ 的清除规范完全继承原
unit-chart；不往四响应或 $h_0$ 重新插入旧规范因子。

DAG 至少支持 `rational`、原字段生成元、`unit_chart_solve`、
`linear_response`、加/乘/负号、带非零证书的 `inverse`，以及
作用于全部输入的 `Galois`。节点内容寻址，源文件仍逐 SHA 绑定。
不会把一个文字形式的未定义符号当成可执行叶子：准确响应必须
带齐原矩阵/右端/选行的确定性 recipe、局部行及其源指针。
原大 $F,R_m$ 数据可由已有 source manifest 读取；若后继需要
准确零判，其实际输入闭包须再取得这些原数据，不能从不存在的
展开矩阵取值，也不能重算已经完成的原前缀。

首 scope 仅产生新的准确点 DAG、非零理由与来源审计。证书区分

```
exact_original_beta_C_as_expression_certified = true
exact_original_descent_point_as_expression_certified = true
expanded_coordinates_exactly_certified = false
original_abstract_A_coordinate_preimage_recovered = false
old_R792_expanded_coordinate_recipe_produced = false
actual_eta_or_height_computed = false
```

只有实际源齐全、$B_0$ 非零见证与原 R791 输入全部匹配后，前两项
才可为 `true`。后继绝不能把本输出塞入原 R792 数值成功入口，
应使用明确的 DAG 适配器。

## 5. 后继 β 加法真正需要的零判

R804 的八节点原 Hom 字已有准确身份；在 $c_1$ 上应用时，须把
全部系数按原 $\sigma,\rho$ 运输。原
$T=D_{\rho^{-1}}\sigma$ 对点的作用是

$$
T^j(x,y)=
\bigl(\rho_j^{-2}\sigma^j(x),\rho_j^{-3}\sigma^j(y)\bigr),
\qquad \rho_j=\prod_{a=0}^{j-1}\sigma^a(\rho),
\tag{DAG.12}
$$

并保持 $T^7=[\zeta^2]$，不是 $T^7=1$。$\sigma$ 必须作用于
$b$、$h_0$、四个响应的全部矩阵与局部行，不能只改最外层坐标。
原 R754/R791 的 $\sigma,\rho$ 来源已经完成；这里只消费。

非零 Hom 字不保证其在 $c_1$ 的点值非零。一般点加法的分支仍须
准确决定 $O$、$x_P-x_Q$、$y_P+y_Q$、$y_P$ 等是否为零。
合法实现可以用带已证非零 chart 的射影公式；如果 chart 尚未
证明非零，就保条件分支或执行准确零判。非零剩余域值能认证
非零；模零或任意有限精度零不能认证特征零相等。

准确零证可由实际 Hom 恒等式、已证共轭/曲线身份、对原
unit-chart 的准确 row-space/bordered-determinant 证书，或
最终准确的十四坐标展开获得。它不要求先展开全部 $2420$ 个
关系系数；但没有这些证据时，也不能仅凭 DAG 语法不同决定非零。
本首 scope 不执行八节点加法，不预填这些点碰撞结果。

## 6. η 与高度入口仍保留的原数据

准确 $\beta_C$ 点 DAG 已提供真实的代数点输入，但 $\eta_h$ 是
原 $Y$ 上完整除子/Picard 类，不能由几个点值恢复。R791
(791R.13b) 的极除子、Galois Norm 及 (791R.13d) 的刚性化主函数
必须经真实短 RR/理想消费者获得，原 $1/3$ 与三同源的抵消也只
在已证规范下使用。当前 R835/R838 后继的约化 $D$ 与短 RR 路线
提供相应全局来源，本 DAG 不重复或代替它们。

原高度还保留真实 $q,v,\kappa$、极化、Poincaré 帧与比较函数、
局部分裂、非 $p$ 项及原 Jacobian 点。一个准确代数点表达式
没有自动给出这些周期/高度，也没有证明原 $T_p$ 非零。

需要数值高度时，可以逐节点在指定 $p$ 进域求值。已证明非零的
分母不一定是 $p$ 单位；必须按实际估值自适应提高工作精度。
有限 DAG 和非零分母保证每次指定精度的求值可终止，但现有
$\ell^{518}$ 数据仅服务指定辅助素数，不能直接当原 $p$ 进高度。
若旧数值接口强制十四个准确有理系数，必须先另做准确展开/零证，
或写清楚消费表达式的新接口；不能把重构候选越过该边界。

## 7. 执行与保存边界

节点生成、旧字段同构、必要模求值及准确零证的新算术均仅在
本公开仓库 Actions。每个完成 stage 保同一来源身份并可续接，
不重做已成 CM jets、响应、原 Hom 或三同源常数。源码、参数、
纸面证明及简明 run/SHA 登记可入 Git；机器证书、坐标、DAG 数组
与全部可重算输出只在一日 active artifact/carrier 中传递。
本篇固定 $p=41$ 的实际接口不改变课题的全 $p$ 完成标准。
