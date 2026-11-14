# R305 — 新原首中央行的五项式、真实下一位与全纯二阶 primitive

日期：2026-11-13。**状态：以下原 $s_{p+1}$ 的有限五项表达、模 $p^2$ 的同一椭圆对数校正、同 degree-$34$ 的全纯二阶分解、完整系数转置及真实 CM13 边界均已证明。没有把分解中的单位常数当作原中央单位，也没有把所有全纯角向乘子加入原单源代数。**

本篇直接计算 R301 所需的真实首系数。与 R299 的 $q^p$ 对数进位不同，这里保留原 $S=z^6+\cdots$，读取它的 $z^{p+1}$ 系数。

## 1. 原偶角坐标和固定四次多项式

先保留 $b\ne0$，最后取 $b=17$；同一公式也适用于固定齐次换标后的 $b=1$。沿用 R288/R297 的规范
$$
y^2=x^3+b,\quad D=\partial_z,\quad
Dx=2y,\quad Dy=3x^2,\quad D\zeta=-x,\quad D\sigma=\zeta\sigma.
$$
取原点支
$$
u=x^{-1/2}=z+\cdots,\qquad t=-bu^6=-b/x^3,\qquad
\Theta=x\sigma^2,\qquad h(t)=z/u.
\tag{1}
$$
于是
$$
Du=\sqrt{1-t},\qquad
h(t)=\sum_{n\ge0}\frac{(1/2)_n}{n!(6n+1)}t^n,
\qquad h+6th'=(1-t)^{-1/2}.
\tag{2}
$$
这里 $t$ 是原 $z^6$ 的角坐标，不新增覆盖或 theta frame。

R297 的准确四次因子给
$$
\boxed{
A(t)=(1-t)(1+8t)\left(1+\frac47t+\frac{16}7t^2\right)
=1+\frac{53}7t-\frac{12}7t^2+\frac{80}7t^3-\frac{128}7t^4,
}
\tag{3}
$$
$$
\boxed{G(t)=\Theta^{17}A(t)=x^3S,\qquad S=-\frac tbG(t).}
\tag{4}
$$
所以 $S$ 的首项仍是 $z^6$。若使用 R299 的三次角 $q$，准确换参为
$$
t=-\frac{q^2}{4(1-q)},\qquad G=(1-q)F_q.
\tag{5}
$$
它同时核定原偶投影：$q\mapsto q/(q-1)$ 固定 $t$，而不是只保留偶数个 $q$ 次数。

原 theta 因子的低系数也有固定的超几何表达。令
$Z_N(t)=\log\Theta^N$，由 $D^2\log\Theta=-4bu^4$ 和 (1) 得
$$
t(1-t)Z_N''+\left(\frac56-\frac43t\right)Z_N'=\frac N9,
\tag{6}
$$
$$
\boxed{[t^n]Z_N=\frac{N}{3n}\frac{(1/3)_n}{(5/6)_n}\quad(n\ge1).}
\tag{7}
$$
例如 $Z_N'(0)=2N/15$。式 (6) 的逐项递推是
$z_n/z_{n-1}=(n-1)(n-2/3)/(n(n-1/6))$，与 (7) 相同，故没有未确定的积分常数。

以下始终取
$$
p=6s-1>7,\qquad p\ne17.
\tag{8}
$$
在所有次数 $<s$ 中，(2)、(7) 的分母和指数展开的阶乘都是 $p$ 单位。因此 $h,h^{-1},\log h,\Theta^{17}$ 在以下首行实际读取的窗口均整。此处不约化 $(7)$ 的第一个坏系数 $n=s$。

## 2. 原 $s_{p+1}$ 的准确五项式

