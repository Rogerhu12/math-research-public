# R239 附录：两组任意重数加一异常位的全高度二维最小逆与高度二严格比较

- 日期：2026-11-13。
- 作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。
- 状态：全高度二维 MP / shear 恒等式及整个高度二 primitive 空间的严格系数 1 已证明。一般更高高度的二维比较尚不由本稿证明；普通 ISP 未完成。
- 主要输入：[完整任意出生与短池 MP](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md) §§10–11；[两组全高度严格比较](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md)；[任意头饱和固定线](R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md) §8；[饱和双侧常数](R239-appendix-saturated-primitive-two-sided-weight-count-constants.md)。
- 精确证书：[完整整数证书](../notes/2026-11-13-two-weight-groups-one-exceptional-height-two-certificate-0c.mjs)；独立物理满层有理核验：[完整物理核验](../notes/2026-11-13-two-weight-groups-one-exceptional-full-mp-check-0c.py)。前者的有限 Newton 表是全参数证明，后者只作公式的独立核验。

## 1. 模型、完整逆与全部 primitive 分支

取两个等权组及一个单独位。对两个等权组分别作标准正交升降串分解，得到短串长度 $q$、长串长度 $L\ge q$ 及一条长度一的异常串。归一化长串的权为一，短串权为 $a>0$、异常权为 $c>0$，写
$$
z=a^2>0,\qquad w=c^2>0.
$$
组内正交串同时约化 $D,D^*$、完整层 Gram、完整逆和 primitive 压缩。所有组内出生与重数均保留。以下先在一个三串张量块中工作。

相对出生为 $t$，高度为
$$
h=q+L+1-2t.
$$
从两串 Clebsch–Gordan 分解再张量长度一的串，或直接计算相邻层维数之差，primitive 分支准确为：$t=0$ 时一维；$1\le t\le q$ 时二维；若 $L\ge q+1$，$t=q+1$ 时一维；其余低半部出生无新 primitive。当 $q=0$ 时直接退化到两权模型。

二维分支写成
$$
t=q-\delta,\qquad L=q+h-1-2\delta,
\qquad 0\le\delta\le q-1,\qquad h\ge2\delta+1.
\tag{1.1}
$$
本稿比较只考虑 $h\ge2$。始终先在整个出生层取逆：
$$
F_n=\frac{D^n(D^*)^n|_{\mathcal H_t}}{(n!)^2},\qquad
\Gamma_n=P_{K_t}F_n^{-1}|_{K_t},\qquad 0\le n\le h.
\tag{1.2}
$$
若 $E:\mathbb C^2\to K_t$ 是下面固定的源映射，记
$$
H_n=E^*F_n^{-1}E.
$$
$H_0=E^*E$ 是真实源 Gram，并非预设单位矩阵。所需算子比较准确等价于
$$
H_nH_{n+1}^{-1}H_n\prec H_{n-1};
\tag{1.3}
$$
对所有矩阵同时用 $H_0^{-1/2}$ 合同便得到原 primitive Hilbert 坐标。

## 2. 两个多项式通道的真正全 MP

把短串各位和异常位看成 $q+1$ 个头，长串看成单位池。$r$ 表示缺失的普通头数，$y\in\{0,1\}$ 表示异常头是否缺失。最高齐次多重仿射源在组内平均后恰为
$$
f(r,y)=x\binom r{\delta+1}+\eta y\binom r\delta.
$$
采用首一坐标
$$
\alpha=\frac{x}{(\delta+1)!},\qquad \beta=\frac\eta{\delta!}.
\tag{2.1}
$$
两个多项式通道写为
$$
F_0(r)=x\binom r{\delta+1}+P_0(r),\qquad
F_1(r)=F_0(r)+\eta\binom r\delta+P_1(r),
\tag{2.2}
$$
其中 $\deg P_0\le\delta$、$\deg P_1\le\delta-1$。等价地，两者都有固定最高系数 $\alpha$，次高系数之差固定为 $\beta$，其余低次系数独立自由。

