# R1034：原 bare 高系数的有限线性化

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126。
o2_high_coefficient / root。

**已证明：在原两行和原相位中，R990/R1005 的固定幂系数可准确降为
一个指定有理函数 \(N_{p,r}/P\) 的单次系数。**
降阶只在有依据的模 \(z^\ell\) 范围内使用；原完整共振误差不被删去。
在 \(r=2\) 行，分子次数准确为 \(3k+1<\deg P\)，给全部分母根的
完整留数和。\(r=8\) 行可能有多项式部分，必须保留。

这不证明目标系数非零，也不把单个总留数条件改写成每个局部留数为零。
本篇没有新的数学程序执行或旧素数窗口重算。

## 1. 原两行、相位与指定输入

保留
\[
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
r=\begin{cases}
2,&p\equiv11\pmod{12},\\
8,&p\equiv5\pmod{12}.
\end{cases}
\]
写
\[
n=p-r=3m,\quad k=\lfloor p/12\rfloor,\quad
\ell=(p+1)/3,\quad d=\ell-1.
\]
全部新降阶恒等式在 \(\mathbf F_p\) 中进行。原正模型为
\[
E_+:y^2=x^3+1,\qquad \omega=dx/(2y),\qquad
(g_2,g_3)=(0,-4),
\]
且
\[
c_n^+=[z_1^nz_2^{n-1}]
 \frac{\sigma_+(z_1+z_2)}{\sigma_+(z_1)\sigma_+(z_2)}.
\]
下文超几何变量 \(z\) 与 \(z_1,z_2\) 不同。
原负模型在这两行的相位保持 \(c_n^-=-c_n^+\)。

取 R990/R1005 已指定而非任意选择的多项式
\[
B(z)={}_2F_1(-k,k+4/3;4/3;z),\qquad \deg B=k,
\]
\[
P(z)=\sum_{i=0}^{d}
 \frac{(1/12)_i(7/12)_i}{(2/3)_i\,i!}z^i,\qquad \deg P=d.
\tag{1034.1}
\]
这里全部需要的分母为 \(p\) 单位，且 \(P(0)=B(0)=1\)。
本篇的 Jacobi 多项式 \(B\) 不是旧 sigma 首极标量。

