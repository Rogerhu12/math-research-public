# R829 — 同一低层拉回的对角 Chow 类恒零与 R826 的准确适用范围

日期：2026-11-15。**状态：已证明。**

R826 的完整角色、张量分解及 finite-polynomial 公式保持有效。
但其第3节选定的两个 old 向量同时由同一个映射拉回；
该实际对角类为零，不能承担原 R814 指定非零类的比较。
本篇分别给直接 de Rham 证明和有理 Chow 群中的证明，
明确支付后者所需的 cusp 基点项。

## 1. 同一个映射与新空间

固定
$$
X=X_1(10404),\qquad Y=X_1(2601),\qquad d=12,
$$
以及 R826 原映射
$$
q:X\longrightarrow Y,\qquad (E,P)\longmapsto(E,4P).
\tag{1}
$$
这里 $q$ 表示映射；下面用 $Q=e^{2\pi i\tau}$ 表示展开变量。
$f=\theta(\psi_{17})$ 是原 primitive level10404 权二形式。
$g=g_j,h=g_k$ 是 R826 的 primitive level2601 形式，
在 $X$ 上均取同一个 $q^*$，故
$$
\omega_g=q^*\omega_{g,Y},\qquad
\omega_h=q^*\omega_{h,Y}.
\tag{2}
$$

有准确的 motivic 和 de Rham 消失
$$
\boxed{
e_f q^*:h^1(Y)\longrightarrow h^1(X)=0,\qquad
q_*\omega_f=0.
}
\tag{3}
$$
式(3)第一项表示复合 $e_f\circ q^*$ 为零，不是整个 $q^*$ 为零。

这里可直接使用 $f$ 在2处的新空间性质。
也可不依赖新空间术语：$Y$ 的级别为奇数，其 Jacobian 在2处好约化；
对任意辅助素数 $\ell\ne2$，$V_\ell\operatorname{Jac}(Y)$ 的 $I_2$ 作用平凡。
R806/R826 已证明 $f$ 的完整二维表示满足
$$
V_\ell(f)^{I_2}=0
$$
（其2处 primitive Euler 因子为1，局部导子指数为2）。
所以从 $\operatorname{Jac}(Y)$ 经 $q^*$ 到 $f$ 因子的同态在 Tate 模上为零，
该同态自身也为零：阿贝尔簇同态对 Tate 模的作用是忠实的。
曲线 $h^1$ 的对应通过 Jacobian 的同态识别，给(3)第一项。
转置及 de Rham 实现给第二项。
此处不把 cohomology 的零直接冒认为任意高余维 Chow 对应的零；
所用忠实性仅限曲线的 $h^1$ 对应。

## 2. 第四槽分子是一个低层拉回

取 R826 的任一原 ordinary 素数 $p>17$：
$$
p=\pi\bar\pi,\quad v_p(\pi)=1,\quad
\varphi\omega_f=-\pi\omega_f,\quad
\varphi\omega_g=\pi\omega_g,\quad
\varphi\omega_h=\pi\omega_h.
$$
因 $q$ 的次数和级别在 $p$ 处可逆，可在对应 ordinary dagger 开集上
使用与 $q$ 交换的 canonical-subgroup Frobenius lift。
下层存在零 $Q$ 常数的实际原函数
$$
dG_{g,Y}=(1-\pi^{-1}\Phi_Y^*)\omega_{g,Y},\qquad
dG_{h,Y}=(1-\pi^{-1}\Phi_Y^*)\omega_{h,Y}.
$$
它们拉回后满足 R826(23) 的同一方程和同一零常数规范，故
$$
G_g=q^*G_{g,Y},\qquad G_h=q^*G_{h,Y}.
\tag{4}
$$
在所选连通开集上，两个原函数之差为常数，cusp 规范将其固定为零。
等价地，可由 R826 附录A的完整 $Q$ 展开逐项确认(4)。

