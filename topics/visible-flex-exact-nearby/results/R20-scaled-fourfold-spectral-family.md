# R20：更扁的可解四重背景族与一致的有限阶可解性

2026-11-10，visible-exact-astra-76e8。

**状态：已证明的中间结论。** 这是 R12 的实际参数族扩展，用于更扁背景
的数值探索；不是把旧背景的几何、真实尾或非线性常数不经证明地转授给
新对象。本文只支付完整谱、闭嵌入背景、真实无穷小场，以及相应的有限阶
可解性。有限振幅候选、直径、reach 和精确等距存在仍须另付。

## 1. 明确对象与全部频率结论

令整数 $k\ge1$，置
$$
\mu=k\sqrt2,\qquad A_k=\mu^2+\frac{\mu}{4},\qquad
V_k=A_k\operatorname{sech}^2x-\mu^2,
\qquad L_{n,k}=-\partial_x^2-n^2V_k.
\tag{1.1}
$$
这些均为 $L^2(\mathbb R)$ 上定义域 $H^2(\mathbb R)$ 的自伴算子。
则全部整数 $n\ge1$ 中，唯一的核发生于 $n=4$：
$$
\ker L_{4,k}=\operatorname{span}\{y_k\},\qquad
y_k=\operatorname{sech}^{4\mu}x.
\tag{1.2}
$$
其余全部谱点，含第四模的非零谱，满足
$$
|\lambda|>\frac1{2000k^2n^2},
\qquad
|\lambda|>\frac1{8k^2n^2}\quad(n\in4\mathbb N).
\tag{1.3}
$$
对四重空间的真实逆，第四模在 $y_k^\perp$ 上取逆，有
$$
\|u\|_2\le8k^2n^2\|f\|_2,\qquad
\|u'\|_2\le12k^3n^3\|f\|_2,\qquad
\|u''\|_2\le17k^4n^4\|f\|_2.
\tag{1.4}
$$
因此在增加扁率参数时，完整频率结论仍然有明确常数；不靠有限扫描
宣称无高频共振。

## 2. 谱公式、唯一核与整数范数

R4/R12 的实参数因式分解对任意势深度成立。令
$$
\ell_n(\ell_n+1)=A_kn^2,\qquad \ell_n>0.
$$
则本质谱为 $[\mu^2n^2,\infty)$，其下全部谱为
$$
E_{n,j}=\mu^2n^2-(\ell_n-j)^2,\qquad
j\in\mathbb Z,\quad0\le j<\ell_n.
\tag{2.1}
$$
设 $E_{n,j}=0$，代入 $\ell_n=\mu n+j$，得到
$$
\mu p=q,\qquad
p=n^2-4n(2j+1),\qquad q=4j(j+1).
\tag{2.2}
$$
$\mu=k\sqrt2$ 无理而 $p,q$ 为整数，故 $p=q=0$，即 $j=0,n=4$。
反过来 $\ell_4=4\mu$，正基态就是 (1.2)。

剔除这个零点后，$2k^2p^2-q^2$ 是非零整数，且
$$
(\ell_n-\mu n-j)(\ell_n+\mu n+j+1)=\frac{\mu p-q}{4}.
\tag{2.3}
$$
对于全部整数频率，$A_k<(5/2)k^2$、$\ell_n<2kn$ 给
$$
|p|\le21kn^2,\quad |q|\le24k^2n^2,\quad
\mu|p|+|q|<56k^2n^2,\quad
\ell_n+\mu n+j+1<7kn.
$$
故
$$
|\mu p-q|\ge\frac1{\mu|p|+|q|}>\frac1{56k^2n^2},
$$
$$
|E_{n,j}|>
\frac{\mu n}{4\cdot56k^2n^2\cdot7kn}
=\frac{\sqrt2}{1568k^2n^2}>
\frac1{2000k^2n^2}.
\tag{2.4}
$$

