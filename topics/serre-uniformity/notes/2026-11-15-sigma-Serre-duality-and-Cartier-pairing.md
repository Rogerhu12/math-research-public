# 原六截面的 Serre 对偶类与独立 Cartier 配对

日期：2026-11-15。状态：**下列配对及其界限已证明；原 critical 逐项乘积的非零仍未证明。**

本笔记接 R784、R788 和 `2026-11-15-sigma-stable-space-research.md`。
它把原六个临界 Taylor 功能写成真正的 $H^1(E,\mathcal O(-12O))$ 类，
并算出另一个确实非零的原有理 Cartier 配对。二者的区别必须保留；
不能把后一个单位直接移到前一个功能上。没有运行新的数学计算。

## 1. 原六维空间不是完整的次数六线丛系

设 $k=\overline{\mathbf F}_p$，$p=6N+5\ge41$，
$$
E:y^2=x^3-1,\qquad \omega=\frac{dx}{2y},\qquad D=\frac d\omega.
$$
这里先只谈真正的代数曲线及有理函数；不把完整普通 sigma Taylor 级数约化。
将 R784 的六截面除去原公共因子 $\sigma^{12}$，按 CM 权 $0,\ldots,5$ 排列为
$$
\begin{aligned}
v_0&=(x^3-4)^2,&v_1&=3xy(x^3-4),&v_2&=x^2(x^3-4),\\
v_3&=-2y(x^3+2),&v_4&=x^4,&v_5&=-x^2y.
\end{aligned}
\tag{SD1}
$$
令 $V=\langle v_0,\ldots,v_5\rangle_k$。这六个函数在 $O$ 的极阶依次为
$12,11,10,9,8,7$，首项系数依次为 $1,-3,1,2,1,1$。
另一方面，$L(6O)$ 的基可取 $1,x,y,x^2,xy,x^3$。
按极阶作三角消元，并用 genus one 的 Riemann--Roch 维数，准确得到
$$
L(12O)=L(6O)\oplus V,\qquad \dim L(12O)=12.
\tag{SD2}
$$

把 $V$ 看成 $\mathcal O(12O)$ 的截面系，它没有基点。
有限点处，$v_0$ 与 $v_4$ 没有共同零点：$x=0$ 时 $v_0=16$；
$x^3=4$ 时 $x^4\ne0$。在 $O$，$v_0$ 的极阶恰为 $12$，
所以作为 $\mathcal O(12O)$ 截面的值也非零。
因此不存在次数六的有效除子 $A$，使此嵌入下的
$V$ 等于 $H^0(\mathcal O(12O-A))$：后者的每个截面在 $A$ 上共同消失。
不能仅凭 $\dim V=6$，把它替换成一个完整的次数六线丛系。

取六次单位根 $\epsilon$，原 CM 作用为
$$
\iota_\epsilon^*x=\epsilon^{-2}x,\qquad
\iota_\epsilon^*y=\epsilon^{-3}y,\qquad
\iota_\epsilon^*\omega=\epsilon\omega.
$$
于是 $v_j$ 的权为 $j$。完整 $L(12O)$ 各权维数为
$$
(3,2,2,2,2,1),
\tag{SD3}
$$
可由基 $1,x,\ldots,x^6,y,xy,\ldots,x^4y$ 直接读出。
特别，只有权 $5$ 的完整空间已经由 $v_5$ 张成。

## 2. 不跨过非整边界的六个 Serre 类

沿用 R760/R765 的原局部参数和截断：
$$
u=x^{-1/2},\quad w=u^6,\quad
y=-u^{-3}\sqrt{1-w},\quad
\omega=\frac{du}{\sqrt{1-w}},
$$
$$
z=uZ(w),\qquad \sigma^6=u^6T(w),\qquad Z(0)=T(0)=1.
\tag{SD4}
$$
这里 $z$、$\sigma$ 先在原特征零规范下使用；只有下文真正需要的有限系数才约化。
$Z$ 的系数为
$\binom{2r}{r}/(4^r(6r+1))$；R765 已证 $T$ 至指标 $N$ 整。
下文至多使用两者的指标 $N-1$，所以所有约化都在已证整的范围内。

对 $0\le j\le5$，置
$$
m_j=p-11+j=6(N-1)+j,
\qquad
\lambda_j(q)=[z^{m_j}]\bigl(q(z)\sigma(z)^{12}\bigr)
\quad(q\in L(12O)).
\tag{SD5}
$$
原临界的六个截面系数正是 $\lambda_j(v_j)$。
在局部函数的商
$$
H^1(E,\mathcal O(-12O))
\simeq
\frac{k((u))}{k[E\setminus\{O\}]+u^{12}k[[u]]}
\tag{SD6}
$$
中，定义下列有限 Laurent 类：
$$
\boxed{
[a_j],\qquad
a_j\equiv u^{22-p-j}T(w)^2Z(w)^{10-j}\pmod{u^{12}}.
}
\tag{SD7}
$$
右端的意思是只取幂次小于 $12$ 的有限部分，不指定一个完整的特征 $p$ sigma 解。
从最小指数 $22-p-j$ 到 $11$，每次增加 $6$；所需指标确实至多为 $N-1$。

