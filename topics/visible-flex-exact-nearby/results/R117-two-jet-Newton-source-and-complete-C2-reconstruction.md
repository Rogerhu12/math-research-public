# R117：只有二阶几何 jet 的真实 Newton 源与完整 C² 重建

2026-11-13，visible-exact-astra-f6a2。

**已证明的完整降阶与重建结论。** 本篇把 R32/R37 的真实物理重建
改写成不要求当前几何三阶导数的形式。对当前严格星形 C² 图，
标量修正 $w\in C^2$、期望应变 $f\in C^1$，只要完整兼容残差
$h$ 连续，就能构造 C² 环境位移，并给明确范数。
当 $f$ 是固定目标度量与当前诱导度量之差时，$h$ 所用的 Newton 源
也有只含当前二阶几何、真实反坐标二阶 jet 和固定目标度量二阶 jet 的公式。

完整球面投影的 $C^0\to C^1$ 费用2048、兼容应变的
$C^1\to C^2$ 原函数费用6，以及接 R114 整帽修复后的费用均已支付；
28个 BigInt 有理门已实际通过。它们不是当前混合型标量逆、
所有高 Sobolev 档、材料角解析估计或非线性收敛的替代品。

## 1. 把 Hessian 项准确并回切向未知量

在当前真实球面坐标中写
$$
F(u)=\rho(u)^{-1}u,\qquad
B=\nabla^2\rho+\rho\sigma,\qquad \rho>0.
$$
R32 的变量满足
$$
\rho^2Dg_F[V]=\mathcal L_q\sigma+2wB,\qquad
V=\rho^{-1}(q+w\nabla\rho)+wu.
$$
定义新的实际切向未知量
$$
p=q+w\nabla\rho=\rho V^\top.
$$
因为
$\mathcal L_{w\nabla\rho}\sigma
=2w\nabla^2\rho+dw\otimes d\rho+d\rho\otimes dw$，
准确得到
$$
\boxed{
\rho^2Dg_F[V]
=\mathcal L_p\sigma+2\rho w\sigma
-dw\otimes d\rho-d\rho\otimes dw,\qquad
V=\rho^{-1}p+wu .
}                                                               \tag{117.1}
$$
于是定义
$$
E=\rho^2 f-2\rho w\sigma
+dw\otimes d\rho+d\rho\otimes dw .                     \tag{117.2}
$$
它属于 $C^1$，只需要 $\rho,w\in C^2$ 和 $f\in C^1$。
没有先分别估计 $q$ 与 $w\nabla\rho$ 的二阶导数再要求 $\rho\in C^3$；
那些三阶项在 (117.1) 中准确相消。

沿用
$$
\mathcal C T=\operatorname{div}\operatorname{div}T
-\Delta\operatorname{tr}T-\operatorname{tr}T,\qquad
\mathcal D_\rho w=\operatorname{cof}(B):\nabla^2w+
                                      (\operatorname{tr}B)w .
$$
按分布有
$$
\boxed{\quad h:=\mathcal CE
=\mathcal C(\rho^2f)+2\mathcal D_\rho w.\quad}           \tag{117.3}
$$
这是因为 $E$ 与 R37 的 $\rho^2f-2wB$ 差一个真实 Lie derivative。
本篇的重建假设是这个**完整** $h$ 为连续函数。
一般的任意 C¹ 张量 $f$ 不保证此条件；下文 §6 对真正 Newton 缺陷
给出连续二阶 jet 公式。只在分布中写一个源并不自动支付本条件。

## 2. 全局兼容 C¹ 应变的 C² 原函数，常数6

本节的 $C^k$ norm 是各阶球面协变导数 Hilbert–Schmidt 点范数
上确界的最大值。若实对称张量 $A\in C^1(S^2)$ 且
$\mathcal CA=0$，则存在切向 $p_A\in C^2$，满足
$$
\mathcal L_{p_A}\sigma=A,\qquad
\boxed{\ \|p_A\|_{C^2}\le6\|A\|_{C^1}\ }.              \tag{117.4}
$$
选择北极为基点，并令下述 ambient 旋转原函数在那里为零，
就给出一个确定的线性选择。

