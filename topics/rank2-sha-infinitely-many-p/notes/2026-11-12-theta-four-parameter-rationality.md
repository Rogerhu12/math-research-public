# 四参数 theta 截面的有理下降：一个十维精确证书

日期：2026-11-12。状态：已证明。这里证明实际固定截面的参数可以同时有理化，
不从逐项“平方为有理数”直接推断平方根符号一致。

## 1. 结论

[次数十七下降](2026-11-12-theta-seventeen-isogeny-descent.md)
给实际截面

$$
 A(z)=\vartheta(z)\sigma_E(z)^{16}
       \bigl(c_1x(z)^6+c_2x(z)^4+c_3x(z)^2+c_4\bigr)
       =\sum_m b_mz^m,
 \tag{1}
$$

其中 $c_j$ 为实代数数，$\vartheta^2=x\sigma_E^2$、$\vartheta(0)=1$。
系数公式是

$$
 e_m=\kappa(17\,Nf)^{-m}b_m^2\quad(4\mid m),\qquad
 \kappa\in\overline{\mathbb Q}\cap\mathbb R_{>0}.
 \tag{2}
$$

首项为 $b_4=c_1$。已经认证的 $e_4\ne0$ 给 $c_1\ne0$；
其证书见[真实首坏项与饱和格](2026-11-12-inert-first-break-and-saturated-jets.md)
§4，使用固定 $7$ 处的精确有限轨道迹
$d_4^{\rm raw}\equiv2+2i\pmod7$，没有借用 BSD 或 CLS 判据。

**定理。** 将 $A$ 除以 $c_1$ 后，可以准确写成

$$
 \boxed{
 A_{\mathbb Q}(z)=
 \vartheta(z)\sigma_E(z)^{16}
       \bigl(x(z)^6+u_2x(z)^4+u_3x(z)^2+u_4\bigr),
 \qquad u_2,u_3,u_4\in\mathbb Q .
 }
 \tag{3}
$$

因此 $A_{\mathbb Q}\in z^4\mathbb Q[[z^4]]$，首项系数一。
相应常数也成为正有理数

$$
 \kappa_{\mathbb Q}=\kappa c_1^2
        =e_4(17\,Nf)^4\in\mathbb Q_{>0}.
 \tag{4}
$$

对每个目标普通 $p$，使用 (3) 的同一有界测度及 principal Mellin
因子 $J_{\mathbb Q,p}$，实际完整分支满足

$$
 F_p^{\Theta,-}(T)=
 \kappa_{\mathbb Q}f\Omega_p
 (1+T)^{\log_p\langle136\rangle/\log_p(1+p)}
 J_{\mathbb Q,p}(T)^2.
 \tag{5}
$$

中心零阶判据保持不变：

$$
 J_{\mathbb Q,p}(0)=0,\qquad
 \Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
       \iff J_{\mathbb Q,p}'(0)\ne0.
 \tag{6}
$$

本定理暂不识别 $u_2,u_3,u_4$ 的实际数值，也不证明 (6) 对无穷多个 $p$
成立。它消除了固定输入中所有不必要的系数数域和逐权符号歧义。

## 2. 为什么一个有限秩检验足够

置 $u=(1,u_2,u_3,u_4)$。记下列四个有理展开为基：

$$
 V_j(z)=\vartheta(z)\sigma_E(z)^{16}x(z)^{8-2j},
 \qquad 1\le j\le4.
$$

对 $n\ge1$，令

$$
 r_{nj}=[z^{4n}]V_j(z)\in\mathbb Q,\qquad
 B_n=[z^{4n}]A_{\mathbb Q}(z)=r_nu.
 \tag{7}
$$

(2) 在 $4n$ 与 $4$ 两个权的比值准确给

$$
 B_n^2=
 \frac{e_{4n}}{e_4}(17\,Nf)^{4n-4}\in\mathbb Q.
 \tag{8}
$$

令十列依次对应

$$
 11,\ 12,\ 13,\ 14,\ 22,\ 23,\ 24,\ 33,\ 34,\ 44,
$$

并构造十乘十矩阵

$$
 M_{n,ij}=
 \begin{cases}
 r_{ni}^2,&i=j,\\
 2r_{ni}r_{nj},&i<j,
 \end{cases}
 \qquad 1\le n\le10.
 \tag{9}
$$

若 $\det M\ne0$，(8) 的十个有理值线性确定全部十个乘积
$u_i u_j$。这些乘积就都属于 $\mathbb Q$。
因 $u_1=1$，第一行的三个非对角乘积直接等于
$u_2,u_3,u_4$，证明 (3)。

