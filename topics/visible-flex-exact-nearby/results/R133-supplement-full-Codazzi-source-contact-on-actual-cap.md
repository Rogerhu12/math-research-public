# R133 续篇：真正旋转正帽的完整 Codazzi 源接触公式

2026-11-13，visible-exact-astra-ac0d / newton_source。

本篇在 R133 的**同一真实旋转参考、同一完整 regular 线**上给出
非零 Fourier 模的完整 inhomogeneous Codazzi 两端公式。两个真实
源、外端 regular 余量和内端 $C$ 迹全部保留。本文的源是下面明确
定义的曲率方程源；它不把未经转换的任意 metric-source 当作这些源，
也不把曲率接触图称为旧 grounded Darboux DN。

数值消费须读取完整通过的 R133 native 报告。证明本身适用于任何
满足 R133 正性和全频门的相同区间 $[r_*,R]$。

## 1. 准确强制系统和所有 Fourier 扇区

设实际正帽的旋转参考曲率为 $(A_0,0,C_0)$，并记
$$
\gamma=\sqrt E/a>0,\quad\beta=a'/a,\quad
\ell=A_0/C_0=K/C_0^2>0.
$$
对每个物理频率 $m\ne0$，先将复 Fourier 行写成
$$
b_m=i\operatorname{sgn}(m)\widehat{\delta B}(m),\qquad
c_m=\widehat{\delta C}(m),\qquad M=|m|\in4\mathbb N.
$$
该单位模变换没有改变 Fourier norm。完整强制 Jacobi 系统是
$$
\begin{split}
b_m'&=-2\beta b_m+M\gamma\ell c_m+f_{b,m},\\
c_m'&=M\gamma b_m-\beta(\ell+1)c_m+f_{c,m}.
\end{split}                                                     \tag{S.1}
$$
因此实 sine/cosine 扇区、另一反射扇区以及负频率都被同一公式覆盖。
若原 $B$ 方程的复源为 $F_{B,m}$，则
$f_{b,m}=i\operatorname{sgn}(m)F_{B,m}$；$f_{c,m}=F_{C,m}$。

令 $q_M>0$ 为 R133 从**真实完整尾**回传的比值。
它满足原径向方向的准确方程
$$
q_M'=M\gamma(q_M^2-\ell)+\beta(\ell-1)q_M.
\tag{S.2}
$$
所有非第四模的真实 regular fee 已包含在这个 $q_M$ 内，不能
重新将它替换成某个稳定中心近似。

## 2. 两个半径权将全部连接项准确消去

