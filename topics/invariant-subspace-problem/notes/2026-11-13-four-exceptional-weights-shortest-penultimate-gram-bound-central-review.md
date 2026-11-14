# 四个异常权最短倒数第二出生块的精确相邻界

日期：2026-11-13  
作者：AI 协作研究，central_review  
状态：已证明；root 已独立全文核验并执行完整 BigInt 证书，全部 2156 个系数矩阵及 32340 个主子式通过。

## 1. 准确范围

考虑四个任意正头权 a_1,…,a_4，加四个单位权弱池位。令
$$
D=\sum_{i=1}^4a_iE_i+D_{\mathrm w},\qquad
s=3,\qquad h=8-2s=2.
$$
只取弱池置换固定的 primitive 块，维数为四。本文没有将这个固定块当作整个八位 K_3。

在完整源孔层上先取
$$
F_n=\frac{D^n(D^*)^n}{(n!)^2}
$$
的逆，再压到该 primitive 块，得到真正的 Γ_n。这里只有相邻阶 n=1。

**定理。** 对任意四个正头权，
$$
\boxed{\Gamma_1\Gamma_2^{-1}\Gamma_1<\frac45\Gamma_0.}
\tag{1.1}
$$
这里 Γ_0=I，严格性指算子差正定。系数 4/5 是 s=3、n=1 的出生因子 (s+n)/(s+n+1)；本文没有附加已被一般反例排除的有限 N 因子。

这个 h=2 边段不落入任意 q 方差法要求的 q=4、h≥12 中段窗口。下面直接处理该真正四维源及完整 inverse Gram，不使用全函数扩张的负方向来判断原不等式。

## 2. 三个真实 Gram 的完整有限式

用[一般头一参数完整 MP 公式](../results/R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)的坐标 x_i=f_i/a_i。置
$$
z_i=a_i^2>0,\qquad z_R=\prod_{i\in R}z_i,
\qquad b_R=(1_{i\in R})_{i=1}^4,\qquad {\bf1}=(1,1,1,1)^T.
$$
实际源为
$$
g(x)=\sum_{\varnothing\ne R\subseteq[4]}
(-1)^{|R|-1}
\frac{a_R}{\binom4{|R|-1}}\,(b_R^Tx)\,
e_{[4]\setminus R}w_{|R|-1}.
\tag{2.1}
$$
令 H_n 为此源的全空间 MP 平方范数 Gram。引用的有限差分与置换平均已支付其确为完整最小值，而非某个试探逆或先压缩的逆。其三个准确式为
$$
H_0=\sum_{R\ne\varnothing}
\frac{z_R}{\binom4{|R|-1}}\,b_Rb_R^T,
\tag{2.2}
$$
$$
H_1=\sum_R\frac{z_R}{\binom4{|R|}}\,b_Rb_R^T
-\frac{\left(\sum_R z_Rb_R/\binom4{|R|}\right)
\left(\sum_R z_Rb_R/\binom4{|R|}\right)^T}
{\sum_R z_R/\binom4{|R|}},
\tag{2.3}
$$
$$
H_2=\sum_{R\ne[4]}
\frac{z_R}{\binom4{|R|+1}}\,
({\bf1}-b_R)({\bf1}-b_R)^T.
\tag{2.4}
$$
H_0 的自由常数被原零阶约束固定为零；H_2 的常数被最高阶约束固定为 b_[4]^Tx。因此 (2.2)、(2.4) 没有丢掉端点最小化条件。

## 3. 清分母后的完整矩阵多项式

以下全部矩阵均为 z_1,…,z_4 的整系数多项式。按 r=|R| 定义三个整数权表：
$$
\begin{array}{c|ccccc}
r&0&1&2&3&4\\ \hline
u_r&0&12&3&2&3\\
v_r&12&3&2&3&12\\
w_r&3&2&3&12&0
\end{array}
$$
置
$$
\mathsf A=\sum_Ru_rz_Rb_Rb_R^T=12H_0,
$$
$$
\mathsf B=\sum_Rw_rz_R({\bf1}-b_R)({\bf1}-b_R)^T=12H_2,
$$
$$
Z=\sum_Rv_rz_R,\qquad
m=\sum_Rv_rz_Rb_R,\qquad
S=\sum_Rv_rz_Rb_Rb_R^T,\qquad
K=ZS-mm^T.
\tag{3.1}
$$
于是
$$
H_1=\frac{K}{12Z}.
$$
Z>0；𝔄 含四个单点正对角项，𝔅 含四个三点补集正对角项，所以二者严格正定，特别 det𝔅>0。

