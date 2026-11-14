# 实际素数对角的 Gauss–Manin 公式与模 $p^2$ Legendre 提升

日期：2026-11-12。状态：实际模函数、尺度、指定对角及 Legendre
替换均已证明；尚未证明其中除 $p$ 后的指定值在无穷多个惰性素数非零。

本篇使用 $E_0:y^2=x^3-x$、$A(z)=z^4+(97/60)z^8+\cdots$ 的规范。
记 $A=\sum b_mz^m$。由 R51 的准确缩放，原曲线 $E_{17}$ 的对应
临界系数只多一个 $17$ 的单位幂，不改变目标惰性素数处的非零判据。

## 1. 一个固定代数模函数及两条固定周期解

取[实际热公式](2026-11-12-inert-critical-heat-derivative.md)中的

$$
 F(\tau)=\sum_{17\nmid n}\lambda(n)\zeta_{289}^{19n^2}
             e^{\pi i\tau n^2/289},\qquad\lambda(3)=-i.
 \tag{1}
$$

令 $\lambda_{\rm Leg}=\vartheta_2^4/\vartheta_3^4$，并在 $\tau=i$
附近取参数 $t=\lambda_{\rm Leg}-1/2$。
**本篇的 $t$ 是模参数，不是椭圆正式参数 $-x/y$。**
固定函数

$$
 M_0(t)=F(\tau(t))/\vartheta_3(\tau(t))
$$

代数于 $\overline{\mathbb Q}(t)$。理由是两个半权 theta 都在一个
共同有限级别上变换，权相除后为模函数。也可以直接用有限 theta
矩阵：对有限个陪集取 $\prod(T-M_0(\gamma\tau))$，系数为
$\Gamma(2)$ 模函数，故有理于 $\lambda_{\rm Leg}$；其 cusp 展开
系数为代数数，因而这些有理函数也有代数系数。
分母参考 theta 在上半平面不为零，故这里的 CM germ 正则。

已证 $F(i)=DF(i)=0$、二阶导数非零，且
$\lambda_{\rm Leg}'(i)\ne0$。因此 $M_0$ 恰有二阶零点。
除去其非零的 $t^2$ 系数，定义一次固定的归一化

$$
 M(t)=t^2+O(t^4).
 \tag{2}
$$

该归一化在素数变化之前完成。下面的坐标比较也证明 $M$ 是偶函数。

在 $t=0$ 取 Picard–Fuchs 解

$$
 \mathscr D y:=(1-4t^2)y''-8ty'-y=0,
$$

$$
 K(0)=1,\ K'(0)=0,\qquad L(0)=0,\ L'(0)=1.
$$

它们准确为

$$
 \begin{aligned}
 K(t)&={}_2F_1(1/4,1/4;1/2;4t^2),\\
 L(t)&=t\,{}_2F_1(3/4,3/4;3/2;4t^2).
 \end{aligned}
 \tag{3}
$$

可不使用任何周期数值来计算它们：若 $y=\sum c_nt^n$，则

$$
 c_{n+2}=\frac{(2n+1)^2}{(n+1)(n+2)}c_n.
 \tag{4}
$$

令 $u=L/K$，则 $u=t+O(t^3)$，由初值和 Wronskian 得

$$
 \frac{du}{dt}=\frac1{(1-4t^2)K(t)^2}.
 \tag{5}
$$

定义准确的协变 Taylor 级数

$$
 \mathcal B(u)=K(t(u))^{1/2}M(t(u))
             =\sum_{N\ge2}C_Nu^N,\qquad C_2=1.
 \tag{6}
$$

所有根取常数项 $1$ 的正式分支。这里没有把平方根周期认定为
一个完整的有限秩线性微分模块；(3) 与固定代数 $M$ 是实际使用的数据。

## 2. 与实际 $b_{2N}$ 的无周期准确尺度

置 $\alpha=4-i$、$\beta=4+i$，并以 $\Omega_0$ 表示 $E_0$ 的正实周期。
热公式的实际尺度是

$$
 h=\frac{\sqrt{\pi_{\mathbb C}/2}\,17}{\Omega_0\alpha}
   =\frac{\sqrt{\pi_{\mathbb C}/2}\,\beta}{\Omega_0}.
$$

为核对 Serre/Cayley 坐标的常数，令

