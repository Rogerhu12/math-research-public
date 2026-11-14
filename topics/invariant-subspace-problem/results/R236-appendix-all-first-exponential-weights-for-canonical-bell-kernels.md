# R236 附录：规范 Bell 核的全部 first 指数权与二次循环性

日期：2026-11-13（UTC）。独占作者：central_next。
状态：已证明；依赖已登记的对称高位平均原 Haar 证明，
本稿单独付清指数倾斜产生的全部常数、主项、闭尾域与局部可除性。
本稿只关闭明确的指数加权核接口；普通 Hilbert ISP 仍未完成。

## 1. 定理及准确加权接口

在实际 Haar 空间 H=L²(Z₂) 上，取规范行
$$
a_j=\frac{(-1)^j}{j+1},\qquad a_*=0,\qquad
u=\sum_{j\ge0}a_j\chi_j .
$$
令
$$
w=c_*+\sum_{j\ge0}b_j\chi_j,\qquad b\in\ell^2(\mathbb C),
\qquad \xi_w=e^w,
$$
并记
$$
t_j=e^{-2b_j},\qquad
R_j=V(t_jN_j)=\frac{I-t_jN_j}{I+t_jN_j}.
\tag{1.1}
$$
R176 §10 给真实闭倾斜 first
$$
X_b=X+H_{a,b},\qquad
H_{a,b}=\sum_j a_j(R_j-V_j)\in\mathcal A,
\qquad \operatorname{Dom}X_b=\operatorname{Dom}X,
\tag{1.2}
$$
其中和按范数绝对收敛。置
$$
B_b=\sum_j a_j^2(I-R_j^2)\in\mathcal A.
\tag{1.3}
$$
每项字符为零，故 B_b 拟幂零。
对零点邻域上任一固定全纯函数 phi，定义
$$
Y_b=\phi(B_b),\qquad T_b=X_b-Y_b .
\tag{1.4}
$$

**定理。**
$$
\boxed{\ker T_b=\{0\}.}
\tag{1.5}
$$
特别，
$$
\boxed{(u^2-1)e^w\text{ 对实际 }A\text{ 循环，任意复 }\ell^2
\text{ first 指数权 }w.}
\tag{1.6}
$$
这里 b 固定后允许常数依赖 b；不要求 b 的任何定量尾速率。

以下只使用原 Haar 的有限局部矩阵与强极限，没有运输未知边界子空间。

## 2. 全部倾斜分母有统一真实界

因为 b_j→0，所以 t_j→1 且每个 t_j 非零。固定
$$
L=\max\left(1,\sup_j|t_j|,\sup_j|t_j|^{-1}\right)<\infty .
\tag{2.1}
$$
实际 N_j 满足
$$
\|N_j\|=1,\qquad N_j^2=\eta_jN_{j+1},\qquad
\eta_j\le\bar\eta_j=e^{-770\,16^j}.
$$
充分高位上 L²η_j≤1/2，因而
$$
(I\pm t_jN_j)^{-1}
=(I\mp t_jN_j)(I-t_j^2N_j^2)^{-1}
$$
的范数至多 2(1+L)。
有限个低位的 I±t_jN_j 因 N_j 拟幂零而分别真实可逆。
所以存在
$$
R=\sup_{j,\ s=\pm1}\|(I+s t_jN_j)^{-1}\|<\infty.
\tag{2.2}
$$
置
$$
V=2R+1,\qquad C_V=2LR^2 .
\tag{2.3}
$$
则 ||V(s t_jN_j)||≤V。
有理逆差恒等式同时给
$$
\|V(t_j\gamma(N_j))-V(s t_jN_j)\|
\le C_V\|\gamma(N_j)-sN_j\|
\tag{2.4}
$$
对任意物理有限反射 gamma 成立。
第一分母由酉共轭保持 (2.2)，第二分母由 s=±1 支付。

这些常数没有把无界点态乘 e^w 当作有界相似。

## 3. 真实高位 gauge、统一预解式及主项

取
$$
m=\lceil e^{r^2}\rceil,\qquad q=r^4,\qquad
I_r=\{m,\dots,m+q-1\},\qquad \ell=m+q-1 .
$$
对 |F|=r、F⊂I_r，置 J_F=∏_{j∈F}M_{χ_j}、
gamma_F(Q)=J_FQJ_F；s_j=-1 当 j∈F，否则为 1。