写 $S(z)=\sum s_mz^m$。令 $X=-bz^6$，则 (1)、(2) 给
$$
X=t h(t)^6.
\tag{9}
$$
这是首系数一的正式换参。Lagrange 留数公式给出特征零等式
$$
\boxed{
s_{p+1}=(-b)^{s-1}[t^{s-1}]
\Theta^{17}A(t)\,(1-t)^{-1/2}h(t)^{-p-2}.
}
\tag{10}
$$
事实上 $S=-tG/b$，而
$$
[X^s]t(X)G(t(X))
=[t^{s-1}]G(t)\frac{h+6th'}{h^{6s+1}},
$$
正是 (10)。所有原 $t$、$z^6$ 和 $b$ 的尺度均已保留。

定义同一个固定特征零级数
$$
\mathcal C(t)=\frac{\Theta^{17}(t)}{h(t)^2\sqrt{1-t}},
\qquad c_n=[t^n]\mathcal C(t),\qquad c_n=0\ (n<0).
\tag{11}
$$
令
$$
\boxed{
T_p=\frac{(-b)^{s-1}}7
\left(7c_{s-1}+53c_{s-2}-12c_{s-3}+80c_{s-4}-128c_{s-5}\right).
}
\tag{12}
$$
在所读窗口 $h^{-p}\equiv1\pmod p$，故
$$
\boxed{s_{p+1}\equiv T_p\pmod p.}
\tag{13}
$$
这里 $c_n$ 仍由真实的 (2)、(7) 决定；(11) 的 theta 和 $h^{-2}$ 都没有被删掉。

如果需要直接在 $\mathbf F_p$ 中生成该行，只须取
$$
h_{<s}=\sum_{0\le n<s}\frac{(1/2)_n}{n!(6n+1)}t^n,
\quad
Z_{<s}=\sum_{1\le n<s}\frac{17}{3n}
\frac{(1/3)_n}{(5/6)_n}t^n,
\tag{14}
$$
然后在 $\mathbf F_p[t]/(t^s)$ 内计算
$e^{Z_{<s}}h_{<s}^{-2}(1-t)^{-1/2}$，再使用 (12)。指数只需 $s-1<p$ 次，所以没有隐藏的 $p!$。

另一个准确的首行表达是
$$
\boxed{
s_{p+1}\equiv6(-b)^{s-1}[t^{s-1}]
\frac{G+tG'}h\pmod p.
}
\tag{15}
$$
它来自 Lagrange 的导数形式
$s_{p+1}=(-b)^{s-1}s^{-1}[t^{s-1}](G+tG')h^{-p-1}$，并用
$s^{-1}\equiv6\pmod p$。式 (15) 不需要对非整的第 $s$ 个 theta 系数求导。

## 3. 首行真正下一位仍含同一个 $\log h$

置
$$
L_p=(-b)^{s-1}[t^{s-1}]A(t)\mathcal C(t)\log h(t)\in\mathbf Z_p.
\tag{16}
$$
这是原椭圆对数 (2)，不是另选的近似对数。在该有限窗口，
$$
h^{-p}=\exp(-p\log h)\equiv1-p\log h\pmod {p^2}.
$$
因此原第一行的下一位准确为
$$
\boxed{s_{p+1}\equiv T_p-pL_p\pmod {p^2}.}
\tag{17}
$$
特别，只有在 $s_{p+1}\in p\mathbf Z_p$（等价于 $T_p\in p\mathbf Z_p$）之后，才可写
$$
\boxed{\overline{s_{p+1}/p}=\overline{T_p/p}-\overline{L_p}.}
\tag{18}
$$
这与 R213 的原下一位现象一致，但 (3) 是本曲线的真实四次角源，全部因子六和 $(-b)^{s-1}$ 已重新证明。不能将 $T_p/p$ 单独代替原除 $p$ 行。

R301/R303 将原完整惰性中央导数的首层接到 $s_{p+1}$；本篇只计算这一指定系数及其下一位。式 (18) 没有把原完整导数的各个中央权独立置零；若继续读取完整导数模 $p^2$，仍须保留其其余权和全尾界。

## 4. 同 degree-$34$ 的全纯二阶分解

令
$$
F=\Theta^{17}=\sigma^{34}x^{17},\qquad
V=\frac{DF}{F}=34\zeta+34\frac yx,\qquad
\nabla_F=D-V.
\tag{19}
$$
对任意有理 $a(x)$，准确有 $\nabla_F^2(Fa)=F D^2a$。而
$$
D^2x^n=2n(2n+1)x^{n+1}+4n(n-1)b x^{n-2}.
\tag{20}
$$
取
$$
\begin{aligned}
a(x)={}&\frac{8991}{24640b}x^{-1}
-\frac{5911}{172480}x^{-4}
-\frac{801b}{30184}x^{-7}\\
&+\frac{6b^2}{539}x^{-10}
-\frac{16b^3}{637}x^{-13},
\qquad C=Fa,
\end{aligned}
\tag{21}
$$
$$
\boxed{\beta=-\frac{8991}{12320b}
=-\frac{3^5\cdot37}{2^5\cdot5\cdot7\cdot11\,b}.}
\tag{22}
$$
则原来源满足完整特征零恒等式
$$
\boxed{S=\nabla_F^2 C+\beta F.}
\tag{23}
$$

这不是有极 primitive。准确地
$$
C=\sigma^{34}\left(
\frac{8991}{24640b}x^{16}
-\frac{5911}{172480}x^{13}
-\frac{801b}{30184}x^{10}
+\frac{6b^2}{539}x^7
-\frac{16b^3}{637}x^4\right)
\tag{24}
$$
属于原 $H^0(E,\mathcal O(34O))$，首阶为二。$F,C,S$ 都保留同一 degree $34$；$C$ 在 $z\mapsto\omega z$ 下取 $\omega^2$，$F,S$ 取一。

**证明及唯一性。** 在输入基 $x^{-1-3j}$（$0\le j\le4$）和输出基 $x^{-3j}$（$0\le j\le5$）下，$D^2$ 的完整矩阵为
$$
M_b=\begin{pmatrix}
2&0&0&0&0\\
8b&56&0&0&0\\
0&80b&182&0&0\\
0&0&224b&380&0\\
0&0&0&440b&650\\
0&0&0&0&728b
\end{pmatrix}.
\tag{25}
$$
原 $S/F$ 的向量是
$\left(0,1,-53b/7,-12b^2/7,-80b^3/7,-128b^4/7\right)^t$。
将常数列 $(1,0,\ldots,0)^t$ 加到 (25)，得到可逆方阵；从末行向上消元准确给 (21)、(22)。这也证明在显示五维 primitive 空间内分解唯一。$\square$

质量不是额外假设：
$$
F(0)=1,\quad [z^2]C=\frac{8991}{24640b},\quad
2[z^2]C+\beta=0=S(0).
\tag{26}
$$
$\beta$ 对充分大的惰性好素数确为单位，但 $F=\Theta^{17}$ 并非已知 CM17 拉回的原秩零参考；$17$ 在本 CM 域中惰性。即使 R302 已支付 $\Theta$ 本身的原中央单位，也不能按乘法把它传给 $\Theta^{17}$。

分解还给出一个准确的原有理 de Rham 类：
$$
\boxed{\eta=\frac SF\,dz=d(Da)+\beta\,dz.}
\tag{26a}
$$
这里没有第三类对数残余，$Da$ 是显示的有理函数。因而在充分大的好约化处，惰性 $p$ 满足 $\mathsf C\eta=0$；普通 $p=6j+1$ 则有
$$
\mathsf C\eta=\beta\binom{3j}{2j}b^j\,dz\ne0.
\tag{26b}
$$
证明只需从 $(x^3+b)^{(p-1)/2}$ 提取 $x^{p-1}$ 系数：惰性时该指数不被三整除，普通时正是显示的单位二项式；Cartier 杀掉 (26a) 的 exact 项。$b,\beta$ 在这里的剩余域原本就在 $\mathbf F_p$。这也直接说明裸有理 Cartier 和本篇原 theta 首行不是同一个观察：惰性时前者已经恒为零，(10) 仍含必须支付的 $\Theta^{17}/h^2$。

## 5. 完整原权转置和首共振的真实抵消

写
$$
w=z^6,\quad F=f(w),\quad C=z^2g(w),\quad
E=6w\partial_w,\quad W(w)=\frac{EF}{F}=\sum_{i\ge1}W_iw^i.
$$
直接对 (23) 进行原微分，而不省去 $V$，得到
$$
\boxed{S=(E+1-W)(E+2-W)g+\beta f.}
\tag{27}
$$
因此对每个 $n\ge0$，全部原权准确为
$$
\boxed{\begin{aligned}
s_{6n}={}&(6n+1)(6n+2)g_n
-\sum_{i=1}^{n}(12n-6i+3)W_i g_{n-i}\\
&+\sum_{\substack{i,j\ge1\\i+j\le n}}
 W_iW_jg_{n-i-j}+\beta f_n.
\end{aligned}}
\tag{28}
$$
该式仍是原 $S$ 的完整系数恒等式；$W$ 的一次和二次项均保留。

在首权 $6s=p+1$，设原共同 sigma 坏系数为
$$
c=[w^s]\log(\sigma/z),\qquad \lambda=34c.
$$
由原椭圆参数的整性，$\lambda$ 是这里唯一可能的负一层；在该权附近，置
$$
\widehat f=e^{-\lambda w^s}f,\quad
\widehat g=e^{-\lambda w^s}g,\quad
\widehat W=W-6s\lambda w^s.
\tag{29}
$$
所读系数均整。故
$f_s=\widehat f_s+\lambda$、
$g_s=\widehat g_s+\lambda g_0$、
$W_s=\widehat W_s+6s\lambda$。
代入 (28)，$\lambda g_0$ 的总系数准确为
$$
(6s+1)(6s+2)-6s(6s+3)-2=0,
\tag{30}
$$
最后的 $-2$ 来自 (26) 的 $\beta=-2g_0$。所以首权可以用 (28) 的全部带帽量读取，而没有负层残余。

这次抵消在特征零中准确发生，并非把某个单独分量的单位进位宣称为非零。它同时说明：式 (22) 的单位不能脱离 $g_s$、$W_sg_0$ 和其余卷积项读取。那些真实整余项正是首中央行尚未消去的内容。

## 6. 真实 CM13 不保持这五维无极 primitive 空间

这里用固定齐次换标 $b=1$。置 $\delta=\sqrt{-3}$、
$\omega=(-1+\delta)/2$、$\gamma=4+\omega=(7+\delta)/2$，并使用 R297 的真实
$M_\gamma=[\gamma]_*[\bar\gamma]^*$，不改变 sigma frame 或迹的归一。

完整 $\omega^2$ 偶块为
$$
\mathcal W_2=\operatorname{span}
\{\sigma^{34}x^{1+3j}:0\le j\le5\}.
\tag{31}
$$
按 R297 的同一完整十三次纤维迹，得到准确六乘六矩阵 $M_2$；其全矩阵见证书，并满足
$$
\boxed{\det(T-M_2)=(T^3+\gamma^3)(T^3+\omega\gamma^3).}
\tag{32}
$$
在 (31) 的顺序中，原 $C$ 的向量是
$$
v_C=\left(0,-\frac{16}{637},\frac6{539},
-\frac{801}{30184},-\frac{5911}{172480},
\frac{8991}{24640}\right)^t.
$$
其实际 Krylov 空间维数为六；原 $z^2$ 系数观察的轨道也具有秩六。特别 $C$ 不是单一真实 CM13 特征来源。

更直接的边界是
$$
\boxed{[\sigma^{34}x]\,M_\gamma C
=d_0=\frac{-1111349706+4877443430\delta}{59594535}\ne0.}
\tag{33}
$$
两个整数分子的最大公因数为二，分母为
$3^5\cdot5\cdot7^3\cdot11\cdot13$。因此对所有 $p>13$ 的惰性素数，$d_0$ 在该未分歧二次整环中是单位：$1,\delta$ 在剩余域上线性独立，不能令两个分子同时为零。

这一列不能无证塞回 (24) 的五维无极空间。由 (20)，
$$
\boxed{\nabla_F^2(\sigma^{34}x)
=\sigma^{34}\left(992x^2+\frac{1088b}{x}\right).}
\tag{34}
$$
所以 $\nabla_F^2M_\gamma C$ 在 $T=(0,\sqrt b)$ 和 $-T$ 有真实一阶极，主部由 $1088b d_0\sigma^{34}/x$ 给出。两点都不是 $O$，$x$ 在那里是一阶参数、$\sigma$ 不为零。对于充分大的惰性好素数，这份边界主部也不消失。

**有限迹证书的完整性。** 使用 R297 已证明的
$$
Q_\gamma=\frac{\sigma(\gamma z)}{\sigma(z)^{13}},\qquad
x(\gamma z)=N_\gamma(x)/D_\gamma(x),
$$
在每条 $f_a=N_\gamma-aD_\gamma$ 的完整十三次纤维上，输入列的输出值准确为
$$
\operatorname{Tr}_{k[x]/(f_a)}
\left[\left(\frac{Q_{\bar\gamma}}{Q_\gamma}\right)^{34}
x(\bar\gamma z)^{1+3j}\right].
\tag{35}
$$
六个纤维 $a=2,\ldots,7$ 确定 (31) 中的输出，第七个 $a=8$ 独立核验；所有纤维均可分。迹用单首多项式恒等式
$\operatorname{Tr}(r)=[x^{12}](r f_a'\bmod f_a)$ 计算。既没有除以十三，也没有删去 $Q$ 的原常数。因此 (32)、(33) 是原 CM 算子的精确结论，不是裸有限 Weyl 矩阵的相位猜测。

## 7. 原有限来源与本篇结果的范围

原 $S$ 在 $O$ 的阶为六。若仅使用单源多项式格
$\mathbf Z_p[S]_{\le d}$，在 $w=z^6$ 下 $S=w+\cdots$。
当 $d<s$ 时，原连续矩阵的前 $d+1$ 行权均为零，并且在
$1,S,\ldots,S^d$ 上为单位下三角。因此这个单源格本身没有 primitive 深核；添加更高目标行不能消去已经存在的单位 minor。

另一方面，(4) 的 $G=x^3S$ 是真正全纯截面，且
$\operatorname{div}(t)=6O-3T-3(-T)$，$G$ 在 $T,-T$ 各五阶零。
因此 $G^m t^j$ 在 $0\le j\le\lfloor5m/3\rfloor$ 时确实全纯，保持原 charge $34m$。这是一份真实 theta 截面格，但尚不是已经付清的原 $\mathbf Q[S]$ 固定次数像；不能仅凭全纯就继承 R249 的三源导子包含或原中央零。

本篇对原中央问题新增的可直接输入是 (10)–(18) 的指定首行，而不是任意角乘子的观察。式 (23)–(30) 进一步将其放入同一个真实全纯二阶连接，式 (33)、(34) 记录继续用 CM 运输时必须支付的原边界。是否能由这些真实关系消去 (11) 中的 $\Theta^{17}/h^2$，仍须新的算术身份。

## 8. 证书

- [check-jzero-original-first-row-and-holomorphic-primitive.py](../scripts/check-jzero-original-first-row-and-holomorphic-primitive.py)
- [check-jzero-original-first-row-and-holomorphic-primitive.json](../scripts/check-jzero-original-first-row-and-holomorphic-primitive.json)

证书核 (3)–(7)、(20)–(26)、(27)–(30)，并用完整固定 CM13 纤维计算 (31)–(35)、两个秩六及真实主部。没有扫描目标素数；(10)–(18) 的所有素数断言由已显示的整窗口、Lagrange 恒等式和原特征零系数证明。
