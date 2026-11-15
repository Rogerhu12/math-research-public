# R792：原 β 的准确合成、共轭选根与二十一次有理因式分解

日期：2026-11-15。状态：**下述原坐标合成、唯一选根和有限算法已证明；R787、R790 的实际完成产物及其合成运行须另行登记。本篇没有预填原 β 的数值。**

保持 R759/R764 的第 4 号原映射
$f=f_4:X_1\to C$、次数 $1206$、$f(c_0)=O$，目标仍是
$C/L:y^2=x^3+b$，并保留原 $c_1=4424$ 和粗参数 $z=a-1$。
本篇只消费已认证的原函数关系、同一模形式基的 CM 值和 R791 的
真实 Galois 作用；不重算周期、整数格、原 cusp Laurent 递推或 Eisenstein 基。

## 1. 区分三个字段和两个点

记

$$
K=\mathbf Q(\zeta),\quad \zeta^2+\zeta+1=0,
\quad \varsigma=1+2\zeta=\sqrt{-3},
\quad F_b=\mathbf Q(b),\quad L=F_b(\zeta).
\tag{792.1}
$$

原 R735 模型给 $[F_b:\mathbf Q]=7$、$[L:K]=7$。
这里 $F_b$ 使用原指定实嵌入；R725 §4 证明该嵌入下 $b>0$。
本篇不需要把 $F_b$ 的全部嵌入宣布为实嵌入。
$F_b$ 也不是 R791 中原 primitive 因子的六次实 CM 子域
$F=\mathbf Q(\zeta_{42})^+$。

本篇直接求的是

$$
\beta_C=f_4(c_1)=f_4(c_1)-f_4(c_0)\in C(L).
\tag{792.2}
$$

R764 已准确证明所选原参考 cusp 归一的映射就是该 $f_4$，其原
$c_0$ 平移为零。R787 的原 $y=A/B$ 因而无需再加三挠平移。
R732 §8 与 R791 将 (792.2) 送到原有理 primitive 模型；那个比较
包含实际同源 $v$，不能把 $\beta_C$ 的坐标未经比较直接写成原
$A_{\theta,1}$ 上的坐标。

## 2. 原共轭关系唯一选择 x 的 CM 方向

R791 的成功 run43686308194 已准确给出

$$
c(f_4)=-[\zeta^2]f_4,
\qquad f_R=f_4+c(f_4)=[1-\zeta^2]f_4.
\tag{792.3}
$$

这里 $c$ 固定 $b$，将 $\zeta$ 送到 $\zeta^2$；它作用于原函数
的全部系数。原 $c_1\in X_1(\mathbf Q)$。若
$\beta_C=(x_0,y_0)$ 有限，则由 (792.3) 得

$$
c(y_0)=-y_0,\qquad c(x_0)=\zeta^2x_0.
\tag{792.4}
$$

因此存在唯一的 $u_0,v_0\in F_b$ 使

$$
y_0=\varsigma v_0,\qquad x_0=\zeta^2u_0,
\qquad u_0^3=y_0^2-b=-3v_0^2-b.
\tag{792.5}
$$

**定理 792.1（原有限 y 加真实共轭输入确定整个点）。**
一旦得到准确的有限原 $y_0$，方程

$$
u^3=y_0^2-b,\qquad u\in F_b
\tag{792.6}
$$

恰有一个解；原点准确为 $(\zeta^2u,y_0)$。

**证明。** 存在性来自已经认证的原映射及 (792.4)：取
$u=\zeta x_0$，则 $c(u)=\zeta^2\zeta^2x_0=\zeta x_0=u$。
若两个非零解 $u,u'$ 在 $F_b$，则 $u'/u\in\mu_3$。
但 $F_b$ 在原嵌入下属于 $\mathbf R$，故不含非平凡三次单位根；
也可由 $[F_b:\mathbf Q]=7$ 排除二次子域 $K$。
所以两个解相同。零值时也只有零解。$\square$

本定理没有任取 $x^3=y_0^2-b$ 的三个根之一。
选根数据是已经完成的 (792.3)。R790 中“单独的 $y$ 不固定三个
CM 方向”仍然正确；本篇增加了一个真实的全局 Galois 输入。

