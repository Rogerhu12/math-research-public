# R878 — 原第一因子的 level867 坐标证书

日期：2026-11-16。

**状态：本篇给出原第一因子 $E_{17}:y^2=x^3+17$ 的完整低层坐标证书和可执行 producer。它将原 level10404 的问题准确放到当前同一个 $M_2(867)$ 乘积基；两个有限末端、全部常数、角色和目标微分均已证明。尚未执行成功的候选不得称为实际模参数，尤其不预设 Manin 常数为1。没有计算出 R859 的原非零 shadow。**

## 1. 同一个原源、第一新形式与两个变量

固定 R831/R848 的
$$
X=X_0(10404),\qquad B=X_0(867),\qquad
\pi:X\longrightarrow B,\quad z\longmapsto6z.
\tag{1}
$$
在 $\infty$ 处写
$$
q=e^{2\pi iz},\qquad Q=q^6,\qquad D_Q=Q\,d/dQ.
$$
故在拉回的级数上 $D_q=6D_Q$。
$\pi$ 的实际次数为18，deck 群为原 $C_3\times S_3$；
不是将另一个较小曲线替换成原源。

令 $f(q)$ 为原 $E_{17}:y^2=x^3+17$ 的首项1新形式。
其完整来源就是 R826 的第一因子，含原2、3、17处 conductor；
$$
f(q)=q-5q^7-7q^{13}-7q^{19}+\cdots
=q\,f_0(Q),\qquad f_0(0)=1.
\tag{2}
$$
这里 $a_n=0$ 除非 $n\equiv1\pmod6$。
这是原 $R:z\mapsto z+1/3$ 上特征 $\omega$、
$S:z\mapsto z+1/2$ 上特征 $-1$ 的完整恒等式。
原 $S_3$ 的两个 transpositions $S,w_4$ 都在第一 $h^1$ 上作用 $-1$，
故是同一 sign 角色。所有三次角色方向照 R848 保持，
包括 $q_1R=R_C^2q_1$。

本篇寻找归一为
$$
F_{17}(\infty)=O,\qquad
F_{17}^*\frac{dx}{2y}=f(q)\frac{dq}{q}
\tag{3}
$$
的**候选**。原准同态空间存在这个方向不等于 (3) 已是整数同态；
本篇只在完整坐标恒等式通过之后认 (3) 为真实态射。

还须从微分作用付清曲线映射的常值。若 (3) 的候选已为真实态射，
因 $R\infty=\infty$，微分和原点归一准确给
$F_{17}R=[\omega]F_{17}$。原 $w_4$ 在 $h^1_f$ 上为 $-1$，
故
$$
F_{17}w_4=-F_{17}+T,\qquad T=F_{17}(w_4\infty)\in E_{17}(\mathbf Q).
\tag{3a}
$$
这里 $w_4$ 与其 cusp 及 $F_{17}$ 都在 $\mathbf Q$ 上。
R848 的实际曲线群给 $w_4R=Rw_4$；代入上式和
$F_{17}R=[\omega]F_{17}$，得到 $[\omega]T=T$。
但 $E_{17}[1-\omega]$ 的非零点准确为 $(0,\pm\sqrt{17})$，
没有 $\mathbf Q$-有理非零点。因此 $T=O$。
同样 $S\infty=\infty$ 直接给 $F_{17}S=-F_{17}$。
所以此处的整个 $S_3$ 是真实曲线映射上的 sign，
而非只在微分上忘掉一个平移。这个论证不使用
Manin 常数、模次数或任意其它 torsion 输入。

## 2. 准确抵消 sign 的权六因子

在 $B$ 的上半平面变量上置
$$
e(Q)=\eta(Q)^{12}=Q^{1/2}\prod_{n\ge1}(1-Q^n)^{12},
\qquad \Delta(Q)=e(Q)^2.
\tag{4}
$$
$e$ 是权六、模2 sign 角色的模形式。这个绝对号可直接由
$$
\eta(\tau+1)=e^{\pi i/12}\eta(\tau),\qquad
\eta(-1/\tau)=(-i\tau)^{1/2}\eta(\tau)
$$
得到：$e|_6T=-e$、$e|_6S=-e$；
$S,T$ 模2都是 $S_3$ 的 transpositions，故角色恰是 sign。

