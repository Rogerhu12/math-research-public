# R150 附录：孤立零点加两个半权单位双点的 rank-four 支路为空


日期：2026-11-20 UTC。作者：Astra-ISP-b2a9acde-20261120 / r150_structure，与root；AI-assisted GPT-6 Astra Pro。**状态：已证明（准确范围为两个单位双点均为半权）。**

本附录只处理 R150 原非 rank-one Bell 临界方程的一个明确支路，不改变普通 Hilbert 不变子空间问题的未解状态。

## 1. 范围、原坐标与原方程

沿用
[原外均值长度五归约](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md)
的外均值 essential-four 约化：原均值的 $3\times4$ catalecticant 秩为 $3$，
$W=\operatorname{ess}(T_3)$ 的维数为 $4$，且 $y\notin W$。
唯一原长度五支撑的 Frobenius 代数在本支为
$$
 \mathcal A=B\oplus\mathbb C,\qquad
 B=\mathbb C[\epsilon]/(\epsilon^2)\oplus
   \mathbb C[\eta]/(\eta^2).
$$
原元素 $L$ 在 $B$ 上为单位，在最后的约化点上为零。
把 $L$ 吸收进活跃因子的 Frobenius 泛函与物理 jet 后，
令 $\tau=\nu L^3$；本附录的额外、明确假设为
$$
 \tau(1,0)=\tau(0,1)=\tfrac12.
$$
每个双点的最高非零 Frobenius 系数可由其局部参数缩放归一为 $1$。
因此，在物理 jet 极坐标 $(X,Y,Z,T)$ 下，
$$
 \tau(x_0,x_1,x_2,x_3)
 =\tfrac12x_0+x_1+\tfrac12x_2+x_3.
$$
这些变换保持每个原曲线点及其一阶 osculating 空间；没有任意改变原 $K$。

设最后零点的极坐标为 $R$，吸收其非零三次系数后，原矩为
$$
 y=\tau X,\qquad H=\tfrac14\tau X^2,\qquad
 V=\tfrac18\tau X^3+\tfrac14R^3.
$$
这里 $X$ 在右边是 $B$-值线性坐标。于是
$$
 T_3=P+R^3,\qquad
 P=(Y+T)\left((Y+T)^2+\tfrac32(X-Z)(T-Y)\right).             \tag{1.1}
$$

活跃物理基记为 $u_0,u_1,v_0,v_1$，零点物理向量为 $w$。
原恒等式 $v(t)^TKv(t)=0$ 及其一阶导数给出活跃 Gram 矩阵
$$
 K_B=
 \begin{pmatrix}
 0&0&A&B\\
 0&C&D&E\\
 A&D&0&0\\
 B&E&0&G
 \end{pmatrix}.                                             \tag{1.2}
$$
令
$$
 U=(u,v,z,\zeta)^T=(K(u_0,w),K(u_1,w),K(v_0,w),K(v_1,w))^T,
 \qquad m=\tfrac12(u+z)+v+\zeta.
$$
全长度五 Gram 矩阵为
$$
 \widehat K=\begin{pmatrix}K_B&U\\U^T&0\end{pmatrix},
 \qquad \operatorname{rank}\widehat K\ge4.                    \tag{1.3}
$$
最后的不等式来自原 $K$ 在六维空间非退化，而长度五原曲线 jets 线性无关：
五维限制的 radical 维数至多为一。

下面只使用原 mean、highest、$N$ 的必要条件。记 $D_K$ 为 $B$ 上的自伴算子
$$
 (D_Kx)_i=\tau\big((K_B)_{i,\bullet}x\big),\qquad
 d=D_K1,\qquad \phi=\tfrac12\tau d.
$$
乘法是两个双数代数的逐因子乘法。原 active mean 为
$$
 e-2D_Kd-2d^2+4\phi d=0,\qquad
 e=(\tau k_0^2,\,2\tau k_0k_1,\,\tau k_2^2,\,2\tau k_2k_3),   \tag{1.4}
$$
其中 $k_i$ 是 (1.2) 的第 $i$ 行，视作 $B$ 的元素。
零点 mean 为
$$
 \tau U^2=2m^2.                                              \tag{1.5}
