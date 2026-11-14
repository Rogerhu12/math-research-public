# R66：准确参数族的正侧领口、自然权 C4 外接段与真实径向入口

2026-11-12，independent_audit。

**状态：已证明的实际参数族与实际外接段结论。** 本篇对当前同一准确
仿射族，统一支付每个参数自己的真实转折至 \(r=1/4\) 的正环带，
并从其真实 \(r=3\) 四阶数据构造到 \(r=25/8\) 的 \(C^4\) 外接段。
后者准确变成径向指数段，给出真正可用的 R11/R22 接尾入口。
所有角向估计涵盖真无限单位切向原函数，包含均值及完整源和两个端口。

外接段是明确的近似等距对象；度量缺陷及其导数有下述有向界。
本文没有把它称为闭精确等距族，也没有把极小半径的单个外接帽称为
已经满足题目尺寸要求的固定握持区。完整真实平尾、上下两帽的相对
刚体条件，以及主课题的有限幅非线性修正仍须在同一对象上完成。

## 1. 准确参数与对象身份

取

\[
 \delta_c=-\frac{7789866024620307}{4611686018427387904},
 \qquad |\delta-\delta_c|\le\frac1{2000000}.
 \tag{66.1}
\]

该盒包含已保存的 \(\delta_5\)；它是已经支付 beta 相位导数的
\(\Delta_5=\delta_3+[-10^{-5},10^{-5}]\) 的子区间。
准确中心对象是
[step4 object](../data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_object.json)，
SHA256 为

    87566dee6e119bb4127200c2dae38f9cdf692a18475c1cde23961a56605919b5

其 origin 和 direction 的 SHA256 依次为

    0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b
    8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab

参数先作用于准确原始多项式，再形成完整的物理 scalar germ。所有入口
数据都是这些同一参数函数的值；区间包络不是给每个系数重新引入互不
相关的自由参数。半径 \(a\) 与 beta 径向偶对称，gamma 与准确高度
\(Z\) 奇对称；两相位在角向都是 \(\sin(4k\theta)\) 的有限和。

实际曲面始终按 [R33](R33-exact-unit-tangent-retraction.md) 定义：

\[
 T=(-\cos\gamma\sin\beta,\cos\gamma\cos\beta,\sin\gamma),\qquad
 F=a\mathcal P_\theta T+Ze_z,\qquad F_\theta=aT.
 \tag{66.2}
\]

分量使用旋转柱坐标基，\(\mathcal P_\theta\) 是完整笛卡尔原函数在该
基下的准确算子。目标度量是
\[
 g_0=E(r)\,dr^2+a(r)^2\,d\theta^2,\qquad
 E=\langle |F_r|^2\rangle_\theta .
 \tag{66.3}
\]
不会用有限 Parseval 和代替此定义。

## 2. 同一族的真实移动根正领口

保存的
[参数根管](../notes/2026-11-12-beta-step3-germ-root-h1e5.json)
已证明整个 \(\Delta_5\) 上各自唯一的简单根 \(t(\delta)\)，且

\[
 .2383968723385157<t(\delta)<.2383968751209642.
 \tag{66.4}
\]

本次程序核对 origin、direction、根管源码及全部依赖 SHA，并以准确
Fraction 比较 (66.1) 与 \(\Delta_5\) 的包含关系后，才调用该结论。
用于计算的 binary64 根外包络向外舍入并再次严格检查。

