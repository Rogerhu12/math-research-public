# R150 附录：unit 2+1+1 的 S=0、线性 f 系数零与值碰撞交面完整排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：本附录限定的整个分支已经完整排除。结论不扩展到 S=0 且 f 系数非零的其余分支，也不宣称非零均值层或普通 Hilbert 不变子空间问题已经完成。

## 1. 原范围与需要排除的交面

沿用[原U值完整分层](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)的同一unit 2+1+1 Frobenius代数

$$
\tau(v)=av_0+v_1+bv_B+cv_C,\qquad a=1-b-c,
$$

及同一个原 Gram／$U$ 缩放后的 $p=1$。保留此前已经支付后的非零条件

$$
q(q-1)(q+1)bcP_0\lambda\ne0,\qquad
V=U/U_0=(1,w,h,k),\quad \lambda=m/U_0.
$$

原 moment 是

$$
\tau(V)=\lambda,\quad \tau(V^2)=2\lambda^2,\quad
\tau(V^3)=4\lambda^3.
$$

在原 $E_0=0,N_0=\lambda P_0$ 全局图中，$N(V)$ 对 $f,t$ 仿射。设

$$
S=h+k+1-2\lambda,\qquad
A_f=\frac12\left[3-4\lambda
-(h-1)(k-1)\left(l+\frac{u(q+1-2u)}q\right)\right],
$$

其中 $l=b+c,u=b+cq$。在 $S=0$ 上 $t$ 系数为零，而 $A_f$ 是剩余的 $f$ 系数。

本附录证明：不存在同时满足全部原必要条件及

$$
S=0,\qquad A_f=0,\qquad (h-1)(k-1)(h-k)=0 \tag{1}
$$

的解。全部值碰撞都逐一保留。

## 2. 原 moment 的碰撞参数化

记

$$
A=2\lambda^2-2\lambda+1,\qquad
B=4\lambda^3-6\lambda^2+3\lambda-1.
$$

原 moment 等价于

$$
b(h-1)^2+c(k-1)^2=A,\qquad
b(h-1)^3+c(k-1)^3=B.
$$

任何值碰撞都满足 $AB\ne0$。令

$$
v=\frac{\lambda(2\lambda-1)^2}{A},\qquad
C=\frac{A^3}{B^2},\qquad
w_c=\frac{\lambda^2(1-2\lambda)}B.
$$

完整碰撞图为：

- $h=1$: $k=v,c=C,w=w_c$，$b$ 自由；
- $k=1$: $h=v,b=C,w=w_c$，$c$ 自由；
- $h=k\ne1$: $h=k=v,b+c=C,w=w_c$。

$h=k=1$ 会要求 $A=B=0$，而 $B=(2\lambda-1)A-\lambda$ 与 $A(0)=1$ 排除这种可能。

在前两图上

$$
S=\frac{4\lambda^2-5\lambda+2}{A},
$$

在第三图上

$$
S=\frac{(2\lambda-1)(2\lambda^2-1)}A. \tag{2}
$$

## 3. 恰一值等于 1 的两图

在 $h=1$ 或 $k=1$ 上，$(h-1)(k-1)=0$，所以

$$
A_f=(3-4\lambda)/2.
$$

若还满足 $S=0$，则由 (2) 有 $4\lambda^2-5\lambda+2=0$。该二次式在 $\lambda=3/4$ 的值为 $1/2$，故不能有 $A_f=0$。两图完整排除，无任何新除数或单独未支付纤维。

## 4. h=k 且 lambda=1/2

(2) 的第一纤维给

$$
\lambda=\tfrac12,\qquad h=k=w=0,\qquad l=\tfrac12.
$$

此时原 S 恒等式直接给

$$
N(V)=A_1/4.
$$

由 $A_f=0$，

$$
u(q+1-2u)=q/2.
$$

因此原 $V_2=b+cq^2=(q+1)u-ql$ 满足 $V_2=2u^2$。全局原 $E_0/N_0$ 图的表达式为

$$
A_1=
2\left(1-l-\frac{u(q+1-2u)}q\right)f+
\frac{(2u-q-1)(V_2-2u^2)+4\lambda P_0}{q}.
$$

前面的 $f$ 系数及第一常数项都为零，所以

$$
A_1=2P_0/q,\qquad N(V)=P_0/(2q)\ne0.
$$

与原 $N(V)=0$ 矛盾。这里明确用了已知非零的 $q,P_0$，未通过删除分母零纤维取得结论。

## 5. h=k 且 2lambda^2=1 的全部权重与 q

只剩 (2) 的第二纤维。模 $2\lambda^2-1$，原 moment 精确给

$$
h=k=\lambda-\tfrac12,\qquad
l=\frac{8(5+\lambda)}{49},\qquad
w=\frac{3\lambda+1}{7}. \tag{3}
$$

设 $z=(h-1)^2$。在 $S=0,A_f=0$ 下，原 $N(V)$ 常数式化为

$$
\frac{11\lambda-6}{2}u+(1-2\lambda)(q+1)=0. \tag{4}
$$

这是原 $N(V)=0$ 在原 $E_0/N_0$ 图上的必要式，并未替换成别的范数条件。$11\lambda-6\ne0$，且在此二次数域