$$
从原
$N=T_{3,Ky}-\phi(yy^T-2H)+4HKH$
直接展开，
$$
 N=N_B+mR^2,                                                \tag{1.6}
$$
$$
 N_B(x)=\tfrac12\tau((d-\phi)x^2)
       -(\tau x)\tau(dx)+\phi(\tau x)^2
       +\tfrac14\tau(xD_Kx).                                \tag{1.7}
$$
在零点有
$$
 N_B(U)=0.                                                  \tag{1.8}
$$
对两个双点，原 highest 与 $N$ 连同一阶 jet 都为零。
例如在 $u_0,u_1$：
$$
 h+u^3=0,\quad h_1+3u^2v=0,\quad
 n+mu^2=0,\quad n_1+2muv=0,                                 \tag{1.9}
$$
其中
$$
 h=P(K_Bu_0),\quad h_1=\partial_{K_Bu_1}P(K_Bu_0),\quad
 n=N_B(K_Bu_0),\quad n_1=\partial_{K_Bu_1}N_B(K_Bu_0).
$$
第二双点同理。因为原多项式在整条原曲线上恒为零，(1.9) 对任何允许的物理 jet 归一均成立。

## 2. 半权 active mean 的穷尽分类

设
$$
 j=C+E,\qquad k=G+E,\qquad h=j+k.
$$
(1.4) 的四个系数恰为
$$
\begin{aligned}
 E_0&=A(j-k)+2Bh,\\
 E_1&=D(3j-k)-(4B+2A)j+2jh+2E(A+B-D),\\
 E_2&=-A(j-k)+2Dh,\\
 E_3&=B(3k-j)-(4D+2A)k+2kh+2E(A+D-B).
\end{aligned}                                               \tag{2.1}
$$
故 $(B+D)h=0$。

### 2.1 $h=0$

这时 $k=-j$，(2.1) 等价于
$$
 Aj=0,\qquad E(B-D)=0,\qquad 2j(D-B)+EA=0.                   \tag{2.2}
$$
它给出以下两族，允许重叠但没有遗漏：
$$
 \text{I: } C=E=G=0,\quad A,B,D\ \text{任意};                \tag{2.3}
$$
$$
 \text{II: } A=0,\quad B=D=\beta,\quad
 C=j-E,\quad G=-j-E.                                        \tag{2.4}
$$
确实，若 $A\ne0$，则 $j=E=0$。若 $A=0,B\ne D$，仍有 $j=E=0$。
剩下的正是 (2.4)。

### 2.2 $h\ne0$

先有 $D=-B$。若 $A=0$，前后两个 mean 系数迫 $B=D=0$，
另两个迫 $j=k=0$，矛盾。所以 $A\ne0$。置
$$
 q=\frac{2B}{A},\qquad
 j=\frac h2(1-q),\qquad k=\frac h2(1+q).
$$
剩下的两个 mean 方程的和与差是
$$
 2h\left(A(2q^2-1)+h+\frac{2AE}{h}\right)=0,\qquad
 q(4AE-Ah-2h^2)=0.                                         \tag{2.5}
$$
因此：
$$
 \text{III: } q=0,\quad B=D=0,\quad
 E=\frac{h(A-h)}{2A},\quad C=G=\frac{h^2}{2A};                \tag{2.6}
$$
或
$$
 \text{IV: } q\ne0,\quad
 h=\frac A4(1-4q^2),\quad
 E=\frac{h(A+2h)}{4A},\quad
 C=\frac h2(1-q)-E,\quad G=\frac h2(1+q)-E.                  \tag{2.7}
$$
在 III、IV 中仍保留 $A,h\ne0$。这些分类只整理 (2.1)，没有代入任何额外消元假设。

## 3. 族 I 为空

此时原 (1.7) 简化为
$$
 N_B=-\tfrac D2XY-\tfrac B2ZT
      +\tfrac12(D-B-\tfrac A2)Y^2
      +\tfrac12(B-D-\tfrac A2)T^2.                          \tag{3.1}