$$
 w=\frac{\tau-i}{\tau+i},\qquad
 \mathcal C(w)=(1-w)^{-1/2}F\!\left(i\frac{1+w}{1-w}\right).
$$

记 $\mathbf K(m)$ 为以参数 $m$ 而非模数 $\sqrt m$ 表示的完全椭圆积分。
经典 theta–椭圆积分恒等式给
$\vartheta_3^2=2\mathbf K/\pi_{\mathbb C}$；Legendre 关系给
$\mathbf K'(1/2)=\pi_{\mathbb C}/(2\mathbf K(1/2))$，且
$\Omega_0=\sqrt2\mathbf K(1/2)$。
这里的导数是参数导数，不是 complementary integral 的上标。
这些规范可核于 NIST DLMF（2026），
[20.9.1–2](https://dlmf.nist.gov/20.9)、导数式
[19.4.1](https://dlmf.nist.gov/19.4) 经 $m=k^2$ 换元，以及
[19.7.1](https://dlmf.nist.gov/19.7)。
等价地，可由两条 PF 解在 $m=0$ 的 Wronskian 渐近直接求出同一常数。

更明确地，令

$$
 k(t)=\mathbf K(1/2+t),\qquad
 \bar k(t)=\mathbf K(1/2-t),\qquad
 k_0=\mathbf K(1/2),\quad k_1=\mathbf K'(1/2).
$$

这里 $\bar k$ 只是 complementary solution 的记号。在所选 CM 分支上，
$\tau=i\bar k/k$。由 (3) 的偶、奇初值，准确有

$$
 K=\frac{k+\bar k}{2k_0},\qquad
 L=\frac{k-\bar k}{2k_1},\qquad
 w=-\frac{k_1}{k_0}\frac{L}{K}.
$$

于是

$$
 w=\gamma u,\qquad\gamma=-\frac{\pi_{\mathbb C}}{\Omega_0^2}.
 \tag{7}
$$

又由 $k=k_0K(1-w)$ 得

$$
 \vartheta_3(\tau)
 =\vartheta_3(i)K(t)^{1/2}(1-w)^{1/2}.
$$

若 $m_2=[t^2]M_0\ne0$，则常数关系准确为
$\mathcal C(\gamma u)=\vartheta_3(i)m_2\mathcal B(u)$。
对权 $k=1/2$ 的 Maass–Shimura 算子，Cayley 展开逐项给

$$
 [w^N]\mathcal C=\frac{(-4\pi_{\mathbb C})^N}{N!}
                         \partial_{1/2}^NF(i).
$$

与已经证明的热式
$B_{2N}^{\rm raw}=(16\pi_{\mathbb C})^N\partial_{1/2}^NF(i)/(2N)!$
及 $b_{2N}=(B_{2N}^{\rm raw}/B_4^{\rm raw})h^{2N-4}$ 比较，得到

$$
 \boxed{\qquad
 b_{2N}=12(2\beta^2)^{N-2}\frac{N!}{(2N)!}\,C_N.
 \qquad} \tag{8}
$$

$\mathcal B$ 只有偶次幂，因为实际 $A$ 只有 $4$ 的倍数次幂；
$K$ 偶且 $u$ 奇，所以 (2) 的 $M$ 也为偶函数。
还有一个有用的定义域加强：实际 $b_m\in\mathbb Q$，故 (8) 给
$C_N\in\mathbb Q(i)$。再由 (3)、(6) 反解，所有 $M$ 的 Taylor
系数也在 $\mathbb Q(i)$ 中。把一个代数方程的系数作有限 Galois
共轭乘积，便得 $M$ 实际代数于 $\mathbb Q(i)(t^2)$。
因此这里确有一个素数变化前固定的代数覆盖和一个已指定的正则分支，
不是只在每个 $p$ 临时选择的模函数。

### $N=4$ 的独立校准

由 (3)–(5)，

$$
 K=1+\frac12t^2+\frac{25}{24}t^4+\cdots,\qquad
 L=t+\frac32t^3+\cdots,\qquad u=t+t^3+\cdots.
$$

故 $C_4=[t^4]M-7/4$，而 (8) 应给

$$
 b_8=\frac{\beta^4}{35}C_4=\frac{97}{60}.
 \tag{9}
$$

脚本
[check-gm-halfweight-calibration.py](../scripts/check-gm-halfweight-calibration.py)
从 (1) 的 Gaussian $\tau$-jets 与独立的 $\vartheta_2,\vartheta_3$
jets 直接构造 $\lambda_{\rm Leg}$ 的逆 jet，随后计算 $M$ 和 $C_4$。
没有把 $b_8$ 输入计算；最后的 Arb 区间与 $97/60$ 的误差严格
小于 $10^{-250}$。Gaussian 尾部使用整数不等式界定。
这项独立校准检查的是非首项的连接/尺度；(8) 本身的证明是上述准确恒等式。

## 3. 指定素数对角的模 $p^2$ 公式

以下取 $p=4r-1\ge7$、$N=(p+1)/2=2r$，并令 $J=L/t$。
对 (6) 使用 (5) 的留数换元，得到特征零恒等式

$$
 \begin{aligned}
 C_N
 &=\operatorname{res}_{t=0}
     \frac{M(t)K(t)^{N-1/2}}{(1-4t^2)L(t)^{N+1}}dt\\
 &=[t^N]\frac{M(t)K(t)^{N-1/2}}
                         {(1-4t^2)J(t)^{N+1}}.
 \end{aligned} \tag{10}
$$

关键是此时 $N-1/2=p/2$。定义一个固定级数

$$
 W(t)=\frac{M(t)}{(1-4t^2)J(t)^{3/2}},\qquad W=t^2+\cdots.
$$

则

$$
 \boxed{\quad
 C_N=[t^N]W(t)\left(\frac{K(t)}{J(t)}\right)^{p/2}.
 \quad} \tag{11}
$$

因为 $M$ 是固定的正则代数 germ，其 Taylor 系数在除去一个固定有限
素数集合后均整；这也可由选取一个在该点 étale 的有限模型直接得到。
不在本文中把这个有限集合未经计算就缩成仅 $2,5,17$。
对其余目标 $p$，(4) 说明 $K,J$ 到次数 $N<p$ 都 $p$ 整。
取根、对数及指数到此次数所除的整数也均小于 $p$。所以真正保留两层的式子是

$$
 \boxed{\quad
 C_N\equiv[t^N]W+
       \frac p2[t^N]W\log(K/J)\pmod{p^2}.
 \quad} \tag{12}
$$

由实际 $b_{p+1}$ 整及 (8)，$p\mid C_N$，所以 (12) 还证明
$p\mid[t^N]W$。最终目标是

$$
 \boxed{\quad
 b_{p+1}\equiv
 -12(2\beta^2)^{N-2}N!
 \left(\frac{[t^N]W}{p}+
             \frac12[t^N]W\log(K/J)\right)\pmod p.
 \quad} \tag{13}
$$

其中前面的因子为单位。式中 $(2N)!=(p+1)!$ 的唯一 $p$ 没有丢掉。
仅保留 (12) 的模 $p$ 零式不足以判断 (13)。

也可把右边括号写成一个固定级数的素数对角：令

$$
 (2t\partial_t-1)Z=W,\qquad
 Z=\sum_{n\ge0}\frac{[t^n]W}{2n-1}t^n,
 \qquad \mathcal G=Z+\frac12W\log(K/J).
 \tag{14}
$$

则括号等于 $[t^N]\mathcal G$。
这是固定代数 $M$、固定秩二 PF 数据及一个明确原函数扩张的表示；
没有由这份有限数据直接断言 $\mathcal G$ 为 D-finite 或其对角非零。

## 4. Hasse 的准确水平提升

置 $n=N-1=(p-1)/2$，这是奇数。
先截取 $L$ 到次数 $n$，记 $L_{<N+1}$。由 (4)，其末端误差准确为

$$
 \mathscr D L_{<N+1}
       =-p^2[t^n]L\,t^n.
 \tag{15}
$$

而 $[t^{N+1}]L=[t^N]J$ 准确有 $p$ 进赋值 $2$：
在 ${}_2F_1(3/4,3/4;3/2;4t^2)$ 的第 $r$ 个系数中，
两个 $(3/4)_r$ 各贡献一个 $p$，分母是单位。
这证明所需截断的 Hasse 水平性确实维持到模 $p^2$，不只是模 $p$。

更方便的全多项式提升是

$$
 \widetilde L_p(t)=\frac{P_n(2t)}{2P_n'(0)}.
 \tag{16}
$$

$P_n$ 是 Legendre 多项式，分母在当前素数处为单位；
它有初值 $0,1$，并准确满足

$$
 \mathscr D\widetilde L_p=-p^2\widetilde L_p.
 \tag{17}
$$

因此由系数递推（所有所需分母小于 $p$）

$$
 \widetilde L_p\equiv L\pmod{p^2,t^{N+2}},\qquad
 \widetilde J_p:=\widetilde L_p/t
       \equiv J\pmod{p^2,t^{N+1}}.
 \tag{18}
$$

其约化是 CM 根的导数归一化 Hasse 多项式：
Deuring 多项式 $\sum_{k=0}^n\binom nk^2\lambda^k$ 满足同一个 PF 方程模 $p$。
移到 $t=\lambda-1/2$ 后，任何次数至多 $n$ 的非零多项式解的最高次数
都必须是 $n$：若最高次数为 $d\le n$，最高项的系数为
$-(2d+1)^2$，在这个范围内只有 $d=n$ 能模 $p$ 为零。
此处次数限制是必要的；不把任意次数的多项式解都归入该断言。
偶部分不可能有该奇数最高次数，
故解是奇函数，且一次系数非零。用该系数归一，(4) 唯一恢复 (16) 的约化。
这同时给出 CM 根是单根的直接验证。

此处只声称所需截断合同；没有把全级数 $J\bmod p$ 误称为一个多项式。

## 5. 另一条周期也能用显式 Legendre 对数替换

令 $Q_n^{\rm Leg}$ 为在 $x=0$ 正则的第二解，规范为

$$
 Q_n^{\rm Leg}(x)
  =\frac12P_n(x)\log\frac{1+x}{1-x}
    -\sum_{k=1}^n\frac1k P_{k-1}(x)P_{n-k}(x).
 \tag{19}
$$

这个公式可由 $Q_0=\operatorname{arctanh}x$、
$Q_1=x\operatorname{arctanh}x-1$ 和三项递推直接证明。
当 $n=2s+1$ 时，$Q_n^{\rm Leg}$ 为偶函数，且

$$
 Q_n^{\rm Leg}(0)=(-1)^{s+1}\frac{(2s)!!}{(2s+1)!!}
                 \in\mathbb Z_{(p)}^\times.
$$

取

$$
 \widetilde K_p(t)=Q_n^{\rm Leg}(2t)/Q_n^{\rm Leg}(0).
 \tag{20}
$$

它有初值 $1,0$，同样满足 $\mathscr D\widetilde K_p=-p^2\widetilde K_p$。
故

$$
 \widetilde K_p\equiv K\pmod{p^2,t^{N+1}}.
 \tag{21}
$$

因此 (12)–(13) 中的 $J,K$ 可以分别替换成 (16)/(20)，仍保留
模 $p^2$ 后除 $p$ 的准确性。这把所需参考写成了 Legendre 多项式、
有理函数和唯一的明确对数 $\log((1+2t)/(1-2t))$；
多项式次数 $n=(p-1)/2$ 仍随 $p$ 增长，不能将其称为固定次数模型。

例如 $p=7,N=4$ 时，

$$
 \widetilde J_7=1-\frac{20}{3}t^2,
 \qquad
 \widetilde K_7=1-24t^2+48t^4+O(t^6).
$$

它们与 $J=1+(3/2)t^2+(147/40)t^4+\cdots$、
$K=1+(1/2)t^2+(25/24)t^4+\cdots$ 的差在所需 jet 中被 $49$ 整除。
若 $m_4=[t^4]M$，(12) 的替换版本给
$C_4\equiv m_4+14-(7/2)(52/3)\pmod{49}$，
与准确值 $C_4=m_4-7/4$ 的差是 $-49\cdot11/12$。

## 6. 下一条真正需要的比较

本篇已经给出指定素数对角的无周期公式，及该公式所需的明确
模 $p^2$ 水平 Hasse 提升。尚未证明的是：除 $p$ 行 (13) 是否等于
固定代数模函数 $M$ 所在覆盖上的某个实际有限秩 Frobenius/相对
Bockstein 泛函，并且该泛函的指定值对无穷 $p$ 非零。

尤其，(17) 是准确的微分方程，不自动等于已经核实的 crystalline
Frobenius 比较；(19) 的对数是模参数函数，也不是一个已知非零的
固定代数单位的 $p$ 进对数。保留这两项区别，才不会把新的可计算
接口误写成尚未证明的无穷性结论。
