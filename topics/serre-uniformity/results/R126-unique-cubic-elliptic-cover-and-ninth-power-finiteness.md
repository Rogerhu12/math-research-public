# R126：唯一三次域椭圆覆盖与九次幂分母支的定性闭合

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本文给 [R120](R120-nine-cartan-twist-and-explicit-cubic-cover.md) 的固定亏格二曲线一个唯一的、完整保留分母的椭圆覆盖接口；另由 Faltings 有限性关闭 R19 中九次幂分母的无限素数分支。

两个结论的范围如下：

1. 该亏格二曲线的每个有理点，都提升到一个固定三次域上的同一个非分歧二覆盖，进而映到一个固定椭圆四次曲线。没有随点变化的平方扭曲参数。
2. 存在一个绝对常数，排除 R19 的所有充分大素数且分母参数为九次幂的实际非 CM 解。这是无条件、目前未有效计算的常数；不覆盖非九次幂参数，也不声称已列出全部有理点。

## 1. 实际分解与准确范数恒等式

保持
\[
\mathcal C:\ y^2=S(x),\qquad
S(x)=7x^6+12x^5-36x^4-10x^3+84x^2-72x+19.
\]
令
\[
L=\mathbb Q(r),\quad r^3-3r-4=0,\qquad \epsilon=r^2+r-7,
\]
并定义
\[
\begin{aligned}
A(x)&=(r^2+3r+3)x^2-(2r^2+3r+2)x+(r^2+r-1),\\
B(x)&=(3r^2-5r-3)x^4+(2r^2-r-6)x^3\\
&\quad+(-9r^2+18r+3)x^2+(6r^2-17r+6)x-r^2+5r-3.
\end{aligned}
\tag{126.1}
\]
在整个多项式环中有
\[
\boxed{AB=S,\qquad N_{L/\mathbb Q}(A(x))=S(x),\qquad
N_{L/\mathbb Q}(\epsilon)=1.}
\tag{126.2}
\]
第二个范数是三个系数嵌入后的多项式相乘，不是逐系数取范数。对第一式取范数，还得到 $N(B(x))=S(x)^2$。

实际 resultant 为
\[
R=\operatorname{Res}_x(A,B)=10773r^2+23652r+19521,
\qquad N_{L/\mathbb Q}(R)=2^8\,3^{14}.
\tag{126.3}
\]
后面保留 $2$ 上的两个不同素理想，不能只看有理素数支撑。所有恒等式均可在 $r^3=3r+4$ 中直接核验。末尾标准库程序准确计算乘积、resultant、范数及已知点；$N(A(x))=S(x)$ 另用次数至多六的多项式在七个整数处的精确值核验。

## 2. 整环、类数及单位平方类

$P(T)=T^3-3T-4$ 没有有理根，判别式为 $-324$。只有 $2,3$ 可能整除幂基指标。Dedekind 指标判据给：

- 模 $2$，$P=T(T+1)^2$；取 $g=T(T+1),h=T+1$，则 $(P-gh)/2=-T^2-2T-2$ 与模二的 $g,h$ 没有共同因子。
- 模 $3$，$P=(T-1)^3$；取 $g=T-1,h=(T-1)^2$，则 $(P-gh)/3=T^2-2T-1$ 在 $T=1$ 处模三非零。

所以
\[
\mathcal O_L=\mathbb Z[r],\qquad D_L=-324,\qquad (r_1,r_2)=(1,1).
\tag{126.4}
\]
记二上的分歧、非分歧素理想分别为
\[
\mathfrak p=(2,r+1),\qquad \mathfrak q=(2,r),\qquad
(2)=\mathfrak p^2\mathfrak q.
\]
它们的范数都是二。以下等式及范数准确给出
\[
N(r+1)=N(r-2)=2,\quad (r-2)(r+1)^2=2,\quad
\mathfrak p=(r+1),\quad\mathfrak q=(r-2).
\tag{126.5}
\]
三全分歧；$\theta=-r^2+r+3$ 满足 $N(\theta)=3$ 和 $(r+1)\theta=r-1$，故三上唯一素理想也主化。模五的 $P$ 没有根，故五惰性。

Minkowski 每类理想代表界为
\[
\frac4\pi\frac{3!}{3^3}\sqrt{324}=\frac{16}{\pi}<6.
\]
范数至多五的素理想已经全部主化；范数四的理想也仅由上述范数二素理想组成。因此
\[
\boxed{h_L=1.}\tag{126.6}
\]
这不调用 GRH 或未认证的类群输出。