在根外包络左端至其右端加 \(1/4096\) 的短区间，支付 \(K_0'>0\)。
由准确等式 \(K_0(t(\delta))=0\)，得到这一段
\(K_0/(r-t(\delta))\) 的界；根以后各段直接认证 \(K_0>0\) 并使用
同一个根包络。比真根略靠内的区间仅用于共同的导数与几何包络，不被
称为正区。所有正负反射 knots 都按准确 Fraction 分割；55 个闭 cell
完整覆盖，没有失败或待处理区间。

完整公式、ground state、角流和源转换均是
[R64](R64-actual-positive-collar-source-and-dn-input.md) 的同一公式。
计算只是将输入从一个准确点替换为 (66.1) 的真实共同 germ，故其证明
逐参数成立且常数统一。实际可取：

| 量 | 对整个 (66.1) 有效的严格安全界 |
|---|---:|
| \(K_0/(r-t)\) | \(14.331<K_0/(r-t)<115.481\) |
| 角流 \(J,J^{-1}\) | \(<1.277\) |
| \(A_0=\operatorname{diag}(1,r-t)\) 的归一正矩阵 | \(0.02475I<C<45.349I\) |
| trace 平方常数 | \(<1902852\) |
| 延拓平方常数 | \(<345\) |
| 零 Dirichlet 逆 | \(<40.389\) |
| 完整 Poisson 与完整 \(V^*\) contact | \(<34025\) |
| 完整 DN | \(<15634\) |
| \(L^2H^{-2/3}\) 到两个完整 contact | \(<5864895\) |
| 物理 \(L^2\) 源到新密度 \(L^2\) 源 | \(<0.299\) |

根端 trace 是 \(H^{1/3}\)，普通端是 \(H^{1/2}\)。在同一真实通量
frame，带正负角权 \(|s|\le2^{-75}\) 的完整归一 Robin 逆 norm
不超过2，Cayley norm 不超过5。两个端口的 cross 和共同常数核均保留。

本节原始证书为
[family collar](../notes/2026-11-12-positive-family-root-collar.json)，
SHA256

    f796e89e61f45ffba22c2aa2ab145a40ec4a80fe39abe30bc797dc0b06b966cc

恢复后已从头重算55个 cell；没有拼接丢失运行的 partial 数据。

## 3. 真实 r=3 数据与自然权外接公式

从真实最后共同 spline span 左侧取 \(r=3\) 的完整 Taylor 系数。
记 \(s=r-3\)、\(\ell=1/8\)，以及

\[
 l_j=[s^j]\log a(3+s),\quad
 c_j=[s^j]\frac{Z'(3+s)}{a(3+s)^2},
\quad
 B_{jk}=[s^j]\frac{\beta_k(3+s)}{a(3+s)^3},\quad
 G_{jk}=[s^j]\frac{\gamma_k(3+s)}{a(3+s)^2}.
 \tag{66.5}
\]

这里系数已除以 \(j!\)。程序先完整计算物理加权 scalar germ，
再作商与对数，不能对四舍五入后的物理导出值求导。
原始入口报告
[entry jets](../notes/2026-11-12-positive-family-exterior-entry-jets.json)
的 SHA256 是

    6748eb485a77031a3f50caccea5111d913e58aa32ac428e30a7689354cfd8f26

取准确多项式

\[
 \chi(u)=(1-u)^5(1+5u+15u^2+35u^3+70u^4)
 =1-126u^5+420u^6-540u^7+315u^8-70u^9 .
 \tag{66.6}
\]

它满足 \(\chi'=-630u^4(1-u)^4\)，故 \(0\le\chi\le1\)，且在两端
分别与1和0匹配至四阶。定义真实外接段：

\[
\begin{aligned}
 \log a_e(s)&=l_0+l_1s+\chi(s/\ell)\sum_{j=2}^4l_js^j,\\
 c_e(s)&=c_0+\chi(s/\ell)\sum_{j=1}^3c_js^j,\\
 Z_e(s)&=Z(3)+\int_0^s a_e(v)^2c_e(v)\,dv,\\
 \beta_{e,k}(s)&=a_e(s)^3\chi(s/\ell)\sum_{j=0}^4B_{jk}s^j,\\
 \gamma_{e,k}(s)&=a_e(s)^2\chi(s/\ell)\sum_{j=0}^4G_{jk}s^j .
\end{aligned}
 \tag{66.7}
\]

这些是每个真实 \(\delta\) 的准确函数定义。区间程序包住其所有系数及
运算；并未用各系数中点重新定义近似对象。

在 \(s=0\)，半径及两相位匹配四阶。\(c_e\) 匹配三阶且
\(Z_e'=a_e^2c_e\)，所以高度也匹配四阶。原函数算子与径向求导交换，
因而整个 \(F\) 匹配四阶。在 \(s=\ell\)，相位及其前四阶径向导数
准确为0；\(\log a_e=l_0+l_1s\)、\(c_e=c_0\) 的相应 jets
也准确匹配。故此处可接

\[
 a_e(s)=\exp(l_0+l_1s),\qquad Z_e'=c_0a_e^2,\qquad
 \beta_e=\gamma_e=0\qquad(s\ge\ell),
 \tag{66.8}
\]

得到真实 \(C^4\) 外延。保留 \(a^3,a^2\) 权重使相位与正在缩小的半径
同阶衰减；不能在物理相位上任意截断后仍借用这些比值界。

整个高度积分以准确正积分定义；程序用
\[
 a_{\rm glob}=\exp\!\left(l_0+l_1[0,\ell]
       +[-R_l,R_l]\right),\quad R_l=\sum_{j=2}^4|l_j|\ell^j,
 \qquad
 c_{\rm glob}=c_0+[-R_c,R_c],\ R_c=\sum_{j=1}^3|c_j|\ell^j
\]
包住 \(a_e,c_e\)，并付
\(|Z_e-Z(3)|\le\ell a_{\rm glob}^2c_{\rm glob}\)。
这些有向门同时给 \(a_e>0,c_e>0,(\log a_e)'<0,Z_e>0\)。

## 4. 真无限角向估计与度量缺陷

使用物理 Fourier Wiener norm
\(\|v\|_\sigma=\sum_n|v_n|e^{\sigma|n|}\)，\(\sigma=1/32\)；
实际相位频率是 \(n=4k\)，不是 \(k\)。
对水平旋转分量，原函数乘子为

\[
 (inI+J)^{-1}=\frac1{1-n^2}
 \begin{pmatrix}in&1\\-1&in\end{pmatrix},\qquad
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
 \tag{66.9}
\]

在 \(n\in4\mathbb Z\setminus\{0\}\) 上，其列和 norm 为
\((|n|-1)^{-1}\le1/3\)；\(n=0\) 的 norm 为1。竖直零均值
原函数 norm 不超过 \(1/4\)。因 \(\beta,\gamma\) 角向奇，
\(\sin\gamma\) 的均值准确为0；水平零模保留，未删去真实平均半径修正。

固定每个径向闭 cell，用形式变量 \(z\) 记录其真实径向 Taylor 系数
的非负上界。令 \(B(z),G(z)\) 分别 majorize 两相位的上述 Wiener
norm，\(L(z),R(z)\) 分别 majorize
\((\log a_e)'\)、\(a_ec_e\)。所有后述式子按非负系数解释。置

\[
\begin{aligned}
 d_x&=\cosh G\,\sinh B,&d_y&=\cosh G\cosh B-1,&d_z&=\sinh G,\\
 d_h&=d_x+d_y,&H&=Ld_h+d_h',&V&=(Ld_z+d_z')/4 .
\end{aligned}
 \tag{66.10}
\]

三分量真切向差由 \(d_x,d_y,d_z\) 控制，真原函数及径向导数由
(66.9) 控制。因此若
\[
 F_r/a=L_{\rm true}e_r+a_ec_e e_z+\Delta X/a,
\]
则水平两分量 Wiener norm 之和不超过 \(H\)，竖直分量不超过 \(V\)。
均值径向分量准确由 \(\langle\cos\gamma\cos\beta-1\rangle\) 产生，
竖直均值准确为0。所以在
\[
 E=a_e^2\big(L_{\rm true}^2+a_e^2c_e^2+\epsilon\big)
 \tag{66.11}
\]
中，\(\epsilon\) 及其径向 Taylor 系数由
\[
 \mathcal E=2L(Ld_y+d_y')+H^2+V^2
 \tag{66.12}
\]
控制。这个二次均值结构是真恒等式的后果，不能换成关于 beta 的线性
粗误差后继续除以 \(a_e^2\)。

另一方面，对目标 (66.3)，准确有 \(e_{\theta\theta}=0\)，且相对
\(a_e^2\) 的两个其余缺陷分量由
\[
 \mathcal Q=Ld_x+Rd_z+H\cosh G\,e^B+Vd_z,\qquad
 \mathcal D=4(LH+RV)+2(H^2+V^2)
 \tag{66.13}
\]
控制。第一式直接展开 \(F_r\cdot F_\theta/a_e^2\)；第二式从
\(|F_r|^2-\langle|F_r|^2\rangle\) 得到，每个非恒定项及其均值各付一次。
乘以 \(a_e^2\) 的绝对 Taylor majorant 得物理缺陷。

若 \(j=r+q\le2\)，由
\(|n|^q\le q!\sigma^{-q}e^{\sigma|n|}\) 得混合物理导数界
\[
 |\partial_r^r\partial_\theta^q e_{ij}|
 \le r!q!\sigma^{-q}
       \max\{[z^r](a_e^2\mathcal Q),[z^r](a_e^2\mathcal D)\}.
 \tag{66.14}
\]
所有矩阵分量和全部混合导数都在此界内。实际64个闭 cell 全部通过，
得到整个 (66.1)、\(3\le r\le25/8\)、完整实角圈上的安全界

| 缺陷 norm | 有向安全上界 |
|---|---:|
| 物理 \(C^0\) | \(1.654\times10^{-30}\) |
| 物理一阶导数最大值 | \(9.299\times10^{-29}\) |
| 物理二阶导数最大值 | \(7.047\times10^{-27}\) |
| 相对 \(a_e^2\) 的 \(C^0\) | \(9.415\times10^{-21}\) |
| 相对 \(a_e^2\) 的一阶导数最大值 | \(4.237\times10^{-19}\) |
| 相对 \(a_e^2\) 的二阶导数最大值 | \(3.009\times10^{-17}\) |

没有角节点抽样，也没有有限 Fourier 截断尾：整个解析切向函数由
Wiener 代数的指数、双曲函数级数直接控制。

## 5. 真目标曲率与几何分母

写 \(L=(\log a_e)'\)、\(L'= (\log a_e)''\)。由 (66.11)，准确恒等式为

\[
 K_0=
 \frac{c_e[c_e(L^2-L')+Lc_e']+
                  (L\epsilon'-2L'\epsilon)/(2a_e^2)}
 {(L^2+a_e^2c_e^2+\epsilon)^2}.
 \tag{66.15}
\]

证明是将 \(a'=aL,a''=a(L^2+L')\)、
\(E=a^2(L^2+a^2c^2+\epsilon)\) 代入
\(K_0=(a'E'-2a''E)/(2aE^2)\) 并准确约去项。
源码先对 \(\epsilon,\epsilon'\) 加入 (66.12) 的区间费用，再形成此
分式；没有先形成易消去的大项差。所有分母严格正。实际得到

\[
 0.0289657051<K_0<0.0294790813,\qquad
 -5.624<L<-5.617,\qquad .961680<c_e<.961690.
 \tag{66.16}
\]

完整 \(F,F_r\) 以 (66.9)–(66.10) 的真原函数界包络，再使用 R64
的真实 frame。记其 \(\mathcal D,\mathcal M,\mathcal W,\mathcal H\)
如 R64(64.5)，则本次64个 cell 同时在实域及物理
\(|\operatorname{Im}\theta|\le1/32\) 支付
\(\operatorname{Re}\mathcal D>0\)、
\(\operatorname{Re}\mathcal H>0\)、\(\operatorname{Re}F_z>0\)。
实域另有 \(|F|^2>0,\mathcal W>0\)。例如整个外接段的严格安全界是

\[
 \mathcal D>4.1429\,10^{-11},\quad
 \mathcal H>3.5645\,10^{-5},\quad
 Y_z>0.9999999993 .
 \tag{66.17}
\]

因此与实际 beta 口径相同的 R37 修正及 \(Y_z\) ground state 合法。
该选择不能不加说明地变为精确度量导数；两者差仍由 R37 的真实
metric defect 系数计入非线性误差。

## 6. 外接段的完整正源与两个普通端口

R64 的准确消元给
\[
 B=\begin{pmatrix}\alpha&\alpha b\\
 \alpha b&\alpha b^2+\eta K_0\end{pmatrix},\quad
 \alpha=\frac{F_z^2\mathcal D}{\mathcal H^2},\quad
 \eta=\frac{F_z^2\mathcal W^2}{\mathcal D\mathcal H^2},\quad
 b=-\mathcal M/\mathcal D .
 \tag{66.18}
\]
解真实角流 \(\Theta_s=b(3+s,\Theta)\)、\(\Theta(0,\phi)=\phi\)。
若 \(I_r=\int\sup|b_\theta|\,ds\)，则 \(J,J^{-1}\le e^{I_r}\)，
拉回矩阵准确为
\(\widetilde B=\operatorname{diag}(J\alpha,\eta K_0/J)\)。
源码按64个准确 cell 的长度逐项积分漂移上界，不用无依据的平均值。
实际
\[
 I_r<1.723\,10^{-11},\quad I_c<2.761\,10^{-11},\qquad
 .029747I<\widetilde B<1.012444I .
 \tag{66.19}
\]

此处两个端口均普通。取
\[
 \|U\|_V^2=\int_0^\ell\!\!\int(|U_s|^2+|U_\phi|^2+|U|^2),\qquad
 \mathcal T=H^{1/2}\oplus H^{1/2}.
 \tag{66.20}
\]
在角频 \(n=\langle k\rangle\) 上令 \(d=\min(\ell/2,1/n)\)。
一维 endpoint 估计
\[
 |u(0)|^2\le(2/d)\int_0^d|u|^2+2d\int_0^d|u'|^2
\]
乘以 \(n\)，用两端互不重叠的区间，给平方 trace 常数
\[
 C_{\rm tr}=2\max(1,2/\ell).
\]
对端点值取长度 \(d\) 的线性 tent，能量为
\((d^{-1}+n^2d/3)|u(0)|^2\)，给平方延拓常数
\[
 C_E=\max(1,2/\ell)+1/3=49/3.
 \tag{66.21}
\]
零 trace Poincaré 给 \(g=(1+\ell^2/\pi^2)/m\)。R35 的同一正 form
从而定义完整 Dirichlet 逆、Poisson、DN 和完整 \(V^*\) source
contact，并给
\[
 \|\mathcal H\|,\|\mathcal K\|\le\sqrt{C_E}(1+Mg)<141.807,
 \qquad\|\Lambda\|\le MC_E<16.537,\quad g<33.670.
 \tag{66.22}
\]
因为 \(\|U\|_{L^2H^1}\le\|U\|_V\)，同一完整 contact 满足
\[
 \mathcal K:L^2_sH^{-1}_\phi\longrightarrow
 H^{-1/2}\oplus H^{-1/2},\qquad \|\mathcal K\|<141.807 .
 \tag{66.23}
\]
保留共同常数核、两个端口 cross 和
\(\langle\mathcal Kf,(1,1)\rangle=-\langle f,1\rangle\)。
只有 \(V_{00}^*\) 源限制不能定义完整边界 charge。

物理密度源准确变为 \(-JY_z f\circ\Theta\)；其 \(L^2\) 转移 norm
小于 \(1.000000001\)。动量先作
\(Y_zp_w-wp_{Y_z}\)，再作边界对偶角密度换元。
带负阶源的声明 (66.23) 使用这些明确最终变量，不免费转授未计费的
原坐标复合 norm。

复角流首次出管论证给宽
\(\rho_*=\sigma/(2e^{I_c})>0.01562499999\)，其真实复系数 norm
小于1.013485。于是 R35 的有向 Fourier moment 和 DN 交换公式给
\[
 N_C<33210,\qquad C_\Lambda<304389,\qquad
 |s|\le 2^{-35}<4.9462\,10^{-11}
 \tag{66.24}
\]
满足全部实际加权门。归一边界
\(Q_\partial=\operatorname{diag}(\langle D\rangle^{1/2},
\langle D\rangle^{1/2})\)，在相同 ground-state frame 取 shear0，
完整带 signed 权 Robin 逆 norm 不超过2，Cayley norm 不超过5。
这两个数没有删去均值，也没有仅在有限频率检查。

## 7. 真实径向入口及持握区边界

在 \(r_e=25/8\)，准确有
\[
 a_*=\exp(l_0+l_1\ell),\quad
 Z_*=Z(3)+\int_0^\ell a_e^2c_e\,ds,\quad
 c_*=c_0,\quad \beta=\gamma=0\text{ 至四阶}.
 \tag{66.25}
\]
实际 \(6.5637\,10^{-6}<a_*<6.5639\,10^{-6}\)、
\(.966198669<Z_*<.966198672\)。
令
\[
 u=4c_0(r-r_e),\qquad h=1/a,\qquad
 \omega=h_u/h=-l_1/(4c_0).
 \tag{66.26}
\]
则准确 \(z_u=a^2/4\)、\(\omega_u=0\)，而
\[
 1.46115285<\omega<1.46115287,\qquad q=\omega_u/\omega^2=0.
 \tag{66.27}
\]
因此 R11 的真实入口盒和 R22 的物理高度归一都满足；不是套用另一
背景的 \(u=4x\) 常数。其自由稳定第四模满足
\(y_u=-4\omega y\)，所以 \(R=y_u/(16\omega y)=-1/4\) 准确。
这只是此径向段的一条真实齐次方向，不把当前非径向核心的未知解
宣布为该方向。

径向指数段的两主曲率为
\[
 \kappa_\theta=\frac{c_0}{\sqrt{l_1^2+c_0^2a^2}},\qquad
 \kappa_s=\frac{c_0l_1^2}{(l_1^2+c_0^2a^2)^{3/2}},
\]
故均小于 \(0.171098\)。真正 R72 connector 及平尾仍需按 (66.26)
作同一高度与两条迹的匹配；全非线性尾输出的高模、mean 和 source
不能删去。当前 \(\delta\) 族的约束只用于构造和选择一个适合核心
相位的对象，不等同于最终公共度量弯曲族的参数。

题目要求 \(\operatorname{diam}F_0(H)\ge0.2D\)。一个半径仅
\(a_*\) 量级的单帽不满足这一尺寸要求。若将两端真正平尾固定区的并
作为 \(H\)，须另证它们的整体尺寸并满足两帽相对 Killing 条件；
一个全局旋转规范不能分别固定两帽。当前结果也没有将两端固定区的
存在误认为有限幅 \(\delta_{\rm hold}\ge0.05D\) 或 reach 已完成。

## 8. 重放、冻结与尚未覆盖的外段

领口由
[uniform collar source](../scripts/fourfold_phase_positive_family_collar.py)
及稳定曲率源重放。外接段由
[natural graft source](../scripts/fourfold_phase_natural_exterior_graft.py)
重放，输出
[graft report](../notes/2026-11-12-positive-family-natural-graft.json)。
入口源与报告、两份领口/外接报告以及完整依赖 SHA 都由随篇 ready
manifest 登记。读取有向上下端点，不使用展示用浮点中点。

~~~bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_natural_exterior_graft.py \
  --center-object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_object.json \
  --half-width 1/2000000 --length 1/8 --angle-strip 1/32 --cells 64 \
  --bits 192 --out /workspace/scratch/f6a2c7886477/graft-replay.json
~~~

本文 §§2、3–7 已完成的实际范围分别是
\([t(\delta),1/4]\) 与 \([3,25/8]\)，后者具有准确径向继续公式。
原始有限 body 的 \([1/4,3]\) 连续覆盖另由稳定曲率程序处理；
在其完整证书登记前，本篇不将两个已付区间之间的空档声明为全域
DN 或全帽。所有接合后的普通源、mean、cross 和相对刚体条件继续
属于同一个全局问题。
