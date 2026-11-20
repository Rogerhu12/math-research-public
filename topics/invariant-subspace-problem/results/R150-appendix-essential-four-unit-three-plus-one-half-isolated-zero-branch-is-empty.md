# R150 附录：单位三重点加单点、孤立零点的半权支路为空

作者：Astra-ISP-b2a9acde-20261120（root 与 r150_structure）；AI-assisted GPT-6 Astra Pro。日期：2026-11-20 UTC。状态：本条明确范围已证明。

## 1. 范围与同一原源

本附录沿用[外均值 essential-four 原长度五代数约化](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md)，并处理
$$
 D=(3+1)_{\rm unit}+1_{\rm zero},\qquad
 \tau_{\rm local}(1)=\tau_{\rm point}(1)=1/2.
$$
仍保留原均值 catalecticant 秩三、$y\notin\operatorname{ess}(T_3)$、
$\dim\operatorname{ess}(T_3)=4$ 与 $\operatorname{rank}H=4$。
它不处理两个 Frobenius 权不相等的支路。

采用[完整零基点配对附录](R150-appendix-essential-four-unit-three-plus-one-isolated-zero-zero-base-pairing-branch-is-empty.md)的同一物理记号：
$$
 \tau(x)=\tfrac12x_0+x_2+\tfrac12x_3,\quad
 K_B=\begin{pmatrix}
 0&0&A&p\\
 0&-2A&B&q\\
 A&B&C&r\\
 p&q&r&0
 \end{pmatrix},\qquad T_3=P+R^3.
$$
$p=0$ 的完整支路由该附录处理。以下 $p\ne0$，利用全部 Gram 配对的共同齐次性令 $p=1$。

所有计算直接使用
$$
 P(x)=\tfrac12\tau(x-\tau(x)1)^3,\quad
 d=D_K1,\quad \phi=\tau d/2,
$$
$$
 e-2D_Kd-2d^2+4\phi d=0,                                   \tag{1.1}
$$
$$
 N=N_B+mR^2,\quad
 N_B(x)=\tfrac12\tau((d-\phi)x^2)
  -(\tau x)\tau(dx)+\phi(\tau x)^2+\tfrac14\tau(xD_Kx).        \tag{1.2}
$$
$D_Kx$ 的第 $i$ 分量为 $\tau((K_B)_{i,\bullet}x)$；
$e$ 使用三重点的 $0,1,2$ 系数，具体同前附录。
没有用任何替代的自由 Gram 或有限呈示。

## 2. 原 mean 的半权形式与原 jet 相容式

定义
$$
 h=2\phi-2A-\tfrac32.
$$
原 mean 的常数系数以及 $\phi$ 的定义给出
$$
 C=-A(2h+1),\qquad r=(h+1)(2A+1).                           \tag{2.1}
$$
此步没有除以 $A,h,A+h$。
剩余三个 mean 为
$$
 E_1=2\{(A+h)B-Ahq\}=0,                                    \tag{2.2}
$$
$$
 E_2=R_2-4B^2-3Bq=0,\qquad E_P=R_P-2Bq=0,                  \tag{2.3}
$$
其中
$$
 Q=2h^2+2h+1,\quad
 R_2=2A^2(h+1)(1-2h)-3AQ,
$$
$$
 R_P=-2A\{Q+2A(h+1)(2h+1)\}.                               \tag{2.4}
$$

设 $x_i=K_Bu_i$，并记
$$
 P(x_0+t x_1+t^2x_2)=p_0+p_1t+p_2t^2+O(t^3),
$$
$$
 N_B(x_0+t x_1+t^2x_2)=n_0+n_1t+n_2t^2+O(t^3).
$$
若零点极坐标为 $u+vt+wt^2+\cdots$，原 highest、$N$ 给
$$
 p_0=-u^3,\ p_1=-3u^2v,\ p_2=-3u^2w-3uv^2,
$$
$$
 n_0=-mu^2,\ n_1=-2muv,\ n_2=-m(v^2+2uw).
$$
所以以下两个相容式在所有零值情况下都成立：
$$
 c_0=3p_0n_1-2n_0p_1=0,
$$
$$
 c_1=6p_0n_2+p_1n_1-4n_0p_2=0.                             \tag{2.5}
$$
它们仅是直接代入的多项式恒等式；尤其不要求 $u,m,p_0,n_0\ne0$。
由原源
$$
 p_0=A^2(A+3/2),\qquad n_0=-A^2(2h+1)/4.                   \tag{2.6}
$$
后面保留 $A=-3/2$ 与 $h=-1/2$，并不把它们除掉。

## 3. 三个完整例外支路

### 3.1 $A=0$

由 (2.3) 有 $Bq=0$ 和 $4B^2+3Bq=0$，故 $B=0$。
(2.1) 又给 $C=0$。因此原三重点空间
$\langle u_0,u_1,u_2\rangle$ 全等向，违反已登记的[原全等向长度三分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)
（不存在非约化长度三全等向支撑）。所以 $A\ne0$。

### 3.2 $h=0$

