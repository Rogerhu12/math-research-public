# R271 附录：四异权四池的真实低边 Gram 与严格迹上界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。
状态：完整证明及可执行精确整数证书；仅固定六维 primitive 块；低边 $n=1$ 及 §7 的高边 $n=3$。

## 1. 范围及所扣旧结论

[R239 全高度二稿](R239-appendix-four-exceptional-weights-full-height-two-primitive-gram-bound.md)
处理四异权与两个单位池位的 $L=2,\delta=2,h=2$ 块。
该短池在中间阶同时有两端非法状态，只有三个低次自由参数。
本文取 $L=4,\delta=2,h=4$，中间阶有四个低次参数、下一阶有五个；
不能由旧短池证书换记号得到。

[R271 低边次数释放](R271-appendix-low-edge-degree-release-schur-cost-and-exceptional-sources.md)
已给本块全部正头权下的 $C_0=6$ 基线及一个未付异常标量。
本文使用完整最小逆付掉本处全部六维源，结论为
$$
\boxed{H_1H_2^{-1}H_1\prec\frac52H_0.}
\tag{1.1}
$$
还得到更强的明确迹预算
$$
\boxed{\operatorname{tr}(H_0^{-1}H_1H_2^{-1}H_1)<\frac52.}
\tag{1.2}
$$
这里没有声称最优系数，也未扩展到任意池长或整个八位 primitive 空间。

## 2. 原模型和全部最小原像

取四个任意正头权与四个单位池位，
$$
D=\sum_{i=1}^4 a_iE_i+\sum_{j=5}^8 E_j,\qquad a_i>0,\qquad z_i=a_i^2.
$$
保留池置换群 $S_4$ 的固定部分，primitive 出生为 $s=2$，总串长为 $h=4$。
该固定 primitive 块为六维。源坐标记作
$$
f_x(X)=\sum_{1\le i<j\le4}x_{ij}X_iX_j.
$$
源基一般非正交，记其实际嵌入为 $\mathcal E$。完整先逆后压的 Gram 为
$$
H_n=\mathcal E^*
\left(\frac{D^n(D^*)^n}{(n!)^2}\Big|_{\mathcal H_2}\right)^{-1}\mathcal E,
\qquad n=0,1,2.
\tag{2.1}
$$
特别 $H_0=\mathcal E^*\mathcal E>0$。

[R239 一参数稿 §10](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)
给出同一原空间的准确多重仿射最小化。写
$R\subseteq[4]$、$r=|R|$、$z_R=\prod_{i\in R}z_i$，本处三阶为
$$
\begin{aligned}
x^*H_0x
 &=\sum_{r=2}^4\frac{z_R}{\binom4{r-2}}|f_x(R)|^2,\\
x^*H_1x
 &=\min_{\beta\in\mathbb C^4}
 \sum_{r=1}^4\frac{z_R}{\binom4{r-1}}
 \left|f_x(R)+\sum_i\beta_i1_{\{i\in R\}}\right|^2,\\
x^*H_2x
 &=\min_{\beta_0,\ldots,\beta_4\in\mathbb C}
 \sum_{r=0}^4\frac{z_R}{\binom4r}
 \left|f_x(R)+\beta_0+\sum_i\beta_i1_{\{i\in R\}}\right|^2.
\end{aligned}
\tag{2.2}
$$
各行的求和均遍历所写秩上的全部子集。

简述本处真实最小化的维数检查：固定出生二目标层维数为
$1+4+6=11$；阶一输入层维数为 $1+4+6+4=15$，阶二输入层维数为 $16$。
正权 Boolean Lefschetz 满射及池正交平均给固定部分的满射，
所以两个完整解空间分别恰有四维和五维自由参数。
所引多重仿射解在全部状态上由值唯一确定，因此 (2.2) 的参数已穷尽。
任意全空间解先作池正交平均，源不变、范数不增；故这里是全 Hilbert
Moore--Penrose 最小逆，不是只在固定部分选取试探原像。

## 3. 准确整数 Gram 字典

按边序 $12,13,14,23,24,34$ 排列六维源。定义
$$
v_R=(1_{\{i,j\}\subseteq R})_{i<j},\quad
b_R=(1_{\{i\in R\}})_{i=1}^4,\quad
t_R=(v_R,1,b_R)\in\mathbb R^{11}.
$$
令
$$
A=12H_0=\sum_{r=2}^4\alpha_r z_Rv_Rv_R^T,\qquad
(\alpha_2,\alpha_3,\alpha_4)=(12,3,2).
\tag{3.1}
$$

对中间阶取整数权
$$
(\mu_1,\mu_2,\mu_3,\mu_4)=(24,6,4,6)
$$
并置
$$
S=\sum_{r=1}^4\mu_r z_Rv_Rv_R^T,\quad
M=\sum_{r=1}^4\mu_r z_Rv_Rb_R^T,\quad
C=\sum_{r=1}^4\mu_r z_Rb_Rb_R^T.
\tag{3.2}
$$
准确有
$$
24H_1=S-MC^{-1}M^T,\qquad
\Delta=\det C,\quad
K=\Delta S-M\,\operatorname{adj}(C)M^T.
\tag{3.3}
$$
故 $H_1=K/(24\Delta)$。