写 $e=A/2$、$Jv=u\times v$，
$\beta_i=\varepsilon^{jk}\nabla_j e_{ik}$，定义实际
$\mathbb R^3$ 值一形式
$$
\eta_i=J(e_i{}^\sharp)+\beta_i u .
$$
R71 的完整曲率交换恒等式为
$d\eta=-(\mathcal Ce)u\,dA_\sigma=0$。
连续且分布闭的形式在每个坐标盘上有 C¹ 原函数；
球面单连通，因此它们接成唯一的 $\Omega$，满足
$D\Omega=\eta,\ \Omega(\text{北极})=0$。
令 $p_A=\Omega\times u$、$\alpha=\Omega\cdot u$。
逐项投影得
$$
\nabla p_A=e+\alpha J,\qquad
d\alpha=\beta+(Jp_A)^\flat .                          \tag{117.5}
$$
后一闭合系统给 $p_A\in C^2$，无需 $A$ 的二阶导数。

置 $K=\|A\|_{C^1}$。有
$|\beta|\le\sqrt2\,|\nabla e|$，
$|D\Omega|\le\sqrt3 K/2<7K/8$。
从北极到任一点可取长度不超过 $\pi<22/7$ 的曲线，所以
$$
|\Omega|,\ |p_A|,\ |\alpha|<11K/4.
$$
由 (117.5) 和 $\nabla J=0$，
$$
|\nabla p_A|\le K/2+\sqrt2\,11K/4<37K/8,
$$
$$
|\nabla^2p_A|
\le|\nabla e|+\sqrt2\,|\beta+(Jp_A)^\flat|
\le3K/2+\sqrt2\,11K/4<45K/8<6K .
$$
这证明了 (117.4) 的全部档。

对保持北极的 D4，基点零值、$\eta$ 的 axial 变换律及叉乘
都等变，所以此选择保 D4。该群的不变 Killing 场只有零：
四分之一轴旋转只可能留下轴向旋转，角反射又将它取负。
因此若输入还保腰反射，输出亦保腰反射；反射后的两个解之差
为一个 D4 不变 Killing 场，必为零。
没有把不同帽上的两个刚体规范当作同一个全局规范。

## 3. 全球兼容投影真正从 C0 到 C1，常数2048

假设 $h\in C^0(S^2)$ 且与一次球谐正交。定义 R37 的同一算子
$$
T=\mathcal C^\dagger h
=\mathcal C^*[(\Delta+1)(\Delta+2)]^\dagger h,\qquad
\mathcal C^*\psi=\nabla^2\psi-(\Delta\psi+\psi)\sigma .
$$
本节证明
$$
\boxed{\qquad \|T\|_{C^1}\le2048\|h\|_\infty .\qquad}  \tag{117.6}
$$
常数模保留：$h_0$ 的输出为 $-h_0\sigma/2$，不是零。
(117.3) 的完整 $h$ 自动满足一次球谐正交，
因为 $\mathcal C^*Y_1=0$。

### 3.1 可积分的热核表示

置 $h_R=h-h_0$，它只含 $\ell\ge2$，并有
$\|h_R\|_\infty\le2\|h\|_\infty$、
$\|h_R\|_2\le\|h\|_2$。
对 $\lambda_\ell=\ell(\ell+1)$，
$$
\frac1{(\lambda_\ell-1)(\lambda_\ell-2)}
=\int_0^\infty(e^{2t}-e^t)e^{-\lambda_\ell t}\,dt .
$$
故在去掉均值的部分可写
$$
\psi_R=\int_0^\infty(e^{2t}-e^t)e^{t\Delta}h_R\,dt,\qquad
T=\mathcal C^*\psi_R-h_0\sigma/2.                     \tag{117.7}
$$