(2.2) 给 $B=0$，(2.3) 的单点式给 $A=-1/2$。
另一个 mean 却给 $R_2=2$，矛盾。故 $h\ne0$。

### 3.3 $A+h=0$

此时 $A=-h\ne0$，(2.2) 给 $q=0$。
令
$$
 T=4h^3+4h^2-1.
$$
(2.3) 给
$$
 T=0,\qquad B^2=\frac{h(3+8h+4h^2-4h^3)}4.                 \tag{3.1}
$$
把同一原 $P,N_B$ 的 jets 代入 (2.5)，在 (3.1) 上，
$$
 c_1=\frac{3h^3}{8}(68h^2-28h-23).                         \tag{3.2}
$$
于是 $T=0$ 与 $68h^2-28h-23=0$ 必须同时成立。
将 $T$ 除以后者，其余式为 $(1063h+263)/289$。
这迫 $h=-263/1063$，但它不是
$4h^3+4h^2-1$ 的有理根：该分数已约分，而有理根定理要求分母整除 $4$。
矛盾。配套源还独立检查这两个 QQ 多项式的 gcd 为一。
这里没有除以 $B$，故 $B=0$ 也已覆盖。

## 4. 正规 mean 支路的单参数形式

现在 $Ah(A+h)\ne0$。令
$$
 \alpha=A+h,\qquad \lambda=Ah/\alpha.
$$
由 (2.2)，$B=\lambda q$，由 (2.3)，$q^2=R_P/(2\lambda)$。
消去 $q^2$ 的恒等式是
$$
 2\alpha R_2-(4hA+3\alpha)R_P
   =8A^2\{2A(h+1)Q+h(4h^2+6h+3)\}.                        \tag{4.1}
$$
设 $C_0=4h^2+6h+3$。因为 $A\ne0$，有
$$
                    2A(h+1)Q+hC_0=0.                     \tag{4.2}
$$
其中 $(h+1)Q\ne0$：$h=-1$ 时 $hC_0=-1\ne0$；
若 $Q=0$，则 $C_0=2h+1\ne0$，又因 $h\ne0$ 矛盾。
因此
$$
 A=-\frac{hC_0}{2(h+1)Q},\quad
 \alpha=\frac{hT}{2(h+1)Q},\quad
 \lambda=-\frac{hC_0}{T},\quad
 q^2=\frac{T^2}{2Q^2}.                                     \tag{4.3}
$$
已知 $\alpha\ne0$，所以 $T\ne0$；已知 $A\ne0$，所以 $C_0\ne0$。
(4.3) 还证明 $q\ne0$，不需要额外假设。
这一推导把所有被除零因子逐一归入已排支路。

## 5. 原一、二阶 jet 的两个互素一元障碍

将 (4.3)、$B=\lambda q$ 代入同一原 jet 式 (2.5)，并仅使用
$q^2=T^2/(2Q^2)$，精确整理为
$$
 \frac{c_0}{q}
  =\frac{3A^4}{4(h+1)QT}f(h),\qquad
 c_1=-\frac{3A^4}{8(h+1)^2Q^2}g(h),                        \tag{5.1}
$$
其中
$$
 f(h)=16h^5+56h^4+92h^3+86h^2+45h+12,
$$
$$
 g(h)=144h^6+584h^5+1124h^4+1268h^3+893h^2+372h+75.          \tag{5.2}
$$
所有 (5.1) 的分母已在第 4 节证明非零，且 $A,q\ne0$。
故原梯度要求 $f(h)=g(h)=0$。
这两个明确的有理系数一元多项式的 Euclidean gcd 为 $1$，不可能。

配套[短 QQ 原源](../notes/2026-11-20-essential-four-unit-three-plus-one-half-verify.py)从 (1.1)、(1.2) 重建全部源、实际读取三个 jet，
逐项核 (2.1)–(5.1) 后在 $\mathbb Q[h]$ 计算上述 gcd。
它不使用有限域提升、一般多元 Gröbner 消元或没有原出处的结果表。

实际run44732550495/job136275725868、冻结提交35d0d768258a205cd0d78552fb7fbfa4018ec70a全部通过，程序计时8.083秒；源码SHA256为1207ffc3c9c49bc2d3c71a9136978c00700d22cffd203414cbce70a9cd4c0a47。[完整运行身份](../notes/2026-11-20-exact-source-run44732550495-b2a9.json)保日志、标准输出SHA和真实pull；只保存源、参数和身份，不保存可重算消元数组。

## 6. 结论

$p\ne0$ 的单位 $3+1$ 半权支路全部为空。
结合已证明的 $p=0$ 完整支路，
外均值 essential-four 的整个
$$
 D=(3+1)_{\rm unit}+1_{\rm zero},\qquad a=b=1/2
$$
支路为空。原支撑含无穷远点时结论不变，因为所有计算均在真实物理 jets 中进行。

$b\ne1/2,\ p\ne0$ 仍是单位 $3+1$ 的未闭范围；
其他剩余支路和普通 Hilbert ISP 主结论没有因此关闭。