$$
两个双点的 highest 值与 jet 为
$$
 u^3=B^2(\tfrac32A-B),\qquad 2u^2v=B^2D,
$$
$$
 z^3=D^2(\tfrac32A-D),\qquad 2z^2\zeta=D^2B.                \tag{3.2}
$$
相应的 $N_B$ 值与 jet 为
$$
 n_u=-\tfrac34AB^2-\tfrac12B^2D+\tfrac12B^3,\quad
 (n_u)_1=-\tfrac12B^2D,
$$
$$
 n_z=-\tfrac34AD^2-\tfrac12D^2B+\tfrac12D^3,\quad
 (n_z)_1=-\tfrac12D^2B.                                     \tag{3.3}
$$

若 $BD\ne0$，(3.2) 迫 $u,z\ne0$。把 (3.2) 代入 (3.3) 后，
$N$ 的两个值式给出
$$
 m=\tfrac12u+v=\tfrac12z+\zeta.
$$
但 $m$ 本来就是这两项的和，故 $m=0$。
第一个 $N$-jet 随即给出 $B^2D=0$，矛盾。

若 $B=0,D\ne0$，则 $u=0$。
当 $z\ne0$ 时，第二个 highest-jet 给 $\zeta=0$，
第二个 $N$ 值给 $m=z/2$，于是 $v=0$。
因此 $U=(z/D)K_B e_1$，且 $e_1^{\mathsf T}K_Be_1=0$；对最后一行列作相同消去，使扩充 Gram 合同于 $K_B\oplus0$。活跃 Gram 秩为二，故 $\operatorname{rank}\widehat K=2$，违反 (1.3)。
当 $z=0$ 时，(3.2) 给 $D=3A/2$，特别是 $A\ne0$。
由 (1.5)，$m=0,\zeta=-v$；再由 (1.8)、(3.1)，
$$
 N_B(U)=-\tfrac A2v^2=0.
$$
故 $U=0$，仍只有 Gram 秩二。
$D=0,B\ne0$ 完全由交换两个原双点得到同一结论。

最后若 $B=D=0$，(3.2) 给 $u=z=0$，(1.5) 给 $\zeta=-v$。
若 $A\ne0$，(1.8) 仍给 $v=0$，Gram 秩二；
若 $A=0$，整个活跃 Gram 为零，任意一列扩充的秩至多为二。
族 I 的所有零除数例外都已包括。

## 4. 族 II 为空

从原 (1.7)，
$$
\begin{aligned}
 N_B={}&-\tfrac\beta2XY-jXY+jYZ-\tfrac\beta2ZT-jXT+jZT\\
 &+\tfrac14(j-E)X^2+\tfrac E2XZ-\tfrac14(j+E)Z^2.
\end{aligned}                                               \tag{4.1}
$$
两个双点处
$$
 P(K_Bu_0)=P(K_Bv_0)=\beta^3,\qquad
 N_B(K_Bu_0)=N_B(K_Bv_0)=0,
$$
$$
 (n_u)_1=\beta^2(j-\beta/2),\qquad
 (n_z)_1=-\beta^2(j+\beta/2).                                \tag{4.2}
$$
若 $\beta\ne0$，highest 值迫 $u,z\ne0$，两个 $N$ 值迫 $m=0$。
两个 $N$-jet 又迫 $j=\beta/2=-\beta/2$，矛盾。

若 $\beta=0$，highest 值给 $u=z=0$。
于是 $\widehat K$ 中两个基点方向 $u_0,v_0$ 的行列全为零，
其秩至多为三，违反 (1.3)。
这里不需要除以 $j,E$ 或任何 jet 交叉数。

## 5. 族 III 为空

方程对所有 Gram 配对的共同缩放齐次，故可令 $A=1$；
把 $h/A$ 仍记为 $h\ne0$。这时
$$
 K_B=
 \begin{pmatrix}
 0&0&1&0\\
 0&h^2/2&0&h(1-h)/2\\
 1&0&0&0\\
 0&h(1-h)/2&0&h^2/2
 \end{pmatrix}.
