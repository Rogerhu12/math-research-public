# R52. 惰性中央权的固定 prime-diagonal 公式及真实连接

日期：2026-11-12。**状态：公式和两个范围限制均已证明；目标对角的无穷非零仍开。**

## 1. 无穷性所需的一个完全明确系数

令
$$
F(v)=\sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(4n+1)}v^n,\qquad
H(v)=\sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(4n+3)}v^n,
$$
并唯一规定
$$
\frac{\Theta'}{\Theta}=\frac{H(v)}{4\sqrt{1-v}},\qquad\Theta(0)=1.
$$
置
$$
P(v)=v+\frac35v^2-\frac15v^3+\frac15v^4,\qquad
\boxed{\Xi(v)=\frac{(\Theta(v)^{17}P(v))'}{F(v)}\in\mathbb Q[[v]].}
\tag{1}
$$
这些全是固定特征零级数，不随 $p$ 重新选择。

对每个惰性 $p=4r-1\ge7$，$[v^{r-1}]\Xi$ 为 $p$ 整数，且 R51 的
实际中央因子满足
$$
\boxed{
b_{p+1}\equiv4\cdot17^{r-1}[v^{r-1}]\Xi(v)\pmod p.
}
\tag{2}
$$
因此由 R50–R51，
$$
\boxed{
[v^{(p-3)/4}]\Xi(v)\not\equiv0\bmod p
\ \Longrightarrow\ \Sha(E_{17}/\mathbb Q)[p^\infty]\text{ 有限}.
}
\tag{3}
$$
若能证明 (3) 左端对无穷多个惰性素数成立，就完成本题。
本文没有证明这一非零性。

## 2. 保留实际 theta 的 Lagrange 反演

在固定二重覆盖上取
$$
u=x^{-1/2},\qquad s=-yu^3,\qquad s^2=1-Du^4,\quad D=17,
$$
并选原点处 $u=z+\cdots,s=1+\cdots$ 的分支。
于是 $du/dz=s$，所以
$$
z=uF(v),\qquad v=Du^4.
\tag{4}
$$
由 $\vartheta=\sigma/u$ 直接求两次对数导数，
$$
(\log\vartheta)'=\zeta-s/u,\qquad
(\log\vartheta)''=Du^2.
$$
原点处的一次导数为零，积分后得到
$$
(\log\vartheta)'=Du^3H(v),\qquad
\vartheta(z(u))=\Theta(v).
\tag{5}
$$
这是实际 sigma/theta 函数的恒等式，没有将连接换成任意代数近似。

R51 的多项式在此坐标中正好为
$$
A_D(z(u))=D^{-1}\Theta(v)^{17}P(v).
\tag{6}
$$
Lagrange 反演给
$$
b_{4r}
 =\frac{4D^{r-1}}{4r}[v^{r-1}]
       (\Theta^{17}P)'F^{-4r}.
\tag{7}
$$

取 $4r=p+1$。必须先核分母：
$F$ 到次数 $r-1$ 的分母都与 $p$ 互素；
$H$ 的首个 $p$ 分母恰在次数 $r-1$，
故 $\Theta$ 的首个可能 $p$ 分母在次数 $r$。
$P(0)=0$ 使这个系数不进入
$(\Theta^{17}P)'$ 的第 $r-1$ 项。
因此 (7) 的全部必要截断均整。
在此截断内
$$
F(v)^p\equiv1\bmod(p,v^r),\qquad (p+1)^{-1}\equiv1\bmod p.
$$
(7) 遂化为 (2)，也证明其整性。

## 3. 整条 $\Xi$ 不是 D-finite

此结论只限制对整个级数的解释，不排除所选 prime diagonal 另有特殊
Frobenius 公式。

更一般地，非零多项式 $Q$ 满足 $Q(0)=0$ 时，
$$
\Xi_Q=(\Theta^{17}Q)'/F
$$
不满足任何非零的有限阶 $\mathbb C(v)$ 系数线性微分方程。

证明使用实际周期分支。令 $\ell$ 是覆盖曲线上 $u,s$ 的一个非零实周期。
沿对应周期环，$z$ 变成 $z+n\ell$。继续后的分支为
$$
\Xi_{Q,n}(v(z))=
\frac{\frac d{dv}\bigl(\vartheta(z+n\ell)^{17}Q(v(z))\bigr)}
 {(z+n\ell)/u(z)}.
\tag{8}
$$
分母 $F=z/u$ 也必须同时继续。

若 $Q(v)=q_jv^j+\cdots$、$q_j\ne0,j\ge1$，
在 $z=-n_0\ell$ 处令 $w=z+n_0\ell$。
由于 $u=w+\cdots,v=Dw^4+\cdots$，
$n=n_0$ 的分支从 $w^{4j-4}$ 开始，系数非零；
其他 $n$ 的分子仍至少从此次数开始，
但分母 $(w+(n-n_0)\ell)/u(w)$ 有一阶极点，
故这些分支至少从 $w^{4j-3}$ 开始。
任意有限线性关系在该点的唯一次数比较都迫使
$n_0$ 的系数为零。所有分支因而任意有限组都线性无关。

拉回后的各项在 $z$ 平面亚纯。
周期路径可避开假定 ODE 的有限奇点之离散逆像；
一个有限阶线性方程的继续分支却必须在有限维解空间里。
这与上述线性无关矛盾，证明非 D-finite。

## 4. sigma 连接不能被直接删成固定常数矩阵

在惰性剩余特征 $p$ 的曲线函数域上，
$$
\delta^p=0,\qquad
\kappa=\delta^{p-1}X
 =-\frac12(-1)^r\binom{2r}{r}D^r\ne0.
$$
引入真实 zeta 变量 $U$、$\mathcal DU=-X$，并在曲线函数上
$\mathcal D=\delta$。则
$$
\mathcal D^p=-\kappa\partial_U,\qquad
B=U^p-\delta^{p-2}X,\qquad\mathcal DB=-\kappa.
$$
实际截面可写成 $\sigma^{17}\sqrt X\,R(X^2)$。
在固定可分覆盖及避开零极点的开集上，其自然算子为
$$
\mathcal L=\mathcal D+17U+
           \delta\log(\sqrt X\,R(X^2)).
$$
有理 gauge 与 Bell–Jacobson 恒等式准确给
$$
\boxed{\mathcal L^p=-\kappa\partial_U+17B,\qquad
       [\partial_U,\mathcal L]=17.}
\tag{9}
$$
gauge 不依赖 $U$；$\delta^p=0$ 在可分代数扩张上仍成立，所以无额外项。

若在这样的可分覆盖上有代数 $U_0$ 满足 $\delta U_0=-X$，
便会同时有 $\delta^pU_0=0$ 和 $-\kappa\ne0$，矛盾。
若要在有限维常数域向量空间 $W$ 上同时实现 (9) 的两个算子，
取迹则给 $0=17\dim W$，所以 $p\mid\dim W$。
因此这套自然算子的正维常数矩阵模型不能有与 $p$ 无关的固定维数。

这里未否定半线性 Frobenius、不同的代数几何对象，
或只针对 (2) 所选系数的另一个恒等式。
当前需要的仍是这种实际比较及随后的无穷非零证明。

### 全文与依赖

- [固定惰性对角、全分支及连接全文](../notes/2026-11-12-inert-theta-diagonal-and-curvature.md)，
  已由根端独立复核。
- R51 给准确 $P$ 和单位缩放；R50给实际 Selmer 充分判据。
- R38及[惰性中央平移](../notes/2026-11-12-central-diagonal-inert-shift.md)
  给上述 $\delta,\mathcal D,\kappa$ 的真实算子恒等式。
