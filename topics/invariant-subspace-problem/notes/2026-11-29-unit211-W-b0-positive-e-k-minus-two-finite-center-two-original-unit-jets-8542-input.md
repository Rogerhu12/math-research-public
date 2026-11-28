# 唯一加强输入：正 e、k 趋负二的有限中心，两原单位 Jacobian 与完整 N5

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro。

状态：未执行。先前弱切锥源 da659b35f9ed3702ccd91a0c35efe4f2a595d083 从未运行，本源以更强的两原单位 Jacobian 完整替代它，不记录旧源失败，也不进入其二元首项/Bézout目标。

本源零依赖，固定总预算 **120 秒/1 GiB**、固定 **12 阶**。源：
2026-11-29-unit211-W-b0-positive-e-k-minus-two-finite-center-two-original-unit-jets-8542.py。

SHA256：3e596cbcbfb8cad9afc49437a1542ff73f41a950080c392daa04f0f59281ae43。

## 1. 唯一当前原中心

前置唯一实际 finite-mu 输入给必要剩余覆盖 $(L-3/5)^2$；原 q2/R6 纸代入后只保
$$
\bar\ell=3/5,\quad\bar\mu=-2,\quad
\bar\lambda=1/2,\quad\bar T=-1/2.
$$
取
$$
x=Z+4/3,\quad Z=(k+2)/e,\quad r=e,\quad
k=-2+rZ,\quad u=1+r,\quad Q=rk.
$$
当前 $v(r)>0,v(x)>0$，允许 x 本身等于零，直到第3节原隐函数唯一性再排除该可能。

原权图准确取消一个 r：
$$
\ell=\frac{(1+r)\{4+r(Z^2-2Z)\}}
 {(-2+rZ)(Z-2+rZ)}.
\tag{1}
$$
设 $\delta=1-Q,m=u-\ell,M=\ell^2\delta-m^2,bc=M/(4\delta)$。

## 2. 原正则化，明确不倒未知 r 或几何头

定义
$$
t_0=-2u-\ell k,\quad j=-2u+\ell k,\quad
a_*=4uk-j,\quad\phi=t_0+4+k,
$$
$$
p_{02}=-2+2r^2+k\{(1+3r)\ell-u\},\qquad
c_*=a_*m^2+j\delta\ell^2 .
$$
逐项完整原身份为
$$
T_0=rt_0,\ J=rj,\ A_*=ra_*,\
\Phi=r\phi,\ P_{02}=rp_{02}.
\tag{2}
$$
原 b0 给
$$
\mu=2\lambda-3,\quad
\kappa=\frac{uk\ell}{a_*},\quad T=\kappa\mu,
$$
$$
A_2=(\mu^2+4\mu+5)/2,\quad
B_3=(\mu^3+6\mu^2+12\mu+7)/2,
$$
$$
D=\ell A_2-T^2,\quad K=\ell^2B_3-3\ell A_2T+2T^3.
$$
新的正则原方程为
$$
q=q_2/(4r)
=\frac{2c_*A_2+2M\ell k(3-4\lambda)-8uk\delta\ell T^2}{4},
$$
$$
R=MK^2-4m^2D^3.
\tag{3}
$$
这是原同点 q2、R6 的定义，未将 r 作为一个 series 对象求逆。

在中心 $(x,r,\mu)=(0,0,-2)$，
$$
k=-2,\ \ell=3/5,\ M=1/5,\ a_*=-24/5,\ \phi=6/5,\ \delta=1.
$$
所有实际分母先以 (2) 取消 r 后，其常数都是 1009 进单位。没有 D、lambda、未知权头或新的范数逆。

## 3. 两原方程的准确单位 Jacobian