准确的最小范数是
$$
\boxed{
H_n[\alpha,\beta]
=\min_{F_0,F_1}\sum_r
\left(\omega_n^0(r)|F_0(r)|^2+w\omega_n^1(r)|F_1(r)|^2\right),
}
\tag{2.3}
$$
$$
\omega_n^0(r)=\frac{\binom qr z^r}{\binom L{n+r-\delta-1}},\qquad
\omega_n^1(r)=\frac{\binom qr z^r}{\binom L{n+r-\delta}}.
\tag{2.4}
$$
求和只取合法池占据；同时强制对应 $F_i$ 在所有非法 $r\in\{0,\ldots,q\}$ 上为零。

这里使用已证明的任意出生、任意短池 MP 引理，其参数为头数 $q+1$、缺失次数 $\delta+1$。其最高源约束自动满足，因为 $L\ge q$ 且 $\delta+1\ge1$。该引理逐集合的有限差分证明保留所有低次多重仿射参数，并用完整满射和维数计数证明穷尽性。再对普通头置换正交平均，低次参数准确变成 (2.2)。因此 (2.3) 是完整 Hilbert 最小逆，不是限制原像得到的试探上界。池固定及普通头固定的唯一最小解必固定，故平均没有遗失较低能量的非固定原像。

## 3. 任意高度、含两端的准确 shear 公式

考虑同一 $q,L,z$ 的两个旧两串问题：

- 旧相对出生 $t-1$、缺失次数 $\delta+1$、高度 $h+1$，未归一费用记为 $v_j$，$0\le j\le h+1$。
- 旧相对出生 $t$、缺失次数 $\delta$、高度 $h-1$，未归一费用记为 $u_j$，$0\le j\le h-1$。

将旧源最高二项式系数改为首一，记
$$
a_j=(\delta+1)!^2v_j,\qquad b_j=\delta!^2u_j.
\tag{3.1}
$$
令 $P_j(r)$ 为权 $\omega_j^0$ 下带全部强制根的首一 $\delta+1$ 次最小多项式，$\mathfrak b_j$ 为其 $r^\delta$ 系数，置
$$
k_n=\mathfrak b_{n+1}-\mathfrak b_n.
\tag{3.2}
$$
那么全部 $0\le n\le h$ 上，
$$
\boxed{
H_n[\alpha,\beta]=A_n|\alpha|^2+B_n|\beta-k_n\alpha|^2,
\quad
A_n=a_n+w a_{n+1}.
}
\tag{3.3}
$$
内部及两个端点准确为
$$
\boxed{
B_n=\frac{w b_{n-1}b_n}{b_{n-1}+w b_n}\quad(1\le n<h),
\qquad B_0=w b_0,\qquad B_h=b_{h-1}.
}
\tag{3.4}
$$
所以
$$
H_n=\begin{pmatrix}
A_n+B_nk_n^2&-B_nk_n\\
-B_nk_n&B_n
\end{pmatrix}.
\tag{3.5}
$$

**证明。** 在第零通道，先去掉所有低于次高项的自由系数。由于 $P_n$ 与全部允许低次多项式正交，剩余费用准确是
$$
a_n|\alpha|^2+b_{n-1}|c_0|^2,
$$
其中次高系数为 $\alpha\mathfrak b_n+c_0$。第一个通道同样为
$$
w a_{n+1}|\alpha|^2+w b_n|c_1|^2.
$$
这里需要核对边段而非只看全支撑内部：旧高次问题 $a_j$ 的强制低、高根数为
$$
u=(\delta+1-j)_+,\qquad v=(\delta-h+j)_+.
$$
旧低次问题 $b_{j-1}$ 有完全相同的强制根。两者去根后的剩余次数恰相差一。因此低次自由向量的最小范数正是 $b_{j-1}$，没有不同权或不同端点的偷换。

两个通道的次高系数差约束是
$$
c_1-c_0=\beta-k_n\alpha.
$$
对 $c_0$ 作标量二次最小化即给 (3.4)。$n=0$ 时第零通道的全部根已固定次数，准确强制 $c_0=0$；$n=h$ 时第一通道同理强制 $c_1=0$，得到所列端点。可把 $b_{-1}=b_h=+\infty$ 仅作为这两个硬约束的简写，但不把无穷数当成实际 Gram。证毕。