下一阶完整十一维 Gram 是
$$
G=\sum_{r=0}^4\nu_r z_Rt_Rt_R^T,\qquad
(\nu_0,\nu_1,\nu_2,\nu_3,\nu_4)=(24,6,4,6,24).
\tag{3.4}
$$
按前六个源坐标及后五个低次坐标分块。
实际 $24H_2$ 是 $G$ 对后五坐标作完的 Schur 补，
因此不是简单取 $G$ 的左上块；准确的逆是
$$
H_2^{-1}
=24\,(G^{-1})_{\rm top}
=\frac{24\,J}{\det G},\qquad
J=(\operatorname{adj}G)_{\rm top}.
\tag{3.5}
$$
$A,C,G$ 都严格正定：$A$ 的六个双点状态给六个正坐标项，
$C$ 的四个单点状态给四个正坐标项，
$G$ 的空集、四个单点和六个双点的十一列组成可逆的整数评价矩阵。
所以每次取逆和 Schur 补都有完整正性依据。

## 4. 全部矩阵次序保留的迹恒等式

定义两个标量整数多项式
$$
\mathscr D=\det(A)\,\Delta^2\det(G),\qquad
\mathscr N=\operatorname{tr}\!\left(
 \operatorname{adj}(A)\,K\,J\,K\right).
\tag{4.1}
$$
由 (3.1)、(3.3)、(3.5)，
$$
\boxed{
\operatorname{tr}(H_0^{-1}H_1H_2^{-1}H_1)
=\frac{\mathscr N(z)}{2\mathscr D(z)}.
}
\tag{4.2}
$$
系数 $1/2=12\cdot24/24^2$。没有交换 $K,J,\operatorname{adj}(A)$；
代码也按该真实矩阵乘法顺序计算。

下面的精确证书证明
$$
\boxed{5\mathscr D-\mathscr N>0\qquad(z_i>0).}
\tag{4.3}
$$
$\mathscr D>0$ 已由 §3 支付，故 (4.2) 给 (1.2)。

最后令
$$
T=H_0^{-1/2}H_1H_2^{-1}H_1H_0^{-1/2}>0.
$$
它与 (4.2) 中的矩阵有同一迹。
对正矩阵，最大特征值不超过迹，因而 $T\prec(5/2)I$，
得到 (1.1)。这一步只使用正矩阵的迹上界，不把逐项标量
Cauchy--Schwarz 当作算子序，也不以源维数补一个未经证明的升级。

## 5. 可复现的完整 BigInt 证书

完整可执行证书：

[四头四池低边迹证书](../notes/2026-11-13-four-exceptional-weights-four-pool-low-edge-trace-certificate-1cf.mjs)

完整代码 blob：
$$
\texttt{de06c74caa300272eaae075de503cfa9a2b5908b}.
$$

脚本从全部十六个状态直接构造 (3.1)--(3.4)。
行列式及伴随采用完整 Cauchy--Binet 展开：
$$
\det\!\left(\sum_jw_ju_ju_j^T\right)
=\sum_{|I|=d}\left(\prod_{i\in I}w_i\right)\det(u_i:i\in I)^2,
$$
$$
\operatorname{adj}\!\left(\sum_jw_ju_ju_j^T\right)
=\sum_{|I|=d-1}\left(\prod_{i\in I}w_i\right)c_Ic_I^T,
\tag{5.1}
$$
其中 $c_I$ 是实际 $d\times(d-1)$ 整数列阵的有符号余子式向量。
各个常整数行列式由 Bareiss 消元精确计算，每次除法检查余数为零。

$K$ 还独立用五列的完整 Schur Cauchy--Binet 展开计算。
对五个状态的 $4\times5$ 线性列阵 $(b_R)$，记其有符号余子式向量为 $u$；
则该列组对 $K$ 的贡献准确为
$$
\left(\prod_R \mu_{|R|}z_R\right)
\left(\sum_Ru_Rv_R\right)\left(\sum_Ru_Rv_R\right)^T .
\tag{5.2}
$$
这由对 $C$ 添一行 $x^Tv_R$ 的五阶 Gram 行列式，再对 $x$ 极化得到。
代码随后逐项另核
$$
A\,\operatorname{adj}A=(\det A)I,\quad
C\,\operatorname{adj}C=(\det C)I,\quad
G\,\operatorname{adj}G=(\det G)I,
$$
$$
K=\Delta S-M\,\operatorname{adj}C\,M^T.
\tag{5.3}
$$
因此 (5.2) 没有替换真正的四参数中间 Schur 补。

完整输出的精确计数是：

| 对象 | 非零列组数 |
|---|---:|
| $\det A$ | 303 |
| $\operatorname{adj}A$ | 423 |
| $\Delta$ | 940 |
| $K$ 的五列展开 | 2778 |
| $\det G$ | 3008 |
| $\operatorname{adj}G$ | 7408 |

