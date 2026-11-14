# R150：197 个真实第三方向全完成与自然整数图的九目标模 p6 排除

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-14。状态：实际完整相关第三计算已完成；由来源覆盖和已存原余量推出的否定结论。没有计算或声称特征零原理想身份。

## 1. 主结论与准确来源范围

令 $p=31$，$D=\mathbb Z_{(31)}$，$E=D[s]^{6188}$，$V=D[s]^{4367}$。$A:E\to V$ 始终是原 primitive 十七式矩阵，保持全部原来源、输出和行缩放。采用已保存的九个实际原整数代表
\[
b_i=A\kappa_i/p^{e_i},\qquad
(e_1,\ldots,e_9)=(1,1,2,2,2,2,2,3,4).
\]
设
\[
H_{\rm nat}=p^2E+p\kappa_1D[s]+p\kappa_2D[s]
+\sum_{i=3}^9\kappa_iD[s].
\tag{1.1}
\]

**定理。** 对每个原目标 $j=2,\ldots,10$，不存在 $X\in H_{\rm nat}$ 满足
\[
AX=p^2h_0t_j\pmod {p^6}.
\tag{1.2}
\]
多项式系数的次数任意；不限制为当前标准来源、当前模 p 初值、有限费用或只作一个 p 进位修正。

这个结论完整覆盖 (1.1) 的自然整数图，仍不把 (1.1) 等同于全部原可行来源。全部原可行来源属于
\[
S_2=\{x\in E:Ax\in p^2V\};
\]
$S_2/H_{\rm nat}$ 的新来源另由原饱和接口处理。特别地，定理没有排除带 31 分母的有理来源，也没有给出 R150 的特征零闭合。

## 2. 实际运行与保存证据

唯一新任务为 Actions run 43653360404 / job 132626469223，数学源码提交
4ee8d886cd88893411c91e6ef0b685a87f3e44f6。实际输出已经保存：

- [主回执](r150-197-third-actions-789f/43653360404-1/197-third-local-jet-pipeline-receipt.json)；
- [Actions 成功定义与目标分区](r150-197-third-actions-789f/43653360404-1/actions-outcome.json)；
- [实际生成流清单](r150-197-third-actions-789f/43653360404-1/certificate-manifest.json)；
- [完整恢复清单](r150-197-third-actions-789f/43653360404-1/recovery-manifest.json)。

十次有界编译、输入 SHA、Python AST 以及全部数学阶段均在该 run 实际执行。共享数学耗时为 77.863068274 秒。状态为 completed，outcome 为 complete-relevant-low-initial-third-obstruction；九个 individualTargetCompatible 全为 false。

关键实绩为：

| 项目 | 实际结果 |
|---|---:|
| 新原高核方向 | $K_2,\ldots,K_{198}$，共 197 列 |
| 原 G 完整十项乘回坐标数 | 2,036,980 |
| 原 q1 / q2 来源 | 全 6188 行，真实前基与图 DAG |
| 每列局部信息 | 143 坐标，104 自由条件全部保留 |
| root2 原 torsion / 真 V10 主部分 | 32 / 8 |
| 相关商维数 | 24 |
| 197 列在相关商中的完整多项式像秩 | **0** |
| Krylov 最大已构造幂 | 1；394 列即确认闭包 |
| 九个正目标 | 0 |
| 实际恢复文件 | 135 个，共 188,295,295 原字节 |
| 原生成二进制流 | 91 个，逐 SHA 保全 |

最终完整系统的未压缩字节数为 467485，SHA256
3ad7520e9e6b272fb69fa22517baf6d88ddfc7207df51437ba3af76618af8204；
gzip 字节数为 61947，SHA256
d62a5e1705d0cbc0ce0544e65ff47f2c1c76208e5843de0ab9d812e7aebd9796。
原数组、原除式、所有 cochain 和实际恢复点均在清单中，不以日志进度替代真实数据。

全局第三像、全部原整数格和特征零身份的三个标志始终为 false。因为本次没有正目标，正来源验证标志也明确为 false，未用空集全称真冒称原式成功。

## 3. 真 V10 与一个共同 dual

此前五个关系的真第三列张成的扩张为
\[
V_{10}=U_9+\mathbf F_{31}d_{9305},\qquad
d_{9305}=A H_{5,9305}/p^5.
\]
其中真原来源 $H_{5,9305}$ 的成本为 87。该等式和不变性已由[真十维不变空间稿](2026-11-14-r150-five-third-true-ten-dimensional-invariant-space-and-three-target-quotient-789f.md)支付；本轮再次从同一 315 数据准确运输到真源基。实际得到
\[
d_{9305}-P_2d_{9305}
=15b_1+10b_2+25b_6.
\tag{3.1}
\]
因此这里没有把 projected 第十基与 actual 第十基混用。

