# 原六挠 Kronecker 权一平方与临界二次卷积

日期：2026-11-15。会话：serre-public-astra-20261115 / sigma_uniform。

**状态：本文的恒等式已纸面证明；不含新的非消失定理。** 原 primitive / Legendre 同标签三单位和 Serre 一致性主目标仍开放。本文保全一个与原 R683 完全同规范的权一模形式解释，并明确为什么不能把 $X(6)$ 的 genus-one Cartier 直接用作临界单位证明。不运行新的算术，也不重新计算已有素数。

## 1. 原点、原十八项与一个固定权一形式

固定 R683 的全部数据：
$$
E_0:y^2=x^3-1,\qquad dz=\frac{dx}{2y},\qquad
\Lambda=\Omega(\mathbf Z+\zeta\mathbf Z),\quad \Omega>0,
$$
$$
Q_{\delta ij}=(\alpha\zeta^i,\delta\beta)+(\zeta^j,0),
\quad \alpha^3=4,\quad \beta^2=3,\quad
\chi(Q_{\delta ij})=\delta\zeta^{j-i},\quad
C_+=144\beta/\alpha^2 .
\tag{KS1}
$$
这里 $\alpha,\beta$ 取原正实嵌入。设 $\tau_0=\zeta$、$y_0=\Im\tau_0$，
$\mathcal A=\Omega^2y_0/\pi$，并沿固定全六层标记把每个 $Q$ 写成
$$
Q=\Omega(a_Q+b_Q\tau_0),\qquad a_Q,b_Q\in\tfrac16\mathbf Z/\mathbf Z.
$$
选择代表之后，在 $\tau$ 变化时保持这两个有理数不变。权 $\chi(Q)$ 也保持原标记不变；这里没有随模参数任取另一组三挠或二挠点。

