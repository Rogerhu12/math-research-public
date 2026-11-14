# R133：开放全频曲率端口图及完整 M128 内端消费

本篇把[已完成的非零中心驱动帽](R133-supplement-complete-nonzero-centred-cap-with-interface-jumps.md)
变成可供内侧 body 联立的真正端口映射。区间仍为 $[L,R]=[1,25/8]$，
真实度量、完整 $|\eta|\le10^{-9}$、全 primitive 尾及全部 $4\mathbb Z$ Fourier 模不变。
曲率数据 $(B,C)$ 采用同一个真实材料正交标架。

本篇给出开放内侧 $c_{\ne0}$ 邻域中的实际解、其 $B_{\ne0}$ 迹和两个 mean 输出，
并严格包含完整 M128 候选的内端数据。它是曲率迹图；没有把这些数据改名为
raw height、grounded flux 或完整 nonlinear regular DN。body 的真正 PDE、内侧两迹精确匹配、
实际外尾条件和全局框架 holonomy 仍须联立。

## 1. 四独立输入和同一真实小球

沿用

$$
C=C_r+c,\qquad Q(B,c)=\frac{B^2+\ell c^2}{C_r+c},\qquad
b_m=i\operatorname{sgn}(m)\widehat B_m,\qquad d_m=b_m+q_m c_m.
\tag{O.1}
$$

$q_m$ 是由真正 R74 regular 线向内传播的全频正 Jacobi 比值，含原非零指数费用。
所有曲率校验都使用分片最大值后 Fourier 求和的完整 $X_0$ 代数；
实际解已通过全部精确接口点源修正，因而径向连续。

此前的单次残差细化给同一严格球

$$
\rho_1\simeq .00010485781069775346,\quad
\varepsilon<3.707847151\cdot10^{-5},\quad
\lambda<.314365134,\quad
L_Q:=\sup\|DQ\|<.026002095.
\tag{O.2}
$$

新的 consumer 从该球的外舍入记录取 **内侧半径端点**，使原完整 $DQ$ 界
确实覆盖新球的每一点。没有根据小数中点或外侧端点扩大先前认证的管。
原初版 producer/report 保留，最终结论明确消费 `v2_inward_radius`。

允许内侧输入在原完整 M64 迹附近满足

$$
c_{\ne0}(L)=\widehat c_{\ne0}(L)+h,\qquad
\|h\|_{A_0}\le10^{-5},
\tag{O.3}
$$

这里 $h$ 可以含无限多个物理模。原三个外输入仍为

$$
\|d_{\ne0}(R)\|_{A_2}\le10^{-8},\qquad
|B_0(R)|\le10^{-8},\qquad |c_0(R)|\le10^{-8}.
\tag{O.4}
$$

$A_2$ 权为 $(1+|m|)^2$。对仅有 $A_0$ 的内侧扰动，得到完整连续曲率解；
当该输入另属于 $A_2$ 时，原角平移证明给未知解的完整二阶角正则及局部 $C^2$ 浸入。
这里不要求 $h$ 的 $A_2$ 范数也小于 $10^{-5}$。

完整线性边界常数为

$$
H_C<2.235854543,\qquad H_D<7.526210559.
\tag{O.5}
$$

故新球像只增加 $H_C10^{-5}$。实际有向消费为

$$
\varepsilon+H_C10^{-5}+\lambda\rho_1
 <.000092400657<\rho_1,
\qquad\text{margin}>.000012457154.
\tag{O.6}
$$

这一严格余量给每组允许数据的实际唯一解，也允许在每组数据附近作真正 Fréchet 微分。
包括 mean 在内的各输入列作用于完整无限 Fourier 空间。

## 2. 完整曲率迹图和两个 mean 行

对 $m\ne0$，准确三角方程为

$$
d_m'=(|m|\gamma q_m-2\beta)d_m
       +(-|m|\gamma+q_m\beta)Q_m.
\tag{O.7}
$$

令 $K_{D,m}(L,s)=\exp[-\int_L^s(|m|\gamma q_m-2\beta)]$，
$T_m=K_{D,m}(L,R)$，则

$$
\begin{aligned}
b_m(L)&=-q_m(L)c_m(L)+T_m d_m(R)+\mathcal N_m(U),\\
\mathcal N_m(U)&=\int_L^R K_{D,m}(L,s)
                  (|m|\gamma-q_m\beta)Q_m(s)\,ds.
\end{aligned}
\tag{O.8}
$$

这是真正非线性解的等式，$\|T\|_{A_0\to A_0}\le1$。
已经支付的完整 D 非线性源核满足

$$
\|\mathcal N(U)-\mathcal N(V)\|_{A_0}
 \le K_D L_Q\|U-V\|_{X_0^2},\qquad K_D<1.390917486.
\tag{O.9}
$$

