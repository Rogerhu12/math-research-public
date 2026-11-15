# 原光滑立方的实际因子轨道与临界偶因子化

日期：2026-11-15。**状态：已证明。** 本 note 进一步缩小原 R697/R701 的真实立方候选，
不判定剩余指定 $\mu J(P^{\rm fact})/p$ 的像。
相对于此前的模三负项排除，这里利用一个实际因子轨道的所有曲线具有同一个数值类。

## 1. 同一候选及其真实轨道

取
$$
p=6s-1>101,\quad D\ge3,\quad f_D<p,\quad
N_D=\dim\mathcal W_D,\quad
\delta_D=N_D-(2s+\ell).
$$
保持原 $\mathcal B_D$、十九个角中心和完整相对 $\bar J$。
假定一个实际非零候选具有
$$
\bar P=d^{-C_D}t^rQF^3\in\ker\bar J,\qquad
F(0,1)=0,\quad(\mathcal EF)(0,1)\ne0,\quad Q(0,1)\ne0.
\tag{1}
$$
只取经过 $(0,1)$ 的 primitive 几何不可约因子作为 $F$。
若原分解含别的在该点为单位的因子，将它们准确并入 $Q$；
这一步只识别约化后的实际因子，不声称保持此前对某个特定最高系数的额外假设。
该因子在 $\bar P$ 中的重数准确为三，记其曲线为 $C$，
$$
b=\deg_YF,\qquad \kappa=C^2\ge0.
$$

若整个 $\bar P$ 的非零 charge 同余模 $q$，其中 $q=2$ 或 $3$，
则 $\mu_q$ 的作用 $Y\mapsto\zeta Y$ 置换它的实际因子。
令 $l$ 为 $C$ 的轨道长，故 $l\mid q$，稳定子阶为 $a=q/l$。
所有轨道因子的重复次数都准确为三。

原帽仍给
$$
r\le M_D=5D+4-(D\bmod2),\qquad 3lb\le D.
\tag{2}
$$
若 $r\ge s$，已有 $s\le M_D$ 的低预算排除。下面保 $r<s$。

## 2. 全十九角上轨道曲线的数值类相同

原 $Y$ 伸缩作用保持 $\mathbb F_4$ 的两个截面、底纤维及每一个原角中心。
在 R495/R680 的逐步角图
$$
z=x^j z_j,\qquad x=Y\text{ 或 }Y^{-1},
$$
伸缩仅将 $x,z_j$ 分别乘以互逆的固定幂单位，
所以每一步的原零中心仍固定。该作用因此提升到整个十九次吹起曲面 $X$。

它逐一固定 $S_0,F_0,E_{\alpha,j}^*$ 的类；这些生成原 Picard 格。
因此轨道中每条严格曲线都与 $C$ 数值等价：
$$
C_\zeta\equiv C.
\tag{3}
$$
这不是只在原平面中比较总次数。

来源截面含有实际有效子除子
$$
\mathscr C_{\rm orb}=3\sum_{\text{轨道}}C_\zeta.
$$
R680 已付各 $C_\zeta$ 和 $\mathcal B_D$ 均 nef。
由 $\mathcal B_D-\mathscr C_{\rm orb}$ 有效，得到
$$
\boxed{
9l^2\kappa=\mathscr C_{\rm orb}^2\le\mathcal B_D^2.
}
\tag{4}
$$
所有其它因子和十九角余量留在有效余除子中，未被删掉。

## 3. 稳定子给同一因子的 a 个高接触点

$F$ 的常数 $Y$ 系数非零，否则它被 $Y$ 整除，不能是 (1) 的因子。
对稳定子中的 $\zeta$，primitive 性先给
$F(t,\zeta Y)=c_\zeta(t)F(t,Y)$；
比较非零常数系数迫 $c_\zeta=1$。
所以
$$
\boxed{
F(t,\zeta Y)=F(t,Y)\quad(\zeta\in\mu_a).
}
\tag{5}
$$
特别 $F$ 只有 $a$ 的倍数 charge。

