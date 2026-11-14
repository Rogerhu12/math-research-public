# R391 — E24 原野三次 Schwartz、绝对相位及十八项 Heisenberg 升层

日期：2026-11-14。**状态：以下同一原角色和 $\alpha=1$ 下的实际三处
不变向量、原九维模型、完整环面生成元、绝对相位、范数及带中心
补偿的十八项升层均已证明。二处向量和全局周期尚须继续支付；
本篇不从局部向量存在推出中央非零或全 Selmer 结论。**

固定 [R389](R389-e24-primitive-wild-local-data-and-actual-hermitian-class.md)
的曲线 $E_{24}:y^2=x^3+24$，
$\delta=\sqrt{-3}=1+2\omega$、$\operatorname{Im}\delta>0$、
$\alpha=1$。三处取
$$
\psi(t)=e^{-2\pi i\{t\}_3},\quad
\chi=\chi_{24,3},\quad
\chi(\delta)=i,\quad
\chi=\chi_{1,3}\vartheta_\delta^{-1}.
\tag{1}
$$
所有原 bad-local 和 reciprocity 方向已在 R389 支付。
特别 $\vartheta_\delta(1+\delta^3)=\omega$。

## 1. 真正要验证的环面生成元

令 $T=K_3^1$，并置
$$
g_*=\frac{1+3\delta}{1-3\delta}
    =\frac{-13+3\delta}{14}.
\tag{2}
$$
整个 $T$ 由 $-1,\omega,g_*$ 拓扑生成。

证明如下。$\mu_6$ 向 $(\mathcal O_{K_3}/\delta^2)^\times$ 的映射
是同构，后者只有六个元素。
$T\cap(1+\delta^2\mathcal O)$ 的对数准确为
$$
\{z\in\delta^2\mathcal O:\operatorname{Tr}z=0\}
 =\delta^3\mathbf Z_3.
$$
此范围的 exponential/logarithm 互逆，因为其 valuation 严格超过
$e/(3-1)=1$。而
$$
\log g_*=2\left(3\delta+\frac{(3\delta)^3}{3}
                   +\frac{(3\delta)^5}{5}+\cdots\right)
 =-2\delta^3\cdot(\text{三进单位}).
$$
故其整数幂在这个对数格中稠密。这证明所列生成元足够；
不是只检查有限模数的几个点。

## 2. 原 Schrödinger splitting 的三个绝对常数

保持 Yang Appendix (A1)–(A3) 的真实嵌入和 section：
$$
\iota(g)=
 \begin{pmatrix}x&9y\\-y/3&x\end{pmatrix},
\qquad g=x+y\delta,
$$
$$
\omega_{1,\chi}(g)=\mu(g)r_S(\iota(g)),\qquad
\mu(g)=\chi(\delta(g-1))\,
 \gamma_3(y(1-x)\psi)\,
 (-3,-2y(1-x))_3 .
\tag{3}
$$
对 $a=3^n u$、$u\in\mathbf Z_3^\times$，原负有限加性角色给
$$
\gamma_3(a\psi)=
 \begin{cases}1,&n\text{ 偶},\\
 -i(u/3),&n\text{ 奇}.
 \end{cases}
\tag{4}
$$
这是 $3$ 项二次 Gauss 和
$\sum_{t\bmod3}e^{-2\pi iut^2/3}$ 的直接规范。
又对任意 $b=3^m v$，
$$(-3,b)_3=(v/3).$$

代入 (3) 准确得到
$$
\boxed{\mu(\omega)=-i,\qquad
       \mu(-\omega)=-i,\qquad
       \mu(g_*)=\omega.}
\tag{5}
$$
各因子可逐项核定：

- 对 $\omega=(-1+\delta)/2$，
  $\delta(\omega-1)=3\omega^2$，其 $\chi$ 值为一；
  $y(1-x)=3/4$ 的 Weil 指数为 $-i$，Hilbert 因子为一。
- 对 $-\omega=(1-\delta)/2$，
  $\delta(-\omega-1)=\delta\omega^2$，其 $\chi$ 值为 $i$；
  $y(1-x)=-1/4$ 的 Weil 指数为一，Hilbert 因子为负一。
- 对 $g_*$，
  $y(1-x)=81/196$，Weil 和 Hilbert 因子都为一。
  另外
  $$
  \delta(g_*-1)=-\frac9{14}(1+3\delta).
  $$
  其 $\delta^4$ 与基单位角色均给一，
  $\vartheta_\delta(1+3\delta)=\omega^2$，
  所以原逆向扭曲给 $\chi(\delta(g_*-1))=\omega$。

特别，(5) 不是只确定到一个 projective scalar。

## 3. 原九维空间、支撑与原有限矩阵

取自对偶测度 $\operatorname{vol}(\mathbf Z_3)=1$，定义
$$
V=\mathcal S(3^{-2}\mathbf Z_3/\mathbf Z_3),\qquad
e_a=\mathbf1_{a/9+\mathbf Z_3}\quad(a\bmod9).
\tag{6}
$$
这是真实 Schwartz 子空间；下述计算也证明它对三个原生成元稳定。

