# R1120：原 full47 四个基本 CM 类的完整带符号坐标

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：已证明，新的公开精确计算全部成功。**
在原 $X_{\rm ns}^+(47)$、辅助素数 $q=4513$ 及原
$\mathcal T/q=\mathbf F_q[H]/P_H$（$H=T_3+T_5$）中，
四个基本 CM 类
$$
u_D=23y_D-C_\infty,\qquad D=-4,-3,-7,-8
$$
相对原 $u_{-4}$ 及原 QC 生成元 $B_qu_{-4}$ 的全部73维坐标均已读出。
这里 $B_q=q+1-T_q$，实际点、符号、粗模重数及 Hecke 嵌入
全部使用 [R1119](R1119-original-signed-CM-coordinates-and-Jacobi-reading.md) 的同一来源。

本结果完成的是指定模4513坐标，不宣称已经计算完整特征零有理坐标，
也不单独宣称第三类值、QC 行秩或八盘唯一。

## 1. 真实执行与复核

- source：[a0eec1a3566503cfec9b5cf7e50601fd3ac0e530](https://github.com/Rogerhu12/math-research-public/commit/a0eec1a3566503cfec9b5cf7e50601fd3ac0e530)。
- [run45994488204](https://github.com/Rogerhu12/math-research-public/actions/runs/45994488204)，
  [job140490328323](https://github.com/Rogerhu12/math-research-public/actions/runs/45994488204/job/140490328323)，attempt1，
  checkout、固定镜像、数学步骤与整个 job 全部 success。
- 新数学总耗时 **21.546368293 秒**；声明预算1800秒、reserve60。
- 固定 SageMath10.6 官方镜像；实际 PARI 版本为 **2.17.1**，
  不是把 R89 的2.19.0版本号沿用过来。
- root/o2 提交前全文纸审；root 读取完整 job log，
  核请求/source、一条完整 receipt、四个完整 case、
  每个坐标向量 hash、全部记录 canonical hash 与证书 canonical hash。

仅首辅助 $(\Delta_0,r_0)=(-11,2027)$ 即达到完整秩73，
故请求中的后续辅助没有执行。
没有重跑层41、原 CM 高矩、全局高度或旧点标签图。

## 2. 实际原空间与完整参考

原 star $+$ 相对空间维189，实际 new157、new Fricke $+$ 维73；
生成路径共 **377** 条，全部为自由路径，无遗漏椭圆零路径。
四个整数功能先在 $\mathbf Q$ 上满足全部 $Ew=j$，
再经分母单位的实际投影进入原 new+ 空间。

第一个 separator 就是原 $H=T_3+T_5$；
完整 new/complement 特征因子在模4513互素，
补空间维116，$[P\ Q]$ 满秩189。
全部 $\pi P=I$ 与三个 Hecke 交换矩阵关系均通过。

Gaussian 参考的真实 Krylov 矩阵
$$
K=[v_{-4N,0},Hv_{-4N,0},\ldots,H^{72}v_{-4N,0}]
$$
满足
$$
\boxed{\operatorname{rank}K=73,\qquad \det K=4364\in\mathbf F_{4513}^{\times}.}
$$
实际 pivot 行为0至72。
因此这一个辅助已经读取全部28个原整 Hecke 块，
没有用任意非零列补上某个缺失分量。

## 3. 四条完整带符号整数路径和

每行均完整计入 $Q$ 与 $-Q$ 两个向量；
四个实际 $r=0,N$ 都保留重合的两个指标。

| $D$ | $\Delta=DN$ | $r$ | 正 $a$ 形式数 | 双指标命中数 | 非零路径数 |
|---:|---:|---:|---:|---:|---:|
| $-4$ | $-8836$ | $0$ | 2262 | 728 | 211 |
| $-3$ | $-6627$ | $2209$ | 2812 | 902 | 211 |
| $-7$ | $-15463$ | $2209$ | 1784 | 508 | 147 |
| $-8$ | $-17672$ | $0$ | 4588 | 1482 | 219 |

全部投影列的共同 SHA-256：
1be78232aa6ca702778c0b5aa7c12711d797c4126ed3ddf81aeadea51f7141bf。

路径数组、精确相对功能、投影矩阵及中间展开均只在 runner 临时目录中；
没有将它们提交、上传 artifact 或 Release。

## 4. 实际点比例和 QC 坐标

由 R1119 的特征零几何身份及原 MW 整性，读取的准确关系是
$$
u_D=\rho_Du_{-4},\qquad
\rho_D=\frac{w_D}{2}\frac{c(DN,r_D)}{c(-4N,0)},\qquad
c_D=\rho_DB_q^{-1}.
$$
四个 $w_D$ 按本表顺序为 $2,3,1,1$。
每个 $c_D$ 均是73个升幂系数的完整向量；
公开日志的 actual_CM_Hecke_coordinate 行保留全部系数，
后继消费时须核下面的完整 hash。

| 原标签 / $D$ | $\rho_D$ 的 SHA-256 | $c_D$ 的 SHA-256 |
|---|---|---|
| 141 / $-4$ | 8af3f7d988a09ab4b20bfb548a2c8205e9a15c5427cc4ab1dc11a378be6e0fc3 | e981818389ff50c9a908e49e66dba6e2f9e8446b55b8d48450f4b2ec9de0cf3b |
| 0 / $-3$ | 6c35482f1af08b673d9998efb68e576fe84d3e90558790189b62f7c3c9817fb0 | c6c8ece5dbc5776cd573bdeb76ec56050c9eb7fea40bfef3af3504992d0bf2fe |
| 76 / $-7$ | 672e3a3206c9f153f2aa546834a9b48b2d44b5c8788f801f2df4599383bc533b | 1ef424955a207d9283c60dc8f93d627352671dbcf2ac36a51df02c158a62c884 |
| 108 / $-8$ | 915a26708b15dcf06a705e24fba428385dec15a47dbb50e64ee4ce3f7976ea47 | 8524dd439680e2469a9eedff96d63464f8373db23cb8a4e10c0e25c0e4497f10 |

特别 $\rho_{-4}=1$，而 $c_{-4}=B_q^{-1}$；
程序逐行核 $B_qc_D=\rho_D$ 和全部原参考列上的实际矩阵作用。
不能把 $\rho_D$ 直接作为 $B_qu_{-4}$ 下的坐标。

R1108 已付的实际 CM Hecke 关系继续给其它四个点：
$$
\begin{aligned}
c_{-16}&=(T_2-1)c_{-4}/2,&
c_{-12}&=T_2c_{-3}/3,\\
c_{-27}&=(T_3-1)c_{-3}/3,&
c_{-28}&=(T_2-2)c_{-7}.
\end{aligned}
$$
这些是同一原点类的关系；本篇不另重算它们，也不从有限域点约化猜首对数。

## 5. 全部 Hecke 嵌入与 $B_q$

坐标多项式 $P_H$ 与原 Hodge 来源的 SHA 完全一致；
从实际模符号读取的 $T_2,T_3,T_5$ 多项式
在原73维 Hodge row 矩阵上逐项回代全部通过。
因此实际 Hecke 嵌入没有由特征多项式的根任意排列。

原 $T_{4513}$ 仅为新的 $B_q(H)$ 嵌入所必需而重建。
它的精确整数特征多项式与 R1089 已认证的 hash 一致，
没有再次登记旧群阶结论。
新读取的 $B_q$ 全73系数 SHA 为
59610e40d29fd17586fcc9717fad28acba256e4f856b30b9b8a1218c90f44e5a，
并核其真实矩阵恒等式及原 determinant551。
这支付原 QC 生成元下的数值作用，不把“是单位”当作“等于一”。

## 6. 复现入口与完整证书

| 对象 | SHA-256 |
|---|---|
| Python consumer | a2e68973344d8e2a4dea9e403cf84c27e6076f55f629276d68264a27ec58adde |
| GP source | 79288572c0d4ca20ca806fb41eefb0b27df98876a827da631af53143df98a574 |
| request | 843c1650845f95027c49b7a352a1a6a332b07f662427eef4f8cc5f5f17afd39c |
| R1119 proof/method | 00ab2d79e6d87e9ea184bf087563f52c424c14573f9b7c0686b7f51dda950b44 |
| 四条完整记录 | b9f610583ea037e18d5e948341af5b09b78c8426a16f7643a6f44bd2949b882e |
| 完整 certificate | 4a4895f692c0eaeab0fa76eed9987af0ebaefa524d03d23fcb00425c2df45ed8 |

- [Python consumer](../scripts/full_p47_signed_Jacobi_CM_coordinates.py)；
- [GP source](../scripts/full_p47_signed_Jacobi_CM_coordinates.gp)；
- [有限请求](../notes/full-p47-signed-Jacobi-CM-coordinates-request.json)；
- [几何与算法证明 R1119](R1119-original-signed-CM-coordinates-and-Jacobi-reading.md)。

## 7. 后继与范围

四基本 CM 坐标已经完整获得。
原 q² 运行不再是 QC 的必要输入，不另启动其后续或重复基本坐标计算；
如该已启动运行随后给出完整记录，其来源仍按实际状态记录。

首4个第三类值仍由原 Miller 请求读取，
其它12例由 R1118 的短 Cartier 请求读取。
这些完成后才与原高度、切向和角作用求真正的两行 QC 矩阵。
已准备的 v2 消费者对 Jacobi 与 Cartier 来源还核原完整矩阵
$\bar T_q=1-\bar B_q(H)=C_{\rm row}$，不会只比较 determinant。

本篇没有关闭八个原4513盘的内部唯一性，
更没有达到全充分大素数 Serre 一致性的 README 完成标准。
继续原实际 QC 及一般素数的全局障碍。
