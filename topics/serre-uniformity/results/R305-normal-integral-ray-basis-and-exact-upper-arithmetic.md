# R305：实际射线域的正规整基、精确乘法表与上层 Norm 算术

日期：2026-11-13。状态：**已证明并完成精确计算；实际忠实 Norm 原像及 $\mathcal L$ 仍未求得。**

固定 R171、R191、R207 的 $p=43$、同一个 $776$ 位素数 $q$、同一个 Weil 根及 tame 生成元。本文给出 $L_q/\mathbb Q(i)$ 的完整正规整基，及选定复共轭不动域 $L_q^+$ 的完整整数基。后者签名是 $(1,21)$，**不是全实域**。

新的实际乘法表只需 $1849$ 个 Gaussian 整数，最大系数为 $887$ bit。它已经通过严格界、$57$ 个小素数的 CRT 全部恢复，并且从新表独立构造的整数乘法矩阵，其特征多项式与 R207 的全部 $44$ 个巨大系数逐项相等。这使后续上层理想和 Norm 算术不再依赖一个未经主化的幂基整环。

## 1. 同一 Kummer 数据及相反角色的精确积

令
$$
p=43,\quad K=\mathbb Q(i),\quad
\mathcal B=K(\zeta_p),\quad r=i(\zeta_p-\zeta_p^{-1}),
$$
并沿用 R191 的实整数 $h=g(r)(2-r)^{22}$、$\sigma(\zeta_p)=\zeta_p^3$。记
$$
h_j=\sigma^j h,\qquad
E_j\in\{1,\ldots,42\},\quad E_j\equiv3^{-j}\pmod p.
$$
R191 的精确行列式及单位范数证明给
$$
\prod_{j=0}^{41}h_j=N_{\mathcal B/K}h=-q.
\tag{305.1}
$$

R207 的正权 Kummer 根为实数 $\alpha_+$，满足
$$
\alpha_+^p=\prod_{j=0}^{41}h_j^{E_j}.
$$
其提升 $\widetilde\sigma$ 阶为 $42$，并与原来的 tame 生成元 $\gamma$ 交换。对每个 $k\in\mathbb F_p^\times$，唯一写 $k=3^a$，定义
$$
R_k=\widetilde\sigma^a\alpha_+.
\tag{305.2}
$$
这些数全为实代数整数，且
$$
\gamma(R_k)=\zeta_p^kR_k,\qquad
R_k^p=\prod_{j=0}^{41}h_j^{[E_jk]_p},
\tag{305.3}
$$
其中 $[\cdot]_p$ 表示 $1,\ldots,p-1$ 的正代表。

因为 $[E_jk]_p+[E_j(-k)]_p=p$，(305.1) 给
$$
(R_kR_{-k})^p=(-q)^p.
$$
两边采用同一实嵌入，$p$ 为奇数，所以这里没有未定的 $p$ 次单位根：
$$
\boxed{R_kR_{-k}=-q.}
\tag{305.4}
$$

令
$$
\theta_n=\sum_{k\in\mathbb F_p^\times}\zeta_p^{nk}R_k
=\gamma^n\theta_0,\qquad n\in\mathbb F_p.
\tag{305.5}
$$
$\theta_0$ 正是 R207 的原生成元。每个 $\theta_n\in L_q$ 为整元；且
$$
\sum_n\theta_n=0,\qquad
\tau\theta_n=\theta_{-n},\qquad
\tau(i)=-i.
\tag{305.6}
$$

## 2. 全部 $43$ 处嵌入的整性：为何可以除以 $43$

定义
$$
\boxed{u_n=\frac{1+\theta_n}{p}\qquad(n\in\mathbb F_p).}
\tag{305.7}
$$
除 $p$ 外，整性已经由 $\theta_n$ 的整性成立。以下检查全部 $p$ 上方素点，不能只检查一个选定根。

在 $\mathcal B$ 的 $p$ 上方，$r$ 和 $\zeta_p-1$ 均有正赋值；R191 给 $g(0)\equiv6\pmod p$。于是
$$
h_j\equiv6\cdot2^{22}=31=17^2\pmod r
\qquad(0\le j<42).
\tag{305.8}
$$
又
$$
\sum_j[E_jk]_p=1+\cdots+42=903=21p,
\qquad31^{21}=1\pmod p.
$$
所以 (305.3) 在任意上方剩余域中给 $\overline{R_k}^{,p}=1$。特征 $p$ 域中 $X^p-1=(X-1)^p$，故
$$
R_k\equiv1\pmod{\mathfrak P}
\tag{305.9}
$$
对所有 $k$、所有 $p$ 上方素点均成立。乘任何可能的 $\zeta_p$ 根也不改变这句话。

