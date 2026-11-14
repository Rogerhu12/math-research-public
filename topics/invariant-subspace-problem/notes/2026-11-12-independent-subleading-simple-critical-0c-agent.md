# 独立次主尾下的简单临界取消，以及多重取消的矩阵增长障碍

日期：2026-11-12（UTC）。子任务：critical_kernel。**状态：简单临界取消定理已证明；多重临界取消仍未解决。**

本条处理至少三个乘积可能出现的第一层临界组合：各相对对数有不同复常数乘同一 $j^{-p}$ 主尾，但各自的 $o(j^{-p})$ 次主尾彼此独立。没有假设这些对数恰是同一个 $L$ 的解析函数。证明的新增工具是：全部次主尾产生的零常数解析函数，其指数算子在主时间尺度上只有 $e^{o(M)}$ 的范数增长。

此外，给出实际进位模型中的明确矩阵反例：若把这个增长结论直接扩到常数项非零但幂零的矩阵解析函数，它会失败，甚至出现超出任意 $e^{CM}$ 的增长。这只否定一种处理多重取消的简化路线，不构造非零核。

依赖：R60 的 BW 不等式；R61 及[指数范围证书](2026-11-12-power-range-negative-integral-0c.md)的负常数和实际近似；R62 的解析芽演算思路。全部新增支配、增长、隐函数和误差步骤在下文证明。

## 1. 各对数的独立次主尾

固定 $1<p\le12/5$。令基准对数 $L$ 对应正实局部差
$$
d_j=(j+2)^{-p},
$$
例如
$$
L=\sum_{j\ge0}
[\log(I+N_j)-\log(I+(1-d_j)N_j)].
\tag{1.1}
$$
它是 R61 的一个已证单射稠密对数，并具有真实近似
$$
\left\|L-G_k-\sum_{j\ge k}d_jE_j\right\|
\le C\eta_{k-1},\qquad G_k^{2^k}=0.
\tag{1.2}
$$

对 $i=1,\ldots,r$，令
$$
L_i=\psi_i(A)+
\sum_{j\ge0}
[\log(I+s_{i,j}N_j)-\log(I+t_{i,j}N_j)],
\tag{1.3}
$$
其中各 $\psi_i$ 是在 $0$ 邻域解析且 $\psi_i(0)=0$ 的标量芽；所有底参数在 $i,j$ 上有共同有限界。假设
$$
s_{i,j}-t_{i,j}=c_i d_j+\epsilon_{i,j},
\qquad
\epsilon_{i,j}=o(d_j).
\tag{1.4}
$$
$c_i$ 可以是任意复数，包括零；次主余项不要求具有渐近系数，不要求彼此成比例。定义
$$
R_i=L_i-c_iL.
\tag{1.5}
$$
它们都属于 $\mathcal A$、拟幂零、与 $A,L$ 及彼此交换。以下给出仅由 (1.3)—(1.4) 推出的共同增长界。

## 2. 一个真正的正系数支配算子

这里的“正”指函数格正算子：把非负函数送成非负函数。它不是关于自伴正算子的断言。

**引理 2.1。** 存在函数格正的 $B\in\mathcal A$，常数系数为零，满足对全部 $f\in H$，
$$
|Af|\le B|f|,\qquad
|R_if|\le B|f|\quad(1\le i\le r)
\tag{2.1}
$$
（几乎处处的函数不等式）。并且存在非负数列
$$
b_j=o((j+2)^{-p})
\tag{2.2}
$$
及低位幂零 $K_k$，使
$$
K_k^{2^k}=0,\qquad
\sup_k\|K_k\|<\infty,\qquad
\left\|B-K_k-\sum_{j\ge k}b_jE_j\right\|
\le C_B\eta_{k-1}.
\tag{2.3}
$$

