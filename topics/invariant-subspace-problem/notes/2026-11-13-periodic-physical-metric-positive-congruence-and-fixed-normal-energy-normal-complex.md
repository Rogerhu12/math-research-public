# 周期物理度量：实际相似、正正常态合同与固定态的准确费用

- 日期：2026-11-13（UTC）
- 作者：AI 辅助研究；normal_complex
- 性质：已证明的工作补充；root 已独立全文核验全空间权、正常态合同与准确指数。供联合源继续使用，不另声称新的核范围或 ISP 结论

本稿接
[联合高幂与 carry 修正目标](2026-11-13-joint-gauge-row-powers-and-carry-corrected-targets-normal-complex.md)
使用的对角度量。全部定义在原 Haar 空间
$H=L^2(\mathbb Z_2,\mu)$。
它是物理二进位柱上的乘法度量，不是 Walsh 占据热权；
不将两种加权表示混同。

## 1. 周期延拓及完整算子范数

令 $H_m=2^m$，
$$
\lambda_m=(100+2^{-m/2})8^{m-1},\qquad
\rho_m=e^{-\lambda_m},
$$
$$
F_m(k)=\lambda_mk+\log W_k
\quad(0\le k<H_m),\qquad F_{*,m}=F_m(H_m-1).
$$
原 bit 权恒等式给
$$
0\le F_m(k)\le F_{*,m},\qquad
F_{*,m}=(35/6+o(1))16^m.
\tag{1.1}
$$
定义全空间的实际正乘法单位
$$
(D_mf)(y)=
\exp\!\left[F_m(y\bmod H_m)-F_{*,m}/2\right]f(y).
\tag{1.2}
$$
每个 $D_m,D_m^{-1}$ 都有界，且
$$
\|D_m\|=\|D_m^{-1}\|=e^{F_{*,m}/2}.
\tag{1.3}
$$
这里不宣称关于 $m$ 一致有界。

原加权 odometer 为
$$
(Af)(y)=\omega(y)f(y-1),\qquad
\omega(y)=\alpha_{v_2(y)}
$$
（单点 $y=0$ 的取值不影响算子）。
准确权递推是
$$
W_{k+1}/W_k=\alpha_{v_2(k+1)},\qquad
W_{H_m-1}=d_m/\alpha_m.
$$
因此对 $k=y\bmod H_m<H_m-1$，
$D_mA^*D_m^{-1}$ 的权恰为 $\rho_m$。
在边界 $k=H_m-1$，若 $v_2(y+1)=m+j$，其权恰为
$$
\rho_m\chi_m\frac{\alpha_{m+j}}{\alpha_m},
\qquad \chi_m=d_m\rho_m^{-H_m}.
\tag{1.4}
$$
$\alpha_j$ 严格递减，而 $\chi_m<1$ 对大 $m$ 成立。
故得到全空间的准确范数，而非仅有限头上界：
$$
\boxed{
A_m^\flat=D_m^{-1}AD_m,\qquad
\|A_m^\flat\|=\rho_m.
}
\tag{1.5}
$$
等号来自全部非边界柱上的恒定权 $\rho_m$。

每个 $j\ge m$ 的 $N_j=A^{2^j}/d_j$ 平移量是 $H_m$ 的倍数，
所以周期乘法准确交换：
$$
\boxed{
[D_m,N_j]=[D_m,Q_j]=0\quad(j\ge m).
}
\tag{1.6}
$$
因而这些高行在 (1.5) 的相似下完全不变；
没有以纯 $E_j$ 替代实际 $N_j$。

若 $f$ 在 $|z|\le\rho_m$ 附近解析，则由收缩解析函数演算
$$
\|f(A_m^\flat)\|\le\sup_{|z|=\rho_m}|f(z)|.
\tag{1.7}
$$
特别，真正固定的零常数解析行在这个表示中变小。
对于本次低行 $f_m(z)=z^rg_m(z)$，已有圆估计给
$$
\|f_m(A_m^\flat)\|\le2|t_r|\rho_m^r,\qquad
\|g_m(A_m^\flat)^{-1}\|\le2/|t_r|.
\tag{1.8}
$$
这些是全空间的真实解析函数演算。