因此 $\theta_n\equiv42\equiv-1\pmod{\mathfrak P}$。R191 §3 已通过完整 Hensel 证书证明 $L_q/K$ 在 $p$ **完全分裂**。所以每个 $\theta_n$ 所在的 $p$ 进完成域都是 $K_p$，而 $K_p/\mathbb Q_p$ 不分歧。其赋值群是 $\mathbb Z$；$v_p(1+\theta_n)>0$ 遂提高为
$$
v_p(1+\theta_n)\ge1.
\tag{305.10}
$$
这证明全部 $u_n$ 在 $p$ 整，因而是全局代数整数。这里只用 R191 已固定的域及所有局部嵌入，并未重新选择一个有利的 Kummer 根。

## 3. 完整正规整基及其精确迹配对

从 Fourier 和 (305.4)，
$$
\operatorname{Tr}_{L_q/K}\theta_n=0,
$$
以及
$$
\begin{aligned}
\operatorname{Tr}_{L_q/K}(\theta_n\theta_m)
&=-pq\sum_{k\ne0}\zeta_p^{(n-m)k}\\
&=pq(1-p\,\mathbf1_{n=m}).
\end{aligned}
\tag{305.11}
$$
置
$$
z_q=\frac{q+1}{p}\in\mathbb Z.
$$
于是
$$
\boxed{
\operatorname{Tr}u_n=1,\qquad
\operatorname{Tr}(u_nu_m)=z_q-q\,\mathbf1_{n=m}.}
\tag{305.12}
$$
其 Gram 矩阵是 $z_qJ_p-qI_p$。在常数向量上特征值为 $pz_q-q=1$，在增广子空间上为 $-q$，所以
$$
\det\bigl(\operatorname{Tr}(u_nu_m)\bigr)=(-q)^{p-1}=q^{42}.
\tag{305.13}
$$

R191 已证明 $L_q/K$ 的导子恰为 $(q)$，在 $2,p$ 均完全分裂。循环素数次扩张的全部 $42$ 个非平凡角色都有该导子；导子—判别式公式遂给相对判别式理想
$$
\mathfrak d_{L_q/K}=(q)^{42}.
\tag{305.14}
$$
所有 $u_n$ 已证明为整元，(305.13) 非零且与 (305.14) 完全一致。因此它们生成的 $\mathbb Z[i]$ 格与整个整数环的指数理想为单位，得到
$$
\boxed{\mathcal O_{L_q}=\bigoplus_{n=0}^{42}\mathbb Z[i]u_n.}
\tag{305.15}
$$
由于 $\gamma u_n=u_{n+1}$，这是一组**完整正规整基**。证明没有假定一般的 Hilbert–Speiser 性，也没有把仅在 $p$ 外极大的整环冒认为完整整数环。

还得到两个直接的精确接口：
$$
\sum_nu_n=1,\qquad
u_n^\vee=\frac{z_q-u_n}{q}
\tag{305.16}
$$
为该基及其迹对偶基，即 $\operatorname{Tr}(u_m u_n^\vee)=\mathbf1_{m=n}$。

## 4. 选定复共轭不动域的完整整数基及签名

令 $H_q=L_q^{\langle\tau\rangle}=L_q^+$。置
$$
A_j=u_j+u_{-j},\qquad B_j=i(u_j-u_{-j}),\qquad1\le j\le21.
\tag{305.17}
$$
则
$$
\boxed{u_0,A_1,\ldots,A_{21},B_1,\ldots,B_{21}}
\tag{305.18}
$$
是 $\mathcal O_{H_q}$ 的完整 $\mathbb Z$ 基。

事实上，(305.15) 中元素 $\sum c_nu_n$ 被 $\tau$ 固定，精确等价于
$c_{-n}=\overline{c_n}$；$c_0$ 是有理整数，其余每对 Gaussian 整数唯一给 (305.17) 的两个整数系数。故 (305.18) 生成全部不动整元，而非仅生成一个候选子格。

