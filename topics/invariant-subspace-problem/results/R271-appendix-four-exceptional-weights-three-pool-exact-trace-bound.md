# R271 附录：四异权三池短块的真实边界约束与严格迹界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。
状态：完整证明与全正权 BigInt 证书；池固定 primitive 出生二。

## 1. 短池范围和定理

考虑四个任意正头权与三个单位池位，
$$
D=\sum_{i=1}^4a_iE_i+\sum_{j=5}^7E_j,\qquad a_i>0.
$$
取单位池置换群 $S_3$ 的固定 primitive 出生二块。
该块为六维，总串长为 $h=3$。
设 $H_n$ 是同一个真实源嵌入下的完整逆后压缩 Gram。

**定理 1。** 两个合法相邻阶均满足
$$
\boxed{
H_1H_2^{-1}H_1\prec\frac94H_0,\qquad
H_2H_3^{-1}H_2\prec\frac94H_1.
}
\tag{1.1}
$$
相应的归一化迹也严格小于 $9/4$。

此块不属于 [任意长池低边稿](R271-appendix-four-exceptional-weights-arbitrary-pool-low-edge-uniform-trace-bound.md)
的 $L\ge4$ 范围。下一阶在全头状态上有必须保留的真实约束，
其可行低次参数只有四个。本稿直接对这个受约束的完整最小逆计算，
不由长池的整数不等式外推。

## 2. 源、真实非法状态和全部参数

记
$$
z_i=a_i^2,\quad z_R=\prod_{i\in R}z_i,\quad
f_x(X)=\sum_{i<j}x_{ij}X_iX_j.
$$
由 [R239 一参数稿 §11](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)
的完整短池参数化，源空间在此无额外最高系数约束：
$|R|>L+\delta=5$ 在四头集合上不会发生。
因此六个 $x_{ij}$ 独立，源嵌入 $\mathcal E$ 单射，且
$$
H_n=\mathcal E^*
\left(\frac{D^n(D^*)^n}{(n!)^2}\Big|_{\mathcal H_2}\right)^{-1}
\mathcal E,\qquad 0\le n\le3.
$$

三个必要的最小化准确为
$$
\begin{aligned}
x^*H_0x
 &=\sum_{r=2}^4\frac{z_R}{\binom3{r-2}}|f_x(R)|^2,\\
x^*H_1x
 &=\min_{\beta\in\mathbb C^4}
   \sum_{r=1}^4\frac{z_R}{\binom3{r-1}}
   |f_x(R)+b_R^T\beta|^2,\\
x^*H_2x
 &=\min_{\substack{P\text{ 仿射}\\(f_x+P)([4])=0}}
   \sum_{r=0}^3\frac{z_R}{\binom3r}|f_x(R)+P(R)|^2,
\end{aligned}
\tag{2.1}
$$
其中 $b_R=(1_{\{i\in R\}})_{i=1}^4$。
第三行不能添加一个带零分母的全头项，也不能删去其约束。

给出独立维数检查：固定目标二孔层维数为 $11$；
一阶输入三孔层、二阶输入四孔层的固定维数均为 $15$。
完整 Boolean Lefschetz 满射经池平均仍满射，
故两个解空间分别有四维自由参数。
(2.1) 的两组四参数可行式由全部布尔值唯一确定；
所引短池有限差分核验其真实输出，所以已经穷尽全部固定解。
任意全空间解经池正交平均不改源且不增范数，
于是这里是全 Hilbert Moore--Penrose 范数。

为实现第三行，取四个独立低次参数 $\gamma_0,\gamma_1,\gamma_2,\gamma_3$，
准确写为
$$
F(X)=f_x(X)-f_x([4])X_4
+\gamma_0(1-X_4)+\sum_{i=1}^3\gamma_i(X_i-X_4).
\tag{2.2}
$$
它的最高二次部分仍是原 $f_x$，且 $F([4])=0$。
反过来每个满足该条件的仿射修正都唯一具有 (2.2)。

## 3. 十维下一阶 Gram 及真实迹恒等式

按源边序 $12,13,14,23,24,34$，
$$
v_R=(1_{\{i,j\}\subseteq R})_{i<j}.
$$
令
$$
A=6H_0
 =\sum_{r=2}^4\alpha_r z_Rv_Rv_R^T,\qquad
(\alpha_2,\alpha_3,\alpha_4)=(6,2,2).
\tag{3.1}
$$
对中间阶使用整数权
$$
(\mu_1,\mu_2,\mu_3,\mu_4)=(6,2,2,6),
$$
并置
$$
S=\sum_{r=1}^4\mu_rz_Rv_Rv_R^T,\quad
M=\sum_{r=1}^4\mu_rz_Rv_Rb_R^T,\quad
C=\sum_{r=1}^4\mu_rz_Rb_Rb_R^T.
$$
写
$$
\Delta=\det C,\qquad
K=\Delta S-M\,\operatorname{adj}(C)M^T.
$$
完整中间最小化给
$$
6H_1=S-MC^{-1}M^T,\qquad H_1=K/(6\Delta).
\tag{3.2}
$$

下一阶必须使用 (2.2)。令
$$
\widehat v_R=v_R-1_{\{4\in R\}}{\bf1}_6,\qquad
u_R=(1-1_{\{4\in R\}},\
 1_{\{1\in R\}}-1_{\{4\in R\}},\
 1_{\{2\in R\}}-1_{\{4\in R\}},\
 1_{\{3\in R\}}-1_{\{4\in R\}}),
