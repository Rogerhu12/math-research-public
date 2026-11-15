# R133：真实 long 外口的两层有限 Sobolev 估计与完整 Poisson 源

2026-11-15，visible-exact-astra-0df9。

**解析证明；完整 Fourier 核、真实 adjoint、物理源单位及有限常数已独立核对。** 本篇将真实 long 图的低阶小量和高阶正则分开。
未知背景只在明确的低范数中小；高范数可以有限而不小。
角阶最高为8160，背景使用至8192阶（高度另保其真实两个角导）。
所有公式在同一实际物理角中，保完整频率、真正曲率反馈、holonomy mean、
未匹配外口、两端高度与独立荷。原度量和真实有限长度固定。

基本工具是零宽 Banach 全纯解图的完整 Fourier Taylor 核。
它不要求未知背景角解析，不在未知函数上作复角平移；
所有复变量只是 Banach 空间的数据参数。
本篇也不直接宣布整个 mixed 网络的 tame inverse 或 nonlinear 迭代。

依赖
[J完整有限角 true long](R133-supplement-finite-angular-jet-true-long-DN-Poisson-and-energy.md)、
[E完整未匹配外口恒等式](R133-supplement-extended-finite-jet-outer-commutator-window.md)、
[N原完整物理源](R119-supplement-actual-long-screening-complete-Sobolev-DN-and-cap-facing-port.md)、
[S真正加权 long 筛选](R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md)。
这里只用它们的零宽方程、真实解析数据依赖和完整正 majorant，不复算旧数值。

## 1. 范数、明确域与两个不同的背景预算

在原完整4Z上使用归一化圆周测度。A表示零宽Wiener代数，
Lambda(n)=(1+n²)^(1/2)，a_n=max(1,|n|)；非mean输入的|D|取|n|。
原固定量为
$$
 z_a=33/10^{11},\qquad r_B=2^{-60},\qquad r_f=10^{-8},
 \qquad \epsilon=e^{-7L/4}<2^{-33554432},\qquad s_B=a_Bw_B .
 \tag{K.1}
$$
Z=(C_R-C_r)_perp是实际物理曲率，f=f_B是long归一化非mean高度，
V_T=(P_T,U_T,K_T,V_T)表示短侧的完整四态（最后一个分量沿用原名）。
K_T含真正holonomy mean。以下写该四态为boldsymbol V_T以免与势混淆。

要求
$$
 \xi=\left(Z/z_a,\ |D|^2f/r_B,\ 64\boldsymbol V_T\right),
 \qquad \|\xi\|_{A,\mathrm{sum}}\le1/16 .
 \tag{K.2}
$$
该域在J.3的完整数据球内。最后一块只用于短侧系数和E_B，
并不进入long方程。short reciprocal和square-root在64倍缩放单位球内
仍有统一非零间隙。
一个充分的入口是||Z||_A≤2^-36、||f||_dotA²≤2^-68、
||boldsymbol V_T||_A≤2^-14：因为2^-36/z_a<1/20，而
1/20+1/128<1/16。这里全部mean均按原定义包含，未投掉独立荷。

对64≤q≤8160定义真实物理高范数
$$
 z_q=z_a^{-1}\|Z\|_{H^{q+32}},\qquad
 f_q=\|f\|_{H^{q+34}},\qquad
 n_q=\|\boldsymbol V_T\|_{H^{q+32},\mathrm{sum}},
$$
$$
 A_q=n_q+f_q+(n_{64}+f_{64}+\epsilon)(1+z_q),\qquad
 D_q=1+z_q+r_B^{-1}f_q+64n_q .
 \tag{K.3}
$$
小量A_q与普通有限量D_q不能互换。
例如帽端两个曲率mean和平均高度跨度不是epsilon-screened输出。
只要求
$$
 A_{64}\le2^{-1048576},\qquad D_q<\infty
       \quad\hbox{于所使用的有限q窗}.
 \tag{K.4}
