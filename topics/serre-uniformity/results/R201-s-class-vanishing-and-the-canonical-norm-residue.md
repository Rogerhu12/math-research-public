# R201：$S$ 类群消失、受支撑 Norm 解与唯一规范剩余符号

**状态：已证明。** 固定 R171 的 $p=43$、同一个 $q$ 与 Weil 标记。
本文证明普通 $S$ 单位 Norm 解存在，并计算同一模 $p^2$ Kummer
规范的根修正。R200 的实际二阶障碍因此为
$\Omega_2^\epsilon=\epsilon(10-\mathcal L)$。
**$\mathcal L$ 尚未求值。** 存在性、根修正与实际 Norm 原像的
剩余值是三个不同命题，本条没有把前两者冒作第三者。
环境丢失后所有源/证书均已重建并实际运行，新 SHA 单独登记。

## 1. 角色与严格局部直线

置
$$
K=\mathbb Q(i),\quad A:y^2=x^3-x,\quad
F=K(A[p])^{\mathbb F_p^\times},\quad L=FL_q,\quad
S=\{2,p,q,\infty\},
\tag{201.1}
$$
$L_q/K$ 是 R191 的循环 $43$ 次扩张，在 $p,2$ 完全分裂、
只在 $q$ tame 分歧。$[F:K]=44$，并有
$$
\operatorname{Gal}(L/\mathbb Q)
 =(C_{44}\times\Gamma)\rtimes\langle\tau\rangle,\qquad
\Gamma=C_{43},
\tag{201.2}
$$
$\tau$ 同时反演两个循环因子。

$W$ 是 $\operatorname{ad}^0(A[p])$ 的二维非 Cartan 分量，
在 $\mathbb F_{p^2}$ 上的 $C_{44}$ 角色为 $\chi,\chi^{-1}$，
$$
\chi(\sigma)=\omega=8+25i,\qquad\operatorname{ord}(\omega)=44.
$$
$\tau$ 交换两条角色线，$W^{C_{44}}=0$。
迹配对给 $W^\vee\simeq W$，乘 $i$ 给 $W\otimes\eta\simeq W$；
这不把 $W$ 和 $W(1)$ 的类群型混淆。

R161、R168 给严格 $p$ 局部直线
$$
H^1_{\rm str,q}(\mathbb Q,W)=\mathbb F_p w.
\tag{201.3}
$$
其在 $p$ 为零、在 $2$ 的整个局部群为零、在 $S$ 外不分歧。
以
$$
F_0=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad K_0=JF_0
$$
为 R168 基，$q$ 处有限/奇异坐标为 $aF_0,bK_0$，满足
$$
a=\lambda_qb,\qquad\lambda_q=16\ne0.
\tag{201.4}
$$
正号首类 $b=-1=42,a=27$，所以 $2a=11\ne0$；负号同时改号。

## 2. 准确的 $S$ 类群型消失

### 定理 201.1

对 $\chi,\chi^{-1}$ 合成的整 $p$ 进等型投影 $e_W$，
$$
e_W(\operatorname{Cl}_S(L)\otimes\mathbb Z_p)=0.
\tag{201.5}
$$
不声称整个 $p$ 类群为零。

**证明。**
若所需分量非零，取
$\operatorname{Hom}(\operatorname{Cl}_S(L),\mathbb F_p)$，
再在该 $C_{44}$ 型中取 $\Gamma$ 不变量，仍非零：
有限 $p$ 群在非零特征 $p$ 空间上有不变量，
且 $C_{44}$ 与 $\Gamma$ 交换。
$\tau$ 交换两个不同角色；prime-to-$p$ 的半单性给出非零 $W$ 型，
即一个非零
$$
z\in\bigl(H^1(G_{L,S},\mathbb F_p)\otimes W\bigr)
 ^{\operatorname{Gal}(L/\mathbb Q)}.
$$
该类处处不分歧，并在 $S$ 上完全分裂。

$C_{44}$ 正规、阶与 $p$ 互素且不变量为零，
Hochschild--Serre 给
$H^j(\operatorname{Gal}(L/\mathbb Q),W)=0$ 对所有 $j$ 成立。
所以 $z$ 唯一下降为非零 $c\in H^1(G_{\mathbb Q,S},W)$。

$p$ 处 $L_q/K$ 分裂，局部 $L=F$；
$[F_p:\mathbb Q_p]=88$ 与 $p$ 互素，限制在 $H^1$ 上单射，
所以 $c_p=0$。$2$ 处用局部消失，其余处不分歧，
故 $c$ 落在 (201.3)。