物理 $B$ 的迹由 $\widehat B_m=-i\operatorname{sgn}(m)b_m$ 还原。
所以旋转参考的物理 Fourier 曲率图是
$\widehat B_m=i\operatorname{sgn}(m)q_m c_m$；在实 sine/cosine 约定下
$B_{m,\sin}=-q_m C_{m,\cos}$。这些方向不能与高度或 grounded flux 的方向混用。

两 mean 方程另给准确关系

$$
\begin{aligned}
B_0(L)&=\tau_B B_0(R),
 &\tau_B&=\frac{a(R)^2}{a(L)^2},\\
c_0(L)&=\tau_C c_0(R)+\mathcal N_0(U),
 &\tau_C&=\frac{a(R)^2C_r(R)}{a(L)^2C_r(L)},\\
\mathcal N_0(U)&=-\int_L^R
 \exp\!\left[\int_L^s\beta(\ell+1)\right]\beta(s)Q_0(s)\,ds.
\end{aligned}
\tag{O.10}
$$

其全频非线性比较为

$$
|\mathcal N_0(U)-\mathcal N_0(V)|
\le K_{\rm mean}L_Q\|U-V\|_{X_0^2},\qquad
K_{\rm mean}<.523455817.
\tag{O.11}
$$

实际完整端点系数另给

$$
\tau_B<2.572084128\cdot10^{-10},\qquad
\tau_C<1.656667537\cdot10^{-10}.
\tag{O.12}
$$

这些 mean 是真实曲率输出，不是可删除的平均误差。特别地，对实解，
$\ell>0$ 且 $C_r+c<0$ 给 $Q\le0$。若 $c_0(R)=0$ 且非零内侧输入不为零，
则 (O.10) 给 $c_0(L)<0$。因此不能在该非平凡正帽的两端同时任意设定这个 mean 为零。
regular mean height 和 flux 也没有被这两个曲率数值替代。

## 3. 开放图的全部微分列和非零迹可逆性

对输入列 $x\in\{c_L,d_R,B_{0R},c_{0R}\}$，记

$$
H_x=(H_C,H_D,1,1)_x.
\tag{O.13}
$$

对真实固定点求导，并用 $\|(I-G_QDQ)^{-1}\|\le(1-\lambda)^{-1}$，得到

$$
\|D_xU\|\le\frac{H_x}{1-\lambda},\qquad
\|D_x\mathcal N\|\le\frac{K_DL_QH_x}{1-\lambda},\qquad
\|D_x\mathcal N_0\|\le\frac{K_{\rm mean}L_QH_x}{1-\lambda}.
\tag{O.14}
$$

第二列中 $D_{d_R}b_L$ 的参考线性项为 $T$；第一列的参考项为 $-q_L$。
mean $c_{0R}$ 列还保留准确线性项 $\tau_C$，mean $B$ 行则始终是准确 $\tau_B$。

实际保守上界为：

| 输入列 | 完整解导数 | 非零 $d_L$ 的非线性余列 | mean $c_0(L)$ 的非线性余列 |
| --- | ---: | ---: | ---: |
| $c_{\ne0}(L)$ | $3.260999$ | $.117940$ | $.044386$ |
| $d_{\ne0}(R)$ | $10.976996$ | $.397003$ | $.149408$ |
| $B_0(R)$ | $1.458503$ | $.052750$ | $.019852$ |
| $c_0(R)$ | $1.458503$ | $.052750$ | $.019852$ |

对于固定其余三个外输入的内侧图 $c_{\ne0}(L)\mapsto b_{\ne0}(L)$，

$$
\|D_{c_L}b_L+q_L\|_{A_0\to A_0}<.117939791,
\qquad q_m(L)>.9429307446.
\tag{O.15}
$$

对角算子 $q_L$ 在完整非零 Fourier $A_0$ 上有有界逆，故 Neumann 定理给

$$
\|(D_{c_L}b_L)^{-1}\|_{A_0\to A_0}
\le\frac1{q_- -\|D_{c_L}b_L+q_L\|}<1.212135.
\tag{O.16}
$$

这里是整个非零频率算子，不是前64或128模矩阵的逆。两个 mean 另有 (O.10)–(O.14)，
没有被混入对角 $q_L$，也没有据此声称完整混合型 body/regular 算子可逆。

## 4. 比全局误差更直接的实际内侧两迹界

原固定内侧 $c_L=\widehat c_L$ 的解已有完整误差
$e<5.407903434\cdot10^{-5}$。直接消费 D 和 mean Green 行可得到更小的左端费用。
设完整含无限尾的常规残差界为 $R_B,R_C,R_0$，完整接口总和为 $J_B,J_C,J_0$，
$e_{dR}$ 是实际中心右迹 $\widehat b_R+q_R\widehat c_R$ 与原允许输入的距离上界。
则

