# R254：普通中心的真实 T2 支撑及完整主函数范数

日期：2026-11-13。

**状态：本篇范围内已证明并完成首个普通中心 `ORD_j05` 的全部实际计算。** 已构造完整三次除子 $T_2P$ 的原 73 坐标、原 $V_2,V_3$ 评价及全部三条实际二同源。R252 的完整实际函数 $\Phi_C$ 在此除子的范数为

$$
 \boxed{\operatorname{Norm}_{T_2P}\Phi_C=2216148,\qquad
 \log_{47}\operatorname{Norm}_{T_2P}\Phi_C=2233158
 \pmod{47^4}.}
\tag{254.1}
$$

这里 $P$ 是真正普通盘中心，$C=P-b$，$\operatorname{div}\Phi_C=mC-A_1(t)$。没有以一个全纯 Hecke 矩阵代替实际移动支撑或主函数。本文不把这一个范数因子称为全部 $\sigma_{F_2,b}$ 高度。

## 1. 原半域中的全部实际二核

R231 给该中心的实际短模型

$$ E:y^2=x^3+2x+17 $$

及原未分歧 840 次半域 $K$ 中的 41 挠点。点以 $(x,b_y)$ 表示实际 $(x,y_0b_y)$，$y_0^2=f$；$P_{41},Q_{41}$ 及 $f$ 全部从已保存真实值读取，不重新选择项链或 Weil 根。

二阶核的 $x$ 多项式为

$$ h(r)=r^3+2r+17.\tag{254.2} $$

它模 47 不可约且可分，因而在 $K$ 中有三个根。程序实际求出全部三个剩余根，选择确定的字典序根，再通过两次单位 Newton 迭代升至 $47^4$。所得 $r$ 满足 $h(r)=0$、$\sigma^3r=r$、$\sigma r\ne r$，三共轭根之和为零；未扩张到新的更大挠点域。

置 $u=3r^2+2$。实际规范 Vélu 映射为

$$
 \phi(x,y)=\left(x+\frac{u}{x-r},
                  y\left(1-\frac{u}{(x-r)^2}\right)\right).
\tag{254.3}
$$

其目标曲线在完整三次代数中的系数为

$$ A'=-8-15r^2,\qquad B'=374+28r.\tag{254.4} $$

程序实际把原两个 41 挠点代入 (254.3)，检查目标曲线方程、两个点的 41 倍均为零及 Weil 配对

$$ e_{41}(\phi P_{41},\phi Q_{41})=\zeta^2.\tag{254.5} $$

保存的始终是原 $\phi P_{41},\phi Q_{41}$，其水平矩阵行列式为 2。没有把第二点偷偷乘 $2^{-1}$ 后仍使用旧项链编号。源项链及完整 $gH$ 代表原样通过二同源运输。

三次不可约核的三个根恰对应全部三个二子群，故该代数描述完整 $T_2P$，没有只取得其中一条分支。

## 2. 准确迹尺度及原 73 坐标

对目标曲线，重新通过实际群律、批量单位斜率和原定义计算全部 1,681 个 weight-one 值，然后按 R102 的原 73 个 basis pairs 和真实项链计算乘积。设其半域元素为 $S$；它已包括原 $y_0^2=f$ 与目标 Weil 根 $\zeta^2$。因为 2 在 $\mathbf F_{41}$ 中为平方，Gauss 二次朝向保持 R231 的原 $i$，没有额外改变二次系数基。

全部 73 个 $S$ 均实际满足 $\sigma^{120}S=S$。目标坐标属于

$$ R_6=R_2[r]/(r^3+2r+17),\qquad R_2=(\mathbf Z/47^4)[i]/(i^2+1). $$

其相对迹定义是

$$ A_S=\operatorname{Tr}_{R_{120}/R_6}S
       =\sum_{j=0}^{19}\sigma^{6j}S.\tag{254.6} $$

为避免对每个基值重复长相对迹，使用三次迹对偶。一般将 (254.2) 写作 $r^3+Ar+B$，其基 $1,r,r^2$ 的迹 Gram 矩阵为

$$
 G=\begin{pmatrix}
 3&0&-2A\\
 0&-2A&-3B\\
 -2A&-3B&2A^2
 \end{pmatrix}.
\tag{254.7}
$$

判别式为单位，程序实际求并核验 $G^{-1}$。若

$$ A_S=\sum_{k=0}^2(a_k+i b_k)r^k, $$

则完整原 840 次半域迹给

$$
 G(a_k)_k=\frac{60}{840}
   \bigl(\operatorname{Tr}_K(r^jS)\bigr)_{j=0}^2,
 \qquad
 G(b_k)_k=-\frac{60}{840}
   \bigl(\operatorname{Tr}_K(i r^jS)\bigr)_{j=0}^2.
\tag{254.8}
$$

准确系数是 $60/k$，不是直接沿用普通有理中心的 $20/k$：先从 $K$ 取到六次域的相对迹需 $120/k$，再取实部或虚部各需 $1/2$。两个迹塔和基 $1,r,r^2$ 的 Gram 矩阵给 (254.8)，没有拟合尺度。

本次另对第一基值独立执行 (254.6) 的全部二十项，将完整半域坐标与 (254.8) 恢复的元素逐项比较，完全一致。随后按原 `basis_inverse` 转回 73 个原坐标。

## 3. 完整曲线与 Hecke 规范检查

取得三次代数中的 $W$ 后，在同一原乘法模型上重建 $V_2,V_3$。对全部 $73\cdot74/2=2701$ 个二次积，程序检查

$$ W_iW_j=V_2c_{ij}\quad\text{在完整 }R_6\text{ 中}.\tag{254.9} $$

