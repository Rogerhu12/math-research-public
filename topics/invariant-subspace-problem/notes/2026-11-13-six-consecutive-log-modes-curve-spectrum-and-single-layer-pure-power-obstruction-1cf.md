# 工作接口：六个连续对数模式的全曲线谱障碍与固定阶纯 first 幂目标

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：以下有限代数、完整合并矩目标及实际 first 谱结论已逐项核验。本稿不作不循环反例，也不宣布原 Hilbert ISP 的正反解。

这里给出一个具体六模式复二次式：其一次全部标量纤维已有真实偏导逆证书，但对任何外层次数 $h\ge2$ 的多项式，其整个第 $h$ 矩层的任意方向都不能经生成式恒等化为某一个空谱 first 的普通纯 $h$ 次幂。这明确限制一类可能的后续接口，不排除多 first 矩形逆、其他闭图证书或原目标循环性。

## 1. 固定原目标及三个真实中心消去

使用原固定中心
$$
U_j=u_j/j,\qquad j=1,\ldots,6.
$$
定义
$$
g_6=5x_1x_5-32x_2x_4+27x_3^2,
$$
$$
g_7=x_1x_6-5x_2x_5+4x_3x_4,
$$
$$
g_8=x_2x_6-5x_3x_5+4x_4^2,
$$
$$
\boxed{F=g_8+i g_7+g_6.}
\tag{1.1}
$$
每组的物理曲线系数和都是零。
实际中心 $U_j\sim S^j/j$ 的各首系数也分别是
$$
1-4+3=0,\qquad
\frac16-\frac12+\frac13=0,\qquad
\frac1{12}-\frac13+\frac14=0.
\tag{1.2}
$$
所以普通最高物理曲线与原最高中心均相消。
最大变量的首系数为 $x_2+i x_1$，其真实行
$(\log(p+2)+i)/(p+2)$ 具有不可和的临界相位缺陷
$\asymp1/[p\log p]$。
最低变量的首系数是 $i x_6+5x_5$，同样没有可和相位缺陷。
这两条原 first 均属于 [R138](../results/R138-first-chaos-complete-spectrum-classification.md)
的全平面连续谱分支。

令
$$
v(z)=(1,z,z^2,z^3,z^4,z^5).
$$
因为每个 $g_s(v(z))=0$，
$$
F(x+t v(z))=F(x)+t\,p(z)\cdot x,
\qquad p(z)=K v(z),
\tag{1.3}
$$
其中 Hessian 为
$$
K=
\begin{pmatrix}
0&0&0&0&5&i\\
0&0&0&-32&-5i&1\\
0&0&54&4i&-5&0\\
0&-32&4i&8&0&0\\
5&-5i&-5&0&0&0\\
i&1&0&0&0&0
\end{pmatrix}.
\tag{1.4}
$$
直接有限行列式展开给
$$
\boxed{\det K=25600\ne0.}
\tag{1.5}
$$
因此 $F$ 的复二次秩为六，特别它不是两个线性形式的乘积。
以下也用到 $K$ 可逆。

## 2. 全部有限曲线方向的准确 first 谱

(1.4) 给
$$
\begin{aligned}
p_1&=iz^5+5z^4,\\
p_2&=z^5-5iz^4-32z^3,\\
p_3&=-5z^4+4iz^3+54z^2,\\
p_4&=8z^3+4iz^2-32z,\\
p_5&=-5z^2-5iz+5,\\
p_6&=z+i.
\end{aligned}
\tag{2.1}
$$
对于归一化六 log 模式，若 $p_6\ne0$，任何可和相位缺陷的方向只能是
$p_6$ 的相位。
指数 $5,4,3$ 都至少是最高指数6的一半，
所以相位缺陷可和必迫
$$
p_5/p_6,\quad p_4/p_6,\quad p_3/p_6\in\mathbb R.
\tag{2.2}
$$
理由是取其中最高的非实系数；其缺陷有正主阶
$(\log p)^{2j-7}/p$，当 $j\ge3$ 均不可和。
最低等号 $j=3$ 正是 $1/[p\log p]$。

下面证明 (2.2) 无解。
置 $z=x+iy$，$D=|z+i|^2>0$。
先由
$$
p_5/p_6=5\left(\frac1{z+i}-z\right)
$$
得到其虚部为零等价于
$$
y(D+1)=-1.
$$
因此 $y=-t$，其中 $0<t<1$，并且
$$
D=(1-t)/t,\qquad
\boxed{x^2=1/t-2+2t-t^2>0.}
\tag{2.3}
$$

