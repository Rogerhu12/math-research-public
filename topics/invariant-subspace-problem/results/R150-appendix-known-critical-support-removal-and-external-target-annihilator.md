# R150：剥离已付临界支撑后的共同余乘子与九目标湮灭因子

日期：2026-11-15 UTC。作者：AI（ChatGPT；Astra-ISP-789f / root、literature_audit）。

## 1. 原模块与共同湮灭多项式

保持原有限来源模块
$$
L=A\,\mathbb Q[s]^{6188}\subseteq Y=\mathbb Q[s]^{4367}
$$
和九个原平方 $t_j$（$2\le j\le10$）。[原泛型像回接](R150-appendix-original-generic-image-bridge-exact-cubic-zero-cost-and-thirteen-free-heads.md)已经证明每个 $[t_j]\in Y/L$ 是扭元素。因此
$$
\mathfrak a=\{a\in\mathbb Q[s]:a t_j\in L\text{ 对全部 }j\}
$$
是一个非零理想。令其首一生成元为 $H_{\mathrm{tar}}$。以下只确定其因子范围，不计算它的系数。

置
$$
\Sigma_0=s(s-2)(s+6)F_+F_-E_8,\qquad
h_*=s^3F_+^2F_-^2E_8.
$$
各因子使用原实际多项式；$F_+,F_-,E_8$ 在 $\mathbb Q$ 上不可约且互不相伴，也不含前三个线性因子。

本篇证明
$$
\boxed{
H_{\mathrm{tar}}\doteq
s^3F_+^{a_+}F_-^{a_-}E_8^{a_8}U,\quad
0\le a_\pm\le2,\quad0\le a_8\le1,\quad
\gcd(U,\Sigma_0)=1,
}
\tag{1.1}
$$
其中非零 $U\in\mathbb Q[s]$ 可取首一，且 $\deg U\le162$。符号 $\doteq$ 表示相差非零有理常数。本篇不声称 $U=1$。

## 2. 已付局部费用逐个给出指数

以下均指同一原来源次数至多三的局部模块。

在 $s=0$，[原泛型像及精确三阶定理](R150-appendix-original-generic-image-bridge-exact-cubic-zero-cost-and-thirteen-free-heads.md)证明 $s^3t_j$ 全部入像，并对 $t_2$ 证明低于三阶不入像。因此
$$
v_s(H_{\mathrm{tar}})=3.
$$

在 $s=2$，[完整有理谱十二及目标局部成员性](R150-appendix-two-complete-third-connection-smith12-and-all-original-square-local-membership.md)证明九个未乘因子的 $t_j$ 全部入像。在 $s=-6$，[同长十二的原投影证明](R150-appendix-minus-six-local-smith-length12-and-original-nine-target-membership.md)给出相同结论。所以
$$
v_{s-2}(H_{\mathrm{tar}})=v_{s+6}(H_{\mathrm{tar}})=0.
$$

[两个三次数域证明](R150-appendix-both-cubic-fields-low-smith33-and-original-nine-target-local-membership.md)给 $F_\pm^2t_j$ 的局部来源，故 $v_{F_\pm}(H_{\mathrm{tar}})\le2$。
[E8 原低投影与精确序列](R150-appendix-original-low-projection-double-linear-divisor-and-E8-local-target-membership.md)给 $E_8t_j$ 的局部来源，故 $v_{E_8}(H_{\mathrm{tar}})\le1$。

这些陈述给出 (1.1) 的全部已知支撑指数。它们不要求原完整最大子式在 $F_\pm,E_8$ 的长度都已经精确确定，也不把临界点集合上的消失当作来源恒等式。

## 3. 从真正 gcd 定义不含已知支撑的余乘子

