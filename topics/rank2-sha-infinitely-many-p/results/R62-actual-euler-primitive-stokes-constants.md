# R62. 实际 Euler 原函数的完整 Stokes 分解

日期：2026-11-12。**状态：完整证明；没有证明中央常数无穷次非零。**

固定 $A=A_1=\sum\beta_mz^m=z^4+O(z^8)$，定义不随 $p$ 改变的
$$
\mathscr H(z)=\int_0^z A(w)\,dw/w.
$$
对每个惰性 $p\ge7$，令 $d=p+1$、$a=17c$、$v_p(c)=-1$，并置
$$
\rho=p^{-1/(2p)},\qquad S=p^{-p/(p^2-1)}<\rho.
$$
R54 的实际分解为 $A=e^{az^d}G$，$G$ 在闭 $\rho$ 盘的 Tate 代数中且
$\|G\|_\rho\le\rho^4$。令 $\mathscr H=e^{az^d}K$，按次数模 $d$ 分解。

## 1. 逐余类的真实常数

对 $j=0,4,\ldots,d-4$，令 $g_{j,h}=[z^{dh+j}]G$，
$$
\mathcal J_{p,j}(u)=\sum_{h\ge0}a^{-h}g_{j,h}(u)_{\underline h}.
$$
其中 $\mathcal J_{p,0}=J_{A,p}$。有准确值
$\mathcal J_{p,j}(k)=k!a^{-k}\beta_{dk+j}$，并定义
$$
\mathcal S_0=-J_{A,p}'(0),\qquad
\mathcal S_j=\mathcal J_{p,j}(-j/d)\quad(j>0).
$$
下降阶乘与上升阶乘的转换及完整余类递推给
$$
K=\frac1d\sum_j\mathcal S_jE_{p,j}+\mathcal R_p,
\qquad \mathcal R_p\in\mathbb Q_p\langle z/\rho\rangle,
\quad\|\mathcal R_p\|_\rho\le\rho^{p+3},
\tag{1}
$$
其中
$$
E_{p,0}=e^{-az^d},\qquad
E_{p,j}=z^j\sum_{h\ge0}\frac{(-a)^hz^{dh}}{(j/d)_{\overline{h+1}}}\quad(j>0).
$$
每个模型的收敛半径准确为 $S$，且沿 $h=p^n$ 的系数不能满足闭 $S$
盘的 Tate 衰减。不同模型支撑在互不相交的余类，不能互相抵消。
(1) 的余项不仅有界，其加权系数也严格趋零。

## 2. 中央条件与实际非中央单位

令 $P_0$ 为次数模 $d$ 的中央投影。则
$$
\boxed{J_{A,p}'(0)=0
\iff P_0K\in\mathbb Q_p\langle z/\rho\rangle
\iff\|P_0K\|_\rho\le\rho^{p+3}.}
\tag{2}
$$
若中央导数不为零，$P_0K$ 的半径准确为 $S$，并且在闭 $S$ 盘也不属于
Tate 代数。这把目标导数识别为实际 Euler 方程的中央 Stokes 常数。

另一方面，全部非中央块有
$\mathcal S_j\equiv\beta_j\pmod p$，实际首项给
$$
\boxed{\mathcal S_4\equiv1\pmod p\qquad(p\ge7\text{ 惰性}).}
\tag{3}
$$
同次数参考 $f_0=\theta((4-i)z)=e^{az^d}G_0$ 的 $G_0$ 在闭 $\rho$ 盘可逆。
故整个固定函数 $\mathscr H/f_0=K/G_0$ 对所有这些素数的半径都准确为
$S$，不论中央导数是否为零。
不能把 (2) 的 $p$ 依赖投影改善升级为整个固定函数的半径改善。

## 3. 固定范数不混合这些常数

取 $b=69$、$p\nmid b$，先用 R61 的真实函数范数，再作线性 shifted 变换。
新次数 $17b^2$ 使用指数 $a_b=b^2a$，得到
$$
\mathcal J^{[a_b]}_{bA(bz),j}(u)
 =b^{j+1}(b^{p-1})^u\mathcal J_{p,j}(u).
$$
所以中央常数只乘 $b$，其他常数各乘一个显式 $p$ 进单位。
这个范数关系准确保留各块的消失性，未将 (3) 传给目标中央块。
式 (2) 仍需一个处理实际 $p$ 依赖投影的全局整数格或相对周期比较。

逐项递推、全部尾界、闭边界计数及范数正规化的证明全文见
[实际 Euler 原函数的全余类 Stokes 分解](../notes/2026-11-12-inert-euler-primitive-stokes-decomposition.md)。


## 4. 同一整数序列的惰性相邻比证书

非中央单位块同时给一个真正可逆的局部自参考。
若 $B_1=A_1^{(4)}$，使用同一首坏指数的变换满足
$$
J_{B_1}(u)=\prod_{r=1}^4(du+r)\mathcal J_{p,4}(u),\qquad
\mathcal J_{p,4}\in1+p\mathbb Z_p\langle u\rangle.
$$
因此 $J_{B_1}(0)=24$，在 $p\mathbb Z_p$ 上为单位；整个单位盘上有显式零点，
不可声称处处可逆。令 $Q_{17}=J_{A_1}/(17J_{B_1})$，则
$Q_{17}\in pu\mathbb Z_p[[u]]$，且对正整数 $p\mid k$ 准确有
$$
Q_{17}(k)=h_{dk}/h_{dk+4}=a_{dk/4}/(17a_{dk/4+1}).
$$
这是同一固定整数流，与 ordinary R60 使用同一相邻比。
令 $n\ge1$、$m_n=(p+1)p^n$、$b_n=(p^n-1)/(p-1)$，则
$$
v_p(h_{m_n+4})=b_n,\qquad
\frac{h_{m_n}}{p^nh_{m_n+4}}
 \equiv\frac{J_{A_1,p}'(0)}{24\cdot17}\pmod{p^{n+1}}.
$$
于是
$$
\boxed{J_{A_1,p}'(0)\ne0
\iff\exists n\ge1:\ v_p(h_{m_n})<b_n+2n+1.}
$$
这在惰性处仍仅作为初级有限的充分条件使用。
分母本身通常被高次 $p$ 整除，不能直接把它当作单位。
根端调用旧整数流独立复算 $p=7,n=1$，得到
$v_7(h_{56})=3$、$v_7(h_{60})=1$、$h_{56}/(7h_{60})=28\bmod49$。
证明全文及准确 $17$ 缩放见
[惰性相邻 Hurwitz 比证书](../notes/2026-11-12-inert-adjacent-hurwitz-ratio-certificate.md)。