$$
$$
t_R=(\widehat v_R,u_R)\in\mathbb R^{10}.
$$
十维完整整数 Gram 为
$$
G=\sum_{r=0}^3\nu_rz_Rt_Rt_R^T,\qquad
(\nu_0,\nu_1,\nu_2,\nu_3)=(6,2,2,6).
\tag{3.3}
$$
它的后四个坐标恰为真实低次参数。令
$J=(\operatorname{adj}G)_{\rm top}$ 保前六坐标，则
$$
\boxed{H_2^{-1}=6J/\det G.}
\tag{3.4}
$$
特别不能把 $\widehat v_R$ 换回 $v_R$，也不能在完整逆前压缩。

$A,C$ 的严格正性由双点、单点评价直接得到。
若 $G$ 有核，则 (2.2) 的多项式在全部十五个合法状态为零，
它在唯一非法状态也本来为零。多重仿射唯一性迫全部参数为零，
故 $G>0$。因此全部逆和 Schur 补合法。

定义
$$
\mathscr N=\operatorname{tr}(\operatorname{adj}(A)KJK),\qquad
\mathscr D=\det A\,\Delta^2\det G>0.
$$
由于三个原始缩放全为 $6$，准确有
$$
\boxed{
\operatorname{tr}(H_0^{-1}H_1H_2^{-1}H_1)
=\frac{\mathscr N}{\mathscr D}.
}
\tag{3.5}
$$

## 4. 完整精确整数证书

代码：

[四头三池短块迹证书](../notes/2026-11-13-four-exceptional-weights-three-pool-low-edge-trace-certificate-1cf.mjs)

完整源 blob：
$$
\texttt{8032ffe85e36aefb1731af1a1f7477d47a49b89a}.
$$

脚本直接生成全部十六个头状态及 (3.1)--(3.3)。
行列式和完整伴随通过 Cauchy--Binet 列组展开；
所有常整数小行列式采用 Bareiss 消元，除法逐次检查无余数。
$K$ 还用五列 Schur 展开计算，再另核真正四参数公式。

完整逐项身份包括
$$
A\,\operatorname{adj}A=(\det A)I,\quad
C\,\operatorname{adj}C=(\det C)I,\quad
G\,\operatorname{adj}G=(\det G)I,
$$
$$
K=\Delta S-M\,\operatorname{adj}C\,M^T.
\tag{4.1}
$$
计算保留全部矩阵乘法次序，不以逐变量极小值替代 Schur 补。

精确证书的输出为：

| 对象 | 非零列组数 |
|---|---:|
| $\det A$ | 303 |
| $\operatorname{adj}A$ | 423 |
| $\Delta$ | 940 |
| $K$ 的五列展开 | 2778 |
| $\det G$ | 2068 |
| $\operatorname{adj}G$ | 4630 |

$\mathscr N,\mathscr D$ 有相同的 **21202** 个非零单项式，
系数全部为正整数。对每一个单项式，脚本准确检查
$$
\boxed{9\mathscr D_\alpha-4\mathscr N_\alpha>0.}
\tag{4.2}
$$
其中最小正差为
$$
\boxed{697143656448},
$$
例如出现在指数 $(20,9,8,8)$；头权置换也可能给同值。
最大单变量指数为 $20$，总次数最大为 $67$。
kernel 与 root 分别原样完整运行，均输出 PASS（root 15973 毫秒）；没有浮点符号判断。

base-$32$ 四槽仍在每次乘法前核指数上界。
本处至多二十四个原始状态因子：
分母为 $6+4+4+10$，分子为 $5+5+9+5$。
所以槽间不可能进位；实际最大输入指数和为 $20$。

由 (4.2)，
$$
9\mathscr D(z)-4\mathscr N(z)>0\qquad(z_i>0).
$$
代 (3.5) 得迹严格小于 $9/4$。
将 $H_1H_2^{-1}H_1$ 以 $H_0^{-1/2}$ 作同余，
其最大特征值不超过正矩阵的迹，得到 (1.1) 第一式。

## 5. 倒数权的另一边及完整出生二固定族

[R239 反向对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)
在本处有 $h=3$：
$$
\Gamma_n(a)=Z^{-1}B_s^*\Gamma_{3-n}(a^{-1})B_s,\qquad s=2.
$$
池权全为一，所以 $B_se_I=a_I^2e_I$ 及其逆与 $S_3$ 平均交换，
确实双射两个六维固定 primitive 块。
对倒数头权使用已证低边，再用严格正矩阵的 Schur 等价交换两个邻居，
然后作上述同余，准确得到
$$
H_2H_3^{-1}H_2\prec(9/4)H_1.
$$
归一化迹由相似与迹循环性也保持同一 $9/4$ 界。
源坐标一般非正交；实际 $\Gamma_n$ 的坐标始终是 $H_0^{-1}H_n$。

因此，现在对四异权、任意整数单位池长 $L\ge0$、相对出生二的固定块，
每个合法相邻阶都有统一粗界
$$
\boxed{\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\preceq16\Gamma_{n-1}.}
\tag{5.1}
$$
准确的逐段来源如下：

- $L=0,1$：串长 $h=L$，没有合法相邻阶；源维数在这些短端不假定为六。
- $L=2$：使用 [R239 四异权全高度二稿](R239-appendix-four-exceptional-weights-full-height-two-primitive-gram-bound.md) 的真实六维固定块系数一。
- $L=3$：本文两个相邻阶均严格小于 $9/4$。
- $L\ge4$：任意池长低边稿已付两端系数三，R239 §10.4 对中段逐阶给
  $(1+3/(n-1))(1+3/(L-n-1))\le4L/(L-3)\le16$。

(5.1) 只闭合了这个相对出生二固定族。
其它相对出生、其它池表示及整个 primitive 空间仍须逐块证明；
一般连续尾的统一常数及原边界 $N=M$ 没有随此结论自动完成。