原模型递归本身、不依赖 b，给
$$
\|\gamma_F(N_k)-s_kN_k\|\le
\begin{cases}
2\alpha_m/\alpha_k,&k<m,\\
2\eta_k,&m\le k\le\ell,\\
0,&k>\ell .
\end{cases}
\tag{3.1}
$$
窗口内未选的位置也保留在第二行中。
若 k 被选中，差等于
η_k E_k^*(N_{k+1}−gamma_F(N_{k+1}))；
若未选中，则为相反次序的同类差。
故求和可用 Σ_{k≥m}barη_k≤2barη_m，不需随 q 增长的常数。

定义
$$
\widehat X_F=X_b+
 \sum_{j\in F}a_j\bigl(V(-t_jN_j)-V(t_jN_j)\bigr),
$$
$$
\widehat B_F=B_b+
 \sum_{j\in F}a_j^2\bigl(V(t_jN_j)^2-V(-t_jN_j)^2\bigr),
\qquad
\widehat Y_F=\phi(\widehat B_F),
$$
$$
A_F=(\widehat X_F-\widehat Y_F)-T_b,\qquad
E_F=\gamma_F(T_b)-(\widehat X_F-\widehat Y_F).
\tag{3.2}
$$
A_F 有界、属于 Acal，与 T_b 完整域交换。

固定位于 phi 全纯邻域内的圆 Gamma={|z|=rho}，令
$$
R_\Gamma=\max_\Gamma\|(z-B_b)^{-1}\|,\qquad
C_\Gamma=2\rho\max_\Gamma|\phi(z)|R_\Gamma^2 .
\tag{3.3}
$$
当 m 足够大，L²barη_m≤1/4。准确恒等式
$$
V(-z)-V(z)=4z(I-z^2)^{-1},
$$
$$
V(-z)^2-V(z)^2=8z(I+z^2)(I-z^2)^{-2}
\tag{3.4}
$$
于是给
$$
\|\widehat B_F-B_b\|\le\frac{32Lr}{(m+1)^2}\longrightarrow0 .
\tag{3.5}
$$
充分大 r 时，全部 widehat B_F 在 Gamma 上的真实预解式统一至多 2R_Gamma；
gamma_F(B_b) 的预解式则恰保 R_Gamma。
因此全部实际函数差可用同一个 C_Gamma 乘对应自变量差。

利用 (3.1)、(2.4)，并用
$$
\sum_{k<m}|a_k|\frac{\alpha_m}{\alpha_k}<2\bar\eta_{m-1},
\qquad
\sum_{k<m}|a_k|^2\frac{\alpha_m}{\alpha_k}<2\bar\eta_{m-1},
$$
可取
$$
\|\gamma_F(X_b)-\widehat X_F\|\le8C_V\bar\eta_{m-1},
$$
$$
\|\gamma_F(B_b)-\widehat B_F\|\le16VC_V\bar\eta_{m-1}.
$$
故
$$
\boxed{
\|E_F\|\le C_E\bar\eta_{m-1},\qquad
C_E=8C_V+16VC_VC_\Gamma .
}
\tag{3.6}
$$

定义归一化所需的准确线性主项
$$
P_F=4\sum_{j\in F}a_jt_jN_j,\qquad
C_A=8L^3+32LC_\Gamma,\qquad K=4L+1 .
\tag{3.7}
$$
(3.4) 的第一式减去 4t_jN_j，范数误差至多
8L³η_j。充分大 m 时 (m+1)barη_m≤1，从而
$$
\boxed{
\|A_F-P_F\|\le\frac{C_Ar}{(m+1)^2},\qquad
\|P_F\|\le\frac{4Lr}{m+1},\qquad
\|A_F\|\le\frac{Kr}{m+1}.
}
\tag{3.8}
$$
最后一个界只需再取 m+1≥C_A。
全部常数固定于 b、phi，独立于 r、F。

## 4. 完整尾域及自然幂

R125 的有限柱空间是 X 的图核心，(1.2) 是有界扰动，所以它也是 X_b 的图核心。
令
$$
X_{b,>\ell}=X_b-\sum_{j\le\ell}a_jR_j .
$$
它有同一个完整域。核心上的有限尾截断只作用大于 ell 的物理位；
其真实极限由 R125 及 (1.2) 的范数收敛给出。
因此任何固定前 ell+1 位局部矩阵 L_0 都满足
$$
L_0\operatorname{Dom}X_{b,>\ell}\subseteq\operatorname{Dom}X_{b,>\ell},
\qquad
X_{b,>\ell}L_0=L_0X_{b,>\ell}
$$
于完整域上：先在有限柱核心交换，再用 L_0 有界及闭性。
特别 J_F 双向保域。

