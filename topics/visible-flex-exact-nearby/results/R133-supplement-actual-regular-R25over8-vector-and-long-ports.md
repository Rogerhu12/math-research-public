# R133：真实 $R=25/8$ 入口向量与完整周期长段非线性端口

**已证明并实际完成有向预算。** 本篇把主体右边界直接放在
$R=25/8$，给出可供有限候选使用的256个物理频率向量，以及与该向量
相接的**全部**非零频率误差、真实非线性 $B,C$ 端口和均值/高度合同。
该结论没有假设新的 moving 候选已落入输入球，也没有把更远端的
nonlinear regular/label 方程设为0。

准确 leading multiplier 是

$$q_*=(1+(a_R/(4\omega))^2)^{-1/2};$$

其分母没有额外的模式 $m$。只有第四模的真实无限尾 multiplier 恰等于
$q_*$；其余模保留明确非零尾误差。真全频共同界为

$$0<q_m(R)<1\qquad(m\in4\mathbb N).\tag{P.1}$$

对于完整物理非mean输入 $Z=(C-C_r)_{\ne0}$ 满足
$\|Z\|_{A^0_\sigma}\le10^{-10}$，及独立
$\|f_B\|_{\dot A^2_\sigma}\le2^{-60}$，本次实际原生计算得到

$$
\|b+q^{\rm true}Z\|_{A^0_\sigma}<1.638400032\cdot10^{-14},\quad
|C_0-C_r|<2.048000040\cdot10^{-15},\quad B_0=0.
\tag{P.2}
$$

采用保存的浮点 nominal vector 后，包含其全部参数误差的第一界仍小于
同一外放小数。这里 $b_m=i\operatorname{sgn}(m)\widehat B_m$。
这是原物理角 $\theta$ 的完整 Fourier 代数界，不是只计算保留的256模。

## 1. 真实尾身份与正确入口公式

有限 body、natural graft 和长段入口仍取同一原完整对象
`type_fixed_step02_d5_exact_affine_step5_object.json`，全
$\delta=-7789843107295549/4611686018427387904+\eta$、
$|\eta|\le10^{-9}$。实际 $a_R,\omega$ 由已完成真实1334盒参考的
`true_R74_entrance` 给出。紧支撑 $E_\nu=Ee^{\nu h}$ 在 $r\ge.18$
准确等于 $E$，因此本入口不依赖主体选择的 $\nu$；这不意味着主体的
其他证书能换参数沿用。

除了原 R74 无限尾，本篇也明确适用于
[强首剪切新尾 V.8–V.12](R119-supplement-stronger-tail-raw-labels-sources-and-regular-boundary.md)
的已证对象：固定其中一个真实 $\Gamma$，用新无限尾重新选择全模
好 bump 参数，并重新停止第四 connector。该篇证明未改入口
$a_*,z_*,\omega$，且令

$$B=2^{24}-25/8,\quad L=\omega B,$$

有真实斜率

$$|\lambda_m+m\omega|<2^{41}m\omega e^{-2mL},\qquad
\lambda_4=-4\omega.\tag{P.3}$$

这是新尾重新实例化后的结论，不是将原来选定的好参数免费沿用。
其后另加第二负区 bump 的对象若尚未重新实例化全标签、第四停止和
好集，则不在本篇的已证身份内。

在准确长段入口用半径坐标 $a$，记
$w_R=a_R/(4\omega)$、$E_a=1+w_R^2$。
真实高度迹消去给

$$
c_m^{\rm ht}=\frac{\omega-\lambda_m}{\omega-\lambda_m/m^2},\qquad
\frac{B_m^{\sin}}{(C-C_r)_m^{\cos}}
=-\frac{m(c_m^{\rm ht}-1)}{\sqrt{E_a}(m^2-c_m^{\rm ht})}
=\frac{\lambda_m}{m\omega\sqrt{E_a}}.
\tag{P.4}
$$

所以

$$q_m^{\rm true}(R)=-\lambda_m/(m\omega\sqrt{E_a}),\qquad
q_4^{\rm true}=q_*,$$
$$|q_m^{\rm true}-q_*|\le e_m,quad
e_4=0,quad e_m=2^{42}e^{-2mL_-}>0\quad(m>4).
\tag{P.5}
$$

该稍宽系数同时包含原 R74 和 (P.3)。非第四四重模至少为8，因此
共同非零尾费可取 $e_\infty=2^{42}e^{-16L_-}$。
真 $a_R>0$ 和完整有向算术实际证明
$q_*^- -e_\infty>0$、$q_*^++e_\infty<1$，得到 (P.1)。
故任意相同 Fourier 权的全频 $q$ 乘子范数都不超过1，包括未保留模式。

## 2. 浮点 proposal 与真全参数误差

数据向量按物理 $m=4,8,\ldots,1024$ 排列，各项取实际 $q_*$ 包络中点的
同一个精确 dyadic 浮点数。这是候选用 proposal，未宣称为真实无限尾
每一个 $q_m$ 的精确值。原生全参数界为

$$q_*\in[0.9999999999993693841724266600,
          0.9999999999993693841724373102],$$

