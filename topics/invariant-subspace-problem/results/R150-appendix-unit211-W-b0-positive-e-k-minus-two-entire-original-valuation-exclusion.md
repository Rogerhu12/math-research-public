# R150：W/b0 正 e、k 剩余值负二的完整原赋值支排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-29（Asia/Taipei）。

## 1. 结论与完整覆盖

在当前正确 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 的原图中，取剩余特征为 $1009$ 的赋值。则不存在同时满足
$$
v(e)>0,\qquad v(k)=0,\qquad \bar k=-2
\tag{1}
$$
的原解。本稿关闭的是整个 (1)，包含全部原 lambda 极点、有限值、ell 首项下降和局部重分歧；不声称整个正 e 射线、内部权图或整个 W 已空。

完整覆盖由下列已成结论和本次唯一新执行组成：

| 原范围 | 完整来源 |
|---|---|
| $v(\ell)>0$ | [正 ell 原式排除及 $Z=(k+2)/e$ 整性](R150-appendix-unit211-W-b0-positive-e-k-minus-two-positive-ell-exclusion-and-integral-center.md) |
| $v(\ell)<0$ | [整个 ell 极点原式排除](R150-appendix-unit211-W-b0-positive-e-k-minus-two-entire-ell-pole-original-exclusion.md)，包括三个相对阶与深 M 中心 |
| $v(\ell)=0,\ v(\mu)<0$，$\mu=2\lambda-3$ | [整个 mu 极点的两原单位局部展开](R150-appendix-unit211-W-b0-positive-e-k-minus-two-ell-unit-entire-mu-pole-exclusion.md)；纸面先迫 $\bar\ell=1$，两个局部图完整覆盖 |
| $v(\ell)=0,\ v(\mu)\ge0$ | [有限 mu 的唯一原剩余中心](R150-appendix-unit211-W-b0-positive-e-k-minus-two-ell-unit-finite-mu-one-residue-center.md)，只余下文 (2) |
| 唯一有限中心 (2) | 本稿的两原单位 Jacobian、完整 N5 第二阶单位首项 |

其中有限 mu 的实际原覆盖是 $(L-3/5)^2$，不是把二重多项式改写为约化理想。该文只在剩余点层面结合原 q2/R6 得到
$$
\bar\ell=\frac35,\quad
\bar\mu=-2,\quad
\bar\lambda=\frac12,\quad
\bar T=-\frac12,\quad
\overline{(k+2)/e}=-\frac43 .
\tag{2}
$$
本稿用原完整局部方程处理 (2)，包括任意分歧和更高阶相消，不把这个剩余点当成一个已确定的 QQ 点。

## 2. 新局部坐标与原 r 因子的准确取消

令
$$
r=e,\quad Z=(k+2)/e,\quad x=Z+\frac43,\quad
k=-2+rZ,\quad u=1+r,\quad Q=rk,\quad \delta=1-Q .
\tag{3}
$$
先行正 ell 结论已经证明 $Z$ 整；在 (2) 中 $v(x)>0$，暂允许 $x=0$。物理原 $e=r$ 始终非零。

原权公式在取消一个明确 r 因子后是
$$
\ell=\frac{(1+r)\{4+r(Z^2-2Z)\}}
 {(-2+rZ)(Z-2+rZ)},\qquad
m=u-\ell,\quad M=\ell^2\delta-m^2,\quad bc=\frac M{4\delta}.
\tag{4}
$$
定义纯正则量
$$
t_0=-2u-\ell k,\quad j=-2u+\ell k,\quad
a_*=4uk-j,\quad \phi=t_0+4+k,
$$
$$
p_{02}=-2+2r^2+k\{(1+3r)\ell-u\},\qquad
c_*=a_*m^2+j\delta\ell^2 .
\tag{5}
$$
完整原定义逐项给
$$
T_0=rt_0,\quad J=rj,\quad A_*=ra_*,\quad
\Phi=r\phi,\quad P_{02}=rp_{02},\quad C_*=rc_* .
\tag{6}
$$
因此没有对初始 jet 中的 r 求逆，也没有把 r 的未知更高阶误当成单位。