在原指定实嵌入中，$v_0$ 为实数，故

$$
w:=y_0^2-b=-3v_0^2-b<0.
\tag{792.7}
$$

所以本原有限点中 $u_0,x_0$ 均非零。没有 $y_0^2=b$ 的例外支路。
这里的符号只用于证明非零，不需要在计算中作浮点实根选择。

## 3. 取根只需 Q 上最高二十一次分解

以下算法在 $F_b$ 中恢复 (792.6)，不要求通用数域多项式分解库。
写 $P_b(B)$ 为原 R735 的七次首一不可约多项式，用
$1,b,\ldots,b^6$ 表示 $F_b$。令 $M_w$ 为乘以 $w$ 的 $7\times7$
有理矩阵，定义

$$
H_w(T)=\det(TI-M_w),\qquad
N_w(X)=H_w(X^3)=\operatorname{Norm}_{F_b/\mathbf Q}(X^3-w).
\tag{792.8}
$$

**定理 792.2（唯一奇数次数因子）。** 假定 $w\ne0$，且已知
$w=u^3$ 对某个 $u\in F_b$ 成立。$N_w$ 在 $\mathbf Q[X]$ 的
准确不可约分解恰有一个奇数次数因子 $q(X)$。

1. 若 $u\in\mathbf Q$，因子次数/重数为 $(1,7)$、$(2,7)$，且
   $q=X-u$。
2. 若 $u\notin\mathbf Q$，因子次数/重数为 $(7,1)$、$(14,1)$，
   且 $q$ 是 $u$ 的首一最小多项式。

在两种情形中，准确有

$$
\gcd_{F_b[X]}\bigl(q(X),X^3-w\bigr)=X-u.
\tag{792.9}
$$

**证明。** 若 $u\in\mathbf Q^\times$，则
$N_w=(X^3-u^3)^7=(X-u)^7(X^2+uX+u^2)^7$。
二次因子的判别式是 $-3u^2$，在 $\mathbf Q$ 中不是平方。

设 $u\notin\mathbf Q$。由于 $[F_b:\mathbf Q]=7$ 为素数，
$\mathbf Q(u)=F_b$。若 $w\in\mathbf Q$，则 $u$ 满足有理三次
多项式 $X^3-w$，与其次数七矛盾。因此同样有
$\mathbf Q(w)=F_b$，$H_w$ 是 $w$ 的七次最小多项式。
在 $\mathbf Q(\zeta u)$ 中，$(\zeta u)^3=w$，所以它含
$\mathbf Q(w)=F_b$，进而含 $u$ 和 $\zeta$。反向包含显然，故

$$
\mathbf Q(\zeta u)=F_b(\zeta),\qquad
[\mathbf Q(\zeta u):\mathbf Q]=14.
\tag{792.10}
$$

$u$ 的七次最小多项式和 $\zeta u$ 的十四次最小多项式都整除
$N_w$，且互素；次数总和二十一，故给出全部分解。
$X^3-w$ 的三个根是 $u,\zeta u,\zeta^2u$。
后两者的有理次数十四，不能是次数七的 $q$ 的根。
故 (792.9) 恰为一次。$\square$

可执行步骤是：

1. 准确检查 $w$ 在原 $F_b$ 中，若 $w=0$ 则直接取 $u=0$。
2. 以 $w b^j\bmod P_b$ 为第 $j$ 列构造 $M_w$，求 $H_w$。
3. 在 $H_w$ 的系数间插入两个零得到 $N_w=H_w(X^3)$；在
   $\mathbf Q[X]$ 准确分解并代回全部因子。
4. 检查上述两种次数/重数模式之一，取唯一奇数次数因子 $q$。
5. 将 $q$ 的有理系数嵌入原 $F_b$，用 Euclid 算法与 $X^3-w$
   求首一最大公因式；检查它的次数确为一，读出 $u$。
6. 准确核 $u^3=w$、$c(u)=u$，最后置 $x_0=\zeta^2u$。