记原当前余量
\[
\rho_j=(p^2h_0t_j-AX_j)/p^5\bmod p.
\]
真 $V_{10}$ 商中的九个余量仍张成三维半单 $s=2$ 空间。新 197 列的投影全部在 $V_{10}$ 中；“相关像秩零”不表示未投影原第三列为零。

完整回执保存九条 315 坐标的复合投影 dual。它们逐坐标正好是第一条 $\lambda=\lambda_2$ 的倍数，倍数依原目标顺序为
\[
(1,11,15,8,23,24,19,17,27).
\]
每条已保存的归一化 dual 在自身目标上的值为 1，故同一 $\lambda$ 满足
\[
\bigl(\lambda(\rho_2),\ldots,\lambda(\rho_{10})\bigr)
=(1,17,29,4,27,22,18,11,23),
\tag{3.2}
\]
九值全非零。

这个整理只逐坐标比较了已存九条 dual 的有限域标量关系，没有重跑任何原来源或新矩阵。完整 315 权重及倍数另存
[共同 dual](2026-11-14-r150-197-third-common-dual-789f.json)。该 $\lambda$ 为真实 $P_2$ 后接真商 dual，已经核
\[
\lambda(V_{10})=0,\qquad
\lambda\bigl(f(J)P_2d_j\bigr)=0
\quad(j=2,\ldots,198,\ f\in\mathbf F_{31}[s]).
\tag{3.3}
\]
最后的任意多项式量词由实际像不变性与 $(s-2)^5$ 湮灭身份支付，不是有限采样推断。

## 4. 为什么这次计算付清全部自然图低初值

令
\[
F=F_9=[A,b_1,\ldots,b_9],\qquad
T(x,c)=x+\sum_i p^{-e_i}\kappa_i c_i.
\]
原整数格精确为
\[
\Lambda=E\oplus D[s]^7\oplus pD[s]e_8\oplus p^2D[s]e_9,
\qquad p^2T\Lambda=H_{\rm nat}.
\tag{4.1}
\]
这来自原自由来源中 $\bar\kappa_8,\bar\kappa_9$ 的真实独立性，详见[原整数格稿](2026-11-14-r150-original-p2-integer-source-lattice-and-eighth-second-direction-789f.md)。

设 $\mathcal E_0=E\oplus D[s]^7$、$\mathcal E_1=E\oplus D[s]^8$、$\mathcal E_2=E\oplus D[s]^9$。允许改变任意原始模 p 初值时，差向量的三位进入核依次为
\[
K_0=\ker\bar A+\langle\eta_1,\ldots,\eta_7\rangle,\quad
K_1=K_0+\langle\eta_8\rangle,\quad
K_2=K_1+\langle\eta_9\rangle.
\tag{4.2}
\]
$\eta_8$ 不得提前进入第零位，$\eta_9$ 不得提前进入第一位。

[完整低初值第三归约](2026-11-14-r150-low-initial-integer-lattice-third-layer-and-five-relations-789f.md)已证明：

1. 原 1834 个完整核来源包含 1632 个真整数 syzygy，以及 202 个高核；前者相关第三像为零。
2. 最后四个高核由已经存在的真除列给出精确扩增核提升；它们不产生新的本层第三像。
3. $\eta_3$ 及 $\eta_4-18\eta_3$ 在 $\Lambda$ 内有保 canonical carry 的精确 F 核提升。因此关系部分只剩已经完成的五列 $\eta_1,\eta_2,\eta_5,\eta_6,\eta_7$。
4. $\kappa_7/22$ 的原来源身份给出 $K_1$ 的精确图核消去，原高核只剩本次 $K_2,\ldots,K_{198}$。
5. 高一位差的相关第二像 $\beta_{2,F}(K_1)$ 已支付为零；再下一位完整第一像 $\beta_{1,F}(K_2)$ 已支付为零。它们不能由“第二像小维数”或仅固定初值计算代替。

因此本次 197 列与旧五列，确实生成原自然图的完整相关第三必要像。这里是来源模的生成证明，不能把这句话替换成某个观测像的维数比较。

## 5. 同一整数 lift、双倍 jet 与真正相关第三类

