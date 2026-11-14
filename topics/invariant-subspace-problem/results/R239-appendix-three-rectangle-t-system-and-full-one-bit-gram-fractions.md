# R239 附录：三矩形 T-system、异常位的完整分式矩阵与底测度障碍

- 日期：2026-11-13。
- 作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。
- 状态：本文给出的 T-system、全高度双线性分式 Gram、完整 Hessian 修正、缺失次数零的真实协方差/秩一交叉项及两个反例均为精确结论；尚未从它们证明一个异常位的任意高度矩阵比较。已付整个高度二、三、四，普通 ISP 仍开。
- 输入：[两权全高度完整 Schur/MP 定理及自足 Hankel–Jacobi / Schur–Toda 证明](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md)，以及[异常位全高度二维 shear](R239-appendix-two-weight-groups-one-exceptional-full-shear-and-height-two-bound.md)。
- 署名：单 Schur Toda 恒等式的出处为 Suvrit Sra, *Monotonicity of Turán-ratios of symmetric polynomials*, v1 (2026-10-07), §2；[作者官方页](https://suvrit.github.io/papers/sym-turan/)。该恒等式的完整证明已在仓库给出。本稿不把该恒等式或 Sra 的导数单调性登记成新结果。

## 1. 三族的形状、变量数和索引

考虑普通短串长度 $q$、普通长串长度 $L\ge q$、一条异常串，长串权归一化为一，另两个权平方为 $z,w>0$。二维分支写成
$$
t=q-\delta\ge1,\qquad L=q+h-1-2\delta,
\quad0\le\delta\le q-1,\quad h\ge2\delta+1.
$$
这里 $h\ge2$。写 $\Theta=z\partial_z=\partial_\theta$，$\theta=\log z$，并令
$$
C=q!/L!.
$$
三族 Schur 多项式的准确参数是
$$
\boxed{
S_j=s_{(t^{\delta+1})}(z^{[j]},1^{[h+1-j]}),\qquad 0\le j\le h+1;
}
\tag{1.1}
$$
$$
\boxed{
P_j=s_{((t-1)^{\delta+2})}(z^{[j+1]},1^{[h+2-j]}),\qquad 0\le j\le h+1;
}
\tag{1.2}
$$
$$
\boxed{
M_j=s_{((t+1)^\delta)}(z^{[j]},1^{[h-1-j]}),\qquad0\le j\le h-1.
}
\tag{1.3}
$$
因此上族 $P$ 的总变量数是 $h+3$，其重复指数比标号多一；下族 $M$ 的总变量数是 $h-1$。$t=1$ 时上族的零宽矩形解释为一；$\delta=0$ 时下族的空形也为一。全部合法多项式在 $z>0$ 严格正。

两个旧两权首一最小范数序列准确为
$$
\boxed{a_j=C\,j!(h+1-j)!\,z^{\delta+1}\frac{P_j}{S_j},\quad0\le j\le h+1,}
\tag{1.4}
$$
$$
\boxed{b_{j-1}=C\,(j-1)!(h-j)!\,z^\delta\frac{S_j}{M_{j-1}},\quad1\le j\le h.}
\tag{1.5}
$$
$a$ 来自相对出生 $t-1$、缺失次数 $\delta+1$、高度 $h+1$；$b$ 来自相对出生 $t$、缺失次数 $\delta$、高度 $h-1$。这些公式均保留真实边段强制根，不能在下族使用越界重复指数。

## 2. 一个精确的三矩形 T-system

**命题。** 对每个 $1\le j\le h$，作为 $z$ 的多项式恒等式，
$$
\boxed{S_j^2-S_{j-1}S_{j+1}=(z-1)^2P_jM_{j-1}.}
\tag{2.1}
$$

**证明。** 令 $f_j=\log S_j$。完整强制根消元后，高次首一范数 $a_j$ 与低次范数 $b_{j-1}$ 共用同一个有限正权，只差一个正交多项式次数。因此 Hankel–Jacobi 恒等式准确给
$$
f_j''=a_j/b_{j-1}.
\tag{2.2}
$$
其有限行列式证明是：若 $Z_d$ 为权 $z^x\rho(x)$ 的 $d$ 阶矩行列式，则
$$
(\log Z_d)''=Z_{d-1}Z_{d+1}/Z_d^2=\mathfrak h_d/\mathfrak h_{d-1}.
$$
强制根和平移引入的 $z$ 单项式对二阶对数导数无贡献；旧固定矩形秩对偶恰把相应 $Z_d$ 化为 $S_j$ 乘这样的单项式和常数。这支付 (2.2)，包括 $j=1,h$。

将 (1.4)、(1.5) 代入，得到
$$
f_j''=j(h+1-j)z\frac{P_jM_{j-1}}{S_j^2}.
\tag{2.3}
$$
另一方面，已自足证明的单 Schur Toda 恒等式，取总变量数 $h+1$，给
$$
f_j''=\frac{z}{(z-1)^2}j(h+1-j)
\left(1-\frac{S_{j-1}S_{j+1}}{S_j^2}\right).
\tag{2.4}
$$
对 $z>0,z\ne1$ 消去相同正因子即得 (2.1)。两边都是多项式，故延拓到 $z=1$，不需要在 $z=1$ 使用奇异商。证毕。

这条恒等式比“每个矩形族各自满足 Toda”更紧：它准确联结实际 MP 中相邻两个出生层的范数。它单独尚不支付异常位的二维 shear 费用。

## 3. 全部高度位置上的两个线性 $w$ 多项式

对 $0\le n\le h$ 定义
$$
R_n=S_nS_{n+1},\qquad
W_n=S_n\Theta S_{n+1}-(\Theta S_n)S_{n+1},
\quad L_n=C\,n!(h-n)!\,z^\delta.
\tag{3.1}
$$
再置
$$
\boxed{
\tau_n^+=(h+1-n)P_nS_{n+1}+w(n+1)P_{n+1}S_n.
}
\tag{3.2}
$$
内部 $1\le n<h$ 置
$$
\boxed{
\tau_n^-=(h-n)S_nM_n+wnS_{n+1}M_{n-1}.
}
\tag{3.3}
$$
两个端点准确定义为
$$
\tau_0^-=hS_0M_0,\qquad
\tau_h^-=whS_{h+1}M_{h-1}.
\tag{3.4}
$$
也就是在 (3.3) 中删除系数为零的项；绝不引入 $M_{-1}$ 或 $M_h$。全部 $\tau_n^\pm$ 在正 $z,w$ 上严格正。

令 $H_n$ 为完整层逆在固定首一 primitive 源 $(\alpha,\beta)$ 上的真实 MP Gram，包括真实源 Gram $H_0$。其全高度 shear 写成
$$
H_n=\begin{pmatrix}A_n+B_nk_n^2&-B_nk_n\\-B_nk_n&B_n\end{pmatrix}.
$$
利用已证完整更新公式和 (1.4)、(1.5)，准确得到
$$
\boxed{
A_n=L_n z\frac{\tau_n^+}{R_n},\quad
B_n=L_n w\frac{R_n}{\tau_n^-},\quad
k_n=-\frac{W_n}{R_n}.
}
\tag{3.5}
$$
例如 $n=0$ 时 (3.4) 给 $B_0=wb_0$，$n=h$ 时给 $B_h=b_{h-1}$；正是两个真实硬约束端点。公共源坐标随 $z,w$ 改变，但对所有 $n$ 相同，故相邻比较保持同一源合同。

于是全部 $0\le n\le h$ 有如下完整分式矩阵：
$$
\boxed{
H_n=\frac{L_n}{\tau_n^-R_n}
\begin{pmatrix}
z\tau_n^+\tau_n^-+wW_n^2&wW_nR_n\\
wW_nR_n&wR_n^2
\end{pmatrix}.
}
\tag{3.6}
$$
特别地，
$$
\boxed{\det H_n=L_n^2wz\frac{\tau_n^+}{\tau_n^-}.}
\tag{3.7}
$$
逆矩阵也准确为
$$
\boxed{
H_n^{-1}=\frac1{L_nz\tau_n^+}
\begin{pmatrix}
R_n&-W_n\\
-W_n&(W_n^2+z\tau_n^+\tau_n^-/w)/R_n
\end{pmatrix}.
}
\tag{3.8}
$$
这里从未把压缩的原 Gram 先取逆，也没有把源 Gram 丢弃。

## 4. 单个负极点的 Stieltjes 形

对每个内部阶 $1\le n<h$，固定 $z$ 并令
$$
v_n=(-k_n,1)^T.
$$
完整更新恰为
$$
\boxed{
\frac{H_n(w)}w=
\left(\frac{a_n}w+a_{n+1}\right)e_1e_1^*
+\frac{b_{n-1}}{w+b_{n-1}/b_n}v_nv_n^*.
}
\tag{4.1}
$$
除 $w=0$ 外，只有一个非零负极点 $-b_{n-1}/b_n$，留数为正秩一矩阵。两个端点退化为 (3.4) 对应的零极点及常数项，仍完整。

旧两权相邻比较使 $b_n/b_{n-1}$ 严格递增，所以这些负极点随高度位置有严格次序。但 $v_n$ 同时变化，其变化恰为中矩形 Turán 导数给出的 shear。极点有序和正留数本身不能代替矩阵相邻序；(3.6) 中的 $W_n$ 项必须真正支付。

(2.1)、(3.6) 提供一个具体的 uniform 目标：从三矩形的联立 Jacobi/Toda 关系，推导这族分式矩阵的完整相邻序，或给出其四次中间系数的统一正分解。称它为 Darboux / Bäcklund 型接口只是结构描述，此处不调用任何未核验的外部变换定理，也不宣称该桥已经闭合。

## 5. 任意正底测度扩展的精确反例

不能把实际乘积权 $\nu_r=\binom qr z^r$ 替换成任意正 $\nu_r$ 后再作无结构的正矩阵证明。这个更强的命题连一维旧问题都失败。

取旧两串形式的 $q=L=3$、缺失次数 $\delta=1$、高度二，并任意化底测度为
$$
\nu=(1,\varepsilon,\varepsilon,1),\qquad\varepsilon>0.
$$
准确的有限最小化定义为
$$
H_n=\min_{F\text{ 首一次、保所有非法态强制根}}
\sum_{r:\,0\le n+r-1\le3}
\frac{\nu_r}{\binom3{n+r-1}}|F(r)|^2.
\tag{5.1}
$$
$n=0$ 的强制根为 $r=0$，所以 $F(r)=r$；$n=2$ 的强制根为 $r=3$，所以 $F(r)=r-3$。直接求和得
$$
H_0=H_2=3+\frac{7\varepsilon}3.
$$
$n=1$ 的权为 $(1,\varepsilon/3,\varepsilon/3,1)$，关于 $3/2$ 对称，唯一最小首一次多项式是 $F(r)=r-3/2$。故
$$
H_1=\frac92+\frac\varepsilon6.
$$
取严格正的 $\varepsilon=1/2$，得到
$$
\boxed{H_0=H_2=25/6,\qquad H_1=55/12,\qquad
H_1^2/(H_0H_2)=121/100>1.}
\tag{5.2}
$$
这只是排除任意底测度的扩大命题，不是实际 Boolean 乘积权的反例。实际 $\binom3r z^r$ 在两端都等于一时必须 $z=1$，中间两个权都是三，而不是二分之一。更一般的真实乘积头权聚合也须满足 Newton / 超 log 凹约束，不能实现这个测度。因此 uniform 证明必须使用真实 binomial/Pearson 或等价乘积结构，不能只使用每个矩阵为正、每个离散权为正。


## 6. 下矩形的完整 Hessian 修正及一个实际负例

以下只取内部位置 $1\le n<h$，不对两个硬端虚设 $b_{-1}$ 或 $b_h$。令
$$
u=b_{n-1},\qquad v=wb_n,\qquad R=u+v,\qquad B=uv/R,
\quad \eta=\log w,
$$
$$
g_0=\log M_{n-1},\qquad g_1=\log M_n,\qquad
\sigma=g_1'-g_0',\qquad
T=\begin{pmatrix}1&0\\\sigma&1\end{pmatrix}.
$$
这里 $g_i$ 仅依赖 $\theta$，撇号仍为 $\partial_\theta$。定义实对称矩阵
$$
Q_n=R\operatorname{Hess}_{(\theta,\eta)}\log R.
$$
它先只是一个 Hessian，尚未断言非负。准确的源矩阵身份为
$$
\boxed{H_n=T^*Q_nT+(u g_0''+v g_1'')e_1e_1^*.}
\tag{6.1}
$$

证明：由 (1.5)，
$$
(\log u)'=\delta+f_n'-g_0',\qquad
(\log v)'=\delta+f_{n+1}'-g_1'.
$$
置 $d=f_{n+1}'-f_n'=-k_n$。直接微分 $\log(u+v)$ 得
$$
Q_n=
\begin{pmatrix}
u(f_n''-g_0'')+v(f_{n+1}''-g_1'')+B(d-\sigma)^2&B(d-\sigma)\\
B(d-\sigma)&B
\end{pmatrix}.
\tag{6.2}
$$
剪切 $T$ 将 $d-\sigma$ 准确换回 $d$；再由 $uf_n''=a_n$、$vf_{n+1}''=wa_{n+1}$ 得 (6.1)。$M_j$ 的系数非负且在正轴不为零，所以 $g_j''\ge0$；这支付最后一项的正性，却不支付 $Q_n\succeq0$。而且 $T$ 依赖 $n$，不能在相邻三个矩阵上免费作不同源合同。

下面给出 $Q_n$ 真正为不定的实际乘积权例。取
$$
q=L=3,\quad t=2,\quad\delta=1,\quad h=3,\quad
n=1,\quad z=1,\quad w=4.
$$
原未重新缩放的两权范数为
$$
u=3z+4z^2+3z^3,\qquad
v=4\frac{Z\Theta^2Z-(\Theta Z)^2}{Z},\qquad
Z=1+z+z^2+z^3.
$$
在 $z=1$，
$$
u=10,\quad v=20,\quad
(\log u)'=2,\quad(\log v)'=3/2,
\quad(\log u)''=3/5,\quad(\log v)''=-9/20.
$$
这些值可由 $Z,\Theta Z,\Theta^2Z,\Theta^3Z,\Theta^4Z=(4,6,14,36,98)$ 直接算出。因此
$$
\boxed{Q_1=\begin{pmatrix}-4/3&-10/3\\-10/3&20/3\end{pmatrix},\qquad
\det Q_1=-20.}
\tag{6.3}
$$
同一例的 $M_0=4$、$M_1=Z$，所以 $\sigma=3/2$ 且 $u g_0''+v g_1''=25$。完整恢复给
$$
T^*Q_1T+25e_1e_1^*
=\begin{pmatrix}86/3&20/3\\20/3&20/3\end{pmatrix}=H_1\succ0.
\tag{6.4}
$$
这排除了删去下矩形正修正、将每个 $Q_n$ 都当正协方差矩阵的归纳。它不是实际相邻序的反例；本例属于已证明的整个高度三。

## 7. 缺失次数零的真实协方差、Beta 矩与交叉修正

当 $\delta=0$ 时，所有 $M_j=1$，(6.1) 准确简化为
$$
\boxed{H_n=R_n\operatorname{Hess}_{(\theta,\eta)}\log R_n,
\qquad R_n=b_{n-1}+wb_n,\quad1\le n<h.}
\tag{7.1}
$$
这里确实有正概率模型。此时 $L=q+h-1$，对 $0\le r\le q$、$k\in\{0,1\}$ 定义
$$
\mu_n(r,k)=\frac{\binom qr z^r w^k}{\binom L{n-1+r+k}}.
\tag{7.2}
$$
内部范围保证所有分母合法、严格正。旧首零次范数给 $R_n=\sum_{r,k}\mu_n(r,k)$；指数族微分由有限求和直接给
$$
H_n=R_n\operatorname{Cov}_n(X),\qquad X=(r,k)^T,
\tag{7.3}
$$
其中概率为 $\mu_n/R_n$。因全部 $(r,k)$ 有正权且 $q\ge1$，协方差正定。这里的正性只对 $\delta=0$ 成立；不与 (6.3) 冲突。

同一个实际测度还给
$$
\boxed{R_n=(L+1)\int_0^\infty
\frac{x^{n-1}(1+zx)^q(1+wx)}{(1+x)^{L+2}}\,dx.}
\tag{7.4}
$$
证明只需逐项展开并用
$$
\int_0^\infty\frac{x^j}{(1+x)^{L+2}}\,dx
=\frac{j!(L-j)!}{(L+1)!}
=\frac1{(L+1)\binom Lj},\qquad0\le j\le L.
$$
可由 $x=t/(1-t)$ 及整数次分部积分自足得到这个 Beta 积分。所有和有限，不发生交换收敛问题。

然而，(7.4) 的正矩结构还不是 $H_n$ 的所需相邻矩阵序。它给出的准确交叉项可以完全写出。设 $2\le n\le h-2$，记
$$
m_j=\mathbb E_jX,\qquad
\Delta_-=m_n-m_{n-1},\qquad
\Delta_+=m_{n+1}-m_n.
$$
则
$$
\boxed{
\begin{pmatrix}
H_{n-1}&H_n-R_n\Delta_-\Delta_+^T\\
H_n-R_n\Delta_+\Delta_-^T&H_{n+1}
\end{pmatrix}\succeq0.}
\tag{7.5}
$$

证明：在 $x>0$ 及有限 $(r,k)$ 上取同一正测度
$$
d\rho=(L+1)\binom qr z^r w^k
\frac{x^{r+k}}{(1+x)^{L+2}}\,dx.
$$
两个向量值函数为
$$
x^{(n-2)/2}(X-m_{n-1}),\qquad
x^{n/2}(X-m_{n+1}).
$$
其 Gram 块对角恰为 $H_{n-1},H_{n+1}$。交叉积分为
$$
\sum_{r,k}\mu_n(r,k)(X-m_{n-1})(X-m_{n+1})^T
=H_n-R_n\Delta_-\Delta_+^T,
$$
故得 (7.5)。所有所需矩由内部范围保证有限。

这个秩一交叉修正不能省成零。将 $d\rho$ 对 $(r,k)$ 求和后，在给定 $x$ 时两个条件均值为
$$
\mathbb E(r\mid x)=\frac{qzx}{1+zx},\qquad
\mathbb E(k\mid x)=\frac{wx}{1+wx}.
$$
它们都严格递增。相邻高度恰把同一 $x$ 边缘概率乘以 $x$ 再归一化；由
$$
\operatorname{Cov}(F(x),x)
=\tfrac12\mathbb E[(F(x)-F(y))(x-y)]>0
$$
（$x,y$ 独立且边缘密度处处正），可知 $\Delta_-,\Delta_+$ 的两个分量都严格正。因此正矩方法实际得到的是 (7.5)，而目标的交叉块为 $H_n$，仍差一个真实非零秩一项。

后续须用乘积权的 Pearson 关系或其他准确结构支付这个交叉修正，同时保留两个硬端；不能从 (7.4) 宣称 primitive 全 Hankel 正或从 (7.5) 直接宣布完整相邻序。
