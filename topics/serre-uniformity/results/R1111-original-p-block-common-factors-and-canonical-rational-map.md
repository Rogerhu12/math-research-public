# R1111：原 Hasse 平方 p-block 的完整公因子与实际有理映射

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明：在 R1048 的原 r=2 行，两个规范 p-block 的全部公因子由原
T₀ 的二重/三重根及三个指定 CM 端点精确决定；约去后得到同一原来源的
可分有理映射，并付清其全部分歧。** 特别地，原 f_N=0 当且仅当
三个 r=0 点各产生恰二重公因子。这是端点问题的新几何判据，不是
端点或 bare 范数非零的证明。

## 1. 只消费原对象

取 R1048 的原范围
\[
p=12g-1\ge41,\qquad p\equiv2,5\pmod9,\qquad
N=2g-1,\quad \ell=(p+1)/3,\quad d=3N+1.
\]
令 k 为 Fp 的代数闭包，沿原有理 Hodge frame 记
\[
r=1-b^3,\quad A=bQ(b^3),\quad \deg A=d,\quad
h=r^{N+1}A,\quad T=T_0\in\mathbf F_p[b^3],
\]
\[
\deg T=d-1=(p-5)/2,\quad \operatorname{lc}(T)=-1,
\]
\[
\mathcal L=r\partial_b^2-4b^2\partial_b-\frac94b,\qquad
\mathcal LA=0,\qquad \mathcal LT=A.
\tag{1111.1}
\]
A 的根全部简单并避开 r=0；原模型、KS、正 CM 标记不变。

消费 R1048 §§3、5、6 的同一规范原函数与唯一规范 primitive：
\[
H=r^{\ell+1}(AT'-TA'),\quad H'=h^2,\qquad
J=P_{\rm prim}/h^2,\quad
J'=\frac{T}{r^{\ell+1}A^3}.
\tag{1111.2}
\]
其实际 p-block 为
\[
h^2=G_0+b^pG_1,\qquad H=H_0+b^pH_1,
\tag{1111.3}
\]
并有
\[
a=[b^{p-3}]h^2\in\mathbf F_p^\times,\qquad
P_{\rm prim}=G_1/a,\qquad H_i'=G_i,
\]
\[
K=(T/A)^2-2HJ=-2H_1/a,
\qquad H_0H_1'-H_1H_0'=\frac a2r^\ell T^2.
\tag{1111.4}
\]
J 在 A=0 的极阶至多 2，在 r=0 的极阶至多 \ell；没有任意
p 次幂自由项进入本篇。

R1048 给 deg H₁=p−1、首系数 −1。又 G₀ 的首项为
a b^(p−3)，H₀'=G₀ 且 deg H₀<p，所以进一步准确有
\[
\deg H_0=p-2,\qquad\operatorname{lc}(H_0)=-a/2.
\tag{1111.5}
\]
此处 p−2 为非零，未跨越一次积分共振。

以下 gcd 均取单首。定义
\[
M=\gcd(T,T'),\qquad D=\gcd(A,T,T'),
\qquad
\epsilon=
\begin{cases}
1,&T(1)=0,\\
0,&T(1)\ne0.
\end{cases}
\tag{1111.6}
\]
由于 T∈Fp[b³]，T 在任一 r=0 点为零当且仅当在全部三个点为零。
原端点尺度仍是 R1043/R1048 的 f_N=−T(1)/6。

## 2. 原 T 的全部可能重根

这些结论直接来自 (1111.1)，不假定 T 无重根。

若 x 满足 r(x)A(x)≠0，且 T(x)=T'(x)=0，则
\[
r(x)T''(x)=A(x)\ne0.
\]
所以该根恰为二重，不能更高。