在原 $\pi$ 上，$e(q^6)=q^3\prod(1-q^{6n})^{12}$。
它在中央 $R$ 上特征1，在原 $S_3$ 上为 sign。
若 (3) 已为真实态射，则其 $y$ 坐标在 $R$ 下不变，
在 $S_3$ 下为 sign；因此
$$
\boxed{V(Q)=e(Q)y(F_{17}(q))}
\tag{5}
$$
准确下降为 $B$ 上一个亚纯权六截面。这里不是把 $y$ 本身
当作 $B$ 上的有理函数。

同样，无论 (3) 是否已经可积，经典新形式始终给
$$
\boxed{\mathcal H(Q)=f(q)^3e(Q)\in M_{12}(\Gamma_0(867)).}
\tag{6}
$$
其 $R$ 特征为 $\omega^3=1$，两个 sign 相乘为1。
源上乘积在所有 cusp 全纯，故下降截面也全纯。
没有在 (6) 使用某条假定存在的椭圆映射。

写 $E(Q)=\prod(1-Q^n)^{12}$，则全部 Fourier 归一为
$$
\Delta=Q E^2,\qquad
\mathcal H=Qf_0^3E=Q-27Q^2+\cdots .
\tag{7}
$$
这些式子没有额外的6或其幂；6只在微分 $D_q=6D_Q$ 中出现。

## 3. 一个完全有理的候选 germ

写形式上的
$$
x(q)=q^{-2}X(Q),\qquad y(q)=q^{-3}U(Q),\qquad
X(0)=1,\quad U(0)=-1.
$$
椭圆方程和 (3) 等价于
$$
\boxed{
X^3=U^2-17Q,\qquad
2Q U'-U=f_0X^2.
}
\tag{8}
$$
第二式用的是 $D_qy=3x^2f$，所以2和17都不能删除。

给一个只含有理数的三角递推。记 $B_n=[Q^n]X^2$，
$U_0=-1,X_0=B_0=1$。在已知小于 $n$ 的系数后，置
$$
\begin{aligned}
s_n&=\sum_{i=1}^{n-1}X_iX_{n-i},\\
t_n&=\sum_{i=1}^{n-1}U_iU_{n-i}
 -17\,1_{n=1}-s_n-\sum_{i=1}^{n-1}B_iX_{n-i}.
\end{aligned}
$$
则准确有
$$
\boxed{
U_n=\frac{2t_n+3s_n
       +3\sum_{i=1}^n(f_0)_iB_{n-i}}{6n+1},
\quad
X_n=\frac{t_n-2U_n}{3},
\quad B_n=2X_n+s_n.
}
\tag{9}
$$
证明是先比较 (8) 第一式的第 $n$ 项，得到
$3X_n=-2U_n+t_n$，再代入第二式。
所有未知线性项的总系数恰为 $(6n+1)/3$。

由 $a_7=-5$，
$$
U_1=-7,\qquad X_1=-1,\qquad
V_{\rm form}=E(Q)U(Q)=-1+5Q+\cdots .
\tag{10}
$$
(9) 是指定 (3) 的形式解，不以其存在推出全局可积性。
程序的模辅助素数计算只在 $3(6n+1)$ 可逆时使用该递推；
最终证书仍在 $\mathbf Q$ 上。

## 4. 直接消费同一个 $M_2(867)$ 乘积基

对偶数 $k\ge2$，取
$$
A\in M_{k+6}(867),\qquad B_0\in M_k(867),\quad B_0\ne0,
\qquad V=A/B_0 .
\tag{11}
$$
本节 $B_0$ 表示分母截面，不是曲线 $B$，也不是递推的 $B_n$。
设当前同一个有理 $M_2(867)$ 有序基为 $g_0,\ldots,g_{119}$。
用完整独立的乘积 recipes
$\mathcal R_{k+6}$、$\mathcal R_k$，候选坐标就是
$$
A=\sum_{I\in\mathcal R_{k+6}}a_I\prod_{i\in I}g_i,\qquad
B_0=\sum_{J\in\mathcal R_k}b_J\prod_{j\in J}g_j.
\tag{12}
$$
因此输出 `sol` 的前一块是 $a_I$，后一块是 $b_J$；
它不是只给一个任意 q-前缀。每个 recipe 是原有序基的整数下标元组。
有限好素数上的满秩证明这些实际乘积在特征零独立；
达到下面的已知维数后，才称为完整基。

原 $B$ 没有 elliptic points，指数1224、cusp 数36、亏格85；
权二线丛是 $\Omega_B^1(\mathrm{cusps})$，次数204。
于是偶数 $w\ge2$ 有
$$
\dim M_w(867)=102w-84.
\tag{13}
$$
$k=2$ 的两块维数为732与120，总852；
$k=4$ 为936与324，总1260。