所有 Acal 元素保持这个域，并与 X_{b,>ell} 交换：它们与 X 完整交换，
与有界倾斜项、有限头项也交换。
E_F 是有限个 gamma_F(R_k)−V(s_kt_kN_k) 的和，
再加 gamma_F(Y_b)−widehat Y_F。
由这个具体表达，E_F 保持同一完整域，并与 X_{b,>ell} 完整交换。

置
$$
D_\ell^{\rm bd}=\sum_{j\le\ell}a_jR_j-Y_b,\qquad
d_r=2\|D_\ell^{\rm bd}\|
\le2V(1+\log(m+q))+2\|Y_b\|=O_{b,\phi}(r^2).
$$
于是
$$
\operatorname{ad}_{T_b}^sE_F
=\operatorname{ad}_{D_\ell^{\rm bd}}^sE_F,\qquad
\|\operatorname{ad}_{T_b}^sE_F\|\le d_r^sC_E\bar\eta_{m-1}.
\tag{4.1}
$$
全部右侧都保持完整一阶域。

设 M_b=kerT_b、f∈M_b、v=J_Ff。则 T_bv=−(A_F+E_F)v。
通过
$$
Q_0=I,\qquad
Q_{n+1}=\operatorname{ad}_{T_b}(Q_n)-Q_n(A_F+E_F)
$$
逐次得 v∈DomT_b^n、T_b^nv=Q_nv。
A_F 权1、ad^s E_F 权 s+1 的同一非交换计数给
$$
\boxed{
\|T_b^rJ_Ff-(-A_F)^rJ_Ff\|
\le(r+1)!C_E\bar\eta_{m-1}
(1+\|A_F\|+d_r)^r\|f\|.
}
\tag{4.2}
$$
系数绝对值总和最多 (r+1)!，且除 (−A_F)^r 外每个单词都含至少一个误差因子。
这给所有 F 的真实自然幂域，不是只给形式 Taylor 公式。

## 5. 改正输入权后，主项仍是同一个强平均

关键是同时把 t_j 纳入输入分母，不能只令 t_j→1 而要求未知尾速率。
记
$$
p_{F,b}=\prod_{j\in F}(a_jt_j),\qquad
\mathcal B_{r,b}=
\frac1{(-2q)^r}\sum_{\substack{F\subset I_r\\|F|=r}}
p_{F,b}^{-1}J_F .
\tag{5.1}
$$
全部 p 非零，并且
$$
S_{r,b}:=\frac1{(2q)^r}\sum_F|p_{F,b}|^{-1}
\le\frac{L^r(m+q)^r}{2^rr!},
\qquad
\boxed{\|\mathcal B_{r,b}\|\le\frac{L^re^{r^3}}{r!}.}
\tag{5.2}
$$
后一式对充分大 r 成立。

置 R_r=1+Kr/(m+1)+d_r=O(r²)。
按 (4.2) 求和，第一项误差最多
$$
(r+1)C_E\bar\eta_{m-1}
 \left(\frac{L(m+q)R_r}{2}\right)^r\|f\|
 \longrightarrow0 .
\tag{5.3}
$$
正对数成本 O(r³+r log r)，被真实 carry 超指数吸收。

利用 (3.8) 逐因子替换 A_F 为 P_F，再乘 (5.2)，完整误差最多
$$
\frac{C_Ar}{K(m+1)}
\left(\frac{KLe}{2}\right)^r e^{rq/m}\|f\|
\longrightarrow0 .
\tag{5.4}
$$
这里 m=e^{r²}+O(1)，且 rq/m=r⁵/m→0。
这是保留 ||A_F||=O_b(r/m) 后的幂估计。

P_F^r 中全部指标不同的项恰是
$$
4^r r!p_{F,b}\prod_{j\in F}N_j .
$$
其它项含某个 N_j²=η_jN_{j+1}，所以原始重复项误差至多
$$
4^r\bar\eta_m\left(\frac{Lr}{m+1}\right)^r .
$$
乘 S_(r,b) 后不超过
$$
\bar\eta_m(2eL^2)^r e^{rq/m}\longrightarrow0 .
\tag{5.5}
$$
而 ||(∏_F N_j)J_F−∏_F E_j||≤rbarη_m。
因为 p_(F,b) 已准确消去，最后替换的全部系数绝对值仍不超过 2^r，
误差仍为
$$
2^rr\bar\eta_m\longrightarrow0 .
\tag{5.6}
$$