在 $H_q$ 上，绝对迹等于 $L_q/K$ 的相对迹，因为 $L_q=KH_q$、$K\cap H_q=\mathbb Q$。由 (305.12)，两块互相正交，且
$$
\begin{aligned}
\operatorname{Tr}(u_0^2)&=z_q-q,&
\operatorname{Tr}(u_0A_j)&=2z_q,\\
\operatorname{Tr}(A_jA_k)&=4z_q-2q\mathbf1_{j=k},&
\operatorname{Tr}(B_jB_k)&=2q\mathbf1_{j=k}.
\end{aligned}
\tag{305.19}
$$
第一块是 $D+z_qvv^t$，其中
$$
D=\operatorname{diag}(-q,-2q,\ldots,-2q),\qquad
v=(1,2,\ldots,2)^t.
$$
$v^tD^{-1}v=-43/q$，所以其行列式为 $-2^{21}q^{21}$；第二块行列式为 $2^{21}q^{21}$。因此
$$
\boxed{\operatorname{disc}(H_q)=-(2q)^{42}.}
\tag{305.20}
$$

签名也必须准确区分。$\operatorname{Gal}(L_q/\mathbb Q)$ 是阶 $86$ 二面体群。$\tau$ 在 $43$ 个 $H_q$ 嵌入上按 $n\mapsto-n$ 作用，恰固定 $n=0$ 一个嵌入，其他 $42$ 个成对。因此
$$
\boxed{(r_1(H_q),r_2(H_q))=(1,21).}
\tag{305.21}
$$
这与 (305.20) 的负号相容；没有仅从判别式负号推断完整签名。

## 5. 小尺寸的真实乘法表

由正规基，只需恢复
$$
u_0u_s=\sum_{t=0}^{42}c_{s,t}u_t,
\qquad c_{s,t}\in\mathbb Z[i].
\tag{305.22}
$$
全部其他乘法由
$$
u_a u_b=\sum_t c_{b-a,t}u_{t+a}
\tag{305.23}
$$
得到，下标模 $43$。

对非零 $k,l,k+l$，定义普通整元
$$
J_{k,l}=\prod_{j:\,[E_jk]_p+[E_jl]_p\ge p}h_j.
\tag{305.24}
$$
恰有 $21$ 个因子：把 $j$ 与 $j+21$ 配对后，恰有一项产生进位。由 (305.3) 取 $p$ 次幂，并再次使用同一个实嵌入，得到
$$
R_kR_l=J_{k,l}R_{k+l},\qquad
R_kR_lR_{-k-l}=-qJ_{k,l}.
\tag{305.25}
$$
这是精确全局恒等式，不是只在 Kummer 商中成立。

令
$$
D_{s,t}=\sum_{\substack{k,l\ne0\\k+l\ne0}}
\zeta_p^{sl-t(k+l)}J_{k,l}.
\tag{305.26}
$$
其 $\widetilde\sigma$ 不变性给 $D_{s,t}\in K$。用 (305.16) 的对偶基计算三重迹：
$$
c_{s,t}=\frac{z_q\operatorname{Tr}(u_0u_s)
-\operatorname{Tr}(u_0u_su_t)}q.
$$
逐项展开 (305.7)，再代入 (305.11)、(305.25)，得到执行公式
$$
\boxed{
c_{s,t}=\frac{q-1+D_{s,t}}{p^2}
 +\frac{\mathbf1_{t=0}+\mathbf1_{s=t}-q\mathbf1_{s=0}}p.}
\tag{305.27}
$$
虽然右边写有分母，(305.15) 已证明其为 Gaussian 整数。复共轭给
$$
\overline{c_{s,t}}=c_{-s,-t},
\tag{305.28}
$$
交换律及 $\sum_su_s=1$ 还给
$$
c_{s,t}=c_{-s,t-s},\qquad
\sum_s c_{s,t}=\mathbf1_{t=0}.
\tag{305.29}
$$
证书在精确整数层面检查了这些等式。

## 6. 严格界、CRT 与已经执行的独立整数检查

