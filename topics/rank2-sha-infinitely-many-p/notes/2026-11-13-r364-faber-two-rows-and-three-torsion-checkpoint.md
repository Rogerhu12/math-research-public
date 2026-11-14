# R364 工作检查点：原两 Faber 行的反序核与三挠变换

日期：2026-11-13。本文件保存 R360 后仍在进行的推导，不新增结果编号。
原两个指定观察的联合非零尚未证明；没有把完整 Hankel 矩阵可逆、
真实截断唯一或某个三次行单位替代这件事。

已完成输入为 [R349](../results/R349-critical-faber-cubic-row-and-complete-norm-three-projections.md)、
[R354](../results/R354-original-hirota-bottom-unit-recursion-and-complete-truncation.md)、
[R355](../results/R355-actual-hirota-isogeny-and-reduced-truncation-ideal.md)、
[R360](../results/R360-original-torsion-jacobian-and-two-faber-transposes.md)。
保持 $p=6s+1>7$、$E_b:y^2=x^3+b$、$b=17$，
$R(U;t)=\sum r_n(t)U^n$、真实 $t_*=-H^3\epsilon_3/24$。

## 1. 已排除的 norm-three 常数导数候选

完整 norm-three 的常数关系是
$$N_0(t)=r_s(t)^3+24t,\qquad N_0(t_*)=0.$$
它在同一真实底部族中的导数准确为
$$
N_0'(t_*)=24\left(1-3t_*\frac{r_s'(t_*)}{r_s(t_*)}\right).
$$

仅复用已经出现的三个有限纤维，不作新的素数扫描：

| $p$ | $s$ | $t_*$ | $r_s$ | $r_s'$ | $N_0'(t_*)$ | $a_p(E_{-1/4})$ |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 4 | 6 | 5 | 5 | 5 |
| 31 | 5 | 13 | 27 | 28 | 4 | 4 |
| 37 | 6 | 17 | 36 | 9 | 14 | 11 |

最后一列的准确曲线是 $E_{-1/4}:y^2=x^3-1/4$，不是 $E_{-4}$。
直接有限点数分别为 $9,28,27$，所以迹分别为 $5,4,11$。
因此由前两个纤维提出的
$N_0'(t_*)\equiv a_p(E_{-1/4})$ 候选，在原 $p=37$ 纤维已被否定。