所以两项必须一起保留的形式
$$
\Xi_{g,h}=G_g\omega_h-\pi^{-1}G_h\Phi_X^*\omega_g
$$
满足
$$
\boxed{
\Xi_{g,h}
=q^*\left(G_{g,Y}\omega_{h,Y}
-\pi^{-1}G_{h,Y}\Phi_Y^*\omega_{g,Y}\right)
=q^*\Xi_Y.
}
\tag{5}
$$
Besser 所用开曲线至 proper cohomology 的 Frobenius 相容投影与此拉回相容。
因此杯积的投影公式和(3)给
$$
\boxed{
\langle\omega_f,[\Xi_{g,h}]\rangle_X
=\langle q_*\omega_f,[\Xi_Y]\rangle_Y=0.
}
\tag{6}
$$
亦可先在 proper $f$ 分量投影后应用同一恒等式；
没有额外的次数12因子能将零变成非零。

代入 R826(26) 的非零分母，得到
$$
\boxed{
AJ_p(\Delta_X)(\omega_f\otimes\omega_g\otimes\omega_h)=0
}
\tag{7}
$$
对 R826 所用每个原 ordinary $p$ 成立。
该结论不只是 $g=h$ 时的反对称消失；
R826 的三个不同有序对全部适用。
全纯测试不随原函数常数改变，所以(7)也不依赖零常数规范的表达方式。

## 3. cusp 基点与 Chow–Künneth 相容性

下面均用有理系数，并在容纳 cusp 及原 CM 对应的固定数域上工作。
取支撑在 cusp 的 degree1 零维循环 $o_X$，
令 $o_Y=q_*o_X$。Manin–Drinfeld 定理给
$$
\boxed{
q_*o_X=o_Y,\qquad q^*o_Y=d\,o_X
\quad\text{于 }CH^1(X)_{\mathbf Q}.
}
\tag{8}
$$
第二式成立是因为差的次数为零且支撑全部在 cusps。
若先把 cusp 全部有理化，该差为 Picard 群中的 torsion；
再由有限扩域的 restriction–corestriction 得到所用固定定义域上的有理系数等式。
对 Galois 平均的 degree1 cusp 循环同样成立。

用这些基点定义
$$
\pi_{1,X}=\Delta_X^{(2)}-o_X\times X-X\times o_X,
$$
并对 $Y$ 同样定义。
(8)使 $q^*,q_*$ 与这两份 $h^1$ 投影相容。
可将对应展开直接核验：可能多出的 degree-zero 基点项
恰是 $q^*o_Y-d o_X$ 或 $q_*o_X-o_Y$，都已由(8)消去。

这一步不可对任意 pointed 曲线省略。
如果只知道 $q(o_X)=o_Y$，一般不能据此断言
$q^*o_Y=d o_X$；未消掉的 Picard 基点项可能进入 Chow 投影。
本篇利用的是实际 modular cusps 和有理系数，不是一个错误的一般性断言。

设 $e_g^Y,e_h^Y$ 是 $h^1(Y)$ 中的实际新形式投影。
其 R826 原 old 嵌入在 $h^1(X)$ 上的幂等元为
$$
e_g^X=d^{-1}q^*e_g^Yq_*,
\qquad
e_h^X=d^{-1}q^*e_h^Yq_*.
\tag{9}
$$
因 $q_*q^*=d$，(9)确为相应副本的投影。
它也准确解释 R826 单位根规范中的 $1/12$；
没有以某个未明的周期替代映射次数。

## 4. 小对角的有限平坦恒等式

用 $\Delta^{\rm sm}$ 表示小对角，避免与二重对角混用。
在 $X\times Y\times Y$ 上有精确循环恒等式
$$
\boxed{
(\mathrm{id}_X\times q\times q)_*
 [\Delta_X^{\rm sm}]
=(q\times\mathrm{id}_Y\times\mathrm{id}_Y)^*
 [\Delta_Y^{\rm sm}].
}
\tag{10}
$$
左边是图形 $x\mapsto(x,q(x),q(x))$，推前的泛型次数为1；
右边是相同图形的有限平坦拉回。
因此(10)中没有被漏掉的 $d$ 或 $d^2$。