## 4. 同一个矩形 Schur 多项式控制 shear 和曲率

令 $\theta=\log z$，撇号表示 $d/d\theta$，并置
$$
S_j(z)=s_{(t^{\delta+1})}(z^{[j]},1^{[h+1-j]}),
\qquad f_j=\log S_j,\qquad 0\le j\le h+1.
\tag{4.1}
$$
则
$$
\boxed{
\mathfrak b_j=-\frac{\delta(\delta+1)}2-f_j',\qquad
k_n=-(f_{n+1}'-f_n').
}
\tag{4.2}
$$
另外，对 $1\le j\le h$，
$$
\boxed{f_j''=\frac{a_j}{b_{j-1}}.}
\tag{4.3}
$$
$f_0''=f_{h+1}''=0$。

**证明。** 对有限正权 $z^x\rho(x)$，首一 $d$ 次正交多项式的次高系数是 $-\partial_\theta\log Z_d$，其中 $Z_d$ 为 $d\times d$ Hankel 行列式。可由 Heine 的 Vandermonde 平方公式展开首项得到：次高系数是粒子坐标和的负期望，正好是对数导数。其 Hankel 恒等式又给
$$
(\log Z_d)''=Z_{d-1}Z_{d+1}/Z_d^2=\mathfrak h_d/\mathfrak h_{d-1}.
$$
这可直接对 Gram 行列式作 Jacobi 恒等式；所有行列式严格正。

对 $a_j$，置 $d_0=\delta+1$、$u=(d_0-j)_+$、$v=(d_0-h-1+j)_+$、$d=d_0-u-v$。先除强制根，再平移 $x=r-u$。原强制根之和为
$$
R_0=\frac{u(u-1)}2+\frac{v(2q-v+1)}2.
$$
所以
$$
\mathfrak b_j=-R_0-du-\partial_\theta\log Z_d.
$$
旧全高度 Schur 公式把 $Z_d$ 写成常数乘 $z^{d(d-1)/2}$ 与一个矩形 Schur。低端和中段的秩对偶直接给 $S_j$；高端的补变量和秩对偶再给因子 $z^{-tv}$。分别核算都满足
$$
R_0+du+d(d-1)/2-tv\,\mathbf1_{v>0}=d_0(d_0-1)/2,
$$
得到 (4.2)。这些额外因子对二阶对数导数均无贡献。同一通道的高、低多项式共用强制根，Hankel 商比正是 $a_j/b_{j-1}$，所以得到 (4.3)。在 $j=0,h+1$ 剩余次数为零，且 $S_0$ 常数、$S_{h+1}$ 为常数乘 $z^{t(\delta+1)}$，曲率为零。

## 5. 一般二维比较的准确费用

同时剪切源坐标，使固定中阶 $k_n$ 变为零。记
$$
d_-=k_{n-1}-k_n,\qquad d_+=k_{n+1}-k_n,
$$
并用下标 $-,0,+$ 表示 $n-1,n,n+1$。真正的 Schur 差
$$
K=H_{n-1}-H_nH_{n+1}^{-1}H_n
$$
准确有
$$
K_{11}=A_- -A_0^2/A_+ +B_-d_-^2,
$$
$$
K_{12}=-B_-d_- -A_0B_0d_+/A_+,
$$
$$
K_{22}=B_- -B_0^2/B_+ -B_0^2d_+^2/A_+.
\tag{5.1}
$$
旧两串严格比较使 $a_j$ 严格 log 凸，因而正线性和 $A_n=a_n+w a_{n+1}$ 仍严格 log 凸。于是 $K_{11}>0$ 已付；全部剩余二维费用准确是 $\det K>0$，不能忽略 shear。

$B_n$ 本身也 log 凸。内部令 $r_n=b_n/b_{n-1}$，旧比较使 $r_n$ 单增；直接代入 (3.4) 给
$$
B_n/B_{n-1}\le r_n\le B_{n+1}/B_n.
$$
端点直接用 (3.4) 核验。这只支付标量对角部分，不能单凭两个标量结论推出整个矩阵序。