设
$$
d_m=b_m+q_Mc_m,\quad D_m=a^2d_m,\quad V_m=a^2C_0c_m.
\tag{S.3}
$$
将 (S.1)、(S.2) 直接相加，得到
$$
d_m'=(M\gamma q_M-2\beta)d_m+f_{b,m}+q_Mf_{c,m}.
$$
而旋转参考自身的准确 Codazzi 行给
$$
\frac{C_0'}{C_0}=\beta(\ell-1).
$$
于是两条强制方程准确三角化为
$$
\boxed{\begin{split}
D_m'&=M\gamma q_MD_m+G_{D,m},\\
V_m'&=-M\gamma q_MV_m+C_0M\gamma D_m+G_{V,m},
\end{split}}                                                    \tag{S.4}
$$
其中
$$
G_{D,m}=a^2(f_{b,m}+q_Mf_{c,m}),\qquad
G_{V,m}=a^2C_0 f_{c,m}.
\tag{S.5}
$$
这里没有用绝对值估计来取消 $\beta$ 项；取消是准确恒等式。
也没有要求 $a'$ 或 $n_z$ 在帽上不变号，因此可以越过旋转最大圆。

## 3. 完整真实两端解与 regular 反射

令
$$
\mathcal K_M(r,t)=
\exp\left(-M\int_{\min(r,t)}^{\max(r,t)}\gamma q_M\,du\right).
$$
给定外端完整 regular 余量 $D_m(R)=D_{R,m}$ 和内端
$V_m(r_*)=V_{*,m}$，准确唯一解为
$$
\begin{split}
D_m(r)&=\mathcal K_M(r,R)D_{R,m}
       -\int_r^R\mathcal K_M(r,t)G_{D,m}(t)\,dt,\\
V_m(r)&=\mathcal K_M(r_*,r)V_{*,m}
       +\int_{r_*}^r\mathcal K_M(t,r)
          [C_0(t)M\gamma(t)D_m(t)+G_{V,m}(t)]\,dt.
\end{split}                                                     \tag{S.6}
$$
第一式的负号来自指定右端值，不可省略。正帽的 ordinary source
完整进入积分，并在内端生成真实缺口
$D_m(r_*)/a(r_*)^2=b_m(r_*)+q_M(r_*)c_m(r_*)$。
外尾若有 particular 或 nonlinear 余量，它就是 $D_{R,m}$ 的输入；
不能因齐次 regular 线为0而把这个真实端源也设为0。

反解为
$$
c_m=\frac{V_m}{a^2C_0},\qquad
b_m=\frac1{a^2}\left(D_m-\frac{q_M}{C_0}V_m\right).
\tag{S.7}
$$
由 $a>0,C_0<0$，这里没有隐藏零分母。式 (S.6) 同时给存在和唯一性；
不需要逆一个在长正帽上指数增长的传递矩阵。

## 4. 全 Fourier 源 norm：必须说明径向和模求和次序

设 R133 全域全频门为
$$
\gamma\ge\gamma_->0,\quad q_M\ge q_->0,\quad
q_M\le q_+,
\quad 0<C_-\le|C_0|\le C_+,\quad\gamma\le\gamma_+,
$$
并置 $\sigma=\gamma_-q_-$、$T=C_+/q_-$。
使用明确的非零模路径 norm
$$
\|F\|_{\mathfrak X^s}
=\sum_{m\in4\mathbb Z\setminus\{0\}}
 |m|^s\sup_{r\in[r_*,R]}|F_m(r)|.
\tag{S.8}
$$
边界向量的 norm 则是相同纯 $|m|^s$ Fourier 权的和。
此处是 **先对每模取径向 sup，再求和**；未经额外论证不能将它
替换为 $L_r^\infty\mathcal A^s$，并免费沿用完整一阶增益。
对每一模先积分指数核，再求和，有
$$
\begin{split}
\|D\|_{\mathfrak X^s}
&\le\|D_R\|_s+\sigma^{-1}\|G_D\|_{\mathfrak X^{s-1}},\\
\|V\|_{\mathfrak X^s}
&\le\|V_*\|_s+T\|D\|_{\mathfrak X^s}
           +\sigma^{-1}\|G_V\|_{\mathfrak X^{s-1}}.
\end{split}                                                     \tag{S.9}
$$
这里第二行的三角费用可准确少付一个全局 $\gamma_+/\gamma_-$：
$$
\begin{split}
\int_{r_*}^r\mathcal K_M(t,r)|C_0(t)|M\gamma(t)\,dt
&\le\frac{C_+}{q_-}\int_{r_*}^r
    M\gamma(t)q_M(t)\mathcal K_M(t,r)\,dt\\
&=\frac{C_+}{q_-}[1-\mathcal K_M(r_*,r)]\le T.
\end{split}
$$
这是对真实非恒定指数核的积分恒等式，不要求 $q_M'$ 为0。
因最小物理频率为4，同阶版本将最后各源项的系数换为
$(4\sigma)^{-1}$。若有共同解析 Fourier 权，它可逐模乘入而
不改变这些常数；这里没有截断无限高模。

原曲率的带半径权 norm 满足
$$
\|a^2c\|_{\mathfrak X^s}\le C_-^{-1}\|V\|_{\mathfrak X^s},
\quad
\|a^2b\|_{\mathfrak X^s}
\le\|D\|_{\mathfrak X^s}+\frac{q_+}{C_-}\|V\|_{\mathfrak X^s}.
\tag{S.10}
$$
去掉 $a^2$ 会支付真实最小半径的倒平方；本文不隐瞒这个物理缩放，
更不将 (S.9) 直接称为无权 material $C^2$ 估计。

## 5. mean 源、位置与重建没有消失

曲率 mean 的完整强制系统是
$$
b_0'=-2\beta b_0+f_{b,0},\qquad
c_0'=-\beta(\ell+1)c_0+f_{c,0}.
$$
因此准确地
$$
(a^2b_0)'=a^2f_{b,0},\qquad
(a^2C_0c_0)'=a^2C_0f_{c,0}.
\tag{S.11}
$$
这里的两个积分常数仍必须与真实周期框架、mean holonomy、regular
高度和普通源电荷联立。纯齐次周期轴对称位移只有轴向平移与绕轴
转动；它们的曲率数据为0，但它们的位移端口没有因 (S.11) 而删除。
本文没有为任意 forced mean 数据声称可逆，也没有将 mean flux
偷换为某个非零 Fourier 乘子。

若 (S.1) 来自完整 metric Newton 源，尚须准确推导它到
$(f_b,f_c)$ 的映射、位移/框架端源和全部 mean 条件，再用相同的
真实参考重建。R133 的非零模曲率图和本篇的源公式提供该步骤的
一个实际正帽接口；完整 mixed inverse、turning connection 和
最终 nonlinear 闭合仍是另外的数学门。

## 6. 真正连续 native 消费与更紧的全频门

consumer 读取 R133 v2 的完整 1,334 闭盒，并检查成功标志、原始
失败 checkpoint 身份、producer、全部依赖和 R74/R126 定理 SHA。
域为准确 $[239/1000,25/8]$、完整 $|\eta|\le10^{-9}$ 与全部
primitive/alias 尾。这里没有重新取有限频率或径向点样本。

还可从同一完整系数盒取得比 R133 (133.23) 更紧的统一全频不变区间。
将向内 Riccati 右侧除以正量 $M\gamma$，得到
$$
\frac{(q_M)_t}{M\gamma}
=\ell-q_M^2-\frac{\beta(\ell-1)}{M\gamma}q_M.
\tag{S.12}
$$
在第 $j$ 个真实径向盒，以有向算术给
$\ell\in[\ell_{j,-},\ell_{j,+}]$，并设
$$
d_{j,-}=\min\left(0,\inf\frac{-\beta(\ell-1)}{4\gamma}\right),
\qquad
d_{j,+}=\max\left(0,\sup\frac{-\beta(\ell-1)}{4\gamma}\right).
$$
因 $M\ge4$，真实线性系数属于 $[d_{j,-},d_{j,+}]$。
取 $x_j>0,y_j>0$ 分别为
$$
\ell_{j,-}+d_{j,-}x_j-x_j^2=0,\qquad
\ell_{j,+}+d_{j,+}y_j-y_j^2=0
\tag{S.13}
$$
的正根。全局下界取所有 $x_j$ 与真实完整尾初始下界的最小值，
全局上界取所有 $y_j$ 与真实初始上界的最大值，再分别乘
$1-2^{-128}$ 和 $1+2^{-128}$ 向外放宽。producer 在每一盒重新核
$$
\ell_{j,-}+d_{j,-}q_--q_-^2>0,\qquad
q_+^2-d_{j,+}q_+-\ell_{j,+}>0,
\tag{S.14}
$$
并核全部真实初值严格在区间内部。因此每一个 $M\in4\mathbb N$
都由严格向内边界条件保留在同一正区间内。除以 $M\gamma$ 之后才
取局部盒端点，避免把不同径向位置的 $\gamma$ 极值无谓地相乘。

实际有向结果的安全十进制放宽是
$$
\boxed{\quad .19460680<q_M(r)<2.50343494,\qquad
\sigma>.21649779.\quad}                                      \tag{S.15}
$$
进而
$$
\sigma^{-1}<4.61898469,\quad(4\sigma)^{-1}<1.15474618,
\quad T<4.60423161.
\tag{S.16}
$$
数值报告保存每个常数的有向 ball、两个全盒最小严格边界 margin、
取得两个根极值的真实盒号、完整真实尾初值及所有身份。

对按顺序排列的输入
$\bigl(\|D_R\|_s,\|V_*\|_s,
\|G_D\|_{\mathfrak X^{s-1}},\|G_V\|_{\mathfrak X^{s-1}}\bigr)$，
输出顺序为 $D,V,a^2b,a^2c$，完整报告还提供逐项有向的 $4\times4$
正矩阵。它不遗漏普通源或外端 regular 余量。
例如下面逐项外舍入矩阵就是一个可直接消费的版本：
$$
\begin{pmatrix}
1&0&4.619&0\\
4.605&1&21.267&4.619\\
68.591&14.680&316.817&67.807\\
26.999&5.864&124.708&27.086
\end{pmatrix}.
\tag{S.17}
$$
去掉半径权的附加费用仍为
$$
\left(\min_{[r_*,R]}a\right)^{-2}<23214174243.
$$
因此半径权不能免费删去。

可重跑入口为

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_codazzi_rotational_cap_source_budget.py \
  --out notes/2026-11-13-R133-Codazzi-cap-source-budget-native.json
```

脚本拒绝覆盖已有输出；复核时应使用新输出路径。
源、报告、本文及全部实际输入的 SHA 存于独立 source-contact manifest。