每个 $c_{ij}$ 都先在原 820 行上检查为真实乘法系数。所有三次基系数的半线性下降也通过；特别，任意原 Frobenius 固定截面在目标代数中落于实三次子代数。

令 $K_1$ 为原 54 维全纯基嵌入，$M_2$ 为 R131 的真实全纯 Hecke 矩阵。实际三分支迹是

$$ \operatorname{Tr}_3W=3W_0-2A W_2. $$

程序独立核验全部 54 项

$$
 \boxed{\frac12\operatorname{Tr}_3(WK_1)
       =W(P)K_1M_2\pmod{47^4}.}
\tag{254.10}
$$

这里 $1/2$ 是 R123/R218 的实际微分拉回尺度，与保存原 Vélu 目标的规范一致。原 raw 配对、迹 Gram、二十项相对迹、全曲线乘法和 (254.10) 一起约束目标点、项链和尺度，没有把检查的等式本身当作待定目标的定义。

完整支撑证书保存全部 $W,V_2$ 三次系数、原半域中的核与两目标挠点、真实源项链、目标模型、两侧 Hecke 迹和所有输入 SHA。

## 4. 完整实际主函数在移动支撑的范数

使用 R252 的同一函数 $\Phi_C$。将其原 455 个主截面、$f_b,f_0,v_1,F_{\rm end},G_{\rm end}$ 全部在真实 $R_6$ 坐标上评价。每个 Frobenius 固定截面的虚部系数准确为零，故数值位于

$$ R_3=(\mathbf Z/47^4)[r]/(r^3+2r+17). $$

每个值的完整三次乘法矩阵行列式都是 47 进单位。因而这里确实可以只逆单位；这是对全部实际因子的检查，而不是从最终函数无极点推断所有中间因子也为单位。

程序按完整正向 DAG 计算 $f_v$：

$$ f_{\rm init}=f_b/f_0,\qquad
 f_v=(F_v/f_0^{d_v})\Big/\prod_{p\to v}f_p.\tag{254.11} $$

继而计算真正终点

$$ \Phi_C=f_Y^{-1}(v_1/f_0)(F_{\rm end}/G_{\rm end}).\tag{254.12} $$

所有逆使用实际三次乘法矩阵的伴随矩阵，并逐项核积为 1。由所得 $\Phi_C$ 的真实三次值取行列式范数，得到 (254.1)。另按 R252 的全部任意精度整数指数，直接乘各个截面的标量范数和初始、终点规范因子；两种范数逐项一致。没有在指数中只保留模 47 的部分。

最后对单位范数用

$$ \log_{47}u=(46)^{-1}\log(u^{46}) $$

的三项整展开得到 2233158。这里未对非单位作未经证明的除 47，也没有在移动支撑上使用一个仅由类坐标推测的范数。

## 5. 接完整 F2 截面的边界

采用 R175 同一 $K_{g_1}$ 代表，普通一般点需要的实际第二除子是

$$
 D_{F_2}(P)=27T_2P+81P_{-12}-27Z_{-8}-54P_{-7}
             +4P+4b+4K_{g_1}.
\tag{254.13}
$$

本篇已经完成其中真正移动支撑 $T_2P$ 的完整输入和范数，故其对 $\log\Phi_C[D_{F_2}(P)]$ 的贡献为 $27\cdot2233158$。固定 CM 支撑、完整典范 106 次除子以及 $P,b$ 的真实切向首项继续计算。还必须保留 R148 的规范纤维坐标、实际第二变量到原 Abel 族的函数运输和相应形式 Poincaré 值；不能把 (254.1) 自身误称为完整 QC 局部高度。

同样，R240/R242 目前已给的 $T_3\nu$ exact 修正不允许直接令 $g_{T_2C}=M_2g_C$。若使用梯度路线，需要真实 $T_2$ 运输项；若使用 R184 路线，需要实际小族 $T_2$ 短链。这个缺项没有因本篇的移动支撑完成而被省略。

## 6. 文件与复现

源码为 `p41_ordinary_t2_support47.py` 和 `p41_ordinary_t2_principal_norm47.py`。支撑证书 `ORD_j05_actual_T2_support47.json.gz` 的 SHA 为 `927f099a42d7262ac934f01ca3ef3683204a0fd0c9b43be40c56433e662c9899`；完整范数证书 `ORD_j05_actual_T2_principal_norm47.json.gz` 的 SHA 为 `372cfcc07b3de42c4b5be71da1e8b36ed89ba73ac30b53a6ac4125c14f4ddaa4`。完整五项交付见 `R254-handoff-manifest.json`。

第一程序使用 R231 相同的 FLINT 半域引擎，完成原三次核与 73 坐标约用 117 秒；第二程序只需现有原矩阵和小三次代数，不再做 Jacobian 群运算或大域挠点计算。复现命令为：

```bash
OPENBLAS_NUM_THREADS=1 python -B scripts/p41_ordinary_t2_support47.py \
  --script-dir scripts --ordinary-lifts scripts/data/p41_ordinary_point_lifts47.json.gz \
  --j 5 --output ORD_j05_actual_T2_support47.json.gz
OPENBLAS_NUM_THREADS=1 python -B scripts/p41_ordinary_t2_principal_norm47.py \
  --script-dir scripts --support ORD_j05_actual_T2_support47.json.gz \
  --principal-expression scripts/data/ORD_j05_actual_principal_function47.json.gz \
  --transport-directory ordinary-principal-transports/ORD_j05 \
  --output ORD_j05_actual_T2_principal_norm47.json.gz
```

主函数目录由 R248 已发布的完整包解出。数据保留全部 455 个截面的实际三次值与范数、所有固定因子、最终实际函数值、完整 $V_3$ 三次系数及输入 SHA，未把原函数替换为无法再评价的日志摘要。