设 $L_i=\mathcal L_{\Omega_i}$ 作用于标量，$\Omega_i=e_i\times u$。
球面 Ricci 为正，Bochner 与热半群的方差恒等式给
$$
|\nabla e^{t\Delta}f|^2
\le\frac{e^{t\Delta}|f|^2-|e^{t\Delta}f|^2}{2t}
\le\frac{\|f\|_\infty^2}{2t}.
$$
例如对方差写
$2\int_0^t e^{s\Delta}|\nabla e^{(t-s)\Delta}f|^2ds$，
再用 Bochner 所给梯度收缩即可得到第一式。
$|\Omega_i|\le1$，且旋转导数与热半群交换，因此对任何有序指标串
$$
\|L_{i_1}\cdots L_{i_j}e^{t\Delta}f\|_\infty
\le\left(\frac j{2t}\right)^{j/2}\|f\|_\infty,
\quad j=1,2,3.                                      \tag{117.8}
$$
这是把时间分成 $j$ 等份依次使用一阶界，并非假设高阶热核估计。

大时间也需要实际衰减。球谐加法公式和 Cauchy–Schwarz 给
$$
\|e^{t\Delta}h_R\|_\infty
\le\left(\sum_{\ell\ge2}(2\ell+1)e^{-2\ell(\ell+1)t}\right)^{1/2}
 \|h\|_\infty .
$$
当 $t\ge1/2$，$\ell=2+n$ 时 $\ell(\ell+1)\ge6+6n$，
且 $e^{-12t}<1/64$，所以括号中的和小于
$$
e^{-12t}\left(\frac5{1-1/64}
+\frac{2/64}{(1-1/64)^2}\right)<9e^{-12t}.
$$
于是
$$
\|e^{t\Delta}h_R\|_\infty\le3e^{-6t}\|h\|_\infty .
\tag{117.9}
$$
对 $t\ge1$ 把时间分成两半，一半用 (117.9)，另一半用 (117.8)，
得到三阶以内的完整大时间界。

### 3.2 三个真实协变阶的具体费用

小时间 $0<t\le1$ 使用
$e^{2t}-e^t\le e^2t<8t$；大时间使用 $e^{2t}$ 和上述衰减。
逐项积分给
$$
\max_{i_1,\ldots,i_j}
\|L_{i_1}\cdots L_{i_j}\psi_R\|_\infty
\le M_j\|h\|_\infty,\qquad
(M_0,M_1,M_2,M_3)=(10,10,19,68).                     \tag{117.10}
$$
具体地，小时间四个上界为 $(8,8,16,60)$，
大时间为 $(3/2,3/2,3,63/8)$；$j=2$ 的合计严格小于19。
其中 $e^2<8$ 由完整正 Taylor 尾有理核算，$e>2$ 已由前三项给出。
因此 (117.7) 的积分可在旋转导数三阶以内一致求导；
它真正给 $\psi_R\in C^3$、$T\in C^1$，不是只给分布正则性。

还要付旋转架到协变导数的全部连接项。
记 $g=\nabla\psi_R$、$H=\nabla^2\psi_R$。
有
$$
\sum_i\Omega_i\otimes\Omega_i=\sigma,\qquad
\nabla_v\Omega_j=u_jJv,\qquad
|g|^2=\sum_i|L_i\psi_R|^2.
$$
所以
$$
|g|<35\|h\|_\infty/2,\qquad
|H|\le3M_2\|h\|_\infty+|g|
<149\|h\|_\infty/2.                                  \tag{117.11}
$$
第二式中的连接矩阵是
$u_j\langle J\Omega_i,g\rangle$，其 Hilbert–Schmidt norm 恰为 $|g|$。

三阶时，逐项微分得到
$$
\begin{aligned}
(\nabla H)(\Omega_i,\Omega_j,\Omega_k)
={}&L_iL_jL_k\psi_R-(L_i u_k)\langle J\Omega_j,g\rangle
+u_ku_jL_i\psi_R\\
&-u_kH(\Omega_i,J\Omega_j)
-u_jH(J\Omega_i,\Omega_k)
-u_kH(\Omega_j,J\Omega_i).
\end{aligned}                                                    \tag{117.12}
$$
三个 $H$ 项各自 norm 至多 $|H|$；前面的两个一阶项分别至多
$\sqrt2|g|$ 和 $|g|$，因为
$\sum_{i,k}|L_i u_k|^2=2$。
因此完整三阶费用小于
$$
3\sqrt3\,M_3\|h\|_\infty+(\sqrt2+1)|g|+3|H|
<\frac{2497}{4}\|h\|_\infty .                         \tag{117.13}
$$
最终 $|\Delta\psi_R|\le\sqrt2|H|$、
$|d\Delta\psi_R|\le\sqrt2|\nabla H|$，给
$$
|T|<\frac{957}{4}\|h\|_\infty<256\|h\|_\infty,\qquad
|\nabla T|<1899\|h\|_\infty<2048\|h\|_\infty .
$$
零次输出中已经加入 $-h_0\sigma/2$；其协变导数为零。
这完成 (117.6)，同时保留 R37 的 $\mathcal CT=h$ 与
$\operatorname{div}T=0$ 的真实分布恒等式。