$q$ 处 $F_q=K_q$ 是未分歧二次，$L/F$ 全分歧 $p$ 次。
限制可以杀奇异坐标，但有限坐标保留为 $2aF_0$。
类群扩张在 $q$ 完全分裂，故 $a=0$；
(201.4) 迫 $b=0$，与严格直线的非零类矛盾。
因此所需模 $p$ 对偶型消失。
有限 $p$ 群非零必有非零模 $p$ 商，
迹自对偶又保证返回的是同一个 $W$ 型，故得 (201.5)。证毕。

## 3. 在正确角色通道清除 $S$ 外支撑

记 $D_L=\operatorname{Div}_{S^c}(L)$。
在 $S$ 外，$L/F$ 不分歧且次数为素数 $p$：
分裂轨道的 Norm 核是增广理想，惰性轨道的 Norm 是乘 $p$、无核。
因此
$$
\ker(N:D_L\to D_F)=(\gamma-1)D_L.
\tag{201.6}
$$
扩到含 $44$ 次单位根的未分歧系数环 $\mathcal O$，
在 $\chi,\chi^{-1}$ 分量分别使用。
由除子正合列与 (201.5)，
$(L^\times\otimes\mathcal O)_\chi\to(D_L\otimes\mathcal O)_\chi$ 满射。
若 $NX=U$ 且 $U$ 是底域 $S$ 单位，写
$\operatorname{div}X=(\gamma-1)D_1$，取 $\operatorname{div}Y=D_1$，
则
$$
X'=X\,Y/\gamma Y
\tag{201.7}
$$
有同一 Norm，且 $S$ 外除子为零。
这是在所需完成的角色通道中进行，不能据局部类群型消失
声称整个类群的 $p$ 部为零。

### 引理 201.2（普通代数数的精确 Norm）

若普通 $U\in E_F^S=\mathcal O_{F,S}^\times$ 的模 $p$ Kummer 类
位于 $e_W$ 型，且 $U$ 是普通全局 Norm，则有普通
$X_U\in E_L^S$ 满足 $NX_U=U$。

**证明。**
按 (201.7) 清除一个 Norm 原像的 $e_W$ 部分。
$(1-e_W)U$ 在 $E_F^S\otimes\mathbb Z_p$ 中是 $p$ 倍；
加入底域元素 $((1-e_W)U)/p$，其 Norm 正好补齐余项。
得完成的 $S$ 单位 $Z_S$，$NZ_S=U$。

$E_L^S$ 有限生成，选普通 $z_0\equiv Z_S\pmod p$。
于是 $Nz_0/U\in E_F^S\cap p(E_F^S\otimes\mathbb Z_p)$。
有限生成阿贝尔群逐自由/有限部分证明
$$
E_F^S\cap p(E_F^S\otimes\mathbb Z_p)=(E_F^S)^p.
\tag{201.8}
$$
本例 $\mu_F$ 无 $p$ 挠元，因 $[F:\mathbb Q]=88$
不能包含次数 $42$ 的 $\mathbb Q(\mu_{43})$。
因此 $Nz_0/U=v_0^p$，$v_0\in E_F^S$。
取 $X_U=z_0/v_0$ 即得精确普通 Norm。证毕。

这里尚未计算 $z_0,v_0$，不能把存在性当成实际剩余值。

## 4. 同一 $d_0$ 的两个目标

令 $u_j=\sigma^j u_0$，$u_0$ 为 R198 scalar norm Robert 单位。
R185 的固定规范是
$$
d_0=\frac{i}{1848}\sum_{j=0}^{43}[u_j]\otimes D_{\omega^j}.
\tag{201.9}
$$
将 $1848^{-1}i\omega^j$ 两坐标取为 $0,\ldots,42$ 中的整数
$c_j,d_j$，置
$$
U=\prod u_j^{c_j},\qquad V=\prod u_j^{d_j}.
\tag{201.10}
$$
于是 $d_0=[U]\otimes F_0+[V]\otimes K_0$，
两个单位的模 $p$ 类都属所需 $W$ 型。

它们是普通全局 Norm：$p,2$ 处分裂；$q$ 的每个素点处 $d_0=0$
且 $W$ 平凡，所以两坐标各为局部 $p$ 次幂；其余处是不分歧扩张上的
单位 Norm。循环 Hasse Norm 定理及引理 201.2 给出
$$
X_U,X_V\in E_L^S,\qquad NX_U=U,\quad NX_V=V.
\tag{201.11}
$$
具体原像未求出。必须作同一 $C_{44}/\tau$ 投影才得到正确表示的
primitive，不能拿任意未平均的 $X_V$ 在一个点的值代替它。

## 5. 模 $p^2$ 根规范的实际修正