**证明。** 取共同底参数界 $S\ge2$。对充分大的 $j$，$S^2\eta_j<1/2$。局部对数的 Taylor 系数为
$$
\log(I+sT)-\log(I+tT)
=\sum_{n\ge1}\frac{(-1)^{n+1}(s^n-t^n)}nT^n.
$$
因
$$
|s^n-t^n|\le nS^{n-1}|s-t|,
$$
(1.4) 说明 $R_i$ 的第 $j$ 个局部函数可以写成
$$
\epsilon_{i,j}T+\sum_{n\ge2}a_{i,j,n}T^n,
\qquad
|a_{i,j,n}|\le C_i(j+2)^{-p}S^{n-1}.
\tag{2.4}
$$
这里已经把 $c_iL$ 的相应系数计入。所有有限低位局部函数都是 $A$ 的实际解析芽；把它们与 $\psi_i(A)$ 合并，记为 $\varphi_i(A)$，$\varphi_i(0)=0$。

若 $\varphi_i(z)=\sum_{n\ge1}\varphi_{i,n}z^n$，定义具有非负系数的解析芽
$$
\varphi_{i,\#}(z)=\sum_{n\ge1}|\varphi_{i,n}|z^n.
$$
它在同一个充分小圆盘内收敛。取足够大的固定 $J$，并令
$$
b_j=\sum_i|\epsilon_{i,j}|\quad(j\ge J),\qquad
C_*=\sum_iC_i.
$$
可取
$$
\begin{aligned}
B={}&A+\sum_i\varphi_{i,\#}(A)\\
&+\sum_{j\ge J}\left[
b_jN_j+
C_*(j+2)^{-p}
 \sum_{n\ge2}S^{n-1}N_j^n\right].
\end{aligned}
\tag{2.5}
$$
有限的 $b_j$ 初值可置零。

所有项都是函数格正的。又 $\|N_j^{2q}\|\le\eta_j^q$、$\|N_j^{2q+1}\|\le\eta_j^q$，所以内层高次和的范数为 $O_S(\eta_j)$；外层级数按范数收敛。各解析芽在拟幂零 $A$ 上的级数也按范数绝对收敛，因此 $B\in\mathcal A$、常数项为零。

$A$ 是正加权平移，故 $|A^nf|\le A^n|f|$，对 $N_j^n$ 同样成立。(2.4) 逐项三角不等式及闭正锥取极限，证明 (2.1)。

在 (2.5) 中把全部低于 $k$ 的 $N_j$ 替换为 $N_j^{[k]}$，各解析芽替换为其 $A_k$ 值，得到 $K_k$。它是 $A_k$ 的无常数项多项式，所以幂零阶至多 $2^k$。R61 的解析芽截断界给 $O(a_k)$；局部函数
$$
b_jT+C_*(j+2)^{-p}ST^2(I-ST)^{-1}
$$
在相关原幂及截断幂上的统一预解式界，给局部差
$$
O((j+2)^{-p})\,a_k/a_j.
$$
求和不超过 $C\eta_{k-1}$。对 $j\ge k$，第一项替换为 $b_jE_j$ 的误差为 $b_j\eta_j$，高次项为 $O((j+2)^{-p}\eta_j)$；它们的总和也为 $O(\eta_{k-1})$。由此得到 (2.3)，同时得到 $\|K_k\|$ 的共同界。证毕。

(2.1) 是对向量绝对值的支配；没有把它误称为 C* 意义下的 $|R_i|\le B$。

## 3. 次主支配算子的主尺度增长只有 $e^{o(M)}$

**引理 3.1。** 对每个固定 $T_0>0$，令 $M\to\infty$，则
$$
\boxed{
\sup_{0\le t\le T_0M^p}\log\|e^{tB}\|=o(M).
}
\tag{3.1}
$$

**证明。** 取 $k=\lfloor(3/4)\log_2M\rfloor$，并置
$$
B_k=K_k+\sum_{j\ge k}b_jE_j.
$$
$K_k$ 与余下各位交换。若 $q_k=2^k\le M^{3/4}$、$\|K_k\|\le K$，则
$$
\|e^{tK_k}\|
\le\sum_{n<q_k}\frac{(tK)^n}{n!}
\le q_k(1+tK)^{q_k-1}.
$$
其对数在 $0\le t\le T_0M^p$ 上至多 $O(M^{3/4}\log M)=o(M)$。

对尾部，
$$
\left\|\exp\left(t\sum_{j\ge k}b_jE_j\right)\right\|
\le\prod_{j\ge k}(1+tb_j).
$$
记
$$
\rho_k=\sup_{j\ge k}(j+2)^p b_j\to0.
$$
用递减函数的和积分比较，
$$
\begin{aligned}
\sum_{j\ge k}\log(1+T_0M^pb_j)
&\le\int_0^\infty
 \log\bigl(1+T_0\rho_k(M/x)^p\bigr)\,dx\\
&=M(T_0\rho_k)^{1/p}
 \int_0^\infty\log(1+y^{-p})\,dy
=o(M).
\end{aligned}
\tag{3.2}
$$
最后的积分有限：在零附近用 $\log2-p\log y$ 控制，在无穷远用 $y^{-p}$ 控制。$p>1$ 正好保证后者可积。

最后 (2.3) 的 Duhamel 差给
$$
\|e^{tB}-e^{tB_k}\|
\le C t\eta_{k-1}e^{C't}
\le\exp(-cM^3+O(M^p+\log M)).
$$
因为 $p\le12/5<3$，该误差趋零，且不影响已经得到的 $e^{o(M)}$ 界。$B$ 正且 $e^{tB}\ge I$，其范数至少为 $1$，故对数无负无穷问题。证毕。

## 4. 任意零常数解析函数也有同一增长界

令 $\Phi(z,r_1,\ldots,r_r)$ 是收敛解析芽，$\Phi(0)=0$，并记
$$
Z=\Phi(A,R_1,\ldots,R_r).
$$
演算按范数绝对收敛，因为这些交换算子都拟幂零；证明与 R62 的多变量 Cauchy 系数界相同。

**引理 4.1。** 对每个固定 $T_0>0$，
$$
\boxed{
\sup_{|t|\le T_0M^p}\log\|e^{tZ}\|=o(M).
}
\tag{4.1}
$$

**证明。** 写 $\Phi=\sum_\alpha c_\alpha Y^\alpha$，其中变量 $Y$ 包括 $A$ 及各 $R_i$。定义单变量非负系数芽
$$
\phi(x)=\sum_\alpha |c_\alpha|x^{|\alpha|}.
$$
它在零点附近收敛，且 $\phi(0)=0$。由 (2.1) 反复应用正算子的保序性，
$$
|Y^\alpha f|\le B^{|\alpha|}|f|,
$$
故
$$
|Zf|\le\phi(B)|f|,\qquad
|Z^nf|\le\phi(B)^n|f|.
\tag{4.2}
$$
这里 $\phi(B)$ 是有界函数格正算子。

写 $\phi(x)=xg(x)$，令 $C_\Phi=\max(1,\|g(B)\|)$。由于 $B$ 与 $g(B)$ 交换，
$$
\|Z^n\|\le\|\phi(B)^n\|
\le C_\Phi^n\|B^n\|.
\tag{4.3}
$$
这一步只是范数和交换乘法的估计。**没有**断言函数格正序 $\phi(B)\le C_\Phi B$；$g(B)$ 一般不是乘法算子。

还需要将绝对范数级数控制回一个指数范数。对任意实 $s\ge0$，$B$ 的正性给
$$
\frac{(2s)^n}{n!}B^n\le e^{2sB}
$$
作为正算子的序关系。因此
$$
\boxed{
\sum_{n\ge0}\frac{s^n}{n!}\|B^n\|
\le\sum_{n\ge0}2^{-n}\|e^{2sB}\|
=2\|e^{2sB}\|.
}
\tag{4.4}
$$
由 (4.3)—(4.4)，
$$
\|e^{tZ}\|
\le2\|e^{2C_\Phi|t|B}\|.
$$
引理 3.1 对固定常数 $2C_\Phi T_0$ 适用，证明 (4.1)。证毕。

## 5. 核上的隐函数替换与 BW 搬运

**定理 5.1。** 对任意上述零常数解析芽 $\Phi$，
$$
S=L-\Phi(A,R_1,\ldots,R_r)
\tag{5.1}
$$
单射且值域稠密。

**证明。** 取 $f\in\ker S$，记 $Z=\Phi(A,R)$。$L$ 与 $Z$ 交换，所以由 $Lf=Zf$ 归纳得到 $L^nf=Z^nf$，进而
$$
e^{tL}f=e^{tZ}f\qquad(t\in\mathbb C).
\tag{5.2}
$$

选择 $p$ 所对应的已认证区间 $[a,b]$：$p\le2$ 时为 $[1,20]$，$p>2$ 时为 $[1/10,30]$。基准系数为 $d_j=(j+2)^{-p}$，故取实时间 $t=uM^p$，$a\le u\le b$。用 (1.2) 的 $k=\lfloor(3/4)\log_2M\rfloor$ 分解
$$
T_k=H_{k,m}+C_m,\qquad
H_{k,m}=G_k+\sum_{k\le j<m}d_jE_j,\quad
C_m=\sum_{j\ge m}d_jE_j.
$$
头尾交换，$e^{tH_{k,m}}$ 是 $t$ 的次数至多 $M+M^{3/4}$ 的多项式。

由 (5.2)，
$$
\begin{aligned}
e^{tH_{k,m}}f-e^{-tC_m}e^{tZ}f
&=e^{-tC_m}(e^{tT_k}-e^{tL})f.
\end{aligned}
\tag{5.3}
$$
这里没有要求 $Z$ 与近似头部或尾部交换。通常的指数 Duhamel 差和 (1.2) 给
$$
\|(5.3)\|
\le Ct\eta_{k-1}e^{C't}\|f\|
\le e^{-cM^3+O(M^p+\log M)}\|f\|.
\tag{5.4}
$$
左乘 $e^{-tC_m}$ 的范数已计入固定的 $e^{C't}$；真实误差未删去。

令
$$
p_m(u)=\langle e^{uM^pH_{k,m}}f,1\rangle.
$$
它的常数项为 $\langle f,1\rangle$。由 (5.3)，
$$
|p_m(u)|
\le\|e^{tZ}\|\|f\|\|e^{-tC_m^*}1\|
+\text{式 (5.4) 的误差}.
$$
引理 4.1 给第一因子 $e^{o(M)}$；基准尾满足
$$
\log\|e^{-tC_m^*}1\|=Mh_p(u)+O(1),
\quad
\|e^{-tC_m^*}1\|\ge e^{-CM}.
$$
所以 (5.4) 可吸收，得到统一边界
$$
|p_m(u)|\le\|f\|\exp(Mh_p(u)+o(M)).
\tag{5.5}
$$
BW 于是给
$$
\log|\langle f,1\rangle|
\le O(1)+MJ_p+g_{a,b}M^{3/4}+o(M)\to-\infty.
$$
核均值为零，再用 $S\in\mathcal A$ 与 $A$ 交换、$1$ 对 $A^*$ 循环，得到 $\ker S=0$。$S$ 的复对称性给稠密值域。证毕。

## 6. 有限指数和的简单临界取消定理

令 $a_i(z)$ 为有限个一元解析芽，考虑
$$
X=\sum_{i=1}^r a_i(A)e^{-L_i}.
\tag{6.1}
$$
定义两个标量
$$
\lambda_0=\sum_i a_i(0),\qquad
\lambda_1=\sum_i a_i(0)c_i.
\tag{6.2}
$$

**定理 6.1。** 若 $\lambda_0\ne0$，则 $X$ 可逆。若
$$
\boxed{\lambda_0=0,\qquad\lambda_1\ne0,}
\tag{6.3}
$$
则 $X$ 单射且值域稠密。因此它把每个已知的 $A$ 循环向量送成非零循环向量。

**证明。** 第一种情况由 $\mathcal A$ 的单点谱直接成立。第二种情况定义多变量解析芽
$$
F(z,w,r_1,\ldots,r_r)
=\sum_i a_i(z)e^{-c_iw-r_i}.
$$
有 $F(0)=0$，且
$$
\partial_wF(0)=-\lambda_1\ne0.
$$
局部解析隐函数分解给
$$
F(z,w,\mathbf r)
=U(z,w,\mathbf r)\,[w-\Phi(z,\mathbf r)],
\tag{6.4}
$$
其中 $U(0)\ne0$、$\Phi(0)=0$。

为说明此步没有假设算子关系：固定围绕 $w=0$ 的一个小圆，使 $F(0,w,0)$ 只有一个简单零点；对小的横向参数 $(z,\mathbf r)$，Rouché 定理仍给一个圆内零点。其位置可用
$$
\frac1{2\pi i}\int
 w\,\frac{\partial_wF(z,w,\mathbf r)}
 {F(z,w,\mathbf r)}\,dw
$$
表示，因而对横向参数解析，记为 $\Phi$。一元可去奇点再给联合解析的非零商 $U$，即 (6.4)。这是 R62 准备引理在次数一和多个横向参数上的同一构造。

在交换拟幂零元 $(A,L,R_1,\ldots,R_r)$ 上作绝对范数收敛的解析芽演算，(6.4) 给
$$
X=U(A,L,\mathbf R)\,[L-\Phi(A,\mathbf R)].
$$
第一因子可逆，第二因子由定理 5.1 单射稠密，故结论成立。没有把独立 $R_i$ 假设为某个 $L$ 的解析函数。证毕。

特别地，当 $r\ge3$、$a_i$ 为标量常数时，本条处理全部常数和为零、但第一主系数矩不为零的临界组合。对三个不同的 $c_i$，它覆盖临界系数平面中的全部点，除了同时满足两个标量线性方程的那条更深取消线。

## 7. 对至少三个 R16 乘积的具体含义

设有限个 R16 向量的尾相对于同一个参考乘积 $g$，具有局部比值差
$$
s_j-t_{i,j}=c_i(j+2)^{-p}+o(j^{-p}),
$$
且各自允许任意有限前缀。这些差都在 $\ell^1$ 中，所以 R61 §8 的实际逐位映射和非零常数归一化给
$$
h_i=p_i(A)\kappa_i e^{-L_i}\xi
$$
（共同循环锚 $\xi$，非零有限多项式 $p_i$，$\kappa_i\ne0$）。

给定有限线性组合，先从全部非零系数对应的有限 $p_i$ 中取出共同的最小 $A$ 次幂。这是有限多项式上的合法分解，所得算子系数为解析芽 $a_i(A)$，且其常数项不全为零。若 (6.2) 的 $\lambda_0\ne0$，组合循环；若 (6.3) 成立，定理 6.1 同样给该组合非零且循环。

因此这是真正允许多个独立次主尾的三项及更多项结果。它没有把同阶之外的有限前缀硬并成常数，也没有对一般范数闭包元素有界除以 $A$。

## 8. 多重取消的矩阵增长障碍：实际模型中的反例

当 $\lambda_0=\lambda_1=0$ 时，沿主方向的零点可能有阶 $d\ge2$。R62 的准备方法会产生一个横向参数矩阵 $M(A,\mathbf R)$，其常数矩阵非零但幂零。不能把引理 4.1 不加证明地推广到这类矩阵。

下面给出实际 $N_j$ 构造的严格反例。固定同一个 $p>1$，令
$$
\varepsilon_j=\frac{(j+2)^{-p}}{\log(j+3)},
\qquad
R=-\sum_{j\ge0}\log(I-\varepsilon_jN_j).
\tag{8.1}
$$
该级数按范数收敛，且
$$
R=\sum_j\sum_{q\ge1}\frac{\varepsilon_j^q}{q}N_j^q
\ge\sum_j\varepsilon_jN_j
$$
为函数格正序。它具有 $o(j^{-p})$ 的一阶尾及真实 $O(\eta_{k-1})$ 截断误差，属于前面次主尾增长引理的类型；例如它的局部底参数可取 $s_j=0,t_j=-\varepsilon_j$。

定义实际矩阵算子
$$
\mathcal M=
\begin{pmatrix}0&I\\R&0\end{pmatrix}
\quad\text{作用于 }H\oplus H.
\tag{8.2}
$$
作为 $R$ 的矩阵解析函数，它在 $R=0$ 的常数矩阵是非零平方零矩阵。

对 $n$ 个互异位，实际归一化幂满足
$$
\left\|\prod_{j=0}^{n-1}N_j\right\|=1.
\tag{8.3}
$$
上界来自各因子范数为一；下界可在低 $n$ 位全为零的柱向量上取到，因为每个 $N_j$ 将该位从零变一时不产生进位，整个归一化路径的权为一。此处是原算子精确关系，没有用 $N_j\approx E_j$ 代替。

展开正算子幂，取互异指标的 $n!$ 个相同乘积项，得到
$$
\|R^n\|\ge n!\prod_{j=0}^{n-1}\varepsilon_j
\ge n!\left[(n+1)^{-p}/\log(n+2)\right]^n.
\tag{8.4}
$$
$e^{t\mathcal M}$ 的左上角为
$$
\sum_{n\ge0}\frac{t^{2n}}{(2n)!}R^n.
$$
全部项为正，故对实 $t>0$ 和每个 $n\ge2$，
$$
\|e^{t\mathcal M}\|
\ge\frac{t^{2n}}{(2n)!}\|R^n\|
\ge\left[
\frac{t^2}{2^{p+3}e\,n^{p+1}\log n}
\right]^n.
\tag{8.5}
$$
这里用 $n!\ge(n/e)^n$、$(2n)!\le(2n)^{2n}$、
$n+1\le2n$、$\log(n+2)\le2\log n$。

取一个充分小的固定 $\epsilon>0$，并令
$$
n=\left\lfloor
\epsilon\,
\frac{t^{2/(p+1)}}{(\log t)^{1/(p+1)}}
\right\rfloor.
$$
当 $t$ 足够大时，(8.5) 的方括号至少为 $2$。因此存在 $c_p>0$，使
$$
\boxed{
\log\|e^{t\mathcal M}\|
\ge c_p
\frac{t^{2/(p+1)}}{(\log t)^{1/(p+1)}}.
}
\tag{8.6}
$$
在主时间 $t=M^p$ 上，
$$
\frac{\log\|e^{M^p\mathcal M}\|}{M}
\longrightarrow+\infty,
$$
因为 $2p/(p+1)>1$。

所以“横向尾是 $o(j^{-p})$，就连带使任意幂零常数矩阵的指数增长为 $e^{o(M)}$”这一说法为假。这个反例甚至保留实际进位、局部对数形式及已需的截断误差。

它**不**证明 $L\otimes I-\mathcal M$ 有非零核，也不证明某个三乘积组合非循环。它只明确阻断将简单取消的增长引理直接套在二阶 companion 矩阵上的步骤。

## 9. 当前剩余问题

已经无条件闭合的是独立 $o(j^{-p})$ 次主尾下的简单临界取消 (6.3)。三项的真正更深缺口为
$$
\sum_i a_i(0)=0,\qquad
\sum_i a_i(0)c_i=0,
$$
而横向尾之间没有额外精确关系的情形。即使不同 $c_i$ 使第二主系数矩不为零，横向的一阶扰动仍可能大于主方向的二阶量；不能仅按主常数的 Vandermonde 阶数忽略它。

后续若继续矩阵 BW，必须使用比全矩阵指数范数更细的核相关结构，或另找能处理这些独立横向一阶项的估计。第 8 节说明，单纯提高同一范数增长引理的矩阵版本并不足够。