对 $\iota(g)=\left(\begin{smallmatrix}x&*\\c&x\end{smallmatrix}\right)$、
$c\ne0$，所用 Rao 核准确为
$$
r_S(\iota(g))\phi(u)
 =|c|_3^{-1/2}\int_{\mathbf Q_3}
 \psi\left(\frac{x(u^2+v^2)-2uv}{2c}\right)\phi(v)\,dv.
\tag{7}
$$
这来自原 upper-triangular/diagonal/Fourier 的 Bruhat 分解，
其中 Fourier 为 $\int\psi(-uv)\phi(v)\,dv$。

### 3.1 $\omega$ 的全部九维行

取 $\zeta=\zeta_9=e^{2\pi i/9}$，故 $\omega=\zeta^3$。
对 $\omega$，(7) 的相位为
$$\frac32(u^2+4uv+v^2).$$
令 $v=a/9+t$、$t\in\mathbf Z_3$，$u=c_0/9$。
线性项的积分为零，除非 $a\equiv c_0\pmod3$；
二次项属于 $\mathbf Z_3$，不再贡献相位。
于是 (5) 给完整有限矩阵
$$
\boxed{
\omega_{1,\chi}(\omega)_{c_0a}
 =\begin{cases}
 \delta^{-1}\zeta^{-5(c_0^2+4c_0a+a^2)/3},
       &a\equiv c_0\pmod3,\\
 0,&a\not\equiv c_0\pmod3.
 \end{cases}
}
\tag{8}
$$
指数的分子在非零情形被三整除；余下除二使用
$2^{-1}\equiv5\pmod9$。因 $-i/\sqrt3=1/\delta$，
(8) 保留了绝对 Gaussian 标量。

对任意 $u$，同一积分条件
$a/3+6u\in\mathbf Z_3$ 先强迫
$u\in3^{-2}\mathbf Z_3$；再平移 $u\mapsto u+1$ 不改变相位。
所以没有遗漏 (6) 以外的输出支撑。

### 3.2 $g_*$ 与负号的全部作用

对 $g_*$，(7) 的相位为
$$
\frac{13}{2}(u^2+v^2)+14uv.
$$
代入 (6)，积分条件为
$13a+14c_0\equiv0\pmod9$，即 $c_0\equiv a\pmod9$。
该处的常数项为 $a^2/3$，所以
$$
\boxed{\omega_{1,\chi}(g_*)e_a
   =\omega^{\,1-a^2}e_a.}
\tag{9}
$$
若 $u$ 不在 (6) 的支撑内，线性项积分同样为零。

把 $-\omega$ 代入 (7)，得到 $\omega$ 的同一核再接
$u\mapsto-u$。由 (5) 两个标量相同，且 $\omega^3=1$，
$$
\boxed{\omega_{1,\chi}(-1)\phi(u)=\phi(-u).}
\tag{10}
$$
因此原不变列必须偶，且 (9) 强迫它在 $3\mid a$ 时为零。
真正留下的是三维空间
$$
V_{\mathrm{prim}}^+
 =\langle e_1+e_{-1},\,e_2+e_{-2},\,e_4+e_{-4}\rangle.
\tag{11}
$$
它不是任取的同次数全纯来源。

## 4. 唯一不变列及准确范数

在 (11) 的有序基中，(8) 是
$$
\boxed{
M=\frac1\delta
 \begin{pmatrix}
 \zeta^8&\zeta^5&\zeta^8\\
 \zeta^5&\zeta^5&\zeta^2\\
 \zeta^8&\zeta^2&\zeta^2
 \end{pmatrix}.
}
\tag{12}
$$
令
$$
B=\begin{pmatrix}
\omega^2&\omega&\omega^2\\
\omega&\omega&1\\
\omega^2&1&1
\end{pmatrix},\qquad M=\zeta^2 B/\delta .
$$
直接相乘给
$$
B^2=
\begin{pmatrix}
\omega-1&-\delta&\omega-1\\
-\delta&-\delta&2+\omega\\
\omega-1&2+\omega&2+\omega
\end{pmatrix},
\quad B^3=3(2+\omega)I=\delta^3\omega I.
\tag{13}
$$
故 $M^3=I$，$\operatorname{Tr}M=0$。
其特征多项式是 $t^3-1$，不变线恰一维。
同一矩阵还给 $M^2=\overline M$；
因为它对称，这也是 $M^*=M^{-1}$ 的完整酉性。

定义实际实向量
$$
\boxed{
\begin{aligned}
f_1&=3+\delta(\zeta-\zeta^8),\\
f_2&=-\delta(\zeta^5-\zeta^4),\\
f_4&=\delta(\zeta-\zeta^8).
\end{aligned}}
\tag{14}
$$
它等于 $3(I+M+M^2)(1,0,0)^{\mathsf t}$，
所以 $M(f_1,f_2,f_4)^{\mathsf t}=(f_1,f_2,f_4)^{\mathsf t}$。
(14) 的每个坐标被复共轭固定，且 $f_1\ne0$。
例如在整数基 $1,\zeta,\ldots,\zeta^5$ 中，三列准确为
$$
\boxed{
\begin{array}{c|rrrrrr}
&1&\zeta&\zeta^2&\zeta^3&\zeta^4&\zeta^5\\ \hline
f_1&3&1&-1&0&2&1\\
f_2&0&-2&2&0&-1&1\\
f_4&0&1&-1&0&2&1 .
\end{array}}
\tag{15}
$$
这里使用 $\zeta^6+\zeta^3+1=0$，常数三已经证明非零。