设
\[
Q(z)=4+12z\frac{B'}B-\frac z{1-z},\qquad
A_0(z)=(1-z)B(z)^2,\qquad g(z)=\frac{B(z)}{P(z)}.
\tag{1034.2}
\]
R1005 给原目标的精确接口
\[
\mathcal J_{p,r}=[z^m]Q\,g^r,\qquad
\boxed{\quad
 c_{p-r}^+=\frac{(-32)^m(r-1)!}{4}\mathcal J_{p,r}.
 \quad}
\tag{1034.3}
\]
外因子为单位，尚不能据此断言 \(\mathcal J_{p,r}\ne0\)。

## 2. 有限降阶的合法范围

令
\[
C(z)=\sum_{i=0}^k\frac{b_i}{3i+1}z^i,\qquad
B(z)=\sum_{i=0}^k b_i z^i.
\]
R1005 的完整恒等式是
\[
K(z)=(1-z)\{PB+3z(PB'-P'B)\}
       =1-\frac{z^\ell C(z)}{B(1)^2}.
\tag{1034.4}
\]
因此作为完整有理函数，有
\[
g+3zg'=\frac{K}{A_0}\,g^2.
\tag{1034.5}
\]
由于 \(K(0)=1\) 且 \(K\equiv1\bmod z^\ell\)，才可在有限级数环中写
\[
\boxed{\quad
 g^2\equiv A_0(g+3zg')\pmod{z^\ell}.
 \quad}
\tag{1034.6}
\]
两行分别有
\[
\begin{array}{c|c|c|c}
p&r&m&\ell\\ \hline
12k+11&2&4k+3&4k+4\\
12k+5&8&4k-1&4k+2 .
\end{array}
\]
所以全部所求系数严格位于共振前。
不能把 (1034.6) 宣称为没有 \(K\) 的全局恒等式。
下文的 \(z\partial_z\) 保持理想 \((z^\ell)\)，
所有乘子在零处正则，故每步降阶都保留这一精度。

## 3. 有限线性递推

定义有理函数 \(F_j\)，从 \(F_r=Q\) 开始，向下递推
\[
\boxed{\quad
F_{j-1}=
 \frac{(j-1-r)A_0F_j-3z(A_0F_j)'}{j-1},
 \qquad j=r,r-1,\ldots,2.
\quad}
\tag{1034.7}
\]
这些分母最多为 \(7\)，均为原允许素数下的单位。

为证明递推，先由 (1034.6) 得
\[
g^j\equiv A_0g^{j-1}
 +\frac{3zA_0}{j-1}(g^{j-1})'
 \pmod{z^\ell}.
\]
令 \(U=A_0F_j,V=g^{j-1}\)。对 \(m<\ell\)，精确系数恒等式
\[
[z^m]\,z(UV)'=m[z^m]UV
\]
给
\[
\begin{aligned}
[z^m]F_jg^j
&=[z^m]\left\{
 \left(1+\frac{3m}{j-1}\right)A_0F_j
   -\frac{3z}{j-1}(A_0F_j)'
       \right\}g^{j-1}\\
&=[z^m]F_{j-1}g^{j-1},
\end{aligned}
\]
最后一步使用原 \(3m=p-r\equiv-r\bmod p\)。
迭代得到
\[
\boxed{\quad
\mathcal J_{p,r}=[z^m]F_1g=[z^m]\frac{N_{p,r}}P,
\qquad N_{p,r}=B F_1 .
\quad}
\tag{1034.8}
\]
因此原 bare 系数现在是
\[
\boxed{\quad
c_{p-r}^+=\frac{(-32)^m(r-1)!}{4}
                [z^m]\frac{N_{p,r}}P .
\quad}
\tag{1034.9}
\]
没有修改 \(P\) 的截断归一、原 \(m\)、原 mod \(9\) 行或相位。

递推首先清掉 \(Q\) 的表观分母，因为
\[
A_0Q=(4-5z)B^2+12z(1-z)BB'\in\mathbf F_p[z].
\tag{1034.10}
\]
此后每步都是多项式乘法与 \(z\partial_z\)，故 \(F_1,N_{p,r}\)
确为指定多项式。逐次次数估计给
\[
\deg F_1\le(r-1)(2k+1),\qquad
\deg N_{p,r}\le k+(r-1)(2k+1).
\tag{1034.11}
\]

## 4. 原 \(r=2\) 行的完整闭式与次数

此时唯一一步为
\[
F_1=-A_0Q-3z(A_0Q)'.
\]
将 (1034.10) 微分并使用原 Jacobi 方程
\[
z(1-z)B''+\left(\frac43-\frac73z\right)B'
           -\frac{55}{144}B=0
\]
消去 \(B''\)，可得
\[
\boxed{\quad
F_1=\left(-4+\frac{25}4z\right)B^2
 +(-24z+30z^2)BB'
 -36z^2(1-z)(B')^2 .
\quad}
\tag{1034.12}
\]
这里的常数项是 \(-4\)，不是从末项猜出的归一。
例如在未消 \(B''\) 的表达式中，三类系数为
\[
(-4+20z)B^2+(-72z+114z^2)BB'
  -36z^2(1-z)\{(B')^2+BB''\};
\]
代入上式后恰为 (1034.12)，保留所有项。

记 \(b_k\ne0\) 为 \(B\) 的首项系数。
(1034.12) 的 \(z^{2k+1}\) 系数是
\[
\left(\frac{25}4+30k+36k^2\right)b_k^2
      =\left(6k+\frac52\right)^2b_k^2.
\]
在本行 \(p=12k+11\) 中，\(6k+5/2=-3\) 于 \(\mathbf F_p\)，
故该系数准确为 \(9b_k^2\ne0\)。于是
\[
\boxed{\quad
\deg F_1=2k+1,\qquad
\deg N_{p,2}=3k+1<4k+3=\deg P=m .
\quad}
\tag{1034.13}
\]

这个次数事实可合法用于**新线性化后的**完整有理微分
\[
\eta=z^{-m-1}\frac{N_{p,2}(z)}{P(z)}\,dz.
\]
原点留数为 \(\mathcal J_{p,2}\)；其他有限极点只可能是 \(P\) 的根。
分子次数低于分母，故无穷远无留数。
从而
\[
\boxed{\quad
\mathcal J_{p,2}
 =-\sum_{P(\alpha)=0}\operatorname{Res}_\alpha\eta .
\quad}
\tag{1034.14}
\]
每个几何根计一次，并按实际重数和约消后的实际极阶取留数。
不假定 \(P\) 无重根，也不假定 \(P,B\) 互素。
在此表达式中没有额外的独立 cusp 项；
若 \(P(1)=0\)，该点照实包含在分母根之中。

(1034.14) 不删去 R1005 旧表达式中的任何局部贡献：
它先在原有限系数范围内证明等价，再对新的完整有理函数取留数。
不能将两种表达式的单个局部留数逐点等同。

## 5. 原 \(r=8\) 行必须保留的多项式部分

这里 (1034.11) 只给
\[
\deg N_{p,8}\le15k+7,\qquad \deg P=4k+1,\qquad m=4k-1.
\]
因此不能将 \(N_{p,8}/P\) 自动看成真分式。
若作唯一欧氏分解
\[
N_{p,8}=P H+R,\qquad \deg R<\deg P,
\]
则原目标是
\[
\boxed{\quad
\mathcal J_{p,8}=[z^m]H+[z^m]\frac RP .
\quad}
\tag{1034.15}
\]
两部分全部保留。
任何使用分母根留数的后继证明，亦须保留该多项式部分对应的
原点系数或无穷远贡献。

## 6. 下一项真实任务与范围

本篇将原固定幂目标降成指定分母 \(P\) 的线性系数，
但没有把一个系数为零提升为更强的有理微分结论。
特别是，\(\mathcal J_{p,2}=0\) 只约束 (1034.14) 的
**全部留数之和**，不强迫每个留数为零，不自动给有理 primitive，
也不强迫某个低次数循环消失。
\(r=8\) 还须保 (1034.15) 的多项式部分。

继续要证的仍是原 \(\mathcal J_{p,r}\ne0\)，从而经
R988/R990 给同一个原高 Hurwitz 坐标及超奇异全迹非零。
原 primitive/Legendre 的同 \(h\) 筛选目标与 O0 的全部全局支路
没有在本篇被替换或关闭。Serre 主目标仍 OPEN。

## 依赖和审核

- [R990](R990-original-hypergeometric-fixed-r-coefficient.md)：
  原 sigma/Ramanujan 来源、相位、有限可约范围、\(Q\) 与 bare 系数单位接口。
- [R1005](R1005-finite-Gauss-companion-and-complete-resonance-defect.md)：
  指定 \(P\)、完整 \(K\) 和共振误差；旧留数和不能只取 cusp 的界限。
- [R988](R988-original-pure-balanced-Cartier-contraction-and-high-trace.md)：
  原高坐标与原全迹接口。
- [R1003](R1003-global-scope-and-remaining-branches.md)：完整 Serre 范围。

o2_high_coefficient 与 root 独立纸核有限级数精度、系数分部积分、
递推每个分母、原相位、\(r=2\) 的所有三类项及准确首系数，
并核 \(r=8\) 不可删除的多项式部分。全文复核后登记。