## 4. 真实 C² 位移与完整残差

给定 §1 的 $\rho,w,f,h$，令 $T=\mathcal C^\dagger h$，
对 $A=E-T$ 使用 §2 得 $p=p_A$。
则
$$
\mathcal L_p\sigma=E-T,\qquad V=\rho^{-1}p+wu\in C^2,
$$
且由 (117.1) 准确得到
$$
\boxed{\quad Dg_F[V]-f=-\rho^{-2}T.\quad}               \tag{117.14}
$$
这是 R37 的同一个实际应变误差，变量改变不删任何项。

记
$$
A_\rho=\|\rho\|_{C^2},\quad B_\rho=\|\rho^{-1}\|_{C^2},\quad
F_1=\|f\|_{C^1},\quad W_2=\|w\|_{C^2},\quad H_0=\|h\|_\infty .
$$
从 (117.2) 的完整 Leibniz 公式，
$$
\|E\|_{C^1}\le3A_\rho^2F_1+10A_\rho W_2.
$$
$10$ 包括 $-2\rho w\sigma$ 的6和两个一形式乘积的4。
结合 §§2–3：
$$
\boxed{
\|p\|_{C^2}\le18A_\rho^2F_1+60A_\rho W_2+12288H_0 .
}                                                               \tag{117.15}
$$

物理位移 norm 使用球面连接于输入指标、ambient 平凡连接于输出。
切向场的 Gauss 公式给
$$
|Dp|\le|\nabla p|+|p|,\qquad
|D^2p|\le|\nabla^2p|+2|\nabla p|+\sqrt2|p|.
$$
把 $\rho^{-1}$ 的全部0、1、2阶乘法项保留，就有
$$
\|\rho^{-1}p\|_{C^2_{\rm amb}}
\le10B_\rho\|p\|_{C^2}.
$$
而 $Du$ 的 Hilbert–Schmidt norm 为 $\sqrt2$，
$D^2u=-u\sigma$，因此
$\|wu\|_{C^2_{\rm amb}}\le6W_2$。
最终
$$
\boxed{
\|V\|_{C^2_{\rm amb}}\le
10B_\rho(18A_\rho^2F_1+60A_\rho W_2+12288H_0)+6W_2 .
}                                                               \tag{117.16}
$$
此式只用当前几何二阶档。若还需从下界 $\rho\ge\rho_*>0$
计算 $B_\rho$，可用
$$
B_\rho\le\max\{\rho_*^{-1},\ A_\rho\rho_*^{-2},\
                 2A_\rho^2\rho_*^{-3}+A_\rho\rho_*^{-2}\}.
$$

## 5. 整个平帽继续准确保持，接 R114

若两个材料小帽在当前图中为平面、$f=0$ 于其上，
则原 $B=0$。因此 (117.3) 的 $h$ 在帽上为零，
$T$ 满足 R114 的局部兼容条件。
按 R114 构造支撑于固定大图的切向 $b$，
$$
\mathcal L_b\sigma=T\quad\text{在整个原小帽上},\qquad
\|b\|_{C^2}\le1024\|T\|_{C^1}\le2^{21}H_0 .
$$
改用 $p+b$，则 (117.14) 的残差改为
$-\rho^{-2}(T-\mathcal L_b\sigma)$，整个原帽上准确为零。
两个大图不交，max norm 不增加因子2。