$$
没有要求高A_q小。若后续网络将低背景阶提高到1856，
可以另加A_1856的小门，不能据本篇自动宣布该门成立。

使用明确常数
$$
 C_q=2^{96q+16384}\quad(q\ge64).
 \tag{K.5}
$$
q≤1856时C_q<2^196608，q≤8160时C_q<2^800000。
这些是下文有序完整核的符号预算，不是新增数值实验。

## 2. 零宽全纯族给出的完整 Fourier 张量

J.3已在完整A代数、原径向sup强空间中构造唯一真实long解、
Phi_R、holonomy小根及全部均值。全部实角平移与原方程交换。
对固定度量，其边界算子族满足准确协变式
$$
 T(C_a\xi)=C_aT(\xi)C_{-a}\qquad(a\in\mathbb R).
 \tag{K.6}
$$
非线性输出同样平移，scalar mean输出按常数处理。
这里不对C_a作未知复角延拓。

先设规范化算子族F(xi):A→A在||xi||<1上全纯，
在||xi||≤3/4上范数不超过M。写F=sum F_k。
Cauchy给同次多项式范数≤M(4/3)^k。
其对称k线性极化的范数至多k^k/k!<3^k倍，因而
$$
 \|\widetilde F_k\|\le M4^k .
 \tag{K.7}
$$
k=0单独使用M。
所有变量属于带有限分量的sum Banach代数；
组件选择已经包含在该范数中，不再乘一个任意维数。

把每个背景参数和唯一方向都取为单一Fourier模。
由(K.6)，第k张量的矩阵系数只有在
$$
                   m=n+\ell_1+\cdots+\ell_k
 \tag{K.8}
$$
时可能非零，且绝对值由(K.7)控制。
这给的是完整张量核的绝对卷积支配，并不把一般A算子范数
直接认作一个Hilbert范数。原径向sup在系数估计内已经支付；
下文只在真正边界上求完整Fourier和。

对于所需p≤q+16≤8176，
$$
 \sum_{k\ge0}(k+1)^p4^{-k}
 \le p!\sum_{k\ge0}{k+p\choose p}4^{-k}
 =p!(4/3)^{p+1}<p!2^{p+1}.
 \tag{K.9}
$$
AM--GM给p!≤((p+1)/2)^p<2^{12p}。
余下的Bessel/pure-power换算可另付2^{p+4}。
因此包括一次指定高因子、两次参数微分和有限组件和时，
单次完整核估计可宽放为
$$
                         2^{L(q)},\qquad
 L(q)=14(q+16)+1024 .
 \tag{K.10}
$$
“指定高因子”使其余因子只消费||xi||_A；
4^k||xi||_A^(k-1)≤4(1/4)^(k-1)。
这解释(K.9)的比率，不含高范数小的假设。

## 3. One-high 卷积、真正半阶和真实 adjoint

对r≥0，由
Lambda(m)≤Lambda(n)+sum Lambda(ell_i)，
可以把Lambda(m)^r以(k+1)^r的费用分配给唯一输入方向
或唯一背景因子。其余全部背景因子在ell¹中，最高因子在ell²中，
用完整Young不等式。由
||u||_A≤2||u||H¹，低方向H^(64+1/2)足够支付所需低A范数。
这是实际one-high估计，不把两个最高背景norm相乘。

对原slope error
$$
 T_{Z,f}=D_f\mathscr K_Z(f)+\mathsf C_L,\qquad
 \mathsf C_L=|D|\coth(L|D|)P_\perp ,
$$
规范化族为a(D)T_{Z,f}|D|^-2。
它的张量核在还原后有实际权|n|²/a_m。
当q≥64，H^(q+1/2)→H^(q-1/2)的主卷积指数为q-3/2；
transpose-adjoint的指数为q+3/2。
两者最高背景阶只差三阶，均被(K.3)的+32余量覆盖。