若 $u_j=2f_j-f_{j-1}-f_{j+1}$，则 (4.2) 给
$$
d_-=-u_n',\qquad d_+=u_{n+1}'.
\tag{5.2}
$$
Suvrit Sra (2026), *Monotonicity of Turán-ratios of symmetric polynomials*, Lemma 2.2 / Theorem 1.1，pp. 3–4 的单矩形导数单调性给 $d_-d_+\le0$；[同一实际四次式及自足短证](../notes/2026-11-13-three-weight-interior-quartic-shear-and-rational-evidence-0c.md)保留署名和完整负部和最大原理。但这个符号不能独立支付两个平方项及四次项。因此本稿不把一般高度的完整比较宣称为已证。

## 6. 高度二的全部二维块

在 $q\le L$ 下，高度二的二维条件 (1.1) 强制
$$
\delta=0,\qquad t=q,\qquad L=q+1,\qquad q\ge1.
\tag{6.1}
$$
置 $Q=q+1$、$\Theta=z\partial_z$，并定义四个有限正系数多项式
$$
L_0(z)=\sum_{r=0}^q(Q-r)z^r,\qquad
R_0(z)=\sum_{r=0}^q(r+1)z^r,
$$
$$
A(z)=\sum_{r=0}^q r(Q-r)(Q+1-r)z^r,
$$
$$
C(z)=\sum_{r=0}^q(q-r)(r+1)(r+2)z^r.
\tag{6.2}
$$
下文简写 $L=L_0(z),R=R_0(z)$，不会再以此 $L$ 表示池长。令
$$
T_L=L\Theta^2L-(\Theta L)^2,\qquad
T_R=R\Theta^2R-(\Theta R)^2,
$$
$$
M=L\Theta^2R+R\Theta^2L-2\Theta L\Theta R,
\quad J=L\Theta R-R\Theta L,
\quad Z=L+wR.
\tag{6.3}
$$
由完整公式 (3.3) 直接得到
$$
H_0=U/Q,\qquad H_1=B/(QZ),\qquad H_2=V/Q,
\tag{6.4}
$$
其中
$$
U=\begin{pmatrix}A+w\Theta^2L&w\Theta L\\w\Theta L&wL\end{pmatrix},
$$
$$
V=\begin{pmatrix}(\Theta-q)^2R+wC&(q-\Theta)R\\(q-\Theta)R&R\end{pmatrix},
$$
$$
B=\begin{pmatrix}T_L+wM+w^2T_R&wJ\\wJ&wLR\end{pmatrix}.
\tag{6.5}
$$
例如旧首一范数准确为
$$
a_0=A/Q,\quad a_1=T_L/(QL),\quad a_2=T_R/(QR),\quad a_3=C/Q,
\quad b_0=L/Q,\quad b_1=R/Q.
$$
旧首一次多项式的次高系数依次为 $0,-\Theta\log L,-\Theta\log R,-q$，这也逐项恢复 (6.5)，包括真实两个端点。

## 7. 一个完整四次行列式及全参数正系数定理

恒等式
$$
\det U=wAL+w^2T_L,\qquad \det V=T_R+wCR,
$$
$$
LRM-J^2=R^2T_L+L^2T_R,\qquad
\det B=wZ(RT_L+wLT_R)
\tag{7.1}
$$
均由二乘二展开得到。置
$$
P_q(z,w)=\det\begin{pmatrix}ZU&B\\B&ZV\end{pmatrix}.
$$
对任意二乘二矩阵的块行列式展开给
$$
P_q=Z^4\det U\det V+(\det B)^2
-Z^2\operatorname{tr}(\operatorname{adj}U\,B\,\operatorname{adj}V\,B).
$$
因此 $P_q=wZ^2R_q$，其中四次多项式准确为
$$
\boxed{
R_q=Z^2(AL+wT_L)(T_R+wCR)
+w(RT_L+wLT_R)^2
-\frac1w\operatorname{tr}(\operatorname{adj}U\,B\,\operatorname{adj}V\,B).
}
\tag{7.2}
$$
最后的迹常数项为零，故除 $w$ 是多项式精确相除。写
$$
R_q(z,w)=\sum_{i=0}^4 w^i R_{q,i}(z).
$$