Dirichlet 单位定理给范数一单位群秩一、无挠，其模平方商恰有两个元素。这里只需非平凡代表，不需要证明基本单位。模二有 $r^3=r,r^4=r^2$，所以
\[
(a+br+cr^2)^2\equiv a^2+(b^2+c^2)r^2\pmod2.
\tag{126.7}
\]
任何平方的 $r$ 系数为零，而 $\epsilon\equiv1+r+r^2$ 的该系数为一。故 $\epsilon$ 不是 $L$ 中的平方：若有平方根，因 $\epsilon$ 为整单位，该根也是整单位，才可应用此式。结合 $N(\epsilon)=1$，
\[
\boxed{\mathcal O_L^{\times,N=1}/
(\mathcal O_L^{\times,N=1})^2=\{1,\epsilon\}.}
\tag{126.8}
\]
范数一单位若有范数为负一的平方根，将根乘以负一即得到范数一的根，平方不变。因此这也准确描述它在 $L^\times/L^{\times2}$ 中的类。

## 3. 每个原始有理点只有一个平方类

无穷远要求 $y/x^3=\pm\sqrt7$，所以 $\mathcal C$ 没有有理无穷远点。任意有理点可写为
\[
x=u/v,\quad y=z/v^3,\quad
u,v,z\in\mathbb Z,\quad v\ne0,\quad (u,v)=1,\quad
z^2=S_h(u,v).
\]
有理数 $z$ 的平方是整数，故 $z$ 为整数。令 $A_h,B_h$ 为二次、四次齐次化，得到
\[
A_h(u,v)B_h(u,v)=z^2,\qquad N(A_h(u,v))=z^2.
\tag{126.9}
\]
$z\ne0$，因为 R120 的 $S$ 在有理数上不可约。

若素理想 $\mathfrak l\nmid R$，原始性保证 $(u:v)$ 是剩余域中的射影点，resultant 单位排除 $A_h,B_h$ 在该点同时消失。乘积等式遂给
\[
v_{\mathfrak l}(A_h(u,v))\equiv0\pmod2
\qquad(\mathfrak l\nmid R).
\tag{126.10}
\]
在 $\mathfrak q=(2,r)$ 处，$R\equiv19521\equiv1$，所以该处也已包含。由 (126.3)，其余可能例外只有 $\mathfrak p$ 和三上唯一素理想。它们的剩余次数都是一，而范数等式又给
\[
v_2(N(A_h))=v_{\mathfrak p}(A_h)+v_{\mathfrak q}(A_h)\equiv0\pmod2,\qquad
v_3(N(A_h))=v_{\mathfrak l_3}(A_h)\equiv0\pmod2.
\]
因此它们的赋值也为偶数，全部素理想均已覆盖。

类数一给 $A_h=\delta a^2$，其中 $a\in\mathcal O_L$、$\delta$ 为范数一单位。吸收单位平方，由 (126.8) 只有 $\delta=1,\epsilon$ 两种可能。对每个原始 $(u,v)$，$A_h$ 的 $r$ 系数是
\[
3u^2-3uv+v^2\equiv u^2+uv+v^2\equiv1\pmod2.
\tag{126.11}
\]
最后一步仅有 $(u,v)\equiv(1,0),(0,1),(1,1)$ 三种情况。式 (126.7) 排除 $\delta=1$，于是
\[
\boxed{A_h(u,v)=\epsilon a^2,\quad
B_h(u,v)=\epsilon b^2,\quad
z=\epsilon ab,\quad a,b\in\mathcal O_L.}
\tag{126.12}
\]
取 $b=z/(\epsilon a)$ 即得第二式；其平方为整元，故 $b$ 整。符号也保留原来的 $z$。

这里使用二次、四次的齐次分解。除以 $v^2,v^4$ 后，平方因子分别吸收到 $a/v,b/v^2$，没有变化的分母平方类。这是全部有理点进入同一覆盖的关键。

## 4. 固定非分歧二覆盖及椭圆四次曲线

令 $\mathcal D/L$ 为
\[
\epsilon a^2=A(x),\qquad\epsilon b^2=B(x)
\tag{126.13}
\]
的光滑射影模型。映射
\[
\mathcal D\longrightarrow\mathcal C_L,\qquad
(x,a,b)\longmapsto(x,\epsilon ab)
\]
是几何连通的非分歧二覆盖。$A$ 的零点都是 Weierstrass 点，在 $\mathcal C$ 上各给偶数阶零点；在两个无穷远点的极点阶也都是二，因此添入 $\sqrt{A/\epsilon}$ 不分歧。

该函数并非 $\overline L(\mathcal C)$ 中的平方：若 $(f+gy)^2=A/\epsilon$，则 $fg=0$。$g=0$ 要求平方自由二次式 $A$ 在 $\overline L(x)$ 中为平方；$f=0$ 要求 $1/(\epsilon B)$ 为平方。两者都不成立。Riemann–Hurwitz 因而给 $g(\mathcal D)=3$。

忘掉 $a$ 得到固定亏格一曲线
\[
\boxed{\mathcal E/L:\quad \epsilon b^2=B(x).}\tag{126.14}
\]
$B$ 平方自由且次数四，所以上述亏格准确为一。以下两个实际提升同时给出 $L$ 点：