$$
在第一个基点 $K_Bu_0=(0,0,1,0)$：
$$
 P(K_Bu_0)=0,\qquad N_B(K_Bu_0)=h^2/8.
$$
highest 迫 $u=0$，而原 $N$ 值遂迫 $h^2/8=0$，矛盾。

## 6. 族 IV 为空：不除以任何零点极坐标

先记录一个直接消去式：任意满足 (1.9) 的 $h,h_1,n,n_1,u,v,m$，都有
$$
 3h\,n_1-2n\,h_1=0.                                        \tag{6.1}
$$
把四个式中的 $h,h_1,n,n_1$ 直接代入就得到零。
这个恒等式对 $u=0$、$m=0$ 同样成立，因此不需要额外排除 $q=\pm3$ 等候选。

仍利用共同齐次性令 $A=1$。于是
$$
 B=q/2,\quad D=-q/2,\quad h=(1-4q^2)/4,\quad
 E=h(1+2h)/4,
$$
$$
 C=h(1-q)/2-E,\qquad G=h(1+q)/2-E,\qquad q\ne0.              \tag{6.2}
$$
对两个双点分别以原 (1.1)、(1.7) 重建 (6.1)，记结果为
$\mathcal E_u,\mathcal E_z$。直接展开、相加相减得
$$
 \mathcal E_u+\mathcal E_z=\frac{3q^2}{512}f(q^2),\qquad
 \mathcal E_u-\mathcal E_z=\frac{3q}{2048}g(q^2),             \tag{6.3}
$$
其中
$$
 f(x)=1-9x+52x^2-160x^3,
$$
$$
 g(x)=3-16x-32x^2+128x^3+256x^4.                             \tag{6.4}
$$
这两个原有理系数一元多项式的 Euclidean gcd 为 $1$。
附带短脚本从 (1.1)、(1.2)、(1.4)、(1.7) 重建 (6.3)，
再在 $\mathbb Q[x]$ 中实际计算此 gcd；不使用有限域提升、数值近似或未展示的 Gröbner 输出。
因为 $q\ne0$，(6.1)–(6.4) 要求 $f(q^2)=g(q^2)=0$，不可能。

## 7. 结论与仍开范围

因此，在本附录的原外均值 essential-four 假设下，
$$
 \operatorname{rank}H=4,\quad
 D=(2+2)+1_{\rm zero},\quad
 \tau(1_{\epsilon})=\tau(1_{\eta})=\tfrac12
$$
不可能满足完整原 mean、highest、$N$ 系统。

证明覆盖本半权支路所有 $A,B,C,D,E,G$ 为零或退化的情况，并保留真实原 jets。
它不声称处理两个双点的一般权重 $a,1-a$，也不处理孤立零点加
$3+1$、$2+1+1$、$1+1+1+1$ 的单位补空间，更不关闭 unit rank-five 或 inner-mean 支路。

## 8. 精确复核源

配套
[原半权2+2精确源码](../notes/2026-11-20-essential-four-unit-two-plus-two-half-isolated-zero-verify.py)
只从上述原源式重建必要恒等式、各族局部值/jet 与最后 $\mathbb Q[x]$ gcd。
只输出分项 PASS；不保存可重算的消元中间表。


实际运行：[Actions run44727076042](https://github.com/Rogerhu12/math-research-public/actions/runs/44727076042)，job136257087646，冻结提交5bd3fd23c037e85ab1587bd684799cd389726da1，SymPy 1.13.3/mpmath 1.3.0、无参数。原P/N/四mean、四族值与jet、无除法兼容式及最终QQ gcd全部通过，用时0.355225056秒。根已读原job日志并匹配源码SHA-256 dbc2e5ec82604944438960ed0e3d9bcf3638c5260093767dd377d6b862561779；该源有界输出SHA-256为025f2bdb9d39f4c86c0b37618019ddd67b11b43d77e453ef6f431c753823b1b3，decoded job-log SHA-256为af614e24da8f13e6d0070da04a59b3080b46bfecab665b1a3244fcdf73ee6da9。只保存源、参数、运行身份与SHA，不存计算余式或日志正文。同job在11:22:32 UTC实际pull成功，两README均未变。