故与未倾斜稿完全同一个物理平均
$$
C_{m,q}=\frac2q\sum_{j=m}^{m+q-1}E_j
$$
满足
$$
\boxed{
\|T_b^r\mathcal B_{r,b}f-C_{m,q}^rf\|
\le\epsilon_{r,b}\|f\|,\qquad
\epsilon_{r,b}\to0,\quad f\in M_b .
}
\tag{5.7}
$$
每个输出属于真实 RanT_b^r。

实际 Haar 上 ||C_(m,q)||≤1+1/q。
有限柱 v 在 m 以上为真空，故
||(C_(m,q)−I)v||=q^(−1/2)||v||，
进而
$$
\|(C_{m,q}^r-I)v\|
\le\frac r{\sqrt q}(1+1/q)^{r-1}\|v\|\to0 .
$$
同时 ||C_(m,q)^r||≤e，有限柱稠密，得到全 H 上强极限。
因此
$$
\boxed{T_b^r\mathcal B_{r,b}f\longrightarrow f
\quad(f\in M_b).}
\tag{5.8}
$$
本论证完全没有使用 b_j 在窗口上以任何指定速度趋零。

## 6. 倾斜后的局部差仍能真实有界除 A

固定任意局部矩阵 D，支撑在第 h 位以前。
令
$$
B_{b,\ge h}=\sum_{j\ge h}a_j^2(I-R_j^2),\qquad
Y_{b,\ge h}=\phi(B_{b,\ge h}),
$$
$$
Z_h=X_{b,\ge h}-Y_{b,\ge h}
+\left(\sum_{j<h}a_j\right)I,
$$
$$
K_h=\sum_{j<h}a_j(R_j-I)-(Y_b-Y_{b,\ge h}).
\tag{6.1}
$$
T_b=Z_h+K_h 于同一个完整域上成立。
Z_h 是真实尾算子，故 D 完整交换并保持其域；
K_h∈Acal 保域且与 Z_h 完整交换。

与未倾斜情形相比，除 A 的明确因子只是多了 t_j：
$$
\sum_{j<h}a_j(R_j-I)=A U_h^{(1)},\qquad
U_h^{(1)}=-2\sum_{j<h}\frac{a_jt_j}{d_j}
 A^{2^j-1}(I+t_jN_j)^{-1},
$$
$$
B_b-B_{b,\ge h}=A U_h^{(2)},\qquad
U_h^{(2)}=4\sum_{j<h}\frac{a_j^2t_j}{d_j}
 A^{2^j-1}(I+t_jN_j)^{-2}.
\tag{6.2}
$$
两者为有限的真实有界 Acal 和。
真实轮廓差商给
$$
Y_b-Y_{b,\ge h}=(B_b-B_{b,\ge h})L_h,
$$
$$
L_h=\frac1{2\pi i}\int_\Gamma
\phi(z)(z-B_b)^{-1}(z-B_{b,\ge h})^{-1}\,dz\in\mathcal A .
\tag{6.3}
$$
h 固定时所有预解式常数有限，不要求一致于 h。
因此
$$
\boxed{K_h=A U_h,\qquad U_h=U_h^{(1)}-U_h^{(2)}L_h\in\mathcal A.}
\tag{6.4}
$$

因为 D、K_h 与 Z_h 完整交换，
ad_(T_b)^r D=ad_(K_h)^rD，且每个嵌套交换子有界并保持原完整域。
实际幂界
$$
\|A^n\|\le e^{-(100/15)n^4+105n^3}
$$
与 K_h=A U_h 给
$$
\boxed{
\|\operatorname{ad}_{T_b}^rD\|
\le\|D\|(2\|U_h\|)^r
 e^{-(5/6)r^4+105r^3}.
}
\tag{6.5}
$$
证明为展开 Σ_s(−1)^s binom(r,s)K_h^(r−s)DK_h^s，
用 s⁴+(r−s)⁴≥r⁴/8 和 s³+(r−s)³≤r³。