对bare curvature Poisson列，规范化族是a(D)B_bare，
其核权为1/a_m，adjoint核权为1/a_n。
于是H^(q-1/2)→H^(q+1/2)的两个指数为q-1/2和q+1/2。
不把curvature输入免费当作高度两导源。
对complex背景先转置并共轭完整张量，再用相同绝对核；
无需假设非对称真实operator自伴。

0≤q≤64的低窗另外使用Peetre权，
把所需至多q+3阶lag权分配给背景卷积。
(K.3)的H96与两高度角导足够，给每一个本身阶数的operator门；
不是从H64 operator界倒推L²界。
mean输出m=0和方向中的独立mean使用a_0=Lambda(0)=1。
只有|D|^-2的非mean高度输入列按定义没有n=0。

## 4. 真实slope和系数的高低分离

J.4/N.11在原零宽球给
$$
 \|T_{Z,f}:\dot A^2\to\dot A^1\oplus\mathbb C\|
   <2^{25}\|f\|_{\dot A^2}+2^{41}\epsilon .
 \tag{K.11}
$$
在f=0的子球，整个族的界为2^41 epsilon。
在完整3/4数据球上可用2^43 r_B，因为epsilon≪r_B。
因此Taylor张量中没有f因子的项全部带epsilon；
有f因子的项以一份真实f而非f/r_B计费，剩余归一化因子
仍由(K.2)的几何级数求和。对含f项作
F_k(Z,f)-F_k(Z,0)的telescoping展开至多多一个k，已计入(K.10)。

N.19–20的实际left coefficients
c_mu=mu_L/mu_0-1、d_L和完整long四态，具有同样分离：
f=0的全部项带epsilon，一般项至少有一份真实f。
所以one-high后出现的是真正
$$
 f_q+(f_{64}+\epsilon)(1+z_q)
 \tag{K.12}
$$
及其低阶版本，而不是一个没有screening的z_q。
short-side coefficients只由n_q及原统一小分母控制。

此推导保持完整Phi_R反馈：
T包含D_f* K_B D_f Phi_R，未将f_*固定来取得较小常数。
Phi_R的零宽存在域、两个真mean和finite-L反射均未改变。
(K.7)是在已存在全纯图上取Taylor张量；
高正则的边界输出由绝对卷积收敛得到，而非预设该解高正则。

## 5. 完整DN差、未匹配E_B和两侧高低门

用N/J的准确物理式
$$
 \Delta\mathcal N_B
 =(\mu_L-\mu_0)\mathsf C_L
            -\mu_LT_{Z,f}P_\perp+\mu_Ld_L\partial_\theta .
 \tag{K.13}
$$
真正的未匹配外口按E的合并式
$$
 \mathcal E_B=P_{\mu_T}
 \{-M_a\mathsf C_L+M_aT_{Z,f}P_\perp+M_b\partial_\theta\},
$$
$$
 a=\mu_T-\mu_L,\quad b=\mu_Ld_L-\mu_Td_T,\quad
 P_{\mu_T}v=v-\frac{\mu_T}{\langle\mu_T\rangle}\langle v\rangle .
 \tag{K.14}
$$
两homogeneous列都杀常高度；齐次总通量mean由真实holonomy微分为零，
不是人为删除一行。affine mean荷仍见第7节。

先对bare slope用第3–4节，再乘真实mu。
ordinary multiplication的完整tame估计把最高导分给系数或方向；
系数的高范数只出现一次。
例如mu_high*T_low中的T_low由A_64控制；
a_high*T_low同样由A_64≤1及A_q吸收。
反向的low coefficient*high slope也只给A_64*high方向
及A_q*low方向。没有一个A_q²项。

P_mu的非identity部分是确切rank-one。
其输入mean由完整低阶算子范数控制，输出mu/<mu>的高norm
按同一个one-high系数估计收费。不能把该rank-one当constant输出；
short-side实际mu的高频保留。