如果真实强尾提供 $w=\lambda_\pm u_z$，平帽为 $z=h_\pm$，
该帽上的正确切向场为
$$
p_{\rm plane}=\frac{\lambda_\pm}{h_\pm}u_z\nabla u_z .
$$
直接代入 $\nabla^2u_z=-u_z\sigma$，它满足 (117.2) 的同一应变。
D4 对称性将两个解之差的局部 Killing 场消为零，所以
$$
\rho^{-1}(p+b)+wu=\lambda_\pm e_z
$$
在各自整个平帽上准确成立；故 $dV=0$，下一步平面度量不变。
没有通过两极零 jet 来代替开握持区。

包括整帽修复的简明界为
$$
\boxed{
\|p+b\|_{C^2}\le18A_\rho^2F_1+60A_\rho W_2+2^{22}H_0 ,
}                                                               \tag{117.17}
$$
以及把此右端放进 $10B_\rho(\cdot)+6W_2$ 的物理 C² 界。
$12288+2^{21}<2^{22}$ 已作有理核验。
R115 的 exact-tail chart 可供应强尾实现；它的实际两迹与主算子
仍必须正确联立，不能只用本地形式给任意标量源指定此尾。

## 6. 固定目标度量的 Newton 源也只有二阶几何

设固定材料流形上的目标度量为 $g_0\in C^2$。
在当前球面坐标中，令 $\chi:S^2\to M$ 为真实材料反坐标，
$$
e=\chi^*g_0,\qquad f=e-g_F .
$$
严格星形 C² 图的径向投影及其逆均 C²；
本节在实际使用的坐标图内作下面的 tensor 计算。
所有 norm 和目标正性仍须按当前几何实际计费。

### 6.1 任意二阶 pullback metric 的完整兼容式

令 $J_i=d\chi(e_i)$，
$B^\chi_{ij}=(\nabla d\chi)_{ij}$ 使用球面及目标的 Levi-Civita 连接，
$\tau=\sum_iB^\chi_{ii}$。这些量只用 $\chi$ 到二阶、$g_0$ 到一阶。
有
$$
\operatorname{div}e=\tfrac12d(\operatorname{tr}e)
                         +\langle J,\tau\rangle_{g_0}.
$$
Bochner 恒等式完整展开为
$$
\tfrac12\Delta|d\chi|^2
=|B^\chi|^2+\langle J,\nabla\tau\rangle
 +|J|^2-\sum_{i,j}\langle
 R^{g_0}(J_i,J_j)J_j,J_i\rangle .
$$
将两式代入 $\mathcal C$，
$\langle J,\nabla\tau\rangle$ 的所有三阶 $\chi$ 项准确抵消。
因目标为二维，得到
$$
\boxed{
\mathcal Ce=
|\tau|_{g_0}^2-|B^\chi|_{\sigma,g_0}^2
-2\operatorname{tr}_\sigma e
+2K_0(\chi)\det_\sigma e .
}                                                               \tag{117.18}
$$
例如恒等球面映射 $e=\sigma$ 给 $-2$，核对了曲率与零阶符号。
这不是只给 principal symbol；目标曲率项和球面 Ricci 项都保留。

再写
$$
Z_i=\langle J_i,\tau\rangle_{g_0}
-\sum_j\langle B^\chi_{ij},J_j\rangle_{g_0}.
$$
完整乘法恒等式为
$$
\mathcal C(se)=s\,\mathcal Ce+2\langle ds,Z\rangle
+\nabla^2s:e-(\Delta s)\operatorname{tr}e .
$$
取 $s=\rho^2$ 得
$$
\boxed{
\begin{aligned}
\mathcal C(\rho^2e)
={}&\rho^2\bigl(|\tau|^2-|B^\chi|^2-2\operatorname{tr}e
                       +2K_0(\chi)\det e\bigr)
+4\rho\langle d\rho,Z\rangle\\
&+(2\rho\nabla^2\rho+2d\rho\otimes d\rho):e
 -(2\rho\Delta\rho+2|d\rho|^2)\operatorname{tr}e .
\end{aligned}}                                                   \tag{117.19}
$$
所有量都在同一点和同一真实 map 上；不能在区间计算中先拆掉相关项。
公式先对光滑对象证明，再在 C² map / C² metric 中光滑逼近。
右侧连续且一致收敛，左侧分布收敛，所以它在所声明的有限正则性下
仍为准确连续代表。

### 6.2 当前诱导度量的准确消去