为复算保存 $p=31,37$ 的完整底部值及参数导数。每个括号为
$(r_n(t_*),r_n'(t_*))$，从 $n=0$ 开始：
$$
\begin{aligned}
p=31:\quad&
(1,0),(13,1),(10,4),(10,25),(7,5),(27,28),\\
& (0,5),(0,6),(0,21),(0,29),(0,1);\\
p=37:\quad&
(1,0),(17,1),(23,36),(33,0),(21,36),(5,6),(36,9),\\
& (0,31),(0,2),(0,22),(0,16),(0,14),(0,1).
\end{aligned}
$$
这些值由 R354 的同一有理递推在双数中逐项计算，未更换 kernel。

## 2. 原 Faber 转置权的精确简化

R360 的两个真实椭圆对数核是
$$
h_O(T)=\sum_{n\ge0}\frac{(1/2)_n}{n!(6n+1)}T^n,\qquad
h_Q(U)=\sum_{n\ge0}\frac{(-1)^n(1/2)_n}{n!(3n+1)}U^n.
$$
原 Faber 系数为
$$
L_{i,n}=(-1)^{n-i}[T^{n-i}]
h_O(T)^{6i-1}(1-T)^{-1/2}.
$$
因为
$$h_O+6T h_O'=(1-T)^{-1/2},$$
对 $1\le i\le n\le s$ 有准确等式
$$
\boxed{
L_{i,n}=(-1)^{n-i}\frac ni
[T^{n-i}]h_O(T)^{6i}.
}
$$
证明只需把右边的原乘积写成
$h_O^{6i}+(T/i)(h_O^{6i})'$，再取指定系数。

使用 R360 的反序变量
$$q_h=(-1)^h(s-h)r_{s-h},\qquad 0\le h\le s-1,$$
得到
$$
\boxed{
\frac{(-1)^h}{s-h}L_{i,s-h}
=\frac{(-1)^{s-i}}i
[T^{s-h-i}]h_O(T)^{6i}.
}
$$
若
$$q_{\mathrm{rev}}(T)=\sum_{h=0}^{s-1}q_hT^h
=(-T)^{s-1}R_*'(-1/T),$$
则原 Faber 坐标准确为
$$
\boxed{
\beta_i=\frac{(-1)^{s-i}}i
[T^{s-i}]h_O(T)^{6i}q_{\mathrm{rev}}(T).
}
$$
因而 $\beta_1$ 在真实 beta-Hankel 对偶中读取的是反序
$h_O^6$ 的整行，不是仅仅读到最高质量 $r_s$。
全部所读次数至多 $s-1$，所以这些变换都在已支付的单位分母范围；
没有跨过原点第一次 $p$ 分母。

## 3. 两种椭圆对数核之间的真实三挠变换

取 $Q=(0,\beta)$、$\beta^2=b$。在 $O$ 附近写
$$
u=x^{-1/2},\quad r=\beta u^3,\quad v=\sqrt{1+r^2},\quad
x(P)=u^{-2},\quad y(P)=-v/u^3.
$$
真实群律给
$$x(P+Q)=2\beta u(v+r),\qquad
U_Q=\frac{x(P+Q)^3}{b}=8r(v+r)^3.$$
以 $w(Q)=0$、$dw=dx/(2y)$ 取局部椭圆对数。
平移不变性使 $w(P+Q)=z(P)$，故得到形式级数恒等式
$$
\boxed{
h_O(-r^2)=(\sqrt{1+r^2}+r)\,
h_Q\!\left(8r(\sqrt{1+r^2}+r)^3\right).
}
$$
这是原群律的真实相位与分支：两个平方根均在零点取 $+1$，
没有另乘未确定的三次单位。

反向地，在 $Q$ 邻域用 $U=x(P')^3/b$，则
$$
\frac{x(P'-Q)^3}{b}
=\tau(U):=\frac{8(1+\sqrt{1+U})^3}{U^2}.
$$
在归一 $b=1$ 的同一 Faber 变换中作留数换元，得到另一个完整式：
$$
\boxed{
L_{i,n}=2^{3n-6i}
[U^{2(n-i)}]\,
(1+\sqrt{1+U})^{3n}
h_Q(U)^{6i-1}(1+U)^{-1/2}.
}
$$
其中 $w=x(P')h_Q(U)/2$。由 $U=x(P')^3$ 换元的
$1/3$ 与正式留数的三重覆盖系数恰好抵消；没有漏掉 3 的尺度。
$n=i$ 时结果为 1，$(i,n)=(1,2)$ 时给 $-6/7$，与 R360 相同。

## 4. 继续处与尚未支付的步骤

下一步是把第 3 节的真实三挠换元代入 R360 的 Jacobi
Rodrigues 对偶，尝试将两个指定旧行变为可控制的实际边界值。
目前这一步仍带有完整 $h_Q^{6i-1}$ 或 $h_O^{6i}$，
没有证明它们可以消掉，也没有证明边界值为单位。

必须保留原观察
$$
\mathcal L=\frac{b^{s-1}}{r_s}\beta_1,\qquad
\mathcal Q=\frac{b^{s-1}}{r_s^2}
\sum_{i+k=s+1}[-18(i-k)^2-3(s+1)]\beta_i\beta_k,
$$
以及 R349 已支付的
$$
p t_0=-H,\qquad
\mathcal K=486\sum_{i+j+k=2s}ijk\,\alpha_i\alpha_j\alpha_k
=-\eta-\frac92H.
$$
完整 Hankel 行列式为单位、真实截断理想为一个约化点、以及
$\mathcal K$ 的非零都不能直接替代这两个指定观察的联合非零。
实 beta 权的正性也不提供模 $p$ 的正性。

本文件通过 GitHub Contents API 保存小文本；未声称执行了本地
git pull。提交前核对根 README 和课题 README 的内容 blob，
分别仍为 f787a306d90892d8dec765dc59747d60ba39f055、
f8dd8071ac0c2b31f344a40c15ac2a42796bf9af，与已读基准
35e391cd9a73d5a514d252312d3ff61962ddbc70 完全相同。
