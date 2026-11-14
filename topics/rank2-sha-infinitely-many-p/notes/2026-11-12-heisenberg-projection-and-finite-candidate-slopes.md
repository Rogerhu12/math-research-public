# 十七处 Heisenberg 投影：进入实际 primitive 类型，但未传递已知斜率

日期：2026-11-12。状态：以下有限维公式与 Mellin 比较已证明。
本篇考察 O8 的具体有限候选方案：把已知导数非零的参考缩放差，
经固定挠点/Heisenberg 操作投影到实际 E17 类型。
结论是可以严格进入该类型，但投影后的导数恰好重新成为待证的
$J_p'(0)$，原先的固定对数非消失没有一起传过来。

## 1. 自然极化中的一个完全明确的投影

取 $i\equiv4\pmod {17}$，在
$V=\operatorname{Fun}(\mathbb F_{17},\mathbb C)$ 上令
$$
(D_af)(y)=f(ay),\qquad
(M_sf)(y)=\zeta_{17}^{\,sy}f(y)
\quad(a\in\mathbb F_{17}^{\times}).
\tag{1}
$$
这是参考 E1 splitting 下的自然极化；相应的局部 Schwartz 函数
支撑于 $\mathbb Z_{17}$，模 $17$ 局部常值。
参考向量为 $\mathbf1$。取四次特征
$\lambda(3)=-i$，定义
$$
e_\lambda=\frac1{16}\sum_{a\in\mathbb F_{17}^{\times}}
                  \lambda(a)D_a,\qquad
v_\lambda(y)=\lambda^{-1}(y)\mathbf1_{y\ne0}.
\tag{2}
$$
所以 $D_av_\lambda=\lambda^{-1}(a)v_\lambda$。
记 $\tau(\lambda)=\sum_{a\ne0}\lambda(a)\zeta_{17}^{a}$。
直接换元得，对 $s\ne0$，
$$
\boxed{
e_\lambda M_s\mathbf1
 =k_s v_\lambda,\qquad
k_s=\frac{\tau(\lambda)}{16}\lambda^{-1}(s)\ne0.
}
\tag{3}
$$
在 $y=0$ 处，两边都为零；在 $y\ne0$ 处，用 $b=asy$
即得该式。这里 $\tau(\lambda)\ne0$ 可由标准有限 Fourier
变换的可逆性直接得到，也可由 $|\tau(\lambda)|^2=17$ 得到。

因此 Heisenberg 调制确实突破了单纯 CM 缩放的 trivial 类型障碍。
R49/R51 和
[类型比较笔记](2026-11-12-theta-rational-cm-scaling-type.md)
核定的实际十七处向量为
$(\sqrt{17}/16)v_\lambda$，所以 (3) 只与它差一个固定非零代数常数。
此外 $4=3^{12}$，故 $\lambda(i)=\lambda(4)=1$；
全局 $\mu_4$ 平均不会消掉这条线。

## 2. 对已知五次缩放差实施这个投影

令
$$
\beta=2+i,\qquad q=\beta/\bar\beta=(3+4i)/5.
$$
用参考全局 splitting，置
$R_q=\omega_f^0(q^{-1})$。由全局 theta 分布的有理不变性，
$R_q$ 使第 $m$ 个 Hermite 矩乘 $q^m$。
对普通目标 $p$ 的 principal Mellin 变量 $T$，因而
$$
\mathcal J_p(R_q\phi,T)=Q_p(T)\mathcal J_p(\phi,T),\qquad
Q_p(T)=(1+T)^{\log_p\langle q\rangle/\log_p(1+p)}.
\tag{4}
$$
这里把所有向量放在同一 theta/周期尺度上。
回到 R51 的最小 E17 规范，只会再乘固定非零常数及
$(1+T)^c$；在已知中心为零时，其一阶非消失不变。
目标 $p\ge13,p\ne17$ 避开了此处的 $2,5,17$。

写参考向量为
$\phi^0=\mathbf1_{17}\otimes\phi^0_{\mathrm{out}}$，
并把 $R_q$ 分成十七处和其余有限处两部分。
因为 $q$ 在十七处是单位，
$$
R_{q,17}=D_{q^{-1}},\qquad
R_{q,17}\mathbf1=\mathbf1,\qquad
R_{q,17}v_\lambda=\lambda(q)v_\lambda.
\tag{5}
$$
设 $\phi^\lambda=v_\lambda\otimes\phi^0_{\mathrm{out}}$。
由 (3)、(5)，真正的非交换投影为
$$
\begin{aligned}
e_\lambda M_s(R_q-1)\phi^0
 &=k_s\,v_\lambda\otimes
           (R_{q,\mathrm{out}}-1)\phi^0_{\mathrm{out}}\\
 &=k_s\bigl(\lambda(q)^{-1}R_q-1\bigr)\phi^\lambda.
\end{aligned}
\tag{6}
$$
这一步没有把 $M_s$ 与 $R_q$ 错当成交换，也没有删掉局部特征值。