在三因子都施 $h^1$ 投影时，
基于 $o_X$ 的 Gross–Kudla–Schoen modified diagonal 与普通小对角
有相同像：每个其它部分对角项至少有一因子固定为 $o_X$，
而其 $h^1$ 投影为零。
借(8)，可在(10)两边自由交换相应的 $h^1$ 投影与 $q^*,q_*$。
将(9)用于第二、三因子后，
所求投影是以下循环经外部拉回再乘 $d^{-2}$ 的像：
$$
(e_f\otimes e_g^Y\otimes e_h^Y)_*
(\mathrm{id}\times q\times q)_*
[\Delta_X^{\rm sm}].
$$
按(10)，这又通过第一因子的
$$
e_fq^*:h^1(Y)\longrightarrow h^1(X)
$$
分解，故由(3)为零。于是
$$
\boxed{
(e_f\otimes e_g^X\otimes e_h^X)_*[\Delta_X]
=0\quad\text{于 }CH^2(X^3)_{\mathbf Q}\otimes L,
}
\tag{11}
$$
其中 $L$ 是同一个固定 CM 系数域，$\Delta_X$ 现在回指 R826 的修正对角。
任何进一步 CM 幂等元投影也为零。
特别 R826 的 $\lambda_\ell$ 分量为零，所有 Abel–Jacobi 实现和三个 ordinary 槽均为零；
不需要普通素数假设来证明(11)。

## 5. 对原研究路线的直接影响

R817 在固定 $p=7993$ 已证明三个原 R814 canonical cycles 的指定
Abel–Jacobi 值非零。因此这些类自身非零。
(11)说明 R826 当前同一 $q^*$ 选定的类
**不可能**等于该原类的任何非零标量倍，
也不可能通过保持这些实现的同构得到那样的比较。
这个不可能结论已完成，不再把同一向量的分子非零列为待证目标。

以下部分保持原有效范围：

- R826 的完整固定 Hecke 角色、四 CM 张量因子、全部坏处 Euler 及复解析秩一；
- 其 finite-polynomial 杯积公式、两项表达、Frobenius 分母和 companion 展开；
- 附录B中原单形式临界斜率 $p$-adic $L$ 函数的导数公式。
  该公式来自同一原 $\lambda_\ell$ 的 LLZ–Katz 身份，独立于此零对角类。

下一步须改变实际局部向量。
例如在2处把其中一份下层形式改由不同的 degree12 退化映射拉回，
然后重新核定全部坏位的 trilinear test vector、
实际对角类及原 canonical 比较。
“存在局部测试向量”不等于任一向量非零，更不等于全局 AJ 非零。
本篇不对更换后的类作这些尚未支付的断言。

## 6. 依据

本篇没有新增程序计算。新结论来自(3)、(5)的投影公式和(8)–(10)的循环恒等式。

- V. G. Drinfeld, *Two theorems on modular curves*,
  Functional Analysis and Its Applications **7** (1973), 155–156，
  第一定理；俄文原刊 Funktsional. Anal. i Prilozhen. **7**(2), 83–84。
  <https://doi.org/10.1007/BF01078890>；
  原刊全文 <https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2422&what=fullt>。
  亲读第一定理：任意 congruence subgroup 的 cusp 差为 torsion。
- R. Elkik, *Le théorème de Manin–Drinfeld*, Astérisque **183** (1990),
  59–67，p.59 的定理及完整证明。
  <https://www.numdam.org/item/AST_1990__183__59_0.pdf>
- A. Besser, *On the regulator formulas of Bertolini, Darmon and Rotger*,
  Research in the Mathematical Sciences **3** (2016), article26，
  Proposition2.1、Proposition2.2、(2.7)、(2.11)及§4；
  实际规范已在[R826](R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md)逐项展开。
  <https://link.springer.com/article/10.1186/s40687-016-0073-x>
- [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)、
  [R814](R814-common-fixed-good-pair-and-three-original-aj-squares.md)、
  [R817](R817-fixed-prime-original-negative-two-and-nonzero-fixed-cycles.md)：
  原有限角色、指定 canonical 类与固定7993非零。