用标准奇 theta 定义 Kronecker 函数
$$
\mathscr F(\xi,\eta;\tau)
=\frac{\vartheta'(0;\tau)\vartheta(\xi+\eta;\tau)}
       {\vartheta(\xi;\tau)\vartheta(\eta;\tau)} ,
$$
其在 $\eta=0$ 的留数为 $1$。定义
$$
\mathscr H(\xi,\eta;\tau)
=\sum_Q\chi(Q)e^{2\pi i b_Q\eta}
  \mathscr F(\xi+a_Q+b_Q\tau,\eta;\tau),
$$
$$
E(\tau)=[\xi^0\eta^0]\mathscr H(\xi,\eta;\tau).
\tag{KS2}
$$
因 $\sum_Q\chi(Q)=0$，$\mathscr H$ 的 $\eta^{-1}$ 项消失；
非零六挠点保证它在 $\xi=0$ 没有极点。因此这里是实际双变量正则 Taylor 系数。

单个常数项为
$$
\frac{\vartheta'(a_Q+b_Q\tau;\tau)}
     {\vartheta(a_Q+b_Q\tau;\tau)}
       +2\pi i b_Q .
\tag{KS3}
$$
theta 的模变换和全六层固定标记给出它的权一变换式：
$\Gamma(6)$ 固定每个 $Q$，准周期修正正由 $2\pi i b_Q$ 消去。
各 cusp 上把 $b_Q$ 取在 $[0,1)$，theta 的乘积展开显示没有负次
$q^{1/6}$；当 $b_Q=0$ 时，$a_Q\notin\mathbf Z$ 保证分母的常数非零。
故
$$
E\in M_1(\Gamma(6)).
\tag{KS4}
$$
此处 $E$ 允许通常的固定 $2\pi i$ 归一；下文保留这个归一本身，不另把它设置为代数单位。

## 2. 保留原 Gaussian 的 mixed-heat 比较

Brown–Levin 的 Kronecker mixed heat equation 是
$$
2\pi i\,\partial_\tau\mathscr F
=\partial_\xi\partial_\eta\mathscr F .
\tag{KS5}
$$
对 (KS2) 的每项，它仍成立：$\tau$ 求导的
$b_Q\partial_\xi\mathscr F$，恰由右侧求导指数
$e^{2\pi i b_Q\eta}$ 所产生的项匹配。于是
$$
[\xi^m\eta^m]\mathscr H
=\frac{(2\pi i)^{2m}}{(m!)^2}\,\theta_q^m E,
\qquad \theta_q=(2\pi i)^{-1}\partial_\tau.
\tag{KS6}
$$

在原 CM 点，准周期是 $\eta_\lambda=\overline\lambda/\mathcal A$。
sigma / theta 的同规范关系因此逐项给出
$$
H^+(z,w)
=\Omega^{-1}e^{zw/\mathcal A}
     \mathscr H(z/\Omega,w/\Omega;\tau_0).
\tag{KS7}
$$
确实，原 R683 指数 $e^{-\overline Qw/\mathcal A}$ 与 sigma 比值的
$Q$ 项合成 $e^{2\pi i b_Qw/\Omega}$；剩余交叉指数是
$e^{zw/\mathcal A}$。没有删掉原 Gaussian。

置
$$
\ell=\frac{2\pi i}{\Omega},\qquad
\delta_k=\theta_q-\frac{k}{4\pi\Im\tau},
\qquad
\delta_k^m=\delta_{k+2m-2}\cdots\delta_{k+2}\delta_k .
$$
因为 $zw/\mathcal A=-\ell^2zw/(4\pi y_0)$，把 (KS6) 乘回 (KS7) 的指数，
与 Maaß 迭代展开逐项比较，得到
$$
\boxed{
[z^mw^m]H^+(z,w)
=\frac{\Omega^{-1}\ell^{2m}}{(m!)^2}
       \delta_1^m E(\tau_0).
}
\tag{KS8}
$$
可直接核对 Maaß 展开中的第 $r$ 项：它在右侧乘
$(m!)^2/(r!(m-r)!^2)$，正是交叉指数贡献的组合系数。
这证明所有 $m$ 的恒等式，不是低阶拟合。

为了完整写卷积，在此临时把 R683 的定义扩展为
$$
C_{m+1}:=\frac{(-3)^m m!}{C_+}[z^mw^m]H^+,\qquad m\ge0 .
\tag{KS9}
$$
原 CM 旋转把十八项置换，并乘总权 $\zeta^{-(2m+1)}$；
因此 $C_{m+1}=0$，除非 $m\equiv1\pmod3$。
在非零允许类上 (KS9) 恰是 R683 的原 $C_k$，无新相位。
特别 $C_1=0$。由 (KS8)：
$$
\boxed{
\delta_1^m E(\tau_0)
=\Omega C_+\,m!(-3)^{-m}\ell^{-2m}C_{m+1}.
}
\tag{KS10}
$$

## 3. 平方产生原临界二次卷积

Maaß 导子的 Leibniz 法则保留各因子的实际权，故
$$
\delta_2^n(E^2)
=\sum_{m=0}^n\binom nm
       (\delta_1^mE)(\delta_1^{n-m}E).
$$
代入 (KS10) 后所有组合阶乘准确约去，得
$$
\boxed{
\frac{(-3)^n\ell^{2n}}
     {(\Omega C_+)^2n!}
     \delta_2^n(E^2)(\tau_0)
=\sum_{m=0}^n C_{m+1}C_{n-m+1}.
}
\tag{KS11}
$$
右侧是原有理数；这个等式也规定左侧的代数归一。
后面在模 $p$ 讨论时约化的是此有理数恒等式，不是先给
$\Omega,\ell$ 或非全纯导子各自指派 supersingular 点值。

令
$$
p=6N+5\ge41,\qquad n=p-6=6N-1.
$$
因为只有 $m\equiv1\pmod3$ 保留，而 $n$ 为奇数，两个指标一为
$1\bmod6$、一为 $4\bmod6$。逐对分组，准确得到
$$
\sum_{m=0}^{p-6}C_{m+1}C_{p-5-m}
=2\sum_{i=0}^{N-1}C_{6i+5}C_{p-9-6i}.
\tag{KS12}
$$
所有这些 $C$ 的下标都在 R683 的 $p$ 整范围内。

保持 R697 / R770 的原截面
$$
F=x\sigma^6=z^4\sum_{i\ge0}f_i z^{6i},\qquad
G=-xy\sigma^6=z\sum_{j\ge0}g_jz^{6j}.
$$
对 $j=N-1-i$、$h=6i+7$，置
$$
m_1=6i+4=h-3,\qquad m_2=6j+1=p-h-3,\qquad m_1+m_2=p-6.
$$
R697 的平方公式逐项为
$$
C_{m_1+1}=3\,2^{-m_1}m_1!f_i^2,\qquad
C_{m_2+1}=-2^{-m_2}m_2!g_j^2.
\tag{KS13}
$$
这里 $m_2$ 为奇数，Wilson 公式给
$$
m_1!m_2!
=\frac{1}{(m_1+1)(m_1+2)(m_1+3)(m_1+4)(m_1+5)}
=\frac{1}{Q_h}\pmod p,
$$
$$
Q_h=(h-2)(h-1)h(h+1)(h+2).
\tag{KS14}
$$
本范围 $7\le h\le p-4$，所以这五个因子全部非零；
没有负阶乘或先模 $p$ 再除零的步骤。又
$2^{-(p-6)}=32$。结合 (KS11)--(KS14)，证明
$$
\boxed{
\frac{(-3)^{p-6}\ell^{2p-12}}
 {(\Omega C_+)^2(p-6)!}\,
\delta_2^{p-6}(E^2)(\tau_0)
\equiv
-192\sum_{i=0}^{N-1}\frac{f_i^2g_{N-1-i}^2}{Q_{6i+7}}
\pmod p.
}
\tag{KS15}
$$
左侧按 (KS11) 的有理归一约化；$192$ 和全部 $Q_h$ 在这些素数处为单位。

这是一条原未筛二次卷积恒等式。右侧可能发生有限域相消；
本文没有证明它非零。即使它非零，也只能推出某个未筛
$f_i g_{N-1-i}\ne0$，不能略过 $(6i+7,p+1)=1$ 或
$P_{6i+6}(1/s)\ne0$。

## 4. $X(6)$ 上的标量 Cartier 并未提供临界单位

Kaneko–Kuwata 的实际模型为
$$
X(6):\quad Y^2=X^3+1.
\tag{KS16}
$$
这里的 $X,Y$ 是这一全六层模曲线的坐标，不是 R812 的固定判别式
辅助坐标，也不是原 $E_0$ 的椭圆坐标。

更具体地，$\eta^4$ 是 $\Gamma(6)$ 的权二 cusp form：
其有限乘子在 $\Gamma(6)$ 上为一；每个 cusp 的宽度为六，
故其局部阶均为一；在上半平面没有零。$X(6)$ 的 genus 为一，
十二个 cusp 给出这个 cusp divisor。因而
$$
E^2/\eta^4\in\mathbf C(X(6))
\tag{KS17}
$$
只有 cusp 上至多简单的极点。权二微分 $E^2d\tau$ 因此是该曲线上
有理的第三类微分。这确实允许对该标量微分使用几何 Cartier。

但是 (KS15) 提取的是 Maaß 迭代的第 $p-6$ 项。令
$$
u=\frac{\tau-\tau_0}{\tau-\overline{\tau_0}},\qquad
v=\tau_0-\overline{\tau_0}=2iy_0 .
$$
直接 Taylor 展开给
$$
[u^r]\bigl((1-u)^{-k}f(\tau(u))\bigr)
=\frac{(-4\pi y_0)^r}{r!}\delta_k^r f(\tau_0).
\tag{KS18}
$$
因为 $d\tau=v(1-u)^{-2}du$，对 $f=E^2$，
$$
[u^{p-1}]\frac{u^5E(\tau(u))^2\,d\tau}{du}
=v\,\frac{(-4\pi y_0)^{p-6}}{(p-6)!}
       \delta_2^{p-6}(E^2)(\tau_0).
\tag{KS19}
$$

式 (KS19) 中需要的是 $u^5E^2d\tau$ 的 Cartier 系数。
Cayley 参数 $u$ 不下降为 $X(6)$ 的有理函数：它是 $\tau$ 的可逆
Möbius 函数，任何非平凡 $\Gamma(6)$ 模变换都会改变它。
因此不能把 (KS17) 的标量 Cartier 结论直接移到 (KS19)。
如用 Gauss–Manin 水平周期表示 $u$，就必须保留这一五次周期因子
及其连接；把它替换成 $X(6)$ 上某个任取的代数局部参数会改变
所提取的原系数。这正是此路线尚缺的比较，本文没有把它补成非消失。

同样，$\theta_q^{p-1}$ 的 Fourier 系数 Frobenius 恒等只能控制其本身。
对权二形式，quasimodular 公式
$$
\partial_{E_2}\theta_q^r f
=\frac{r(r+1)}{12}\theta_q^{r-1}f
$$
在 $r=p-1$ 的首系数已为零；它不能在模 $p$ 中反除这个零因子，
以恢复五阶以下的 (KS15)。这不是一个可由未保留的 $p$ 分母消去的步骤。

## 5. 原来源及边界

- [R683](../results/R683-even-weight-Cartier-channel-and-actual-r3.md)，
  (683.1)--(683.4)、(683.11)--(683.16)：原十八项、字符、
  $C_+$、对角系数及 $p$ 整范围。
- [R697](../results/R697-original-sigma-six-sections-and-integral-square-roots.md)，
  (697.2)--(697.3)：两类原平方常数。
- R770：原同标签指标 $h=6i+7$、$j=N-1-i$ 与实际
  primitive / Legendre 三因子。
- Francis Brown and Andrey Levin,
  *Multiple elliptic polylogarithms*, §3.4, Proposition 5(ii),
  https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2011/2011_063.pdf .
  此处只用原 Kronecker mixed heat equation；(KS6)--(KS15) 的尺度在正文推导。
- Masanobu Kaneko and Masato Kuwata,
  *Elliptic normal curves of even degree and theta functions*, §8,
  https://www2.math.kyushu-u.ac.jp/~mkaneko/papers/KKtheta.pdf ，
  PDF 第 32 页：实际 $X(6)$ 模型、eta 坐标与群作用。
- Maaß 迭代的通用展开可对照 Larson–Smith,
  https://arxiv.org/pdf/1406.2999 ，式 (9)。本文的 (KS8)、(KS18)
  也由指数展开直接证明，不使用该文仅针对全模群的超奇异高阶整除定理。

本篇既没有把这个全层权一模形式识别成原 Jacobian 的 Hom，也没有
把非零的全局 $E^2$ 当成指定 supersingular Taylor 系数非零。
下一步若使用 (KS15)，仍须给出保留原同标签筛选的实际非消失证明。