完整高阶域也由同一嵌套族付清：
若 D_k=ad_(T_b)^kD，则每个 D_k 保持 DomT_b^n，并有
$$
T_b^nD_kx=\sum_{s=0}^n\binom nsD_{k+s}T_b^{n-s}x,
\qquad x\in\operatorname{Dom}T_b^n .
\tag{6.6}
$$
这是先在完整一阶域使用 [T_b,D_k]=D_(k+1)，然后逐自然幂归纳的等式。

## 7. 最高交换子配对，及局部代数排核

T_b 是真实 C 自伴：X_b 由 R176 已付清，Y_b 是有界 Acal 元素。
以实际双线性型 B(u,v)=<u,Cv> 配对。
对 f,g∈M_b 与 u_r=mathcal B_(r,b)f∈DomT_b^r，
完整 Leibniz 及 (6.6) 给
$$
B(DT_b^r\mathcal B_{r,b}f,g)
=(-1)^r B((\operatorname{ad}_{T_b}^rD)\mathcal B_{r,b}f,g).
\tag{7.1}
$$
全部低阶项有正次 T_b 移到 g 后为零。
右端范数至多
$$
\frac{\|D\|(2L\|U_h\|)^r}{r!}
 e^{-(5/6)r^4+106r^3}\|f\|\|g\|
\longrightarrow0 .
\tag{7.2}
$$
左端由 (5.8) 趋于 B(Df,g)，故 B(Df,g)=0。

原 Haar 的有限局部 *-代数不可约：
前 h 位真空投影强趋于参考向量 1 的秩一投影；
任意与局部代数交换的投影因此在 1 上是 0 或 I，
局部代数作用于 1 稠密，再得该投影是 0 或 I。
故每个非零 f 的局部代数轨道线性张成稠密。
取 g=f，若 f≠0，上述配对迫 Cf 正交于稠密轨道，矛盾。
因此 M_b=0，得到 (1.5)。

## 8. 指数加权危险平方循环性

分别取 phi(z)=±sqrt(1−z)。
两个真实分支 X_b−sqrt(I−B_b)、X_b+sqrt(I−B_b) 均无核。
平方根是有界 Acal 单位并保持全部 X_b 自然幂域。
因此
$$
P_b=X_b^2+B_b-I
$$
在 DomX_b² 上的核为零。
明确地，若 P_bx=0，则 y=(X_b+sqrt(I−B_b))x∈DomX_b；
第一分支杀 y，故 y=0；再由第二分支单射，得 x=0。

R176 §10 给
$$
\xi_w\in\bigcap_n\operatorname{Dom}X_b^n,\qquad
P_b\xi_w=(u^2-1)e^w,
$$
并证明 xi_w 循环、P_b 在准确自然域上 C 自伴，
以及
$$
[(u^2-1)e^w]_A=\overline{\operatorname{Ran}P_b}.
$$
单射与 C 自伴给右侧等于 H，完成 (1.6)。


### 8.1 任意非零二次多项式的全部 first 指数权

对固定规范 $u$、任意复 $\ell^2$ first 指数权 $w$，任意非零次数至多二的 $q$ 都满足 $q(u)e^w$ 循环。

写 $q(z)=c_2(z^2+\alpha z+\beta)$，$c_2\ne0$，并置 $\Delta=\alpha^2/4-\beta$。若 $\Delta\ne0$，取零点附近的全纯函数
$
\phi_\pm(z)=-\alpha/2\pm\sqrt{\Delta-z}.
$
本稿定理给 $X_b-\phi_\pm(B_b)$ 单射。其自然乘积恰为 $X_b^2+\alpha X_b+B_b+\beta I$，域为 $\operatorname{Dom}X_b^2$；两个有界系数与 $X_b$ 完整交换，故乘积也单射。R176 (10.15) 的准确加权图范围识别遂给 $q(u)e^w$ 循环。

若 $\Delta=0$，则 $q(u)e^w=c_2(u+\alpha/2)^2e^w$，由 [R147 §1、§9](../results/R147-exponential-weighted-first-mode-polynomial-cyclicity.md) 的全部指数加权点态幂直接得循环性。一次情形和非零常数也由 R147 的相应结论处理。这里引用的是明确带任意复 first 指数权的 R147，而非把不加权 R144 免费延伸。

这里完成的是规范行及任意 first 指数权的全部非零二次及更低次数多项式。
没有由此推出任意高次点态多项式、全部复 ell² 行的所有 Bell 分支、
一般正常湮灭者、边界 N=M 或完整普通 ISP。