R207 已用有理区间算术证明全部 $\theta_n$ 的复绝对值不超过整数 $R$；该 $R$ 有 $639$ bit。故 $|u_n|\le(R+1)/p$，从对偶迹公式得
$$
|c_{s,t}|\le
\frac{z_q(z_q+q)+(R+1)^3/p^2}{q}.
$$
取整数上界
$$
\boxed{C=\left\lceil
\frac{p^2z_q(z_q+q)+(R+1)^3}{p^2q}\right\rceil.}
\tag{305.30}
$$
Gaussian 系数的实部、虚部绝对值都不超过这个 $1128$ bit 的界。

计算取 $\ell\equiv1\pmod{172}$，沿 R207 相同的小素数序列。每个素数仍由试除验证。在 $\mathbb F_\ell$ 选阶 $172$ 的 $\xi$，准确取
$$
r=\xi+\xi^{-1},\qquad i=-\xi^{43},\qquad\zeta_p=\xi^{44};
\tag{305.31}
$$
于是 $r=i(\zeta_p-\zeta_p^{-1})$。这个 $i$ 的方向用于恢复 Gaussian 虚部，不能默换其符号。

先计算 $42$ 个 $h_j$ 和 (305.24) 的 $1722$ 个乘积。置
$$
M_{l,m}=J_{-l-m,l}
$$
（含零指标或 $l+m=0$ 时置零），$F_{s,l}=\zeta_p^{sl}$，则 (305.26) 是二维有限 Fourier 变换 $D=FMF^t$。代入 (305.27)，再由 (305.28) 分离实、虚部。程序中的 $43$ 项整数矩阵点积有显式 $43(\ell-1)^2<2^{63}$ 检查，不依赖溢出后的偶然余数。

实际执行结果为：

| 项目 | 实际值 |
|---|---:|
| Gaussian 乘法系数个数 | $43^2=1849$ |
| 严格实、虚部界 $C$ 的 bit 长度 | $1128$ |
| 使用的 CRT 素数 | $57$ 个 |
| CRT 模数 bit 长度 | $1139$ |
| 最大实际系数 bit 长度 | $887$ |
| 压缩证书大小 | $194203$ 字节 |

CRT 模数 $M>2C$，故居中恢复唯一确定了全部整数系数。新脚本的 `--verify` 方式重新计算全部 $57$ 行及严格界，而非仅抽查证书中的哈希。

另作了两类已经执行的检查。

第一，在三个未参与重建的素数 $3000541,3001057,3002089$ 上，重新计算全部乘法表。随后在真正的 $43$ 维代数
$$
\mathbb F_\ell[Z]/\left(Z^p-\prod_jh_j^{E_j}\right)
$$
中直接相乘全部 $u_0u_s$，与 (305.22) 逐系数比较。所用 $R_k$ 是单项式
$$
R_k=Z^k\prod_jh_j^{-\lfloor E_jk/p\rfloor},
\tag{305.32}
$$
所以这个检查绕过了三重迹的 Fourier 公式。可分代数不必是域，计算仍有效。

第二，由已恢复的整数表，在真实基 (305.18) 上构造“乘 $\theta_0=pu_0-1$”的 **$43\times43$ 整数矩阵**，使用 FLINT 作完整整数特征多项式。其全部系数与 R207 原证书逐项相等，包括最大 $26948$ bit 的系数。这个检查使用新乘法表和整数矩阵，未从 R207 的多项式反推新表。

## 7. 直接用于实际上层的整数环、Norm 与剩余读取

继续记 R201/R219 的
$$
F=K(z),\qquad H=F^{\langle\tau\rangle},\qquad
L=FL_q,
\qquad [F:K]=44.
$$
$F/K$ 只在 $2,p$ 分歧，$L_q/K$ 只在 $q$ 分歧，且两者次数互素。因此相对判别式支集不交。逐局部看，至少一个整数环扩张为 étale，故张量整数环已经正规；得到
$$
\boxed{\mathcal O_L=\mathcal O_F\otimes_{\mathbb Z[i]}\mathcal O_{L_q}
=\bigoplus_{n=0}^{42}\mathcal O_F u_n.}
\tag{305.33}
$$
这包括 $2,p,q$ 三处，不存在新的上层指数要先因式分解。

