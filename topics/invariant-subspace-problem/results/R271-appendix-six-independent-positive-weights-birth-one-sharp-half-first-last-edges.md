# 六个独立正权：完整出生一首末边的尖锐 1/2 常数

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f / stable_kernel_return。

**状态：全文结论已证明。** 对六个任意独立正权，整个五维物理出生一源上的首边和末边均严格具有常数 $1/2$，且此统一常数不能再小。这里使用原六位整个精度矩阵；此前单独六位满支持块的均值流失败仍按原范围保留，没有被改记为成功。

## 1. 定理与完整精度

在六位物理 Boolean Hilbert 空间上任取 $b_i>0$，令
$$
d=\sum_{i=1}^{6}b_iE_i,\qquad
K=\ker d\cap\mathcal H_1,\qquad \dim K=5,
$$
$$
\Gamma_j=\mathcal J_{j,1}^*\mathcal J_{j,1},\qquad
\mathcal J_{j,1}=(d^j/j!)^\dagger|_K,\qquad 0\le j\le4.
$$
全部 MP 逆均先在完整层取逆，再压到这个实际 primitive 源。则
$$
\boxed{
\Gamma_1\Gamma_2^{-1}\Gamma_1\prec\frac12 I_K,\qquad
\Gamma_3\Gamma_4^{-1}\Gamma_3\prec\frac12\Gamma_2.
}
\tag{1.1}
$$

写 $z_i=b_i^2$、$b=(b_i)$、$T_0=\operatorname{diag}z_i$、$Q_0=bb^*$，以及 $S=e_1(z)$、$Z=e_2(z)$、$W=e_3(z)$。完整出生一精度公式为
$$
F_1=SI-2T_0+Q_0,\qquad
F_2=ZI-2ST_0+3T_0^2+SQ_0-T_0Q_0-Q_0T_0,
$$
$$
C_2=F_1-\frac{(S-T_0)Q_0(S-T_0)}{Z},
$$
$$
C_3=F_2-\frac{(Z-ST_0+T_0^2)Q_0(Z-ST_0+T_0^2)}{W}.
\tag{1.2}
$$
这里 $C_2,C_3$ 分别是 $\Gamma_1^{-1},\Gamma_2^{-1}$ 在 $\mathbb Cb$ 上的零延拓，沿用此前 half 稿的下标。它们确为物理自伴，且同时消去 $b$。

首边等价于
$$
H=C_2^2-2C_3\succ0\quad\hbox{在 }K\hbox{ 上}.
$$
令 $J=Z^2W\,H$，其中标量因子在正权上严格正。

## 2. 先形成整个矩阵，再除去真实零线

[原来源推导](../notes/2026-11-28-six-bit-full-birth-one-half-companion-characteristic-8542.md)完整给出了六点求值相似。物理去权坐标的内积为 $\operatorname{diag}z_i$；在互异 $z_i$ 上进一步用 $1,x,\ldots,x^5$ 求值基，$T_0$ 成为六次 companion 矩阵 $\mathcal T$，$Q_0$ 成为只有首行 $(p_1,\ldots,p_6)$ 非零的 $\mathcal Q$，其中 $p_j=\sum_i z_i^j$。

仍在完整六维来源上置
$$
\mathcal A=Z F_1-(S-\mathcal T)\mathcal Q(S-\mathcal T),
\qquad
\mathcal G=Z-S\mathcal T+\mathcal T^2.
$$
于是完整无分母式为
$$
\boxed{
J=W\mathcal A^2-2Z^2W F_2+2Z^2\mathcal G\mathcal Q\mathcal G.
}
\tag{2.1}
$$
形成 (2.1) 后，其第一列准确为零。这是原 $C_2b=C_3b=0$，而非人为删除源。令 $\widehat J$ 为之后取出的右下 $5\times5$ 商块，即
$$
\det(tI_6+J)=t\det(tI_5+\widehat J)
=t(t^5+c_1t^4+c_2t^3+c_3t^2+c_4t+c_5).
\tag{2.2}
$$
五个商特征值正是物理 $J|_K$ 的实特征值。最终实际特征系数通过连续性延拓到重复权；不要求在重复权处继续使用可逆求值基，也没有把 companion 普通转置替代物理伴随。

## 3. 原完整特征系数的首次实际返回