准确多项式除法给
$$
p_4/p_6=8z^2-4iz-36+\frac{36i}{z+i}.
$$
其虚部为
$$
x(16y-4+36/D).
$$
由于 (2.3) 给 $x\ne0$，第二个实性条件迫
$$
\boxed{4t^2+6t-1=0.}
\tag{2.4}
$$

再作一次准确除法，
$$
p_3/p_6=-5z^3+9iz^2+63z-63i-\frac{63}{z+i}.
$$
用 $p_5/p_6$ 的实性关系及 (2.3)，其虚部成为
$$
\operatorname{Im}(p_3/p_6)
=x^2(9+15t)-5t^3-9t^2-63
=\frac9t-66-12t+12t^2-20t^3.
$$
由 (2.4)，$1/t=4t+6$、
$t^2=(1-6t)/4$、$t^3=(5/2)t-3/8$，故准确化为
$$
\boxed{\operatorname{Im}(p_3/p_6)=-44t-\frac32<0.}
\tag{2.5}
$$
与第三个实性条件矛盾。

唯一未包括的有限点 $z=-i$ 有
$$
p_6=0,\qquad p_5=5,\qquad p_4=36i.
$$
最高指数5与非同相的指数4仍给不可和相位缺陷，所以该点也不空谱。

射影端点 $z=\infty$ 对应 $K e_6=(i,1,0,0,0,0)$，
即 first $iU_1+U_2$。
它的缺陷与 $1/[p\log p]$ 同阶，同样不可和。

所有上述非零行都属于 $\ell^2\setminus\ell^1$。
由 R138 §1 的 (1.4) 及其实际近似谱证明，
$$
\boxed{
\sigma(X_{p(z)\cdot U})
=\sigma_{\mathrm{ap}}(X_{p(z)\cdot U})
=\mathbb C
\quad(z\in\mathbb{CP}^1).
}
\tag{2.6}
$$
所有谱点均连续；乘非零复常数或加入任意常数不改变这个结论。
这里没有将纯坐标模型的计算替代原实际域分类。

## 3. 一次纤维仍已有完整循环证书

(2.6) 不表示 $F(U)$ 不循环。
因为 $K$ 可逆，任取 $1\le j\le6$，
可以选固定向量 $b=K^{-1}e_j$，
使
$$
(b\cdot\nabla)F=x_j.
$$
一次矩层的六行互相独立，所以这是一个合法的实际矩目标；
在当前归一化坐标中无需额外 $\rho_j$ 比例。
完整二次 Bell 的高矩或累积量部分对一次显示变量的该导数为零。
因此原 $(F-\lambda)e^w$ 的真实偏导恰为
$X_{U_j,w}$，它有已付的全域有界交换逆。

[实像二次判据](../results/R150-appendix-real-image-quadratic-criterion-and-all-five-mode-translates.md)
或[全域偏导逆接口](../results/R150-appendix-global-derivative-inverses-real-quadratic-logarithmic-resonances-and-all-powers.md)
遂给
$$
\boxed{[F(U)-\lambda]e^w\text{ 对所有 }\lambda,w\text{ 非零且循环}.}
\tag{3.1}
$$
它使用任意一次矩方向，不限于 (1.3) 的物理曲线方向。
但一次层的任意方向不能直接提升为所有高阶合并层中的同一个纯幂方向。

## 4. 一个有限秩一幂引理

对 $h\ge2$，令
$$
\mathcal S_h=
\operatorname{span}_{\mathbb C}
\{(v(z)\cdot x)^h:z\in\mathbb{CP}^1\}.
$$
若一个非零向量 $r\in\mathbb C^6$ 满足
$$
(r\cdot x)^h\in\mathcal S_h,
$$
则 $r$ 本身必是某个 $v(z)$ 的非零标量倍。

给出自含证明。
所有二次 Hankel 小行列式
$$
q_{ij}(r)=r_i r_{j+1}-r_{i+1}r_j,
\qquad 0\le i<j\le4,
$$
均在 $(1,z,\ldots,z^5)$ 上为零。
任取线性形式 $L$ 使 $L(r)\ne0$。
齐次多项式 $q_{ij}L^{h-2}$ 在每个 $v(z)$ 上为零。
把它当作常系数微分算子作用于
$(r\cdot x)^h$，所得为
$h!q_{ij}(r)L(r)^{h-2}$；
由于 $(r\cdot x)^h\in\mathcal S_h$，这个值必须为零。
所以全部 $q_{ij}(r)=0$。