| $x$ | $y$ | $a$ | $b$ |
|---:|---:|---|---|
| $1$ | $2$ | $r^2+2r+2$ | $r^2+2r+1$ |
| $-1$ | $12$ | $4r^2+9r+8$ | $r^2+4r+1$ |

每行均满足 (126.13) 和 $\epsilon ab=y$。指定第一行在 $\mathcal E$ 中的像为原点，即把它视为一条固定椭圆曲线。

全部 $\mathcal C(\mathbb Q)$ 因此包含于单个椭圆 Chabauty 问题
\[
\{Q\in\mathcal E(L):x(Q)\in\mathbb Q\}.
\tag{126.15}
\]
从该上集恢复 $\mathcal C(\mathbb Q)$ 时，再检查 $A(x(Q))/\epsilon$ 为 $L$ 中的平方。通过后，$\epsilon ab$ 的平方为有理数；因 $[L:\mathbb Q]=3$，$L$ 不含二次子域，故 $\epsilon ab$ 自动有理。没有遗漏的下降条件。

本文未给出 $\operatorname{rank}\mathcal E(L)$ 上界，也未列出 (126.15)。若秩小于三，可以继续椭圆 Chabauty；秩条件本身不等于全部有理点已求完。

## 5. 九次幂分母的 $p\to\infty$ 分支已经定性关闭

[R114](R114-exact-cm-congruence-depth-from-minimal-deformations.md) 已证明对 R19 全部实际解，
\[
Z=Y^9\Longrightarrow E[9]\simeq(y^2=x^3-x)[9].
\]
R120 将这样的 $E$ 的 $j$ 值送入**固定**亏格二曲线 $\mathcal C(\mathbb Q)$ 在有理函数 $J$ 下的像。

Faltings 的 Mordell 定理保证 $\mathcal C(\mathbb Q)$ 有限，所以
\[
\mathscr J=\{J(P):P\in\mathcal C(\mathbb Q),\ J(P)\ne\infty\}
\]
是固定有限集。R120 已证有理整 $j$ 纤维只有 CM；R19 的实际非 CM 解则满足
\[
\operatorname{den}(j(E))=|Z|^p=|Y|^{9p}>1.
\tag{126.16}
\]
此为既约正分母的等式，使用 R19 的完整互素条件。

定义
\[
B_9=\max\left(
37,\left\{\frac{-v_q(j)}9:
j\in\mathscr J\setminus\mathbb Z,\quad v_q(j)<0\right\}
\right),
\tag{126.17}
\]
内集合为空时只取 $37$。它是有限的绝对常数：曲线、函数和有限集均与 $E,p,Y$ 无关。任取实际解的 $q\mid Y$，有
\[
9p\le9p\,v_q(Y)=-v_q(j(E))\le9B_9.
\]
故
\[
\boxed{p>B_9\Longrightarrow
\text{R19 的实际非 CM 解中，}Z\text{不是九次幂。}}
\tag{126.18}
\]
所有更高 $3^n$ 次幂支（$n\ge2$）也随之排除。这里不需要随二次扭曲统一的 Serre 常数，也没有假定已计算 $\mathcal C(\mathbb Q)$；只用了固定曲线有限性和准确分母指数。

目前 (126.17) 未有效求值，不给 $B_9=37$ 或任何数值界。完整点分类及 (126.14) 是改进显式门槛的途径。**就本课题存在绝对常数的目标而言，九次幂子支已定性关闭；R19 的真正渐近剩余为非九次幂，尤其非立方参数。** 这不能扩大为所有 $Z$ 的统一排除。

## 6. 证书与来源

~~~sh
python3 -B topics/serre-uniformity/notes/verify_r126_cubic_elliptic_cover.py --check
~~~

- [标准库精确核验](../notes/verify_r126_cubic_elliptic_cover.py)。
- [有限证书](../notes/r126_cubic_elliptic_cover_certificate.json)，SHA256 c48edccc81e22962a4318342b74ec6a9c87d829b92d7cbc97617dc3eca18fb59。

证书核验全部多项式恒等式、素理想生成元范数、坏二素理想的区分、单位非平方判据和两个实际提升。整环、类数及全部赋值的论证在正文。发现阶段曾用 PARI 子域/因式分解，最终证明不依赖未认证的数域黑箱。

固定曲线和模映射来自 R120，同余深度来自 R114。有限性输入为 G. Faltings，*Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*，Inventiones Mathematicae **73** (1983), 349–366，Satz 7：[原文](https://math.uchicago.edu/~drinfeld/Deligne%27s_conjecture_Manin_conf/Faltings_argument/Faltings.pdf)。这里只用固定亏格至少二曲线的有理点有限性，不把它解释成有效高度或已经完成的点枚举。