**准确的 Serre 配对。** 对每个 $q\in L(12O)$，有
$$
\boxed{\lambda_j(q)=\operatorname{Res}_O(q a_j\omega).}
\tag{SD8}
$$
证明先在特征零中作合法的有限系数换元：
$$
[z^{m_j}](q\sigma^{12})
=\operatorname{Res}_O(q\sigma^{12}z^{-m_j-1}dz),
$$
而
$$
\sigma^{12}z^{-m_j-1}
=u^{22-p-j}T^2 Z^{-p+10-j}.
$$
在所需有限指标内，$Z^{-p}\equiv1\pmod p$，因而得到 (SD7)。
$q$ 的极阶至多为 $12$，所以 $u^{12}$ 以上的部分不影响残数。
这证明 (SD8)。商 (SD6) 中的全局有理部分与此配对为零，由全局残数定理；
局部 $u^{12}$ 部分也与 $L(12O)$ 配对为零。这正是通常的 Serre 对偶残数描述。

由 CM 权，$\lambda_j$ 在权不等于 $j$ 的空间上为零。
若 R788 的**未筛选** critical 乘积全部为零，则 R788 已证
$$
\lambda_j(v_j)=0\quad(0\le j\le5).
\tag{SD9}
$$
所以六个类各自落入 $V$ 的正交补。
但按 (SD2)--(SD3)，该正交补维数为 $6$，对应各权的剩余维数
$(2,1,1,1,1,0)$；对于前五个类，(SD9) 并不等于类在整个 $H^1$ 中消失。
真正 primitive/Legendre 可见子集的失败甚至不能直接推出 (SD9)，见 R788 §6。

### 2.1 六个标量的共同有限系数形式

令 $C=(1-w)^{-1/2}$，$\ell=N-1$。将 (SD1)、(SD4) 逐项代入 (SD8)，
所有残数的公共幂次均为 $u^{5-6N}du$，所以准确得到
$$
\begin{aligned}
\lambda_0(v_0)&=[w^\ell]\,C T^2Z^{10}(1-4w)^2,\\
\lambda_1(v_1)&=-3[w^\ell]\,T^2Z^9(1-4w),\\
\lambda_2(v_2)&=[w^\ell]\,C T^2Z^8(1-4w),\\
\lambda_3(v_3)&=2[w^\ell]\,T^2Z^7(1+2w),\\
\lambda_4(v_4)&=[w^\ell]\,C T^2Z^6,\\
\lambda_5(v_5)&=[w^\ell]\,T^2Z^5.
\end{aligned}
\tag{SD9a}
$$
这只是 (SD8) 的显式坐标，不额外断言其中有一个非零。

## 3. 最后一个类为零时，Cartier 为零没有矛盾

最后一个完整权空间只有 $kv_5$。因而
$$
\lambda_5(v_5)=0\quad\Longleftrightarrow\quad[a_5]=0
\text{ in }H^1(E,\mathcal O(-12O)).
\tag{SD10}
$$
这里使用的是 (SD8) 的完整 Serre 对偶，不是只在 $V$ 上宣称非退化。
由 (SD7)，
$$
a_5\equiv u^{17-p}T^2 Z^5\pmod{u^{12}}.
\tag{SD11}
$$
若 (SD10) 成立，(SD6) 表明存在
$$
r\in L((p-17)O),\qquad r\equiv a_5\pmod{u^{12}}.
\tag{SD12}
$$
$a_5$ 的 CM 权为零。对 $r$ 作六次单位根平均可保留 (SD12)，
故可取 $r$ 也为权零。由于 $p-17=6(N-2)$，此时
$$
r\in k[x^3],\qquad \deg_{x^3}r\le N-2.
\tag{SD13}
$$

令 $\mathcal C$ 为 Cartier 算子。微分 $r\omega$ 只可能在 $O$ 有极点，
极阶小于 $p$，且其残数为零。Cartier 的局部公式因而表明
$\mathcal C(r\omega)$ 全纯。
另一方面，$r\omega$ 的 CM 权为 $1$；Cartier 的 $p^{-1}$ 半线性
及 $p\equiv-1\pmod6$ 给像的权为 $-1\equiv5$。
全纯微分空间 $k\omega$ 的权是 $1$，两权不同，于是
$$
\boxed{\mathcal C(r\omega)=0.}
\tag{SD14}
$$
这是由极阶和 CM 权自动得到的零值。
它不与 R574 的 $B\ne0$ 相冲突，也不迫使 $r=0$；
例如常数 $r$ 的 Cartier 像本来就是零，因为本曲线超奇异。
所以“最后一个 Serre 类若为零，就与 Cartier 单位矛盾”的直接推法不成立。