因此对O=Delta N_B或E_B及其真正adjoint，在64≤q≤8160有
$$
 \boxed{\quad
 \|Ou\|_{H^{q-1/2}}
 \le C_q\left[
      A_{64}\|u\|_{H^{q+1/2}}
                     +A_q\|u\|_{H^{64+1/2}}\right].
 \quad}                                                   \tag{K.15}
$$
对0≤q≤64另有
$$
 \|O:H^{q+1/2}\to H^{q-1/2}\|
                      \le C_{64}A_{64}.
 \tag{K.16}
$$
negative Sobolev门以真实adjoint和对偶解释，
不把正阶方向上的一个高norm上界冒称所有负阶inverse。

为核定(K.5)，使用至多六次(K.10)的完整族/系数/列估计，
再为所有两因子tame乘法、rank-one读取和单位有限和收
4(q+8)+256 bits。总指数
6L(q)+4(q+8)+256=88q+7776<96q+16384。
四态固定缩放64、z_a^-1<2^32、r_B^-1=2^60都在每次1024位
固定余量内；没有把它们作为未记录的“常数”省掉。

## 6. 独立曲率Poisson保真实屏蔽和物理单位

先取
$$
 \mathcal B_{\rm bare}
       =-s_BD_{f_*}\mathcal K_B\,D_Z\Phi_R,\qquad
 \mathcal B_Z=\mu_L\mathcal B_{\rm bare}.
 \tag{K.17}
$$
完整零宽A→dot A¹⊕C界为2^10 s_B epsilon。
第2–3节先作用于bare族，之后再按真实tame乘法乘mu_L。
因此对于64≤q≤8160，真正B_Z及其adjoint均有
$$
 \boxed{\quad
 \|\mathcal B_Zv\|_{H^{q+1/2}}
 \le C_q s_B\epsilon
   \left[\|v\|_{H^{q-1/2}}
                     +D_q\|v\|_{H^{64-1/2}}\right].
 \quad}                                                   \tag{K.18}
$$
0≤q≤64对应界为
C_64 s_B epsilon D_64：该D_64不是可以自动省略的1。
真正s_B保留，尤其不把normalized f_B和物理高度混名。

另一个incoming源f_*^src仍用它的原dot H^(q+2)单位；
其bare列为-s_B D_f* K_B，重复同一kernel证明即可，
但不能把此输入改称H^(q-1/2)的curvature。
准确有序变化仍为
$$
 \delta f_*=D_f\Phi_R\,P_\perp g/s_B
                 +D_Z\Phi_R\,\delta Z+f_*^{src}.
 \tag{K.19}
$$
physical高度g的1/s_B只在(K.19)中的正确位置抵消；
其它独立source不凭该抵消丢掉s_B。

## 7. 全部mean、实际外荷与未受屏蔽的输出

完整N.24在本域逐字保持：
$$
 q_L=q_A-\int g_0,\qquad
 \pi_{\rm tmp}=r_\mu\pi_L+b_\mu H_\theta+\mu_Tb_\perp
                              +F_T^t-r_\mu F_L^t,
$$
$$
 \pi_T=P_{\mu_T}\pi_{\rm tmp}
       +\frac{\mu_T}{\langle\mu_T\rangle}q_T,\qquad
 c_B=\frac{q_T-\langle\pi_{\rm tmp}\rangle}{\langle\mu_T\rangle}.
 \tag{K.20}
$$
r_mu=mu_T/mu_L和b_mu=mu_T(d_L-d_T)的tame系数差由A_q控制；
各裸单位列及常数1保其原径向scalar，source本身的weak/atom/bare trace
规范没有被ordinary norm取代。P_mu的高频rank输出按第5节收费。
mean scalar分母在(K.2)的整个复球上有真下界。

帽端的真实输出仍为
$$
 B_R=\chi_R(V_R-P_R)/\sqrt{D_R},\qquad
 C_R=-\chi_RJ_R/(\sqrt E_R\sqrt{D_R}),
 \qquad d_m=i\operatorname{sgn}(m)(B_R)_m+q_mZ_m .
 \tag{K.21}