按变量 $(\mu,r)$ 的次序、固定 Z 求导，准确矩阵是
$$
\begin{pmatrix}
\partial_\mu q&\partial_rq\\
\partial_\mu R&\partial_rR
\end{pmatrix}
=
\begin{pmatrix}
-9/25&217/375\\
0&-27/62500
\end{pmatrix}.
\tag{4}
$$
其行列式 $243/1562500$ 为 1009 进单位。源在新目标开始时，从完整原式的第一阶 series 差逐列返回 (4)。

这里 $\partial_rR$ 并非假定 R 的一般头非零。可直接看：在中心 R 对 ell、T、mu 的三导数都为零；固定 ell 后，$m_r=1$、$\delta_r=2$、$M_r=2\ell^2-2m=-2/25$，所以
$$
\partial_rR=(-2/25)(1/50)^2-8(2/5)(1/20)^3
=-27/62500.
$$
完整权图中的 $\ell_r=47/75$、$\kappa_r=7/36$、$T_r=-7/18$ 给出 (4) 的另一项 $217/375$。

整隐函数定理给唯一
$$
\mu(x),r(x)\in\mathbb Z_{1009}[[x]],\qquad
\mu(0)=-2,\ r(0)=0
$$
通过该中心并满足原两式 (3)。任一假想原赋值解在完成后必须是这同一隐函数的取值。如果 x=0，则原唯一性迫 r=0，与原 e 非零矛盾；所以物理解的 x 必非零且有正估值。

本次在 QQ 上逐系数构造到12阶，每阶只解固定 (4)。全部低于当前阶的 q/R 系数必须精确为零，每个新系数分母逐一为 1009 进单位，最终原 q/R 的所有12阶坐标完整返回。底层 Laurent/Taylor 类显式传播已知精度，不把截断之外的尾项冒作零。

## 4. 同点完整 NV 的第一次原必要项

由 (2)，
$$
g=\lambda p_{02}+rt_0,\qquad
p_c=kp_{02}(\ell+T)-gt_0,\qquad
G=rg,\quad P_c=r^2p_c.
$$
因此完整原定义正则成为
$$
t_s=-p_c/(bc\,k\phi),\quad
V_s=-g/k-p_c/(k\phi),\quad W_s=rt_0/2,
$$
$$
y_s=(\ell W_s-uV_s)/M,\quad w=\lambda-1-T,\quad c_\lambda=-\mu,
$$
$$
z_1=-2(\ell c_\lambda+2T)y_s-2\ell w+mTt_s/\delta,\quad
z_2=-2g/k-4my_s,
$$
$$
Z_0=2(\ell c_\lambda+T)(\ell uw+V_sT)+2bc\,t_sT^2,
$$
$$
N_5=2mD(Z_0+Dz_2)+MKz_1.
\tag{5}
$$
(5) 是已刊完整原 NV 的必要身份，不是选择个别分量。所用 s 下标量为原 f 常数系数，不施加物理 f=0。

N5 在当前局部环正则。用12阶 jet 替换真正的 $\mu(x),r(x)$ 只改变13阶以后项。源只读取 N5 的第一个 QQ 精确非零系数 c：

- 如果其阶数不超过12，且 c 模1009非零，则它是单位首项；由于 x 非零且 $v(x)>0$，原 N5 不可能等于零，排除此完整有限中心；
- 如果12阶全部为零，保留整个中心；
- 如果第一个 QQ 非零系数模1009为零，也保留中心，不跳过该系数、不以更后项冒充首项。

这使用整局部唯一性与完整原式，不是裸模空性提升 QQ，也不要求全值商或原几何环境自由。

## 5. 独立目标与边界

已成 finite-mu 两固定结式仅用于确定当前必要中心，不再计算；L=1 的两个 pole 输入也不进入。先前弱切锥源从未运行并被本输入替代，不作为失败或冻结数学目标登记。

只有本次实际完整返回单位首项才可关闭当前有限中心。源不预报阶数、系数、整 ellunit 或整个 W 为空；固定12阶、固定120秒/1GiB，无追加或换目标。