所求的原三处函数是
$$
\boxed{
\phi_3=f_1(e_1+e_{-1})
      +f_2(e_2+e_{-2})
      +f_4(e_4+e_{-4}).
}
\tag{16}
$$
(9)、(10)、(12) 及 §1 的拓扑生成元证明它被整个
$(T,\omega_{1,\chi_{24,3}})$ 固定。
其支撑恰在 $3^{-2}\mathbf Z_3^\times$，
不可能由较低分母的 ground function 替代。

记 $\Pi=(I+M+M^2)/3$。由 (14)，$f=9\Pi e_1$。
正交投影性给
$$
f_1^2+f_2^2+f_4^2=9f_1.
$$
每个 $e_a$ 的体积为一，六个陪集互不相交，于是
$$
\boxed{\|\phi_3\|^2=18f_1>0.}
\tag{17}
$$
这也给 $f_1$ 的严格正性，不使用浮点近似。

## 5. 与旧 ground 来源的真实 Heisenberg 升层

本节支付一个可实际复用的有限运输，而非仅记录新的不变列。
令
$$
h_0=\mathbf1_{3^{-1}\mathbf Z_3},\qquad
(\tau_a f)(u)=f(u-a),\qquad (m_j f)(u)=\psi(ju)f(u).
$$
直接在 $u=k/3+\mathbf Z_3$ 上求三个角色和，得到
$$
e_0=\frac13(1+m_1+m_2)h_0,\qquad
e_1+e_{-1}=(\tau_{1/9}+\tau_{-1/9})e_0.
\tag{18}
$$
将 (18) 代入 (14) 的 projector，
$$
\boxed{
\phi_3=(I+M+M^2)
 (\tau_{1/9}+\tau_{-1/9})(1+m_1+m_2)h_0.
}
\tag{19}
$$
这里 $M$ 表示整个原算子 $\omega_{1,\chi_{24,3}}(\omega)$，
在需要的三维子空间中才用 (12) 书写。

为保持真正的 theta 群中心，定义对称 Weyl lift
$$
(\mathcal H(a,j)f)(u)
 =\psi(j(u-a/2))f(u-a).
$$
则
$$
\tau_a m_j=\psi(-ja/2)\mathcal H(a,j),
$$
所以全部六个平移的准确中心相位为
$$
\boxed{
\phi_3=(I+M+M^2)
 \sum_{\varepsilon=\pm1}\sum_{j=0}^2
 \zeta^{5\varepsilon j}\mathcal H(\varepsilon/9,j)h_0.
}
\tag{20}
$$
这是十八项原 Weyl/环面运输；分母九、逆二和每项中心相位都已保留。
(20) 不是说新旧整条环面表示相同：
$h_0$ 属于旧 ground 数据，而输出由实际 projector 选出
R389 的野三次特征。不能以相同 $\alpha=1$ 删去这个升层。

## 6. 可复现性与当前范围

固定域 $\mathbf Q(\zeta_9)$ 中，按
$\zeta^6+\zeta^3+1=0$ 约简即可重建 (8)、(12)、(15)。
已直接执行的精确整数多项式计算逐项核定：

- 整个九维矩阵的三次幂为一；
- 六个 unit 坐标上的完整九维不变列；
- $g_*$ 的原角色及 primitive 支撑；
- 三维矩阵的原绝对标量、共轭实性和 (17) 的范数；
- $\delta^2=-3$ 及 (13) 的全部矩阵项。

正文的 (8)、(9)、(13)、(15) 已给出全部固定输入和证明，
不需要依赖一次数值识别，也没有新增按 $p$ 扫描。

本篇完成的是固定 $E_{24}$ 的三处原始向量和真实升层。
二处的 conductor-eight 向量、全局有理支撑、原周期和完整平方常数
还须继续计算；因此尚不能把旧 $D_{16}$ 的中央行换名为本曲线中央行，
也不能省略后来要用的全 Selmer 比较。

## 文献与提交

T. Yang, *Nonvanishing of central Hecke L-values and rank of certain
elliptic curves*, Compositio Math. **117** (1999), 337–359，
Appendix (A1)–(A3) 的原 splitting；
[作者全文](https://people.math.wisc.edu/~tonghaiyang/rank.pdf)。
本篇不从仅处理低 conductor 的 Corollary 1.4 推出野三次向量；
(2)–(20) 直接在原 Schrödinger 表示中证明。

坏点角色及绝对 reciprocity 见
[R389](R389-e24-primitive-wild-local-data-and-actual-hermitian-class.md)。
提交前 API 读取 main 为
$3de8a229098636a24dd223db832fe2a19ad94d59$，两份 README blob 未变。
执行终端仍不可用，本篇为根规矩八允许的小文本 API 提交，
不是本地 git pull。