若 $n=4r$，则 $p\in16\mathbb Z$、$q\in8\mathbb Z$，
所以非零范数 $2k^2p^2-q^2$ 的绝对值至少 $64$。
利用 $n\ge4$ 和 $\ell_n<8kn/5$，还有
$$
|p|<15kn^2,\quad |q|<12k^2n^2,\quad
\mu|p|+|q|<35k^2n^2,\quad
\ell_n+\mu n+j+1<5kn.
$$
于是
$$
|E_{n,j}|>
\frac{64\mu n}{4\cdot35k^2n^2\cdot5kn}
=\frac{16\sqrt2}{175k^2n^2}>
\frac1{8k^2n^2}.
\tag{2.5}
$$
本质谱下端也满足相同界。对第四模，除基态外的最小特征值实际为
$8\mu-1>10k$。

## 3. 逆的导数界与深度横截

由谱定理得到 (1.4) 第一式。因为 $|V_k|\le\mu^2=2k^2$，
$$
\|u''\|_2\le\|f\|_2+2k^2n^2\|u\|_2
\le17k^4n^4\|f\|_2.
$$
再由 $\|u'\|_2^2\le\|u\|_2\|u''\|_2$ 得中间式。
这些是全实线逆，不是截断边界的代用品。

若只把深度 $A$ 当作参数，第四模最低特征值满足
$$
E_{4,0}'(A_k)=-\frac{32\ell_4}{2\ell_4+1}
=-\frac{128\mu}{8\mu+1}\in(-16,-14).
\tag{3.1}
$$
每个整数 $k\ge1$ 都有相同的严格横截区间。
它仍只控制最低模；固定非零深度改动后，不允许自动继承 (2.5)
的全部高频算术距离。

## 4. 真正的闭 $C^2$ 旋转背景

取偶解
$$
h''+V_kh=0,\qquad h(0)=1,\quad h'(0)=0.
\tag{4.1}
$$
先证明其正性。因为
$\ell_1(\ell_1+1)=\mu^2+\mu/4<\mu(\mu+1)$，有 $\ell_1<\mu$。
因式分解给
$$
L_{1,k}\ge\mu^2-\ell_1^2>0.
$$
更明确地，
$$
\mu-\ell_1=\frac{3\mu}{4(\mu+\ell_1+1)},
\qquad
\mu^2-\ell_1^2>\frac{3\mu^2}{4(2\mu+1)}>\frac{\mu}{4}.
\tag{4.2}
$$
最后一步用了 $\mu>1$。若 $h$ 在正轴有首零点，将其偶延拓限制在
两首零点之间，分部积分会与 (4.2) 矛盾。因此 $h>0$。

当 $x\ge2$ 时，$\operatorname{sech}^2x<4/49$，且
$A_k/\mu^2=1+1/(4\mu)<5/4$，所以
$$
h''/h=\mu^2-A_k\operatorname{sech}^2x>\frac12\mu^2.
$$
若 $h'$ 永不变正，反向能量比较给指数衰减，从而产生
$L_{1,k}$ 的非零 $L^2$ 零解，矛盾。故 $h$ 最终增长。
Riccati 比较遂给
$$
h'/h\to\mu,\qquad h''/h\to\mu^2.
\tag{4.3}
$$
如 R8/R16 的积分因子论证，由 $\mu\ge\sqrt2$ 还可得
$h(x)=c_ke^{\mu x}(1+O(e^{-2x}))$，且固定阶导数有相应界。