$$|q_* -q^{\rm nom}|<9.149586252\cdot10^{-18}.\tag{P.6}$$

每个模式的完整误差为 (P.6) 加 (P.5) 的对应 $e_m$；native 对每个
非第四模验证 $e_m>0$，其巨大负指数不会因转成 double 时下溢而被
删除。共同费约为 $1.289\cdot10^{-170341211}$，但证明始终使用
Arb 指数形式。

若完整边界迹包含所有非零模，则

$$
\|b+q^{\rm true}Z\|
\le\|b+q^{\rm nom}Z\|
+\sum_{m\ne0}(|q_*-q^{\rm nom}|+e_{|m|})|Z_m|e^{\sigma|m|}.
\tag{P.7}
$$

只保存有限 nominal 数组时，未保留真实 $b,Z$ 的全尾还须另付
$\|b_{\rm tail}\|+\|Z_{\rm tail}\|$，由 (P.1) 支付；不能用一个采样
FFT 尾代替此完整尾。

## 3. 完整 $C$ 到实际周期长段 Dirichlet 的可调小球

采用[真实周期长段接合](R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md)
的完整非线性 Dirichlet 解与 M.10–M.19。这里只收缩其输入球，不改变
方程、有限长反射、mean holonomy 小根或另端数据。

允许 $0\le\sigma\le1/8$，范数为

$$\|Z\|_{A^0_\sigma}=\sum_{m\ne0}e^{\sigma|m|}|Z_m|,
\quad\|f\|_{\dot A^2_\sigma}=\sum_{m\ne0}e^{\sigma|m|}|m|^2|f_m|.$$

取 $\|Z\|\le r_Z$、$\|f_B\|\le r_B\le2^{-60}$，设

$$r_f=10(r_Z+r_B),\quad F=r_f+r_B,\quad H_*=6F.$$

以下实际门要求 $2F<2^{-25}$、$H_*<2^{-20}$；本次
$r_Z=10^{-10}$ 明确满足。准确线性 $C$ 算子为

$$({\cal L}_C)_m=\chi\sqrt{E_a}(m^2-c_{|m|}),\quad
\chi=1/(4\omega),\quad c_M=M\coth(ML),$$

其全频逆范数 $A^0_\sigma\to\dot A^2_\sigma$ 小于9，
因为 $M^2/(M^2-c_M)\le1020/763$、$1/(\chi\sqrt{E_a})<6$。
准确非线性方程为

$$f_*={\cal L}_C^{-1}
 [Z-\chi\sqrt{E_a}S f_B-{\cal R}_C(f_B,f_*)],\quad
S_M=Me^{-2L}\operatorname{csch}(ML).\tag{P.8}$$

既有完整证明给 $\|{\cal R}_C\|\le2^{12}F^2$，真 long 解
$\|h\|_{\mathcal Y_\sigma}<6F$，以及有限长反射
$\|{\cal L}_C^{-1}\chi\sqrt{E_a}S\|\le2e^{-6L_-}=:\epsilon_s$。
因此球像及收缩门为

$$I_C=9r_Z+\epsilon_s r_B+9\cdot2^{12}F^2<r_f,$$
$$\lambda_C=9\cdot4\cdot2^{12}F<1,\quad
J_f:=\|D_Zf_*\|\le9/(1-\lambda_C).
\tag{P.9}$$

导数费来自在半径 $F$ 的完整复 Banach 球上作 Cauchy 估计，较大球的
总边界范数至多 $2F<2^{-25}$，始终处于原真实全纯域中。
本次有向结果为

$$r_f<1.000000009\cdot10^{-9},\quad
I_C<9.000368641\cdot10^{-10},\quad
\lambda_C<.000147456002,\quad J_f<9.001327300.$$

这给完整无限频率的实际周期长段及 $Z\mapsto f_*$，不是反演一个有限
边界矩阵。共同偶反射由唯一性保持。

## 4. 真非线性两曲率端口，均值与反射不删

令 $q_M^L=M(c_M-1)/(\sqrt{E_a}(M^2-c_M))$ 为有限长线性图。
准确代数和 $\coth(ML)$ 的指数式给

$$|q_M^L-q_*|\le8e^{-8L_-},\qquad
\epsilon_q=e_\infty+8e^{-8L_-}>0.$$

真实 $f_*$ 解 (P.8) 后，给主体的完整非mean端口定义为

$$d_m=i\operatorname{sgn}(m)B_m^{\rm long}
+q_m^{\rm true}Z_m.\tag{P.10}$$

沿用准确曲率公式和非线性 holonomy 小根的完整界，

$$
\|d\|\le\epsilon_qr_Z+\epsilon_s r_B+2^{14}F^2=:e_d,
\quad |C_0-C_r|\le2^{11}F^2=:e_0,
\quad B_0=0.\tag{P.11}
$$

最后一个等式只因实际共同反射；$C_0-C_r$ 是真输出，未设为0。
对固定但任意 $f_B$，其完整 $Z$ 导数为

$$\|D_Zd\|\le\epsilon_q+4\cdot2^{14}FJ_f,
\quad\|D_Z(C_0-C_r)\|\le4\cdot2^{11}FJ_f.\tag{P.12}$$

