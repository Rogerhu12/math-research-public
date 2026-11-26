# R1033：原有理 CM 圆盘上最低型的准确共同尺度与完整尾界

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；
global_route / root。

**已证明：R1029 的实际整最低惯性型，在原
\(w=(a-1)/p^3\) 圆盘上有准确共同尺度 \(p\varepsilon\)。**
原 Abel-log 除以该尺度后的模 \(p\) 轮廓是次数至多
\((p-2)/3=4g-1\) 的多项式；整个类型块的最高系数非零，
并由 R1032 的同一个真实 CM jet 给出。
全部 \(p\) 倍次数的积分分母已包括，formal 坐标与 log
在此规范下有相同的模 \(p\) 轮廓。

这不是最低非零 \(w\) 系数的单位定理，不是某个指定
\(\mathbf Q\)-简单商的 Néron 尺度定理，也不将除去真实
Mordell–Weil 空间后的尺度宣称为一。

## 1. 原参数和不能删除的单位

设
\[
p=12g-1>37,\quad m=(p-1)/2,\quad e_0=m(p+1),\quad
\pi_0^{e_0}=p,\quad\varepsilon=\pi_0^m .
\]
可在 full-\(p\) 图取 \(\varpi^2=\pi_0\)。
完全消费 R378 §§2–4 仍有效的原曲线几何参数：
\[
z=\frac{a-1}{\varpi^{\,3p(p-1)}},\qquad
w=\frac{a-1}{p^3},\qquad
\boxed{\quad z=\varepsilon^3w .\quad}
\tag{1033.1}
\]
\(z\) 是原 \(c_1\) 处的整完成参数，
\(\widehat O_{\mathcal X,c_1}=R[[z]]\)，
且整个形式环上
\[
\sigma(z)=\xi^{3m}z,\qquad \sigma(w)=w.
\tag{1033.2}
\]
不采用 R378 已被 R575 撤回的旧全局秩零商身份；
本篇的实际目标是 R1029 已独立构造的整类型块。

在 R1032 的同一个尾上用 \(t=\sqrt x\)，令
\[
\lambda_0=\left.\frac{d\bar z}{dt}\right|_Q\in k^\times.
\tag{1033.3}
\]
R378 的原 Dickson 一次项及 tame 三次商证明
\(\lambda_0\ne0\)。它不被设成一。
较高的 \(z(t)\) 项不会降低第一个 \(t\) 次数。

取一个实际类型一的权 \(m\) 整不变微分 \(\Omega\)；
其底 Hodge 向量为 R1032 的 \(L\)。
在原 \(z\) 盘写
\[
\Omega=\sum_{n\ge1}a_nz^{n-1}\,dz .
\tag{1033.4}
\]
R1032 给
\[
a_n\in\pi_0^{4m}R\quad\text{对所有 }n,
\]
并令 \(n_0=4g-1=(p-2)/3\)，有
\[
\boxed{\quad
a_{n_0}\equiv\varepsilon^4
 \kappa_1R_L(1)n_0\sqrt{A_{\rm tail}}\,
                \lambda_0^{-n_0}
     \pmod{\pi_0^{4m+1}} .
\quad}
\tag{1033.5}
\]
这个式子同时保留 R1032 的原 \(\kappa_1,\theta_s\) 与原参数的
\(\lambda_0\)。

## 2. 完整惯性角色给逐系数赋值

由 (1033.2)、\(\sigma\Omega=\xi^m\Omega\)，
\[
\sigma(a_n)=\xi^{m-3mn}a_n.
\]
令 \(r_n\) 为 \(m-3mn\bmod e_0\) 的最小非负代表，则
\[
a_n=\pi_0^{r_n}c_n,\qquad c_n\in W(k).
\]
代入 \(z=\varepsilon^3w\) 并除以 \(\varepsilon\)，得到
\[
\varepsilon^{-1}\Omega
 =\sum_{n\ge1}p^{d_n}c_n w^{n-1}\,dw,\qquad
\boxed{\quad d_n=\left\lceil\frac{3n-1}{p+1}\right\rceil.\quad}
\tag{1033.6}
\]
有限未分歧底域时，将 \(W(k)\) 读作该实际整数环即可。
这里明确取了最小剩余角色及向上取整，没有漏掉一个 \(p^{-1}\)。