定义
$$
a=1/h,\qquad z(x)=\int_0^x h^{-2},\qquad
X_k=a e_r+z e_z,\qquad
s_x=\frac{\sqrt{1+h'^2}}{h^2}.
\tag{4.4}
$$
弧长和高度两端均有限，内部 $z$ 严格递增，所以没有自交。
在上极点以 $a$ 为图半径，
$$
z_a=-1/h',\qquad z_a/a\to-1/\mu,\qquad
z_{aa}=-h''h^2/(h')^3\to-1/\mu.
\tag{4.5}
$$
因此真实 Cartesian Hessian 连续延拓为 $-\mu^{-1}I$，
两极补点后为闭 $C^2$ 嵌入球面。两极 Gauss 曲率为 $\mu^{-2}$；
腰圈的 Gauss 曲率为 $-\mu/4$。这些局部值不能替代全局 reach 证明。

实际径向 Sturm 势仍为
$$a^3a_{ss}/z_s^4=-h''/h=V_k,$$
故此几何与第 1—3 节的算子来自同一个对象。

## 5. 非刚体场和极点正则性

取
$$
U=y_k/h,\qquad T=-U/4,\qquad
W=(h'/h)y_k-y_k'/16,
$$
$$
Z_k=U\cos4\theta\,e_r+T\sin4\theta\,e_\theta+
W\cos4\theta\,e_z.
\tag{5.1}
$$
R4 对任意 $h$、任意整数角模已经逐项验证：
$L_{4,k}y_k=0$ 正好等价于三个线性等距方程。
因而 $Z_k$ 是真实全局无穷小等距场。
其固定阶 $x$ 导数在尾部为 $O(e^{-4\mu|x|})$；
Cartesian 至多二阶求导只增加 $O(h^2)$，故全部二阶导数趋零。
两极补零后得到 $C^2$ 场和零二 jet。
腰圈法向分量为 $\cos4\theta$，排除了刚体速度场。

## 6. 与任意有限阶递推相容的紧支均值方向

为保证 R16 的核投影在新背景中仍实际可解，不能直接复制旧常数。
明确取
$$
\phi_k(x)=
\begin{cases}
\exp\!\left(1-\dfrac1{1-64k^2x^2}\right),&|x|<1/(8k),\\
0,&|x|\ge1/(8k).
\end{cases}
\tag{6.1}
$$
用 $h_\alpha=h e^{\alpha\phi_k}$ 定义真实轴对称变分 $V$。
其径向部分紧支，竖直部分在两帽端各为常数；帽外 $dV=0$。
R16 的准确微分恒等式与两次分部积分给横截分母
$$
\kappa_k=-32\int_{\mathbb R}\phi_k
\left[(y_k'-wy_k)^2+15q\,y_k^2\right]dx,
\quad w=h'/h,\quad q=h''/h.
\tag{6.2}
$$
这里公式不要求 $\mu=\sqrt2$，因为角模仍是 $4$。

在 $|x|\le1/(8k)$，
$$
-\frac{3k}{8}<q
=\mu^2\tanh^2x-\frac{\mu}{4}\operatorname{sech}^2x
\le\frac1{32}-\frac{7k}{20}\frac{63}{64}<-\frac14.
$$
所以 $h$ 向外递减且 $h\le1$，而
$$
h\ge1-\frac{3k}{16}x^2>\frac78,\qquad
|h'|\le\frac{3k}{8}|x|\le\frac3{64},\qquad |w|\le\frac3{56}.
$$
又 $|y_k'/y_k|=4\mu|\tanh x|<3/4$，得到
$$
(y_k'-wy_k)^2+15q\,y_k^2<-\frac{11}{4}y_k^2.
$$
在 $|x|\le1/(16k)$ 上，
$\phi_k\ge e^{-1/3}>2/3$，且
$y_k^2\ge e^{-4\mu x^2}>125/128$。所以
$$
\boxed{\kappa_k>\frac{1375}{192k}>\frac7k.}
\tag{6.3}
$$

R16 第 4—5 节的递推现在全部合法：每个偶数阶允许一个均值
$\alpha_{2j}V$，下一奇数阶以
$-\langle y_k,f_{2j+1,4}^0\rangle/\kappa_k$ 精确消核；
其余模式使用 (1.4)，第四模使用真实核外逆。
源的尾衰减及极点二 jet 的归纳只把 $\sqrt2$ 换为 $\mu$。
由于固定阶数下模式仍有限，所有这些场属于真实闭面 $C^2$ 空间。
因此每个固定整数 $k$、每个指定有限奇数阶，都有 R16 型的准确有限阶
近似及完整非均值度量残差恒等式。
这仍没有给随阶数增长的统一界或无穷级数收敛。

## 7. 数值探索与后续范围

$k=4$ 对应当前脚本探索的 $\mu=4\sqrt2$。数值上更小的直径可能降低
达到相对可见位移所需的腰圈振幅，但这种解释不是已证全局几何界，
也不保证 Newton 收敛。

R11/R14/R15/R19 若原本固定 $\mu=\sqrt2$，不能仅通过本谱定理自动应用
于 $k>1$。例如负势帽和增长斜率的原单位已经改变；必须重写坐标和
范数转换、实际尾接线、完整源、曲率及支撑常数。本文只将新背景的
谱与有限阶可解性从猜测改成了完整证明，主完成条件仍未满足。