对真实环境缩放变分 $V=F$，有
$w=\rho^{-1}$、$q=-\rho^{-1}\nabla\rho$ 及 $Dg_F[F]=2g_F$。
R32 恒等式因此直接给
$$
\boxed{\quad
\mathcal C(\rho^2g_F)=-\mathcal D_\rho(\rho^{-1}).
\quad}                                                         \tag{117.20}
$$
右侧只用 $\rho$ 到二阶。结合 (117.19)，真正 Newton 标量源为
$$
\boxed{
-\tfrac12\mathcal C(\rho^2f)
=-\tfrac12\left[
       \mathcal C(\rho^2\chi^*g_0)+\mathcal D_\rho(\rho^{-1})
                         \right].
}                                                               \tag{117.21}
$$
它只含当前二阶几何、真实 $\chi$ 的二阶 jet 以及固定 $g_0$ 的二阶 jet。
这说明对真正 metric defect，不应先独立估计
$\partial^2(g_F)$ 中会出现的三阶 $F$ 再丢掉本来的消去。

(117.21) 付的是准确阶数与连续性，不是当前候选源的数值小量。
实际相关区间、坐标逆费用和整个径向 cover 仍须供应。
若目标度量随参数更新，须同时加入其真实参数导数与 Taylor 余项，
不能在一步完成后任意重选目标来删除尚未控制的非零模。

### 6.3 在材料坐标中保持小量相关项

(117.21) 的两个大项可以进一步准确合并，避免用大数相减去包一个小源。
以下给直接可供连续盒计算的版本。
在同一材料坐标 $(r,\theta)$ 中，令
$
\gamma=g_F,\quad s=U^*\sigma,\quad f=g_0-\gamma,\quad U=F/|F|,
$
并把球面所有收缩用 $s$ 表示。设
$
B_F{}^k_{ij}=\Gamma_\gamma{}^k_{ij}-\Gamma_s{}^k_{ij},\quad
D^k_{ij}=\Gamma_0{}^k_{ij}-\Gamma_\gamma{}^k_{ij},\quad
\tau_F^k=s^{ij}B_F{}^k_{ij},\quad \delta\tau^k=s^{ij}D^k_{ij}.
$
这是 §6.1 对恒等材料映射的两个真实目标连接。
差张量的准确式为
$
D^k_{ij}
=\tfrac12(g_0^{-1})^{k\ell}
(\nabla^\gamma_i f_{j\ell}+\nabla^\gamma_j f_{i\ell}
                                  -\nabla^\gamma_\ell f_{ij}),
\tag{117.22}
$
因此它只需要小缺陷 $f$ 的一阶导数，不需要把两套大连接分别取绝对值。

置
$
\begin{aligned}
Q={}&f(\tau_F,\tau_F)+2g_0(\tau_F,\delta\tau)
                        +g_0(\delta\tau,\delta\tau)\\
&-s^{ia}s^{jb}\{f(B_{F,ij},B_{F,ab})
 +2g_0(B_{F,ij},D_{ab})+g_0(D_{ij},D_{ab})\},\\
Z_i={}&f_{ik}\tau_F^k+(g_0)_{ik}\delta\tau^k
 -s^{jl}\{f_{k\ell}B_F{}^k_{ij}+(g_0)_{k\ell}D^k_{ij}\}.
\end{aligned}
$
这里 $Z$ 是两个 (117.19) 中一阶交叉向量的**差**。
令 $G=\det\gamma$，并使用 R113 同一几何的
$\Delta=(K_\gamma-K_0)G^2$。
二维准确恒等式给
$
d_G:=\det g_0-G=\operatorname{cof}(\gamma):f+\det f,\qquad
K_0\det g_0-K_\gamma G=K_0d_G-\Delta/G.
$
于是 (117.18)–(117.19) 的差准确为
$
\boxed{
\begin{aligned}
\mathcal C_s(\rho^2f)
={}&\rho^2\left[
 Q-2\operatorname{tr}_s f+
 \frac{2(K_0d_G-\Delta/G)}{\det s}\right]
 +4\rho\,s^{ij}\rho_i Z_j\\
&+(2\rho\nabla_s^2\rho+2d\rho\otimes d\rho):_s f\\
&-(2\rho\Delta_s\rho+2|d\rho|_s^2)\operatorname{tr}_s f .
\end{aligned}}                                                   \tag{117.23}
$
$\mathcal C_s$ 是同一个球面兼容算子在真实材料坐标中的表达，
不是目标 $g_0$ 的兼容算子。
每个右端项都显式带 $f$、$\nabla^\gamma f$ 或相关曲率分子 $\Delta$。
完整非线性二次交叉项已经写出，没有以线性近似替代恒等式。