定义以同一个 \(c_1\) 为零常数的原 Abel-log primitive
\[
H_\Omega(w)=\frac1{p\varepsilon}
                 \int_{c_1}^{P(w)}\Omega .
\tag{1033.7}
\]
其 \(w^n\) 系数的下界为
\[
\boxed{\quad
v_p([w^n]H_\Omega)\ge d_n-1-v_p(n).
\quad}
\tag{1033.8}
\]
这是对完整积分的估计，不能先从微分的约化猜 primitive。

## 3. 所有越过 \(n_0\) 的项，包括 \(p\) 倍次数

对 \(1\le n\le n_0<p\)，有 \(d_n=1\)，而 \(n\) 为单位；
所以这些 primitive 系数整。

还有一个必须单独处理的次数
\[
n=4g=n_0+1=(p+1)/3 .
\]
此时 \(d_n=1,r_n=m\)。
但 (1033.4) 的实际 normal 下界是 \(a_n\in\pi_0^{4m}R\)；
同一个精确角色迫其改进为
\[
a_{4g}\in\pi_0^{e_0+m}R .
\tag{1033.9}
\]
因此这个次数在除 \(p\varepsilon\) 后仍含一个额外 \(p\)。

若 \(n\ge4g+1\) 且 \(p\nmid n\)，则 \(d_n\ge2\)，
(1033.8) 已给一个额外 \(p\)。

最后令 \(r=v_p(n)\ge1\)，于是 \(n\ge p^r\)。
对所有 \(p>3,r\ge1\) 有
\[
3p^r-1>(r+1)(p+1).
\tag{1033.10}
\]
例如 \(p^r\ge pr\)，并且
\(3pr-1-(r+1)(p+1)=(2r-1)p-r-2>0\)；
\(p^r\ge pr\) 可由 \(p^{r-1}\ge r\) 直接归纳。
故 \(d_n\ge r+2\)，从而
\[
d_n-1-v_p(n)\ge1.
\]
这排除了所有 \(w^p,w^{2p},\ldots\) 项的遗漏。
右侧的一般下界随 \(n\) 趋向无穷，故完整 primitive 收敛于 Tate 代数，
并满足
\[
\boxed{\quad
H_\Omega\in W(k)\langle w\rangle,\qquad
\deg\overline{H_\Omega}\le n_0 .
\quad}
\tag{1033.11}
\]
没有把 \(O(\pi_0)\) 当成 \(O(p)\)；
整数赋值来自 (1033.6) 的真正未分歧系数。

## 4. 原最高系数及共同尺度的准确性

将 (1033.5) 代入 primitive，使用
\[
4m+3mn_0=e_0+m,\qquad n_0<p,
\]
得到
\[
\boxed{\quad
[w^{n_0}]\overline{H_\Omega}
 =\kappa_1R_L(1)\sqrt{A_{\rm tail}}\lambda_0^{-n_0}
 =\frac{2\kappa_1\sqrt{A_{\rm tail}}}{m}
      \lambda_0^{-n_0}
         \sum_s\frac{L_s\theta_s}{(1-s)^2}.
\quad}
\tag{1033.12}
\]
所有共乘因子是原单位。

原 \(S\) 非空，且每个 \(\theta_s\) 与 \(1-s\) 都为单位。
所以 R1032 的线性泛函在整个底 Hodge 空间上非零。
可选一个整权 \(m\) 基，其中某个向量有
\([w^{n_0}]\overline{H_\Omega}\ne0\)。
因此整个实际类型块的规范轮廓最高次数准确为 \(n_0\)，
其未除去 \(p\) 的共同系数赋值准确为
\[
\boxed{\quad M=1\quad\text{在 }\varepsilon^{-1}
              \text{ 归一的原 Abel-log 上}.\quad}
\tag{1033.13}
\]
不声称每个线性组合均有单位最高系数。

## 5. 实际 formal 坐标与 log 的同一轮廓

