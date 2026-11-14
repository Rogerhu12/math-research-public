# R759 原完整整数周期格及实际映射次数证书

日期：2026-11-14。状态：**精确计算完成**。全部新算术来自公开仓库的 [Actions run 43625474728](https://github.com/Rogerhu12/math-research-public/actions/runs/43625474728)，没有本地数学运行。

## 1. 结论与准确范围

沿用 R735 的原正目标 \(C/L:y^2=x^3+b\)、R738 的原源 \(X_1\)、原 \(c_0,c_1\) 及 800 个整数闭链，R745 的六个原 Hodge 微分和 R751 的原绝对周期标度。R754 已得到完整六维 \(K=\mathbf Q(\zeta)\) 有理 Hom 空间。此次在该同一空间内完成：

1. 全部 1600 个有理周期坐标条件的整数饱和，得到完整秩 12 的 \(\mathbf Z\) 格、秩 6 的 \(\mathcal O_K\) 格；
2. 原交配矩阵上的准确求解、正定整数次数形式及完整 \(\zeta\) 作用；
3. 有理数精确 LLL 及其全部不等式核验；
4. 十二个实际整数周期微分在原六 Hodge 基中的完整 \(L\) 坐标、全部 800 闭链整数周期及实际次数。

按实际输出顺序，十二个 LLL 基向量的映射次数为
\[
(1485,1602,2448,1521,1206,1836,1206,1485,1521,1485,1206,1206).
\tag{759.1}
\]
确定选择零起始编号 4，其次数是
\[
\boxed{d=1206.}
\tag{759.2}
\]
这是十二个已给基向量中的最小值，**不声称整个格的全局最小映射次数**。每个向量给从原 \(c_0\) 积分的实际代数映射；此次没有计算其有理函数表达式、原 \(\beta\) 坐标或高度。

## 2. 完整格为什么不是分别清分母的子格

详细预运行证明见[原方法](../notes/R759-original-integral-period-lattice-and-map-degree-method.md)。这里把方法与此次真实产物连接。

R754 的六个 \(K\) 基记为 \(h_\ell\)，原闭链周期写成
\[
\frac{R_C}{\Omega_0}\int_{\gamma_i}h_\ell
 =a_{i\ell}+b_{i\ell}\zeta,\qquad a_{i\ell},b_{i\ell}\in\mathbf Q.
\]
按照 \(h_0,\ldots,h_5,\zeta h_0,\ldots,\zeta h_5\) 的列序，原第 \(i\) 条闭链贡献两行
\[
P_{2i,*}=(a_{i,*},-b_{i,*}),\qquad
P_{2i+1,*}=(b_{i,*},a_{i,*}-b_{i,*}).
\tag{759.3}
\]
令 \(D\) 清除 \(P\) 的全部分母，\(H\) 为 \(DP\) 全部行生成的格的非零行 Hermite 基。此次真实处理所有 1600 行，分块保留并准确验证每个整系数幺模变换、双向行格相等和最终秩 12。因此
\[
\mathcal S=\{v:Pv\in\mathbf Z^{1600}\}
 =D H^{-1}\mathbf Z^{12}.
\tag{759.4}
\]
这里 \(H\) 存行泛函，基向量是 \(DH^{-1}\) 的列，不加转置。实际输出逐项检查 \(P D H^{-1}\) 为整数。

初始 \(\zeta\) 矩阵为
\[
J_0=\begin{pmatrix}0&-I\\I&-I\end{pmatrix}.
\]
以实际格基共轭后，矩阵仍整且满足 \(J^2+J+I=0\)。这证明完整 \(\mathcal O_K\) 稳定性。由原整数周期积分、原微分和 \(c_0\mapsto O\) 的唯一性，所有这些映射均下降到原 \(L\)。这描述原正有理 Hom 空间内的完整 \(\operatorname{Hom}_L(J_{X_1},C)\) 格；未把它等同于原商 \(A_{\theta,1}\) 上未经证明的整同源饱和。

## 3. 原交配、次数正号及实际 LLL

R759 方法通过原模图与 Manin 横截链的对偶关系证明，R738 保存的
\(\Omega_{ij}\) 是本次 \(\gamma_i\) 的同调交配矩阵。原微分的两个周期列为 \(a,b\)，坐标序为 \(1,\zeta\)、\(\operatorname{Im}\zeta>0\)，故
\[
\deg f=-a^t\Omega^{-1}b.
\tag{759.5}
\]
原正向椭圆基上的恒等映射给正号；不取绝对值补正号。

此次只对已存 \(\Omega\) 解十二个右端并精确代回，没有重造拓扑或完整逆矩阵。设完整格的两个周期矩阵为 \(A,B_1\)，求
\[
\Omega Y=B_1,\qquad C_0=-A^tY,\qquad S=C_0+C_0^t.
\]
实际验证 \(Y\) 整、\(S\) 对称整且对角偶，准确 \(LDL^t\) 分解全部正，并验证 \(J^tSJ=S\)。由此每个整列 \(n\) 的次数恰为 \(n^tSn/2\)。

LLL 使用 \(\delta=3/4\)、全部有理 Gram–Schmidt 和整幺模行操作。实际证书验证基变换行列式 \(\pm1\)、Gram 共轭关系、每个 size-reduction 与 Lovász 不等式。若该变换为 \(U\)，新的微分列基是 \(DH^{-1}U^t\)，新 Gram 是 \(USU^t\)。应用到原六 \(L\) 微分向量时完整保留原 \(b\) 域、有理分母、原 \(\alpha s\) 与一次 \(\zeta^2\) 运输，得到 (759.1)。

## 4. 真实运行与全部来源绑定

| 项目 | 实际记录 |
|---|---|
| 仓库 | Rogerhu12/math-research-public |
| run / attempt | 43625474728 / 1 |
| source commit | 4728e6868e2509556e5c60e138fd97c9b4120d8e |
| 核心源 SHA-256 | 17403f45f74e03e5a138376068e64e54c9bf6b2622a7b91bb178747d407708e0 |
| 方法 SHA-256 | fe08b7f1b994984b61c08bfb68147383556b68d6b7b11bca4a22b91eec6c4c66 |
| 正式 request SHA-256 | bec5f5a0da04cfe153a57330092e783bf9e8008f08b498ddd88c85eafe590dc2 |
| 核心时间 | 8.629164621000001 秒 |
| wrapper 完成时刻 | 2026-11-14T18:14:47.767369+00:00 |
| Python-FLINT | 0.9.0 |
| 最终证书 SHA-256 | 7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0 |

准确复用的三份数学输入为：

| 输入 | SHA-256 |
|---|---|
| R754 最终证书 | da4ef0eeac285da5cf32ad1372155dbb9d03917c18044b81b8236fac6e51107c |
| 同次 R754 全部已验证闭链周期 | fc300cb79a3299bb896ce6ae5a1ec577248750692202d1993c27a69d3886672b |
| R738 原整数闭链及交配 | d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf |

R754 输入必须来自成功 run 43620862489，核心源 SHA
f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251。
完整输入 receipt 核实际 run/source/manifest，核心核原证书内阶段 SHA 与相同规范。原模型、拓扑、有限表示、周期与 Hom 核均未重算。

## 5. 完整产物与复用检查点

[小证书、receipt 和 manifest 目录](../computations/R759-original-integral-period-lattice-and-map-degrees/43625474728-1/)已在公开仓库。核心 receipt SHA 为
119beb1ee381250e4820735a42467c52e9f101d74470ef989f20d1738217682e；
run receipt SHA 为
5a2f78e06e59e9cb7904048ae49fcff13bb6df3e9ae7dc78b515bad80a8a3225。

完整 artifact 名
serre-global-R759-original-integral-period-lattice-and-map-degrees-43625474728-1，
ID 14125233728，ZIP 568524 字节，ZIP SHA-256
2ae069c394c7038f10743c7d9c7981b509579780bca3d0c69772419e3836b883。
完整 manifest SHA 为
fb61ded80deb7f6904de7e0aa2e7a3f3b161a0ecd2f5f0c329e96935c4e9f1aa。

| artifact 内文件 | 字节 | SHA-256 |
|---|---:|---|
| R759-complete-period-row-HNF.json.gz | 182123 | 2056829ee12406e292cfbacb4e86de18eb0efdfabee9c3daba5703d7fa54e6d6 |
| R759-saturated-integral-period-lattice.json.gz | 149793 | 17bb7bf3ed0891492f53c404e17f426ce5334f2997291513d9332138e33c1fcf |
| R759-original-map-degree-form.json.gz | 76172 | 1ab2dd846d36c586ebc0a3e3142d9ae437f8e2088d67e597b8fddbd5738b19af |
| R759-exact-degree-LLL.json.gz | 3707 | 5a1b6d44694389ac3fe48686a00c1745976726fefd8ff5196e2f60d4ef063825 |
| R759-original-integral-maps-and-bounded-recovery-input.json.gz | 148620 | 037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc |

后继任务直接读取已完成的最后一份微分/次数数据及相应证书，无需重跑 HNF、degree solve 或 LLL。全部可重建矩阵只保 artifact，源、参数、小证书及 SHA 保 Git。

## 6. 后继的有限输入及尚未完成的工作

此次原源 \(g=400\)、\(\deg a=820\)。实际 \(d=1206\) 在原 R759 方法给
\[
m=4,\quad D=4(a)_0,\quad M_0=5692,
\quad\text{RR 基至 }q^{8104},\quad h/dq\text{ 至 }q^{9310}.
\tag{759.6}
\]
这些是已生成的有限恢复输入，不是已经生成的函数。

[R762](R762-original-mu3-quotient-and-single-function-map-recovery.md)
进一步使用原 \(\mu_3\) 商和十九条既有树边，把实际尖点像与 \(c_0\) 平移变成精确 \(K\) 周期和次数模 3 的有限计算。R764 直接消耗本次十二个原微分及实际次数；随后仍须原商的 RR 基、实际单函数、原 \(c_1\) 的 \(\beta\)、Poincaré 规范与真正高度。这些数据和全 \(p\) 排除尚未完成，主目标保持 OPEN。

依据：[R754 实际周期证书](R754-certified-original-p41-periods-and-Hom-kernel.md)、[R759 完整预运行方法](../notes/R759-original-integral-period-lattice-and-map-degree-method.md)、原 R732/R735/R738/R745/R751 证明，以及以上同源绑定的公开真实输出。