求最大公因式时可先将次数至多七的 $q$ 对 $X^3-w$ 取余；以后
只需次数不超过三的 $F_b$ 多项式操作。原 R754 的七次字段运算
已经足够。所需 Python FLINT 0.9.0 接口为
[`fmpq_mat.charpoly()`](https://python-flint.readthedocs.io/en/latest/fmpq_mat.html)
和 [`fmpq_poly.factor(monic=True)`](https://python-flint.readthedocs.io/en/latest/fmpq_poly.html)。
这两个接口分别给有理特征多项式和有理不可约因子；算法不调用
数值根、数值嵌入猜测或有理重构。

## 4. R787、R790、R791 的字段坐标准确接合

R787 的最终 `R787-original-function-recipe.json.gz` 必须有
`candidate_only_until_full_exact_verification=false`、
`exact_original_A_equals_yB=true`、`B_nonzero=true` 及
`full_129_original_relations_verified=true`，并由其成功证书的
`relation_spec` 逐字节/SHA 绑定。
尚在 Dixon 提升中的候选不能进入本篇算法。

其每个系数的十四个整数坐标顺序为

$$
B_{\rm fld}^i\varsigma^j,\qquad
j=0,1\text{ 为外层},\ i=0,\ldots,6,
\qquad B_{\rm fld}=\lambda b.
\tag{792.11}
$$

必须读同一 recipe 的 `field.lambda` 以及
`field.original_b_minimal_polynomial`，后者与原 R735 证书逐项
相等。对一行 $c_0,\ldots,c_{13}$，在 R754/R791 的原
$a(b)+d(b)\zeta$ 坐标中准确为

$$
\sum_{i=0}^6\lambda^i
\bigl((c_i+c_{7+i})+2c_{7+i}\zeta\bigr)b^i.
\tag{792.12}
$$

这是 $\varsigma=1+2\zeta$ 的代入，不改变原 $b$，不选另一扭曲。
R787 已对整条 $(A,B)$ 共同清分母、除整数 content；这两个共同
因子不应再乘回，因为它们在函数比值和其导数中同时约去。

R790 的每行 `value_K_1_zeta`、`derivative_z_K_1_zeta` 都是
$a+d\zeta$，每个有理数使用 `[numerator_string,denominator_string]`。
将其作为原 $L$ 中的常数多项式嵌入即可，不能把两个有理坐标
当成 $1,\varsigma$ 坐标。R791 的切向量已直接使用同一原
$b,\zeta$ 表示。

求导只对原粗参数 $z=a-1$ 进行；$b,\lambda,\zeta$ 和 R787
关系系数都是算术常数，不随该几何参数变化。

## 5. 保留原基顺序和 82 的全部尺度

R786 的 1234 列是同一个原 R775 power5 基，准确列为
$82^{10}F_\nu$。R790 输出的是

$$
\widehat\psi_i=82^2\frac{T_iE_6}{E_4^2},\qquad
\bigl(\widehat\psi_i(P_1),\widehat\psi_i'(P_1)\bigr),
\quad 0\le i<146.
\tag{792.13}
$$

其 `original_M2_scale`、逐行 `integer_scale` 均为 `6724`；
`R786_power5_product_scale` 为 `13744803133596058624`。
所以五次原乘积已经包含 $82^{10}$。不能在合成后再乘一次这个数。
R787 原 Laurent 验证中出现的 $246^3$、$\kappa$、尖点相位
$\xi^{10n}$ 也不能在 CM 评价时重新附加：它们已经用于认证
同一全局函数关系，没有改变全局截面坐标。

递归消费 R775 已保存的 `kind=product` recipe：

$$
(k,i)\longmapsto(k_1,i_1),(k_2,i_2),
\qquad k_1,k_2>0,\ k_1+k_2=k\le5.
\tag{792.14}
$$

从 $(v,d)$ 的准确一阶乘法

$$
(v,d)(v',d')=(vv',dv'+vd')
\tag{792.15}
$$

得到五次基的值/导数。此公式不除以任何 $v$，允许某些原权二
基在 CM 点取零。记忆化只合成尚未合成的 recipe 节点，不重跑
原 Fourier 系数或基选择。

准确对齐的证据链是：

| 接口 | 必须验证的实际关系 |
|---|---|
| R787 → R786 | recipe 的 `R786_producer` 等于原 R787 configuration 中生产者；`R786_basis_index` 等于成功 R786 证书 `basis_index`；全 1234 列保持原顺序 |
| R786 → R775 | R786 的 `R775_completed_prefix_producer.files` 与本次消费的 M2、power2–5 文件 SHA 相等 |
| 新 R775 → 旧 R775 prefix | 新成功 run43679160495 的这五个阶段与 R786 曾消费的旧 run43631335355 阶段逐字节 SHA 相同；不以相同维数替代该校验 |
| R790 → R775 | 146 个行 index、完整 `original_recipe` 和 `M2_recipe_source_sha256` 与同一 M2 文件相同 |
| R791 → 原模型 | 原第 4 号、次数1206、同一 R735 模数；`original_c1_slash_count=1`；原微分方向不再乘 $\zeta^2$ |

R790 的一日续传 bundle 已保留 R775 power2–5 作为
`continuation_only_retained_files`，它们不改 R790 的数学输入。
R786 的 basis index 只列各准确行的 SHA，并不展开全部乘积树；
因而不能误以为只有 index 就足够合成所有五次 CM 值。

## 6. 任意真实共同零的处理与第一阶何时足够

将共同局部框架换成 R790 的 $(E_6/E_4^2)^5$ 后，记

$$
\widetilde A(z)=\sum_{r\ge0}a_rz^r,\qquad
\widetilde B(z)=\sum_{r\ge0}b_rz^r.
\tag{792.16}
$$

两者使用同一个非消失局部平凡化，因此
$y=\widetilde A/\widetilde B$，截面的真实零阶不变。
R790 定理790.1 给

$$
r_0:=\min\{r:(a_r,b_r)\ne(0,0)\}\le154.
\tag{792.17}
$$

若 $b_{r_0}\ne0$，则准确的有限值是
$y_0=a_{r_0}/b_{r_0}$；用定理792.1–792.2 即得整个 $\beta_C$。
若 $b_{r_0}=0$，则 $a_{r_0}\ne0$，原 $y$ 有极点，故
$\beta_C=O$。

初次 R790 给 $a_0,a_1,b_0,b_1$。全部分支为：

| 已认证的一阶输入 | 准确结论 |
|---|---|
| $b_0\ne0$ | $y_0=a_0/b_0$，以共轭选根恢复整个原点 |
| $b_0=0,\ a_0\ne0$ | 原像为 $O$ |
| $a_0=b_0=0,\ b_1\ne0$ | $y_0=a_1/b_1$，同样恢复整个原点；无需第二 coarse jet |
| $a_0=b_0=0,\ b_1=0,\ a_1\ne0$ | 原像为 $O$ |
| $a_0=b_0=a_1=b_1=0$ | 只证明真实共同零阶至少二；继续准确局部评价，不能输出数值点 |

这比单靠 $x=3(y^2-b)h/dy$ 的接法少需一个共同零后的系数。
一旦共同零阶是 $r_0$，本篇只需至 $z^{r_0}$ 的系数；无须为了
选择 $x$ 再求 $z^{r_0+1}$。
最坏情况下 R790 的原155项界已足够整个点，不再另增第156项。
这仍是严格有限界，不表示初次实际共同零阶已经得到。

## 7. 原切向作为独立检验和导数输出

R791 的同源产物给

$$
h_0=\left.\frac{f_4^*(dx/(2y))}{dz}\right|_{c_1}\in L^\times.
\tag{792.18}
$$

这个值已包括 R748/R745 的一次原 $c_1$ slash，不再乘相位。
由原椭圆方程和实际 pullback 微分，恒有

$$
dy=3x^2h.
\tag{792.19}
$$

因此有限点一旦由上节恢复，准确得到

$$
y'_0=3x_0^2h_0\ne0.
\tag{792.20}
$$

若 $b_0\ne0$，R790 的原一阶合成还独立给

$$
y'_0=\frac{a_1b_0-a_0b_1}{b_0^2}.
\tag{792.21}
$$

程序必须逐坐标核 (792.20)=(792.21)。这同时检验原 $z$、
$82^2$ 尺度、字段换基及原 $h$ 方向的接口。
若共同零阶为一而初次只给一阶数据，则 (792.20) 仍给准确导数；
不声称此时已经用截面商的第二阶数据独立检验它。

若原像是 $O$，$h_0\ne0$ 说明 $f_4$ 在 $c_1$ 不分歧。
原目标 $y$ 在 $O$ 有三阶极点，所以在原 $z$ 中也恰有三阶极点。
例如在 $a_0\ne0,b_0=0$ 分支，必须有 $b_1=0$；如果实际一阶
输入违反这一点，应拒绝接口，而非给出一个不一致的原点。

## 8. 直接输出原实下降模型上的点

R791 的准确三次自同源给

$$
x_R=-\frac{\zeta x_0(y_0^2+3b)}{3(y_0^2-b)},\qquad
y_R=\frac{y_0(y_0^2-9b)}{3\varsigma(y_0^2-b)}.
\tag{792.22}
$$

代入 (792.5)，可直接在原 $F_b$ 内写成

$$
\boxed{
x_R=-\frac{u_0(y_0^2+3b)}{3(y_0^2-b)},\qquad
y_R=\frac{v_0(y_0^2-9b)}{3(y_0^2-b)}.}
\tag{792.23}
$$

由 (792.7)，有限原点的这些分母均非零。
准确核 $x_R,y_R\in F_b$ 和 $y_R^2=x_R^3+b$。
若 $\beta_C=O$，则实下降点也为 $O$。

这个点是 $f_R(c_1)\in C(F_b)$，对应原
$q_R([c_1-c_0])\in\operatorname{Res}_{F_b/\mathbf Q}C(\mathbf Q)$。
R791 已证明 $q_R=vq$ 的像属于原 primitive 因子，并给实际
$\kappa v^\dagger v$；本篇不把 $v$ 的次数或原极化尺度置为一。
点坐标完成也不自动完成 $Y$ 上实际极除子、$\eta_h$、Poincaré
求值、Néron 高度或全 $p$ 排除。

## 9. 实际执行和证书边界

接续核心为 `scripts/R792_original_beta_composition.py`。
输入只接受成功原生产者的 manifest、cert、run/source/core 回执
及其逐字节/SHA 绑定的所需阶段。
R787 或 R790 尚未完成时不填写假定的成功 run 或数学值。
所有新有限域外算术，包括本篇很小的字段合成与多项式分解，仍只
在公开仓库 Actions 执行。

输出应分别记录：

- 实际四个合成系数 $a_0,a_1,b_0,b_1$ 与采用的共同零分支；
- 若有限，原 $L$ 的 $x_0,y_0$，$F_b$ 的 $u_0,v_0$，以及
  (792.8)–(792.9) 因子/gcd 证书；
- 原椭圆方程、共轭关系、原尺度和完整 input SHA 检查；
- (792.20) 的原导数，并明确是否还通过 (792.21) 独立验证；
- 原实下降点 $(x_R,y_R)$ 或 $O$，同时保留它与原 $q$ 的同源范围。

若前两阶均共同为零，输出只能是需继续的准确状态，并保留已经
完成的合成，不能标记 `actual_beta_computed=true`。
可重算的完整数据仅留一日的当前接续 artifact，不写 Git 或 Release；
仓库只记录脚本、参数、run/source/输出 SHA 及实际数学结论。

### 依据

- [R725 原 CM 目标与实方向](R725-original-CM-elliptic-model-and-splitting-field.md)。
- [R732 原点差与 Weil restriction 比较](R732-original-CM-period-kernel-and-bounded-rational-function-recovery.md)，§7–8。
- [R764 原尖点及零平移](R764-certified-original-cusp-images-and-base-translation.md)。
- [R786 原五次截面及完整129条关系](R786-original-power5-sections-and-129-Laurent-recovery.md)。
- [R787 原关系求解方法](../notes/R787-original-power5-relation-solver-method.md)。
- [R790 原 CM 框架与共同零界](R790-original-CM-fiber-regularization-and-155-jet-evaluation.md)。
- [R791 真实 Hom 下降、尺度与非分歧](R791-certified-original-Hom-descent-and-eta-inputs.md)。