**全参数系数命题。** 对每个整数 $q\ge1$，$R_{q,i}$ 的全部 $z$ 系数非负；并且
$$
[w^4z]R_q=2q^2(q+1)>0.
\tag{7.3}
$$
所以全部 $z,w>0$ 有 $R_q(z,w)>0$。

以下给可复现的有限精确代数证明，而非有限 $q$ 数值试验。用
$$
W=\frac{1-z^Q}{1-z},\quad
L=(Q-\Theta)W,\quad R=(1+\Theta)W,
$$
$$
A=\Theta(Q-\Theta)(Q+1-\Theta)W,
\quad C=(Q-1-\Theta)(1+\Theta)(2+\Theta)W
\tag{7.4}
$$
在 (7.2) 中作完全整数的稀疏运算。每一系数得到
$$
R_{q,i}(z)=\frac{\sum_{\lambda,s}p_{i,\lambda,s}(Q)z^{\lambda Q+s}}{(1-z)^{16}},
\qquad p_{i,\lambda,s}\in\mathbb Z[Q],\qquad 0\le s\le15.
\tag{7.5}
$$
证书中的 `make` 从 (7.4) 和二乘二矩阵运算原样构造这些分子，未插入猜出的系数。分子 $Q$ 次数依次为 $8,9,10,9,8$；故下文分区系数的先验总次数依次为
$$
D_i=23,24,25,24,23.
\tag{7.6}
$$

先给覆盖所有 $q$ 的次数证明：$L,R,A$ 的次数至多为 $q$，$C$ 至多为 $q-1$；最高项相消使 $T_L,T_R,M,J$ 至多为 $2q-1$。在 $V$ 中，除 $V_{22}=R$ 外其余项都至多 $q-1$。于是 (7.2) 的前两项次数分别至多 $6q-1,6q-2$。迹项中，若两个 $B$ 因子都取次数 $2q$ 的 $B_{22}$，对应的 $\operatorname{adj}V$ 元素只能是 $V_{11}$，次数至多 $q-1$；否则至少一个 $B$ 因子次数至多 $2q-1$。故迹项也至多 $6q-1$。除 $w$ 不改变 $z$ 次数，这证明 $\deg_z R_{q,i}\le6q-1$，独立于任何有限参数核验。

因此仅需六个分区
$$
k=jQ+u,\qquad 0\le j\le5,\quad 0\le u<Q.
$$
置 $v=Q-u-1\ge0$，即 $Q=u+v+1$。对每个固定 $i,j$，系数 $[z^k]R_{q,i}$ 是以下关于非负整数 $u,v$ 的多项式：
$$
C_{i,j}(u,v)=\sum_{\lambda\le j,s}
 p_{i,\lambda,s}(u+v+1)
 \binom{(j-\lambda)(u+v+1)+u-s+15}{15}.
\tag{7.7}
$$
若 $\lambda>j$，因 $s\ge0$ 且 $u<Q$，原幂级数系数为零。若 $\lambda\le j$，二项式上标至少 $15-s\ge0$；低于 15 时它作为次数 15 的二项式多项式正好取零。因此 (7.7) 在整个第一象限都是合法多项式，无需分段延拓。由 (7.5) 预先得到总次数界 (7.6)。六区覆盖实际全部非零 $z$ 系数；$q\ge1$ 对应 $Q\ge2$，而证书甚至包含冗余退化点 $Q=1$。

对已知次数上界 $D_i$ 的多项式，Newton 展开恒等为
$$
C_{i,j}(u,v)=\sum_{a=0}^{D_i}\sum_{b=0}^{D_i}
 (\Delta_u^a\Delta_v^b C_{i,j})(0,0)
 \binom ua\binom vb.
\tag{7.8}
$$
故精确检查 $(D_i+1)^2$ 网格的前向差分，就证明所有非负整数 $u,v$ 的系数非负。程序仅用 BigInt，逐项断言所有 Newton 系数非负。各行按 $j=0,\ldots,5$ 的严格正系数数目为

| $i$ | 先验次数 | 六区的正 Newton 系数数目 |
|---|---:|---|
| 0 | 23 | 69, 135, 135, 133, 127, 34 |
| 1 | 24 | 84, 135, 135, 133, 127, 40 |
| 2 | 25 | 75, 135, 135, 133, 127, 45 |
| 3 | 24 | 65, 135, 135, 133, 127, 49 |
| 4 | 23 | 54, 135, 134, 132, 124, 39 |