同一 Teichmüller 提升为
$$
\widehat\omega=352+197i\pmod{1849},\quad
\widehat\omega^{44}=1,\quad
\widehat\omega\overline{\widehat\omega}=1.
$$
例如 $352^2+197^2=88\cdot1849+1$。
$1848^{-1}=-1\pmod{1849}$，故高权为 $-i\widehat\omega^j$。
取两坐标标准整数 $C_j,D_j$，写
$C_j=c_j+43a_j,D_j=d_j+43b_j$，则
$$
U_2=UZ_U^{43},\quad V_2=VZ_V^{43},\quad
Z_U=\prod u_j^{a_j},\quad Z_V=\prod u_j^{b_j}.
\tag{201.12}
$$

在同一 $q$ 素点和 Weil 根 $\zeta$ 下，记
$$
m=(q^2-1)/43,\qquad\ell(z)=\log_\zeta(z^m).
$$
全部 $1848$ 个 $\psi_{11}$ 值重算给
$$
m\equiv21\pmod{43},\qquad\ell(Z_U)=0,\quad\ell(Z_V)=3.
\tag{201.13}
$$
$\ell$ 是幂剩余符号，不是 $\mu_{43}$ 分量的直接指数。
若 $Z=Z_m\zeta^t$、$Z_m^m=1$，则 $\ell(Z)=mt$；
因此 $Z_V$ 的 $\mu_{43}$ 指数为 $21^{-1}3=-6$。

$U,V$ 的 $\mu_m$ 规范 $43$ 根是
$$
\beta_U=U^e,\quad\beta_V=V^e,\qquad e=(1+2m)/43.
$$
程序核验 $e$ 整、根等式及 $\mu_m$ 条件。
$V_2$ 的规范根为 $\beta_V Z_{V,m}$；
除以 $Z_V=Z_{V,m}\zeta^{-6}$ 降回低权目标后，得到
$$
\boxed{(\beta_U,\ \beta_V\zeta^6)}.
\tag{201.14}
$$
程序也直接核验 $U_2,V_2$ 的规范 $p^2$ 根。
这是 tame/singular 坐标，没有未分歧二次 Frobenius 的除 $2$；
R198 有限坐标的因子不能沿用。

## 6. 唯一未知符号

在同一 $C_{44}/\tau$ 投影、$S$ 支撑及 R200 有限坐标归零规范后，
令 $t$ 表示低权根 $\beta_V$ 下正 Norm primitive 的 $K_0$ 坐标
$\mu_{43}$ 指数。它包含全部投影，不是未平均原像的单个值。
(201.14) 将它改为 $t-6$；
实际 $-2i\kappa_q$ 作用给 R200 的实奇异坐标
$$
v=2(t-6)=2t-12.
$$
定义 $\mathcal L=mt=21t$，则 $v=-4\mathcal L-12$。
R200 已处理 reference/cyclotomic 抵消与 $\eta$ 方程，
给 $\Omega_2^\epsilon=\epsilon(13+11v)$，故
$$
\boxed{\Omega_2^\epsilon=\epsilon(10-\mathcal L)}.
\tag{201.15}
$$
从而
$$
\Omega_2^\epsilon=0
\iff\mathcal L=10\iff t=23\iff v=34.
\tag{201.16}
$$
程序遍历 $t\in\mathbb F_{43}$ 核算这些代数等价。

$\mathcal L$ 仍未求值。R189 的 primal 局部值恰也为 $10$，
但不是这个 Norm 原像符号，不能混用。

## 7. 源、证书与引用

- [verify_r201_norm_target_gauge.js](../scripts/verify_r201_norm_target_gauge.js)
- [r201_norm_target_gauge_certificate.json](../notes/r201_norm_target_gauge_certificate.json)

~~~sh
node scripts/verify_r201_norm_target_gauge.js notes/r201_norm_target_gauge_certificate.json
~~~

程序内嵌输入，传 JSON 时逐项比较全部目标、根和 $44$ 行。
用 `--certificate <路径>` 可重新生成证书。实际输出：
~~~json
{"status":"PASS","psi11_evaluations":1848,"teich_omega":[352,197],
"power_logs_high_over_low":[0,3],"mu43_root_corrections":[0,6],
"target_mu_index":23,"target_power_residue_log":10,
"actual_norm_preimage_computed":false}
~~~

依赖 R161、R168、R171、R185、R191、R196、R198、R200。
循环 Hasse norm theorem：J. S. Milne, *Class Field Theory*,
Chapter VIII, Theorem 3.1, printed p.234：
<https://www.jmilne.org/math/CourseNotes/CFT.pdf>。
类群消失、支撑清除和返回普通代数数已在本文证明。