沿用真正完整特征零最大子式 gcd
$$
\Delta_{\mathrm{aff}},\qquad
K_{158}=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4,
\qquad
R=\Delta_{\mathrm{aff}}/K_{158}.
$$
[无穷远完整小投影](R150-appendix-infinity-original-projection-exact-length61-and-full-length-gap-five.md)给
$$
\deg R\le162.
$$
零点、二点和负六点的完整原长度分别已经精确为 $66,12,12$，等于 $K_{158}$ 在各点的次数。因此
$$
R(0)R(2)R(-6)\ne0.
\tag{3.1}
$$

两个三次点完整长度在 $6$ 与 $8$ 之间，E8 完整长度在 $4$ 与 $5$ 之间。因此
$$
e_\pm:=v_{F_\pm}(R)\in\{0,1,2\},\qquad
e_8:=v_{E_8}(R)\in\{0,1\}.
$$
定义
$$
R_{\mathrm{out}}
=\frac{R}{F_+^{e_+}F_-^{e_-}E_8^{e_8}}.
\tag{3.2}
$$
这是非零有理多项式，并且
$$
\boxed{
\gcd(R_{\mathrm{out}},\Sigma_0)=1,\qquad
\deg R_{\mathrm{out}}\le162-3e_+-3e_--8e_8\le162.
}
\tag{3.3}
$$
若只希望用多项式运算表达，(3.2) 的分母可取首一 $\gcd(R,F_+^2F_-^2E_8)$；差一个非零常数无关。

## 4. 全局来源不受这次剥离影响

[删除二点因子定理](R150-appendix-removing-two-factor-from-global-nine-target-multiplier.md)已经给
$$
Rh_*t_j\in L.
$$
现在证明更强的
$$
\boxed{R_{\mathrm{out}}h_*t_j\in L\quad(2\le j\le10).}
\tag{4.1}
$$

在 $F_+,F_-,E_8$ 的局部环，$h_*t_j$ 本身已经有第 2 节的原来源，所以删除 $R$ 在这些点的因子不影响局部成员性。在其他任一不可约素点，(3.2) 的分母是单位，故旧关系 $Rh_*t_j\in L$ 直接给出新局部关系。对全部最大理想应用有限生成 $\mathbb Q[s]$ 模的局部判准，得到 (4.1)。

因此 $H_{\mathrm{tar}}\mid R_{\mathrm{out}}h_*$。与第 2 节的准确局部指数结合，(1.1) 中的未知因子 $U$ 满足
$$
U\mid R_{\mathrm{out}},
$$
从而 $\deg U\le162$。这个论证只使用原局部来源及 PID 上的局部判准；它没有对未知的来源向量逐坐标除以被剥离的因子。

同一个 $R_{\mathrm{out}}$ 对九列使用，且
$$
\deg(R_{\mathrm{out}}h_*)\le185.
$$
沿[同一原方阵的三支成本整理](R150-appendix-global-residual-multiplier-nine-sources-cost8531.md)，目标权至多 $225$，三个分支至多 $8526,8531,333$。故九个实际多项式来源可同时取成本至多 $8531$，原 $m$ 乘子次数仍至多三。

## 5. 下一缺口的准确位置

旧[泛参数临界分类](R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md)把例外集合定义为 $\{g\Delta_{\mathrm{aff}}=0\}$。它没有把该集合证明为仅包含 $\Sigma_0$ 的根。[非接触中心算子秩控制](R150-appendix-rank-one-noncontact-centered-rank-controls-macaulay-projection.md)给投影秩的上界；在线性块满秩的点，还需完整原 Macaulay 来源的相反下界或等价局部来源，才能得到 $W$ 入像。

所以 (3.3) 把未处理的九目标支撑隔离到 $\Sigma_0$ 之外，却没有将它删除。$R_{\mathrm{out}}$ 可能含完整模块和低投影共享的扭因子，这些因子未必作用于九目标；也可能含真正目标障碍。后继应比较真实完整/投影长度或直接构造九目标来源，不能把 $R_{\mathrm{out}}$ 的每个因子直接当作必须新增的目标因子。

本篇无新数值运算。它不提供 $R_{\mathrm{out}}$、$U$ 或九来源的展开系数，不给系数高度或固定 $31$ 分母。