原 $b_0=0$ 在当前中心可准确恢复为
$$
\kappa=\frac{uk\ell}{a_*},\quad T=\kappa\mu,\quad
\lambda=\frac{\mu+3}{2},
$$
$$
A_2=\frac{\mu^2+4\mu+5}{2},\quad
B_3=\frac{\mu^3+6\mu^2+12\mu+7}{2},
$$
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell A_2T+2T^3 .
\tag{7}
$$
这里的两个新正则原方程仅是
$$
q=\frac{q_2}{4r}
=\frac{2c_*A_2+2M\ell k(3-4\lambda)-8uk\delta\ell T^2}{4},
$$
$$
R=MK^2-4m^2D^3 .
\tag{8}
$$
$q=R=0$ 直接来自同一点的完整 q2/R6。对 $q_2$ 的 r 取消已在 (6) 中作为原多项式公因子完成，不取任何未知几何头的逆。

在 $(x,r,\mu)=(0,0,-2)$，
$$
k=-2,\quad \ell=\frac35,\quad m=\frac25,\quad
M=\frac15,\quad a_*=-\frac{24}{5},\quad
\phi=\frac65,\quad \delta=1,
$$
$$
D=\frac1{20},\qquad K=\frac1{50}.
\tag{9}
$$
(4)—(8) 的全部实际分母在此都是 1009 进单位。此处没有物理 D 的反演。

## 3. 两原单位 Jacobian 控制全部局部分支

按未知量 $(\mu,r)$ 的次序，固定 $Z$，实际完整第一阶返回为
$$
\frac{\partial(q,R)}{\partial(\mu,r)}
=
\begin{pmatrix}
-9/25&217/375\\
0&-27/62500
\end{pmatrix},
\qquad
\det=\frac{243}{1562500}.
\tag{10}
$$
行列式模 1009 为 $123$，因此为整单位。

(10) 的第二行保留真实的 r 变化。中心处 R 对 ell、T、mu 的导数都为零；固定 ell 时
$m_r=1,\delta_r=2,M_r=-2/25$，故
$$
\partial_rR
=-\frac2{25}\left(\frac1{50}\right)^2
 -8\frac25\left(\frac1{20}\right)^3
=-\frac{27}{62500}.
$$
完整权式的 $\ell_r=47/75,\kappa_r=7/36,T_r=-7/18$ 给出 q 行的另一项 $217/375$。本次源从完整 (4)—(8) 的第一阶 series 逐列核回 (10)，没有单凭显示矩阵假定它是原 Jacobian。

令 $A=\mathbb Z_{(1009)}$。单位隐函数定理在当前整局部图给出唯一
$$
\mu(x),r(x)\in A[[x]],\qquad
\mu(0)=-2,\quad r(0)=0,
\tag{11}
$$
满足原两式 (8)。任意假想原代数解，经同一赋值完成及必要代数扩张后，必须取自这同一整隐函数；不另选择一个有利分支。

若 $x=0$，唯一性给 $r=0$，与物理 $e\ne0$ 矛盾。因此任一可能的原解必须有
$$
x\ne0,\qquad v(x)>0.
\tag{12}
$$
这一步同时保全部非约化、任意分歧和任意更高阶接近方式。

本次在 QQ 上预先固定构造 12 阶：每阶只解 (10)，全部已知低阶原 q/R 系数必须精确为零；每一个实际系数分母均检查为 1009 进单位。最终两个完整原式都返回到第 12 阶。整隐函数定理负责无限尾的整性，执行并未以有限截断替代整隐函数本身。

## 4. 同一点完整 N5 的正则原表达式