$$
B_R,0与C_R,0-C_r是原独立scalar输出，不带epsilon小门。
为完全固定其源和读出单位，定义
$$
 \mathscr W_R=(P_R,U_R,K_R,V_R,B_R/\chi_R,C_R/\chi_R),
$$
$$
 d_q=\|\delta Z/z_a\|_{H^{q+32}}
       +\||D|^2\delta f/r_B\|_{H^{q+32}}
       +64\|\delta\boldsymbol V_T\|_{H^{q+32},\mathrm{sum}} .
$$
d_64使用同一公式的H96；其中实际高度仍含它的两个额外角导。
J.3/S.5–7的完整complex数据球给long四态总量<4·2^-20，
原D/J分母使两个归一曲率输出总量<4，故整个W_R的A-sum可取<8。
(K.7)–(K.10)对同一真实图的有向微分因而给
$$
 \|\delta\mathscr W_R\|_{H^q,\mathrm{sum}}
       \le C_q\{d_q+D_qd_{64}\},
       \qquad64\le q\le8160 .
 \tag{K.21a}
$$
这保留全部mean。物理B_R/C_R输出准确乘回固定径向scalar chi_R；
原Robin行中的q_m delta Z仍是独立的原source列。
额外f_*^src必须按(K.19)的原单位另付，不能藏入d_q。
固定metric之外的delta chi_R亦不在(K.21a)内。
本篇不把这些普通D_q界加入A_q来伪称所有cap-side mean都受远端屏蔽。

一个常高度gauge继续独立。mean高度跨度是
$$
 \delta[v_0(L)-v_0(0)]
       =\int_0^L aw\,D\mu_t(h)\,\delta h\,dt .
 \tag{K.22}
$$
S.21对纯incoming变化付aw(L)/165，无额外epsilon。
对完整有序源，仍用该原weighted积分核和真实两端lifts，
以D_q作one-high费用；aw(L)以及物理高度输入的1/s_B
按原单位保留。不能用(K.18)的屏蔽常数代替(K.22)。

若度量、长度、Gamma、nu或形状参数改变，
必须继续微分s_B、mu_0、C_L和Phi_R的显式参数，
以及(K.20)–(K.22)全部原行。本篇不为这些参数导数捏造一个
与L无关的新统一常数；它证明的是固定度量的真实未知高度/曲率接口。

## 8. 完整能量门与真实坐标的使用范围

radial N_B,0≥|D|/6，齐次常高度被准确杀掉。
由(K.16)的q=0及真实半阶norm换算，完整boundary form相对差
可取2^8 C_64 A_64。若真实short connector已付eta_C，
$$
                   \eta_C+2^{10}C_{64}A_{64}<1/2
 \tag{K.23}
$$
就给同一个zero-root-trace能量逆及其真adjoint因子小于2。
全部affine mean/height/curvature列照原有序Schur代入。
(K.23)不含高A_q的小门；高regularity读取用(K.15)/(K.18)的tame项，
并没有据此直接证明全mixed传播网络的高阶tame inverse。

全部陈述先在实际物理theta中。若另用固定x表示，
真实scalar height和conormal density必须按D的同一j变换。
good derivative按U交换D_j、weighted mean和primitive；
raw pulled height另有b h_x，raw residual另有其真实transport项。
未经付费的C_tau-I或把density当scalar的转换都不在本篇结论内。

本篇给出的具体后继输入是：
low阶operator小，high阶仅线性依赖A_q或D_q；
完整two-source、两mean、unscreened高度跨度及实际E_B均在。
仍需将它们放入同一背景的principal/网络tame估计，
支付径向residual三jets、保持所有源域和端口，再闭合实际平滑迭代。
没有声称极小低球已包含现有数值中心的完整残差。