在所选十七处嵌入下，
$$
q\equiv14=3^9,\qquad \lambda(q)=-i.
$$
故 (4)、(6) 给出完整的准确公式
$$
\boxed{
\mathcal J_p(e_\lambda M_s(R_q-1)\phi^0,T)
 =k_s\bigl(iQ_p(T)-1\bigr)\mathcal J_p(\phi^\lambda,T).
}
\tag{7}
$$
而 $\mathcal J_p(\phi^\lambda,T)$ 与实际 $J_p(T)$ 只差上述
非零规范因子，特别地其中心也为零。因此
$$
\boxed{
\mathcal J_p'(e_\lambda M_s(R_q-1)\phi^0,0)
 =k_s(i-1)\mathcal J_p'(\phi^\lambda,0).
}
\tag{8}
$$
$(i-1)$ 在所有这些奇素数处都是单位。
原本能从参考五次差得到的
$\log_p(q)\mathcal J_p(\phi^0,0)$，在 (8) 中已不存在；
求导产生的那一项乘上了
$\mathcal J_p(\phi^\lambda,0)=0$。
所以 (7) 是到实际 primitive 中心导数的有效比较，
却不是一个新的非消失证明。

若另选 $q$ 使 $\lambda(q)=1$，则投影后的导数反而直接为
$k_sQ_p'(0)\mathcal J_p(\phi^\lambda,0)=0$。
把局部 Euler 因子安排成中心零点，也不能由此产生 rank2 primitive
导数的已知非零值。

## 3. 五维空间不等于五条可用的秩二曲线

伸缩群 $\mathbb F_{17}^{\times}$ 在 $V$ 上的分解非常直接：
平凡特征出现两次，基可取 $\delta_0,\mathbf1_{\mathbb F_{17}^{\times}}$；
每个非平凡特征出现一次。
再施加全局 $i$ 不变性，即要求在 $4\in\mathbb F_{17}^{\times}$
上的特征值为一，剩下
$$
\boxed{
V^{\langle D_4\rangle}
\simeq \mathbf1^{\oplus2}\oplus
\lambda\oplus\lambda^2\oplus\lambda^3.
}
\tag{9}
$$
其维数为五，与十七次、$i$ 不变 theta 截面的维数吻合。
但平凡的二维部分保留了参考 old 向量，非平凡部分才对应
不同的 primitive 局部类型。线性空间维数不能给出这三个部分的
Mordell–Weil 秩证书，更不能把 old 部分的非零导数移入它们。

特别是，即使另外独立证明某几个非平凡类型均来自秩至少二的曲线，
已知参考缩放差的非零性仍不说明它在这些类型的投影非零。
公式 (7)–(8) 已对实际 $\lambda$ 类型把这个缺口准确显示出来。

## 4. 有限 Heisenberg 轨道的望远镜公式

下面是便于继续尝试其他平移的抽象形式。
设固定投影 $\Pi$ 与 $R_q$ 交换，并以
$$
H_sR_q=R_qH_{\tau(s)}
$$
定义 Heisenberg 参数上的置换 $\tau$；选用 Weyl 规范或把中心相位
纳入参数，以保证此式确切成立。由 (4) 立即有
$$
\begin{aligned}
\mathcal J_p'(\Pi H_s(R_q-1)\phi,0)
={}&Q_p'(0)\mathcal J_p(\Pi H_{\tau(s)}\phi,0)\\
&+\mathcal J_p'(\Pi H_{\tau(s)}\phi,0)
-\mathcal J_p'(\Pi H_s\phi,0).
\end{aligned}
\tag{10}
$$
后两项是非交换操作额外引入的真实未知导数。
若在一个确实有限的 $\tau$ 轨道上按不变权重求和，它们望远镜消去，
完整表达式也就是
$$
(Q_p(T)-1)\,
\mathcal J_p\!\left(\sum_s c_s\Pi H_s\phi,T\right).
\tag{11}
$$
如果投影后的所有 primitive 中心均为零，(11) 的一阶导数仍为零。
不使用轨道不变权重时，(10) 的未知导数一般不会消去。
这里只对真实有限轨道作此断言；没有假定任意有理 CM 作用在整个
有限 adelic Schwartz 空间中的轨道均有限。

## 5. 当前有限覆盖路线还需要什么

有限候选抽屉原理本身完全足够：若能找到固定有限条已证秩至少二的
曲线，并证明对无穷多个 $p$，其 primitive 中心导数至少一个非零，
就有一条固定曲线在无穷多个 $p$ 成功。

当前明确取得的是 (7)，它已经把真实非交换投影比较到实际 E17；
没有取得一个独立已知非零、且完全位于这些 rank2 primitive 类型内
的导数组合。对于今后的候选，须补的是这种组合的非零证据，
而不是再利用有限维性或把参考的 auxiliary Euler 零点当成原始秩。

使用的完整接口：
R49/R51（2026-11-12）的实际向量与归一化；
[五次参考截面](2026-11-12-degree-five-theta-lucas-interface.md)；
[有理 CM 缩放类型](2026-11-12-theta-rational-cm-scaling-type.md)。
其中有限 Schwartz/Weil 规范的原始来源为
Yang，*Theta liftings and Hecke L-functions*，
J. reine angew. Math. 485 (1997), 25–53，式 (2.28) 与 Corollary 2.14：
[作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
有限 Gauss 投影与 (6)–(11) 的证明均已在本篇给出。