同一光滑支 $Y=\psi(t)$ 因而给 $a$ 个互异点
$(0,\zeta)$ 及支 $\zeta\psi(t)$。
这些点避开原吹起中心，且相对于 $\zeta g(t)$ 的接触阶相同。
令 $h=\operatorname{ord}_t(\psi-g)$。
由原第二长行和 (1) 的两个单位，
$$
\min(h,s)\ge(s-r)/2.
\tag{6}
$$
R680 的全局 Euler forcing 在同一个 $C$ 上不恒零，
其总零长度至多 $3\kappa+8b$。
在 (5) 的全部 $a$ 个不同点相加原局部交数估计，得到
$$
\boxed{
\frac ql\min(h,s)\le3\kappa+8b.
}
\tag{7}
$$
这里仅用同一原截断 ODE；接触超过 $s$ 时仍取最小值，
没有向共振之后延长方程。

联立 (4)、(6)、(7) 即得新的完整有限必要条件
$$
\boxed{
3ql(s-r)\le2\mathcal B_D^2+48l^2b.
}
\tag{8}
$$
与只把三个重复根视作一个总次数不同，(8) 同时保留实际轨道数 $l$
和稳定子实际接触点数 $q/l$。

## 4. 原维数临界中的排除与偶因子化

准确使用
$$
\mathcal B_D^2=2N_D-2D-17
=4s+2\ell+2\delta_D-2D-17.
\tag{9}
$$
若
$$
D\to\infty,\qquad \delta_D=o(D^2),\qquad
\ell=o(D^2),\qquad p/D^2\to47/8,
$$
则 (2)、(8)–(9) 给
$$
\boxed{ql\le8/3}
\tag{10}
$$
这一必要条件：若 $ql>8/3$，(8) 的二次主项已经严格矛盾。
$q,l\le3$ 固定，所以所有被保留的线性项都确实是 $o(D^2)$。

因此：

- $q=3$ 时，无论真实轨道长是一还是三，都不存在 (1) 的临界候选。
- $q=2$ 时，轨道长二被排除，只能有 $l=1$。
  此时稳定子为整个 $\mu_2$，(5) 准确迫
  $$F(t,Y)\in k[t,Y^2].$$

这条偶性属于经过指定点的真实不可约因子，
不是从整个多项式偶性直接跳到所有因子偶性。
排除轨道长二正是所需的额外论证。

对于 $q=2,l=2$，(8) 有特别简短的有限形式：
$$
\boxed{
s\le
\delta_D+\ell+3r-D-\frac{17}{2}+48b
\le\delta_D+\ell+3r+7D-\frac{17}{2}.
}
\tag{11}
$$
最后使用 $6b\le D$。
再以 (2) 消去 $r$，可写成完全由原预算给出的必要条件
$$
\boxed{
s\le\delta_D+\ell+22D+\frac72-3(D\bmod2).
}
\tag{12}
$$
这些是有理数不等式，整数 $s$ 按原值读取；没有向上舍掉一个单位。

## 5. 对剩余同 R 问题的限制

在仍可能存在的模二临界立方中，
约化因子 $F$ 本身为 $Y^2$ 的多项式，所以其约化最高 charge 缺口至少为二。
如要用 R701 的两 charge **整**返回，仍须检验同一个实际整提升的缺口、
两个无穷远矩条件和四份无穷远缓冲；本 note 没有自动赋予这些条件。

尤其不能把同一个第一修正 $R$ 也强行改成偶函数。
当前原目标只在指定 $g$ 轴读取；
一个未知 $R(t,-Y)$ 并未被证明在该目标上解决同一方程。
因此后续仍须保整个原 $\mathcal W_D$ 的两种 parity、
原顶两/三 charge、两条十三行和同一个完整 $d_2$。

最大公因数为一的候选，以及这里剩下的真正偶因子候选，
继续进入原 $\mu J(P^{\rm fact})/p$ 的全 $J$ 首像测试。
本 note 不把 (8) 的实际候选排除认作主中央非零。

依赖：[R495](../results/R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R680](../results/R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)；
[前一模三 note](2026-11-15-critical-mod-three-smooth-cube-exclusion.md)；
[R701](../results/R701-sharp-two-charge-clearing-and-complete-same-correction-cap.md)。