[冻结原源码](../notes/2026-11-28-six-bit-full-birth-one-half-companion-characteristic-8542.py)使用 Faddeev–LeVerrier，逐阶保存完整整数系数。run **46048997934**、job **140675340048** 的首次实际运行耗时 0.255475250 秒，最大 RSS 35,240 KiB，退出码 0；内层依次在约 0.02475、0.05748、0.11087、0.13712、0.18506 秒返回五阶。完整 Cayley–Hamilton 余矩阵为零。

[唯一完整原参数](../notes/2026-11-28-six-bit-full-half-characteristic-exact-input-8542.json)仅 9,168 字节，原 SHA256 为
$$
\texttt{3528a1b7b56167987e4c1c7c35048330a76cd2179ea263f49bf6cb29c4022bdf}.
$$
在只除去明确正整数和 elementary 单项式因子后，得到准确分解
$$
\begin{aligned}
c_1&=f_1,\\
c_2&=2Z^2W\,f_2,\\
c_3&=2Z^4W^2\,f_3,\\
c_4&=Z^6W^3\,f_4,\\
c_5&=SZ^8W^4\,f_5.
\end{aligned}
\tag{3.1}
$$
全部 $f_k$ 的系数均保存在唯一原参数中；没有仅保某个首项或数值采样。

| $k$ | $c_k$ 加权次数 | $f_k$ 加权次数 | 完整 elementary 项数 |
|---|---:|---:|---:|
| 1 | 9 | 9 | 7 |
| 2 | 18 | 11 | 20 |
| 3 | 27 | 13 | 41 |
| 4 | 36 | 15 | 65 |
| 5 | 45 | 16 | 54 |

原程序还逐阶核对同一物理等权值 $c_k(1,\ldots,1)=\binom5k18000^k$。它返回的状态准确为 $\texttt{EXACT\_CHARACTERISTIC\_READY}$；下一节才支付原正权正性。

## 4. 三十三条均值正差支付全部五阶

