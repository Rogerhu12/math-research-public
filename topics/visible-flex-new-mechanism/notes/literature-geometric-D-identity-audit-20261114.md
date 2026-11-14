# 实际几何系数 D 恒为零：独立审计

日期：2026-11-14。结论是实际六项周期积分的精确恒等式，不是数值秩猜测。本文只核对系数映射，不证明任何有限等距族存在或不存在。

## 1. 核对来源和坐标

重新只读核对公开提交
`e241fa6511d1719d5398eff9313d036dbc11c4d4` 中：

- `scripts/literature_band_second_order.py` 的 `polynomial_period_operator`；源 blob 为 `82f141646500a9fcb5eb96219ce49f741883a660`。
- `results/R7-nine-coefficients-and-polynomial-profiles.md` 的九参数表示。
- `results/R8-flat-profile-period-equation.md` 的式 (3)。
- `notes/literature-volterra-polynomial-20261114.md` 的原始几何积分及一次分部积分版本。

九参数顺序是
\[
(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_0,t_1),
\qquad
p_0=A_1(0),\ s_1=B_1'(0),\ t_0=B_2(0).
\]
因此 R8 的常数
\[
D=p_0/2+s_1-2t_0
\]
与本次核对的组合完全相同。以下撇号若作用于 \(B_j\)，均表示对 profile 坐标 \(\xi\) 求导。

## 2. 点态推导

固定几何参数 \(s\)，记
\[
h>0,\quad k=\kappa,\quad H=h_s,\quad \omega_s=z_s,\quad
z=\omega+\xi,\quad d=h\omega-k,\quad d_s=H\omega-h\omega_s.
\]
这里 \(d_s\) 的表达式来自几何相容关系 \(k_s=2h\omega_s\)，并已在代码中直接代入。再记
\[
K_0=kz^2-\frac{k^2+1}{h}z,\qquad
Q_s=\frac{\omega_s}{h}-\frac{zH}{h^2}.
\]
需要的三个被积函数是
\[
a_1=-\frac{k}{2h}\{1+(hz-k)^2\},\qquad
b_1=\frac{K_0d+d_sQ_s}{4},\qquad
b_2=\frac{K_0h+HQ_s}{8}.
\]

在 \(\xi=0\) 处直接求导并相减：
\[
\begin{aligned}
4\{(\partial_\xi b_1)(0)-2b_2(0)\}
={}&\left(2k\omega-\frac{k^2+1}{h}\right)d
-kh\omega^2+(k^2+1)\omega\\
&+\frac{H}{h^2}(-d_s-h\omega_s+\omega H).
\end{aligned}
\]
第二行括号因 \(d_s=H\omega-h\omega_s\) 严格为零。第一行代入 \(d=h\omega-k\) 得
\[
kh\omega^2-2k^2\omega+\frac{k(k^2+1)}h
=\frac{k}{h}\{1+(h\omega-k)^2\}.
\]
于是逐点成立
\[
\boxed{\quad
(\partial_\xi b_1)(0)-2b_2(0)
=\frac{k(1+d^2)}{4h}=-\frac{a_1(0)}2.
\quad}
\tag{1}
\]

事实上同样展开给所有 \(\xi\) 的点态恒等式
\[
\boxed{\quad
\frac{a_1(\xi)}2+\partial_\xi b_1(\xi)
+2\xi\,\partial_\xi b_2(\xi)-2b_2(\xi)=0.
\quad}
\tag{2}
\]
例如在未加 \(2\xi\partial_\xi b_2\) 时，左侧恰是
\[
\frac{\xi}{4}
\left(1+k^2+\frac{H^2}{h^2}-2khz\right),
\]
而 \(2\xi\partial_\xi b_2\) 是其相反数。

三个几何系数采用相同的 \(ds\) 权重积分，因此 (1) 立即推出
\[
\boxed{A_1(0)/2+B_1'(0)-2B_2(0)=0,\qquad D=0.}
\tag{3}
\]

这一步不产生任何边界项，也不需要在此处再用周期闭合来抵消某个积分。它是已编码的几何微分相容性强制的点态关系。因此改变积分权重、加密网格或扩大几何控制空间都不能使同一几何模型得到 \(D\ne0\)。

## 3. 仿射归一化和 Jacobian

对 \(\xi=c+\ell x\)、\(\ell>0\)，正确变换的系数为
\[
\widetilde A_1=A_1/\ell,\quad
\widetilde B_1=(B_1+2cB_2)/\ell^2,\quad
\widetilde B_2=B_2/\ell,
\]
右侧函数均在 \(c+\ell x\) 求值。由 (2) 或九参数多项式展开，
\[
\widetilde D
=\frac{A_1(c)/2+B_1'(c)+2cB_2'(c)-2B_2(c)}{\ell}
=\frac D\ell=0.
\tag{4}
\]
故 profile 平移、缩放不会解除这条关系。

设几何控制参数为 \(u\)，九系数映射为 \(F(u)\)。在其可微处，
\[
(1/2,0,0,0,0,0,1,-2,0)\,DF(u)=0.
\tag{5}
\]
因此真正的九行几何 Jacobian 秩至多为 8。若数值输出对各行另作缩放，左零向量也须对应反向缩放；不能直接用未调整的向量比较。一个约 \(10^{-11}\) 的最后奇异值与这一精确关系相容，不能当成已实现九维满秩的证据。

原有关系 \([\xi]A_1+4[\xi^2]B_1=0\)、
\([\xi^2]A_1+4[\xi^2]B_2=0\) 等已经在 R7 的九参数形式中消去；(3) 是该九参数形式进一步降至至多八个实际自由系数的约束。

## 4. 对已有形式例和后续证明的范围

R13 的精确有理系数具有 \(D=-8\)。其抽象局部方程存在论证可作为更大形式系数类中的结论保留，但这组系数不属于当前实际几何积分映射的像；“再寻找闭曲线实现这组固定系数”已被 (3) 排除。不能把这一形式例继续称作同一实际几何路线的待实现种子。

\(D=0\) 本身不排除所有非零 profile。将它用于外尾排除定理时，仍须逐一保留该定理的其余条件，例如内部 \(C>0\)、指定左端根和四阶首项，以及规定的正则性。特别是 \(C\) 变号、\(C\equiv0\) 或更退化端点须单独论证。满足 \(D=0\) 也远不足以证明某组八参数能由闭曲线实现。

本审计只做独立代数推导与公开源文件核对，没有运行研究规模求解、没有改变任何物理参数，也没有把二阶周期条件提升为有限弯曲。
