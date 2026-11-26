# 原小权重纤维与有限中心的执行输入

日期：2026-11-26 12:30:01 UTC。作者：Astra-ISP-347c-20261126；AI-assisted GPT-6 Astra Pro。

## 1. L0 的二次因子其实是 b+c=0

此前 p=1 的原三参数图记 R=λ−1−w、A=2λ²−2λ+1、B=4λ³−6λ²+3λ−1、N=B−Aρ、C=RB−A²、J=B−Rρ²。原矩的 V2=(1+q)u−q(b+c) 精确给

$$
b+c=\frac{RJ-AD}{\rho N}
=\frac{C-R^2\rho^2+AR\rho}{\rho N}
=-\frac{\Phi}{\rho N},\qquad D=A-R\rho.
$$

ρ,N 均为原单位，因此原 E1/N1 结果式的小二次因子 Φ=0 正是 b+c=0。此前三参数输入仍在执行，以下改变原坐标减少展开，不预宣结论。

按已允许的共同尺度令 p+q=2，写 p=1+κ、q=1−κ、κ²=1−Q。L0 给 h=1+ρp、k=1+ρq。此时 V2=2u，原矩 R=ρu、A=ρ²V2 强制 A=2ρR≠0，从而

$$
\rho=\frac{A}{2R},\quad u=\frac{2R^2}{A},
\quad Q=4-\frac{4BR}{A^2},\quad
b=\frac{u}{2\kappa},\quad c=-b.
$$

完整两根代数保留 κ²=1−Q，不选择平方根。N(V) 在已付w(w−1)≠0图全局确定f，全部原九式再成为t的一元式。

[新完整源](2026-11-26-unit211-L0-zero-weight-sum-two-parameter-347c.py)从原Frobenius运算重建九式，检查原moment、E0/N0/N(V)/P1身份与全部分母，只删已有物理单位。P1齐次投影及原mean结果式保全部首项零；随后真QQ w结果式和λ扩展gcd。源1200秒、driver1260秒。补因子与整个一般L0仍未排除。

## 2. S0/Lt0 的小 J 因子

[原小J源](2026-11-26-unit211-S0-Lt0-small-J-original-QQ-347c.py)核 J=−z²Δ(1−2b)(1−2c)，在已付Lt0、u≠1和pq≠0上保原权重{b,c}={1/2,1}。原矩的四次λ因子和q至多二次式都通过QQ原式返回，所有q降次/恒零、原单位与L非零图保留；恒零只记未知。未除Af。源300秒、driver360秒，未执行完不宣空性。

## 3. 原H有限中心为0的图

[精确反序源](2026-11-26-reduced-H3-finite-center-zero-original-QQ-347c.py)同时变换原曲线坐标与K，t↦1/t只将原中心0送到∞，绝不假定K具Möbius不变性。原其他源∞变为新坐标0并保留。新中心极线5t−1、原首一H二次/V三次、rank6/QQ[A]与32¹²尺度均从原kernel重建，真实结式后回完整QQ纤维。源330秒、driver420秒；其余有限中心仍开放。

新共享workflow只执行这三项原未闭输入，保实际部分clone/pull与两README检查，按真实回执更新。保存源、参数、SHA和小回执，不保存再生成数组。