(1.6) 与 (1.8) 可以同时使用。
但不能将包括所有高行的慢标量形式级数当成在该圆上解析的函数：
高行保持不变，不意味着其形式标量函数在该圆内没有极点。

## 2. 原反射与双线性配对准确保留

原反射共轭为
$$
(Cf)(y)=\overline{f(-1-y)}.
$$
由于二进位补集，
$$
W_{H_m-1-k}=W_{H_m-1}/W_k,
$$
从而
$$
F_m(H_m-1-k)=F_{*,m}-F_m(k).
$$
这给
$$
\boxed{CD_mC=D_m^{-1}.}
\tag{2.1}
$$
所以原双线性配对满足
$$
B(D_mf,D_mg)=B(f,g).
\tag{2.2}
$$

若 $R$ 对原 $C$ 对称，则
$$
R_m^\flat=D_m^{-1}RD_m
$$
仍对同一个 $C$ 对称：
$$
CR_m^\flat C
=D_mR^*D_m^{-1}=(R_m^\flat)^*.
\tag{2.3}
$$
新交换子代数是准确相似像
$$
\{A_m^\flat\}'=D_m^{-1}A'D_m.
$$
固定 dyadic gauge 的乘法酉 $U_\zeta$ 与 $D_m$ 交换，
因此同一个 gauge 在新表示中仍满足
$$
U_\zeta A_m^\flat U_\zeta^*=\zeta A_m^\flat.
$$
没有新增无限相位可实施性的假设。

## 3. 正密度必须作双侧合同，湮灭行也随之改变