R1029 的整群幂等元给原形式群的实际直和因子
\(\widehat{\mathcal G}_1\)。
取整参数 \(Y_i\)，其零截面的一次项对应整 Hodge 基 \(\Omega_i\)；
对完整 tame 惯性作单位平均，可令
\[
\sigma Y_i=\xi^mY_i
\]
为形式环上的准确恒等式。
这只使用已证整类型块和 tame 下降，
没有移用旧 CM 通道的额外 \(\mathcal O_{K_p}\)-作用。

对原 Abel 点 \(P(w)-c_1\) 先在原 \(J\) 的形式群中取像，
再施加真正 \(e_1\)。
在 \(w\) 的单位盘上，\(z=\varepsilon^3w\) 已约化到 \(c_1\)，
所以此操作有定义。
参数拉回写 \(Y_i(P(z))=\sum_{n\ge1}b_{i,n}z^n\in R[[z]]\)，
常数项为零。
与 §2 同一个角色计算给
\[
\boxed{\quad
\varepsilon^{-1}Y_i(P(w))\in pW(k)\langle w\rangle .
\quad}
\tag{1033.14}
\]
这里没有积分分母；\(d_n\ge1\) 对每个 \(n\ge1\) 已足够。

整形式群的不变微分给 formal-log 的齐次次数 \(d\) 项
系数赋值至少 \(-v_p(d)\)：
可沿径向积分整不变微分，唯一所需分母是总次数 \(d\)。
由 (1033.14)，每个输入 \(Y_i\) 的赋值至少
\(1+1/(p+1)\)。所以对 \(d\ge2\)，除 \(p\varepsilon\)
后非线性项的赋值至少
\[
(d-1)\left(1+\frac1{p+1}\right)-v_p(d)>1 .
\tag{1033.15}
\]
界随 \(d\) 趋向无穷，足以保证同一单位盘上的收敛和
\[
\boxed{\quad
\frac{\log_i(P(w))-Y_i(P(w))}{p\varepsilon}
                 \in pR\langle w\rangle .
\quad}
\tag{1033.16}
\]
因此 formal 坐标与 (1033.7) 的真正积分在该规范下具有
同一模 \(p\) 轮廓；(1033.13) 也给实际 formal map 的
共同尺度 \(M=1\)。

## 6. 后继还须保留的实际问题

R378 已登记的整解析圆盘、候选深度及全部 tail 证书，可在
本篇已核的 \(k_i=1,M=1\) 处消费，不重新推算或扫描。
本篇新取得的是那个条件框架在原真实整类型块上的准确尺度，
以及 (1033.12) 的实际最高单位系数来源。

最高系数单位并不说明最低非零系数单位。
低于 \(n_0\) 的系数还可能影响原 \(v_p(w)>0\) 子盘的零点；
不能据次数界独断只有 \(w=0\) 一个零点。
同样，原 \(\mathbf Q\)-简单商的 Néron 格，
以及真正饱和 \(F_0\log\beta\) 空间的消去，
可能带来额外的相对尺度。
本篇不把整个类型块的 \(M=1\) 自动传给它们。

后继须继续求原低系数或实际消去后的单位条件，
并控制同一有理盘的全方程。
R1003/O0 的完整全局覆盖亦仍开放。

## 来源与审核

- [R378](R378-actual-cm-disc-parameter-and-uniform-integral-tail.md)，
  §§2–4 的原参数、Dickson 单位及其有理下降；
  §§5–7 的一般角色系数与完整尾界仅按本篇已重核的实际目标消费。
  不使用被 R575 撤回的旧秩零商身份。
- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md)，
  原整 \(p\)-可除群直和因子和纯权 \(m\) Hodge 格。
- [R1032](R1032-original-lowest-type-complete-CM-normal-jet-functional.md)，
  完整第 \(4m\) normal 下界、原最高项及全部节点与 Serre 尺度。

global_route 与 root 纸核原参数、\(\lambda_0\) 次幂、
所有 normal 与 Taylor 次数、向上取整、特殊次数 \(4g\)、
全部 \(p\) 倍积分次数及多变量 formal-log 的分母与收敛。
没有数学执行或旧窗口重算。
Serre 主目标仍 OPEN。