所有背景量仍只需当前 $F$ 到二阶。例如
$
s_{ij}=\langle U_i,U_j\rangle,\qquad
\Gamma_s{}^k_{ij}=s^{k\ell}\langle U_\ell,U_{ij}\rangle,\qquad
\Gamma_\gamma{}^k_{ij}=\gamma^{k\ell}\langle F_\ell,F_{ij}\rangle .
$
R113 还给 $\det s=S^2/T^3>0$；
这里 $S=(F_\theta\times F_r)\cdot F$、$T=|F|^2$，
不能与本节的 metric $s$ 混同。
故 (117.23) 可直接复用完整 primitive/Fourier 的0–2阶数据、
真实度量缺陷的0–1阶数据和同一相关 $\Delta$。
这是真实 Newton **源**的二阶路线；
尚须对它进行实际全角、整参数、连续径向认证，不能把公式本身称为小量已付。

## 7. 接回固定型别误差与材料 C²

若仍用 R37 的准确修正算子
$\widehat{\mathcal D}=\mathcal D_\rho+\mathcal E$ 解
$$
\widehat{\mathcal D}w=-\tfrac12\mathcal C(\rho^2f)+r_{\rm sc},
$$
则 (117.3) 精确成为
$$
h=2(r_{\rm sc}-\mathcal Ew).
$$
从而 (117.14) 正是 R37 的完整应变残差公式。
在材料圆柱中 $\mathcal E$ 仍为实际
$j_u^{-1}Q_\ell^*(\chi\omega)Q_\ell$；
其强 C0 计算保留全部角导数、ground state、密度和 cutoff。
本篇不把它的弱 $H^{-1}$ 界自动换成 C0，也不将普通源删去。
R113 的相关 $\Delta$ 公式和这里的两 jet 消去可以同时使用。

从球面回到固定材料坐标亦有实际费用。
若当前径向投影 $U:M\to S^2$ 的
$\|dU\|_{\rm op}\le L_1$、
$\|\nabla dU\|_{\rm HS}\le L_2$，
链式法则给
$$
\|V\circ U\|_{C^2(M;\mathbb R^3)}
\le\max(1,L_1,L_1^2+L_2)\|V\|_{C^2_{\rm amb}(S^2)} .
$$
这些数必须来自同一当前背景/邻域；不得默认为1。

因此本篇消除了完整物理 C² 重建中的额外径向三阶几何要求，
并给真实 Newton 源的二阶表示。
它没有证明完整标量解 $w$ 已在所需邻域取得 C² / 强角范数，
没有支付材料角解析性或所有高 Sobolev 的投影/整帽延拓费用，
也没有从一次更新的恒等式推断迭代必收敛。
完整强逆、源的数值大小、相应尺度与累计几何预算继续按 open.md 推进。

## 8. 实际有理核与重放

源码 scripts/fourfold_two_jet_C2_reconstruction_exact.mjs，
完整报告 notes/2026-11-13-R117-two-jet-C2-reconstruction.json。
相同纯 BigInt 核已在 V8 实际通过28门；
native CLI 尚未执行，报告明确分开。

源码 SHA256：
16975a1506584d7557de586472aa1d32c801089e3261d587869d70677019def1。

报告 SHA256：
4c914377a7f5b0b06bac6a7f40cb3571928d6914a067caf93a65b26d620c22e5。

~~~sh
node scripts/fourfold_two_jet_C2_reconstruction_exact.mjs \
 --out notes/2026-11-13-R117-two-jet-C2-reconstruction-replayed.json
~~~

这些门核的是本篇已经完整证明的普适常数。
它们没有输入一个尚未求得的非线性解，也不把源码存在当成候选数值证书。