对
$$
X=\sum_n x_nu_n\in L,\qquad x_n\in F,
$$
乘法矩阵的准确公式为
$$
(M_X)_{k,j}=\sum_{n=0}^{42}x_n c_{j-n,k-n},\qquad
\boxed{N_{L/F}X=\det M_X.}
\tag{305.34}
$$
因此实际 ordinary-unit Norm 问题可以在已知最大整环的 $43$ 个 $F$ 坐标中执行，使用 $887$ bit 的固定结构常数；它不需要重建上层的绝对 $3784$ 次幂基整数环。若使用 R219 的实目标，则
$$
\tau X=X\quad\Longleftrightarrow\quad x_{-n}=\tau(x_n)
\tag{305.35}
$$
是精确的线性约束。

也有
$$
L^+=HH_q,\qquad[L^+:\mathbb Q]=44\cdot43=1892.
$$
把 $H$ 的整数基与 (305.18) 张量，至少在 $2$ 外已经是最大整环的基，因为两因子的奇分歧支集分别位于 $p$ 和 $q$。本文不把这个实数域张量基在 $2$ 处自动说成完整最大整环；完整的 (305.33) 没有这项不足。

在 R191 的已标记 $q$ 素点，每个 $\theta_n$ 的唯一最低项为 $\zeta_p^nR_1$，所以都具有赋值 $1/p$。于是
$$
u_n\equiv p^{-1}\pmod{\mathfrak Q}.
\tag{305.36}
$$
若 $X$ 为真实 Norm 见证、$N X$ 在该处是单位，则 $X$ 在 $\mathfrak Q$ 是单位；由 (305.33)，其所有 $x_n$ 在对应底域素点均为整元。因此
$$
\boxed{\overline X=p^{-1}\sum_n\overline{x_n}
=p^{-1}\overline{\operatorname{Tr}_{L/F}X}.}
\tag{305.37}
$$
同一公式适用于所有所需 $C_{44}$ 共轭，保留原来的 $\gamma$ 方向。它给 R201 剩余符号一个新的低成本读取法；它**没有**替全局 Norm 方程选择一个剩余根。

若只找到普通非单位 Norm 见证，R200 的正号外支撑 Artin 修正仍然必须加入。这里的最大整环、迹公式及 local integrality 不能删掉那项修正。

## 8. 文件、执行方式及明确剩余工作

- [构造与完整核验脚本](../scripts/build_r305_normal_integral_basis.py)
- [精确正规整基乘法表证书](../notes/r305_normal_integral_basis_certificate.json.gz)
- 输入为 [R207 的完整 Gaussian trace 证书](../notes/r207_gaussian_trace_degree43_certificate.json)，源字节 SHA256 已写进新证书。

脚本使用 Python、NumPy 和 `python-flint` 的整数矩阵特征多项式。重建并写证书：

~~~sh
python scripts/build_r305_normal_integral_basis.py \
  --source notes/r207_gaussian_trace_degree43_certificate.json \
  --output notes/r305_normal_integral_basis_certificate.json.gz
~~~

完整复核既有证书（重新计算全部 CRT 行、所有额外直接乘积及整数特征多项式）：

~~~sh
python scripts/build_r305_normal_integral_basis.py \
  --source notes/r207_gaussian_trace_degree43_certificate.json \
  --output notes/r305_normal_integral_basis_certificate.json.gz --verify
~~~

压缩数据 SHA256：
~~~text
e8cc0efb536e5a248933e95b567cb2e6efbca4a78472503518e9c387d50aa19b
~~~

本条新增的是同一个实际上层域的完整整数算术输入，不是另一个辅助域。$L_q^+$ 的全部 $43$ 个整数基、上层 $L/F$ 的全部乘法和指定 $q$ 剩余读取均已具体化。下一步仍需在 (305.34) 中真正取得 R219/R239 的 faithful Norm 原像；目前 **$X$ 和 $\mathcal L$ 都没有求出**，R202 保留给实际求值。

主要已发表输入仅为相对导子—判别式公式及整数环的无交分歧基变换性质；前者可参 J. S. Milne, *Class Field Theory*, Chapter V, Theorem 3.27, p. 165 的 conductor–discriminant formula，[课程原文](https://www.jmilne.org/math/CourseNotes/CFT.pdf)。全部特定 Kummer 乘积、$43$ 整性、迹配对、基判别式、乘法系数和高度界已在本文展开。域、导子及原标记仍是 [R191](R191-cyclotomic-principalization-and-eta-ray-field.md)、[R207](R207-gaussian-trace-model-of-the-actual-ray-extension.md) 的已核输入。