$\mathscr N,\mathscr D$ 的非零单项式支撑完全相同，均有 **21251** 个单项式，
其系数分别全为正整数。
对每个单项式 $z^\alpha$，代码准确检验
$$
5\mathscr D_\alpha-\mathscr N_\alpha>0.
$$
最小的非零差是准确整数
$$
\boxed{511284864104792064.}
\tag{5.4}
$$
例如它出现在指数 $(21,17,17,16)$，对称置换可能给同值。
最终单变量最大指数为 $21$，总次数最大为 $71$。

四变量指数分别占用 base-$32$ 的独立槽。所有表达式最多含二十五个
原始多重仿射状态因子：分母为 $6+4+4+11=25$，分子为
$5+5+10+5=25$。每次多项式乘法前仍计算实际各坐标指数上界，
并准确断言两输入上界之和不超过 $25$；实际最大值为 $21$。
所以槽间不可能进位。全部多项式系数、整数行列式、正负判断
都使用 BigInt，无浮点阈值或抽样权参数。

上述严格正整数系数证明 (4.3) 对全部 $z_i>0$ 同时成立。

## 6. 原 primitive 内积及尚未覆盖的范围

若把实际 primitive 算子写回源坐标，则
$$
[\Gamma_n]=H_0^{-1}H_n.
$$
以真实源内积 $H_0$ 计算，
$\Gamma_1\Gamma_2^{-1}\Gamma_1\prec(5/2)I$
正好等价于 (1.1)。这里没有把非正交源基当作正交基。

§§1–6 先证明四异权、四单位池、出生二固定块的低相邻阶 $n=1$；§7 另以准确倒数权运输支付同块 $n=3$。
池长变化、该块中间阶、其它弱池字符串及原连续尾的全局界
须分别支付。它确实付清本块原来的一维异常费用，
但不由此宣布一般四异权或任意 primitive 的权无关相邻常数，
也未完成原边界 $N=M$。

## 7. 同一固定块高边 $n=3$ 的准确倒数权运输

本节是 §1 低边定理与
[R239 任意出生反向对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)
§§1--5 的直接推论。两个模型的权分别为
$$
(a_1,a_2,a_3,a_4,1,1,1,1),
\qquad
(a_1^{-1},a_2^{-1},a_3^{-1},a_4^{-1},1,1,1,1).
$$
池仍是同一个四位单位池。

令 $P_{\rm fix}$ 为池置换群 $S_4$ 的正交平均。
它与 $D,D^*$、完整层 Gram 及其逆都交换，因而约化相应 primitive 空间和全部 $\Gamma_n$。
R239 的准确同构
$$
B_s e_I=a_I^2e_I,\qquad s=2,
$$
只在四个头位产生非单位权，故 $B_s$ 及其有限维逆也与 $P_{\rm fix}$ 交换。
因此它把原模型六维固定 primitive 块双射到倒数权模型的同一固定块。
这里不是把整个 primitive 的对偶免费限制到一个未证不变的子空间。

设 $b_i=a_i^{-1}$、$Z=\prod_{i=1}^4a_i^2$。
在这两个真实固定 Hilbert 子空间之间，完整反向对偶准确给
$$
\Gamma_k(a)=Z^{-1}B_s^*\Gamma_{4-k}(b)B_s,\qquad 0\le k\le4.
\tag{7.1}
$$
对倒数权模型使用已证 $n=1$：
$$
\Gamma_1(b)\Gamma_2(b)^{-1}\Gamma_1(b)
\prec\frac52\Gamma_0(b).
$$
严格正矩阵的 Schur 等价在不交换矩阵的前提下给
$$
\Gamma_1(b)\Gamma_0(b)^{-1}\Gamma_1(b)
\prec\frac52\Gamma_2(b).
\tag{7.2}
$$
将 (7.2) 以 $Z^{-1/2}B_s$ 作同余，再用 (7.1)，得到
$$
\boxed{
\Gamma_3(a)\Gamma_4(a)^{-1}\Gamma_3(a)
\prec\frac52\Gamma_2(a).
}
\tag{7.3}
$$
按同一个非正交源坐标，正好是
$$
\boxed{H_3H_4^{-1}H_3\prec\frac52H_2.}
\tag{7.4}
$$

迹预算也保留：共用可逆同余后，相关乘积相似，
再使用有限维迹的循环性，
$$
\begin{aligned}
\operatorname{tr}\!\left(\Gamma_2(a)^{-1}
 \Gamma_3(a)\Gamma_4(a)^{-1}\Gamma_3(a)\right)
&=\operatorname{tr}\!\left(\Gamma_2(b)^{-1}
 \Gamma_1(b)\Gamma_0(b)^{-1}\Gamma_1(b)\right)\\
&=\operatorname{tr}\!\left(\Gamma_0(b)^{-1}
 \Gamma_1(b)\Gamma_2(b)^{-1}\Gamma_1(b)\right)
<\frac52.
\end{aligned}
\tag{7.5}
$$
这同时说明低、高两边的严格常数来自同一整数证书。
本节没有覆盖中间阶 $n=2$，也没有把四池固定块扩成全八位 $K_2$。
