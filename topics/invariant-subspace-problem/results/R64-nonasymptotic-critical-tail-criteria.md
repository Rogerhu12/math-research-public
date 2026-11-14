# R64：非渐近临界尾的移动归一化与平均相位缺陷判据

日期：2026-11-12（UTC）。子任务：critical_kernel。**状态：以下两个尾判据及明确例子已证明，属中间结论。**

本条继续[复参数推广稿](R61-complex-power-asymptotic-product-cyclicity.md)及[指数扩充证书](../notes/2026-11-12-power-range-negative-integral-0c.md)，不再要求 $\delta_j\sim c(j+2)^{-p}$ 具有一个固定复主系数。第一类允许截点依赖的归一化，覆盖相位无限旋转的对数复幂；第二类允许非零平均缺陷，覆盖持续小角摆动及正密度的完整符号翻转。全部结论仍针对真实进位算子，而非纯张量模型。

## 1. 共用的真实算子框架

取有界复数列 $s_j,t_j$，令 $\delta_j=s_j-t_j$。令 $R$ 是一个在 $0$ 邻域解析的标量函数，$R(0)=1$，使用通常全纯演算定义 $R(A)$。考虑
$$
Q=R(A)\prod_{j\ge0}(I+t_jN_j)(I+s_jN_j)^{-1},
\qquad D=I-Q.
\tag{1.1}
$$
在以下各条件下 $\delta\in\ell^1$；必要时也可直接将此项作为假设。有限前缀仍允许任意复数。

先前推广稿 §2–3 的对数及真实截断论证实际上只使用底参数有界和 $\delta\in\ell^1$，不使用任何幂渐近。因此它原样给出
$$
L=-\log R(A)+
\sum_j[\log(I+s_jN_j)-\log(I+t_jN_j)],
\quad Q=e^{-L},
$$
$$
D=L\Psi(L),\qquad
\Psi(z)=\frac{1-e^{-z}}z,\quad\Psi(L)\text{ 可逆}.
\tag{1.2}
$$
这里 $-\log R$ 使用在 $0$ 为零的解析芽。