这一论证不要求事先给每个 $B_n$ 选择相容的平方根，
也不要求知道十个中央值的具体大小。

## 3. 有理展开的明确递推

为使秩证书可独立复算，暂写一般曲线
$E_D:y^2=x^3-Dx$，并置 $w=z^4$、

$$
 x(z)=z^{-2}X(w),\qquad X(w)=1+\sum_{n\ge1}X_nw^n.
$$

由 $x''=6x^2-2D$，

$$
 X_n=
 \frac{6\sum_{j=1}^{n-1}X_jX_{n-j}-2D\,{\bf1}_{n=1}}
      {(4n-2)(4n-3)-12}.
 \tag{10}
$$

$g_3=0$ 已由只保留 $z^{4n-2}$ 的展开固定。
由 $\zeta'=-x$ 及 $\sigma'/\sigma=\zeta$，

$$
 L(w):=\log(\sigma_E(z)/z)
     =-\sum_{n\ge1}\frac{X_n}{4n(4n-1)}w^n.
 \tag{11}
$$

$\vartheta^2=x\sigma^2$ 给
$\vartheta=X^{1/2}\exp L$。所以四个基精确成为

$$
 V_j(z)=w^j
 \exp\!\left(\frac{17-4j}{2}\log X(w)+17L(w)\right),
 \qquad1\le j\le4.
 \tag{12}
$$

(10)–(12) 全部在 $\mathbb Q[[w]]$ 中计算。
计算 $\log$ 与 $\exp$ 时可用

$$
 [w^n]\log X
 =X_n-\frac1n\sum_{k=1}^{n-1}
                 k[w^k](\log X)\,X_{n-k},
$$

$$
 [w^n]\exp H
 =\frac1n\sum_{k=1}^{n}kH_k[w^{n-k}]\exp H
 \quad(H_0=0).
 \tag{13}
$$

不涉及浮点数、复周期或任何未定的 $p$-进周期。

## 4. 模 $101$ 的非零行列式

先取 $D=1$。
(10)–(13) 算到 $n=10$ 的全部有理分母在 $101$ 处都是单位。
所得四列系数行模 $101$ 如下：

| $n$ | $r_{n1}$ | $r_{n2}$ | $r_{n3}$ | $r_{n4}$ |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 |
| 2 | 33 | 1 | 0 | 0 |
| 3 | 25 | 73 | 1 | 0 |
| 4 | 14 | 90 | 12 | 1 |
| 5 | 62 | 82 | 38 | 52 |
| 6 | 55 | 76 | 20 | 71 |
| 7 | 20 | 76 | 2 | 97 |
| 8 | 59 | 0 | 73 | 75 |
| 9 | 64 | 83 | 71 | 81 |
| 10 | 38 | 78 | 2 | 54 |

按 (9) 的列序及非对角因子 $2$ 构造矩阵，精确消元给

$$
                       \det M_{D=1}\equiv56\pmod{101}.
 \tag{14}
$$

对于一般 $D$，(10) 给 $X_n(D)=D^nX_n(1)$，
从而

$$
 r_{nj}(D)=D^{n-j}r_{nj}(1)
 \quad(n\ge j),\qquad r_{nj}=0\quad(n<j).
 \tag{15}
$$

(9) 的第 $n$ 行因此可抽出 $D^{2n}$，
第 $ij$ 列抽出 $D^{-i-j}$。因为

$$
 2\sum_{n=1}^{10}n-\sum_{1\le i\le j\le4}(i+j)
                         =110-50=60,
$$

有

$$
 \det M_D=D^{60}\det M_1.
 \tag{16}
$$

$17$ 是 $101$ 的单位，所以 (14) 已证明本题的有理行列式非零。
直接模计算还给 $17^{60}\equiv1\pmod{101}$，
故 $\det M_{17}\equiv56\pmod{101}$。这完成第 2 节的秩证明。

## 5. 可复查证书与边界

精确脚本：

[check-theta-four-parameter-rigidity.py](../scripts/check-theta-four-parameter-rigidity.py)

只用 Python 标准库的 fractions.Fraction，先在 $\mathbb Q$ 上按
(10)–(13) 求全部系数，再逐个检查分母不被 $101$ 整除，
最后在 $\mathbb F_{101}$ 上求行列式。
它还在有理数上逐项核对 (15)，不靠模数值假定曲线缩放关系。

输出的两个行列式均为 $56$，有理秩为十。
这是一份固定的十维线性代数证书；
没有把有限个素数的计算当成无穷非消失结论。

本篇的外部数学输入只有此前已经证明的固定 theta 分解、次数十七下降、
中央系数有理性和 $e_4\ne0$。新的有理下降则由 (8)–(16) 完整证明。