$$
\frac{2(2\lambda-1)}{11\lambda-6}=\frac l2.
$$

故 (4) 给 $u=l(q+1)/2$。由 $u=b+cq,l=b+c$ 及 $q\ne1$，

$$
b=c=l/2=\frac{4(5+\lambda)}{49}. \tag{5}
$$

再将 (5) 代回原 $A_f=0$，精确得到

$$
(13-17\lambda)q^2+(64\lambda-23)q+(13-17\lambda)=0. \tag{6}
$$

$13-17\lambda\ne0$，所以这里没有丢失一次或常数的降次纤维。判别式为

$$
(64\lambda-23)^2-4(13-17\lambda)^2
=147(1-4\lambda)^2.
$$

因此四个系数纤维完整由数域

$$
K=\mathbb Q(\sqrt2,\sqrt3)
$$

的四个嵌入涵盖：取

$$
\lambda=\sqrt2/2,\qquad
q=\frac{23-64\lambda+7\sqrt3(1-4\lambda)}{2(13-17\lambda)},
$$

另外三个嵌入独立改变两个平方根的符号。不能只取任意一个 q 根而忽略其余根；本方法使用整个四次数域，完整保留所有共轭。实际源检查了数域次数为 4，并精确验证 $bcq(q-1)(q+1)uP_0\ne0$。数域中的非零元素在每个嵌入下仍非零。

## 6. 原九式在 K[f,t] 中的精确单位理想

在 (3)--(6) 的系数数域中，仍从同一个原 Frobenius 运算重建

$$
K_{\mathrm{active}}=
\begin{pmatrix}
0&0&1&q\\
0&A_1&r&s\\
1&r&0&t\\
q&s&t&0
\end{pmatrix}.
$$

用原 $E_0=0,N_0=\lambda P_0$ 图表达 $A_1,r,s$ 后，原 $f=\tau(d)/2$、原 $P(V)=N(V)=0$ 都实际核为零。然后完整保留以下九条原多项式：

$$
E_1,\ E_B,\ E_C,
$$

$$
P_1-3wP_0,\quad P_B-h^3P_0,\quad P_C-k^3P_0,
$$

$$
N_1-2\lambda wP_0,\quad N_B-\lambda h^2P_0,\quad N_C-\lambda k^2P_0.
$$

$P_1,N_1$ 始终是原双点一阶 germ 系数；源码使用真正的极化/导数公式生成，没有把第二行视为新的简单点。

实际输入规模如下：

| 原式 | f,t 的分别次数 | 项数 |
|---|---:|---:|
| $E_1,E_B,E_C$ | $(2,2)$ | 各 6 |
| $P_1-3wP_0$ | $(1,1)$ | 3 |
| $P_B-h^3P_0,P_C-k^3P_0$ | $(3,3)$ | 各 10 |
| $N_1-2\lambda wP_0$ | $(2,2)$ | 6 |
| $N_B-\lambda h^2P_0,N_C-\lambda k^2P_0$ | $(3,3)$ | 各 10 |

在 $K[f,t]$ 上以 grevlex 次序、精确 F5b 算法计算的约化 Gröbner 基为 $\{1\}$。因此四个嵌入下都没有满足这些必要条件的复数解。这个负面结论足以排除原物理解，不需要、也没有声称这些抽象必要方程充分刻画物理几何。

结合第 3、4 节，整个 (1) 分支已排除。

## 7. 实际执行、失败修复与源身份

[成功源码](../notes/2026-11-26-unit211-U-value-S0-collision-347c.py)和[实际小回执](../notes/2026-11-26-unit211-U-value-S0-collision-completed-execution-347c.json)保留本次完整执行。

冻结 blob：849653c3b99fa90d0f84f4d251cf2f917ac18b9b。源码 SHA256：9e843f0cad6ae672258021d650ff68e72e914405fc1848ca41de5f6d1f3d5bab；4629 bytes。依赖 Python 3.12、SymPy 1.14.0。

成功执行为公开 Actions run 45803350694 / job 139852028594，冻结源提交 31ec7ed7c882830bd16e320a111f93f8ef161c67。源内计时 3.961885 秒、峰值 RSS 80708 KiB；驱动计时 4.277630321 秒，退出码 0。原九式输入 SHA256 为 59c1d30d305e4238e2d4a8e912c8519a5cfb630d0421cbc3f202ca9db15d084a；stdout SHA256 为 2cc4e7f2a4f3ff7c3da9d5d45ebb52f7a1b739440239285392dbcd68f95d2e8a。最终状态为 exact_original_fiber_excluded，最终基恰为一个零次、一项多项式。

历史上两个执行失败分别是 SymPy ANP 与 Python 0 的结构相等判断，以及 Python int / ANP 的反向除法接口不支持。修复仅使用精确差值判零和 K.one / ANP，未修改任何原方程、q 共轭或参数图。它们各自保留失败回执，不能作为数学排除的证据；本结论只依据上面的完整成功执行。

本job的结果与U值图短恒等式job分别登记；源、输入及stdout身份均在上述回执内。非零均值整层与普通 ISP 的完成状态不由本分支排除自动改变。