对每个 $k\ge1$，存在只作用于低 $k$ 位的 $G_k$，以及一个固定常数 $C$，满足
$$
G_k^{2^k}=0,\qquad
T_k=G_k+\sum_{j\ge k}\delta_jE_j,\qquad
\|L-T_k\|\le C\eta_{k-1}.
\tag{1.3}
$$
$\|G_k\|$ 一致有界，$\eta_j\le e^{-770\,16^j}$。给定 $m>k$，置
$$
H_{k,m}=G_k+\sum_{k\le j<m}\delta_jE_j,\qquad
C_m=\sum_{j\ge m}\delta_jE_j.
$$
头尾交换，且
$$
H_{k,m}^{2^k+m-k}=0.
\tag{1.4}
$$
任意 $f\in\ker L$ 和复时间 $\tau$ 都满足精确误差恒等式
$$
e^{\tau H_{k,m}}f-e^{-\tau C_m}f
=\tau\int_0^1e^{(1-r)\tau H_{k,m}}e^{-r\tau C_m}T_kf\,dr,
$$
故
$$
\|e^{\tau H_{k,m}}f-e^{-\tau C_m}f\|
\le C|\tau|e^{C'|\tau|}\eta_{k-1}\|f\|.
\tag{1.5}
$$
这些公式保留全部真实进位误差。

尾范数的精确式为
$$
F_m(\tau)=\|e^{-\overline\tau C_m^*}1\|
=\prod_{j\ge m}P_{\mathbb C}(\tau\delta_j)^{1/2},
$$
$$
P_{\mathbb C}(z)=1-\operatorname{Re}z+\frac{|z|^2}{2}
=\frac{1+|z-1|^2}{2}.
\tag{1.6}
$$
记 $\ell_{\mathbb C}(z)=\frac12\log P_{\mathbb C}(z)$，则
$$
\|\nabla\ell_{\mathbb C}(z)\|\le\frac12,\qquad
|\ell_{\mathbb C}(z)|\le\frac{|z|}{2}.
\tag{1.7}
$$
以下两个判据分别利用 (1.7) 的小平均误差及更精细的相位误差。

## 2. 移动归一化判据

令 $1<p\le12/5$ 固定，$M=m+2$。假设对每个充分大的 $m$ 可选 $c_m\in\mathbb C\setminus\{0\}$，使
$$
\boxed{
E_m=\frac{M^{p-1}}{|c_m|}
 \sum_{j\ge m}
 \left|\delta_j-c_m(j+2)^{-p}\right|
\longrightarrow0.
}
\tag{2.1}
$$
另假设对每个 $\epsilon>0$，充分大的 $m$ 满足
$$
\boxed{|c_m|^{-1}\le M^\epsilon.}
\tag{2.2}
$$
这只限制归一化不能衰减得太快；不要求 $c_m$ 收敛、相位收敛或有固定极限。条件 (2.1) 为有限值时，差尾属于 $\ell^1$；基准尾也属于 $\ell^1$，所以它已经推出 $\delta\in\ell^1$。

**定理 2.1。** 在 (2.1)—(2.2) 下，(1.1) 的 $D$ 和 (1.2) 的 $L$ 都单射且值域稠密。

**证明。** 根据 $p$ 选择已认证区间：$1<p\le2$ 时选 $[a,b]=[1,20]$；$2\le p\le12/5$ 时选 $[a,b]=[1/10,30]$。对应
$$
J_p=g_{a,b}+\int_a^b h_p(u)\,d\nu_{a,b}(u)<0
$$
已有固定负常数，分别可用 $-13/100$ 或 $-1/2000$。

取移动复时间
$$
\tau=\frac{M^p}{c_m}u,\qquad a\le u\le b.
$$
由 (1.7)，与正实幂基准比较得到
$$
\left|
\log F_m(\tau)
-\sum_{j\ge m}\ell_{\mathbb C}
 \left(uM^p(j+2)^{-p}\right)
\right|
\le\frac{uM}{2}E_m.
\tag{2.3}
$$
基准尾的 Riemann 和误差仍至多 $u/2$，因而
$$
\boxed{
|\log F_m(\tau)-Mh_p(u)|
\le\frac b2+\frac{bM}{2}E_m=o(M)
}
\tag{2.4}
$$
在整个区间内一致成立。又 $|h_p(u)|\le u/[2(p-1)]$，所以某个固定 $C_1$ 给
$$
F_m(\tau)\ge e^{-C_1M}
\tag{2.5}
$$
对充分大的 $m$ 一致成立。

仍选 $k=\lfloor(3/4)\log_2M\rfloor$。由 (2.2)，可选 $\epsilon>0$ 使 $p+\epsilon<3$，并得到
$$
|\tau|\le bM^{p+\epsilon}.
$$
因此 (1.5) 的误差除以 $\|f\|$ 后至多
$$
\exp(-c_0M^3+O(M^{p+\epsilon}+\log M)),
$$
远小于 (2.5)。而
$$
p_m(u)=\left\langle
e^{(M^p/c_m)uH_{k,m}}f,1\right\rangle
$$
仍是次数至多 $M+M^{3/4}$ 的复多项式，$p_m(0)=\langle f,1\rangle$ 与 $m$ 无关。移动系数 $c_m$ 不影响这两个事实。

由尾范数界及加权 Bernstein–Walsh 估计，
$$
\log|\langle f,1\rangle|
\le O(1)+o(M)+M J_p+g_{a,b}M^{3/4}
\longrightarrow-\infty.
$$
故 $\ker L\perp1$。再用 $\ker L$ 对 $A$ 不变及 $1$ 对 $A^*$ 循环，得 $\ker L=0$。复对称性给稠密值域，(1.2) 传给 $D$。证毕。

**较弱的尺度假设。** (2.2) 是方便的充分条件。完整证明只需存在某个 $\beta\in(1/4,1)$，使
$$
M^p/|c_m|=o(M^{4\beta}).
$$
此时取 $k=\lfloor\beta\log_2M\rfloor$；真实误差的指数为 $-cM^{4\beta}$，头部次数增量为 $O(M^\beta)=o(M)$，仍可完成同一证明。

## 3. 相位无限旋转的明确对数复幂

取任意实数 $\sigma,\tau$，以及 $1<p\le12/5$，令
$$
\boxed{
\delta_j=(j+2)^{-p}(\log(j+3))^{\sigma+\mathrm i\tau},
}
\tag{3.1}
$$
其中
$$
(\log(j+3))^{\sigma+\mathrm i\tau}
=\exp\bigl[(\sigma+\mathrm i\tau)\log\log(j+3)\bigr].
$$
有限前缀可任意修改。取
$$
c_m=(\log(m+3))^{\sigma+\mathrm i\tau}.
\tag{3.2}
$$
其倒数模为对数实幂，故满足 (2.2)。

下面直接证明 (2.1)，不调用未说明的正则变差定理。记
$$
x_j=(j+2)/(m+2)\ge1,\qquad
L_j=(\log(j+3))^{\sigma+\mathrm i\tau}.
$$
则
$$
E_m=\frac1M\sum_{j\ge m}
 x_j^{-p}\left|\frac{L_j}{L_m}-1\right|.
\tag{3.3}
$$
固定 $R>1$ 时，$1\le x_j\le R$ 上
$$
\frac{\log(j+3)}{\log(m+3)}\to1
$$
一致成立，因此 $L_j/L_m\to1$ 也一致成立。这部分在 (3.3) 中的贡献趋零。

对远尾，固定 $0<\epsilon<p-1$。若 $\sigma\le0$，则 $|L_j/L_m|\le1$。若 $\sigma>0$，注意 $j+3\le(m+3)x_j$，故
$$
\left|\frac{L_j}{L_m}\right|
\le\left(1+\frac{\log x_j}{\log(m+3)}\right)^\sigma
\le x_j^{\sigma/\log(m+3)}
\le x_j^\epsilon
$$
对充分大的 $m$ 和所有 $j\ge m$ 一致成立。因此远尾可用
$$
\frac1M\sum_{x_j\ge R}x_j^{-p}(1+x_j^\epsilon)
\le C_{p,\epsilon}R^{1-p+\epsilon}+o(1)
$$
控制。先令 $m\to\infty$，再令 $R\to\infty$，即得 $E_m\to0$。

所以 (3.1) 的实际临界乘积都满足定理 2.1。当 $\tau\ne0$ 时，尾相位 $\tau\log\log(j+3)$ 无限旋转，没有固定复主系数；当 $\sigma\ne0$ 时，幅度相对于纯幂也不趋向非零常数。这些不是固定 $c$ 渐近定理的直接特例。

## 4. 非零平均相位缺陷判据

现在固定 $p=2$ 和任意 $c\ne0$，不要求任何渐近。写
$$
\delta_j=c(j+2)^{-2}z_j.
$$
对 $z\ne0$ 定义非负缺陷
$$
\mathfrak e(z)=
1-\operatorname{Re}\frac z{|z|}
+\frac12\bigl||z|-1\bigr|,
\qquad
\mathfrak e(0)=\frac12.
\tag{4.1}
$$
其相位部分是平方量级，而不是相位差的一阶绝对值。

对任意 $q\ge0$，
$$
\boxed{
\ell_{\mathbb C}(qz)
\le\ell_{\mathbb C}(q)+q\,\mathfrak e(z).
}
\tag{4.2}
$$
证明：若 $z=\rho\omega$，$|\omega|=1$，(1.7) 给
$$
\ell_{\mathbb C}(q\rho\omega)
-\ell_{\mathbb C}(q\omega)
\le\frac q2|\rho-1|.
$$
又
$$
P_{\mathbb C}(q\omega)
=P(q)+q(1-\operatorname{Re}\omega),
$$
利用 $\log(1+x)\le x$ 及 $P(q)\ge1/2$，
$$
\ell_{\mathbb C}(q\omega)-\ell_{\mathbb C}(q)
\le q(1-\operatorname{Re}\omega).
$$
相加即得。$z=0$ 由 (1.7) 直接给出。另有
$$
|z|\le1+2\mathfrak e(z).
\tag{4.3}
$$

假设
$$
\boxed{
\limsup_{m\to\infty}\mathcal E_m\le\frac1{40},
\qquad
\mathcal E_m=(m+2)
\sum_{j\ge m}\frac{\mathfrak e(z_j)}{(j+2)^2}.
}
\tag{4.4}
$$
这个条件由 (4.3) 推出 $\delta\in\ell^1$。

**定理 4.1。** 在 (4.4) 下，(1.1) 的实际 $D$ 和 $L$ 单射且值域稠密。

**证明。** 取原区间 $[1,20]$ 和固定复时间 $\tau=M^2u/c$。式 (4.2) 及基准 Riemann 和误差给
$$
\boxed{
\log F_m(\tau)
\le Mh_2(u)+\frac u2+uM\mathcal E_m.
}
\tag{4.5}
$$
另一方面，(1.7)、(4.3) 给
$$
\log F_m(\tau)
\ge-\frac u2\left(M+1+2M\mathcal E_m\right),
\tag{4.6}
$$
所以仍有统一的 $e^{-CM}$ 下界。真实 Duhamel 误差仍以 $e^{-cM^3+O(M^2)}$ 衰减。按 (1.4)—(1.5) 构造同一个头部多项式，得到
$$
\begin{aligned}
\log|\langle f,1\rangle|
&\le O(1)+M J_2(1,20)
 +\sqrt{20}\,M\mathcal E_m+g_{1,20}M^{3/4}\\
&\le O(1)-\frac7{400}M+o(M)+g_{1,20}M^{3/4}.
\end{aligned}
\tag{4.7}
$$
最后用了
$$
J_2(1,20)<-\frac{13}{100},\qquad
\sqrt{20}<\frac92,\qquad
-\frac{13}{100}+\frac9{80}=-\frac7{400}.
$$
由 (4.4) 可写 $\mathcal E_m\le1/40+o(1)$。右边趋向 $-\infty$，故核均值为零；实际 $A$ 不变性及 $1$ 的伴随循环性再排除全核。复对称性和 (1.2) 给稠密值域。证毕。

## 5. 没有渐近主项的明确尾类型

### 5.1 持续且任意的小角摆动

若充分远的每个 $j$ 都满足
$$
\frac{99}{100}\le|z_j|\le\frac{101}{100},
\qquad
\operatorname{Re}\frac{z_j}{|z_j|}\ge\frac{49}{50},
\tag{5.1}
$$
则 $\mathfrak e(z_j)\le1/50+1/200=1/40$。又
$$
M\sum_{j\ge m}(j+2)^{-2}\to1,
$$
所以 (4.4) 成立。各 $z_j$ 完全可以不收敛；例如相位在 $+1/5$ 与 $-1/5$ 弧度之间按任意规则持续切换，因 $\cos(1/5)\ge1-1/50=49/50$ 满足条件。

此结论允许比对复系数用一阶小扰动界更大的相位摆动：相位损失按 $1-\cos\theta$ 计算。

### 5.2 正密度的完整符号翻转

令
$$
z_j=
\begin{cases}
-1,&j\equiv0\pmod {100},\\
1,&\text{其他 }j.
\end{cases}
\tag{5.2}
$$
则 $\mathfrak e(z_j)=2$ 或 $0$。对单个模 $100$ 的剩余类，单调函数的和积分比较给
$$
M\sum_{\substack{j\ge m\\j\equiv0\ (100)}}(j+2)^{-2}
\longrightarrow\frac1{100}.
$$
故 $\mathcal E_m\to1/50<1/40$，定理 4.1 适用。

这里尾部在正密度的指标上完整翻转符号，不存在相对于任何固定 $c'$ 的纯幂渐近，也不满足 (5.1) 的小相位锥。它给出一个真正无序的实尾实例，而不是只在稀疏零密度集合上修改既有定理。

更一般地，若翻转指标集合有自然密度 $d\le1/80$，部分求和给
$$
M\sum_{\substack{j\ge m\\j\in S}}(j+2)^{-2}\to d,
$$
所以同样适用。此处使用的是存在的自然密度；没有把任意上密度界直接等同于该尾加权极限。

### 5.3 稀疏大偏差

条件 (4.4) 只约束加权尾平均，不要求逐项有界的相对偏差。作为例子，可在 $j=2^n$ 上令 $z_j$ 的模为 $j^\theta$、相位任意，其中固定 $0<\theta<1$；其他位置令 $z_j=1$。因为
$$
\mathfrak e(z_j)\le C(1+j^\theta)
$$
在这些位置成立，几何和给
$$
M\sum_{\substack{j\ge m\\j=2^n}}
(j+2)^{-2}\mathfrak e(z_j)
=O(M^{\theta-1})\to0.
$$
所以无限多个相对幅度趋无穷的异常仍被允许。实际 $\delta_j$ 在异常位置只有 $O(j^{\theta-2})$，保持可和。

## 6. 对两个 R16 乘积及其有限前缀的后果

上述两个判据都保证相应 $\delta=s-t\in\ell^1$，并对任意真正解析单位前因子成立。因此先前推广稿 §8 的完整归约继续适用：

- 两个 R16 向量先在共同有限截点写成不同有限前缀乘收敛乘积尾。
- 局部比值差为 $\delta_j$；相对零坐标标量的乘积通过尾均值乘积和 $\ell^1$ 比值差归一化，得到非零常数 $\kappa$。
- 不同有限前缀由真实有限多项式 $p_v(A),p_w(A)$ 作用于同一循环锚向量表示。
- 不同首阶用单射稠密的有限 $A$ 次幂及一个可逆因子处理；同首阶唯一临界系数给 $R(A)Q_{\rm tail}$，其中 $R$ 是明确有理单位。
- 定理 2.1 或 4.1 排除这个临界 $I-Q$ 的核并给稠密值域，所以全部非平凡线性组合非零且循环。

因此相位无限旋转的 (3.1)、任意持续小角摆动、正密度符号翻转和稀疏大异常，都可作为两个乘积局部比值差的新允许类型。这里仍没有对一般 $\mathcal A$ 元素有界除以 $A$。

## 7. 剩余边界

这些判据仍要求尾部在某种加权或移动尺度意义下保持足够的平均相位一致性。它们不处理任意可和复尾、不处理平均相位完全抵消的尾，也不证明任意三个乘积之和循环。移动归一化不等于随意为每个 $m$ 选择一个拟合常数：必须真正证明 (2.1) 及时间尺度条件。

所有结论只扩充明确临界乘子的单射稠密类及对应两乘积的循环类；具体 odometer 的一般普通不变子空间及完整 Hilbert ISP 继续未解决。


## 8. 同时覆盖非零二元解析芽

R62 的有限矩阵放大同样适用于本条两类 $L$。精确地，若 $0\ne F\in\mathbb C\{z,w\}$，则 $F(A,L)$ 单射且值域稠密，且把每个循环向量送到非零循环向量。

证明中只需在 (1.3) 的真实低位头中减去一个解析矩阵 $M(A_k)$。R62 给出 $\|M(A)-M(A_k)\|=O(a_k)$；若 $M(0)^d=0$，新的头部幂零阶至多 $d2^k$，故加上中间位后的次数是 $m+d2^k-k-1$。所有指数误差仍是 (1.5) 的形式，负指数常数及尾部边界界仍由定理 2.1 或 4.1 提供；只新增 $d g_{a,b}2^k=o(m)$。R62 的伴随矩阵、解析因式分解和复对称性随后逐项适用。此扩展未给任意范数闭包元素的单射性。