### 4.1 低线性读数的准确末端

置
$$
L_k=204k+612 .
$$
读取
$$
\boxed{A-V_{\rm form}B_0=0
       \quad\text{于全部 }Q^0,\ldots,Q^{L_k}.}
\tag{14}
$$
如果两个实际全局比值满足这一前缀，其交叉差分子
$A_1B_2-A_2B_1$ 为权 $2k+6$ 全纯模形式。
分母的 cusp 消失只会增加差分子的消失阶，故 (14) 迫其消到
$Q^{L_k+1}$。这个权的 Sturm 界准确是
$102(2k+6)=L_k$，所以差分子全零。

因此成功时的比值唯一；多维线性核可来自共同分母，不是多个候选映射。
(14) 本身仍不认证一个形式比值为原椭圆映射，须检查下一节。

## 5. 完整椭圆恒等式和第二个有限末端

令 $E_2(Q)=1-24\sum_{n\ge1}\sigma_1(n)Q^n$，
并定义
$$
\boxed{
C=(D_QA)B_0-A(D_QB_0)-\frac12E_2AB_0.
}
\tag{15}
$$
这是完整的 Serre 导数差：
$$
C=\partial_{k+6}A\cdot B_0-A\cdot\partial_kB_0,\qquad
\partial_w=D_Q-\frac w{12}E_2.
$$
故 $C$ 为权 $2k+8$ 的全纯模形式。不能将 (15) 的 $E_2/2$ 删除。

所需且足够的全局恒等式是
$$
\boxed{
8\Delta\,C^3
=\mathcal H\,B_0^2
      (A^2-17\Delta B_0^2)^2.
}
\tag{16}
$$
两边权都准确为 $6k+36$。
在 $\mathbf Q$ 上核 (16) 的全部系数
$$
\boxed{Q^0,\ldots,Q^{612(k+6)}}
\tag{17}
$$
即由 Sturm 得到完整恒等式，包含末端。这里 $k=2,4$ 的严格末端
分别是4896、6120。所用 $\mathcal H,\Delta,E_2$ 和模形式基
必须是同一原全局对象的加长前缀。

若 (14)、(16) 成立并保 (10) 的原点主项，则在原 $X$ 上定义
$$
\boxed{
y=\frac{A}{e B_0},\qquad
x=\frac{f(q)(A^2-17\Delta B_0^2)}{2e C}.
}
\tag{18}
$$
这些是原源上的真正亚纯函数，全部有限角色已在 §2 支付。
由 (16)、$\mathcal H=f^3e$、$\Delta=e^2$，直接得到
$$
x^3=y^2-17,\qquad
D_qy=3x^2 f.
$$
因此
$$
\frac{dx}{2y}=\frac{dy}{3x^2}=f(q)\frac{dq}{q}.
\tag{19}
$$
在 $\infty$，
$$
y=-q^{-3}+O(q^3),\qquad x=q^{-2}+O(q^4).
$$
所以 (18) 在原点取 $O$，并非某个未定平移。
到射影光滑椭圆曲线的有理映射自动在整条光滑源曲线上延拓。
这就认证了 (3) 的实际整数同态；此时才可说该规范的 Manin 倍数为1。

若一个既定 $\Gamma_f$ 是这个微分的其它代数倍，仍须在实际
$h^1$ 对应里保该倍数。本篇不把所有代数倍都认成椭圆曲线的整数倍映射。

## 6. 有界分母截面的条件保证

这一节只解释一个**已知实际映射次数**如何保证 (11) 的存在，
不将未核的数值用作当前算法前提。

若 (3) 已为真实态射、次数为 $d_F$，则 $y$ 的极除子次数为 $3d_F$。
(5)中 $e$ 在所有 cusp 全纯，因此
$$
18\deg(\operatorname{pole}V)\le3d_F,\qquad
\deg(\operatorname{pole}V)\le d_F/6 .
\tag{20}
$$
这里按实际18次覆盖拉回除子，所有 cusp 分歧重数都包括在内。
极除子在 $B$ 上为整数除子；不把半整数的 sign 局部参数单独计作分支点。