对六变量定义归一对称单项式均值
$$
M_\lambda(z)=\frac1{6!}\sum_{\sigma\in S_6}z_{\sigma(1)}^{\lambda_1}\cdots z_{\sigma(6)}^{\lambda_6}.
$$
使用精确身份
$$
S^n=\sum_{\lambda\vdash n,\ \ell(\lambda)\le6}
\frac{n!}{\lambda_1!\cdots\lambda_6!}
\frac{6!}{\prod_a(\#\{i:\lambda_i=a\})!}M_\lambda,
$$
$$
M_\lambda e_j=\sum_{|I|=j}
M_{\operatorname{sort}(\lambda+\mathbf1_I)},
\tag{4.1}
$$
将同一保存的 $f_k$ 以 BigInt Horner 完整变回原变量。

若两个指数为 $a\ge b+2$，把 $(a,b)$ 改为 $(a-1,b+1)$ 并排序所得 $\mu$ 满足 $M_\lambda-M_\mu\ge0$。其自足平方身份为
$$
x^ay^b+x^by^a-x^{a-1}y^{b+1}-x^{b+1}y^{a-1}
=x^by^b(x-y)^2
\sum_{j=0}^{a-b-2}x^{a-b-2-j}y^j.
\tag{4.2}
$$
乘其余四个变量幂并完整对称平均即得该正差。

[完整三十三条正差](../notes/2026-11-28-six-bit-full-half-mean-differences-8542.json)只有 2,016 字节。完整[证书源码](../notes/2026-11-28-six-bit-full-half-positive-certificate-8542.mjs)逐项核对原 9,168 字节与源码 SHA256、原五个多项式和除因子后多项式的全部 SHA256、每个正因子与次数、(4.1) 的原变量展开、每条合法正差，以及减去这些差后的全部非负均值权。相同证书核心已在纯 V8 BigInt 中实际执行，耗时 **56 毫秒**；[完整回执](../notes/2026-11-28-six-bit-full-half-positive-certificate-8542.json)给：

| $k$ | 原变量轨道数 | 原负轨道数 | 正差数 | 剩余严格正轨道 | 最小剩余均值权 |
|---|---:|---:|---:|---:|---:|
| 1 | 18 | 0 | 0 | 18 | 120 |
| 2 | 35 | 0 | 0 | 35 | 360 |
| 3 | 61 | 0 | 0 | 61 | 120 |
| 4 | 96 | 3 | 3 | 93 | 120 |
| 5 | 96 | 20 | 30 | 65 | 120 |

因此每个 $f_k$ 都是有限个正倍数的 (4.2) 对称均值差，加上一个非空的严格正均值和。对全部 $z_i>0$，有 $f_k>0$，进而 (3.1) 的五个实际 $c_k$ 全部严格正。

若 $J|_K$ 有负特征值 $\lambda<0$，则 (2.2) 的五次因子在 $t=-\lambda>0$ 为零，与全部正系数矛盾；$c_5>0$ 排除零特征值。因此 $J|_K\succ0$，证明首边。

## 5. 真实倒数权末边

[R239 全出生倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)是同一个可逆源同余，保全部物理 Gram。在六位出生一合法高度 $h=4$ 下，它把倒数权首边返回为
$$
\Gamma_3\Gamma_2^{-1}\Gamma_3\prec\frac12\Gamma_4.
$$
对正定 $A,B,C$，$AB^{-1}A\prec cC$ 当且仅当 $AC^{-1}A\prec cB$，因为相应两个归一化算子互为伴随并具有相同范数。取 $A=\Gamma_3,B=\Gamma_2,C=\Gamma_4$ 得 (1.1) 的末边。没有交换 primitive 压缩与逆。

## 6. 常数 1/2 的真正尖锐性

取实际六位权
$$
b=(\sqrt t,1,1,1,1,1),\qquad t>0.
$$
在头坐标和五个尾坐标的归一平均组成的二维物理空间中，完整 $F_1,F_2$ 分别为
$$
F_1=\begin{pmatrix}5&\sqrt{5t}\\\sqrt{5t}&t+8\end{pmatrix},
\qquad
F_2=\begin{pmatrix}10&4\sqrt{5t}\\4\sqrt{5t}&8t+18\end{pmatrix}.
$$
其行列式准确为 $40,180$。尾部置换作用使这个二维空间约化这两个完整算子，故完整逆确在此块内计算。

其中实际 primitive 单位向量为
$$
u=\frac{(\sqrt5,-\sqrt t)}{\sqrt{t+5}},
$$
在原六坐标中与 $(5,-\sqrt t,-\sqrt t,-\sqrt t,-\sqrt t,-\sqrt t)$ 同向。整个 $K$ 中的尾置换不变子空间只有这一维，因此 $\Gamma_1,\Gamma_2$ 都在它上为标量。取真正完整逆压缩，得到
$$
\Gamma_1|_{\mathbb Cu}=\frac{t+2}{2(t+5)},\qquad
\Gamma_2|_{\mathbb Cu}=\frac{t+1}{2(t+5)}.
$$
所以同一实际源上的首边比为
$$
\frac{(t+2)^2}{2(t+5)(t+1)}\longrightarrow\frac12
\qquad(t\longrightarrow\infty).
$$
每个有限 $t>0$ 仍严格小于 $1/2$，因为
$(t+5)(t+1)-(t+2)^2=2t+1>0$；但任何小于 $1/2$ 的统一常数都会被充分大的有限 $t$ 违反。真实倒数权对偶也使末边常数尖锐。

## 7. 与全位数 2/3 尖锐常数的相容范围

本文只固定六位。[旧全位数 $2/3$ 定理](R271-appendix-sharp-two-thirds-universal-birth-one-first-and-last-edges.md)同时量化所有位数，因此其尖锐性与本文一致。$1/2$ 不能移到七位：例如实际权
$$
b=(6,1,1,1,1,1,1)
$$
的尾置换不变 primitive 直线由 $(1,-1,-1,-1,-1,-1,-1)$ 张成。相同完整二维逆给
$$
\Gamma_1=11/30,\qquad\Gamma_2=4/15,\qquad
\Gamma_1^2/\Gamma_2=121/240>1/2
$$
在该直线上成立。这只排除七位的同一 half 常数，不反驳旧 $2/3$ 或普通常数一。

本文支付整个六位出生一首末边及同源 half 预算；内部高度、一般高出生以及其与原边界物理头的 joint 来源仍按原开放项继续。已刊六位出生二首边使用其自己的完整上来源，不能仅由本定理代替更高位数所需的 S1/S2。原 $N=M$ 与普通 ISP 未因此完成。