定义
$$
\boxed{
\mathcal P(z)=
4Z^2\det(\mathsf B)\,\mathsf A
-5K\,\operatorname{adj}(\mathsf B)\,K.
}
\tag{3.2}
$$
准确清分母恒等式为
$$
\boxed{
\frac45H_0-H_1H_2^{-1}H_1
=\frac{\mathcal P(z)}{60Z^2\det(\mathsf B)}.
}
\tag{3.3}
$$
这里保留 K、adj𝔅、K 的矩阵乘法次序，不按标量比替代非交换乘积。

## 4. 完整整系数证书

独立可执行的完整证书见：

[四头最短块 BigInt 证书](../notes/2026-11-13-four-exceptional-weights-shortest-penultimate-gram-certificate-central-review.mjs)

其源 blob 为
$$
\texttt{efe5393171cec712e213d70dccde0c0cc057b529}.
$$
脚本只由 (3.1)—(3.2) 的十六个状态构造全部多项式，再作整系数加法、乘法、行列式及主子式。没有使用数值采样、浮点特征值、外部符号软件或预先列入的待证正系数表。

将完整矩阵多项式展开为
$$
\mathcal P(z)=\sum_{\alpha\in\mathbb N^4} C_\alpha z^\alpha.
$$
执行结果准确为：

- 共有 2156 个非零系数矩阵 C_α，全部是对称四乘四整数矩阵。
- 对每个 C_α 检查全部 15 个非空主子式，共 32340 项；全部非负。
- 秩为一、二、三、四的系数矩阵个数依次为 77、356、598、1125。
- 最终单变量最高次数为 6，总次数最高为 24。
- 脚本另逐多项式项核对 𝔅 adj𝔅=(det𝔅)I 及 𝒫 的对称性。

对实对称矩阵，全部主子式非负等价于半正定，所以这逐一证明 C_α≽0。所有 z_i>0 时，各单项式均非负，遂有 𝒫(z)≽0。

单项式编码也在每次乘法前付清：四个指数放在独立的 base-32 位，代码计算输入多项式各指数上界，并要求相加不超过 7。所有乘法由至多七个原始多重仿射因子生成，因此指数槽之间不可能进位；实际执行最大输入指数和为 6。行列式及主子式系数全部为 BigInt，无截断或溢出。完整验证只需固定有限循环，脚本中的计数断言使漏项或更改不能静默通过。

## 5. 严格锚与算子坐标

四次单项式 z_1z_2z_3z_4 的系数准确为
$$
C_{1111}=
\begin{pmatrix}
165888&77760&77760&77760\\
77760&165888&77760&77760\\
77760&77760&165888&77760\\
77760&77760&77760&165888
\end{pmatrix}.
\tag{5.1}
$$
其常数方向特征值为 399168，正交三维方向特征值为 88128，均严格为正。因此
$$
\mathcal P(z)\succeq z_1z_2z_3z_4\,C_{1111}>0.
\tag{5.2}
$$
(3.3) 给出严格
$$
H_1H_2^{-1}H_1<\frac45H_0.
$$

最后，源基一般不正交。真正 Γ_n 的坐标为 H_0^{-1}H_n，故 Γ_1Γ_2^{-1}Γ_1 的坐标准确为
$$
H_0^{-1}H_1H_2^{-1}H_1.
$$
以源 Gram H_0 比较，正好得到 (1.1)。这一合同没有改变全层逆后压缩的次序。

本结果只关闭四头、四位等权池、相对出生三的四维固定块及其唯一相邻阶。其他弱池表示、其他出生、更多池位的早期阶数、任意全权尾和 ISP 主问题，仍需各自的完整证明。