取 $B_0$ 的零除子覆盖 $\operatorname{pole}V$ 后，$A=VB_0$ 全纯。
Riemann–Roch 保证这种非零 $B_0\in M_k$ 存在，只需
$$
102k-\deg(\operatorname{pole}V)\ge85.
\tag{21}
$$
例如**如果另已认证** $d_F=1296$，则极次数至多216，
$k=4$ 的 (21) 成立。这里不以数据库的 degree/Manin 条目代替该前提。
程序对 $k=2,4$ 的完整 PASS 不依赖这个可选保证。

某个 $k$ 的有限矩阵满列秩可严格排该权下的指定比值。
有限 CRT 预算耗尽只表示尚未得到证书；
两者都不能据此否认原模参数或更大整数倍存在。

## 7. 原 $E_0$、端点及 shadow 的实际接口

(18)输出的目标是 $E_{17}$。取原 $\theta_{17}^6=17$，
按同一个 $H_{17}$ 嵌入作
$$
\phi_{17}:E_{17}\to E_0,\qquad
(x,y)\longmapsto(x/\theta_{17}^2,y/\theta_{17}^3),
\qquad \phi_{17}^*\omega_0=\theta_{17}\omega_{17}.
\tag{22}
$$
这是原 $F$ 因子的尺度，不是新的有限角色或 period。
若原 $\Gamma_f$ 有另一个已固定系数，仍按 R839/R862 保留在有限组合中。

原 R859 读取仍为
$$
S_r\bigl(\Pi(F,a q_0,b q_2)_*[X]\bigr)
=\operatorname{Alb}(bq_2)_*(a q_0-\phi_rF)^*[O].
\tag{23}
$$
(18)补的是此前欠缺的第一坐标；原 $a,b$ 的认证、$q_0/q_2$、
闭点重数、全部 $\operatorname{Gal}(H_{34}/K)$ 权、整数 $D$、
$X_0$ 的 $6^{-2}$、$X_1$ 的 $12^{-2}$ 和 $1632/816$ 均不变。
特别不能把一次候选的成功相认 R814 canonical cycle 或其7993证书。

程序可与当前 $g$ 坐标任务独立运行，也可接同进程中的
`forms2` 与完整乘积 recipes；`sol` 块的定义严格是 (12)。
不应只保存一个 hash 后声称已有可求值的函数：
实际消费者须在同进程接收这些对象，或按已提交 producer 确定性重算。

## 8. 公开执行和输出范围

附带 producer
`scripts/produce-r878-original-first-factor-map.py`
只在本公开仓库 Actions 执行；默认依次检查 $k=2,4$。
它用原 $E_{17}$ 的完整 `anlist` 生成 $f$，
核 $a_2=a_3=a_{17}=0$ 与原 $1\bmod6$ 支持；
不从另一个四次曲线或二耗尽形式取输入。

有限素数仅用于选真实全局乘积基和提出有理 CRT 系数；
只有 (16) 的完整有理恒等式及原点主项才输出
`certified_original_first_factor=true`。
输出只含源码、参数、全部摘要/hash 和是否通过，
不产生可重算数据文件或 Release 附件。
所有模辅助素数与目标 shadow 的惰性 $r$ 严格区分。

本篇没有预报程序运行结果；也没有把经典点或复微分等式
代替 (16) 的全局代数认证。

## 9. 依赖与实际原文范围

- [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)、
  [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)、
  [R847](R847-original-dyadic-s3-and-genus-seven-lower-bound.md)、
  [R848](R848-original-degree-eighteen-hecke-quotient-and-top-form.md)：
  原第一形式、$C_3\times S_3$、$Q=q^6$ 以及两个原退化端点。
- [R870](R870-original-low-weight-quotient-and-exact-elliptic-coordinate-certificate.md)：
  同一 $M_2(867)$ 全局基、原曲线的维数/次数和 Sturm 认证规范。
  本篇重新支付 sign、权六 Serre 导数、8与17，未搬用该篇的不同目标公式。
- Sage 官方 `EllipticCurve_rational_field.anlist` 与模形式 q-expansion：
  <https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html>。
  程序只用其完整新形式系数，不调用 `modular_parametrization()` 推定可积性。
- 标准 Dedekind eta 的两个生成元变换已在 §2 显式给出；
  所有后续下降和常数由这两式及原源群直接推出。


实际公开执行参数：
```
sage -python scripts/produce-r878-original-first-factor-map.py --weights 2,4 --max-primes 96 --prime-start 1000000000 --product-prime 1000037
```
Sage10.6固定镜像 `sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb`；实际run与输出hash在完成后记录。这个启动不是已通过证书的声明。