固定正迹类 $\rho\ne0$，记 $\tau=\operatorname{Tr}\rho$。
定义
$$
\rho_m^\flat=D_m^{-1}\rho D_m^{-1}\ge0,\qquad
R_m^\flat=D_m^{-1}RD_m.
\tag{3.1}
$$
对任意有界行 $S$，准确有
$$
\boxed{
\operatorname{Tr}\left[
\rho_m^\flat(D_mSD_m)R_m^\flat
\right]=\operatorname{Tr}(\rho SR).
}
\tag{3.2}
$$
因此原条件 $\varphi_\rho(SA')=0$ 变为
$$
\operatorname{Tr}\rho_m^\flat
\left[D_m^2 S_m^\flat R_m^\flat\right]=0
\quad(R_m^\flat\in\{A_m^\flat\}').
\tag{3.3}
$$
左行是 $D_m^2S_m^\flat$，不是未经权重的 $S_m^\flat$。
它一般不属于新的交换子代数。
这是保正合同的准确代价。

若只作相似密度 $D_m^{-1}\rho D_m$，确可保持普通行
$S_m^\flat$ 的配对，但该密度一般不正；不能同时免费得到两者。

真核条件与纯湮灭条件不同。
若
$$
T\rho^{1/2}=0,
$$
则
$$
T_m^\flat(\rho_m^\flat)^{1/2}=0.
\tag{3.4}
$$
例如由
$T_m^\flat\rho_m^\flat(T_m^\flat)^*
=D_m^{-1}T\rho T^*D_m^{-1}=0$
即可得到它。
所以同一个合同密度仍支撑于真实相似核，
但另一条正常湮灭行须保留 (3.3) 的左权。

原单位锚也变成
$$
\operatorname{Tr}(\rho_m^\flat D_m^2)=\tau,
\tag{3.5}
$$
不是自动变成 $\operatorname{Tr}\rho_m^\flat=\tau$。
下一节定量说明这个差别不能由固定正常性消去。

## 4. 每个固定正正常态都支付完整的四次主型

**命题。** 对任意固定非零正迹类 $\rho$，准确有
$$
\boxed{
\lim_{m\to\infty}16^{-m}
\log\frac{\operatorname{Tr}(\rho D_m^{2})}{\tau}
=
\lim_{m\to\infty}16^{-m}
\log\frac{\operatorname{Tr}(\rho D_m^{-2})}{\tau}
=\frac{35}{6}.
}
\tag{4.1}
$$
$\rho$ 必须固定；此结论不针对随 $m$ 自适应变化的密度。

给出完整证明。写
$$
F_m(k)=\sum_{j<m}\varepsilon_j(k)t_{m,j},
\qquad
t_{m,j}=\lambda_m2^j-\Lambda_j\ge0,\quad
\Lambda_j=-\log d_j.
$$
固定整数 $K\ge1$，选取远处的 $K$ 个位
$$
I_{m,K}=\{m-K-1,\ldots,m-2\}.
$$
令 $P_{m,K}^+$ 与 $P_{m,K}^-$ 分别为这些位全部为一、全部为零的
实际乘法投影。
它们都满足
$$
P_{m,K}^{\pm}\longrightarrow2^{-K}I
\quad\mathrm{WOT}.
\tag{4.2}
$$
确实，对两个固定有限柱，待这些位移至支撑之后，内积准确分解；
统一投影范数再延拓到全部向量。
正规性因此给
$$
\operatorname{Tr}(\rho P_{m,K}^{\pm})
\longrightarrow2^{-K}\tau>0.
\tag{4.3}
$$

把未选择的最高位及较低位总贡献记为
$$
R_{m,K}=t_{m,m-1}+\sum_{j=0}^{m-K-2}t_{m,j}.
$$
最高位的四次主项恰相消，故 $t_{m,m-1}=o(16^m)$。
其余项用 $t_{m,j}\le\lambda_m2^j$ 得到
$$
\limsup_m16^{-m}R_{m,K}
\le\frac{25}{4}\,2^{-K}.
\tag{4.4}
$$
在 $P_{m,K}^+$ 上，
$F_m\ge F_{*,m}-R_{m,K}$；
在 $P_{m,K}^-$ 上，
$F_m\le R_{m,K}$。
由 (1.2)，
$$
D_m^2\ge e^{F_{*,m}-2R_{m,K}}P_{m,K}^+,\qquad
D_m^{-2}\ge e^{F_{*,m}-2R_{m,K}}P_{m,K}^-.
$$
同时 $D_m^{\pm2}\le e^{F_{*,m}}I$。
取正态期望，使用 (4.3)，再除以 $16^m$，得到两个极限的下界
$$
\frac{35}{6}-\frac{25}{2}\,2^{-K}
$$
和上界 $35/6$。
先令 $m\to\infty$，然后令固定整数 $K\to\infty$，
便得 (4.1)。没有让正常性替代任何随 $m$ 变化的无界测试极限。

特别，固定 $h\ne0$ 时，
$$
16^{-m}\log\frac{\|D_m^{\pm1}h\|}{\|h\|}
\longrightarrow\frac{35}{12}.
\tag{4.5}
$$
以及固定 $\rho$ 的两侧 Cauchy--Schwarz 能量
$$
\mathcal E_m(\rho)=
\left[
\operatorname{Tr}(\rho D_m^2)
\operatorname{Tr}(\rho D_m^{-2})
\right]^{1/2}
$$
满足
$$
16^{-m}\log\frac{\mathcal E_m(\rho)}{\tau}
\longrightarrow\frac{35}{6}.
\tag{4.6}
$$
它在四次主型上达到这套相似的完整条件数。
这不排除其他度量、其他原像或实际相消，只说明不能仅凭
$\rho$ 固定且正常就把本套能量的主指数降掉。

若将 (3.1) 的正密度归一化为
$$
\sigma_m^\flat=
\frac{\rho_m^\flat}{\operatorname{Tr}\rho_m^\flat},
$$
则原单位锚的期望准确为
$$
\operatorname{Tr}(\sigma_m^\flat D_m^2)
=\frac{\tau}{\operatorname{Tr}(\rho D_m^{-2})}.
$$
由 (4.1)，它的对数除以 $16^m$ 趋于 $-35/6$。
因此“先相似使低行很小，再保持正态归一化”的操作，
必须同时保留这一锚费用。

## 5. 当前可用接口

周期度量提供的是全空间实际恒等式：
低解析函数可按 $\rho_m$ 估计，高行 $N_j$ 对 $j\ge m$ 保持不变，
同一个 $C$ 与 gauge 也保留。
在纯源的矩阵估计中可以只付一次条件数，
这正是联合高幂稿的改进。

若改用正密度，则应采用 (3.2)--(3.5) 的双侧合同与加权行。
原慢行不能因相似后低解析部分变小，就被宣布具有同一正正常
湮灭者的普通小行模型。真核、加权湮灭及单位锚三者须同时保留。

本工作补充没有给出新的临界联合源上界，也没有关闭普通 ISP。