继续用 (5)，设
$$
g=\lambda p_{02}+rt_0,\qquad
p_c=kp_{02}(\ell+T)-gt_0,\qquad
G=rg,\quad P_c=r^2p_c .
$$
完整原恢复准确成为
$$
t_s=-\frac{p_c}{bc\,k\phi},\quad
V_s=-\frac gk-\frac{p_c}{k\phi},\quad W_s=\frac{rt_0}{2},
$$
$$
y_s=\frac{\ell W_s-uV_s}{M},\qquad
w=\lambda-1-T,\qquad c_\lambda=-\mu ,
$$
$$
z_1=-2(\ell c_\lambda+2T)y_s-2\ell w+\frac{mTt_s}{\delta},
\qquad z_2=-\frac{2g}{k}-4my_s,
$$
$$
Z_0=2(\ell c_\lambda+T)(\ell uw+V_sT)+2bc\,t_sT^2 .
\tag{13}
$$
所用必要式仍是同一点、完整原 NV 的
$$
N_5=2mD(Z_0+Dz_2)+MKz_1=0 .
\tag{14}
$$
其原来源是[全 N5 值恒等式](R150-appendix-unit211-W-entire-b0-two-original-curves-5772-weights-46176-normalized-points.md)及相同的
[原定义源](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725。
下标 s 表示原 f 常数系数；本稿没有施加物理 $f=0$，也没有把完整 NV 换为某个独立分量或范数根。

(9) 保证 (13) 的所有实际分母都是当前整局部单位，因此 (14) 是 $A[[x]]$ 中的普通正则级数。替换 12 阶隐函数只改变第 13 阶及以后项，不会改变下文的第二阶首项。

## 5. 唯一实际首项排除整个有限中心

本次实际返回
$$
N_5(\mu(x),r(x),x)=c_2x^2+O(x^3),
\tag{15}
$$
其中第零、第一系数在 QQ 上严格为零，且
$$
c_2\in A^\times,\qquad \bar c_2=733\in\mathbb F_{1009}^\times .
\tag{16}
$$
实际 $r(x)$ 的首非零阶也是 2；证明 (15) 的矛盾只需要 (12)，不预设 $v(r)=2v(x)$。

$c_2$ 的精确定义是 (4)—(14) 经 (11) 的原隐函数替换后的 $[x^2]$。实际 10 字节规范 QQ 系数字符串 SHA-256 为
**53ff6deb3bc9e4ed3a237370361ea42235f67a15f95577b5e84aedbf5c1de14a**。
这里保存原定义、实际首项阶数及单位返回，不保存可重算的 jet 系数载荷。

由于所有尾系数整而 $v(x)>0$，(15) 的第一项严格低于其余项：
$$
v(N_5)=2v(x)<+\infty .
$$
它不可能为零，与完整原必要式 (14) 矛盾。因此 (2) 的整个原赋值中心排除。这是整局部唯一性加原完整值首项的结论，不是从一个有限域点、模 D 幂零或一个裸模 rank 外推 QQ 空性。

## 6. 唯一执行、精确来源与保存范围

源：
[2026-11-29-unit211-W-b0-positive-e-k-minus-two-finite-center-two-original-unit-jets-8542.py](../notes/2026-11-29-unit211-W-b0-positive-e-k-minus-two-finite-center-two-original-unit-jets-8542.py)。

源 blob **719469bead8b8388a6c93b9aa37b8e0162c8be23**，SHA-256
**3e596cbcbfb8cad9afc49437a1542ff73f41a950080c392daa04f0f59281ae43**；零依赖、固定 120 秒/1 GiB、固定 12 阶。

[唯一 run 46174918280](https://github.com/Rogerhu12/math-research-public/actions/runs/46174918280)，job **141071333935**，全部三个数学记录已亲读：

- 实际 **0.9118542709999957 秒 / 39264 KiB / exit 0**；最后数学阶段 **0.8564376100000004 秒**。
- 两原 Jacobian 全返回、q/R 完整至 12 阶、N5 第二阶单位首项；32 个 series 坐标返回、24 个隐函数系数、66 个 p 整系数检查、1 个完整 N5 jet。
- source commit **18f615c941b4e18e503d1ba028437b891fab5d85**；实际 pull 到 **43c2d3b4c98d50648ddb238c1fb346da890137ee**，**2026-11-28 18:16:20.009379 UTC**，两 README 与已读版本相同。
- stdout **1947 B**，SHA-256 **6232914f40e8b7b5b2b0bc72757b695689cd0293625f8e617a9bb599efcd11f8**。
- 完整 mu jet、e jet、N5 jet 只保存规范定义和摘要身份，不保存或传送可重算的系数缓存。

[小回执](../notes/2026-11-29-unit211-W-b0-positive-e-k-minus-two-finite-center-two-original-unit-jets-receipt-8542.json)保留全部三个原始数学记录和实际执行身份。

先前弱切锥源 da659b35f9ed3702ccd91a0c35efe4f2a595d083 从未执行，已在首次运行前被本源替代；不把它记录为数学失败。此次没有重做已成有限 mu 投影、两 pole jet、旧 C74/C78、六射线或原 PRS 门。

## 7. 整个 k 剩余值负二支的合成

$\ell$ 是原图非零量，故其估值仅分正、零、负。§1 的两条先行整支分别排正、负，剩 ell 单位；此时 mu 要么有极点，要么整，前者已经全闭，后者原覆盖只给 (2)，现由 §5 全闭。因此 (1) 无原解。

这个合成没有把单点数界当自由模，也没有把已付物理单位预设为赋值环单位。只有在各明确中心中由原首值实际证明单位的量才被用于局部恢复。其余正 e、其他 k 剩余值和内部 $v(e)=v(k)=0$ 的原 DVR 边界仍由各自新原输入处理。