也就是矩阵
$$
\begin{pmatrix}
r_0&r_1&r_2&r_3&r_4\\
r_1&r_2&r_3&r_4&r_5
\end{pmatrix}
$$
秩至多一。
若 $r_0\ne0$，两行比例给
$r_j=r_0z^j$。
若 $r_0=0$，设最早非零坐标为 $r_k$；
当 $k\le4$ 时，第 $k-1,k$ 两列的小行列式为 $-r_k^2$，矛盾。
所以只有 $r_5\ne0$，就是射影无穷端点。
引理得证。

因 $K$ 可逆，同一结论经过线性变换得到：
$$
\boxed{
(r\cdot x)^h\in
\operatorname{span}\{(p(z)\cdot x)^h\}
\quad\Longrightarrow\quad
r\in\mathbb C^\times p(\mathbb{CP}^1).
}
\tag{4.1}
$$
这一结论只涉及有限标量多项式，不作任何无界算子坐标变换。

## 5. 整个固定 $h$ 阶矩层不能产生空谱 first 的纯幂

取任意非零外层多项式 $Q$、$\deg Q=h\ge2$，
最高系数为 $q_h\ne0$，并令 $G=Q(F)$。
总矩阶 $h$ 的原归一六模式合并键为
$$
(h,m),\qquad m=0,\ldots,5h.
$$
由完整生成式，
$$
\sum_m z^m\,\partial_{W_{h,m}}Q_G
=\frac{(-2)^{h-1}}{h!}
Q_{(v(z)\cdot\nabla)^hG}.
\tag{5.1}
$$
(1.3) 给准确链式等式
$$
(v(z)\cdot\nabla)^hG=h!q_h(p(z)\cdot x)^h.
\tag{5.2}
$$
全部较低外层次数在此导数下为零。
所以 (5.1) 的普通标量目标空间准确为
$$
\boxed{
\operatorname{span}_{\mathbb C}\{(p(z)\cdot x)^h:z\in\mathbb{CP}^1\}.
}
\tag{5.3}
$$
说明“准确”：有限多项式 $z\mapsto(p(z)\cdot x)^h$ 的系数张成与其取值张成相同，
可在任意足够多不同有限参数上使用通常的有限 Vandermonde 逆；
最高系数也包含无穷端点。
第 $h$ 层的全部合法合并方向恰好对应这些系数的任意固定线性组合。
这不拆开重复的原矩行。

若某个非零目标成为
$c(r\cdot x)^h$、$c\ne0$，则 (4.1) 强迫
$r$ 是某个 $p(z)$ 的非零标量倍。
因此其原实际 first 的谱由 (2.6) 为整个复平面，不能是空谱 first。

若目标被写成一个非恒定仿射 first 符号
$a_0+r\cdot x$ 的纯 $h$ 次，同样比较最高齐次项得到上述必要条件；
加入常数不改变 (2.6)。
所以准确得到
$$
\boxed{
\begin{gathered}
h\ge2,\quad G=Q(F),\quad \deg Q=h;\\
\text{第 }h\text{ 矩层中，没有任何非零合法方向的普通标量目标}\\
\text{是某个空谱 first 符号的纯 }h\text{ 次幂。}
\end{gathered}}
\tag{5.4}
$$

普通矩变换 $H\mapsto Q_H$ 是有限标量线性单射：
将全部高矩变量置零，剩余就是 $H$ 的一次变量表达。
因此 (5.4) 确实限制通过完整生成式取得该种单 first ordinary Bell 目标的方式，
没有把不同显示多项式通过未付的实际商关系等同。

这只是固定第 $h$ 层的结论；没有把混合不同总矩阶的方向纳入本节排除范围。

## 6. 本稿没有证明的断言

(5.4) 不排除某个目标的完整 Bell 本来具有其他来源的全域有界逆；
也不排除由多个空谱 first 构成的矩形、多项式 Bézout、变化列或其他真实算子证书。
混合不同总矩阶的方向同样不受 (5.4) 的单层结论限制。
它没有证明 $Q(F(U))e^w$ 不循环，更不是原算子存在非平凡不变子空间的证据。

已完成的是一个明确六模式例子、全部射影曲线方向的实际谱计算，
以及完整第 $h$ 矩层线性目标中单 first 普通纯幂接口的准确限制。
原一次全参数结论 (3.1) 与此障碍并存。