总计 3199 个严格正系数，其余为零。程序也直接提取 $i=4,k=1$ 的符号系数，准确为 $2Q(Q-1)^2$，证明 (7.3)。这是正性证明所需的全部有限运算。

为独立核对稀疏有理生成的实现，程序还对 $q=1,2,3,7$ 从 (6.2) 的有限多项式直接作稠密整数运算，核对每个 $i$ 的完整恒等式
$$
(1-z)^{16}R_{q,i}(z)=\sum_{\lambda,s}p_{i,\lambda,s}(Q)z^{\lambda Q+s}.
$$
这些独立检查不承担从有限 $q$ 推到全 $q$ 的职责；全 $q$ 结论由先验次数、完整分区和 (7.8) 支付。

## 8. 严格矩阵比较及整个 primitive 空间

真实四乘四块为
$$
\begin{pmatrix}H_0&H_1\\H_1&H_2\end{pmatrix}
=\frac1{QZ}\begin{pmatrix}ZU&B\\B&ZV\end{pmatrix}.
$$
所以其行列式与 $R_q$ 同号，全部正权时严格为正。$H_2$ 是严格正的真实 MP Gram；于是 $\det K>0$，其中 $K=H_0-H_1H_2^{-1}H_1$。§5 已给 $K_{11}>0$，故整个二维 Hermitian 矩阵 $K$ 严格正定。这证明任意 $q\ge1,z,w>0$ 的完整高度二二维分支满足 (1.3)。

现回到任意两个等权组加一个异常位的整个高度二 $K_s$。逐组正交串全部保留；每个二维分支由 (6.1) 归入刚证明的 $q,q+1,1$ 情形。其余一维分支分别如下。

- 相对真空 $t=0$：高度二意味着剩余总位数为二，普通标量 Newton 或已证两权结论支付严格系数小于一。
- $q=0$：退化成一个共同权组与一个异常位，直接使用已证两权全高度严格结论。
- 最高出生 $t=q+1$：高度二强制长串长度为 $q+3$。这是 $q$ 个共同权头与一个任意异常权头加单位池的饱和固定线，准确由已证任意头饱和正矩及双侧常数支付严格相邻系数小于一。这里仍可能有三个不同权，不能把它误称为两权分支。

因此所有非零分支严格成立，有限正交直和后得到整个 $K_s$ 上
$$
\boxed{\Gamma_1\Gamma_2^{-1}\Gamma_1\prec\Gamma_0=I.}
\tag{8.1}
$$
没有丢弃不在对称子空间的 primitive、多重数、短串或最高逆。

## 9. 核验记录与下一接口

[完整物理核验](../notes/2026-11-13-two-weight-groups-one-exceptional-full-mp-check-0c.py) 从三串物理基底直接构造 $D^n/n!$、真实输入范数矩阵及上述两个源，取完整有理逆，再与 (3.5) 比较。在 $q=1,\ldots,4$、$L=q,\ldots,q+3$、全部合法二维出生、全部 $0\le n\le h$，以及 $(a,c)=(2,3),(1/2,2)$ 上，424 个矩阵完全相等。该记录检验推导和实现；全参数证明在 §§2–8。

高度二的新结论可立即独立登记。一般高度的准确费用已经缩减为 §5 的 shear 行列式；四次中间系数、带标记变量的矩形 Schur 结构、固定出生与固定物理层之间的矩阵桥仍需继续。全两权已证、全高度二三组特例已证，并不解决任意有限正权、原连续尾 Schur 返回或普通 ISP。


[证书完整输出](../notes/2026-11-13-two-weight-groups-one-exceptional-height-two-certificate-0c.json)仅记录可重算的有限整数结果；一般内部四次式的 1840 组精确有理记录仍是有限证据，见上述笔记。另一个已闭无限参数子族为[短串三位、相对出生三的全部高度](R239-appendix-three-equal-short-weights-one-exceptional-saturated-two-dimensional-all-heights.md)，不扩其余出生。