$$
\begin{aligned}
e_{bL}&\le e_{dR}
 +\frac{R_B+q_+R_C}{\sigma_D}+J_B+q_+J_C+K_DL_Qe,\\
e_{c0L}&\le\tau_C\bigl(e_{c0R}+|\widehat c_0(R)|\bigr)
 +K_0R_0+J_0+K_{\rm mean}L_Qe.
\end{aligned}
\tag{O.17}
$$

非零 $c_L$ 本来准确固定，故 $b_L$ 的误差恰等于 $d_L$ 的误差。
完整算法仍按实际无限输入支付 $q_R$ 的 R74 fee；没有用舍入为零的浮点费用替代它。
native 给

$$
\begin{aligned}
\|b_L-\widehat b_L\|_{A_0}&<5.934453818\cdot10^{-6},\\
|c_0(L)-\widehat c_0(L)|&<7.482648847\cdot10^{-7},\\
|B_0(L)|&<2.572084128\cdot10^{-18}.
\end{aligned}
\tag{O.18}
$$

最后一行使用整个允许的 $|B_0(R)|\le10^{-8}$；它不是丢弃该 mean。
完整中心的原始字节保留；内侧迹的全部有理数另保存于报告。

## 5. 全 M128 候选的准确内侧消费

已完成的 M128 有限 BVP 候选具有实际二进制参数

$$
\nu=-6837290349363917/288230376151711744,
\tag{O.19}
$$

以及保存的二进制振幅对应于诊断数 $.65$。其 body 度量与 M64 中心的 body 度量不同；
两者的紧支撑修改在 $r\ge.18$ 都准确为零，所以本篇 $r\ge1$ 的真实帽度量一致。
这条消失恒等式经 producer metadata 和完整候选 SHA 校验，不能用于内侧修改区间。

`fourfold_codazzi_cap_M128_inner_trace.py` 加载 M128 的全部三次分片，
在准确 $r=1$ 逐系数作有理数 Horner 求值。它比较全部128正模及负共轭，
把原 M64 缺少的高模作为精确零延拓。没有截取 M128 的前64模来判断输入是否可用。

记两候选内端差为 $\Delta b,\Delta c,\Delta c_0$，则实际严格界为

$$
\|\Delta c\|_{A_0}<3.690959461\cdot10^{-9}<10^{-5},
\qquad
\|\Delta b+q_L\Delta c\|_{A_0}<5.964042711\cdot10^{-9}.
\tag{O.20}
$$

第二行保留完整真实 $q_m(L)$ 的区间，不用浮点最优比值。
因此 M128 的整个真实内侧非零 $c$ 迹落在已证明的开放图内。
取该准确输入的真实帽，借 (O.15)、(O.18) 和完整 mean 余列，得到

$$
\begin{aligned}
\|b_L^{\rm cap}-b_L^{128}\|_{A_0}
 &\le e_{bL}+\|\Delta b+q_L\Delta c\|_{A_0}
       +.117939791\|\Delta c\|_{A_0}
 <5.940853172\cdot10^{-6},\\
|c_{0,L}^{\rm cap}-c_{0,L}^{128}|
 &\le e_{c0L}+|\Delta c_0|+.044385286\|\Delta c\|_{A_0}
 <7.484999822\cdot10^{-7}.
\end{aligned}
\tag{O.21}
$$

非零 $C$ 迹由定义准确一致，$B$ 非零迹和 $c$ mean 的上述量仍是未消去的匹配残差。
真实帽输出的无限高模已包含在界中。M128 的有限 body 本身尚未变成真正连续 PDE 解，
其原始径向 PPoly 接口在后续 body 验证中仍须逐个付费。

## 6. 复跑、保存与下一项必须联立的数据

两个最终 consumer 只消费已保存的完整真实证书和全部准确候选字节：

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_cap_open_curvature_ports_v2.py \
  --out /tmp/R133-open-curvature-ports.json.gz

PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_cap_M128_inner_trace.py \
  --out /tmp/R133-M128-inner-trace.json.gz
```

完整报告为 `notes/2026-11-13-R133-open-curvature-ports-r1-v2-native.json.gz`
和 `notes/2026-11-13-R133-M128-actual-inner-cap-trace-native.json.gz`。
它们保存逐输入列、全部 exact dyadic 差、所有 mean、完整 SHA、真实失败范围和独立范围旗标。
初版开放图的 source/report 原样归档；最终使用内侧解析半径的 v2。

接入真实 regular 尾时，仍须使用实际高度/flux、normal/shear 和 mean 转换，
并解真正 $F(a,f_*)=0$。仅有 (O.21) 或曲率小量不支付 tail 的相对标签强范数。
本篇为这次联立提供一个已验证的开放全频曲率端口图和实测匹配残差，而没有替代尚未证明的外尾逆。