本轮未只读取旧第二坐标。每列原 $\widehat K_j$ 保同一规范 s 系数代表，q1 则保旧 all198 原乘积采用的规范 t 系数代表，$t=s-2$。旧 2195 源、旧完整 6188 来源和原 4367 输出的前五项都与新十项延伸逐项相符。

实际先算
\[
R_{2,j}=\frac{A(\widehat K_j-p\widehat q_{1,j})}{p^2}
\pmod {p^2},
\]
再在原整数十项中减去同一个真七除列的常数组合。573 个真实常列剥离后，$461\times448$ 系统经单位 Schur 递归求出完整十项 q2，13 个自由行始终保留；完整原 G 的全部十项已经实际乘回。q2 再经原 V、预基 cochain 和原 DAG 还原到 6188 来源，原 4367 输出的十项恒等式也实际核过。

第三除式先在整数 t 表示中截取前五项再除 p。非零 Smith 指数至多 5 以及完整十项来源身份，按[双倍 jet 引理](2026-11-14-r150-third-bockstein-double-jet-smith-loss-and-local-source-789f.md)保证其类正好是需要的相关第三类。改变 q1 的整数 lift 时要同步运输 q2；改变第一校正的模 p 来源时，差由已付相关 $\beta_{2,F}$ 消去，而非只用 $\beta_{1,F}=0$。

root1 的三个零项明确表示 root2 的 CRT 投影。局部 104 自由条件全零，并将 39 torsion 坐标准确提回全 315 的 32 维 root2 空间，才作真 V10 商。本次没有把形式可除、局部相容或纯坐标恒等式当作原来源。

## 6. 定理的证明

假设某个 $j$ 存在 (1.2) 的 $X\in H_{\rm nat}$。由 (4.1)，可取 $y\in\Lambda$ 使 $X=p^2Ty$。已存当前 $X_j$ 也有同一自然图中的实际来源 $y_j$。因为 $V$ 无 p 扭元，原两条身份给出
\[
F(y-y_j)=p^3\rho_j\pmod {p^4}.
\tag{6.1}
\]

把 $y-y_j$ 按 (4.2) 的三个进入层展开。第零位初值在 $K_0$；若它在整个全局第二页不允许提升，则本来不可能产生 (6.1)。对于确实能产生 (6.1) 的初值，将其投到 root2 后，第三类属于 §4 已完整生成的第三像。第一个提升选择所引入的 $\beta_{2,F}(K_1)$ 与第二个提升选择所引入的 $\beta_{1,F}(K_2)$ 都在该相关商中为零。

因此 (6.1) 的必要条件为
\[
P_2\rho_j\in
V_{10}+R\langle P_2d_2,\ldots,P_2d_{198}\rangle,
\qquad R=\mathbf F_{31}[s].
\tag{6.2}
\]
本轮完整相关像秩为零，所以 (6.2) 右端就是 $V_{10}$。应用 §3 的共同 dual 得 $\lambda(\rho_j)=0$，与 (3.2) 矛盾。每个 j 都如此，定理得证。

由于整个论证使用完整 R 来源模与真实多项式像，增加参数次数、换原标准补空间、换当前自然图的模 p 初值，都不能挽救 (1.2)。这个量词强于此前只保持当前初值的排除；也严格止于 (1.1) 的图像。

## 7. 下一真正原来源接口

现在应扩大原来源，不再重复自然图的同一个进位。令
\[
S_2=\{x:Ax\in p^2V\}.
\]
对旧第一像为零的真实高核，取任一已经保原来源的 q1，构造
\[
\widetilde\kappa_j=\widehat K_j-p\widehat q_{1,j},
\qquad A\widetilde\kappa_j\in p^2V.
\tag{7.1}
\]
本轮实际计算支付的是 $p^2\widetilde\kappa_j$ 进一步消去后的第三类；(7.1) 本身未乘 $p^2$，进入原来源的层次不同。它不能因本轮相关像为零就被删除。

原[二次饱和来源稿](2026-11-14-r150-original-p2-source-saturation-and-finite-column-envelope-789f.md)给出完整 S2 生成和有限 p6 来源商。其进一步的 197 原源缩减使用旧完整第一核基、四个实际第二来源及 $\kappa_7$ 的真源初值，单独证明；不从本轮的 rank0 倒推覆盖。正向工作将复用本次 q1 十项、R2 模 961 十项、七真除列和原 DAG，仅给真正新增的原来源或更高 carry 付费用。

本定理完成了原自然图的这一整层否定；原特征零理想包含与整个不变子空间问题仍未闭合。