## 4. 原有理六截面确实给一个非零 Cartier 功能

现改看另一个、完全代数的映射
$$
\mathcal C:V\omega\longrightarrow H^0(E,\Omega_E^1)=k\omega.
\tag{SD15}
$$
它的像全纯：每个 $v_j\omega$ 的唯一可能极点阶至多 $12<p$，
且唯一极点的残数必须为零。

R574 给原常数 $B\in\mathbf F_p^\times$ 和
$$
D^{p-1}x=-B.
\tag{SD16}
$$
令 $\xi=-B^{-1}D^{p-2}x$，则 $D\xi=1$，所以 $d\xi=\omega$。
函数域 $k(E)$ 在 $k(E)^p$ 上以 $1,\xi,\ldots,\xi^{p-1}$ 为基。
写
$$
x=\sum_{i=0}^{p-1}c_i^p\xi^i.
$$
Wilson 公式给 $D^{p-1}x=-c_{p-1}^p$，故 $c_{p-1}^p=B$；
Cartier 的定义立即给
$$
\mathcal C(x\omega)=B^{1/p}\omega.
\tag{SD17}
$$

由 $Dx=2y$、$Dy=3x^2$，逐次微分得到
$$
D^4x=120x^3-48,\qquad D^5x=720x^2y,
$$
$$
D^6x=5040x^4-2880x.
$$
因此
$$
x^4=\frac{D^6x}{5040}+\frac47x.
\tag{SD18}
$$
所有显示分母对 $p\ge41$ 可逆；Cartier 消灭恰当微分
$(D^6x)\omega=d(D^5x)$，于是
$$
\boxed{\mathcal C(v_4\omega)=\mathcal C(x^4\omega)
=\frac47 B^{1/p}\omega\ne0.}
\tag{SD19}
$$
本规范中 $B\in\mathbf F_p$，故也可把 $B^{1/p}$ 写成 $B$。

对其它 $v_j$，输入 $v_j\omega$ 的 CM 权为 $j+1$，
Cartier 像的权为 $-(j+1)$。
要等于全纯微分的权 $1$，必须 $j=4$。因此
$$
\boxed{
\mathcal C(v_j\omega)=0\ (j\ne4),\qquad
\operatorname{rank}\bigl(\mathcal C|_{V\omega}\bigr)=1.
}
\tag{SD20}
$$
这给出了原曲线、原六截面、原 $B$ 上的真实非零配对；不是人为选择的非零抽象泛函。

## 5. 尚缺的是哪一个桥

(SD19) 作用于有理微分 $q\omega$。
(SD8) 作用于 $q a_j\omega$ 的局部残数，且六个 $a_j$ 含
原规范 $T^2Z^{10-j}$ 的不同有限部分。二者并非同一功能。
要从 (SD19) 推出临界非零，仍须证明一个准确的线性或几何关系，
把这个 Cartier 单位表达为六个原 $\lambda_j(v_j)$ 的组合，
并控制全部系数、极部及跨 $p$ 的项。本文没有这样的关系。

R788 的低六阶行列式 $36$ 证明的是 $V$ 在阶 $0,\ldots,5$ 的规范 jet 非退化；
它不自动给阶 $p-11,\ldots,p-6$ 的六个功能非零。
同样，完整 Serre 对偶的非退化不能替换为对真子空间 $V$ 的任意限制都非退化。
以上计算准确保留了一个可用的 Cartier 单位，以及它与所需临界功能之间尚未建立的桥；
未筛选 critical 全零与真正 primitive 可见集全零都仍未排除。

## 来源

- R574，`R574-completed-zeta-Cartier-input.md`：原 $D^{p-1}x=-B$ 及规范。
- R765，`R765-first-obstructed-sigma-coefficient-and-Cartier-unit-residual.md`：原 $T$ 的整截断边界。
- R784，`R784-original-full-sigma-kernel-and-primitive-preserving-left-inverse.md`：原六截面及全部规范首项。
- R788，`R788-original-cross-p-Cartier-correction-and-rank-six-coupling.md`：首 $p$ 矩形、未筛全零的六零行后果及 primitive 限制。
- `2026-11-15-sigma-stable-space-research.md`：原有理稳定空间及 (SD18) 的既有计算。