若 A(s)=0、T(s)=0，则有两种情形。T'(s)≠0 时是单根。
若 T'(s)=0，先由 (1111.1) 得 T''(s)=0，再将方程微分得到
\[
r(s)T'''(s)=A'(s)\ne0.
\]
故此时恰为三重。这里 p>3，三阶导数准确检测三重根。
特别地，A 根上不出现恰二重的 T 根。

在 \rho³=1 处，原两个方程给
\[
A'(\rho)=-\frac{9A(\rho)}{16\rho},\qquad
T'(\rho)=-\frac{9T(\rho)}{16\rho}
          -\frac{A(\rho)}{4\rho^2},
\]
因而
\[
(AT'-TA')(\rho)=-\frac{A(\rho)^2}{4\rho^2}\ne0.
\tag{1111.7}
\]
无论 \epsilon 如何，H 在每个 \rho 的零阶都恰为 \ell+1。
若 T(\rho)=0，则 T'(\rho)=−A(\rho)/(4\rho²)≠0，T 在这里为单根。

于是 M 的零点只有两类：离开 A r 的二重 T 根，在 M 中重数一；
A 上的三重 T 根，在 M 中重数二。D 正是后一类根的单首
平方自由乘积，故 D²∣M，且 r 与 M D 互素。

## 3. 全部 p-block 公因子的准确公式

**定理。**
\[
\boxed{\quad
G:=\gcd(H_0,H_1)=M D\,(b^3-1)^{2\epsilon}.
\quad}
\tag{1111.8}
\]

若 H₀(x)=H₁(x)=0，(1111.4) 的 Wronskian 迫
r(x)T(x)=0。因此只须处理第2节的全部根，不能略掉 A 根。

### 3.1. 离开 A r 的根

若 T(x)=0 且 T'(x)≠0，(1111.2) 给 H(x)≠0，故不可能是公根。

若 T(x)=T'(x)=0，则第2节给恰二重根，并且 H(x)=0。
这里 h(x)≠0，所以 J 在 x 正则。由 (1111.4) 得 K(x)=0，
从而 H₁(x)=H₀(x)=0。另一方面 H'=h² 在 x 为单位，故 H 的
零阶恰为一；两个 p-block 的共同零阶只能恰为一。这正是 M
在该点的重数。

### 3.2. 原全部 supersingular 根 A(s)=0

若 T(s)≠0，则 (1111.4) 的 Wronskian 在 s 非零，没有公根。

若 T(s)=0 且 T'(s)≠0，则 T/A 在 s 为单位。由 H'=h² 及
H(s)=0，H 在 s 的零阶恰为三。J 的极阶至多二，所以 HJ 在
s 为零。因此
\[
K(s)=\bigl(T'(s)/A'(s)\bigr)^2\ne0.
\]
H₁(s) 为单位，仍没有公根。

剩下 T 在 s 为三重的情形。此时 T/A 的零阶为二，J' 在 s
正则；J 的已知极阶严格小于 p，因此 J 自身也正则。H 的零阶
仍恰为三。式 (1111.4) 遂给 ord_s(H₁)≥3，继而
ord_s(H₀)≥3。由于 H 的零阶恰三，最小值必恰三。这正是
M D 在该点的重数 2+1。

### 3.3. 三个指定 CM 点 r=0

若 T(\rho)≠0，J 的极阶至多 \ell 而 H 的零阶为 \ell+1；
故 HJ 在 \rho 为零。于是 K(\rho)=(T(\rho)/A(\rho))²
为单位，两个 p-block 无公根。

若 T(\rho)=0，置 t=b−\rho，并记 A₀=A(\rho)、T₁=T'(\rho)、
r₁=−3\rho²。第2节给 T₁=−A₀/(4\rho²)。实际主部为
\[
H=r_1^{\ell+1}A_0T_1t^{\ell+1}+O(t^{\ell+2}),
\]
\[
J=\frac{T_1}{r_1^{\ell+1}A_0^3(1-\ell)}
       t^{1-\ell}+O(t^{2-\ell}).
\tag{1111.9}
\]
这里 1−\ell=2/3 于 Fp，是单位；J 的规范不能改变此负次主部。
代入 K=(T/A)²−2HJ，并用 \ell=1/3 于 Fp，得
\[
K=-2(T_1/A_0)^2t^2+O(t^3)
  =-\frac{t^2}{8\rho^4}+O(t^3),
\]
\[
\boxed{\quad
H_1=\frac{a}{16\rho^4}t^2+O(t^3),\qquad
H_0=-\frac{a\rho^p}{16\rho^4}t^2+O(t^3).
\quad}
\tag{1111.10}
\]
因为 \ell+1>2，H=H₀+b^pH₁ 的高阶零不改变这两个二次首项。
所以三个共同零阶都恰为二，不只是“至少二重”。

以上穷尽全部有限点，证明 (1111.8)。由 (1111.5)，将
H₀,H₁ 都齐次化到次数 p−1 时，H₁ 在∞非零，所以∞没有
遗漏的共同基点。

## 4. 清除全部基点后的原有理映射及完整分歧

置
\[
U=-H_0/G,\quad V=H_1/G,\quad
\varphi=U/V=-H_0/H_1,\qquad n=p-1-\deg G.
\tag{1111.11}
\]
这是完全指定的实际有理函数，不是另选一个同微分的 primitive。
U,V 互素，且
\[
\deg V=n,\quad \deg U=n-1,\quad
\varphi(b)=-\frac a{2b}+O(b^{-2})\quad(b\to\infty).
\tag{1111.12}
\]
因此映射次数为 n，∞不分歧并映到 0。

定义
\[
C=\frac{T}{M D\,(b^3-1)^\epsilon}.
\tag{1111.13}
\]
第2节的根分类证明 C 是平方自由多项式，且 gcd(C,r)=1：
普通二重根除去 M 后留一重；A 上三重根由 M D 全部除去；
A 上单根保留；r=0 的单根由最后因子除去。

原 Wronskian 因而精确化成
\[
\boxed{\quad
U'V-UV'=\frac a2\,r^{\ell-2\epsilon}C^2,\qquad
\varphi'=\frac{a\,r^{\ell-2\epsilon}C^2}{2V^2}.
\quad}
\tag{1111.14}
\]
这不是仅模掉某一组根的身份，所有原 p-block 及常数 a/2 都保留。

右侧不恒零，故映射可分。n≤p−1，所有分歧都是 tame。
对互素的齐次坐标，U'V−UV' 是有限 chart 的分歧截面；
即使 V(x)=0，采用 1/\varphi 的局部坐标也给同一零阶。
因此完整分歧为：

| 点 | 分歧指数 |
| --- | --- |
| 每个 \rho³=1 | \ell+1−2\epsilon |
| 每个 C 的根 | 3 |
| 其余点，包括∞和被 M D 完全消去的 A 上三重根 | 1 |

特别地，没有把原 denominator 的零点当作丢弃的极点。

式 (1111.2) 还付三个指定端点的像。恒等式
\[
\varphi=b^p-H/H_1
\tag{1111.15}
\]
与 H、H₁ 的已知零阶给
\[
\boxed{\quad \varphi(\rho)=\rho^p,\qquad
e_\rho(\varphi)=\ell+1-2\epsilon.\quad}
\tag{1111.16}
\]
由于这些阶都小于 p，(b−\rho)^p 项不影响首项。
这与 (1111.14) 一致，是原 Frobenius 标记，不重选三个值。

最后有
\[
3(\ell-2\epsilon)+2\deg C=2n-2.
\tag{1111.17}
\]
故显示的分歧确实用尽 Riemann–Hurwitz 总次数。
此外，G∈Fp[b³]：除 0 外各根按 μ₃ 三元组出现；若 0 是 T 根，
它必是 A 上三重根，G 在 0 的次数也是三。因此
\[
\varphi(\zeta b)=\zeta^{-1}\varphi(b),\quad n\equiv1\pmod3
\qquad(\zeta^3=1).
\tag{1111.18}
\]
由 deg C≥0，还得 n≥(p+3)/2−3\epsilon。此界不区分
\epsilon=0 与 \epsilon=1，不应当作端点非零证明。

## 5. 返回原 f_N 与保留的主问题

由 R1043/R1048 的同一 f_N=−T(1)/6，(1111.8)–(1111.10) 给
\[
\boxed{
\begin{aligned}
f_N=0
&\iff r^2\mid\gcd(H_0,H_1)\\
&\iff e_\rho(\varphi)=\ell-1\text{，对全部 }\rho^3=1;\\
f_N\ne0
&\iff \gcd(r,\gcd(H_0,H_1))=1\\
&\iff e_\rho(\varphi)=\ell+1\text{，对全部 }\rho^3=1.
\end{aligned}}
\tag{1111.19}
\]
这把原端点失败刻画为该实际有理映射在三个 CM 点的精确降阶；
一般有理映射的存在、tame 分歧或平方导数均没有排除降阶情形。
继续工作必须使用本篇原 U,V 的来源，不能以任意同分歧型映射代替。

本篇没有证明 T(1)≠0，没有证明 R1048 的
B(c₀,c₀)=−a⁻¹Σ_{A(s)=0}H(s)^pG₁(s) 非零，也没有把两者等同。
r=8、同一本原 h 的两 mask、真正高度与所有充分大 p 的完整
Serre 一致性，均不由本篇自动解决。

## 来源与执行范围

- [R1048](R1048-original-AS-primitive-and-kernel-critical-value-norm.md)，
  §§1、3、5、6.1–6.2：原 A,T、规范 H,J、完整 p-block 及其
  Wronskian、a 的单位、原端点平方。
- [R1041](R1041-original-r2-bare-coefficient-and-Hodge-kernel-norm.md)，
  §§1–3：同一原族的整个 Hodge frame 与 LT=A。
- [R1043](R1043-original-fN-and-Hodge-kernel-CM-endpoint.md)：原
  f_N=−T₀(1)/6 的标记及完整尺度。

所有新结论均由这些原身份的纸面局部展开、精确公因子和
P¹ 上可分有理映射的分歧计算证明。无数学程序执行，无有限素数
扫描；只传输本篇小文本。主课题继续。