本次分别小于 $.000589910992$、$.0000737388740$。
实际 $e_d<1.638400032\cdot10^{-14}$、
$e_0<2.048000040\cdot10^{-15}$。nominal $q$ 的额外费是
$(|q_*-q^{\rm nom}|+e_\infty)r_Z$，已在原生报告加入。
不能仅由输入 $10^{-10}$ 的数量级把充分二次余项声称为 $10^{-20}$；
完整系数 $2^{14}F^2$ 必须保留。

在 moving 变量 $\mathfrak m=\langle v\rangle_\phi$ 中，准确物理
$C$ 平均为 $1/\mathfrak m$。所以右端真实 mean 方程是

$$1/\mathfrak m-C_r=c_0(Z,f_B),\tag{P.13}$$

不是直接把右端 $\mathfrak m$ 固定为 $1/C_r$ 后宣称 nonlinear mean
已满足。有限候选可以先用零右端，但 (P.11)–(P.12) 要进入后验系统。

## 5. 高度、另一端 regular 方程与真实身份

曲率没有消去位置常数。实际端口继续保留

$$v_\perp(R)=a_Rw_Rf_*,\quad
v_a(R)=w_R[\mu+2f_*+h_t(L)],\quad Z_{\rm surface}=Z_{\rm ref}-v,$$
$$v_r(R)=-4c_0\omega a_Rw_R[\mu+2f_*+h_t(L)],$$
$$v_0(L)-v_0(0)=\int_0^L aw\mu_t(h)\,dt.\tag{P.14}$$

其中整体 mean height 平移独立；最后一式不是两个可任意指定的
Dirichlet mean。$\mu$ 是实际 holonomy 小根，
$|\mu|\le256H_*^2$，并非删除的平均修正。
本次原生给完整 raw 高度、$a$ 导数和 mean height 差分别小于
$4.607130650\cdot10^{-22}$、$2.829841791\cdot10^{-16}$、
$3.396745321\cdot10^{-26}$。它们仍是 raw 两迹，没有误称 grounded flux。

独立 $f_B$ 必须最终等于实际 tail labels 产生的物理输入，并联立

$$\mathfrak F(a,f_*)=k_B(a)+C_Lf_B(a)-S_Lf_*
-E_D(f_B(a),f_*)=0.\tag{P.15}$$

将 $f_B=0$ 作为一个允许的参数值，并不意味着 (P.15) 已解。
同样，新主体只有在完整物理 $B,C$（包括 mean）与该周期长段一致后，
才能消费实际框架唯一输运和周期拼接；一条小线性 Robin 残差不自动
给出闭 surface、握持或 reach。

## 6. 从旧 $r=1.5$ 截断改用本口的完整字段

1. 主体真实区间终点改为 $25/8$；初猜必须在新增区间真实构造，不能
   对旧 PPoly 作区间外延拓。
2. `q_values`、`physical_frequencies` 的格式仍可沿用，但报告
   `kind` 为 `floating_actual_R74_regular_endpoint_q_vector`，
   `left=right=right_boundary='25/8'`。旧cut的身份检查须相应修改。
   现在 `all_nonmean_q_abs_upper=1`，不使用旧cut的 $1.06$。
3. 所有边界模式仍是物理 $\theta$ 的真实 Fourier 矩。moving 解需用
   真实角图的完整矩公式，而非把 $\phi$ Fourier 数直接当作 $B,C$ 迹。
4. 全非mean行保留 $b+qZ=d(Z,f_B)$，mean按 (P.13) 保留，参数列照实际
   全方程微分。若有限未知 $b,c$ 曾除以振幅 $\alpha$，上面的物理余项
   也须除以 $|\alpha|$ 后放进相同归一的行。
5. 原 $r\le1.5$ 的 target jet provider 不许在新增区间外插。后半body
   及 natural graft 须逐真实 scalar germ 支付其目标 jet。
6. 最后仍保留 (P.15)、mean height 和最终完整固定度量身份；本口的
   $\nu$ 无关性只来自支持确实在 $.18$ 结束。

## 7. 最小可复跑资料

源码为 `scripts/fourfold_codazzi_actual_regular_endpoint_ports.py`；
向量为 `notes/2026-11-13-R133-regular-r25over8-q256-floating.json`；
完整原生为 `notes/2026-11-13-R133-regular-r25over8-q256-long-ports-native.json.gz`。
原生实际正常完成约0.19秒，保存所有256个真实尾费、全频正性门、
可调小球收缩、全部两曲率端口和高度条件。

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python scripts/fourfold_codazzi_actual_regular_endpoint_ports.py --modes 256 --C-radius 1/10000000000 --floating notes/2026-11-13-R133-regular-r25over8-q256-floating.json --native notes/2026-11-13-R133-regular-r25over8-q256-long-ports-native.json.gz
```

`--C-radius` 可用实际已证的完整输入上界重新实例化，旧报告保持原样。
该程序不验证某个新候选确在此球内；完整新候选的物理无限尾、径向
残差、混合型两端逆及 nonlinear regular 方程仍须继续支付。
